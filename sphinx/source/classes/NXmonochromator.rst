..  _NXmonochromator:

###############
NXmonochromator
###############

.. index::  ! classes - base_classes; NXmonochromator

category
    base_classes

NXDL source:
    NXmonochromator
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXmonochromator.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXmonochromator.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcrystal`, :ref:`NXdata`, :ref:`NXgeometry`, :ref:`NXvelocity_selector`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXmonochromator
==================================

::

    NXmonochromator (base class, version 1.0)
      energy:NX_FLOAT
      energy_error:NX_FLOAT
      wavelength:NX_FLOAT
      wavelength_error:NX_FLOAT
      NXcrystal
      distribution:NXdata
      geometry:NXgeometry
      NXvelocity_selector
    
