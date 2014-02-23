How to bite Flask, SQLAlchemy and pytest all at once
####################################################

:tags: [Python, pytest, Flask, SQLAlchemy]
:date: 22.02.2014

I finally got to understand how `Flask`_ application and request contexts work,
how to use properly `SQLAlchemy`_'s scoped sessions and how to test my REST
applications with `pytest`_ efficiently.  Here's what I learnt, split into
topics.

.. contents:: Table of contents
    :depth: 2
    :backlinks: none

How does SQLAlchemy handle sessions
===================================

Your SQLAlchemy ``Session`` is the main place where you usually talk to your
database.

.. code-block:: python

    # somewhere globally in your application
    session = sqlalchemy.orm.sessionmaker()

    # somewhere in your views
    users = session.query(User).filter(User.name = "Piotr").all()

When someone accesses your page containing above snippet, they ought to use
a different session object, because `sessions must not be used concurrently`_.
It's dangerous.  It should not be the same object talking to your database
in two different requests (and users).

.. _sessions must not be used concurrently: http://docs.sqlalchemy.org/en/rel_0_9/orm/session.html#is-the-session-thread-safe

So you have to somehow spawn another ``Session`` object.  SQLAlchemy has
something exactly for you.  It's called *scoped sessions*.

.. note::
    Scoped sessions is a different programming pattern than ``sessionmaker``.
    The former is a `registry pattern`_, whereas the latter is a `factory`_.

.. _registry: http://martinfowler.com/eaaCatalog/registry.html

.. _factory: https://en.wikipedia.org/wiki/Factory_method_pattern

Scoped sessions
---------------

It's quite easy to understand how session for application scope is being
constructed.  For every incoming request, a different ``Session`` object is
being served.

So user *Mark* gets *session A*, user *Ellen* gets *session B* and user *Sam*
gets *session C*.  The key is that all these sessions are accessible via the
same line of code::

    users = session.query(User).filter(User.name = "Piotr").all()

All the required setup is this one little object, `scoped_session`_.

.. _scoped_session: http://docs.sqlalchemy.org/en/latest/orm/session.html#sqlalchemy.orm.scoping.scoped_session

You feed it with some session-factory-maker, like ``sessionmaker``::

    session = scoped_session(sessionmaker())

Only one part is missing... how does scoped session know when to "spawn"
a different session?  :ref:`I'll come back to that <zipping-flask-sa-together>`
after explaining what are Flask application and request contexts and how to
work with them.

What are Flask application and request contexts
===============================================

I like to think about Flask application context as being bound to one thread of
the actual application.  That context might be a set of global objects, like
database connection and app settings.  These objects should only exist once
per your application, right?  (I don't see a point duplicating application
settings).

.. note::
    SQLAlchemy provides a `pool of connections`_ to the database.  You can pop
    a connection any time and push it back after you're done.  This, however,
    doesn't mean you have to pop two or more connections at once!

.. _pool of connections: http://docs.sqlalchemy.org/en/latest/core/pooling.html

.. warning::
    This is not really true, you can manipulate application contexts

.. zipping-flask-sa-together:

Zipping Flask request contexts and SQLAlchemy scoped sessions together
======================================================================


.. _Django: https://www.djangoproject.com/

.. _Flask: http://flask.pocoo.org/

.. _Flask-SQLAlchemy: https://pythonhosted.org/Flask-SQLAlchemy/

.. _SQLAlchemy: http://docs.sqlalchemy.org/

.. _pytest: http://pytest.org/latest/
