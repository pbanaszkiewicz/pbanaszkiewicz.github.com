---
layout: post
title: "Peer instruction: update 2"
tags: [peer instruction, javascript, mozilla, gsoc]
date: 07.06.2014
---

In this week's videoconference between my mentors, Greg Wilson and Mike
Hoye, [Software Carpentry](http://software-carpentry.org/)'s instructor
[David Rio](https://github.com/drio), and me, we decided to temporarily
drop [my current codebase](https://github.com/pbanaszkiewicz/peer-instruction)
and what I've done with [Licode](http://lynckia.com/licode/) and Erizo.

Instead, my current efforts will be focused on developing and enhancing
David's [excellent work](https://github.com/drio/pitt) that uses
[PeerJS](http://peerjs.com/).

This has some interesting consequences.

Firstly, we can't have broadcasting using MCU in teacher's mode.
Instead, in this mode, we'll have to open P2P connections, what's
probably going to be quite challenging for teacher's internet
connection.

{:.message}
**Note**: In **teacher's mode**, the teacher broadcasts his stream to all of
their students. In **student's mode**, students are split into smaller groups
(6 people per group in real life, at most 4 people via Internet - more is
less efficient) and talk with each other.

But for now we want to ship first version as soon as possible, so we'll
care about that later.

Secondly, we'll have a lot clearer and "closer to the metal" code.
Opening sockets and handling all data transfers will be much easier, and
I like that fact a lot!

On my personal side of news, I'm currently preparing for exams (first
one: next Thursday), which leaves me very little time for GSOC
`#sadface`…
