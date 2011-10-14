..  _NXsas:

#####
NXsas
#####

.. index::  ! classes - applications; NXsas

category
    applications

NXDL source:
    NXsas
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXsas.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXsas.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcollimator`, :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXgeometry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXmonochromator`, :ref:`NXsample`, :ref:`NXshape`, :ref:`NXsource`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXsas
========================

::

    NXsas (application definition, version 1.0b)
      (overlays NXentry)
      NXentry
        @entry
        definition:NX_CHAR
        end_time:NX_DATE_TIME
        start_time:NX_DATE_TIME
        title:NX_CHAR
        data:NXdata
          data --> /NXentry/NXinstrument/NXdetector/data
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
            data:NX_NUMBER[nXPixel,nYPixel]
            distance:NX_FLOAT
            polar_angle:NX_FLOAT
            rotation_angle:NX_FLOAT
            x_pixel_size:NX_FLOAT
            y_pixel_size:NX_FLOAT
          monochromator:NXmonochromator
            wavelength:NX_FLOAT
            wavelength_spread:NX_FLOAT
          source:NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        control:NXmonitor
          integral:NX_FLOAT
          mode:NX_CHAR
          preset:NX_FLOAT
        sample:NXsample
          aequatorial_angle:NX_FLOAT
          name:NX_CHAR
    
