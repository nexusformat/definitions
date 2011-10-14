..  _NXbeam_stop:

###########
NXbeam_stop
###########

.. index::  ! classes - base_classes; NXbeam_stop

category
    base_classes

NXDL source:
    NXbeam_stop
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXbeam_stop.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXbeam_stop.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXbeam_stop
==============================

::

    NXbeam_stop (base class, version 1.0)
      description:NX_CHAR
      distance_to_detector:NX_FLOAT
      size:NX_FLOAT
      status:NX_CHAR
      x:NX_FLOAT
      y:NX_FLOAT
      NXgeometry
    
