..  _NXcrystal:

#########
NXcrystal
#########

.. index::  ! . NXDL base_classes; NXcrystal

category:
    base_classes

NXDL source:
    NXcrystal
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXcrystal.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`, :ref:`NXlog`, :ref:`NXshape`

documentation:
    Template of a crystal monochromator or analyzer. Permits double bent
    monochromator comprised of multiple segments with anisotropic
    Gaussian mosaic.
    
    If curvatures are set to zero or are absent, array
    is considered to be flat.
    
    Scattering vector is perpendicular to surface. Crystal is oriented
    parallel to beam incident on crystal before rotation, and lies in
    vertical plane.
    


.. rubric:: Basic Structure of **NXcrystal**

.. code-block:: text
    :linenos:
    
    NXcrystal (base class, version 1.0)
      azimuthal_angle:NX_FLOAT[i]
      bragg_angle:NX_FLOAT[i]
      chemical_formula:NX_CHAR
      curvature_horizontal:NX_FLOAT
      curvature_vertical:NX_FLOAT
      cut_angle:NX_FLOAT
      cylindrical_orientation_angle:NX_NUMBER
      d_spacing:NX_FLOAT
      density:NX_NUMBER
      is_cylindrical:NX_BOOLEAN
      mosaic_horizontal:NX_FLOAT
      mosaic_vertical:NX_FLOAT
      order_no:NX_INT
      orientation_matrix:NX_FLOAT[3,3]
      polar_angle:NX_FLOAT[i]
      reflection:NX_INT[3]
      scattering_vector:NX_FLOAT
      segment_columns:NX_FLOAT
      segment_gap:NX_FLOAT
      segment_height:NX_FLOAT
      segment_rows:NX_FLOAT
      segment_thickness:NX_FLOAT
      segment_width:NX_FLOAT
      space_group:NX_CHAR
      temperature:NX_FLOAT
      temperature_coefficient:NX_FLOAT
      thickness:NX_FLOAT
      type:NX_CHAR
      unit_cell:NX_FLOAT[n_comp,6]
      unit_cell_a:NX_FLOAT
      unit_cell_alpha:NX_FLOAT
      unit_cell_b:NX_FLOAT
      unit_cell_beta:NX_FLOAT
      unit_cell_c:NX_FLOAT
      unit_cell_gamma:NX_FLOAT
      unit_cell_volume:NX_FLOAT
      usage:NX_CHAR
      wavelength:NX_FLOAT[i]
      reflectivity:NXdata
      transmission:NXdata
      NXgeometry
      temperature_log:NXlog
      shape:NXshape
    

.. rubric:: Symbols used in definition of **NXcrystal**

These symbols will be used below to coordinate dimensions with the same lengths.

+------------+------------------------------------------------+
| Symbol     | Description                                    |
+============+================================================+
| ``n_comp`` | number of different unit cells to be described |
+------------+------------------------------------------------+
| ``i``      | number of wavelengths                          |
+------------+------------------------------------------------+




.. rubric:: Comprehensive Structure of **NXcrystal**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
