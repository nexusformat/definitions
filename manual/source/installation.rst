.. index::
   ! single: NAPI; installation
   see: installation; NAPI installation
   see: precompiled executable; NAPI installation
   see: binary executable; NAPI installation

.. _Installation:

============
Installation
============

.. index::
   single: NAPI; installation; download location
   see: download location; NAPI installation
   see repository; NAPI installation

This section describes how to install the NeXus API and details the requirements. The NeXus API is distributed under the terms of the `GNU Lesser General Public License version 3 <http://www.gnu.org/licenses/lgpl-3.0.txt>`_.

The source code and binary versions for some popular platforms can be found on
http://download.nexusformat.org/kits/. Up to date instructions can be found on 
the :ref:`NeXus.wiki` Download page (http://www.nexusformat.org/Download).
In case you need help, feel free to contact the 
NeXus mailing list: http://lists.nexusformat.org/mailman/listinfo/nexus

.. _Installation-Binary:

Precompiled Binary Installation
###############################

.. _Installation-Prerequisites:

Prerequisites
=============

.. _Installation-Prerequisites-HDF:

.. index::
    see: binary format; file format
    file format; HDF
    HDF

HDF5/HDF4
---------

.. note:: HDF5 is the preferred format to use for NeXus.

NeXus uses HDF5 as the main underlying binary format.  
(HDF4 is supported as a legacy underlying binary format
but is not recommended for new use.)
It is necessary first to
install the HDF subroutine libraries and include files before compiling the NeXus API. It
is not usually necessary to download the HDF source code since precompiled object libraries
exist for a variety of operating systems including Windows, Mac OS X, Linux, and various
other flavors of Unix. Check the HDF web pages for more information: http://www.hdfgroup.org/

Packages for HDF4 and HDF5 are available for both Fedora (hdf, hdf5, hdf-devel,
hdf5-devel) and Ubuntu/Debian (libhdf4g, libhdf5).

.. _Installation-Prerequisites-XML:

.. index::
    file format; XML
    !XML; file format

XML
---

.. note:: XML is not the preferred format to use for NeXus.

The NeXus API also supports
using XML as a legacy underlying on-disk format. 
This uses the Mini-XML library, developed by
Michael Sweet, which is also available as a precompiled 
binary library for several operating
systems. Check the Mini-XML web pages
for more information: http://www.minixml.org/

Packages for MXML are available for both Fedora (mxml, mxml-devel) and Ubuntu/Debian
(libmxml1).

.. _Installation-Linux:

Linux RPM Distribution Kits
===========================

.. index::
   NAPI; installation; RPM
   see: RPM; NAPI installation

An installation kit (source or binary) can be downloaded from:
http://download.nexusformat.org/kits/

A NeXus binary RPM (nexus-\*.i386.rpm) contains ready compiled NeXus libraries whereas a
source RPM (nexus-\*.src.rpm) needs to be compiled into a binary RPM before it can be
installed. In general, a binary RPM is installed using the command

.. code-block:: guess

	rpm -Uvh file.i386.rpm

or, to change installation location from the default (e.g. /usr/local) area, using

.. code-block:: guess

	rpm -Uvh --prefix /alternative/directory file.i386.rpm

If the binary RPMS are not the correct architecture for you (e.g. you need x86_64 rather
than i386) or the binary RPM requires libraries (e.g. HDF4) that you do not have, you can
instead rebuild a source RPM (.src.rpm) to generate the correct binary RPM for you machine.
Download the source RPM file and then run

.. code-block:: guess

	rpmbuild --rebuild file.src.rpm

This should generate a binary RPM file which you can install as above. Be careful if
you think about specifying an alternative buildroot for rpmbuild by using
``--buildroot`` option as the "buildroot" directory tree will get remove (so
``--buildroot`` / is a really bad idea). Only change buildroot it if the default
area turns out not to be big enough to compile the package.

If you are using Fedora, then you can install all the dependencies by typing

.. code-block:: guess

	yum install hdf hdf-devel hdf5 hdf5-devel mxml mxml-devel

.. _Installation-Windows:

Microsoft Windows Installation Kit
==================================

.. index::
   NAPI; installation; Windows
   see: Microsoft Windows; NAPI installation
   see: Windows; NAPI installation

A Windows MSI based installation kit is available and can be downloaded from: 
http://download.nexusformat.org/kits/windows/

.. _Installation-MacOS:

Mac OS X Installation Kit
=========================

.. index::
   NAPI; installation; Mac OS X
   see: Mac OS X; NAPI installation


An installation disk image (.dmg) can be downloaded from: 
http://download.nexusformat.org/kits/macosx/

.. _Installation-Source:

Source Installation
###################

.. _Installation-Source-Generic:

NeXus Source Code Distribution
==============================

.. index::
   NAPI; installation; source distribution
   see: source distribution; NAPI installation

The build uses ``autoconf`` (so autools are required)
to determine what features will be available by your system.
You must have the *development* libraries installed
for all the file backends you want support for (see above).
If you intend to build more than the C language
bindings, you need to have the respective build support in a place where autoconf will pick them up
(i.e. python development files, a Java Development Kit, etc.).

For more information see the
README in the toplevel of the source distribution.
In case you need help, feel free to contact the 
:ref:`NeXus.mailinglist.main`: 

:Archives:
   http://lists.nexusformat.org/mailman/listinfo/nexus
:email:
   nexus@nexusformat.org

Download the appropriate gzipped tar file, unpack it, and run the standard configure
procedure from the resulting nexus directory. For example, for version 4.2.1;

.. code-block:: guess

	$ tar zxvf nexus-4.2.1.tar.gz
	$ cd nexus-4.2.1
	$ ./configure

To find out how to customize the installation, e.g., to choose different installation
directories, type

.. code-block:: guess

	$ ./configure --help

Carefully check the final output of the ``configure`` run. Make sure all features requested
are actually enabled.

.. code-block:: guess

	$ make
	$ make install

See the README file for further instructions.

.. _Installation-Source-Cygwin:

Cygwin Kits
===========

.. index::
   NAPI; installation; Cygwin
   see: Cygwin; NAPI installation


HDF4 is not supported under CYGWIN - both HDF5 and MXML are supported and can be
downloaded and built as usual. When configuring HDF5 you should explicitly pass a prefix to
the configure script to make sure the libraries are installed in a "usual" location
i.e.

.. code-block:: guess

	./configure --prefix=/usr/local/hdf5

Otherwise you will have to use the ``--with-hdf5=/path/to/hdf5`` option later when configuring NeXus to tell it where to look for hdf5.
After building hdf5, configure and build NeXus using the instructions for source code distribution above.
