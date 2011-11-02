..  _NXdata:

######
NXdata
######

.. index::  ! . NXDL base_classes; NXdata

category:
    base_classes

NXDL source:
    NXdata
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXdata.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

documentation:
    (required) NXdata is a template of
    plottable data and their dimension scales.
    
    NeXus basic motivation
    default plot
    
    It is mandatory  that there is at least one NXdata group
    in each NXentry group.
    Note that the variable and data
    can be defined with different names.
    The signal and axes attribute of the
    data item define which items
    are plottable data and which are dimension scales.
    
    NeXus basic motivation
    default plot
    
    Each NXdata group will consist of only one data set
    containing plottable data and their standard deviations.
    
    This data set may be of arbitrary rank up to a maximum
    of NX_MAXRANK=32.
    
    The plottable data will be identified by the attribute:
    signal="1"
    
    The plottable data will identify the dimension
    scale(s) in the axes attribute.
    
    If available, the standard deviations of the data are to be
    stored in a data set of the same rank and dimensions, with the name errors.
    
    For each data dimension, there should be a one-dimensional array
    of the same length.
    
    These one-dimensional arrays are the dimension scales of the
    data,  i.e. the values of the independent variables at which the data
    is measured, such as scattering angle or energy transfer.
    
    There are two methods of linking
    
    link
    
    each data dimension to its respective dimension scale.
    
    The preferred (and recommended) method uses the axes
    
    axes
    
    attribute to specify the names of each dimension scale.
    
    The older method uses the axis attribute on each
    dimension scale
    to identify
    with an integer the axis whose value is the number of the dimension.
    
    NXdata is used to implement one of the basic motivations in NeXus,
    to provide a default plot for the data of this NXentry.  The actual data
    might be stored in another group and (hard) linked to the NXdata group.
    


.. rubric:: Basic Structure of **NXdata**

.. code-block:: text
    :linenos:
    
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
    

.. rubric:: Symbols used in definition of **NXdata**

These symbols will be used below to coordinate datasets with the same shape.

+--------------+------------------------------+
| Symbol       | Description                  |
+==============+==============================+
| ``dataRank`` | rank of the data field       |
+--------------+------------------------------+
| ``n``        | length of the variable field |
+--------------+------------------------------+
| ``nx``       | length of the x field        |
+--------------+------------------------------+
| ``ny``       | length of the y field        |
+--------------+------------------------------+
| ``nz``       | length of the z field        |
+--------------+------------------------------+




.. rubric:: Comprehensive Structure of **NXdata**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
