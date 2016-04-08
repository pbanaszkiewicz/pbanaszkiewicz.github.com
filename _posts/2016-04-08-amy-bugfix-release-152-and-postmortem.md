---
layout: post
title: "AMY bugfix release v1.5.2 and bug postmortem"
tags: [swcarpentry, django, release notes, postmortem]
date: 2016-04-08
---

24 hours ago, Maneesha Sane
[noticed and informed](https://github.com/swcarpentry/amy/issues/744) on GitHub
that one of the tags in AMY is missing.

This observation led to an investigation on the servers and eventually to fix
for a critical bug that caused the data loss.

But before we jump into sysadmin work…

## What is a "tag" in AMY terms?

A tag is label that we give to various workshops. For example, all Software
Carpentry workshops will have `SWC` tag, and all Data Carpentry workshops will
have `DC` tag.

There are more labels we use, and the one that went missing was `DC`.

One event can have between zero and all the tags we have in the system, which
means it's a many-to-many relationship between events and tags. This type of
relationship requires additional intermediate table in the database.

Contents from that table were missing because they were removed with removal
of the `DC` tag.

## Investigation

I started the investigation by narrowing timespan where the event, that led to
data loss, occurred.

Then I followed by reading WWW server access logs to find out what happened in
that timespan in hope I could find the bug.

After narrowing list of suspects, I was able to reproduce the bug.

Finally I retrieved the lost data from the most recent backup that still had
it.

### Ways to remove tags from AMY

There's no interface for removing tags other than Django's auto-generated admin
interface; only a couple of people have access to it.

So the data loss was either human error or it was caused by code bug. This
conclusion helped me define what I should be looking for in the WWW server log.

### Narrowing event occurence timespan

AMY's being backed-up by multiple systems; I logged into each of them and run
multiple SQL queries on different databases to find out which backup had the
`DC` tag and was the newest.

It turned out that backup from 2016-04-06 17:00 UTC-4 was the most recent still
with the `DC` tag.

In the meantime I was fighting timezone correction… Our backup systems are in
different datacenters and were running on different timezones.

### Reading access log

First thing I checked in the access log is if anyone was using the admin panel
to remove the tag. Unfortunately this possibility was quickly ruled out; so
the loss was caused by code bug.

However, after reading the log no action stood out.

Short, important side story: Software Carpentry website rebuilds every 30
minutes. Each rebuild is shown in the log by multiple requests to AMY's API:

{% highlight nginx %}
[…] GET /api/v1/export/badges.yaml => generated 69122 bytes […]
[…] GET /api/v1/export/instructors.yaml => generated 50488 bytes […]
[…] GET /api/v1/events/published.yaml?tag=SWC => generated 231344 bytes […]
[…] GET /api/v1/events/published.yaml?tag=DC => generated 17806 bytes […]
[…] GET /api/v1/events/published.yaml?tag=TTT => generated 7879 bytes […]
{% endhighlight %}

Website grabs published events tagged by `SWC`, `DC` and `TTT` tags. This
sequence of requests repeats every 30 minutes.

After reading the log over and over I noticed that two consecutive calls to
`/api/v1/events/published.yaml?tag=DC` yielded results of very different
response lengths:

{% highlight nginx %}
[…] [Wed Apr  6 15:01:11 2016] GET /api/v1/events/published.yaml?tag=DC => generated 17806 bytes […]
[... many more requests ...]
[…] [Wed Apr  6 15:30:10 2016] GET /api/v1/events/published.yaml?tag=DC => generated 261521 bytes […]
{% endhighlight %}

Apparently then the DC tag disappeared, the API started returning all the
published events, no matter if they were tagged `SWC` or something else.

This was a clear indication that the `DC` tag disappeared between 15:01 and
15:30.

That timespan doesn't look like 17:00. Timezones... programmer's nightmare.

### Suspects

There was some user activity in this 30-minutes long window and one thing
caught my eye:

{% highlight nginx %}
[…] POST /workshops/events/merge?event_a_0=2016-05-06-RDAP16-Atlanta&event_b_0=2016-05-06-asist […]
{% endhighlight %}

(The actual URL was slightly changed to remove unnecessary information.)

This was a call to event merge functionality: someone wanted to merge
workshops `2016-05-06-RDAP16-Atlanta` and `2016-05-06-asist`.

{:.message}
*Short side note*: merge functionality allows user to use more advanced
strategy for merge; one can select which properties (or fields) in the final
event should be used from event A (`2016-05-06-RDAP16-Atlanta` in our example)
and which should be from event B (`2016-05-06-asist`). Additionally in case of
event's tags it's possible to combine them from both base events.

I started testing different strategies. I had a feeling that the bug had
something to do with strategy for event tags. :)

Finally I reproduced the bug by using following strategy:

* base event: `2016-05-06-RDAP16-Atlanta` (event A)
* tags: from event B.

### Data retrieval

At that point I decided to retrieve the lost data using SQL import/export
functionality from the optimal (newest & containing the lost data) backup found
earlier.

### Bug

The only code used in event merge functionality that would trigger accidental
removal is:

{% highlight python %}
            if value == 'obj_a' and manager != related_a:
                manager.all().delete()
                manager.add(*list(related_a.all()))

            elif value == 'obj_b' and manager != related_b:
                manager.all().delete()
                manager.add(*list(related_b.all()))
{% endhighlight %}

This code is used for substituting related objects (tags in our case). It works
like this:

> if some field's strategy is to switch to objects from the other event, then
> remove all currently assigned objects and add objects from the other event's
> field.

Translated into tags:

> if user wants to use event `2016-05-06-RDAP16-Atlanta` as base event, but
> keep tags from the other event (`2016-05-06-asist`) then remove current tags
> from base event and add tags from the other event.

See what's going on here? Base event's tags were removed instead of being
unassigned.

#### Django: related manager and assignments

In this section I'm going to talk about how relations work and if they can be
unassigned instead of being removed.

For many-to-many relationships (e.g. multiple events can be assigned multiple
tags) Django creates an intermediate table that stores assignments. In this
case, unassigning event from tag is as simple as removing that stored
assignment from the intermediate table.

For one-to-many relationships (e.g. multiple events can have the same
organizer) there's no need for additional table; storing the organizer looks
like `event.organizer = SomeOrganizer`.

In case of the one-to-many relationships we can unassign the event from
`SomeOrganizer` if and only if `event.organizer` field can store `NULL` value.
If it cannot, then we have to remove the event.

So the bug existed because the case of unassignment was not taken into account
– only removal of related objects was accounted for.

### Fix: need to find out when we can unassign

Long story short: in Django only related manager with `.clear` method can
unassign; if this method is not present then the only option is removal.

So fixed code looks like this (minus the comments):

{% highlight python %}
            if value == 'obj_a' and manager != related_a:
                if hasattr(manager, 'clear'):
                    manager.clear()
                else:
                    manager.all().delete()
                manager.set(list(related_a.all()))

            elif value == 'obj_b' and manager != related_b:
                if hasattr(manager, 'clear'):
                    manager.clear()
                else:
                    manager.all().delete()
                manager.set(list(related_b.all()))
{% endhighlight %}

(Yes, it probably should use `try - except` block instead of `hasattr`; pull
request's welcome!)

## Final words

All in all, I feel good about this bug; if anything, I'd like eliminate the
errorneous timezone arithmetics.

Also all backup mechanics and logging worked really nice.

As a result of investigation described above, the bug and the solution to it
last night I released AMY [v1.5.2][].

  [v1.5.2]: https://github.com/swcarpentry/amy/milestones/v1.5.2

