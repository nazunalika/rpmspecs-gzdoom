rpmspecs-gzdoom
^^^^^^^^^^^^^^^

This is the RPM spec files that I have created for gzdoom. I am not affiliated with the gzdoom project and only provide this as a service.

.. contents::

Information
-----------

**Note:** I am not responsible for system damages, break-ins, or faulty code of the software that can cause the formerly listed. Always develop and test in an isolated environment at all times. **Always keep SELinux enabled.**

**Note:** 32 bit builds have been disabled. Please use 64 bit. Arm builds are now supported: AARCH64

Frequently Asked Questions
--------------------------

Do you have any SRPMS available?
++++++++++++++++++++++++++++++++

They'll normally be available from my copr builds, if you are interested in making changes and using mock for yourself.

Have any documentation or guides?
+++++++++++++++++++++++++++++++++

If you're starting out rpm packaging, please consider reading the following documentation. The packaging guidelines may seem strict, but they are deemed best practices if you are considering on being a package maintainer (sponsored or not). Keep in mind, **I am always learning**. I am in no way an expert, nor do I claim to be.

`FHS <http://www.pathname.com/fhs/>`_

`Fedora: Fedora Packaging Guidelines <https://docs.fedoraproject.org/en-US/packaging-guidelines/>`_

`Fedora: Creating RPM Packages <https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_GNU_Hello/>`_

What you should get from the above is there are specific guidelines that should be followed, for maintainability, portability, and easy review. My RPM specs will have an FAQ of the "purpose". 

Do you have any repositories?
+++++++++++++++++++++++++++++

Yes, I do.

`Copr <https://copr.fedorainfracloud.org/coprs/nalika/>`_

Do you take requests?
+++++++++++++++++++++

I normally don't. But, if what you're asking for doesn't have an RPM or project in copr, I'll consider it based on what it is, and if it fits licensing and guidelines. You can drop me an email or a line here and I will get back to you.

Do you package for other systems?
+++++++++++++++++++++++++++++++++

At this present time, I do not. I have considered packaging for OpenSUSE. However OpenSUSE, much like Arch, already have plenty of maintainers with tons upon tons of packages (up to date or not) and their own build systems similar to Fedora. So some of the packages you may see here may already exist for those distributions in base or extra repositories they provide. The COPR build system does support OpenSUSE now, so it may end up being a viable option in the future.

Presently, this does not build in copr for OpenSUSE, simply because dependencies are not in the SUSE base. I do not have a way to extend copr to the additional repositories.

.. rubric:: Footnotes

.. [#f1] https://wiki.centos.org/About/Product
