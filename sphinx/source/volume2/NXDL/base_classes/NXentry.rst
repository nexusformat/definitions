..  _NXentry:

#######
NXentry
#######

.. index::  ! . NXDL base_classes; NXentry

category:
    base_classes

NXDL source:
    NXentry
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXentry.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcharacterization`, :ref:`NXdata`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXnote`, :ref:`NXprocess`, :ref:`NXsample`, :ref:`NXsubentry`, :ref:`NXuser`

symbol list:
    none

documentation:
    (required) Template of the top-level NeXus group which contains all the data and associated
    information that comprise a single measurement. It is mandatory that there is at least one
    group of this type in the NeXus file.
    


.. rubric:: Basic Structure of **NXentry**

::

    NXentry (base class, version 1.0)
      @IDF_Version
      collection_description:NX_CHAR
      collection_identifier:NX_CHAR
      collection_time:NX_FLOAT
      definition:NX_CHAR
        @version
        @URL
      definition_local:NX_CHAR
        @version
        @URL
      duration:NX_INT
      end_time:NX_DATE_TIME
      entry_identifier:NX_CHAR
      experiment_description:NX_CHAR
      experiment_identifier:NX_CHAR
      pre_sample_flightpath:NX_FLOAT
      program_name:NX_CHAR
        @version
        @configuration
      revision:NX_CHAR
        @comment
      run_cycle:NX_CHAR
      start_time:NX_DATE_TIME
      title:NX_CHAR
      NXcharacterization
      NXdata
      NXinstrument
      NXmonitor
      experiment_documentation:NXnote
      notes:NXnote
      thumbnail:NXnote
        @mime_type
      NXprocess
      NXsample
      NXsubentry
      NXuser
    

.. rubric:: Comprehensive Structure of **NXentry**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        