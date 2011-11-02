..  _NXxas:

#####
NXxas
#####

.. index::  ! . NXDL applications; NXxas

category:
    applications

NXDL source:
    NXxas
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxas.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXmonochromator`, :ref:`NXsample`, :ref:`NXsource`

documentation:
    This is an application definition for raw data from an X-ray absorption
    spectroscopy experiment. This is essentially a scan on energy versus incoming/
    absorbed beam
    


.. rubric:: Basic Structure of **NXxas**

.. code-block:: text
    :linenos:
    
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
    

.. rubric:: Symbols used in definition of **NXxas**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXxas**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
