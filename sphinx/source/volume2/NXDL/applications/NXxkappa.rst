..  _NXxkappa:

########
NXxkappa
########

.. index::  ! . NXDL applications; NXxkappa

category:
    applications

NXDL source:
    NXxkappa
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxkappa.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXxbase`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXsample`

documentation:
    This is the application definition for raw data from a kappa geometry (CAD4) single crystal
    diffractometer. It extends NXxbase, so the full definition is the content of NXxbase plus the
    data defined here.
    


.. rubric:: Basic Structure of **NXxkappa**

.. code-block:: text
    :linenos:
    
    NXxkappa (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        name:NXdata
          kappa --> /NXentry/NXsample/kappa
          phi --> /NXentry/NXsample/phi
          polar_angle --> /NXentry/NXinstrument/NXdetector/polar_angle
          rotation_angle --> /NXentry/NXsample/rotation_angle
        instrument:NXinstrument
          detector:NXdetector
            polar_angle:NX_FLOAT[np]
        sample:NXsample
          alpha:NX_FLOAT
          kappa:NX_FLOAT[np]
          phi:NX_FLOAT[np]
          rotation_angle:NX_FLOAT[np]
    

.. rubric:: Symbols used in definition of **NXxkappa**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXxkappa**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
