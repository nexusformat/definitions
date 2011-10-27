..  _NXbeamline:

##########
NXbeamline
##########

.. index::  ! . NXDL contributed_definitions; NXbeamline

category:
    contributed_definitions

NXDL source:
    NXbeamline
    
    (http://svn.nexusformat.org/definitions/trunk/contributed_definitions/NXbeamline.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXaperture`, :ref:`NXbending_magnet`, :ref:`NXcollection`, :ref:`NXelectrostatic_kicker`, :ref:`NXmagnetic_kicker`, :ref:`NXquadrupole_magnet`, :ref:`NXseparator`, :ref:`NXsolenoid_magnet`, :ref:`NXspin_rotator`

documentation:
    container for elements describing beamline.
    


.. rubric:: Basic Structure of **NXbeamline**

.. code-block:: text
    :linenos:
    
    NXbeamline (contributed definition, version 1.0)
      (base class definition, NXentry or NXsubentry not found)
      beamline:NX_CHAR
      NXaperture
      NXbending_magnet
      diagnostics:NXcollection
      NXelectrostatic_kicker
      NXmagnetic_kicker
      NXquadrupole_magnet
      NXseparator
      NXsolenoid_magnet
      NXspin_rotator
    

.. rubric:: Symbols used in definition of **NXbeamline**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXbeamline**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
