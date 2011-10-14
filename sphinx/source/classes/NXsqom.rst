..  _NXsqom:

######
NXsqom
######

.. index::  ! classes - applications; NXsqom

category
    applications

NXDL source:
    NXsqom
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXsqom.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXsqom.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXparameters`, :ref:`NXparameters`, :ref:`NXprocess`, :ref:`NXsample`, :ref:`NXsource`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXsqom
=========================

::

    NXsqom (application definition, version 1.0b)
      (overlays NXentry)
      NXentry
        @entry
        definition:NX_CHAR
        title:NX_CHAR
        NXdata
          data:NX_INT[NP]
          en:NX_FLOAT[NP]
          qx:NX_CHAR
          qy:NX_CHAR
          qz:NX_CHAR
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
    
