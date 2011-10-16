..  _NXtas:

#####
NXtas
#####

.. index::  ! . NXDL applications; NXtas

category:
    applications

NXDL source:
    NXtas
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXtas.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcrystal`, :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXsample`, :ref:`NXsource`

symbol list:
    none

documentation:
    This is an application definition for a triple axis spectrometer. It is for the trademark
    scan of the TAS, the Q-E scan. For your alignment scans use the rules in NXscan.
    


.. rubric:: Basic Structure of **NXtas**

::

    NXtas (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        start_time:NX_DATE_TIME
        title:NX_CHAR
        NXdata
          data --> /NXentry/NXinstrument/NXdetector/data
          ef --> /NXentry/NXinstrument/analyzer:NXcrystal/ef
          ei --> /NXentry/NXinstrument/monochromator:NXcrystal/ei
          en --> /NXentry/NXsample/en
          qh --> /NXentry/NXsample/qh
          qk --> /NXentry/NXsample/qk
          ql --> /NXentry/NXsample/ql
        NXinstrument
          monochromator:NXcrystal
            ei:NX_FLOAT[np]
            rotation_angle:NX_FLOAT[np]
          analyser:NXcrystal
            ef:NX_FLOAT[np]
            polar_angle:NX_FLOAT[np]
            rotation_angle:NX_FLOAT[np]
          NXdetector
            data:NX_INT[np]
            polar_angle:NX_FLOAT[np]
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
        NXmonitor
          data:NX_FLOAT[np]
          mode:NX_CHAR
          preset:NX_FLOAT
        NXsample
          en:NX_FLOAT[np]
          name:NX_CHAR
          orientation_matrix:NX_FLOAT[9]
          polar_angle:NX_FLOAT[np]
          qh:NX_FLOAT[np]
          qk:NX_FLOAT[np]
          ql:NX_FLOAT[np]
          rotation_angle:NX_FLOAT[np]
          sgl:NX_FLOAT[np]
          sgu:NX_FLOAT[np]
          unit_cell:NX_FLOAT[6]
    

.. rubric:: Comprehensive Structure of **NXtas**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        