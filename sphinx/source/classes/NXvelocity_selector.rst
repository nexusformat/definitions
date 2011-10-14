..  _NXvelocity_selector:

###################
NXvelocity_selector
###################

.. index::  ! classes - base_classes; NXvelocity_selector

category
    base_classes

NXDL source:
    NXvelocity_selector
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXvelocity_selector.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXvelocity_selector.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXvelocity_selector
======================================

::

    NXvelocity_selector (base class, version 1.0)
      height:NX_FLOAT
      length:NX_FLOAT
      num:NX_INT
      radius:NX_FLOAT
      rotation_speed:NX_FLOAT
      spwidth:NX_FLOAT
      table:NX_FLOAT
      twist:NX_FLOAT
      type:NX_CHAR
      wavelength:NX_FLOAT
      wavelength_spread:NX_FLOAT
      width:NX_FLOAT
      geometry:NXgeometry
    
