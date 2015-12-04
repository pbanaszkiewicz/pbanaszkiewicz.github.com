---
layout: post
title: "How to bite Flask, SQLAlchemy and pytest all at once"
slug: how-to-bite-flask-sqlalchemy-and-pytest-all-at-once
tags: [Python, pytest, Flask, SQLAlchemy, good practices]
date: 22.02.2014
---

As a person who started with [Django], I had some hard time figuring out how
application and request contexts work in [Flask]. I think I finally got to
understand them. I also learnt how to use [SQLAlchemy]'s scoped sessions
properly and how to test my REST applications with [pytest] efficiently.

Here's what I got to know, split into topics.

{:.message}
**Warning**: [Flask] and [SQLAlchemy] are very flexible, compared to
[Django]. This article presents only one approach out of many on how to deal
with thread-local stuff in your code. But I think that it's one of the best
approaches.

{:.toc}
1. [How does SQLAlchemy handle sessions](#how-does-sqlalchemy-handle-sessions)
    1. [Scoped sessions](#scoped-sessions)
2. [Transactions in SQLAlchemy](#transactions-in-sqlalchemy)
3. [What are Flask ap­pli­ca­tion and request contexts](#what-are-flask-application-and-request-contexts)
    1. [Ap­pli­ca­tion context](#application-context)
    2. [Request context](#request-context)
4. [Zipping Flask request contexts and SQLAlchemy scoped sessions together](#zipping-together)
5. [Testing everything](#testing-everything)
    1. [Fixtures](#fixtures)
    2. [Fixture scope](#fixture-scope)
    3. [Trans­ac­tions in tests](#transactions-in-tests)
    4. [Cooler fixtures](#cooler-fixtures)
6. [Sewing it all together: Flask, SQLAlchemy and pytest](#sewing-together)
    1. [Actual ap­pli­ca­tion](#actual-application)
    2. [Tests with pytest](#tests-with-pytest)
    3. [Boil­er­plate](#boilerplate)

How does SQLAlchemy handle sessions
-----------------------------------

Your SQLAlchemy `Session` is the main place where you usually talk to
your database.

{% highlight python %}
# somewhere globally in your application
from sqlalchemy.orm import sessionmaker
session = sessionmaker()

# somewhere in your views
users = session.query(User).filter(User.name == "Piotr").all()
{% endhighlight %}

This code is perfectly fine **if used non-concurrently**.
Non-concurrently, that means only one user can use session at once; that
means, only one user connects to your website at once.

In reality that's not always a case. I bet you *want* your site to be
safely accessible by many users all at once.

If so, then you can't use `sessionmaker` alone. [It's not
designed](http://docs.sqlalchemy.org/en/rel_0_9/orm/session.html#is-the-session-thread-safe)
to create safe `Session` objects for multiple threads.

So what's the solution? It's actually pretty clever. It's called *scoped
sessions*: sessions, that are bound to the specific "scope" of your
application, for example: the scope of one user's connection.

{:.message}
**Notes**: "Scoped sessions" is a different programming pattern than
`sessionmaker`. The former is a
[registry pattern](http://martinfowler.com/eaaCatalog/registry.html),
whereas the latter is a
[factory](https://en.wikipedia.org/wiki/Factory_method_pattern).

### Scoped sessions

It's quite easy to understand how session for application scope is being
constructed. For every incoming request, a different `Session` object is
being served.

So user *Mark* gets *session A*, user *Ellen* gets *session B* and user
*Sam* gets *session C*. The key is that all these sessions are
accessible in your code via the very same line:

{% highlight python %}
# somewhere globally in your application
from sqlalchemy.orm import scoped_session, sessionmaker
session = scoped_session(sessionmaker())

# somewhere in your views
users = session.query(User).filter(User.name == "Piotr").all()
{% endhighlight %}

(Look at the previous snippet; they're almost the same!)

All the required setup is this one little object, [scoped_session].
You feed it with some session-factory-maker, like `sessionmaker`, and
voilà.

There's only one part missing... how does scoped session know when to
"spawn" a different session? It somehow has to recognize that a new user
is requesting your views.

I'll come back to that in later after explaining what are Flask
application and request contexts and how to work with them.

Transactions in SQLAlchemy
--------------------------

SQLAlchemy supports at least two different kinds of transactions. The
most popular type is [Session based
transaction](http://docs.sqlalchemy.org/en/rel_0_9/orm/session.html#committing):

{% highlight python %}
u1 = User(name="Piotr", email="test@example.org")
session.add(u1)
try:
    session.commit()
except sqlalchemy.exc.IntegrityError:
    session.rollback()
{% endhighlight %}

The [second
type](http://docs.sqlalchemy.org/en/rel_0_9/core/connections.html#using-transactions)
is more superior. It can roll back even committed session changes! It's
really powerful for testing purposes.

What are Flask application and request contexts
-----------------------------------------------

### Application context

I like to think about Flask application context as being bound to one
thread of your actual application (website). That context might be a set
of global objects, like database connection and app settings. These
objects should only exist once per your application, right? (I don't see
a point in duplicating app settings or database connections all over the
place).

{:.message}
**Note**: SQLAlchemy provides a
[pool of connections](http://docs.sqlalchemy.org/en/latest/core/pooling.html)
to the database. You can pop a connection any time and push it back after
you're done. This, however, doesn't mean you have to pop two or more
connections at once!

In Flask,
[current\_app](http://flask.pocoo.org/docs/api/#flask.current_app) is
aware of the active application context. If you have your web
application running on two threads, and one user accesses the first
thread, they'll use different Flask application than the other user
accessing second thread.

### Request context

Request context is very similar to the application context. Every time
anyone goes to some page on your site (ie. sends request), a new context
is created.

This new context holds information that should only be available within
that particular second when the user is being served. *I'm assuming you
can serve your user within one second :)*

For example, imagine you have a view that adds a new blog post to your
site:

{% highlight python %}
@app.route("/blogpost". methods=["POST", ])
def blogpost_view():
    return "New blog post: {}".format(request.form)
{% endhighlight %}

Flask internals ensure that you **do not** access a different request's
data. Two requests may be simultaneous, yet you will access exactly the
correct request in your code.

{:.message}
**Note**: New request context creates new application context, if the latter is
not available.

Zipping Flask request contexts and SQLAlchemy scoped sessions together {#zipping-together}
----------------------------------------------------------------------

So now you know what powers Flask contexts and that you should choose
scoped SQLAlchemy sessions over "normal" ones. But how to make a
`scoped_session` that works *with* Flask contexts?

Take a closer look at [scoped_session].  You can see it has a
[scopefunc](http://docs.sqlalchemy.org/en/latest/orm/session.html#sqlalchemy.orm.scoping.scoped_session.params.scopefunc)
argument:

> `scopefunc` – optional function which defines the current scope. If
> not passed, the `scoped_session` object assumes "thread-local" scope,
> and will use a Python `threading.local()` in order to maintain the
> current `Session`. If passed, the function should return a hashable
> token; this token will be used as the key in a dictionary in order to
> store and retrieve the current `Session`.

So... `scopefunc` has to unambiguously represent each individual
context. I was looking for a good way of handling that, and found one in
[Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/). This
[Flask] extension
[uses](https://github.com/mitsuhiko/flask-sqlalchemy/blob/d4560013c1c51ef035381e35dd42a1628bb212ee/flask_sqlalchemy/__init__.py#L665)
internal context stack to build hashable context tokens. The code looks
like this:

{% highlight python %}
# somewhere globally in your application
from flask import _app_ctx_stack
from sqlalchemy.orm import scoped_session, sessionmaker
session = scoped_session(sessionmaker(),
                         scopefunc=_app_ctx_stack.\_\_ident_func__)
{% endhighlight %}

Testing everything
------------------

Because of the aforementioned flexibility that [Flask] and [SQLAlchemy] have,
I had really hard time figuring how to test the whole thing. **Testing is very
important**, and with the help of wonderful Python libraries like
[pytest] it actually becomes a pleasure.

Still, when trying out [pytest] for a first time, there is a small learning
curve if you come from Java-based
[unittest](http://docs.python.org/3/library/unittest.html#module-unittest)
world.

The biggest change is in the ideology: now you don't have to write
classes (test cases) to test your code. You can write **a lot simpler**
functions instead.

The important feature of [pytest] is
[fixtures](http://pytest.org/latest/fixture.html). Use them when you want to
set up or tear down your tests.

### Fixtures

A fixture is a function that, for example, returns a database session
object, which can be leveraged by your tests.

Or it can return a file descriptor to the file in `/tmp/random_name`. Or
your application object. Or Redis connection object.

Look at [fixtures](http://pytest.org/latest/fixture.html) docs for more
examples.

### Fixture scope

Every fixture can be set for a `session` scope, `module` scope, or
`function` scope. This means, that the fixture is **only run once** per
testing session, or once per whole module (containing tests), or once
for every test function.

Take for example this `db_connect` fixture.

{% highlight python %}
import pytest

@pytest.fixture(scope="session")
def db_connect(request):
    db = sql.connect()

    def teardown():
        db.close()

    # There's no "add_teardown", see comments below
    # request.add_teardown(teardown)
    request.addfinalizer(teardown)

    return db
{% endhighlight %}

It's dumb and won't work, but I hope you get the gist. Even if you have
a thousand tests that use this fixture, it will be invoked only once,
then memorized (cached).

{:.message}
**Note**: This small fixture uses another fixture!
[request](http://pytest.org/latest/builtin.html#_pytest.python.FixtureRequest)
is a built-in pytest fixture that helps you with teardowns.

I suggest to (at least) create a session-scoped fixture that builds your
Flask application object (using
[application factory](http://flask.pocoo.org/docs/patterns/appfactories/)),
and a session-scoped fixture that builds your SQLAlchemy session and manages
transactions.

### Transactions in tests

Shortly: it's way faster to roll back all the changes from database than
to recreate whole database from scratch on every new test.

### Cooler fixtures

I really like the [fixtures](http://pytest.org/latest/yieldfixture.html)
that leverage Python's `yield` statement.

With `yield`, the above fixture example looks a lot clearer now:

{% highlight python %}
import pytest

@pytest.yieldfixture(scope="session")
def db_connect(request):
    db = sql.connect()

    yield db

    # everything after yield statement works as a teardown code
    db.close()
{% endhighlight %}

Sewing it all together: Flask, SQLAlchemy and pytest {#sewing-together}
----------------------------------------------------

### Actual application

1.  Use
    [application factory](http://flask.pocoo.org/docs/patterns/appfactories/)
    to easily create Flask application object. This will be used in
    different parts of your codebase, like tests or dev server.
2.  Create global [scoped_session] object that spawns actual SQLAlchemy
    sessions when accessed. Use `scopefunc` keyword argument to provide
    hashable function that's used to recognize context switches.
3.  Don't bind that `scoped_session` object to any engine yet. Bind it
    in your application factory using
    [scoped\_session.configure()](http://docs.sqlalchemy.org/en/rel_0_9/orm/session.html#sqlalchemy.orm.scoping.scoped_session.configure).
4.  During `app.teardown_appcontext`
    [remove](http://docs.sqlalchemy.org/en/rel_0_9/orm/session.html#sqlalchemy.orm.scoping.scoped_session.remove)
    database sessions.

### Tests with pytest

This one's more complicated, so I'll paste some boilerplate below.

1.  In your `conftest.py` prepare one session-scoped fixture that
    creates your app (using factory), creates all the tables,
    explicitely pops a connection, binds global `scoped_session` to that
    connection and yields that app
2.  Prepare second fixture, that creates a new transaction, new
    application context and yields database session.

### Boilerplate

Here's that promised boilerplate. First application factory
`create_app`:

{% highlight python %}
# database session registry object, configured from
# create_app factory
DbSession = scoped_session(
    sessionmaker(),
    # __ident_func__ should be hashable, therefore used
    # for recognizing different incoming requests
    scopefunc=_app_ctx_stack.\_\_ident_func__
)

def create_app(name_handler, config_object):
    """
    Application factory

    :param name_handler: name of the application.
    :param config_object: the configuration object.
    """
    app = Flask(name_handler)
    app.config.from_object(config_object)
    app.engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

    global DbSession
    # BaseQuery class provides some additional methods like
    # first_or_404() or get_or_404() -- borrowed from
    # mitsuhiko's Flask-SQLAlchemy
    DbSession.configure(bind=app.engine, query_cls=BaseQuery)

    @app.teardown_appcontext
    def teardown(exception=None):
        global DbSession
        if DbSession:
            DbSession.remove()

    return app
{% endhighlight %}

And test configuration from `conftest.py`:

{% highlight python %}
from your_application.global import create_app, DbSession

@pytest.yield_fixture(scope="session")
def app():
    """
    Creates a new Flask application for a test duration.
    Uses application factory `create_app`.
    """
    _app = create_app("testingsession", config_object=TestConfig)

    # Base is declarative_base()
    Base.metadata.create_all(bind=_app.engine)
    _app.connection = _app.engine.connect()

    # No idea why, but between this app() fixture and session()
    # fixture there is being created a new session object
    # somewhere.  And in my tests I found out that in order to
    # have transactions working properly, I need to have all these
    # scoped sessions configured to use current connection.
    DbSession.configure(bind=_app.connection)

    yield _app

    # the code after yield statement works as a teardown
    _app.connection.close()
    Base.metadata.drop_all(bind=_app.engine)


@pytest.yield_fixture(scope="function")
def session(app):
    """
    Creates a new database session (with working transaction)
    for a test duration.
    """
    app.transaction = app.connection.begin()

    # pushing new Flask application context for multiple-thread
    # tests to work
    ctx = app.app_context()
    ctx.push()

    session = DbSession()

    yield session

    # the code after yield statement works as a teardown
    app.transaction.close()
    session.close()
    ctx.pop()
{% endhighlight %}

  [Flask]: http://flask.pocoo.org/
  [SQLAlchemy]: http://docs.sqlalchemy.org/
  [Django]: https://www.djangoproject.com/
  [pytest]: http://pytest.org/latest/
  [scoped_session]: http://docs.sqlalchemy.org/en/latest/orm/session.html#sqlalchemy.orm.scoping.scoped_session
