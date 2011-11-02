..  _NXaperture:

##########
NXaperture
##########

.. index::  ! . NXDL base_classes; NXaperture

category:
    base_classes

NXDL source:
    NXaperture
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXaperture.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`, :ref:`NXnote`

documentation:
    Template of a beamline aperture.
    


.. rubric:: Basic Structure of **NXaperture**

.. code-block:: text
    :linenos:
    
    NXaperture (base class, version 1.0)
      description:NX_CHAR
      material:NX_CHAR
      NXgeometry
      NXgeometry
      NXnote
    

.. rubric:: Symbols used in definition of **NXaperture**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXaperture**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
