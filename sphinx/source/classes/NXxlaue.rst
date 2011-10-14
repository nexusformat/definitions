..  _NXxlaue:

#######
NXxlaue
#######

.. index::  ! classes - applications; NXxlaue

category
    applications

NXDL source:
    NXxlaue
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxlaue.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXxlaue.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXxrot`

other classes included:
    :ref:`NXdata`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXsource`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXxlaue
==========================

::

    NXxlaue (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        instrument:NXinstrument
          source:NXsource
            distribution:NXdata
              data:NX_CHAR
              wavelength:NX_CHAR
    
