..  _NXroot:

######
NXroot
######

.. index::  ! . NXDL base_classes; NXroot

category:
    base_classes

NXDL source:
    NXroot
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXroot.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXentry`

documentation:
    Definition of the root NeXus group.
    


.. rubric:: Basic Structure of **NXroot**

.. code-block:: text
    :linenos:
    
    NXroot (base class, version 1.0)
      @NX_class
      @file_time
      @file_name
      @file_update_time
      @NeXus_version
      @HDF_version
      @HDF5_Version
      @XML_version
      @creator
      NXentry
    

.. rubric:: Symbols used in definition of **NXroot**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXroot**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
