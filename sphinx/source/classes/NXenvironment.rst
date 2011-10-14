..  _NXenvironment:

#############
NXenvironment
#############

.. index::  ! classes - base_classes; NXenvironment

category
    base_classes

NXDL source:
    NXenvironment
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXenvironment.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXenvironment.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`, :ref:`NXnote`, :ref:`NXsensor`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXenvironment
================================

::

    NXenvironment (base class, version 1.0)
      description:NX_CHAR
      name:NX_CHAR
      program:NX_CHAR
      short_name:NX_CHAR
      type:NX_CHAR
      position:NXgeometry
      NXnote
      NXsensor
    
