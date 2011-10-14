..  _NXmonitor:

#########
NXmonitor
#########

.. index::  ! classes - base_classes; NXmonitor

category
    base_classes

NXDL source:
    NXmonitor
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXmonitor.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXmonitor.nxdl.xml 829 2011-02-20 15:04:56Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`, :ref:`NXlog`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXmonitor
============================

::

    NXmonitor (base class, version 1.0)
      count_time:NX_FLOAT
      data:NX_NUMBER[n]
        @signal
        @axes
      distance:NX_FLOAT
      efficiency:NX_NUMBER[]
      end_time:NX_DATE_TIME
      integral:NX_NUMBER
      mode:NX_CHAR
      preset:NX_NUMBER
      range:NX_FLOAT[2]
      sampled_fraction:NX_FLOAT
      start_time:NX_DATE_TIME
      time_of_flight:NX_FLOAT[]
      type:NX_CHAR
      NXgeometry
      integral_log:NXlog
    
