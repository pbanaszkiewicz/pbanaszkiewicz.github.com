---
layout: post
title: "Peer instruction: update 4"
tags: [peer instruction, javascript, mozilla, gsoc]
date: 22.06.2014
---

This week me and Greg Wilson, my mentor, we decided to test run
[Pitt](https://github.com/pbanaszkiewicz/pitt). It was a success and,
while revealing some annoying bugs, it made Greg really excited.

Current release
---------------

Current version is v0.3, altough I might have tagged it wrong in git.
Fortunately it seems that tag was not published to the GitHub
repository.

### Current features

This is a quick recap on what Pitt is capable of right now.

1.  Users coming in and quitting: thanks to signalling, as soon as
    someone appears online, they're being logged in and everyone can see
    them.
2.  Quick switch mode: the instructor can easily and very quickly switch
    modes from broadcasting (to all students) to work in small groups
    (students are split into pairs or groups of 3).

The code is decent. I presume there are some bugs with saved state of
the application. For example, what to do if the instructor is
broadcasting and someone joins in? What if another instructor joins in?
What if there are two instructors and one starts broadcasting, should
other instructors see their stream too?

These kind of questions will be addressed for the [v0.4
release](https://github.com/pbanaszkiewicz/pitt/issues?milestone=2&state=open).
Right now I'm working to get [v0.3.1
release](https://github.com/pbanaszkiewicz/pitt/issues?milestone=1&state=open)
by Friday, 27.06.2014.

### Exposed bugs

During my test run with Greg we quickly found out one super annoying
bug.

There's a very interesting human behavior: people slow down their talk
when they hear themselves with small delay. It's really hard to overcome
this basic reflex.

Back to the bug: we found out that local stream video (ie. the one where
you can see yourself, because browser plays the video from your webcam)
is not muted by default. Add the playback delay to the mix and as a
result Greg was struggling to speak.

This bug was really easy to fix (in HTML5:
`<video src="..." muted="muted">`) and the fix is included in the recent
code.

There was also issue with the state of the application - it somehow
broke for Greg (when he was a student). I have yet to discover the
actual bug.

### Missing features

Greg wants me to add these two new features to the upcoming release:

1.  Countdown. The instructor presses "back to broadcast mode" button
    and the switch doesn't happen immediately. First there's 30 seconds
    countdown so that no students are interrupted in the middle of the
    sentence.
2.  Variable group size. The instructor can specify if the students are
    split into pairs or groups of 3, or groups of 6. This task is more
    challenging than it seems: I have to ensure that no students are
    left alone (what is often the case when there's odd number of
    students).

Next release
------------

I'm planning to release next version, v0.3.1, on Friday 27.06.2014 or
earlier.

I have 3 exams before Friday and 2 after it. Ouch...
