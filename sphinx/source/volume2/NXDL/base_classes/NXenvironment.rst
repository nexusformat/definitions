..  _NXenvironment:

#############
NXenvironment
#############

.. index::  ! . NXDL base_classes; NXenvironment

category:
    base_classes

NXDL source:
    NXenvironment
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXenvironment.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`, :ref:`NXnote`, :ref:`NXsensor`

documentation:
    This class describes an external condition applied to the sample
    


.. rubric:: Basic Structure of **NXenvironment**

.. code-block:: text
    :linenos:
    
    NXenvironment (base class, version 1.0)
      description:NX_CHAR
      name:NX_CHAR
      program:NX_CHAR
      short_name:NX_CHAR
      type:NX_CHAR
      position:NXgeometry
      NXnote
      NXsensor
    

.. rubric:: Symbols used in definition of **NXenvironment**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXenvironment**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
