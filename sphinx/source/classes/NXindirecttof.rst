..  _NXindirecttof:

#############
NXindirecttof
#############

.. index::  ! classes - applications; NXindirecttof

category
    applications

NXDL source:
    NXindirecttof
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXindirecttof.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXindirecttof.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXtofraw`

other classes included:
    :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonochromator`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXindirecttof
================================

::

    NXindirecttof (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        start_time:NX_DATE_TIME
        title:NX_CHAR
        NXinstrument
          analyser:NXmonochromator
            distance:NX_FLOAT[ndet]
            energy:NX_FLOAT[nDet]
            polar_angle:NX_FLOAT[ndet]
    
