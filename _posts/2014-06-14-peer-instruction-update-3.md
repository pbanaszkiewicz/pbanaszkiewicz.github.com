---
layout: post
title: "Peer instruction: update 3"
tags: [peer instruction, javascript, mozilla, gsoc]
date: 14.06.2014
---

The decision [has been made](http://piotr.banaszkiewicz.org/blog/2014/06/07/peer-instruction-update-2/),
and I switched to a [different codebase](https://github.com/drio/pitt).

I had one exam this week (*Aparatura Automatyzacji*, eng. *Automation
Systems*) and five more in next 2-3 weeks, so it is quite challenging
for me to find time for peer instruction right now.

I did, however, spend most of this weekend trying to make
[Pitt](https://github.com/drio/pitt) broadcasting mode for instructors.

It works! Proof below:

{:.figure}
![Me as instructor and two students.](http://i.imgur.com/43MTXXS.png)
Having dual monitor setup helps getting this kind of screenshots.
[(click to enlarge)](http://imgur.com/43MTXXS)

As you can see, the layout and design in general is very rough. And so
is the code.

This code is mostly based upon multiple events being propagated through
[sockets](http://socket.io/).

But I really don't like the design of these events, and, frankly
speaking, I much more prefer a "pub/sub" (publication - subscription)
architecture.

At this moment, when the instructor triggers an event, the server has to
repropagate it to every student.

In "pub/sub" arch, however, there's no repropagation in between.

Some people use [redis](http://redis.io/) for pub/sub, but I found some
really cool protocol: [WAMP] (don't confuse it with
Windows, Apache, MySQL, PHP stack!).

[WAMP] authors clearly explain [why it is good](http://wamp.ws/why/) so
please go there and read. Let me just point out a few cool features of
[WAMP]:

* [WAMP] is not a NodeJS module, it's a protocol
* it can be (and indeed is!) implemented in
  [various languages](http://wamp.ws/implementations/)
* therefore it's a solid foundation for a quickly changing service.

What I dislike about [WAMP] is that at the moment there's only one leading
implementation: [Autobahn](http://autobahn.ws/). And I'm not yet sure if
I want to drop NodeJS backend in the future, but if so, then there's
already fast Autobahn|Python.

  [WAMP]: http://wamp.ws/
