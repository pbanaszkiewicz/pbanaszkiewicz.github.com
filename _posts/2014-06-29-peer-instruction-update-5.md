---
layout: post
title: "Peer instruction: update 5"
tags: [peer instruction, javascript, mozilla, gsoc]
date: 29.06.2014
---

This is gonna be a short one. Because of exams, I have to study a lot.
And because there was not much progress on
[Pitt](https://github.com/pbanaszkiewicz/pitt) during this week.

Current release
---------------

Current version is v0.3.1, and it's tagged in git repository. I'm
incorporating the
[git-flow](http://nvie.com/posts/a-successful-git-branching-model/)
model.

What I wanted to get in was two major features:

1. countdown before switch from group split to broadcasting mode,
2. small groups of students of variable-defined size.

I can tell that I was successful and these features are now part of
[v0.3.1](https://github.com/pbanaszkiewicz/pitt/issues?milestone=1&state=closed)
release.

Bugs
----

While testing with Greg and Mike at their office and me here in Kraków,
I couldn't connect to them and vice versa. Connections between Mike and
Greg worked as intended.

This was strange, because I didn't change the code so much that it'd
break. More so: last week while testing with Greg alone it worked!

So I conducted few more tests:

1)  Pitt: Kraków ↔ Kraków
2)  Pitt: Kraków ↔ Toronto Mozilla Office
3)  Pitt older version: Kraków ↔ Toronto Mozilla Office
4)  Other WebRTC application: Kraków ↔ Toronto Mozilla Office

In the previous week, I'm guessing Greg worked from his home. We wanted
to try Pitt in this configuration (Kraków ↔ Greg's home), but due to
holidays in Canada we were not able to.

From what I can tell, the issue lies in the client IP addresses
resolution. Here's a lengthy article about how hard it is to do WebRTC
properly:
<http://www.html5rocks.com/en/tutorials/webrtc/basics/#toc-signaling>

Anyway, I hopefully will be able to easily overcome this issue.
