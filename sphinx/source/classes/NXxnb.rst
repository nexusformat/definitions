..  _NXxnb:

#####
NXxnb
#####

.. index::  ! classes - applications; NXxnb

category
    applications

NXDL source:
    NXxnb
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxnb.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXxnb.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXxbase`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXsample`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXxnb
========================

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
    
