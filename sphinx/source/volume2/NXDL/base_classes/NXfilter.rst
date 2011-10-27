..  _NXfilter:

########
NXfilter
########

.. index::  ! . NXDL base_classes; NXfilter

category:
    base_classes

NXDL source:
    NXfilter
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXfilter.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`, :ref:`NXlog`, :ref:`NXsensor`

documentation:
    Template for specifying the state of band pass filters.
    If uncertain whether to use NXfilter (band-pass filter)
    or NXattenuator (reduces beam intensity), then use
    NXattenuator.
    


.. rubric:: Basic Structure of **NXfilter**

.. code-block:: text
    :linenos:
    
    NXfilter (base class, version 1.0)
      chemical_formula:NX_CHAR
      coating_material:NX_CHAR
      coating_roughness:NX_FLOAT[nsurf]
      density:NX_NUMBER
      description:NX_CHAR
      m_value:NX_FLOAT
      orientation_matrix:NX_FLOAT[n_comp,3,3]
      status:NX_CHAR
      substrate_material:NX_CHAR
      substrate_roughness:NX_FLOAT
      substrate_thickness:NX_FLOAT
      temperature:NX_FLOAT
      thickness:NX_FLOAT
      unit_cell_a:NX_FLOAT
      unit_cell_alpha:NX_FLOAT
      unit_cell_b:NX_FLOAT
      unit_cell_beta:NX_FLOAT
      unit_cell_c:NX_FLOAT
      unit_cell_gamma:NX_FLOAT
      unit_cell_volume:NX_FLOAT[n_comp]
      transmission:NXdata
      NXgeometry
      temperature_log:NXlog
      sensor_type:NXsensor
    

.. rubric:: Symbols used in definition of **NXfilter**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXfilter**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
