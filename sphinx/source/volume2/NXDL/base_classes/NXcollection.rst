..  _NXcollection:

############
NXcollection
############

.. index::  ! . NXDL base_classes; NXcollection

category:
    base_classes

NXDL source:
    NXcollection
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXcollection.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

documentation:
    Use NXcollection to gather together any set of terms.
    The original suggestion is to use this as a container
    class for the description of a beamline.
    
    For NeXus validation, NXcollection will always generate
    a warning since it is always an optional group.  Anything (groups, fields,
    or attributes) placed in
    an NXcollection group will not be validated.
    


.. rubric:: Basic Structure of **NXcollection**

.. code-block:: text
    :linenos:
    
    NXcollection (contributed definition, version 1.0)
      beamline:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXcollection**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXcollection**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
