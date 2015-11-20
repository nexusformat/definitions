..  _NXsai_controller:

################
NXsai_controller
################

.. index::  ! . NXDL contributed_definitions; NXsai_controller

category:
    contributed_definitions

NXDL source:
    NXsai_controller
    
    (http://svn.nexusformat.org/definitions/trunk/contributed_definitions/NXsai_controller.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXtechnical_data`

documentation:
    (definition implied by usage) Subclass of NXinstrument used by Soleil. This class appears
    in the example data files provided from Soleil. This class should be considered as a base
    class (and relocated there, once approved by the NIAC).
    


.. rubric:: Basic Structure of **NXsai_controller**

.. code-block:: text
    :linenos:
    
    NXsai_controller (contributed definition, version 1.0)
      (base class definition, NXentry or NXsubentry not found)
      Frequency:NXtechnical_data
      IntegrationTime:NXtechnical_data
      TriggerNumber:NXtechnical_data
    

.. rubric:: Symbols used in definition of **NXsai_controller**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXsai_controller**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
