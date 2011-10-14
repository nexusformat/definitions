..  _NXxas:

#####
NXxas
#####

.. index::  ! classes - applications; NXxas

category
    applications

NXDL source:
    NXxas
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxas.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXxas.nxdl.xml 823 2011-02-16 15:12:48Z Mark Koennecke $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXmonochromator`, :ref:`NXsample`, :ref:`NXsource`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXxas
========================

::

    NXxas (application definition, version 1.0)
      (overlays NXentry)
      NXentry
        @entry
        definition:NX_CHAR
        start_time:NX_DATE_TIME
        title:NX_CHAR
        NXdata
          absorbed_beam --> /entry/instrument/absorbed_beam
          energy --> /entry/instrument/monochromator/energy
        NXinstrument
          incoming_beam:NXdetector
            data:NX_INT[np]
          absorbed_beam:NXdetector
            data:NX_INT[np]
          monochromator:NXmonochromator
            energy:NX_CHAR
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        NXmonitor
          data:NX_INT[np]
          mode:NX_CHAR
          preset:NX_FLOAT
        NXsample
          name:NX_CHAR
    
