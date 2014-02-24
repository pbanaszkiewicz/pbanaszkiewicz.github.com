How to bite Flask, SQLAlchemy and pytest all at once
####################################################

:tags: [Python, pytest, Flask, SQLAlchemy, good practices]
:date: 22.02.2014

As a person who started with Django, I had some hard time figuring out how
application and request contexts work in `Flask`_.  I think I finally got to
understand them.  I also learnt how to use |SA|_'s scoped sessions properly
and how to test my REST applications with `pytest`_ efficiently.

.. _Flask: http://flask.pocoo.org/
.. _pytest: http://pytest.org/latest/

Here's what I got to know, split into topics.

.. warning::
    `Flask`_ and `SQLAlchemy`_ are very flexible, compared to `Django`_.  This
    article presents only one approach out of many on how to deal with
    thread-local stuff in your code.  But I think that it's one of the best
    approaches.

.. _Django: https://www.djangoproject.com/
.. |SA| replace:: SQLAlchemy
.. _SA: http://docs.sqlalchemy.org/
.. _SQLAlchemy: http://docs.sqlalchemy.org/

.. contents:: Table of contents
    :depth: 2
    :backlinks: none

How does SQLAlchemy handle sessions
===================================

Your SQLAlchemy ``Session`` is the main place where you usually talk to your
database.

.. code-block:: python

    # somewhere globally in your application
    from sqlalchemy.orm import sessionmaker
    session = sessionmaker()

    # somewhere in your views
    users = session.query(User).filter(User.name == "Piotr").all()

This code is perfectly fine **if used non-concurrently**.  Non-concurrently,
that means only one user can use session at once; that means, only one user
connects to your website at once.

In reality that's not always a case.  I bet you *want* your site to be safely
accessible by many users all at once.

If so, then you can't use ``sessionmaker`` alone.
`It's not designed <http://docs.sqlalchemy.org/en/rel_0_9/orm/session.html#is-the-session-thread-safe>`__
to create safe ``Session`` objects for multiple threads.

So what's the solution?  It's actually pretty clever.  It's called *scoped
sessions*: sessions, that are bound to the specific "scope" of your
application, for example: the scope of one user's connection.

.. note::
    Scoped sessions is a different programming pattern than ``sessionmaker``.
    The former is a `registry pattern`_, whereas the latter is a `factory`_.

.. _registry pattern: http://martinfowler.com/eaaCatalog/registry.html
.. _factory: https://en.wikipedia.org/wiki/Factory_method_pattern

Scoped sessions
---------------

It's quite easy to understand how session for application scope is being
constructed.  For every incoming request, a different ``Session`` object is
being served.

So user *Mark* gets *session A*, user *Ellen* gets *session B* and user *Sam*
gets *session C*.  The key is that all these sessions are accessible in your
code via the very same line:

.. code-block:: python

    # somewhere globally in your application
    from sqlalchemy.orm import scoped_session, sessionmaker
    session = scoped_session(sessionmaker())

    # somewhere in your views
    users = session.query(User).filter(User.name == "Piotr").all()

(Look at the previous snippet; they're almost the same!)

All the required setup is this one little object, `scoped_session`_.  You feed
it with some session-factory-maker, like ``sessionmaker``, and voilà.

.. _scoped_session: http://docs.sqlalchemy.org/en/latest/orm/session.html#sqlalchemy.orm.scoping.scoped_session

There's only one part missing... how does scoped session know when to "spawn"
a different session?  It somehow has to recognize that a new user is requesting
your views.

`I'll come back to that <zipping-flask-sa-together>`_
after explaining what are Flask application and request contexts and how to
work with them.

Transactions in |SA|
====================

|SA| supports at least two different kinds of transactions.  The most popular
type is `Session based transaction`_:

.. _Session based transaction: http://docs.sqlalchemy.org/en/rel_0_9/orm/session.html#committing

.. code-block:: python

    u1 = User(name="Piotr", email="test@example.org")
    session.add(u1)
    try:
        session.commit()
    except sqlalchemy.exc.IntegrityError:
        session.rollback()

The `second type <http://docs.sqlalchemy.org/en/rel_0_9/core/connections.html#using-transactions>`__ is more superior.  It can roll back even committed
session changes!  It's really powerful for testing purposes.

What are Flask application and request contexts
===============================================

Application context
-------------------

I like to think about Flask application context as being bound to one thread of
your actual application (website).  That context might be a set of global
objects, like database connection and app settings.  These objects should only
exist once per your application, right?  (I don't see a point in duplicating
app settings or database connections all over the place).

.. note::
    SQLAlchemy provides a `pool of connections`_ to the database.  You can pop
    a connection any time and push it back after you're done.  This, however,
    doesn't mean you have to pop two or more connections at once!

.. _pool of connections: http://docs.sqlalchemy.org/en/latest/core/pooling.html

In Flask, `current_app`_ is aware of the active application context.  If you
have your web application running on two threads, and one user accesses the
first thread, they'll use different Flask application than the other user
accessing second thread.

.. _current_app: http://flask.pocoo.org/docs/api/#flask.current_app

Request context
---------------

Request context is very similar to the application context.  Every time anyone
goes to some page on your site (ie. sends request), a new context is created.

This new context holds information that should only be available within that
particular second when the user is being served.  *I'm assuming you can serve
your user within one second :)*

