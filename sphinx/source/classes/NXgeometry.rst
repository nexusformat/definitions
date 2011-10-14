..  _NXgeometry:

##########
NXgeometry
##########

.. index::  ! classes - base_classes; NXgeometry

category
    base_classes

NXDL source:
    NXgeometry
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXgeometry.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXgeometry.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXorientation`, :ref:`NXshape`, :ref:`NXtranslation`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXgeometry
=============================

::

    NXgeometry (base class, version 1.0)
      component_index:NX_INT
      description:NX_CHAR
      NXorientation
      NXshape
      NXtranslation
    
