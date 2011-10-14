..  _NXcollimator:

############
NXcollimator
############

.. index::  ! classes - base_classes; NXcollimator

category
    base_classes

NXDL source:
    NXcollimator
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXcollimator.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXcollimator.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`, :ref:`NXlog`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXcollimator
===============================

::

    NXcollimator (base class, version 1.0)
      absorbing_material:NX_CHAR
      blade_spacing:NX_FLOAT
      blade_thickness:NX_FLOAT
      divergence_x:NX_FLOAT
      divergence_y:NX_FLOAT
      frequency:NX_FLOAT
      soller_angle:NX_FLOAT
      transmitting_material:NX_CHAR
      type:NX_CHAR
      NXgeometry
      frequency_log:NXlog
    
