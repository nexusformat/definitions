..  _NXdisk_chopper:

##############
NXdisk_chopper
##############

.. index::  ! . NXDL base_classes; NXdisk_chopper

category:
    base_classes

NXDL source:
    NXdisk_chopper
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXdisk_chopper.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`

documentation:
    No documentation provided.


.. rubric:: Basic Structure of **NXdisk_chopper**

.. code-block:: text
    :linenos:
    
    NXdisk_chopper (base class, version 1.0)
      distance:NX_FLOAT
      pair_separation:NX_FLOAT
      phase:NX_FLOAT
      radius:NX_FLOAT
      ratio:NX_INT
      rotation_speed:NX_FLOAT
      slit_angle:NX_FLOAT
      slit_height:NX_FLOAT
      slits:NX_INT
      type:NX_CHAR
      wavelength_range:NX_FLOAT[2]
      NXgeometry
    

.. rubric:: Symbols used in definition of **NXdisk_chopper**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXdisk_chopper**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
