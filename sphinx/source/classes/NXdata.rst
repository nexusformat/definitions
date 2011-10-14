..  _NXdata:

######
NXdata
######

.. index::  ! classes - base_classes; NXdata

category
    base_classes

NXDL source:
    NXdata
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXdata.nxdl.xml)

version
    1.0

SVN Id
    $Id: NXdata.nxdl.xml 833 2011-03-08 23:08:25Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    none

symbol list:
    These symbols will be used below to coordinate datasets with the same shape.
    
    ``dataRank``
        rank of the 
    
    ``n``
        length of the 
    
    ``nx``
        length of the 
    
    ``ny``
        length of the 
    
    ``nz``
        length of the 
    
    

documentation:
    ? process with db2rst ?


Basic Structure of NXdata
=========================

::

    NXdata (base class, version 1.0)
      data:NX_NUMBER[n]
        @signal
        @axes
        @uncertainties
        @long_name
      errors:NX_NUMBER[n]
      offset:NX_FLOAT
      scaling_factor:NX_FLOAT
      variable:NX_NUMBER[n]
        @long_name
        @distribution
        @first_good
        @last_good
        @axis
      variable_errors:NX_NUMBER[n]
      x:NX_FLOAT[nx]
      y:NX_FLOAT[ny]
      z:NX_FLOAT[nz]
    
