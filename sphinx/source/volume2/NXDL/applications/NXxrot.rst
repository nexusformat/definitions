..  _NXxrot:

######
NXxrot
######

.. index::  ! . NXDL applications; NXxrot

category:
    applications

NXDL source:
    NXxrot
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxrot.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXxbase`

other classes included:
    :ref:`NXattenuator`, :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXsample`

documentation:
    This is the application definition for raw data from a rotation camera. It extends NXxbase,
    so the full definition is the content of NXxbase plus the data defined here.
    


.. rubric:: Basic Structure of **NXxrot**

.. code-block:: text
    :linenos:
    
    NXxrot (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        name:NXdata
          rotation_angle --> /NXentry/NXsample/rotation_angle
        instrument:NXinstrument
          attenuator:NXattenuator
            attenuator_transmission:NX_FLOAT
          detector:NXdetector
            beam_center_x:NX_FLOAT
            beam_center_y:NX_FLOAT
            polar_angle:NX_FLOAT
        sample:NXsample
          rotation_angle:NX_FLOAT[np]
          rotation_angle_step:NX_FLOAT[np]
    

.. rubric:: Symbols used in definition of **NXxrot**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXxrot**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
