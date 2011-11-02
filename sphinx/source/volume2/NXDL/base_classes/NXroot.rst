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



.. rubric:: Attributes of ``definition`` element in **NXroot**

+-------------------+---------+-------+--------------------------------+
| Attributes        | Type    | Units | Description (and Occurrences)  |
+===================+=========+=======+================================+
| @NX_class         | NX_CHAR | ..    | ..                             |
+-------------------+---------+-------+--------------------------------+
| @file_time        | NX_CHAR | ..    | ..                             |
+-------------------+---------+-------+--------------------------------+
| @file_name        | NX_CHAR | ..    | ..                             |
+-------------------+---------+-------+--------------------------------+
| @file_update_time | NX_CHAR | ..    | ..                             |
+-------------------+---------+-------+--------------------------------+
| @NeXus_version    | NX_CHAR | ..    | ..                             |
+-------------------+---------+-------+--------------------------------+
| @HDF_version      | NX_CHAR | ..    | ..                             |
+-------------------+---------+-------+--------------------------------+
| @HDF5_Version     | NX_CHAR | ..    | ..                             |
+-------------------+---------+-------+--------------------------------+
| @XML_version      | NX_CHAR | ..    | ..                             |
+-------------------+---------+-------+--------------------------------+
| @creator          | NX_CHAR | ..    | ..                             |
+-------------------+---------+-------+--------------------------------+


.. rubric:: Comprehensive Structure of **NXroot**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
