..  _NXbending_magnet:

################
NXbending_magnet
################

.. index::  ! . NXDL base_classes; NXbending_magnet

category:
    base_classes

NXDL source:
    NXbending_magnet
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXbending_magnet.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`

documentation:
    description for a bending magnet
    


.. rubric:: Basic Structure of **NXbending_magnet**

.. code-block:: text
    :linenos:
    
    NXbending_magnet (base class, version 1.0)
      accepted_photon_beam_divergence:NX_FLOAT
      bending_radius:NX_FLOAT
      critical_energy:NX_FLOAT
      divergence_x_minus:NX_FLOAT
      divergence_x_plus:NX_FLOAT
      divergence_y_minus:NX_FLOAT
      divergence_y_plus:NX_FLOAT
      magnetic_field:NX_FLOAT
      source_distance_x:NX_FLOAT
      source_distance_y:NX_FLOAT
      spectrum:NXdata
      NXgeometry
    

.. rubric:: Symbols used in definition of **NXbending_magnet**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXbending_magnet**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
