..  _NXflipper:

#########
NXflipper
#########

.. index::  ! . NXDL base_classes; NXflipper

category:
    base_classes

NXDL source:
    NXflipper
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXflipper.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

documentation:
    Template of a beamline spin flipper.
    


.. rubric:: Basic Structure of **NXflipper**

.. code-block:: text
    :linenos:
    
    NXflipper (base class, version 1.0)
      comp_current:NX_FLOAT
      comp_turns:NX_FLOAT
      flip_current:NX_FLOAT
      flip_turns:NX_FLOAT
      guide_current:NX_FLOAT
      guide_turns:NX_FLOAT
      thickness:NX_FLOAT
      type:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXflipper**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXflipper**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
