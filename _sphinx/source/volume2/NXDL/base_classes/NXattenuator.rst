..  _NXattenuator:

############
NXattenuator
############

.. index::  ! . NXDL base_classes; NXattenuator

category:
    base_classes

NXDL source:
    NXattenuator
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXattenuator.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

documentation:
    Template of a beamline attenuator.
    If uncertain whether to use NXfilter (band-pass filter)
    or NXattenuator (reduces beam intensity), then use
    NXattenuator.
    


.. rubric:: Basic Structure of **NXattenuator**

.. code-block:: text
    :linenos:
    
    NXattenuator (base class, version 1.0)
      absorption_cross_section:NX_FLOAT
      attenuator_transmission:NX_FLOAT
      distance:NX_FLOAT
      scattering_cross_section:NX_FLOAT
      status:NX_CHAR
        @time
      thickness:NX_FLOAT
      type:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXattenuator**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXattenuator**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
