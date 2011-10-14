..  _NXtofnpd:

########
NXtofnpd
########

.. index::  ! classes - applications; NXtofnpd

category
    applications

NXDL source:
    NXtofnpd
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXtofnpd.nxdl.xml)

version
    1.0b

SVN Id
    $Id: NXtofnpd.nxdl.xml 816 2011-02-04 22:28:36Z Pete Jemian $

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`, :ref:`NXmonitor`, :ref:`NXsample`, :ref:`NXuser`

symbol list:
    none

documentation:
    ? process with db2rst ?


Basic Structure of NXtofnpd
===========================

::

    NXtofnpd (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        pre_sample_flightpath:NX_FLOAT
        start_time:NX_DATE_TIME
        title:NX_CHAR
        data:NXdata
          data --> /NXentry/NXinstrument/NXdetector/data
          detector_number --> /NXentry/NXinstrument/NXdetector/detector_number
          time_of_flight --> /NXentry/NXinstrument/NXdetector/time_of_flight
        NXinstrument
          detector:NXdetector
            azimuthal_angle:NX_FLOAT[ndet]
            data:NX_INT[ndet,ntimechan]
            detector_number:NX_INT[ndet]
            distance:NX_FLOAT[ndet]
            polar_angle:NX_FLOAT[ndet]
            time_of_flight:NX_FLOAT[ntimechan]
        NXmonitor
          data:NX_INT[ntimechan]
          distance:NX_FLOAT
          mode:NX_CHAR
          preset:NX_FLOAT
          time_of_flight:NX_FLOAT[ntimechan]
        NXsample
          name:NX_CHAR
        user:NXuser
          name:NX_CHAR
    
