..  _NXelectrostatic_kicker:

######################
NXelectrostatic_kicker
######################

.. index::  ! classes - contributed_definitions; NXelectrostatic_kicker

category
    contributed_definitions

NXDL source:
    NXelectrostatic_kicker
    
    (http://svn.nexusformat.org/definitions/trunk/contributed_definitions/NXelectrostatic_kicker.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXelectrostatic_kicker.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXlog`, :ref:`NXlog`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXelectrostatic_kicker
=========================================

::

    NXelectrostatic_kicker (contributed definition, version 1.0)
      (base class definition, NXentry or NXsubentry not found)
      beamline_distance:NX_FLOAT
      description:NX_CHAR
      set_current:NX_FLOAT
      set_voltage:NX_FLOAT
      timing:NX_FLOAT
        @description
      read_current:NXlog
        value:NX_CHAR
      read_voltage:NXlog
        value:NX_CHAR
    