For example, imagine you have a view that adds a new blog post to your site:

.. code-block:: python

    @app.route("/blogpost". methods=["POST", ])
    def blogpost_view():
        return "New blog post: {}".format(request.form)

Flask internals ensure that you do not access a different's request data.  Two
requests may be simultaneous, yet you will access exactly the correct request
in your code.

.. note::
    New request context creates new application context, if the latter is not
    available.

.. zipping-flask-sa-together:

Zipping Flask request contexts and SQLAlchemy scoped sessions together
======================================================================

So now you know what powers Flask contexts and that you should choose scoped
|SA| sessions over "normal" ones.  But how to make a ``scoped_session`` that
works *with* Flask contexts?

Take a closer look at `scoped_session`_.  You can see it has a `scopefunc`_
argument:

    ``scopefunc`` – optional function which defines the current scope.  If not
    passed, the ``scoped_session`` object assumes “thread-local” scope, and
    will use a Python ``threading.local()`` in order to maintain the current
    ``Session``.  If passed, the function should return a hashable token;
    this token will be used as the key in a dictionary in order to store and
    retrieve the current ``Session``.

.. _scopefunc: http://docs.sqlalchemy.org/en/latest/orm/session.html#sqlalchemy.orm.scoping.scoped_session.params.scopefunc

So... ``scopefunc`` has to unambiguously represent each individual context.
I was looking for a good way of handling that, and found one in
`Flask-SQLAlchemy`_.  This `Flask`_ extension `uses <https://github.com/mitsuhiko/flask-sqlalchemy/blob/d4560013c1c51ef035381e35dd42a1628bb212ee/flask_sqlalchemy/__init__.py#L665>`__ internal context stack to build hashable
context tokens.  The code looks like this:

.. _Flask-SQLAlchemy: https://pythonhosted.org/Flask-SQLAlchemy/

.. code-block:: python

    # somewhere globally in your application
    from flask import _app_ctx_stack
    from sqlalchemy.orm import scoped_session, sessionmaker
    session = scoped_session(sessionmaker(),
                             scopefunc=_app_ctx_stack.__ident_func__)


Testing everything
==================

Because of the aforementioned flexibility that `Flask`_ and |SA|_ have, I had
really hard time figuring the whole thing out.  **Testing is very important**,
and with the help of wonderful Python libraries like `pytest`_ it's actually
a pleasure.

Still, when trying out `pytest`_ for a first time, there is a small learning
curve if you come from Java-based `unittest`_ world.

.. _unittest: http://docs.python.org/3/library/unittest.html#module-unittest

The biggest change is in the ideology: now you don't have to write classes
(test cases) to test your code.  You can write **a lot simpler** functions
instead.

The important feature of `pytest`_ is `fixtures`_.  Use them when you want to
set up or tear down your tests.

.. _fixtures: http://pytest.org/latest/fixture.html

Fixtures
--------

A fixture is a function that, for example, returns a database session object,
which can be leveraged by your tests.

Or it can return a file descriptor to the file in ``/tmp/random_name``.  Or
your application object.  Or Redis connection object.

Look at `fixtures`_ docs for more examples.

Fixture scope
-------------

Every fixture can be set for a ``session`` scope, ``module`` scope, or
``function`` scope.  This means, that the fixture is only run once per testing
session, or once per whole module (containing tests), or once for every test
function.

Take for example this ``db_connect`` fixture.

.. code-block:: python

    import pytest

    @pytest.fixture(scope="session")
    def db_connect(request):
        db = sql.connect()

        def teardown():
            db.close()
        request.add_teardown(teardown)

        return db

It's dumb and won't work, but I hope you get the gist.  Even if you have
a thousand tests that use this fixture, it will be invoked only once, then
memorized (cached).

.. note::
    This small fixture uses another fixture!  `request <http://pytest.org/latest/builtin.html#_pytest.python.FixtureRequest>`__ is a built-in pytest fixture that helps you with teardowns.

I suggest to (at least) create a session-scoped fixture that builds your Flask
application object (using `application factory`_), and a session-scoped fixture
that builds your |SA| session and manages transactions.

.. _application factory: http://flask.pocoo.org/docs/patterns/appfactories/

Transactions in tests
---------------------

Shortly: it's way faster to roll back all the changes from database than to
recreate whole database from scratch on every new test.


Cooler fixtures
---------------

I really like the `fixtures <http://pytest.org/latest/yieldfixture.html>`__
that leverage Python's ``yield`` statement.

If using ``yield``, the above fixture example looks a lot clearer now:

.. code-block:: python

    import pytest

    @pytest.yieldfixture(scope="session")
    def db_connect(request):
        db = sql.connect()

        yield db

        # everything after yield statement works as a teardown code
        db.close()


Sewing it all together: Flask, |SA| and pytest
==============================================

Blah blah
