..  _NXtechnical_data:

################
NXtechnical_data
################

.. index::  ! classes - contributed_definitions; NXtechnical_data

category
    contributed_definitions

NXDL source:
    NXtechnical_data
    
    (http://svn.nexusformat.org/definitions/trunk/contributed_definitions/NXtechnical_data.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXtechnical_data.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXtechnical_data
===================================

::

    NXtechnical_data (contributed definition, version 1.0)
      (base class definition, NXentry or NXsubentry not found)
      data:NX_NUMBER
        @units
        @timestamp
        @description
      description:NX_CHAR
        @description
    
