---
layout: post
title: "Peer instruction: update 9"
tags: [peer instruction, javascript, mozilla, gsoc]
date: 11.08.2014
---

This summer was great. I'm really glad I had the chance to work with
Mozilla Science Lab on bringing a new teaching tool.

Here are a few of my thoughts about the good, the bad parts about GSoC
2014 and the future of my project.

What's cool about this summer
-----------------------------

This summer was special for a variety of reasons.

I was working on a bleeding edge technology with a language I didn't
really understand previously. It gave me opportunity to not only dig
into software architectures I haven't known before (like pub/sub) but
also to learn how professionals write JavaScript.

I met quite a few people interested in my project (despite very low
number of stars or watchers on GitHub) and spent fruitful time with my
mentors on discussions about the project.

What's not cool about this summer
---------------------------------

A few things that come to my mind that could've been done better.

First, at the beginning of this project I pivoted a little. The actual
codebase and architecture (pub/sub) is, I think, third or even fifth
iteration.

I was promised a community hosting for my project at Mozilla but didn't
get one, even though I went through some lengthy procedures. Instead, my
mentor had to allow me on his private server.

I'm also a little sad that my project doesn't bring as much attention
and excitement as it excites me. Hopefully I will be able to present it
during [MozFest](http://2014.mozillafestival.org/) and it will spark
some interest.

Conclusions
-----------

JavaScript's poor object-programming design causes programmers to write
things in many different ways. There's actually no one good way to write
JavaScript. I found some really well-written JavaScript libraries but I
was unable to write pretty code myself. Python for browsers anyone?

{:.message}
**Note**: CoffeeScript or Dart were crossed out at the beginning. In April,
during PyCon in Montreal, actually. Reason: too fresh, too unstable and with
little support, even though they may provide a better language experience.

Running multiple camera streams within browser is very resource-heavy.

I'm pretty happy that I end the summer with a working application that
still can fit multiple features, ehancements and improvements. There's
even place for [something that wasn't done
before](https://github.com/pbanaszkiewicz/pitt/issues/22), I think.

Peer instruction teaching tool features
---------------------------------------

I "end" this project with these specific features implemented:

* broadcasting mode
* discussions in small groups mode
* really quick switching between these modes
* countdown with audio aid before disabling discussions mode
* variable small group sizes
* better interface for tablets
* basic text chat

It might seem like not that much, but I spent whole summer on this and I
think I did pretty good :)

In near future I want to see these features implemented:

* better chat
* better interface
* better backend and frontend code structure
* sharing files
* connections routing / mesh

Acknowledgements
----------------

I want to highlight and thank Greg Wilson and Mike Hoye - my mentors
during this summer. Their efforts and continuous work and long meetings
with me... I call this summer a success; it wouldn't be without your
help. **Thank you!** :)
