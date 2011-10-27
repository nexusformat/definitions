..  _NXcollimator:

############
NXcollimator
############

.. index::  ! . NXDL base_classes; NXcollimator

category:
    base_classes

NXDL source:
    NXcollimator
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXcollimator.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`, :ref:`NXlog`

documentation:
    Template of a beamline collimator.
    


.. rubric:: Basic Structure of **NXcollimator**

.. code-block:: text
    :linenos:
    
    NXcollimator (base class, version 1.0)
      absorbing_material:NX_CHAR
      blade_spacing:NX_FLOAT
      blade_thickness:NX_FLOAT
      divergence_x:NX_FLOAT
      divergence_y:NX_FLOAT
      frequency:NX_FLOAT
      soller_angle:NX_FLOAT
      transmitting_material:NX_CHAR
      type:NX_CHAR
      NXgeometry
      frequency_log:NXlog
    

.. rubric:: Symbols used in definition of **NXcollimator**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXcollimator**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
