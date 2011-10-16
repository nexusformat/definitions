..  _NXcharacterization:

##################
NXcharacterization
##################

.. index::  ! . NXDL base_classes; NXcharacterization

category:
    base_classes

NXDL source:
    NXcharacterization
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXcharacterization.nxdl.xml)

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
    .. COMMENT: TODO: NXcharacterization needs proper documentation
    
    .. COMMENT: Template of the top-level NeXus group which contains
                all the data and associated information that comprise a
                single measurement.  It is mandatory that there is at least
                one group of this type in the NeXus file.
    


.. rubric:: Basic Structure of **NXcharacterization**

::

    NXcharacterization (base class, version 1.0)
      @source
      @location
      @mime_type
      definition:NX_CHAR
        @version
        @URL
    

.. rubric:: Comprehensive Structure of **NXcharacterization**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        