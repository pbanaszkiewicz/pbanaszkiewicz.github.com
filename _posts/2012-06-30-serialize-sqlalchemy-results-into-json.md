---
layout: post
title: Serialize SQLAlchemy query results to JSON
slug: serialize-sqlalchemy-results-into-json
tags: [python, sqlalchemy, flask, json]
date: 30.06.2012
---

Consider you have following model and you want to create super---duper
RESTful interface to it.

{% highlight python %}
from application.database import db

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.Text)
{% endhighlight %}

And here's one of your views, which returns all the available blog
posts:

{% highlight python %}
from flask import jsonify
from application.models import BlogPost

@app.route("/posts")
def blog_posts():
    return jsonify(posts=list(BlogPost.query.all()))
{% endhighlight %}

But unfortunately SQLAlchemy results cannot be serialized to JSON. What
to do?

<div class="message">
    <h3>Note</h3>
    Recently a great Python project for serialization surfaced:
    <a href="https://marshmallow.readthedocs.org/en/latest/">Marshmallow</a>.
    It is ORM / framework agnostic, so with very little effort should work with
    your SQLAlchemy project!
</div>

You can spend some time and extend SQLAlchemy's pickle serializer
extension (it's awkward to extend what's already extended, but
nevermind), however there's a quicker way. Just make your model class
inherit from this base class as well:

{% highlight python %}
from collections import OrderedDict

class DictSerializable(object):
    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result
{% endhighlight %}

`simplejson` looks for `_asdict()` method when iterating through objects
to be serialized. We can cheat and return our model and its fields as an
ordered dictionary, which is then easily parsed to JSON.

This might not be the quickest method, but certainly is the easiest one.
