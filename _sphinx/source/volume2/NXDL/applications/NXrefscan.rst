..  _NXrefscan:

#########
NXrefscan
#########

.. index::  ! . NXDL applications; NXrefscan

category:
    applications

NXDL source:
    NXrefscan
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXrefscan.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXmonochromator`, :ref:`NXsample`, :ref:`NXsource`

documentation:
    This is an application definition for a monochromatic scanning reflectometer.
    It does not have the information to calculate the resolution
    since it does not have any apertures.
    


.. rubric:: Basic Structure of **NXrefscan**

.. code-block:: text
    :linenos:
    
    NXrefscan (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        end_time:NX_DATE_TIME
        start_time:NX_DATE_TIME
        title:NX_CHAR
        data:NXdata
          data --> /NXentry/NXinstrument/NXdetector/data
          polar_angle --> /NXentry/NXinstrument/NXdetector/polar_angle
          rotation_angle --> /NXentry/NXsample/rotation_angle
        instrument:NXinstrument
          NXdetector
            data:NX_INT[NP]
            polar_angle:NX_FLOAT[NP]
          monochromator:NXmonochromator
            wavelength:NX_FLOAT
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        control:NXmonitor
          data:NX_FLOAT[NP]
          mode:NX_CHAR
          preset:NX_FLOAT
        sample:NXsample
          name:NX_CHAR
          rotation_angle:NX_FLOAT[NP]
    

.. rubric:: Symbols used in definition of **NXrefscan**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXrefscan**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
