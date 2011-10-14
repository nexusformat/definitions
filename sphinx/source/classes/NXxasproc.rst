..  _NXxasproc:

#########
NXxasproc
#########

.. index::  ! classes - applications; NXxasproc

category
    applications

NXDL source:
    NXxasproc
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxasproc.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXxasproc.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXentry`, :ref:`NXparameters`, :ref:`NXprocess`, :ref:`NXsample`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXxasproc
============================

::

    NXxasproc (application definition, version 1.0)
      (overlays NXentry)
      NXentry
        @entry
        definition:NX_CHAR
        title:NX_CHAR
        NXdata
          data:NX_FLOAT[np]
          energy:NX_CHAR
        XAS_data_reduction:NXprocess
          date:NX_DATE_TIME
          program:NX_CHAR
          version:NX_CHAR
          parameters:NXparameters
            raw_file:NX_CHAR
        NXsample
          name:NX_CHAR
    
