..  _NXxnb:

#####
NXxnb
#####

.. index::  ! . NXDL applications; NXxnb

category:
    applications

NXDL source:
    NXxnb
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxnb.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXxbase`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXsample`

symbol list:
    none

documentation:
    This is the application definition for raw data from a single crystal diffractometer
    measuring in normal beam mode. It extends NXxbase, so the full definition is the content of
    NXxbase plus the data defined here. All angles are logged in order to support arbitray scans in
    reciprocal space.
    


.. rubric:: Basic Structure of **NXxnb**

::

    NXxnb (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        name:NXdata
          polar_angle --> /NXentry/NXinstrument/NXdetector/polar_angle
          rotation_angle --> /NXentry/NXsample/rotation_angle
          tilt --> /NXentry/NXinstrument/NXdetector/tilt
        instrument:NXinstrument
          detector:NXdetector
            polar_angle:NX_FLOAT[np]
            tilt_angle:NX_FLOAT[np]
        sample:NXsample
          rotation_angle:NX_FLOAT[np]
    

.. rubric:: Comprehensive Structure of **NXxnb**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        