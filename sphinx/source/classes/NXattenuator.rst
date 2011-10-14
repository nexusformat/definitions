..  _NXattenuator:

############
NXattenuator
############

.. index::  ! classes - base_classes; NXattenuator

category
    base_classes

NXDL source:
    NXattenuator
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXattenuator.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXattenuator.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXattenuator
===============================

::

    NXattenuator (base class, version 1.0)
      absorption_cross_section:NX_FLOAT
      attenuator_transmission:NX_FLOAT
      distance:NX_FLOAT
      scattering_cross_section:NX_FLOAT
      status:NX_CHAR
        @time
      thickness:NX_FLOAT
      type:NX_CHAR
    
