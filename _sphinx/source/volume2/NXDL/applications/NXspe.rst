..  _NXspe:

#####
NXspe
#####

.. index::  ! . NXDL applications; NXspe

category:
    applications

NXDL source:
    NXspe
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXspe.nxdl.xml)

version:
    1.0

SVN Id:
    none

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcollection`, :ref:`NXdata`, :ref:`NXentry`, :ref:`NXfermi_chopper`, :ref:`NXinstrument`, :ref:`NXsample`

documentation:
    NXSPE Inelastic Format.  Application definition for NXSPE file format.
    


.. rubric:: Basic Structure of **NXspe**

.. code-block:: text
    :linenos:
    
    NXspe (application definition, version 1.0)
      (overlays NXentry)
      NXentry
        definition:NX_CHAR
          @version
        program_name:NX_CHAR
        NXSPE_info:NXcollection
          fixed_energy:NX_FLOAT
          ki_over_kf_scaling:NX_BOOLEAN
          psi:NX_FLOAT
        data:NXdata
          azimuthal:NX_FLOAT
          azimuthal_width:NX_FLOAT
          data:NX_NUMBER
          distance:NX_FLOAT
          energy:NX_FLOAT
          error:NX_NUMBER
          polar:NX_FLOAT
          polar_width:NX_FLOAT
        NXinstrument
          name:NX_CHAR
          NXfermi_chopper
            energy:NX_NUMBER
        NXsample
          rotation_angle:NX_NUMBER
          seblock:NX_CHAR
          temperature:NX_NUMBER
    

.. rubric:: Symbols used in definition of **NXspe**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXspe**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
