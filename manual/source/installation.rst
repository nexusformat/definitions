.. index::
   ! single: NAPI; installation
   see: installation; NAPI installation
   see: precompiled executable; NAPI installation
   see: binary executable; NAPI installation

.. _Installation:

Installation
############

.. index::
   single: NAPI; installation; download location
   see: download location; NAPI installation
   see: repository; NAPI installation

This section describes how to install the NeXus API and details the
requirements. The NeXus API is distributed under the terms of the 
`GNU Lesser General Public License version 3 <http://www.gnu.org/licenses/lgpl-3.0.txt>`_.

The source distribution of NAPI can be downloaded from the 
`release page of the associated GitHub project <https://github.com/nexusformat/code/releases>`_.
Instructions how to build the code can be found in the `INSTALL.rst` file
shipped with the source distribution.
In case you need help, feel free to contact the 
NeXus mailing list: http://lists.nexusformat.org/mailman/listinfo/nexus

.. _Installation-Binary:

Precompiled Binary Installation
*******************************


.. _Installation-Linux:

Linux RPM Distribution Kits
===========================

.. index::
   NAPI; installation; RPM
   see: RPM; NAPI installation

An installation kit (source or binary) can be downloaded from:
https://github.com/nexusformat/code/releases/tag/4.3.0

A NeXus binary RPM (nexus-\*.i386.rpm) contains ready compiled NeXus libraries whereas a
source RPM (nexus-\*.src.rpm) needs to be compiled into a binary RPM before it can be
installed. In general, a binary RPM is installed using the command

.. code-block:: bash

	rpm -Uvh file.i386.rpm

or, to change installation location from the default (e.g. /usr/local) area, using

.. code-block:: bash

	rpm -Uvh --prefix /alternative/directory file.i386.rpm

If the binary RPMS are not the correct architecture for you (e.g. you need x86_64 rather
than i386) or the binary RPM requires libraries (e.g. HDF4) that you do not have, you can
instead rebuild a source RPM (.src.rpm) to generate the correct binary RPM for you machine.
Download the source RPM file and then run

.. code-block:: bash

	rpmbuild --rebuild file.src.rpm

This should generate a binary RPM file which you can install as above. Be careful if
you think about specifying an alternative buildroot for rpmbuild by using
``--buildroot`` option as the "buildroot" directory tree will get remove (so
``--buildroot`` / is a really bad idea). Only change buildroot it if the default
area turns out not to be big enough to compile the package.

If you are using Fedora, then you can install all the dependencies by typing

.. code-block:: bash

	yum install hdf hdf-devel hdf5 hdf5-devel mxml mxml-devel

.. _Installation-Windows:

Microsoft Windows Installation Kit
==================================

.. index::
   NAPI; installation; Windows
   see: Microsoft Windows; NAPI installation
   see: Windows; NAPI installation

A Windows MSI based installation kit is available and can be downloaded from: 
https://github.com/nexusformat/code/releases/tag/4.3.0

.. _Installation-MacOS:

Mac OS X Installation Kit
=========================

.. index::
   NAPI; installation; Mac OS X
   see: Mac OS X; NAPI installation


An installation disk image (.dmg) can be downloaded from: 
https://github.com/nexusformat/code/releases/tag/4.3.0

.. _Installation-Source:

Source Installation
*******************

.. _Installation-Source-Generic:

NeXus Source Code Distribution
==============================

.. index::
   NAPI; installation; source distribution
   see: source distribution; NAPI installation

The source code distribution can be obtained from GitHub. One can either
checkout the git repositories to get access to the most recent development
code.  To clone the definitions repository use 

.. code-block:: bash

   $ git clone https://github.com/nexusformat/definitions.git definitions

or for the NAPI

.. code-block:: bash

   $ git clone https://github.com/nexusformat/code.git code

For release tarballs go to the release page for the 
`NAPI <https://github.com/nexusformat/code/releases>`_ or the 
`definitions <https://github.com/nexusformat/definitions/releases>`_.
For the definitions it is currently recommended to work directly with the 
Git repository as the actual release is rather outdated.

Instructions how to build the NAPI code can be found either on the 
GitHub project website or in the `README.rst` file shipped with the source
distribution.

.. index::
   ! release; NeXus definitions

.. _Releases:

Releases
********

The NeXus definitions are expected to evolve.
The evolution is marked as a series of *releases*
which are snapshots of the repository (and current
state of the NeXus standard).
Each new *release* of the definitions
will be posted to the definitions GitHub repository
and announced to the community via the
NeXus mailing list: :ref:`nexus@nexusformat.org<NeXus.mailinglist.main>`

NeXus definitions
=================

Releases of the NeXus definitions are listed on the GitHub web site:
https://github.com/nexusformat/definitions/releases

.. index:: release; notes

Release Notes
-------------

Detailed notes about each release (start with v3.3) are posted
to the definitions GitHub wiki:
https://github.com/nexusformat/definitions/wiki/Release-Notes

.. index:: release; process

Release Process
---------------

The process to make a new release of the NeXus definitions
repository is documented in the repository's GitHub wiki:
https://github.com/nexusformat/definitions/wiki/Release-Procedure.

The release process starts by creating a GitHub 
[Milestone](https://help.github.com/articles/tracking-the-progress-of-your-work-with-milestones/) 
for the new release.
Milestones for the NeXus definitions repository are
available on the GitHub site:
https://github.com/nexusformat/definitions/milestones

.. index:: release; versioning
.. index:: release; tags
.. index:: tags

.. version.tags_:

Versioning (Tags)
-----------------

Versioning of each of the NXDL files, as well as the 
complete set of NXDL files is now described in the wiki [#]_
of the NeXus definitions repository [#]_.  
Please see that wiki for complete information.

.. [#] Release Procedure: 
   https://github.com/nexusformat/definitions/wiki/Release-Procedure
.. [#] Definitions repository:
   https://github.com/nexusformat/definitions

-----------

In case you need help, feel free to contact the 
:ref:`NeXus.mailinglist.main`: 

:Archives:
   http://lists.nexusformat.org/mailman/listinfo/nexus
:email:
   nexus@nexusformat.org
