..  _NXreftof:

########
NXreftof
########

.. index::  ! classes - applications; NXreftof

category
    applications

NXDL source:
    NXreftof
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXreftof.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXreftof.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXdisk_chopper`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXsample`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXreftof
===========================

::

    NXreftof (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        end_time:NX_DATE_TIME
        start_time:NX_DATE_TIME
        title:NX_CHAR
        data:NXdata
          data --> /NXentry/NXinstrument/NXdetector/data
          time_binning --> /NXentry/NXinstrument/NXdetector/time_binning
        instrument:NXinstrument
          name:NX_CHAR
          detector:NXdetector
            data:NX_INT[xsize,ysize,nTOF]
            distance:NX_FLOAT
            polar_angle:NX_FLOAT
            time_of_flight:NX_FLOAT[nTOF]
            x_pixel_size:NX_FLOAT
            y_pixel_size:NX_FLOAT
          chopper:NXdisk_chopper
            distance:NX_FLOAT
        control:NXmonitor
          data:NX_INT
          integral:NX_INT
          mode:NX_CHAR
          preset:NX_FLOAT
          time_of_flight:NX_FLOAT
        sample:NXsample
          name:NX_CHAR
          rotation_angle:NX_FLOAT
    
