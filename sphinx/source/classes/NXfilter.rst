..  _NXfilter:

########
NXfilter
########

.. index::  ! classes - base_classes; NXfilter

category
    base_classes

NXDL source:
    NXfilter
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXfilter.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXfilter.nxdl.xml 829 2011-02-20 15:04:56Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`, :ref:`NXlog`, :ref:`NXsensor`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXfilter
===========================

::

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
    
