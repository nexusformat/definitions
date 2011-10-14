..  _NXtomo:

######
NXtomo
######

.. index::  ! classes - applications; NXtomo

category
    applications

NXDL source:
    NXtomo
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXtomo.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXtomo.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXdetector`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXsample`, :ref:`NXsource`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXtomo
=========================

::

    NXtomo (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        end_time:NX_DATE_TIME
        start_time:NX_DATE_TIME
        title:NX_CHAR
        data:NXdata
          data --> /NXentry/NXinstrument/data:NXdetector/data
          rotation_angle --> /NXentry/NXsample/rotation_angle
        instrument:NXinstrument
          bright_field:NXdetector
            data:NX_INT[nBrightFrames,xsize,ysize]
            sequence_number:NX_CHAR
          dark_field:NXdetector
            data:NX_INT[nDarkFrames,xsize,ysize]
            sequence_number:NX_CHAR
          sample:NXdetector
            data:NX_INT[nSampleFrames,xsize,ysize]
            distance:NX_FLOAT
            sequence_number:NX_CHAR
            x_pixel_size:NX_FLOAT
            y_pixel_size:NX_FLOAT
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        control:NXmonitor
          integral:NX_FLOAT[nDarkFrames + nBrightFrames + nSampleFrame]
        sample:NXsample
          name:NX_CHAR
          rotation_angle:NX_FLOAT[nSampleFrames]
          x_translation:NX_FLOAT[nSampleFrames]
          y_translation:NX_FLOAT[nSampleFrames]
          z_translation:NX_FLOAT[nSampleFrames]
    
