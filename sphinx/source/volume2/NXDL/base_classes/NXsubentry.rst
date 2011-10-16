..  _NXsubentry:

##########
NXsubentry
##########

.. index::  ! . NXDL base_classes; NXsubentry

category:
    base_classes

NXDL source:
    NXsubentry
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXsubentry.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcharacterization`, :ref:`NXdata`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXnote`, :ref:`NXprocess`, :ref:`NXsample`, :ref:`NXuser`

symbol list:
    none

documentation:
    NXsubentry is a base class virtually identical to NXentry
    and is used as the (overlay) location for application definitions.
    Use a separate NXsubentry for each application definition.
    
    To use NXsubentry with a hypothetical application definition
    called NXmyappdef:
    
    Create a group with attribute
    NX_class="NXsubentry".
    
    Within that group, create a field called
    definition="NXmyappdef".
    
    There are two optional attributes of definition:
    version and URL
    
    The intended use is to define application definitions for a
    multi-technique NXentry. Previously, an application definition
    replaced NXentry with its own definition.
    With the increasing popularity of instruments combining
    multiple techniques for data collection (such as SAXS/WAXS instruments),
    it was recognized the application definitions must be entered in the NeXus
    data file tree as children of NXentry.
    


.. rubric:: Basic Structure of **NXsubentry**

::

    NXsubentry (base class, version 1.0)
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
      NXuser
    

.. rubric:: Comprehensive Structure of **NXsubentry**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        