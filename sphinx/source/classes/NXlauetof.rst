..  _NXlauetof:

#########
NXlauetof
#########

.. index::  ! classes - applications; NXlauetof

category
    applications

NXDL source:
    NXlauetof
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXlauetof.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXlauetof.nxdl.xml 822 2011-02-15 20:00:32Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXsample`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXlauetof
============================

::

    NXlauetof (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        name:NXdata
          data --> /NXentry/NXinstrument/NXdetector/data
          time_of_flight --> /NXentry/NXinstrument/NXdetector/time_of_flight
        instrument:NXinstrument
          detector:NXdetector
            azimuthal_angle:NX_FLOAT
            data:NX_INT[number of x pixels,number of y pixels,nTOF]
              @signal
            distance:NX_FLOAT
            polar_angle:NX_FLOAT
            time_of_flight:NX_FLOAT[nTOF]
            x_pixel_size:NX_FLOAT
            y_pixel_size:NX_FLOAT
        control:NXmonitor
          data:NX_INT[nTOF]
          mode:NX_CHAR
          preset:NX_FLOAT
          time_of_flight:NX_FLOAT[nTOF]
        sample:NXsample
          name:NX_CHAR
          orientation_matrix:NX_FLOAT[3,3]
          unit_cell:NX_FLOAT[6]
    
