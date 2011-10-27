..  _NXxasproc:

#########
NXxasproc
#########

.. index::  ! . NXDL applications; NXxasproc

category:
    applications

NXDL source:
    NXxasproc
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxasproc.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXentry`, :ref:`NXparameters`, :ref:`NXprocess`, :ref:`NXsample`

documentation:
    This is an application definition for processed data from XAS. This
    is energy versus I(i)/I(a)
    


.. rubric:: Basic Structure of **NXxasproc**

.. code-block:: text
    :linenos:
    
    NXxasproc (application definition, version 1.0)
      (overlays NXentry)
      NXentry
        @entry
        definition:NX_CHAR
        title:NX_CHAR
        NXdata
          data:NX_FLOAT[np]
          energy:NX_CHAR
        XAS_data_reduction:NXprocess
          date:NX_DATE_TIME
          program:NX_CHAR
          version:NX_CHAR
          parameters:NXparameters
            raw_file:NX_CHAR
        NXsample
          name:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXxasproc**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXxasproc**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
