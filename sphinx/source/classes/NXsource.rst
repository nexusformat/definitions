..  _NXsource:

########
NXsource
########

.. index::  ! classes - base_classes; NXsource

category
    base_classes

NXDL source:
    NXsource
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXsource.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXsource.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdata`, :ref:`NXdata`, :ref:`NXgeometry`, :ref:`NXnote`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXsource
===========================

::

    NXsource (base class, version 1.0)
      bunch_distance:NX_FLOAT
      bunch_length:NX_FLOAT
      current:NX_FLOAT
      distance:NX_FLOAT
      emittance_x:NX_FLOAT
      emittance_y:NX_FLOAT
      energy:NX_FLOAT
      flux:NX_FLOAT
      frequency:NX_FLOAT
      last_fill:NX_NUMBER
        @time
      mode:NX_CHAR
      name:NX_CHAR
        @short_name
      number_of_bunches:NX_INT
      period:NX_FLOAT
      power:NX_FLOAT
      probe:NX_CHAR
      pulse_width:NX_FLOAT
      sigma_x:NX_FLOAT
      sigma_y:NX_FLOAT
      target_material:NX_CHAR
      top_up:NX_BOOLEAN
      type:NX_CHAR
      voltage:NX_FLOAT
      bunch_pattern:NXdata
        title:NX_CHAR
      pulse_shape:NXdata
      distribution:NXdata
      geometry:NXgeometry
      notes:NXnote
    
