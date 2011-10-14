..  _NXscan:

######
NXscan
######

.. index::  ! classes - applications; NXscan

category
    applications

NXDL source:
    NXscan
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXscan.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXscan.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXsample`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXscan
=========================

::

    NXscan (application definition, version 1.0b)
      (overlays NXentry)
      NXentry
        definition:NX_CHAR
        end_time:NX_DATE_TIME
        start_time:NX_DATE_TIME
        title:NX_CHAR
        NXdata
          data --> /NXentry/NXinstrument/NXdetector/data
          rotation_angle --> /NXentry/NXsample/rotation_angle
        NXinstrument
          NXdetector
            data:NX_INT[NP,xdim,ydim]
        NXmonitor
          data:NX_INT[NP]
        NXsample
          rotation_angle:NX_FLOAT[NP]
    
