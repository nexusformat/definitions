..  _NXevent_data:

############
NXevent_data
############

.. index::  ! . NXDL base_classes; NXevent_data

category:
    base_classes

NXDL source:
    NXevent_data
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXevent_data.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    Time-of-flight events
    


.. rubric:: Basic Structure of **NXevent_data**

::

    NXevent_data (base class, version 1.0)
      events_per_pulse:NX_INT[j]
      pixel_number:NX_INT[i]
      pulse_height:NX_FLOAT[i,k]
      pulse_time:NX_INT[j]
        @offset
      time_of_flight:NX_INT[i]
    

.. rubric:: Comprehensive Structure of **NXevent_data**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        