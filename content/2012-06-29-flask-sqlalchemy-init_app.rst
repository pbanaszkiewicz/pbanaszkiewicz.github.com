Flask and SQLAlchemy: init_app
##############################

:slug: flask-sqlalchemy-init_app
:tags: [python, flask, sqlalchemy]
:date: 29.06.2012

I've been recently refactoring my Flask application and one of the most
important changes I've made was
`an application factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_.
You can find out many different (but similar) syntax constructions to use
SQLAlchemy with it. Here one and most common:

.. sourcecode:: python

    from flask import Flask
    from flask.ext.sqlalchemy import SQLAlchemy
    db = SQLAlchemy()
    def create_app():
        app = Flask(__name__)
        db.init_app(app)
        db.create_all()
        return app

However, you might stumple upon this exception: ``RuntimeError: application
not registered on db instance and no application bound to current context``,
perhaps in your tests on during ``db.create_all()``.

Documentation isn't that clear on that matter. After a lot of searching I
found out three options to solve this issue.

Option #1
~~~~~~~~~

Create your ``db`` object with ``app`` as a parameter:

.. sourcecode:: python

    def create_app():
        app = Flask(__name__)
        db = SQLAlchemy(app)
        db.create_all()
        return app

The drawback is that you don't have a global ``db`` object and thus your
blueprints won't work. And you won't be able to easily create models.

(BTW: setting ``global db`` and then ``db = SQLAlchemy(app)`` did not work
for me.)

Option #2
~~~~~~~~~

Assign created application to ``db.app``:

.. sourcecode:: python

    db = SQLAlchemy()
    def create_app():
        app = Flask(__name__)
        db.init_app()
        db.app = app
        db.create_all()
        return app

The possible drawback: you might mess something up in ``db``'s internals. You
don't want that, do you?

Option #3
~~~~~~~~~

Call ``db.create_all()`` (that's the thing we had troubles with) within
application context:

.. sourcecode:: python

    db = SQLAlchemy()
    def create_app():
        app = Flask(__name__)
        db.init_app()
        with app.test_request_context():
            db.create_all()
        return app

The drawback: it's ``test_request_context`` (test!). But, after all, it works
fine for me. And all my tests pass! ;)

Use any method you want.

If you had this issue and you solved it another way, please let me know in the
comments.

Additional tips
~~~~~~~~~~~~~~~

You will need to import models themselves before issuing ``db.create_all``:

.. sourcecode:: python

    with app.test_request_context():
        from application.models import Post
        db.create_all()

It's a good idea to keep your ``SQLAlchemy`` object instance in separate
file, to avoid circular imports:

.. sourcecode:: python

    # application/database.py
    from flask.ext.sqlalchemy import SQLAlchemy
    db = SQLAlchemy()

    # application factory
    from application.database import db
    def create_app():
        ...
        db.init_app(app)
        ...

    # application/models.py
    from application.database import db
    class Post(db.Model):
        ...
