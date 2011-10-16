..  _NXarchive:

#########
NXarchive
#########

.. index::  ! . NXDL applications; NXarchive

category:
    applications

NXDL source:
    NXarchive
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXarchive.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXsample`, :ref:`NXsource`, :ref:`NXuser`

symbol list:
    none

documentation:
    This is a definition for data to be archived by ICAT (see:
    http://www.icatproject.org/),
    
    .. COMMENT: text from the icatproject.org site
    the database (with supporting software) that provides an
    interface to all ISIS experimental data and will provide
    a mechanism to link all aspects of ISIS research from
    proposal through to publication.
    


.. rubric:: Basic Structure of **NXarchive**

::

    NXarchive (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        @index
        collection_description:NX_CHAR
        collection_identifier:NX_CHAR
        collection_time:NX_FLOAT
        definition:NX_CHAR
        duration:NX_FLOAT
        end_time:NX_DATE_TIME
        entry_identifier:NX_CHAR
        experiment_description:NX_CHAR
        experiment_identifer:NX_CHAR
        program:NX_CHAR
          @version
        release_date:NX_CHAR
        revision:NX_CHAR
        run_cycle:NX_CHAR
        start_time:NX_DATE_TIME
        title:NX_CHAR
        instrument:NXinstrument
          description:NX_CHAR
          name:NX_CHAR
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        sample:NXsample
          chemical_formula:NX_CHAR
          description:NX_CHAR
          electric_field:NX_FLOAT
          magnetic_field:NX_FLOAT
          name:NX_CHAR
          preparation_date:NX_CHAR
          pressure:NX_FLOAT
          sample_id:NX_CHAR
          situation:NX_CHAR
          stress_field:NX_FLOAT
          temperature:NX_FLOAT
          type:NX_CHAR
        user:NXuser
          facility_user_id:NX_CHAR
          name:NX_CHAR
          role:NX_CHAR
    

.. rubric:: Comprehensive Structure of **NXarchive**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        