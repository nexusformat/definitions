..  _NXquadrupole_magnet:

###################
NXquadrupole_magnet
###################

.. index::  ! . NXDL contributed_definitions; NXquadrupole_magnet

category:
    contributed_definitions

NXDL source:
    NXquadrupole_magnet
    
    (http://svn.nexusformat.org/definitions/trunk/contributed_definitions/NXquadrupole_magnet.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXlog`

documentation:
    definition for a quadrupole magnet.
    


.. rubric:: Basic Structure of **NXquadrupole_magnet**

.. code-block:: text
    :linenos:
    
    NXquadrupole_magnet (contributed definition, version 1.0)
      (base class definition, NXentry or NXsubentry not found)
      beamline_distance:NX_FLOAT
      description:NX_CHAR
      set_current:NX_FLOAT
      read_current:NXlog
        value:NX_CHAR
      read_voltage:NXlog
        value:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXquadrupole_magnet**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXquadrupole_magnet**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
