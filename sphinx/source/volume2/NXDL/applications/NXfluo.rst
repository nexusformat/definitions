..  _NXfluo:

######
NXfluo
######

.. index::  ! . NXDL applications; NXfluo

category:
    applications

NXDL source:
    NXfluo
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXfluo.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXmonochromator`, :ref:`NXsample`, :ref:`NXsource`

symbol list:
    none

documentation:
    This is an application definition for raw data from an X-ray fluorescence
    experiment
    


.. rubric:: Basic Structure of **NXfluo**

::

    NXfluo (application definition, version 1.0)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        start_time:NX_DATE_TIME
        title:NX_CHAR
        NXdata
          data --> /entry/instrument/fluorecence/data
          energy --> /entry/instrument/fluorecence/energy
        NXinstrument
          fluorescence:NXdetector
            data:NX_INT[nenergy]
            energy:NX_FLOAT[nenergy]
          monochromator:NXmonochromator
            wavelength:NX_FLOAT
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        NXmonitor
          data:NX_INT
          mode:NX_CHAR
          preset:NX_FLOAT
        NXsample
          name:NX_CHAR
    

.. rubric:: Comprehensive Structure of **NXfluo**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        