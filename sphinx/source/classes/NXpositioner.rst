..  _NXpositioner:

############
NXpositioner
############

.. index::  ! classes - base_classes; NXpositioner

category
    base_classes

NXDL source:
    NXpositioner
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXpositioner.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXpositioner.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXpositioner
===============================

::

    NXpositioner (base class, version 1.0)
      acceleration_time:NX_NUMBER
      controller_record:NX_CHAR
      description:NX_CHAR
      name:NX_CHAR
      raw_value:NX_NUMBER[n]
      soft_limit_max:NX_NUMBER
      soft_limit_min:NX_NUMBER
      target_value:NX_NUMBER[n]
      tolerance:NX_NUMBER[n]
      value:NX_NUMBER[n]
      velocity:NX_NUMBER
    
