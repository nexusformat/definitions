..  _NXbeamline:

##########
NXbeamline
##########

.. index::  ! classes - contributed_definitions; NXbeamline

category
    contributed_definitions

NXDL source:
    NXbeamline
    
    (http://svn.nexusformat.org/definitions/trunk/contributed_definitions/NXbeamline.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXbeamline.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXaperture`, :ref:`NXbending_magnet`, :ref:`NXcollection`, :ref:`NXelectrostatic_kicker`, :ref:`NXmagnetic_kicker`, :ref:`NXquadrupole_magnet`, :ref:`NXseparator`, :ref:`NXsolenoid_magnet`, :ref:`NXspin_rotator`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXbeamline
=============================

::

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
    
