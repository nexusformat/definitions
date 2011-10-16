..  _NXscan:

######
NXscan
######

.. index::  ! . NXDL applications; NXscan

category:
    applications

NXDL source:
    NXscan
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXscan.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXsample`

symbol list:
    none

documentation:
    Application definition for a generic scan instrument. This definition is more an
    example then a stringent definition as the content of a given NeXus scan file needs to
    differ for different types of scans. This example definition shows a scan like done
    on a rotation camera: the sample is rotated and a detector image, the rotation angle
    and a monitor value is stored at each step in the scan. In the following I use
    the symbol NP as a placeholder for the number of scan points. These are the rules for
    storing scan data in NeXus files which are implemented in this example:
    
    Each value varied throughout a scan is stored as an array of
    length NP at its respective location within the NeXus hierarchy.
    
    For area detectors, NP is the first dimension,
    example for a detector of 256x256:  data[NP,256,256]
    
    The NXdata group contains links to all variables varied in the scan and the data.
    This to give an equivalent to the more familiar classical tabular representation of scans.
    
    These rules exist for a reason: HDF allows the first dimension of a data set to be
    unlimited. This means the data can be appended too. Thus a NeXus file built according
    to the rules given above can be used in the following way:
    
    At the start of a scan, write all the static information.
    
    At each scan point, append new data from varied variables
    and the detector to the file.
    


.. rubric:: Basic Structure of **NXscan**

::

    NXscan (application definition, version 1.0b)
      (overlays NXentry)
      NXentry
        definition:NX_CHAR
        end_time:NX_DATE_TIME
        start_time:NX_DATE_TIME
        title:NX_CHAR
        NXdata
          data --> /NXentry/NXinstrument/NXdetector/data
          rotation_angle --> /NXentry/NXsample/rotation_angle
        NXinstrument
          NXdetector
            data:NX_INT[NP,xdim,ydim]
        NXmonitor
          data:NX_INT[NP]
        NXsample
          rotation_angle:NX_FLOAT[NP]
    

.. rubric:: Comprehensive Structure of **NXscan**


=====================  ========  =========  ===================================
Name and Attributes    Type      Units      Description (and Occurrences)
=====================  ========  =========  ===================================
class                  ..        ..         ..
=====================  ========  =========  ===================================
        