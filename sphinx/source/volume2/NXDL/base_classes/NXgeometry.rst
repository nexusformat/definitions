..  _NXgeometry:

##########
NXgeometry
##########

.. index::  ! . NXDL base_classes; NXgeometry

category:
    base_classes

NXDL source:
    NXgeometry
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXgeometry.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXorientation`, :ref:`NXshape`, :ref:`NXtranslation`

symbol list:
    none

documentation:
    This is the description for a general position of a component.
    It is recommended to name an instance of NXgeometry as "geometry"
    to aid in the use of the definition in simulation codes such as McStas.
    Also, in HDF, linked items must share the same name.
    However, it might not be possible or practical in all situations.
    


.. rubric:: Basic Structure of **NXgeometry**

::

    NXgeometry (base class, version 1.0)
      component_index:NX_INT
      description:NX_CHAR
      NXorientation
      NXshape
      NXtranslation
    

.. rubric:: Comprehensive Structure of **NXgeometry**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        