..  _NXdetector:

##########
NXdetector
##########

.. index::  ! classes - base_classes; NXdetector

category
    base_classes

NXDL source:
    NXdetector
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXdetector.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXdetector.nxdl.xml 829 2011-02-20 15:04:56Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcharacterization`, :ref:`NXdata`, :ref:`NXgeometry`, :ref:`NXnote`, :ref:`NXnote`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXdetector
=============================

::

    NXdetector (base class, version 1.0)
      azimuthal_angle:NX_FLOAT[np,i,j]
      beam_center_x:NX_FLOAT
      beam_center_y:NX_FLOAT
      calibration_date:NX_DATE_TIME
      count_time:NX_NUMBER[np]
      crate:NX_INT[i,j]
        @local_name
      data:NX_NUMBER[np,i,j,tof]
        @signal
        @axes
        @long_name
        @check_sum
        @link
      data_error:NX_NUMBER[np,i,j,tof]
        @units
        @link
      dead_time:NX_FLOAT[np,i,j]
      description:NX_CHAR
      detection_gas_path:NX_FLOAT
      detector_number:NX_INT[i,j]
      diameter:NX_FLOAT
      distance:NX_FLOAT[np,i,j]
      frame_start_number:NX_INT
      gas_pressure:NX_FLOAT[i,j]
      input:NX_INT[i,j]
        @local_name
      layout:NX_CHAR
      local_name:NX_CHAR
      polar_angle:NX_FLOAT[np,i,j]
      raw_time_of_flight:NX_INT[tof+1]
        @frequency
      sequence_number:NX_CHAR
      slot:NX_INT[i,j]
        @local_name
      solid_angle:NX_FLOAT[i,j]
      time_of_flight:NX_FLOAT[tof+1]
        @axis
        @primary
        @long_name
        @link
      type:NX_CHAR
      x_pixel_offset:NX_FLOAT[i]
        @axis
        @primary
        @long_name
        @link
      x_pixel_size:NX_FLOAT[i,j]
      y_pixel_offset:NX_FLOAT[j]
        @axis
        @primary
        @long_name
      y_pixel_size:NX_FLOAT[i,j]
      NXcharacterization
      efficiency:NXdata
        efficiency:NX_FLOAT[i,j,k]
        real_time:NX_NUMBER[i,j,k]
        wavelength:NX_FLOAT[i,j,k]
      NXgeometry
      calibration_method:NXnote
      data_file:NXnote
    
