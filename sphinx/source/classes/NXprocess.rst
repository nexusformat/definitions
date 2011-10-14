..  _NXprocess:

#########
NXprocess
#########

.. index::  ! classes - base_classes; NXprocess

category
    base_classes

NXDL source:
    NXprocess
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXprocess.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXprocess.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXnote`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXprocess
============================

::

    NXprocess (base class, version 1.0)
      date:NX_DATE_TIME
      program:NX_CHAR
      version:NX_CHAR
      NXnote
    
