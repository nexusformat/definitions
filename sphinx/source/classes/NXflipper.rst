..  _NXflipper:

#########
NXflipper
#########

.. index::  ! classes - base_classes; NXflipper

category
    base_classes

NXDL source:
    NXflipper
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXflipper.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXflipper.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXflipper
============================

::

    NXflipper (base class, version 1.0)
      comp_current:NX_FLOAT
      comp_turns:NX_FLOAT
      flip_current:NX_FLOAT
      flip_turns:NX_FLOAT
      guide_current:NX_FLOAT
      guide_turns:NX_FLOAT
      thickness:NX_FLOAT
      type:NX_CHAR
    
