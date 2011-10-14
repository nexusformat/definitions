..  _NXtomoproc:

##########
NXtomoproc
##########

.. index::  ! classes - applications; NXtomoproc

category
    applications

NXDL source:
    NXtomoproc
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXtomoproc.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXtomoproc.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXparameters`, :ref:`NXprocess`, :ref:`NXsample`, :ref:`NXsource`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXtomoproc
=============================

::

    NXtomoproc (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        title:NX_CHAR
        data:NXdata
          data:NX_INT[nx,nx,nz]
            @transform
            @offset
            @scaling
          x:NX_FLOAT[nx]
          y:NX_FLOAT[ny]
          z:NX_FLOAT[nz]
        NXinstrument
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        reconstruction:NXprocess
          date:NX_DATE_TIME
          program:NX_CHAR
          version:NX_CHAR
          parameters:NXparameters
            raw_file:NX_CHAR
        NXsample
          name:NX_CHAR
    
