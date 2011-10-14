..  _NXinstrument:

############
NXinstrument
############

.. index::  ! classes - base_classes; NXinstrument

category
    base_classes

NXDL source:
    NXinstrument
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXinstrument.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXinstrument.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXaperture`, :ref:`NXattenuator`, :ref:`NXbeam_stop`, :ref:`NXbeam`, :ref:`NXbending_magnet`, :ref:`NXcollimator`, :ref:`NXcrystal`, :ref:`NXdetector`, :ref:`NXdisk_chopper`, :ref:`NXfermi_chopper`, :ref:`NXfilter`, :ref:`NXflipper`, :ref:`NXguide`, :ref:`NXinsertion_device`, :ref:`NXmirror`, :ref:`NXmoderator`, :ref:`NXpolarizer`, :ref:`NXsource`, :ref:`NXvelocity_selector`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXinstrument
===============================

::

    NXinstrument (base class, version 1.0)
      name:NX_CHAR
        @short_name
      NXaperture
      NXattenuator
      NXbeam
      NXbeam_stop
      NXbending_magnet
      NXcollimator
      NXcrystal
      NXdetector
      NXdisk_chopper
      NXfermi_chopper
      NXfilter
      NXflipper
      NXguide
      NXinsertion_device
      NXmirror
      NXmoderator
      NXpolarizer
      NXsource
      NXvelocity_selector
    
