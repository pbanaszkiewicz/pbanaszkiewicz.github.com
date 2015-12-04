My Own Blog
###########


This repository structure
-------------------------

My blog is hosted on GitHub as GitHub Pages service.  This service
automatically reacts on changes in this repository main branch, which is
`master`_, and hosts its content.

But my entries are written in rsT and then compiled to HTML.  I keep them in
`blog_content`_ branch, which also contains my theme and some settings files.


Installation
------------

Requirements:

* `Acrylamid`_ for blog software
* `Docutils`_ for rsT format parsing
* `ghp import`_ for deploying to `master_` branch
* `Pygments`_ for colorized code output

.. code-block:: console

    $ git clone ...
    # create a virtual environment and activate it...
    $ cd ...
    $ git checkout blog_content
    $ pip install -r requirements.txt

.. _master: https://github.com/pbanaszkiewicz/pbanaszkiewicz.github.com/tree/master
.. _blog_content: https://github.com/pbanaszkiewicz/pbanaszkiewicz.github.com/tree/blog_content
.. _Acrylamid: http://posativ.org/acrylamid/
.. _Docutils: http://docutils.sourceforge.net/
.. _ghp import: https://github.com/davisp/ghp-import
.. _Pygments: http://pygments.org/


Compilation
-----------

.. code-block:: console

    $ acrylamid compile

In order to work on the blog, use this command:

.. code-block:: console

    $ acrylamid autocompile

`Acrylamid`_ also supports indexing and searching, but I don't use this
feature at all.


Deployment
----------

To clean all the mess:

.. code-block:: console

    $ acrylamid deploy clean

To deploy your changes:

.. code-block:: console

    $ acrylamid compile
    $ acrylamid deploy


License
-------

**Blog content** is licensed under `CC BY-SA 3.0 license <http://creativecommons.org/licenses/by-sa/3.0/>`_.
It allows you to copy, distribute and transmit my work, adapt it and make
commercial use out of it **if** you assert that I was the original author
and your mix has the same or similar license.

Code examples published via this blog are
`public domain <http://en.wikipedia.org/wiki/Public_domain>`_.

My theme is copyrighted by me, Piotr Banaszkiewicz.
