..  _NXmonitor:

#########
NXmonitor
#########

.. index::  ! . NXDL base_classes; NXmonitor

category:
    base_classes

NXDL source:
    NXmonitor
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXmonitor.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXgeometry`, :ref:`NXlog`

documentation:
    Template of monitor data. It is similar to the NXdata groups containing
    monitor data and its associated dimension scale, e.g. time_of_flight or
    wavelength in pulsed neutron instruments. However, it may also include
    integrals, or scalar monitor counts, which are often used in both in both
    pulsed and steady-state instrumentation.
    


.. rubric:: Basic Structure of **NXmonitor**

.. code-block:: text
    :linenos:
    
    NXmonitor (base class, version 1.0)
      count_time:NX_FLOAT
      data:NX_NUMBER[n]
        @signal
        @axes
      distance:NX_FLOAT
      efficiency:NX_NUMBER[]
      end_time:NX_DATE_TIME
      integral:NX_NUMBER
      mode:NX_CHAR
      preset:NX_NUMBER
      range:NX_FLOAT[2]
      sampled_fraction:NX_FLOAT
      start_time:NX_DATE_TIME
      time_of_flight:NX_FLOAT[]
      type:NX_CHAR
      NXgeometry
      integral_log:NXlog
    

.. rubric:: Symbols used in definition of **NXmonitor**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXmonitor**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
