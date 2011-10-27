..  _NXiqproc:

########
NXiqproc
########

.. index::  ! . NXDL applications; NXiqproc

category:
    applications

NXDL source:
    NXiqproc
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXiqproc.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXparameters`, :ref:`NXprocess`, :ref:`NXsample`, :ref:`NXsource`

documentation:
    Actually this is a template from which to start an application definition.
    


.. rubric:: Basic Structure of **NXiqproc**

.. code-block:: text
    :linenos:
    
    NXiqproc (application definition, version 1.0b)
      (overlays NXentry)
      NXentry
        @entry
        definition:NX_CHAR
        title:NX_CHAR
        NXdata
          data:NX_INT[NE,NQX,NQY]
          qx:NX_CHAR
          qy:NX_CHAR
          variable:NX_CHAR
            @varied_variable
        instrument:NXinstrument
          name:NX_CHAR
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        reduction:NXprocess
          program:NX_CHAR
          version:NX_CHAR
          input:NXparameters
            filenames:NX_CHAR
          output:NXparameters
        NXsample
          name:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXiqproc**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXiqproc**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
