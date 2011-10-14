..  _NXroot:

######
NXroot
######

.. index::  ! classes - base_classes; NXroot

category
    base_classes

NXDL source:
    NXroot
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXroot.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXroot.nxdl.xml 866 2011-07-19 12:46:16Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXentry`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXroot
=========================

::

    NXroot (base class, version 1.0)
      @NX_class
      @file_time
      @file_name
      @file_update_time
      @NeXus_version
      @HDF_version
      @HDF5_Version
      @XML_version
      @creator
      NXentry
    
