..  _NXvelocity_selector:

###################
NXvelocity_selector
###################

.. index::  ! . NXDL base_classes; NXvelocity_selector

category:
    base_classes

NXDL source:
    NXvelocity_selector
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXvelocity_selector.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`

documentation:
    This is the description for a (typically neutron) velocity selector
    


.. rubric:: Basic Structure of **NXvelocity_selector**

.. code-block:: text
    :linenos:
    
    NXvelocity_selector (base class, version 1.0)
      height:NX_FLOAT
      length:NX_FLOAT
      num:NX_INT
      radius:NX_FLOAT
      rotation_speed:NX_FLOAT
      spwidth:NX_FLOAT
      table:NX_FLOAT
      twist:NX_FLOAT
      type:NX_CHAR
      wavelength:NX_FLOAT
      wavelength_spread:NX_FLOAT
      width:NX_FLOAT
      geometry:NXgeometry
    

.. rubric:: Symbols used in definition of **NXvelocity_selector**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXvelocity_selector**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
