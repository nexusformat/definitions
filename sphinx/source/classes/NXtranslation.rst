..  _NXtranslation:

#############
NXtranslation
#############

.. index::  ! classes - base_classes; NXtranslation

category
    base_classes

NXDL source:
    NXtranslation
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXtranslation.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXtranslation.nxdl.xml 829 2011-02-20 15:04:56Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXtranslation
================================

::

    NXtranslation (base class, version 1.0)
      distances:NX_FLOAT[numobj,3]
      geometry:NXgeometry
    
