..  _NXmirror:

########
NXmirror
########

.. index::  ! . NXDL base_classes; NXmirror

category:
    base_classes

NXDL source:
    NXmirror
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXmirror.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`, :ref:`NXshape`

documentation:
    Template of a beamline mirror or supermirror.
    


.. rubric:: Basic Structure of **NXmirror**

.. code-block:: text
    :linenos:
    
    NXmirror (base class, version 1.0)
      bend_angle_x:NX_FLOAT
      bend_angle_y:NX_FLOAT
      coating_material:NX_CHAR
      coating_roughness:NX_FLOAT
      description:NX_CHAR
      even_layer_density:NX_FLOAT
      even_layer_material:NX_CHAR
      external_material:NX_CHAR
      incident_angle:NX_FLOAT
      interior_atmosphere:NX_CHAR
      layer_thickness:NX_FLOAT
      m_value:NX_FLOAT
      odd_layer_density:NX_FLOAT
      odd_layer_material:NX_CHAR
      substrate_density:NX_FLOAT
      substrate_material:NX_CHAR
      substrate_roughness:NX_FLOAT
      substrate_thickness:NX_FLOAT
      type:NX_CHAR
      reflectivity:NXdata
      figure_data:NXdata
      NXgeometry
      shape:NXshape
    

.. rubric:: Symbols used in definition of **NXmirror**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXmirror**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
