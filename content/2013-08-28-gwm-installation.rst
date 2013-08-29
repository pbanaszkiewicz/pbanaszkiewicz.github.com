Ganeti Web Manager installation
###############################

:tags: [gsoc, 2013, gwm, devops]
:date: 28.08.2013

Due to my efforts, |GWM| is now a proper Python Package.

The main reasons for this change are:

* minimizing necessary dependencies (no more fabric!)
* keeping GWM codebase clean
* easing development

.. |GWM| replace:: Ganeti Web Manager


What does this change mean?
===========================

For end users
-------------

With GWM being Python package comes one huge advantage: easier installation.
It's actually one line to install whole GWM with dependencies!

Because my GSoC project is to make GWM installation easier for end users, I'm
writing a setup script, that will create virtual environment (helps with
separation), install GWM's dependencies and then GWM itself.

To install Ganeti Web Manager, simply get `setup.sh`_ script, make it
executable and run ``setup.sh -h`` to get familiar with it's command line
arguments.

.. _setup.sh: https://github.com/pbanaszkiewicz/ganeti_webmgr-setup/blob/develop/setup.sh

.. code-block:: console

    $ wget -c https://github.com/pbanaszkiewicz/ganeti_webmgr-setup/blob/develop/setup.sh
    $ chmod +x setup.sh
    $ ./setup.sh -h
    $ ./setup.sh -d /opt/gwm


.. note::

    As of 29/08/2013, this setup script is Work In Progress (TM).  Some parts
    of it may not be completed and simply won't work.  Be careful.  Or wait for
    |GWM| next release, which should be **0.11**.


For developers
--------------

To start working on GWM, you have to:

1. make virtual environment
2. ``git clone`` GWM repository
3. install GWM as a development package

(I suggest using ``virtualenvwrapper`` for #1, as it keeps your directory with
code clean.)

In shell terms it looks like this:

.. code-block:: console

    $ mkvirtualenv gwm
    (gwm)$ git clone git://git.osuosl.org/gitolite/ganeti/ganeti_webmgr
    (gwm)$ cd ganeti_webmgr
    (gwm)$ python setup.py develop

And that's it, now you can work on GWM.
(Alternatively you could install GWM development dependencies instead of whole
package:)

.. code-block:: console

    (gwm)$ pip install -r requirements/development.txt
