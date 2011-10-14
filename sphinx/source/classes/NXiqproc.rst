..  _NXiqproc:

########
NXiqproc
########

.. index::  ! classes - applications; NXiqproc

category
    applications

NXDL source:
    NXiqproc
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXiqproc.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXiqproc.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXparameters`, :ref:`NXparameters`, :ref:`NXprocess`, :ref:`NXsample`, :ref:`NXsource`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXiqproc
===========================

::

    NXiqproc (application definition, version 1.0b)
      (overlays NXentry)
      NXentry
        @entry
        definition:NX_CHAR
        title:NX_CHAR
        NXdata
          data:NX_INT[NE,NQX,NQY]
          qx:NX_CHAR
          qy:NX_CHAR
          variable:NX_CHAR
            @varied_variable
        instrument:NXinstrument
          name:NX_CHAR
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        reduction:NXprocess
          program:NX_CHAR
          version:NX_CHAR
          input:NXparameters
            filenames:NX_CHAR
          output:NXparameters
        NXsample
          name:NX_CHAR
    
