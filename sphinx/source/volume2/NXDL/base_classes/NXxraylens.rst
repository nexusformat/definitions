..  _NXxraylens:

##########
NXxraylens
##########

.. index::  ! . NXDL base_classes; NXxraylens

category:
    base_classes

NXDL source:
    NXxraylens
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXxraylens.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXnote`

symbol list:
    none

documentation:
    This is a dictionary of field names to use dor describing a X-ray lens as used at
    synchrotron beam lines. Based on information provided by Gerd Wellenreuther.
    


.. rubric:: Basic Structure of **NXxraylens**

::

    NXxraylens (base class, version 1.0)
      aperture:NX_FLOAT
      curvature:NX_FLOAT
      cylindrical:NX_BOOLEAN
      focus_type:NX_CHAR
      gas:NX_CHAR
      gas_pressure:NX_FLOAT
      lens_geometry:NX_CHAR
      lens_length:NX_FLOAT
      lens_material:NX_CHAR
      lens_thickness:NX_FLOAT
      number_of_lenses:NX_INT
      symmetric:NX_BOOLEAN
      cylinder_orientation:NXnote
    

.. rubric:: Comprehensive Structure of **NXxraylens**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        