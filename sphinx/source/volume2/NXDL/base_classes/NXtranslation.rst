..  _NXtranslation:

#############
NXtranslation
#############

.. index::  ! . NXDL base_classes; NXtranslation

category:
    base_classes

NXDL source:
    NXtranslation
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXtranslation.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`

symbol list:
    none

documentation:
    This is the description for the general spatial location
    of a component - it is used by the NXgeometry class
    


.. rubric:: Basic Structure of **NXtranslation**

::

    NXtranslation (base class, version 1.0)
      distances:NX_FLOAT[numobj,3]
      geometry:NXgeometry
    

.. rubric:: Comprehensive Structure of **NXtranslation**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        