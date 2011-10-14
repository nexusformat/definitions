..  _NXsolenoid_magnet:

#################
NXsolenoid_magnet
#################

.. index::  ! classes - contributed_definitions; NXsolenoid_magnet

category
    contributed_definitions

NXDL source:
    NXsolenoid_magnet
    
    (http://svn.nexusformat.org/definitions/trunk/contributed_definitions/NXsolenoid_magnet.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXsolenoid_magnet.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXlog`, :ref:`NXlog`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXsolenoid_magnet
====================================

::

    NXsolenoid_magnet (contributed definition, version 1.0)
      (base class definition, NXentry or NXsubentry not found)
      beamline_distance:NX_FLOAT
      description:NX_CHAR
      set_current:NX_FLOAT
      read_current:NXlog
        value:NX_CHAR
      read_voltage:NXlog
        value:NX_CHAR
    
