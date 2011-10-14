..  _NXsensor:

########
NXsensor
########

.. index::  ! classes - base_classes; NXsensor

category
    base_classes

NXDL source:
    NXsensor
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXsensor.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXsensor.nxdl.xml 829 2011-02-20 15:04:56Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`, :ref:`NXlog`, :ref:`NXlog`, :ref:`NXlog`, :ref:`NXorientation`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXsensor
===========================

::

    NXsensor (base class, version 1.0)
      attached_to:NX_CHAR
      external_field_brief:NX_CHAR
      high_trip_value:NX_FLOAT
      low_trip_value:NX_FLOAT
      measurement:NX_CHAR
      model:NX_CHAR
      name:NX_CHAR
      run_control:NX_BOOLEAN
      short_name:NX_CHAR
      type:NX_CHAR
      value:NX_FLOAT[n]
      value_deriv1:NX_FLOAT[]
      value_deriv2:NX_FLOAT[]
      geometry:NXgeometry
      value_log:NXlog
      value_deriv1_log:NXlog
      value_deriv2_log:NXlog
      external_field_full:NXorientation
    
