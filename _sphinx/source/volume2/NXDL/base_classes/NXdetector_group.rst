..  _NXdetector_group:

################
NXdetector_group
################

.. index::  ! . NXDL base_classes; NXdetector_group

category:
    base_classes

NXDL source:
    NXdetector_group
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXdetector_group.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

documentation:
    This class is used to allow a logical
    grouping of detector elements (e.g. which tube, bank or group of banks) to be
    recorded in the file. As well as allowing you to e.g just select the "left" or
    "east" detectors, it may also be useful for determining which elements belong to the
    same PSD tube and hence have e.g. the same dead time.
    
    For example, if we had "bank1" composed
    of "tube1", "tube2" and "tube3" then group_names would be the string "bank1,
    bank1/tube1, bank1/tube2,bank1/tube3" group_index would be {1,2,3,4} group_parent
    would be {-1,1,1,1}
    
    The mapping array is interpreted as
    group 1 is a top level group containing groups 2, 3 and 4
    
    A group_index array in
    NXdetector give the base group for a detector element.
    


.. rubric:: Basic Structure of **NXdetector_group**

.. code-block:: text
    :linenos:
    
    NXdetector_group (base class, version 1.0)
      group_index:NX_INT[i]
      group_names:NX_CHAR
      group_parent:NX_INT[]
      group_type:NX_INT[]
    

.. rubric:: Symbols used in definition of **NXdetector_group**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXdetector_group**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
