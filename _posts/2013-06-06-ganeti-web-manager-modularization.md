---
layout: post
title: "Ganeti Web Manager Modularization"
tags: [gwm, python, gsoc]
date: 6.06.2013
---

I've got accepted in for this year's Google Summer of Code. My project
requires me not only to program, but also to improve automation and work
flow for GWM developers.

The least Django version Ganeti Web Manager is compatible with is 1.4.5.
However, GWM doesn't use the [new project
layout](https://docs.djangoproject.com/en/dev/releases/1.4/#updated-default-project-layout-and-manage-py)
introduced with Django 1.4.

The result is GWM's main directory being very cluttered. As for 0.10
release, there are 25 files and/or directories. With just the switch to
newer project layout, only 21 files/directories exists now in top level
dir. That number will soon decrease, as more files get moved to
appropriate places.

I'm sure setting files and files containing URLs will get tossed out
into related Django application directories, too.

Speaking of which: originally GWM was written as one single Django
application. Since [commit
dde1fdf1cc](https://github.com/pbanaszkiewicz/ganeti_webmgr/commit/dde1fdf1ccffc42fcb3fb5789d52b09df3fe78e8)
(WIP) it's now splitted into many smaller applications: `auth` (I might
change that name in future), `clusters` (containing code related to
clusters; surprise!), `ganeti_web` (original app), `jobs`, `nodes`,
`utils` (or doesn't-fit-anything-else category), and
`virtualmachines`. Two additional apps are moved from top-level
directory and both relate to
[Muddle](https://code.osuosl.org/projects/muddle). I'm not sure about
their fate; it's possible that they're gonna get sentenced.

The rationale for such splitting is mainly the construction of Django
models in `ganeti_web` application. That [single
file](https://github.com/osuosl/ganeti_webmgr/blob/release/0.10/ganeti_web/models.py)
itself changed its size from 1,958 down to 295 lines!

Next steps in GWM modularization will involve moving forms, templates,
tests, views, models, and URLs to appropriate places. And testing, lots
and lots of testing is required.

I also hope to document my work and general progress at least here. GWM
recently started hosting its documentation on the
[ReadTheDocs](https://gwm.readthedocs.org/en/latest/), I'll update it as
well.

All in all, I'm very happy with my project and GSoC 2013. :) Its
timeline has shifted so now GSoC covers more of my summer holiday. \#win
