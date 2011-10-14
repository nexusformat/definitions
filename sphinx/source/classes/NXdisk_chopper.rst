..  _NXdisk_chopper:

##############
NXdisk_chopper
##############

.. index::  ! classes - base_classes; NXdisk_chopper

category
    base_classes

NXDL source:
    NXdisk_chopper
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXdisk_chopper.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXdisk_chopper.nxdl.xml 829 2011-02-20 15:04:56Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXdisk_chopper
=================================

::

    NXdisk_chopper (base class, version 1.0)
      distance:NX_FLOAT
      pair_separation:NX_FLOAT
      phase:NX_FLOAT
      radius:NX_FLOAT
      ratio:NX_INT
      rotation_speed:NX_FLOAT
      slit_angle:NX_FLOAT
      slit_height:NX_FLOAT
      slits:NX_INT
      type:NX_CHAR
      wavelength_range:NX_FLOAT[2]
      NXgeometry
    
