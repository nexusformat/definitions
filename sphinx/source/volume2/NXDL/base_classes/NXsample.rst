..  _NXsample:

########
NXsample
########

.. index::  ! . NXDL base_classes; NXsample

category:
    base_classes

NXDL source:
    NXsample
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXsample.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXbeam`, :ref:`NXdata`, :ref:`NXenvironment`, :ref:`NXgeometry`, :ref:`NXlog`

documentation:
    Template of the state of the sample. This could include scanned variables that
    are associated with one of the data dimensions, e.g. the magnetic field, or
    logged data, e.g. monitored temperature vs elapsed time.
    


.. rubric:: Basic Structure of **NXsample**

.. code-block:: text
    :linenos:
    
    NXsample (base class, version 1.0)
      changer_position:NX_INT
      chemical_formula:NX_CHAR
      component:NX_CHAR
      concentration:NX_FLOAT[n_comp]
      density:NX_FLOAT[n_comp]
      description:NX_CHAR
      distance:NX_FLOAT
      electric_field:NX_FLOAT[n_eField]
        @direction
      external_DAC:NX_FLOAT
      magnetic_field:NX_FLOAT[n_mField]
        @direction
      mass:NX_FLOAT[n_comp]
      name:NX_CHAR
      orientation_matrix:NX_FLOAT[n_comp,3,3]
      path_length:NX_FLOAT
      path_length_window:NX_FLOAT
      preparation_date:NX_DATE_TIME
      pressure:NX_FLOAT[n_pField]
      relative_molecular_mass:NX_FLOAT[n_comp]
      rotation_angle:NX_FLOAT
      sample_component:NX_CHAR
      sample_orientation:NX_FLOAT[3]
      scattering_length_density:NX_FLOAT[n_comp]
      short_title:NX_CHAR
      situation:NX_CHAR
      stress_field:NX_FLOAT[n_sField]
        @direction
      temperature:NX_FLOAT[n_Temp]
      thickness:NX_FLOAT
      type:NX_CHAR
      unit_cell:NX_FLOAT[n_comp,6]
      unit_cell_class:NX_CHAR
      unit_cell_group:NX_CHAR
      unit_cell_volume:NX_FLOAT[n_comp]
      volume_fraction:NX_FLOAT[n_comp]
      x_translation:NX_FLOAT
      NXbeam
      transmission:NXdata
      temperature_env:NXenvironment
      magnetic_field_env:NXenvironment
      geometry:NXgeometry
      temperature_log:NXlog
      magnetic_field_log:NXlog
      external_ADC:NXlog
    

.. rubric:: Symbols used in definition of **NXsample**

symbolic array lengths to be coordinated between various fields

+--------------+--------------------------------------------+
| Symbol       | Description                                |
+==============+============================================+
| ``n_comp``   | number of compositions                     |
+--------------+--------------------------------------------+
| ``n_Temp``   | number of temperatures                     |
+--------------+--------------------------------------------+
| ``n_eField`` | number of values in applied electric field |
+--------------+--------------------------------------------+
| ``n_mField`` | number of values in applied magnetic field |
+--------------+--------------------------------------------+
| ``n_pField`` | number of values in applied pressure field |
+--------------+--------------------------------------------+
| ``n_sField`` | number of values in applied stress field   |
+--------------+--------------------------------------------+




.. rubric:: Comprehensive Structure of **NXsample**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
