..  _NXguide:

#######
NXguide
#######

.. index::  ! . NXDL base_classes; NXguide

category:
    base_classes

NXDL source:
    NXguide
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXguide.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`

documentation:
    NXguide is used by neutron instruments to describe
    a guide consists of several mirrors building a shape through which
    neutrons can be guided or directed. The simplest such form is box shaped
    although elliptical guides are gaining in popularity.
    The individual parts of a guide usually have common characteristics
    but there are cases where they are different.
    For example,  a neutron guide might consist of 2 or 4 coated walls or
    a supermirror bender with multiple, coated vanes.
    
    To describe polarizing supermirrors such as used in neutron reflection,
    it may be necessary to revise this definition of NXguide
    to include NXpolarizer and/or NXmirror.
    
    When even greater complexity exists in the definition of what
    constitutes a guide,
    it has been suggested that NXguide
    be redefined as a NXcollection of
    NXmirrors each having their own
    NXgeometries describing their location(s).
    
    For the more general case when describing mirrors, consider using
    NXmirror.
    
    NOTE: The NeXus International Advisory Committee welcomes
    comments for revision and improvement of
    this definition of NXguide.
    


.. rubric:: Basic Structure of **NXguide**

.. code-block:: text
    :linenos:
    
    NXguide (base class, version 1.0)
      bend_angle_x:NX_FLOAT
      bend_angle_y:NX_FLOAT
      coating_material:NX_FLOAT[nsurf]
      coating_roughness:NX_FLOAT[nsurf]
      description:NX_CHAR
      external_material:NX_CHAR
      incident_angle:NX_FLOAT
      interior_atmosphere:NX_CHAR
      m_value:NX_FLOAT[nsurf]
      number_sections:NX_INT
      substrate_material:NX_FLOAT[nsurf]
      substrate_roughness:NX_FLOAT[nsurf]
      substrate_thickness:NX_FLOAT[nsurf]
      reflectivity:NXdata
        data:NX_NUMBER[nsurf,nwl]
          @signal
          @axes
        surface:NX_NUMBER[nsurf]
        wavelength:NX_NUMBER[nwl]
      NXgeometry
    

.. rubric:: Symbols used in definition of **NXguide**

+-----------+-------------------------------+
| Symbol    | Description                   |
+===========+===============================+
| ``nsurf`` | number of reflecting surfaces |
+-----------+-------------------------------+
| ``nwl``   | number of wavelengths         |
+-----------+-------------------------------+




.. rubric:: Comprehensive Structure of **NXguide**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
