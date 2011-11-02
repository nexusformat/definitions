..  _NXpolarizer:

###########
NXpolarizer
###########

.. index::  ! . NXDL base_classes; NXpolarizer

category:
    base_classes

NXDL source:
    NXpolarizer
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXpolarizer.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

documentation:
    Template of a beamline spin polarizer.
    
    This is a draft and is subject to revision.
    


.. rubric:: Basic Structure of **NXpolarizer**

.. code-block:: text
    :linenos:
    
    NXpolarizer (base class, version 1.0)
      composition:NX_CHAR
      efficiency:NX_FLOAT
      reflection:NX_INT[3]
      type:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXpolarizer**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXpolarizer**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
