..  _NXinsertion_device:

##################
NXinsertion_device
##################

.. index::  ! classes - base_classes; NXinsertion_device

category
    base_classes

NXDL source:
    NXinsertion_device
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXinsertion_device.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXinsertion_device.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXinsertion_device
=====================================

::

    NXinsertion_device (base class, version 1.0)
      bandwidth:NX_FLOAT
      energy:NX_FLOAT
      gap:NX_FLOAT
      harmonic:NX_INT
      k:NX_FLOAT
      length:NX_FLOAT
      magnetic_wavelength:NX_FLOAT
      phase:NX_FLOAT
      poles:NX_INT
      power:NX_FLOAT
      taper:NX_FLOAT
      type:NX_CHAR
      spectrum:NXdata
      NXgeometry
    
