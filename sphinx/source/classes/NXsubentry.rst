..  _NXsubentry:

##########
NXsubentry
##########

.. index::  ! classes - base_classes; NXsubentry

category
    base_classes

NXDL source:
    NXsubentry
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXsubentry.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXsubentry.nxdl.xml 811 2011-02-04 16:02:51Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXcharacterization`, :ref:`NXdata`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXnote`, :ref:`NXnote`, :ref:`NXnote`, :ref:`NXprocess`, :ref:`NXsample`, :ref:`NXuser`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXsubentry
=============================

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
    
