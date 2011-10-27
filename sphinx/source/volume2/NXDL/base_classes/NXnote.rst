..  _NXnote:

######
NXnote
######

.. index::  ! . NXDL base_classes; NXnote

category:
    base_classes

NXDL source:
    NXnote
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXnote.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

documentation:
    This class can be used to store additional information in a
    NeXus file e.g. pictures, movies, audio, additional text logs
    


.. rubric:: Basic Structure of **NXnote**

.. code-block:: text
    :linenos:
    
    NXnote (base class, version 1.0)
      author:NX_CHAR
      data:NX_BINARY
      date:NX_DATE_TIME
      description:NX_CHAR
      file_name:NX_CHAR
      type:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXnote**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXnote**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
