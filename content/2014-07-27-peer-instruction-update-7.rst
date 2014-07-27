Peer instruction: update 7
##########################

:tags: [peer instruction, javascript, mozilla, gsoc]
:date: 27.07.2014

I'm feeling terrible - I forgot to blog post last week.  Again.  I'll try to
make up for it...

Software Carpentry sprint summary
=================================

The sprint lasted two days (22-23 July 2014) and it was a blast!  Poland had
wonderful representation in Kraków, where I'm living.

Most of the group worked on Data Carpentry lessons:

* writing new in Excel or Python+Pandas
* checking existing in Bash

As far as I know, everything was merged in!  That's what I call a success.

I was the only person working on a different project, ie. on my Pitt.

Most of the time I was working alone, but once or twice we've got together with
Mozilla Paris to test some things.

I want to kindly thank Rémi Emonet and Raniere Silva for their help!  These
guys not only contributed feedback and bug reports, but also took part in
coordinated calls with me.  Thank you!

Having tested Pitt with Paris, I'm now more certain that the signalling part of
my application is now very close to being bug-free.  Or maybe it is already.
I'm really liking how easy it is to add new features and still be certain, that
the application won't break accidentally.

Pitt progress during sprint
===========================

Here's the list of everything that was achieved during the sprint:

* five hundred lines of documentation have been written
* fixed too high volume for the warning beep
* forced low video resolution
* dropped ``_pubsub`` part from directories or file names
* turned on TURN server for testing -- and successfully tested with Mozilla
  Paris

Exciting features coming
========================

For the next big update, I'm thinking about setting some huge goals.

1. Mobile-friendly interface (at least for tablets) and fixes for non-full-HD
   devices (https://github.com/pbanaszkiewicz/pitt/issues/18)
2. Testing (and fixing in case of errors) voice-only connections -- that's
   something I didn't get to test during the sprint
   (https://github.com/pbanaszkiewicz/pitt/issues/19)
3. Etherpad integration -- as far as I am concerned, Etherpad doesn't provide
   any way to share chat with other sites.  That's a bummer.  While I don't
   need Etherpad's content integration, shared chat would be extra nice.  This
   needs futher invesitagion (https://github.com/pbanaszkiewicz/pitt/issues/23)
4. Chat: if not possible to integrate with Etherpad, write our own
   (https://github.com/pbanaszkiewicz/pitt/issues/20)
5. Peer2Peer file sharing -- something exactly like ShareFest
   (https://github.com/pbanaszkiewicz/pitt/issues/21)
6. **Hard**: better broadcasting mesh (students act like relays / proxies),
   read more at https://github.com/pbanaszkiewicz/pitt/issues/22

I think the end of Google Summer of Code is nearing, but I like this project
a lot, and I definitely will continue working on it.