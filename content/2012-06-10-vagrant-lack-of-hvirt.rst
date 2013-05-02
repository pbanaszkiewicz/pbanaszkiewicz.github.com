Thing about Vagrant, VirtualBox and lack of hardware virtualization
###################################################################

:slug: vagrant-lack-of-hvirt
:tags: [hardware, vagrant, virtualbox, virtualization]
:date: 10.06.2012

If you don't have a very modern computer with CPU supporting
`hardware virtualization <http://en.wikipedia.org/wiki/X86_virtualization>`_,
like me, and you want to use Vagrant, you'll likely have lots of issues.

**TL;DR**: you'd better buy a new PC. Hardware virtualization is a must-have
nowadays.

In case you don't want to buy it, here's some issues I had with Vagrant and
how I fixed them.

VM can't be started (even through VirtualBox GUI) due to "VT-x is not available".
==================================================================================

**Solution**: In this GUI select VM → Settings → System → Acceleration, then
uncheck everything.

-------------

Acceleration tab is not active.
===============================

**Solution**: Go to the directory containing your VirtualBox VMs, then to your
VM's directory, then edit ``*.vbox`` XML file. Within ``<CPU>`` tag children
(like ``<HardwareVirtEx>`` or ``<PAE>``), replace every ``enabled="true"``
with ``enabled="false"``.

-------------

I can do that all with Vagrantfile and do not need to change my ``*.vbox`` config!
==================================================================================

**Solution**: Even though you can turn hardware virtualization off via
Vagrantfile (``config.vm.customize ["modifyvm", :id, "--hwvirtex", "off"]``),
it might not work. At least it didn't in my case. If it does the same for you,
go and change your ``*.vbox`` XML file.

-------------

Still not working. What can be wrong?
=====================================

**Solution**: Check if number of CPUs for your Vagrant virtual machine is
greater than 1. If so, go and change the ``count`` of CPUs in your ``*.vbox``
file to one. (Yes, you could do it from Vagrantfile, but it may not work. It
did not in my case.)
