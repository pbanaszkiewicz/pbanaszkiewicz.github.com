Sublime Text 3 for Python development
#####################################

:tags: [python, sublimetext, configuration, projects]
:date: 24.08.2013

I've been heavy vim user for a couple of years.  I had a very cool
configuration, really got all these fancy vim key *shortcuts* muscle-memorized.

But then vim plugins (bundles) started annoying me.  Often my configuration
become obsolete after an upgrade.  I had to go through documentation and set
everything once again.

So I decided to give |ST2| a try.  And in August 2013 I switched almost
completely.  I still love vim, but now I program mainly in |ST3|_.

.. |ST3| replace:: Sublime Text 3
.. |ST2| replace:: Sublime Text 2
.. _ST2: http://www.sublimetext.com/
.. _ST3: http://www.sublimetext.com/3

.. contents:: Table of contents
    :depth: 2
    :backlinks: none


Why switch to |ST3|_?
=====================

For me, these are the reasons:

* |ST3| is **sooo** `pretty <http://imgur.com/v8lb6mX>`_
* it's also so freaking fast, way faster than |ST2|
* vast range of plugins, easy configuration

Not much, you say?  It was enough to made me switch editors.


Brief history
=============

|ST2| was using Python 2.x as an API interpreter.  Early in 2013, first build
of |ST3| appeared, not even remotely complete.  And it shipped with Python 3.3
interpreter.

Since then, |ST3| (now beta build 3047 or bleeding edge dev build 3052) has
come a long way and can be used by everyday programmer.

What's important is that many |ST2| plugins have been either ported or made
Python2/3 compatible.


Configuration
=============

Theme
*****

There's `lots <https://sublime.wbond.net/search/scheme>`__ and
`lots <http://colorsublime.com/>`__ of themes for |ST3|.  I currently use
`Monokai Extended`_, with `Soda`_ dark theme.

`Perv Orange`_ is also very good, but a bit darker than Monokai.

.. _Monokai Extended: https://sublime.wbond.net/packages/Monokai%20Extended
.. _Soda: https://sublime.wbond.net/packages/Theme%20-%20Soda
.. _Perv Orange: https://sublime.wbond.net/packages/Perv%20-%20Color%20Scheme

Both schemes have better restructuredText coloring.  Default |ST3| syntax
highlighting for rsT is... in a poor state.

.. figure:: http://i.imgur.com/v8lb6mXl.png
    :alt: Soda theme with Monokai Extended color scheme
    :align: center
    :target: http://imgur.com/v8lb6mX

    Visual preview of my current configuration.

Some visual settings:

.. code-block:: json

    {
        "always_show_minimap_viewport": true,
        "bold_folder_labels": true,
        "draw_minimap_border": true,
        "highlight_modified_tabs": true,
        "indent_guide_options":
        [
            "draw_active",
            "draw_normal"
        ],
        "soda_classic_tabs": true,
        "soda_folder_icons": false,
    }

Typeface
********

I've tested `Consolas`_, `Monaco`_, `Ubuntu Mono`_ and `Meslo`_.  Last two are
my favorite, I switch them back and forth very often.

.. _Consolas: http://www.microsoft.com/typography/fonts/family.aspx?FID=300
.. _Monaco: http://en.wikipedia.org/wiki/Monaco_%28typeface%29
.. _Ubuntu Mono: http://font.ubuntu.com/#charset-mono-regular
.. _Meslo: https://github.com/andreberg/Meslo-Font

Configuration for Meslo:

.. code-block:: json

    {
        "font_face": "Meslo LG L",
        "font_size": 10,
        "line_padding_bottom": 0,
        "line_padding_top": 0,
    }

Configuration for Ubuntu Mono:

.. code-block:: json

    {
        "font_face": "Ubuntu Mono",
        "font_size": 12,
        "line_padding_bottom": 1,
        "line_padding_top": 1,
    }

And some additional typeface-agnostinc but font-related settings:

