..  _NXguide:

#######
NXguide
#######

.. index::  ! classes - base_classes; NXguide

category
    base_classes

NXDL source:
    NXguide
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXguide.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXguide.nxdl.xml 822 2011-02-15 20:00:32Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXgeometry`

symbol list:
    ``nsurf``
        number of reflecting surfaces
    
    ``nwl``
        number of wavelengths
    
    

documentation:
    ? process with db2rst ?


Basic Structure of NXguide
==========================

::

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
    
