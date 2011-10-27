..  _NXsolenoid_magnet:

#################
NXsolenoid_magnet
#################

.. index::  ! . NXDL contributed_definitions; NXsolenoid_magnet

category:
    contributed_definitions

NXDL source:
    NXsolenoid_magnet
    
    (http://svn.nexusformat.org/definitions/trunk/contributed_definitions/NXsolenoid_magnet.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXlog`

documentation:
    definition for a solenoid magnet.
    


.. rubric:: Basic Structure of **NXsolenoid_magnet**

.. code-block:: text
    :linenos:
    
    NXsolenoid_magnet (contributed definition, version 1.0)
      (base class definition, NXentry or NXsubentry not found)
      beamline_distance:NX_FLOAT
      description:NX_CHAR
      set_current:NX_FLOAT
      read_current:NXlog
        value:NX_CHAR
      read_voltage:NXlog
        value:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXsolenoid_magnet**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXsolenoid_magnet**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
