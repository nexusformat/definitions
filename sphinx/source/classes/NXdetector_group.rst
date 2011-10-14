..  _NXdetector_group:

################
NXdetector_group
################

.. index::  ! classes - base_classes; NXdetector_group

category
    base_classes

NXDL source:
    NXdetector_group
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXdetector_group.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXdetector_group.nxdl.xml 829 2011-02-20 15:04:56Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXdetector_group
===================================

::

    NXdetector_group (base class, version 1.0)
      group_index:NX_INT[i]
      group_names:NX_CHAR
      group_parent:NX_INT[]
      group_type:NX_INT[]
    
