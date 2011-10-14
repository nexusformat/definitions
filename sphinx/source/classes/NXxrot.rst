..  _NXxrot:

######
NXxrot
######

.. index::  ! classes - applications; NXxrot

category
    applications

NXDL source:
    NXxrot
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxrot.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXxrot.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXxbase`

other classes included:
    :ref:`NXattenuator`, :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXsample`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXxrot
=========================

::

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
    
