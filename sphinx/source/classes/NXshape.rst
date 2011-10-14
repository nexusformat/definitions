..  _NXshape:

#######
NXshape
#######

.. index::  ! classes - base_classes; NXshape

category
    base_classes

NXDL source:
    NXshape
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXshape.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXshape.nxdl.xml 829 2011-02-20 15:04:56Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXshape
==========================

::

    NXshape (base class, version 1.0)
      direction:NX_CHAR
      shape:NX_CHAR
      size:NX_FLOAT[numobj,nshapepar]
    
