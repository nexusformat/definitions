..  _NXevent_data:

############
NXevent_data
############

.. index::  ! classes - base_classes; NXevent_data

category
    base_classes

NXDL source:
    NXevent_data
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXevent_data.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXevent_data.nxdl.xml 822 2011-02-15 20:00:32Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXevent_data
===============================

::

    NXevent_data (base class, version 1.0)
      events_per_pulse:NX_INT[j]
      pixel_number:NX_INT[i]
      pulse_height:NX_FLOAT[i,k]
      pulse_time:NX_INT[j]
        @offset
      time_of_flight:NX_INT[i]
    
