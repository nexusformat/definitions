..  _NXshape:

#######
NXshape
#######

.. index::  ! . NXDL base_classes; NXshape

category:
    base_classes

NXDL source:
    NXshape
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXshape.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

documentation:
    This is the description of the general shape and size of a
    component, which may be made up of "numobj" separate
    elements - it is used by the NXgeometry class
    


.. rubric:: Basic Structure of **NXshape**

.. code-block:: text
    :linenos:
    
    NXshape (base class, version 1.0)
      direction:NX_CHAR
      shape:NX_CHAR
      size:NX_FLOAT[numobj,nshapepar]
    

.. rubric:: Symbols used in definition of **NXshape**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXshape**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
