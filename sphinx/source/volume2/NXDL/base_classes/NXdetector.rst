..  _NXdetector:

##########
NXdetector
##########

.. index::  ! . NXDL base_classes; NXdetector

category:
    base_classes

NXDL source:
    NXdetector
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXdetector.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcharacterization`, :ref:`NXdata`, :ref:`NXgeometry`, :ref:`NXnote`

documentation:
    Template of a detector, detector bank, or multidetector.
    


.. rubric:: Basic Structure of **NXdetector**

.. code-block:: text
    :linenos:
    
    NXdetector (base class, version 1.0)
      acquisition_mode:NX_CHAR
      angular_calibration:NX_FLOAT[i,j]
      angular_calibration_applied:NX_BOOLEAN
      azimuthal_angle:NX_FLOAT[np,i,j]
      beam_center_x:NX_FLOAT
      beam_center_y:NX_FLOAT
      bit_depth_readout:NX_INT
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
      detector_readout_time:NX_FLOAT
      diameter:NX_FLOAT
      distance:NX_FLOAT[np,i,j]
      flatfield:NX_FLOAT[i,j]
      flatfield_applied:NX_BOOLEAN
      flatfield_error:NX_FLOAT[i,j]
      frame_start_number:NX_INT
      gain_setting:NX_CHAR
      gas_pressure:NX_FLOAT[i,j]
      input:NX_INT[i,j]
        @local_name
      layout:NX_CHAR
      local_name:NX_CHAR
      number_of_cycles:NX_INT
      pixel_mask:NX_FLOAT[i,j]
      pixel_mask_applied:NX_BOOLEAN
      polar_angle:NX_FLOAT[np,i,j]
      raw_time_of_flight:NX_INT[tof+1]
        @frequency
      saturation_value:NX_INT
      sensor_material:NX_CHAR
      sensor_thickness:NX_FLOAT
      sequence_number:NX_CHAR
      slot:NX_INT[i,j]
        @local_name
      solid_angle:NX_FLOAT[i,j]
      threshold_energy:NX_FLOAT
      time_of_flight:NX_FLOAT[tof+1]
        @axis
        @primary
        @long_name
        @link
      trigger_dead_time:NX_FLOAT
      trigger_delay_time:NX_FLOAT
      type:NX_CHAR
      x_pixel_offset:NX_FLOAT[i,j]
        @axis
        @primary
        @long_name
        @link
      x_pixel_size:NX_FLOAT[i,j]
      y_pixel_offset:NX_FLOAT[i,j]
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
    

.. rubric:: Symbols used in definition of **NXdetector**

These symbols will be used below to coordinate datasets with the same shape.

+---------+-----------------------------------------------------------------------------+
| Symbol  | Description                                                                 |
+=========+=============================================================================+
| ``np``  | number of scan points (only present in scanning measurements)               |
+---------+-----------------------------------------------------------------------------+
| ``i``   | number of detector pixels in the first (X, slowest) direction               |
+---------+-----------------------------------------------------------------------------+
| ``j``   | number of detector pixels in the second (Y, faster) direction               |
+---------+-----------------------------------------------------------------------------+
| ``k``   | number of detector pixels in the third (Z, if necessary, fastest) direction |
+---------+-----------------------------------------------------------------------------+
| ``tof`` | number of bins in the time-of-flight histogram                              |
+---------+-----------------------------------------------------------------------------+




.. rubric:: Comprehensive Structure of **NXdetector**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
