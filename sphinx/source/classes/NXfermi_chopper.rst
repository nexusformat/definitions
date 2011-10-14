..  _NXfermi_chopper:

###############
NXfermi_chopper
###############

.. index::  ! classes - base_classes; NXfermi_chopper

category
    base_classes

NXDL source:
    NXfermi_chopper
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXfermi_chopper.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXfermi_chopper.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXfermi_chopper
==================================

::

    NXfermi_chopper (base class, version 1.0)
      absorbing_material:NX_CHAR
      distance:NX_FLOAT
      energy:NX_FLOAT
      height:NX_FLOAT
      number:NX_INT
      r_slit:NX_FLOAT
      radius:NX_FLOAT
      rotation_speed:NX_FLOAT
      slit:NX_FLOAT
      transmitting_material:NX_CHAR
      type:NX_CHAR
      wavelength:NX_FLOAT
      width:NX_FLOAT
      NXgeometry
    
