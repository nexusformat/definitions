..  _NXsource:

########
NXsource
########

.. index::  ! . NXDL base_classes; NXsource

category:
    base_classes

NXDL source:
    NXsource
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXsource.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`, :ref:`NXnote`

documentation:
    Template of the neutron or x-ray source, insertion devices and/or moderators.
    


.. rubric:: Basic Structure of **NXsource**

.. code-block:: text
    :linenos:
    
    NXsource (base class, version 1.0)
      bunch_distance:NX_FLOAT
      bunch_length:NX_FLOAT
      current:NX_FLOAT
      distance:NX_FLOAT
      emittance_x:NX_FLOAT
      emittance_y:NX_FLOAT
      energy:NX_FLOAT
      flux:NX_FLOAT
      frequency:NX_FLOAT
      last_fill:NX_NUMBER
        @time
      mode:NX_CHAR
      name:NX_CHAR
        @short_name
      number_of_bunches:NX_INT
      period:NX_FLOAT
      power:NX_FLOAT
      probe:NX_CHAR
      pulse_width:NX_FLOAT
      sigma_x:NX_FLOAT
      sigma_y:NX_FLOAT
      target_material:NX_CHAR
      top_up:NX_BOOLEAN
      type:NX_CHAR
      voltage:NX_FLOAT
      bunch_pattern:NXdata
        title:NX_CHAR
      pulse_shape:NXdata
      distribution:NXdata
      geometry:NXgeometry
      notes:NXnote
    

.. rubric:: Symbols used in definition of **NXsource**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXsource**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
