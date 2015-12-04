---
layout: post
title: "Sublime Text 3 for Python development"
tags: [python, sublime text, configuration, projects]
date: 24.08.2013
---

I've been heavy vim user for a couple of years. I had a very cool
configuration, really got all these fancy vim key shortcuts
muscle-memorized.

But then vim plugins (bundles) started annoying me. Often my
configuration became obsolete after an upgrade. I had to go through
documentation and set everything yet again.

So I decided to give [Sublime Text 2] a try, and then [Sublime Text 3]. And in
August 2013 I switched almost completely. I still love vim, but now I program
mainly in [Sublime Text 3].

{:.toc}
1. [Why switch to Sublime Text 3?](#why-switch-to-sublime-text-3)
2. [Brief history](#brief-history)
3. [Configuration](#configuration)
    1. [Theme](#theme)
    2. [Typeface](#typeface)
    3. [Python](#python)
    4. [Behavior](#behavior)
    5. [Configuration file](#configuration-file)
4. [Plugins](#plugins)
    1. [Package Control](#packagecontrol)
    2. [Git](#git)
    3. [GitGutter](#gitgutter)
    4. [SideBarEnhancements](#sidebarenhancements)
    5. [Anaconda](#anaconda)
    6. [Gist](#gist)
5. [Final words](#final-words)
6. [Two years later update](#two-years-later-update)

Why switch to Sublime Text 3?
-------------------------------

For me, these are the reasons:

* Sublime Text 3 is **sooo** [pretty](http://imgur.com/v8lb6mX)
* it's also so freaking fast, way faster than Sublime Text 2
* and has vast range of plugins, and easy configuration.

Not much, you say? It was enough to made me switch editors.

Brief history
-------------

Sublime Text 2 was using Python 2.x as an API interpreter. Early in
2013, first build of Sublime Text 3 appeared, not even remotely
complete. And it shipped with Python 3.3 interpreter.

Since then, Sublime Text 3 (now beta build 3047 or [bleeding edge dev
build](http://www.sublimetext.com/3dev) 3052) has come a long way and can be
used by everyday programmer.

What's important is that many Sublime Text 2 plugins have been either
ported or made Python2/3 compatible.

Configuration
-------------

### Theme

There's [lots](https://sublime.wbond.net/search/scheme) and
[lots](http://colorsublime.com/) of themes for Sublime Text 3. 
I currently use [Monokai Extended](https://sublime.wbond.net/packages/Monokai%20Extended), with
[Soda](https://sublime.wbond.net/packages/Theme%20-%20Soda) dark theme.

[Perv Orange](https://sublime.wbond.net/packages/Perv%20-%20Color%20Scheme) is
also very good, but a bit darker than Monokai.

Both schemes have better restructuredText coloring. Default Sublime Text
3 syntax highlighting for rsT is... in a poor state.

{:.figure}
![Soda theme with Monokai Extended color scheme](http://i.imgur.com/v8lb6mXl.png)
Visual preview of my current configuration. [(click to enlarge)](http://imgur.com/v8lb6mX)

Some visual settings:

{% highlight json %}
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
{% endhighlight %}

### Typeface

I've tested
[Consolas](http://www.microsoft.com/typography/fonts/family.aspx?FID=300),
[Monaco](http://en.wikipedia.org/wiki/Monaco_%28typeface%29), [Ubuntu
Mono](http://font.ubuntu.com/#charset-mono-regular) and
[Meslo](https://github.com/andreberg/Meslo-Font). Last two are my
favorite, I switch them back and forth very often.

Configuration for Meslo:

{% highlight json %}
{
    "font_face": "Meslo LG L",
    "font_size": 10,
    "line_padding_bottom": 0,
    "line_padding_top": 0,
}
{% endhighlight %}

Configuration for Ubuntu Mono:

{% highlight json %}
{
    "font_face": "Ubuntu Mono",
    "font_size": 12,
    "line_padding_bottom": 1,
    "line_padding_top": 1,
}
{% endhighlight %}

And some additional typeface-agnostic but font-related settings:

{% highlight json %}
{
    "caret_style": "solid",
    "font_options":
    [
        "subpixel_antialias"
    ],
    "highlight_line": true,
}
{% endhighlight %}

### Python

This part of configuration helps with writing Python.

{% highlight json %}
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
{% endhighlight %}

### Behavior

Fixes some minor annoyings, like opening a preview after selecting file
in side bar.

{% highlight json %}
{
    "enable_telemetry": false,
    "preview_on_click": false,
    "shift_tab_unindent": true,
    "show_panel_on_build": false,
}
{% endhighlight %}

You can also change some settings on a per-project basis. 
Simply open your `project.sublime-project` file
(`Project → Edit Project`) and add `settings` section:

{% highlight json %}
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
{% endhighlight %}

### Configuration file

For lazy people: <https://gist.github.com/pbanaszkiewicz/6351258>.

{% gist 6351258 %}

Plugins
-------

These are the plugins I can't live (and program) without. Absolutely
necessary.

### [Package Control](https://sublime.wbond.net/installation) {#packagecontrol}

A package manager for Sublime Text 3. Helps you search for, install,
upgrade and remove most of available Sublime Text 3 packages.

### [Git](https://sublime.wbond.net/packages/Git) {#git}

Very popular and quite easy for basic application. There's also some
payable [SublimeGit](https://sublimegit.net/) plugin I haven't tried out
yet. (It seems nice, though!)

**Update 30.08.2013:** I switched to
[SublimeGit](https://sublimegit.net/) plugin. It's very similar to vim's
fugitive, so I'm already feeling good about it. Definitely well spent
money on an alternative to
[Git](https://sublime.wbond.net/packages/Git).

### [GitGutter](https://sublime.wbond.net/packages/GitGutter) {#gitgutter}

Adds small icons in left margin indicating which lines have been added,
modified or deleted.

{:.figure}
![GitGutter icons example](http://i.imgur.com/xseT2Eq.png)
GitGutter icons: for deleted, added and modified lines. [(click to enlarge)](http://imgur.com/xseT2Eq)

### [SideBarEnhancements](https://sublime.wbond.net/packages/SideBarEnhancements) {#sidebarenhancements}

Adds obvious (but missing from pure Sublime Text 3!) context menu
options for side bar.

{:.figure}
![Additional entries in sidebar's context menu.](http://i.imgur.com/qW4H6Kd.png)
Additional items in sidebar's context. [(click to enlarge)](http://imgur.com/qW4H6Kd)

### [Anaconda](https://sublime.wbond.net/packages/Anaconda) {#anaconda}

So far, the best Python completion and linter for Sublime Text 3. You
can believe me, I tested other ones, too.

Anaconda is actively developed, and its' author is very responsive.

I highly recommend installing this package from `git`, as I'm not sure
if recent critical patches were already pulled in by Package Control.

**Warning**: do not mistake with Continuum.io's [excellent Anaconda suite for Python](https://www.continuum.io/).

### [Gist](https://sublime.wbond.net/packages/Gist) {#gist}

This plugins helps managing (adding, editing and removing) GitHub gists.
Needs a little bit of configuration efforts, but it's generally
worthwhile.

{:.message}
**Warning**: After installing each plugin, check if your configuration and
favorite key bindings still work. It will be harmful for you to discover after
pulling in four plugins that one of them disabled selecting multiple
cosecutive lines separately (`Shift+Alt+Up/Down`) or inserting
multiple carets in EOLs in your selection (`Ctrl+Shift+L`).
I even recall some plugin changing behavior of inserting brackets
around selection! That was just mean...

Final words
-----------

I hope I was somehow able to help you boost your Python development or
encourage to use Sublime Text 3. Have a good time and nothing to debug!

Two years later update
----------------------

It's December 2015, so over 2 years have passed since this post was originally
published. What changed in Sublime Text 3? Am I still using it?

The answer is: yes! Even though the development of Sublime Text 3 is stalled
(if only it was open source) I'm still using it. It's a great product that
"just works".

Here are changes in my configuration:

* I switched my theme to Solarized Light, because I'm programming a lot in
  a daylight and I need a good, light background.
* I'm using a new font: [Hack](http://sourcefoundry.org/hack/). It works great,
  but as I mentioned in the original article, I like to switch fonts now and
  then. I'll probably switch to something else really soon.
* Now I also use a bigger font size, and it works better for my eyes.

{:.figure}
![Screenshot of some code.](http://i.imgur.com/Fo16Tc7.png)
Solarized Light, Hack font face, and some of [AMY]'s code. [(click to enlarge)](https://imgur.com/Fo16Tc7)

Here is a list of plugins that I got rid of:

* Gist: I'm not sharing so much code to be in need of plugin for that service.

New plugins:

* SublimeGit: it was mentioned in update to the original article, but this
  plugin works excellent. It may not work great during rebases (doesn't show
  conflicting files), but I'd not trust any tool except `git` in such time.
* SublimeLinter: excellent for checking my Python and JavaScript syntax
  correctness, and standards (like [PEP8]) compliance.

I'm really interested to see how my usage of Sublime Text 3 develops in future.


  [Sublime Text 2]: http://www.sublimetext.com/
  [Sublime Text 3]: http://www.sublimetext.com/3
  [PEP8]: https://www.python.org/dev/peps/pep-0008/
  [AMY]: https://github.com/swcarpentry/amy
