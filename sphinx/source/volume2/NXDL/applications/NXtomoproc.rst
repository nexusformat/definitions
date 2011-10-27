..  _NXtomoproc:

##########
NXtomoproc
##########

.. index::  ! . NXDL applications; NXtomoproc

category:
    applications

NXDL source:
    NXtomoproc
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXtomoproc.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXparameters`, :ref:`NXprocess`, :ref:`NXsample`, :ref:`NXsource`

documentation:
    This is an application definition for the final result of a tomography experiment: a 3D construction of some volume of physical properties.
    


.. rubric:: Basic Structure of **NXtomoproc**

.. code-block:: text
    :linenos:
    
    NXtomoproc (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        title:NX_CHAR
        data:NXdata
          data:NX_INT[nx,nx,nz]
            @transform
            @offset
            @scaling
          x:NX_FLOAT[nx]
          y:NX_FLOAT[ny]
          z:NX_FLOAT[nz]
        NXinstrument
          NXsource
            name:NX_CHAR
            probe:NX_CHAR
            type:NX_CHAR
        reconstruction:NXprocess
          date:NX_DATE_TIME
          program:NX_CHAR
          version:NX_CHAR
          parameters:NXparameters
            raw_file:NX_CHAR
        NXsample
          name:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXtomoproc**

These symbols will be used below to coordinate datasets with the same shape.

+--------+---------------------------------+
| Symbol | Description                     |
+========+=================================+
| ``nx`` | number of voxels in X direction |
+--------+---------------------------------+
| ``ny`` | number of voxels in Y direction |
+--------+---------------------------------+
| ``nz`` | number of voxels in Z direction |
+--------+---------------------------------+


.. rubric:: Comprehensive Structure of **NXtomoproc**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
