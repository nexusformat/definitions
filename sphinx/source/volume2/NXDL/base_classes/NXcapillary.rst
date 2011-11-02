..  _NXcapillary:

###########
NXcapillary
###########

.. index::  ! . NXDL base_classes; NXcapillary

category:
    base_classes

NXDL source:
    NXcapillary
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXcapillary.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`

documentation:
    This is a dictionary of field names to use for describing a capillary as used
    in X-ray beamlines. Based on information provided by Gerd Wellenreuther.
    


.. rubric:: Basic Structure of **NXcapillary**

.. code-block:: text
    :linenos:
    
    NXcapillary (base class, version 1.0)
      accepting_aperture:NX_FLOAT
      focal_size:NX_FLOAT
      manufacturer:NX_CHAR
      maximum_incident_angle:NX_FLOAT
      type:NX_CHAR
      working_distance:NX_FLOAT
      gain:NXdata
      transmission:NXdata
    

.. rubric:: Symbols used in definition of **NXcapillary**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXcapillary**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
