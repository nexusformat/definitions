..  _NXxlaueplate:

############
NXxlaueplate
############

.. index::  ! classes - applications; NXxlaueplate

category
    applications

NXDL source:
    NXxlaueplate
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxlaueplate.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXxlaueplate.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXxlaue`

other classes included:
    :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXxlaueplate
===============================

::

    NXxlaueplate (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        instrument:NXinstrument
          detector:NXdetector
            diameter:NX_FLOAT
    