.. code-block:: json

    {
        "caret_style": "solid",
        "font_options":
        [
            "subpixel_antialias"
        ],
        "highlight_line": true,
    }

Python
******

This part of configuration helps with writing Python.

.. code-block:: json

    {
        "ensure_newline_at_eof_on_save": true,
        "folder_exclude_patterns":
        [
            ".svn",
            ".git",
            ".hg",
            "CVS",
            "__pycache__"
        ],
        "indent_to_bracket": true,
        "rulers":
        [
            79
        ],
        "shift_tab_unindent": true,
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true,
        "wrap_width": 80
    }

Behavior
********

Fixes some minor annoyings, like opening a preview after selecting file in side
bar.

.. code-block:: json

    {
        "enable_telemetry": false,
        "preview_on_click": false,
        "shift_tab_unindent": true,
        "show_panel_on_build": false,
    }


.. note::

    You can change some settings on a per-project basis.  Simply open your
    ``project.sublime-project`` file (``Project → Edit Project``) and add
    ``settings`` section:

    .. code-block:: json

        {
            "folders":
            [
                ...
            ],
            "settings":
            {
                "python_interpreter": "/home/piotr/.virtualenvs/project/bin/python"
            }
        }

Configuration file
******************

For lazy people: https://gist.github.com/6351258.


Plugins
=======

These are the plugins I can't live (and program) without.  Absolutely
necessary.

`Package Control`_
******************

A package manager for |ST3|.  Helps you search for, install, upgrade and remove
most of available |ST3| packages.

`Git`_
******

Very popular and quite easy for basic application.  There's also some payable
`SublimeGit`_ plugin I haven't tried out yet. (It seems nice, though!)

**Update 30.08.2013:** I switched to `SublimeGit`_ plugin.  It's very similar
to vim's fugitive, so I'm already feeling good about it.  Definitely well spent
money on an alternative to `Git`_.

`GitGutter`_
************

Adds small icons in left margin indicating which lines have been added,
modified or deleted.

.. figure:: http://i.imgur.com/xseT2Eq.png
    :alt: GitGutter icons example
    :align: left
    :target: http://imgur.com/xseT2Eq

    GitGutter icons: for deleted, added and modified lines.

`SideBarEnhancements`_
**********************

Adds obvious (but missing from pure |ST3|!) context menu options for side bar.

.. figure:: http://i.imgur.com/qW4H6Kd.png
    :alt: GitGutter icons example
    :align: left
    :target: http://imgur.com/qW4H6Kd

    Additional items in side bar's context menu.

`Anaconda`_
***********

So far, the best Python completion and linter for |ST3|.  You can believe me,
I tested other ones, too.

Anaconda is actively developed, and it's author is very responsive.

I highly recommend installing this package from ``git``, as I'm not sure if
recent critical patches were already pulled in by Package Control.

`Gist`_
*******

This plugins helps managing (adding, editing and removing) GitHub gists.  Needs
a little bit of configuration efforts, but it's generally worthwhile.

.. _Package Control: https://sublime.wbond.net/installation
.. _Git: https://sublime.wbond.net/packages/Git
.. _SublimeGit: https://sublimegit.net/
.. _GitGutter: https://sublime.wbond.net/packages/GitGutter
.. _SideBarEnhancements: https://sublime.wbond.net/packages/SideBarEnhancements
.. _Anaconda: https://sublime.wbond.net/packages/Anaconda
.. _Gist: https://sublime.wbond.net/packages/Gist

.. warning::

    After installing each plugin, check if your configuration and favorite key
    bindings still work.  It will be harmful for you to discover after pulling
    in four plugins that one of them disabled selecting multiple cosecutive
    lines separately (``Shift+Alt+Up/Down``) or inserting multiple carets in
    EOLs in your selection (``Ctrl+Shift+L``).

    I even recall some plugin changing behavior of inserting brackets around
    selection!  That was just mean...


Final words
===========

I hope I was somehow able to help you boost your Python development or
encourage to use |ST3|.  Have a good time and nothing to debug!
