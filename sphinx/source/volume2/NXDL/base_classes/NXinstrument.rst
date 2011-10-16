..  _NXinstrument:

############
NXinstrument
############

.. index::  ! . NXDL base_classes; NXinstrument

category:
    base_classes

NXDL source:
    NXinstrument
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXinstrument.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXaperture`, :ref:`NXattenuator`, :ref:`NXbeam_stop`, :ref:`NXbeam`, :ref:`NXbending_magnet`, :ref:`NXcollimator`, :ref:`NXcrystal`, :ref:`NXdetector`, :ref:`NXdisk_chopper`, :ref:`NXfermi_chopper`, :ref:`NXfilter`, :ref:`NXflipper`, :ref:`NXguide`, :ref:`NXinsertion_device`, :ref:`NXmirror`, :ref:`NXmoderator`, :ref:`NXpolarizer`, :ref:`NXsource`, :ref:`NXvelocity_selector`

symbol list:
    none

documentation:
    Template of instrument descriptions comprising various beamline components.
    Each component will also be a NeXus group defined by its distance from the
    sample. Negative distances represent beamline components that are before the
    sample while positive distances represent components that are after the sample.
    This device allows the unique identification of beamline components in a way
    that is valid for both reactor and pulsed instrumentation.
    


.. rubric:: Basic Structure of **NXinstrument**

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
    

.. rubric:: Comprehensive Structure of **NXinstrument**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        