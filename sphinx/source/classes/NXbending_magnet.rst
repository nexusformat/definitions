..  _NXbending_magnet:

################
NXbending_magnet
################

.. index::  ! classes - base_classes; NXbending_magnet

category
    base_classes

NXDL source:
    NXbending_magnet
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXbending_magnet.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXbending_magnet.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXbending_magnet
===================================

::

    NXbending_magnet (base class, version 1.0)
      accepted_photon_beam_divergence:NX_FLOAT
      bending_radius:NX_FLOAT
      critical_energy:NX_FLOAT
      divergence_x_minus:NX_FLOAT
      divergence_x_plus:NX_FLOAT
      divergence_y_minus:NX_FLOAT
      divergence_y_plus:NX_FLOAT
      magnetic_field:NX_FLOAT
      source_distance_x:NX_FLOAT
      source_distance_y:NX_FLOAT
      spectrum:NXdata
      NXgeometry
    
