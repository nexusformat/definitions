..  _NXbeam:

######
NXbeam
######

.. index::  ! classes - base_classes; NXbeam

category
    base_classes

NXDL source:
    NXbeam
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXbeam.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXbeam.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXbeam
=========================

::

    NXbeam (base class, version 1.0)
      distance:NX_FLOAT
      energy_transfer:NX_FLOAT[i]
      final_beam_divergence:NX_FLOAT[2,j]
      final_energy:NX_FLOAT[i]
      final_polarization:NX_FLOAT[2,j]
      final_wavelength:NX_FLOAT[i]
      final_wavelength_spread:NX_FLOAT[i]
      flux:NX_FLOAT[i]
      incident_beam_divergence:NX_FLOAT[2,j]
      incident_energy:NX_FLOAT[i]
      incident_polarization:NX_FLOAT[2,j]
      incident_wavelength:NX_FLOAT[i]
      incident_wavelength_spread:NX_FLOAT[i]
      NXdata
    
