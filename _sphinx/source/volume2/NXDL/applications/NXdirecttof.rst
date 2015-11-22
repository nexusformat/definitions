..  _NXdirecttof:

###########
NXdirecttof
###########

.. index::  ! . NXDL applications; NXdirecttof

category:
    applications

NXDL source:
    NXdirecttof
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXdirecttof.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXtofraw`

other classes included:
    :ref:`NXentry`, :ref:`NXfermi_chopper`, :ref:`NXinstrument`

documentation:
    This is a application definition for raw data from a direct geometry TOF spectrometer
    


.. rubric:: Basic Structure of **NXdirecttof**

.. code-block:: text
    :linenos:
    
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
    

.. rubric:: Symbols used in definition of **NXdirecttof**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXdirecttof**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
