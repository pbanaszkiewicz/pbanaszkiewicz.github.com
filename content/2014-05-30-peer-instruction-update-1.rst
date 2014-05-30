Peer instruction: update 1
##########################

:tags: [peer instruction, javascript, mozilla, gsoc]
:date: 30.05.2014

I always avoided JavaScript.  With my long exposure to Python, JS never
appealed to me.  And yet my whole Google Summer of Code project consists
mainly of JS.

Let me quickly reintroduce basic ideas and plans for Peer Instruction project.

Peer instruction concepts
=========================

The most important feature of Peer Instruction is the ability to, from the
technical point of view, quickly switch between teacher and student modes.

Teacher's mode
--------------

Teacher mode is basicly a broadcast sent to every student in a classroom.  This
might be quite challenging: you can have many direct connections and suffer
from capped bandwidth and high CPU usage.

.. figure:: http://i.imgur.com/ZRhkiWq.png
    :alt: Teacher broadcasts their stream to multiple students
    :align: center
    :target: http://imgur.com/ZRhkiWq

    Teacher broadcasts their stream to multiple students.

The solution is to introduce additional server that helps to "spread" the
stream to multiple students.  It essentially looks like this:

.. figure:: http://i.imgur.com/QP13jQQ.png
    :alt: Teacher broadcasts their stream to multiple students through Multipoint Control Unit
    :align: center
    :target: http://imgur.com/QP13jQQ

    Teacher broadcasts their stream to multiple students through Multipoint
    Control Unit.

What's really good about this design?  There's an excellent open-source MCU
available: `Licode`_.  I must admit Licode is a little too complicated to set
up, but authors' support and continuous development make it a great option if
someone wants, for example, to host their own alternative to Google Hangouts or
Skype.

.. _Licode: http://lynckia.com/licode/

.. figure:: http://i.imgur.com/CNGCY7S.png
    :alt: Me testing teacher's mode
    :align: center
    :target: http://imgur.com/CNGCY7S

    Me testing teacher's mode.  (I was suprised it worked!)

As you can see above, the interface is pretty simple, but it works (at least
for 1 student).  I have yet to test it for more students, but I haven't
received a server account at Mozilla to do so.

Student's mode
--------------

This is the second mode of broadcasting.  A very crucial from the point of
science of peer instruction.

In this mode students are split into smaller groups so that they can talk with
each other.

Right now I'm thinking how to implement this mode.  One of the ideas is to
create one `Erizo Room`_ for every group of students.

.. _Erizo Room: http://lynckia.com/licode/client-api.html#room

The way events are propagated within Erizo makes it really easy to subscribe to
other students' streams within one particular room.  Using multiple rooms also
helps manage all these smaller groups.

I should also mention that Erizo can create "full MCU" rooms - ie. rooms where
streams are going through the server - and Peer-to-Peer rooms, where the server
only handles sessions, signalling and events, but the streams are actually
transferred between the room participants.

I think for small groups of 2-4 students it's a good idea to use P2P rooms and
save resources on the server.

Unfortunately, this solution has some drawbacks, too.  I found out that Erizo
can only handle so much rooms at once (it's specified in configuration, but I
don't know the retionale behind it).

Current issues
==============

My main focus for next week(s) is working PoC of students mode.  Right now I'm
working on a protocol used by Licode events.

It's possible to send data through Erizo streams.  I want to use this "channel"
to communicate with students' browsers.

For now I'll only send data like "join room ABC for small group discussion" and
"leave room ABC".  In future Peer Instruction might be more advanced - quite
important feature is chat, and I will likely leverage the existing protocol
for that.

Anyway, that's the update status on my project.  I highly welcome any
contribution or comments.

Here's project GIT repository: https://github.com/pbanaszkiewicz/peer-instruction