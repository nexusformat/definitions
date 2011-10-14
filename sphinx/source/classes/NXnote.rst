..  _NXnote:

######
NXnote
######

.. index::  ! classes - base_classes; NXnote

category
    base_classes

NXDL source:
    NXnote
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXnote.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXnote.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXnote
=========================

::

    NXnote (base class, version 1.0)
      author:NX_CHAR
      data:NX_BINARY
      date:NX_DATE_TIME
      description:NX_CHAR
      file_name:NX_CHAR
      type:NX_CHAR
    
