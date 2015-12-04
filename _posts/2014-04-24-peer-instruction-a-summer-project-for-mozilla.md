---
layout: post
title: "Peer instruction - a summer project for Mozilla"
tags: [peer instruction, teaching, mooc, software carpentry, mozilla, gsoc]
date: 24.04.2014
---

I was accepted for [Google Summer of Code 2014]. My project is called
"Peer instruction", and I'm doing it under the wings of [Mozilla
foundation](https://www.mozilla.org/en-US/) (or, more specifically,
[Software Carpentry](http://software-carpentry.org/)).

Peer instruction
----------------

[Science tells us](http://www.slideshare.net/richardcookau/john-hattie-effect-sizes-on-achievement)
that students in groups learn more effectively [^1]. This concept is
widely used in peer instruction.

[Peer instruction](http://en.wikipedia.org/wiki/Peer_instruction) is a
teaching methodology developed over 20 years ago. It's different from
typical learning classes in today's colleges or universities. The basic
workflow goes more or less like this:

1. Teacher asks a question.
2. Students individually answer it.
3. Students are split into small groups to discuss their answers.
4. Teacher reveals the good answer.

The key feature of this methodology is splitting students into small
groups.

Summer project
--------------

If you take an online classes by Udacity, Coursera, Khan Academy or
whoever there is, you may notice they don't deploy peer instruction.

But with web technologies of today, it is possible to create a virtual
classroom that leverages this promising teaching methodology! And my
task is to do it.

The minimum outcome
-------------------

No, I don't want to create a "full-stack" virtual classroom. The
**minimum viable product** of my work will be a **proof-of-concept**
working web service that lets you quickly switch from broadcasting (or
"teacher mode") to many few-to-few multiplexed broadcasts (or
"small-groups-talk mode").

Of course, if I can, I'll implement as many additional features as
possible.

The obstacles
-------------

The only two difficulties I foresee right now are:

1. The lack of fast MCU technology.
2. The lack of fast internet.

MCU stands for "Multipoint Control Unit", a software or hardware used to
bridge media transmissions.

The only one open source software MCU for WebRTC (technology used for
media transmission in modern browsers) I found so far is
[Erizo](https://github.com/ging/licode/tree/master/erizo). I may have to
implement an Erizo API module for Python if I decide to stick to Python.

So that's the only issue I can somehow overcome. I cannot fix the
internet speeds, though...

Possible features
-----------------

If I have enough time and knowledge, I'll implement:

* whiteboard
* voting system
* quizes
* translations

It's going to be exciting summer. I'm looking forward to it! :)

Contributing
------------

I welcome and highly appreciate any feedback, ideas, suggestions, or
complaints. I released publicly [my
proposal](https://gist.github.com/pbanaszkiewicz/11292070), so you can
comment it or even fork and make a better one.

I also want to share the link to the [Git
repository](https://github.com/pbanaszkiewicz/peer-instruction), where
my work will reside. Feel free to send pull requests :)

[^1]: Peer tutoring is ranked as having 0.55 influence on student's
    achievement, while 0.0 is none.

  [Google Summer of Code 2014]: http://www.google-melange.com/gsoc/homepage/google/gsoc2014
