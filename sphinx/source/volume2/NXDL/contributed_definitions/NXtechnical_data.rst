..  _NXtechnical_data:

################
NXtechnical_data
################

.. index::  ! . NXDL contributed_definitions; NXtechnical_data

category:
    contributed_definitions

NXDL source:
    NXtechnical_data
    
    (http://svn.nexusformat.org/definitions/trunk/contributed_definitions/NXtechnical_data.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    none

documentation:
    (definition implied by usage) Some measure of metadata not already considered by the other
    base classes. This class appears in the example data files provided from Soleil. This class
    should be considered as a base class (and relocated there, once approved by the NIAC). This
    class is used by Soleil as a child of (at least) these classes: NXsai_controller,
    NXdetector, NXsource
    


.. rubric:: Basic Structure of **NXtechnical_data**

::

    NXtechnical_data (contributed definition, version 1.0)
      (base class definition, NXentry or NXsubentry not found)
      data:NX_NUMBER
        @units
        @timestamp
        @description
      description:NX_CHAR
        @description
    

.. rubric:: Comprehensive Structure of **NXtechnical_data**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        