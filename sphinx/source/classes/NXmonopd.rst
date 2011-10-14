..  _NXmonopd:

########
NXmonopd
########

.. index::  ! classes - applications; NXmonopd

category
    applications

NXDL source:
    NXmonopd
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXmonopd.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXmonopd.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcrystal`, :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXsample`, :ref:`NXsource`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXmonopd
===========================

::

    NXmonopd (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        start_time:NX_DATE_TIME
        title:NX_CHAR
        NXdata
          data --> /NXentry/NXinstrument/NXdetector/data
          polar_angle --> /NXentry/NXinstrument/NXdetector/polar_angle
        NXinstrument
          NXcrystal
            wavelength:NX_FLOAT[i]
          NXdetector
            data:NX_INT[ndet]
            polar_angle:NX_FLOAT[ndet]
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        NXmonitor
          integral:NX_FLOAT
          mode:NX_CHAR
          preset:NX_FLOAT
        NXsample
          name:NX_CHAR
          rotation_angle:NX_FLOAT
    
