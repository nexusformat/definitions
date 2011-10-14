..  _NXmoderator:

###########
NXmoderator
###########

.. index::  ! classes - base_classes; NXmoderator

category
    base_classes

NXDL source:
    NXmoderator
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXmoderator.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXmoderator.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`, :ref:`NXlog`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXmoderator
==============================

::

    NXmoderator (base class, version 1.0)
      coupled:NX_BOOLEAN
      coupling_material:NX_CHAR
      distance:NX_FLOAT
      poison_depth:NX_FLOAT
      poison_material:NX_CHAR
      temperature:NX_FLOAT
      type:NX_CHAR
      pulse_shape:NXdata
      NXgeometry
      temperature_log:NXlog
    
