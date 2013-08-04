Google Summer of Code update #1
###############################

:tags: [python, gwm, gsoc]
:date: 08.07.2013

So far in the `Google Summer of Code 2013`_ I've been working on
`Ganeti Web Manager`_.

.. _Google Summer of Code 2013: http://www.google-melange.com/gsoc/homepage/google/gsoc2013
.. _Ganeti Web Manager: https://code.osuosl.org/projects/ganeti-webmgr

My job was to refactor |GWM| so that instead of one huge, bloated Django application (``ganeti_web``), the project would consist of many smaller apps.

I shared more details in `this`_ blog post.

.. _this: http://piotr.banaszkiewicz.org/blog/2013/06/06/ganeti-web-manager-modularization/

Now I can say my work is mostly done.  I've got smaller apps extracted and
(this one's big) I worked on database migrations.

Now (hopefully!) any user can checkout `my branch`_ and successfully run it
against their codebase.

.. _my branch: https://github.com/pbanaszkiewicz/ganeti_webmgr/tree/enhancement/13599

Why are you doing this, one can ask.  There's no visible benefit for end
users.  Actually even worse: they for example have to use `settings file`_
which is now stored completely `elsewhere`_.

.. _settings file: http://ganeti-webmgr.readthedocs.org/en/latest/installing.html#minimum-configuration
.. _elsewhere: https://github.com/pbanaszkiewicz/ganeti_webmgr/tree/enhancement/13599/ganeti_web/ganeti_web/settings

This work brings hope and sunlight to all the GWM developers.  It helps new
ones "see" and understand code, as the code is now simpler!  And it helps old
devs navigate through the code, while fixing or enhancing it.

I hope to get my work merged soon, although it's quite big change so the
proper code review is really necessary.

Next on the `GSOC agenda`_: taking care of |GWM| dependencies.  I.e.
documenting, testing, uploading to `PyPI`_, maybe even setting up a `CI`_.

.. _GSOC agenda: http://staff.osuosl.org/~pbanaszkiewicz/proposal_osuosl_gsoc2013.html

.. _PyPI: https://pypi.python.org/pypi
.. _CI: https://travis-ci.org/

.. |GWM| replace:: Ganeti Web Manager
