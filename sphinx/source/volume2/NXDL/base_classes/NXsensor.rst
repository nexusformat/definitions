..  _NXsensor:

########
NXsensor
########

.. index::  ! . NXDL base_classes; NXsensor

category:
    base_classes

NXDL source:
    NXsensor
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXsensor.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`, :ref:`NXlog`, :ref:`NXorientation`

symbol list:
    none

documentation:
    This class describes a sensor used to monitor an external condition
    - the condition itself is described in NXenvironment
    


.. rubric:: Basic Structure of **NXsensor**

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
    

.. rubric:: Comprehensive Structure of **NXsensor**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        