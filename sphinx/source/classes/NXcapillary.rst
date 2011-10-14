..  _NXcapillary:

###########
NXcapillary
###########

.. index::  ! classes - base_classes; NXcapillary

category
    base_classes

NXDL source:
    NXcapillary
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXcapillary.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXcapillary.nxdl.xml 662 2010-10-21 15:47:35Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdata`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXcapillary
==============================

::

    NXcapillary (base class, version 1.0)
      accepting_aperture:NX_FLOAT
      focal_size:NX_FLOAT
      manufacturer:NX_CHAR
      maximum_incident_angle:NX_FLOAT
      type:NX_CHAR
      working_distance:NX_FLOAT
      gain:NXdata
      transmission:NXdata
    
