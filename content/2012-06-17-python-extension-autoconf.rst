Python extension and './configure'
##################################

:slug: python-extension-autoconf
:tags: [compilation, configure, distutils, extension, python, rrdtool]
:date: 17.06.2012

Recently I have been working on
`python-rrdtool <https://github.com/pbanaszkiewicz/python-rrdtool>`_ Python
binding to rrdtool utility.

On PyPI there has already existed ``py-rrdtool`` package, but it did not work
at all.

It turned out, that ``rrdtool`` sources had a nice looking ``rrdtoolmodule.c``,
all I needed was to compile it.

Long story short: ``rrdtoolmodule.c`` includes a non-existent header, which is
created during ``./configure`` run. So I had to figure out how to call
``./configure`` from inside ``setup.py`` script.

(You may take a look at actual
`setup.py <https://github.com/pbanaszkiewicz/python-rrdtool/blob/master/setup.py>`_
instead of reading this blog post.)

.. sourcecode:: python

    from distutils.core import setup, Command
    from distutils.command.build_ext import build_ext
    ...
    setup(
        ...
        cmdclass={"build_configure": BuildConfigure, "build_ext": BuildExtension},
        ...
    )

In order to run ``./configure`` at specific moment before your module is being
built, you have to use distutils command extensions: ``build_configure`` and
``build_ext``.

.. sourcecode:: python

    class BuildConfigure(Command):
        def run(self):
            # run `./configure` here, I did it using subprocess module
            ...

``BuildConfigure`` class has to call the ``configure`` executable. But this
class is not enough, distutils requires special building extension.

.. sourcecode:: python

    class BuildExtension(build_ext):
        def run(self):
            for cmd_name in self.get_sub_commands():
                self.run_command(cmd_name)

            build_ext.run(self)

        sub_commands = [("build_configure", None)] + build_ext.sub_commands

I override ``run`` method to explicitly run our commands. In ``sub_commands``
list of 2-element tuples, first element stays for command extension, and
second for usage circumstances (None == always, function == depending on it's
boolean output).

**Note**: if you happen to see "permission error" somewhere, make sure that
you set chmods for ``configure`` executable:

.. sourcecode:: python

    os.chmod(executable, 0777)
