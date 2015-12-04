---
layout: post
title: "Google Summer of Code update #1"
tags: [python, gwm, gsoc]
date: 08.07.2013
---

So far in the [Google Summer of Code 2013] I’ve been working on [Ganeti
Web Manager].

My job was to refactor Ganeti Web Manager so that instead of one huge,
bloated Django application (`ganeti_web`), the project would consist of
many smaller apps.

I shared more details in [this] blog post.

Now I can say my work is mostly done. I’ve got smaller apps extracted
and (this one’s big) I worked on database migrations.

Now (hopefully!) any user can checkout [my branch] and successfully run
it against their codebase.

Why are you doing this, one can ask. There’s no visible benefit for end
users. Actually even worse: they for example have to use [settings file]
which is now stored completely [elsewhere].

This work brings hope and sunlight to all the GWM developers. It helps
new ones “see” and understand code, as the code is now simpler! And it
helps old devs navigate through the code, while fixing or enhancing it.

I hope to get my work merged soon, although it’s quite big change so the
proper code review is really necessary.

Next on the [GSOC agenda]: taking care of Ganeti Web Manager
dependencies. I.e. documenting, testing, uploading to [PyPI], maybe even
setting up a [CI].

  [Google Summer of Code 2013]: http://www.google-melange.com/gsoc/homepage/google/gsoc2013
  [Ganeti Web Manager]: https://code.osuosl.org/projects/ganeti-webmgr
  [this]: http://piotr.banaszkiewicz.org/blog/2013/06/06/ganeti-web-manager-modularization/
  [my branch]: https://github.com/pbanaszkiewicz/ganeti_webmgr/tree/enhancement/13599
  [settings file]: http://ganeti-webmgr.readthedocs.org/en/latest/installing.html#minimum-configuration
  [elsewhere]: https://github.com/pbanaszkiewicz/ganeti_webmgr/tree/enhancement/13599/ganeti_web/ganeti_web/settings
  [GSOC agenda]: http://staff.osuosl.org/~pbanaszkiewicz/proposal_osuosl_gsoc2013.html
  [PyPI]: https://pypi.python.org/pypi
  [CI]: https://travis-ci.org/
