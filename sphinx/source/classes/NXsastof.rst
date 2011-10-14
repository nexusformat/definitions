..  _NXsastof:

########
NXsastof
########

.. index::  ! classes - applications; NXsastof

category
    applications

NXDL source:
    NXsastof
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXsastof.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXsastof.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcollimator`, :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXgeometry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXsample`, :ref:`NXshape`, :ref:`NXsource`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXsastof
===========================

::

    NXsastof (application definition, version 1.0b)
      (overlays NXentry)
      NXentry
        @entry
        definition:NX_CHAR
        start_time:NX_DATE_TIME
        title:NX_CHAR
        data:NXdata
          data --> /NXentry/NXinstrument/NXdetector/data
          time_of_flight --> /NXentry/NXinstrument/NXdetector/time_of_flight
        instrument:NXinstrument
          name:NX_CHAR
          collimator:NXcollimator
            geometry:NXgeometry
              shape:NXshape
                shape:NX_CHAR
                size:NX_FLOAT
          detector:NXdetector
            aequatorial_angle:NX_FLOAT
            azimuthal_angle:NX_FLOAT
            beam_center_x:NX_FLOAT
            beam_center_y:NX_FLOAT
            data:NX_NUMBER[nXPixel,nYPixel,nTOF]
            distance:NX_FLOAT
            polar_angle:NX_FLOAT
            rotation_angle:NX_FLOAT
            time_of_flight:NX_FLOAT[nTOF]
            x_pixel_size:NX_FLOAT
            y_pixel_size:NX_FLOAT
          source:NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        control:NXmonitor
          data:NX_INT[nTOF]
          mode:NX_CHAR
          preset:NX_FLOAT
          time_of_flight:NX_FLOAT[nTOF]
        sample:NXsample
          aequatorial_angle:NX_FLOAT
          name:NX_CHAR
    
