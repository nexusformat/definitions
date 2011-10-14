..  _NXxeuler:

########
NXxeuler
########

.. index::  ! classes - applications; NXxeuler

category
    applications

NXDL source:
    NXxeuler
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxeuler.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXxeuler.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXxbase`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXsample`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXxeuler
===========================

::

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
    
