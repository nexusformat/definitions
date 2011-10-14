..  _NXseparator:

###########
NXseparator
###########

.. index::  ! classes - contributed_definitions; NXseparator

category
    contributed_definitions

NXDL source:
    NXseparator
    
    (http://svn.nexusformat.org/definitions/trunk/contributed_definitions/NXseparator.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXseparator.nxdl.xml 818 2011-02-04 23:25:25Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXlog`, :ref:`NXlog`, :ref:`NXlog`, :ref:`NXlog`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXseparator
==============================

::

    NXseparator (contributed definition, version 1.0)
      (base class definition, NXentry or NXsubentry not found)
      beamline_distance:NX_FLOAT
      description:NX_CHAR
      set_Bfield_current:NX_FLOAT
      set_Efield_voltage:NX_FLOAT
      read_Bfield_current:NXlog
        value:NX_CHAR
      read_Bfield_voltage:NXlog
        value:NX_CHAR
      read_Efield_current:NXlog
        value:NX_CHAR
      read_Efield_voltage:NXlog
        value:NX_CHAR
    
