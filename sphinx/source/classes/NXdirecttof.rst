..  _NXdirecttof:

###########
NXdirecttof
###########

.. index::  ! classes - applications; NXdirecttof

category
    applications

NXDL source:
    NXdirecttof
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXdirecttof.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXdirecttof.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXtofraw`

other classes included:
    :ref:`NXentry`, :ref:`NXfermi_chopper`, :ref:`NXinstrument`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXdirecttof
==============================

::

    NXdirecttof (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        start_time:NX_DATE_TIME
        title:NX_CHAR
        NXinstrument
          fermi_chopper:NXfermi_chopper
            energy:NX_FLOAT
            rotation_speed:NX_FLOAT
    
