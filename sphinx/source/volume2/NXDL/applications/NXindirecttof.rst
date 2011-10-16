..  _NXindirecttof:

#############
NXindirecttof
#############

.. index::  ! . NXDL applications; NXindirecttof

category:
    applications

NXDL source:
    NXindirecttof
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXindirecttof.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXtofraw`

other classes included:
    :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonochromator`

symbol list:
    none

documentation:
    This is a application definition for raw data from a direct geometry TOF spectrometer
    


.. rubric:: Basic Structure of **NXindirecttof**

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
    

.. rubric:: Comprehensive Structure of **NXindirecttof**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        