..  _NXxeuler:

########
NXxeuler
########

.. index::  ! . NXDL applications; NXxeuler

category:
    applications

NXDL source:
    NXxeuler
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxeuler.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXxbase`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXsample`

documentation:
    This is the application definition for raw data from a
    four circle diffractometer with an eulerian cradle.
    It extends NXxbase, so the full definition is the content
    of NXxbase plus the data defined here. All four angles are
    logged in order to support arbitray scans in reciprocal space.
    


.. rubric:: Basic Structure of **NXxeuler**

.. code-block:: text
    :linenos:
    
    NXxeuler (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        name:NXdata
          chi --> /NXentry/NXsample/chi
          phi --> /NXentry/NXsample/phi
          polar_angle --> /NXentry/NXinstrument/NXdetector/polar_angle
          rotation_angle --> /NXentry/NXsample/rotation_angle
        instrument:NXinstrument
          detector:NXdetector
            polar_angle:NX_FLOAT[np]
        sample:NXsample
          chi:NX_FLOAT[np]
          phi:NX_FLOAT[np]
          rotation_angle:NX_FLOAT[np]
    

.. rubric:: Symbols used in definition of **NXxeuler**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXxeuler**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
