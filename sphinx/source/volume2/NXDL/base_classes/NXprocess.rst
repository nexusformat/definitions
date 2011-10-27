..  _NXprocess:

#########
NXprocess
#########

.. index::  ! . NXDL base_classes; NXprocess

category:
    base_classes

NXDL source:
    NXprocess
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXprocess.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXnote`

documentation:
    Document an event of data processing, reconstruction, or analysis for this data.
    


.. rubric:: Basic Structure of **NXprocess**

.. code-block:: text
    :linenos:
    
    NXprocess (base class, version 1.0)
      date:NX_DATE_TIME
      program:NX_CHAR
      version:NX_CHAR
      NXnote
    

.. rubric:: Symbols used in definition of **NXprocess**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXprocess**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
