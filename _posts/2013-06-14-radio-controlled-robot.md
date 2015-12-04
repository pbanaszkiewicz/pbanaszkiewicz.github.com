---
layout: post
title: "Radio controlled robot"
tags: [cpp, agh, science, robotics]
date: 14.06.2013
---

Since last October I've been involved into
[Focus](http://focus.agh.edu.pl/) Scientific Circle (or group) at my
university. (Yeah, I know our webpage is horrible...)

From the very beginning we wanted to make a robot. A cool one,
precisely. So the idea we had was: let's take
[Kinect](http://en.wikipedia.org/wiki/Kinect), some mobile
platform/chassis, remote control, [Raspberry
Pi](http://www.raspberrypi.org/) and mix it all together.

I took a **long, long** time, but finally we have a semi-working
prototype. This week my friends made it possible to control our platform
via remote control (the same used to control high-end RC aircrafts).
That's a huge progress for our project.

Meanwhile I've been working on special algorithm, which is going to help
our [Kinect](http://en.wikipedia.org/wiki/Kinect) orientate in space.

The idea is to make 3-D maps of insides. The thing is,
[Kinect](http://en.wikipedia.org/wiki/Kinect) doesn't revolve around any
solid axis. Thus I think we could track (via Kinect's camera) a set of
points (features) and measure by which angle our robot turns.

If we know that angle, we could make those 3-D views of insides.

I'm going to use [OpenCV](http://docs.opencv.org/) and code everything
in C++. Hopefully it will work quite fast on our [Raspberry
Pi](http://www.raspberrypi.org/).
