..  _NXlog:

#####
NXlog
#####

.. index::  ! classes - base_classes; NXlog

category
    base_classes

NXDL source:
    NXlog
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXlog.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXlog.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXlog
========================

::

    NXlog (base class, version 1.0)
      average_value:NX_FLOAT
      average_value_error:NX_FLOAT
      description:NX_CHAR
      duration:NX_FLOAT
      maximum_value:NX_FLOAT
      minimum_value:NX_FLOAT
      raw_value:NX_NUMBER
      time:NX_FLOAT
        @start
      value:NX_NUMBER
    
