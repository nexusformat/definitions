.. _DataRules:

===========================================
Rules for Storing Data Items in NeXus Files
===========================================

This section describes the rules which apply for storing single data items.

.. _Design-Naming:

Naming Conventions
##################

.. index:: 
   single: naming convention
   single: NX; used as NX class prefix 
   single: attribute; NXclass
   single: NXclass (attribute)

Group and field names used within NeXus follow a naming convention
described by the following :index:`rules <rules; naming>`:

* The names of NeXus *group* and *field* items
  must only contain a restricted set of characters.
  
  This set is described by a regular expression 
  syntax :index:`regular expression`
  :ref:`regular expression syntax <RegExpName>`,
  as described below.

* For the class names [#]_ of NeXus *group* items,
  the prefix *NX* is reserved as shown in the :ref:`table <reserved_prefixes>` below. 
  Thus all NeXus class names start with NX.
  The chapter titled :ref:`ReferenceDocumentation` lists the 
  available NeXus class names as either *base classes*, 
  *application definitions*, or *contributed definitions*.

.. [#] The *class name* is the value assigned to the
   *NX_class* attribute of an HDF5 group in the NeXus data file.
   This *class name* is different than the *name* of the HDF5 group.
   This is important when not using the NAPI to either read or write
   the HDF5 data file.

.. rubric:: NXDL group and field names

.. compound::
   
   The names of NeXus *group* and *field* items
   are validated according to these boundaries:

   * *Recommended* names [#lc]_

     - lower case words separated by underscores and, if needed, with a trailing number
     - NOTE: this is used by the NeXus base classes

   * *Allowed* names

     - any combination of upper and lower case letter, numbers, underscores and periods, except that periods cannot be at the start or end of the string
     - NOTE: this matches the *validItemName* regular expression :ref:`below<validItemName>`

   * *Invalid* names

     - NOTE: does not match the *validItemName* regular expression :ref:`below<validItemName>`

   .. _RegExpName:

   .. rubric:: Regular expression pattern for NXDL group and field names
   
   The NIAC recognises that the majority of the world uses characters
   outside of the basic latin (a.k.a. US-ASCII, 7-bit ASCII) set
   currently included in the allowed names. The restriction given here
   reflects current technical issues and we expect to revisit the issue
   and relax such restrictions in future.

   .. [#7bit-ASCII] https://en.wikipedia.org/wiki/ASCII

   The names of NeXus *group* and *field* items must match
   this regular expression (named *validItemName* in the
   XML Schema file: *nxdl.xsd*):

   ..
     To understand this complicated RegExp, see
     https://github.com/nexusformat/definitions/pull/671#issuecomment-708395846

     Also, an online test is shown here:
     https://regex101.com/r/Yknm4v/3
    
   .. _validItemName:

   .. code-block:: text
       :linenos:
   
       ^[a-zA-Z0-9_]([a-zA-Z0-9_.]*[a-zA-Z0-9_])?$
   
   The length should be limited to no more than 
   63 characters (imposed by the HDF5 :index:`rules <rules; HDF5>` for names).
   
   It is recognized that some facilities will construct data files with
   group and field names with upper case letters or start names with a
   number or include a period in a name. [#lc]_

   .. [#lc] NeXus data files with group or field names
      that match the regular expression but contain upper case
      characters, start with a digit, or include a period in the group
      or field names might not be accepted by all software that reads
      NeXus data files.  These names will be flagged as a warning during
      data file validation.
	
.. _use-underscore:

.. rubric:: Use of underscore in descriptive names

Sometimes it is necessary to combine words in order to build a
descriptive name for a field or a group.
In such cases lowercase words are connected by underscores.

.. code-block:: text
    :linenos:

    number_of_lenses

For all fields, only names from the NeXus base class dictionaries should be used.
If a field name or even a complete component is missing,
please suggest the addition to the :ref:`NIAC`. The addition will usually be
accepted provided it is not a duplication of an existing field and
adequately documented.

    .. note::
	    The NeXus base classes provide a comprehensive dictionary of terms that can be used for each class.  
	    The expected spelling and definition of each term is specified in the base classes.  
	    It is not required to provide all the terms specified in a base class.  
	    Terms with other names are permitted but might not be recognized by standard software. 
	    Rather than persist in using names not specified in the standard, please suggest additions to the :ref:`NIAC`.

.. _target_value:

The data stored in NeXus fields must be *readback* values. 
This means values as read from the detector, other hardware, etc. 
There are occasions where it is sensible to store the target value 
the variable was supposed to have. In such cases, the 
*target* value is stored with a name built by appending 
``_set`` to the NeXus (readback) field name.  

Consider this example:

.. code-block:: text
    :linenos:

    temperature
    temperature_set

The ``temperature`` field will hold the readback from the 
cryostat/furnace/whatever. The field ``temperature_set`` will hold 
the target value for the temperature as set by the 
experiment control software. 

.. 2020-10-13, added per NIAC 2020
   https://github.com/nexusformat/definitions/issues/791
   We'll leave existing names as-is, 
   but make this recommendation for the future.

Some fields share a common part of their name and an additional part
name that makes the whole name specific.  For example, a ``unit_cell``
might have parts named ``abc``, ``alphabetagamma``, and ``volume``.  It
is recommended to write them with the common part first, an underscore
(``_``), and then the specific part.  In this way, the fields will sort
alphabetically on the common name. So, in this example:

.. code-block:: text
    :linenos:

    unit_cell_abc
    unit_cell_alphabetagamma
    unit_cell_volume


.. index:: ! reserved prefixes

.. _reserved_prefixes:

.. rubric:: Reserved prefixes

When naming a field, NeXus has reserved certain prefixes to the names to
ensure that names written in NeXus files will not conflict with future
releases as the NeXus standard evolves. Prefixes should follow a naming
scheme of uppercase letters followed by an underscore, but exceptions
will be made for cases already in wide use. The following table lists
the prefixes reserved by NeXus.

.. index::
    reserved prefixes; NX
    reserved prefixes; NX_
    reserved prefixes; BLUESKY_
    reserved prefixes; IDF_
    reserved prefixes; NDAttr
    reserved prefixes; PDBX_
    reserved prefixes; SAS_
    reserved prefixes; SILX_

============  ==========  ==========================================  ===============================
prefix 	      use 	    meaning 	                                URL
============  ==========  ==========================================  ===============================
``BLUESKY_``  attributes  reserved for use by Bluesky project 	      https://blueskyproject.io
``IDF_``      attributes  reserved for use by ISIS Muon Facility      https://www.isis.stfc.ac.uk
``NDAttr``    attributes  reserved for use by EPICS area detector     https://github.com/areaDetector
``NX``        NXDL class  for the class names used with NeXus groups  https://www.nexusformat.org
``NX_``       attributes  reserved for use by NeXus 	              https://www.nexusformat.org
``PDBX_``     attributes  reserved for the US protein data bank       https://www.rcsb.org
``SAS_``      attributes  reserved for use by canSAS 	              http://www.cansas.org
``SILX_``     attributes  reserved for use by silx 	              https://www.silx.org
============  ==========  ==========================================  ===============================

.. index:: ! reserved suffixes

.. _reserved_suffixes:

.. rubric:: Reserved suffixes

When naming a field (or dataset), NeXus has reserved certain suffixes to the names
so that a specific meaning may be attached.  Consider a field named ``DATASET``,
the following table lists the suffixes reserved by NeXus.

.. index::
    reserved suffixes; end
    reserved suffixes; errors
    reserved suffixes; increment_set
    reserved suffixes; indices
    reserved suffixes; mask
    reserved suffixes; set
    reserved suffixes; weights

==================  =========================================  =================================
suffix              reference                                  meaning
==================  =========================================  =================================
``_end``            :ref:`NXtransformations`                   end points of the motions that start with ``DATASET``
``_errors``         :ref:`NXdata`                              uncertainties (a.k.a., errors)
``_increment_set``  :ref:`NXtransformations`                   intended average range through which the corresponding axis moves during the exposure of a frame
``_indices``        :ref:`NXdata`                              Integer array that defines the indices of the signal field which need to be used in the ``DATASET`` in order to reference the corresponding axis value
``_mask``           ..                                         Field containing a signal mask, where 0 means the pixel is not masked. If required, bit masks are defined in :ref:`NXdetector` ``pixel_mask``.
``_set``            :ref:`target values <target_value>`        Target value of ``DATASET``
``_weights``        ..                                         divide ``DATASET`` by these weights [#]_
==================  =========================================  =================================

.. [#] If ``DATASET_weights`` exists and has the same shape as the dataset, 
   you are supposed to divide ``DATASET`` by the weights.

.. Note that the following line might be added to the above table pending discussion:

   `_axes`            :ref:`NXdata`              String array naming data fields for each axis of ``DATASET``


.. _Design-Variants:


Variants
#########

Sometimes it is necessary to store alternate values of a NeXus dataset 
in a NeXus file. A common example may be the beam center of which a 
rough value is available at data acquisition. But later on, a better beam 
center is calculated as part of the data reduction. In order to store 
this without losing the historical information, the original field can be given a variant attribute that points to 
a new dataset containing the obsolete value. If even better values 
become available, further datasets can be inserted into the chain of variant attributes 
pointing to the preceeding value for the dataset. A reader can thus 
keep the best value in the pre-defined dataset, and also be able to 
follow the variant chain and locate older variants. 

A little example is in order to illustrate the scheme:

.. code-block:: text
    :linenos:

    beam_center_x
            @variant=beam_center_x_refined
    beam_center_x_refined
            @variant=beam_center_x_initial_guess
    beam_center_x_initial_guess

NeXus borrowed this scheme from CIF. In this way all the different
variants of a dataset can be preserved. The expectation is that
variants will be rarely used and NXprocess groups with the results of
data reduction will be written instead. 


.. _Design-Uncertainties:

Uncertainties or Errors
########################

It is desirable to store experimental errors (also known as 
*uncertainties*) together with the data. NeXus supports this through 
a convention: uncertainties or experimental errors on data are 
stored in a separate field which has a name consisting of the 
original name of the data with ``_errors`` appended to it. 
These uncertainties fields have the same shape as the original data field.

An example, from NXdetector:

.. code-block:: text
    :linenos:

    data
    data_errors
    beam_center_x
    beam_center_x_errors

Where data errors would contain the errors on data, and beam_center_x_errors the error on 
the beam center for x. 


.. _Design-ArrayStorageOrder:

NeXus Array Storage Order
#########################

NeXus stores :index:`multi-dimensional <dimension; storage order>` 
arrays of physical values in C language storage order,
where the first dimension has the :index:`slowest varying <dimension; slowest varying>` index when iterating through the array in storage order,
and the last dimension is the :index:`fastest varying <dimension; fastest varying>`. This is the rule.
*Good reasons are required to deviate from this rule.*

Where the array contains data from a detector, the array dimensions may correspond to physical directions or axes. The slowest, slow, fast, fastest qualifiers can then apply to these axes too.

It is possible to store data in storage orders other than C language order.

..  TODO: see note with "Design-DataValueTransformations" section below

As well it is possible to specify that the data needs to be converted first
before being useful.  Consider one situation, when data must be
streamed to disk as fast as possible and conversion to C language
storage order causes unnecessary latency.  This case presents a
good reason to make an exception to the standard rule.


.. index:: dimension; storage order

.. _Design-NonCStorageOrder:

Non C Storage Order
===================

In order to indicate that the storage order is different from C storage order two
additional data set attributes, offset and stride, have to be stored which together define the storage
layout of the data. Offset and stride contain rank numbers according to the rank of the multidimensional
data set. Offset describes the step to make when the dimension is multiplied by 1. Stride defines the step to
make when incrementing the dimension. This is best explained by some examples.

.. compound::

    .. rubric:: Offset and Stride for 1 D data:

    .. literalinclude:: examples/offset-stride-1d.txt
        :tab-width: 4
        :linenos:
        :language: text

.. compound::

    .. rubric:: Offset and Stride for 2D Data

    .. literalinclude:: examples/offset-stride-2d.txt
        :tab-width: 4
        :linenos:
        :language: text

.. compound::

    .. rubric:: Offset and Stride for 3D Data

    .. literalinclude:: examples/offset-stride-3d.txt
        :tab-width: 4
        :linenos:
        :language: text

..  TODO: 2011-10-22,PRJ:
    It is too early to include a section about Data Value Transformations and ``NXformula``.
    There is no ``NXformula`` class in NeXus yet.
    <section xml:id="Design-DataValueTransformations">
    <title>Data Value Transformations</title>
    <para>
    It is possible to store raw values in NeXus data files. Such data has to be stored in
    special <literal>NXformula</literal> groups together with the data and information required to transform
    it into physical values.
    <note>
    <para>NeXus has not yet defined the <literal>NXformula</literal> group for use in NeXus data files.
    The exact content of the <literal>NXformula</literal> group is still under discussion.</para>
    </note>
    </para>
    </section>

..  =========================
    section: NeXus Data Types
    =========================

.. _Design-DataTypes:

NeXus Data Types
################

================ ============================
description      matching regular expression
================ ============================
integer          ``NX_INT(8|16|32|64)``
floating-point   ``NX_FLOAT(32|64)``
array            ``(\\[0-9\\])?``
valid item name  ``^[a-zA-Z0-9_]([a-zA-Z0-9_.]*[a-zA-Z0-9_])?$``
valid class name ``^NX[A-Za-z0-9_]*$``
================ ============================

NeXus supports numeric data as either integer or floating-point
numbers.  A number follows that indicates the number of bits in the word.
The table above shows the regular expressions that
match the data type specifier.

.. index::
    ! integers
    see: numbers; integers

**integers**
    ``NX_INT8``,
    ``NX_INT16``,
    ``NX_INT32``,
    or
    ``NX_INT64``

.. index::
    ! floating-point numbers
    see: numbers; floating-point numbers

**floating-point numbers**
    ``NX_FLOAT32``
    or
    ``NX_FLOAT64``

.. index:: date and time

**date / time stamps**
    ``NX_DATE_TIME`` or  ``ISO8601``:
    Dates and times are specified using
    ISO-8601 standard definitions.
    Refer to :ref:`Design-Dates-Times`.

.. index:: ! strings
.. index:: ! UTF-8

**strings**
   ``NX_CHAR``:
   The preferred string representation is UTF-8. 
   Both fixed-length strings and variable-length strings are valid. 
   String arrays cannot be used where only a string is expected 
   (title, start_time, end_time, ``NX_class`` attribute,...). 
   Fields or attributes requiring the use of string arrays will be 
   clearly marked as such (like the ``NXdata`` attribute auxiliary_signals).
   
   .. https://github.com/nexusformat/NIAC/issues/31#issuecomment-433481024

   ..
      All strings are to be encoded in UTF-8. Since most strings in a
      NeXus file are restricted to a small set of characters 
      and the first 128 characters are standard across encodings,
      the encoding of most of the strings in a NeXus file will be a moot point.
      Encoding in UTF-8 will be important when recording people's names 
      in ``NXuser`` and text notes in ``NXnotes``.
   
   .. https://github.com/nexusformat/NIAC/issues/23#issuecomment-308773465
   
   .. index:: strings; variable-length
   .. index:: strings; fixed-length
   .. index:: strings; arrays
   
   .. https://github.com/nexusformat/definitions/issues/281


   ..
      NeXus accepts both variable and fixed length strings, 
      as well as arrays of strings.
      Software that reads NeXus data files should support 
      all of these.

      Some file writers write strings as a string array
      of rank 1 and length 1.
      Clients should be prepared to handle such strings.

.. index:: binary data

**binary data**
    Binary data is to be written as ``UINT8``.

.. index:: images

**images**
    Binary image data is to be written using ``UINT8``, the same as binary data, but with an accompanying image mime-type.
    If the data is text, the line terminator is ``[CR][LF]``.

..  ==============================
    section: NeXus dates and times
    ==============================

.. _Design-Dates-Times:

NeXus dates and times
=====================

.. index:: date and time

NeXus  :index:`dates and times <date and time>`
should be stored using the `ISO 8601`_ [#]_  format,
e.g. ``1996-07-31T21:15:22+0600`` (which includes
a time zone offset of ``+0600``).
Note:  The time zone offset is always numeric or ``Z`` (which means UTC).
The standard also allows for time intervals in fractional seconds
with *1 or more digits of precision*.
This avoids confusion, e.g. between U.S. and European conventions,
and is appropriate for machine sorting.
It is recommended to add an explicit time zone,
otherwise the local time zone is assumed per ISO8601.
The norm is that if there is no time zone, it is assumed
local time, however, when a file moves from one country to
another it is undefined. If the local time zone is written,
the ambiguity is gone.

.. _ISO 8601: https://www.w3.org/TR/NOTE-datetime
.. [#] ISO 8601: https://www.w3.org/TR/NOTE-datetime


.. compound::

    .. rubric:: strftime() format specifiers for ISO-8601 time

    .. code-block:: text
    
    	%Y-%m-%dT%H:%M:%S%z

.. note:: Note that the ``T`` appears literally in the string,
          to indicate the beginning of the time element, as specified
          in ISO 8601.  It is common to use a space in place of the
          ``T``, such as ``1996-07-31 21:15:22+0600``.
          While human-readable (and later allowed in a relaxed revision
          of the standard), compatibility with libraries supporting
          the ISO 8601 standard is not
          assured with this substitution.  The ``strftime()``
          format specifier for this is "``%Y-%m-%d %H:%M:%S%z``".


.. index:: !units
	Unidata UDunits
	UDunits

.. _Design-Units:

NeXus Data Units
################

Given the plethora of possible applications of NeXus, it is difficult to
define units to use. Therefore, the general rule is that you are free to
store data in any unit you find fit. However, any field must have a
units attribute which describes the units, Wherever possible, SI units are
preferred. NeXus units are written as a string attribute (``NX_CHAR``)
and describe the engineering units. The string
should be appropriate for the value.
Values for the NeXus units must be specified in
a format compatible with `Unidata UDunits`_ [#UDunits]_
Application definitions may specify units to be used for fields
using :index:`an <enumeration>` ``enumeration``.

.. _Unidata UDunits: http://www.unidata.ucar.edu/software/udunits
.. [#UDunits]
    The :index:`UDunits`
    specification also includes instructions  for derived units.
    At present, the contents of NeXus ``units`` attributes
    are not validated in data files.

    ..  thus backwards compatible

.. _Rules-StoringDetectors:

Storing Detectors
#################

There are very different types of detectors out there. Storing their data
can be a challenge. As a general guide line: if the detector has some
well defined form, this should be reflected in the data file. A linear
detector becomes a linear array, a rectangular detector becomes an
array of size ``xsize`` times ``ysize``.
Some detectors are so irregular that this
does not work. Then the detector data is stored as a linear array, with the
index being detector number till ``ndet``. Such detectors must be accompanied
by further arrays of length ``ndet`` which give
``azimuthal_angle, polar_angle and distance`` for each detector.

If data from a time of flight (TOF) instrument must be described, then the
TOF dimension becomes the last dimension, for example an area detector of
``xsize`` *vs.* ``ysize``
is stored with TOF as an array with dimensions
``xsize, ysize,
ntof``.

.. _Rules-StoringData-Monitors:

Monitors are Special
####################


:index:`Monitors <monitor>`, detectors that measure the properties
of the experimental probe rather than the probe's interaction with the
sample, have a special place in NeXus files. Monitors are crucial to normalize data.
To emphasize their role, monitors are not stored in the
``NXinstrument`` hierarchy but on ``NXentry`` level
in their own groups as there might be multiple monitors. Of special
importance is the monitor in a group called ``control``.
This is the main monitor against which the data has to be normalized.
This group also contains the counting control information,
i.e. counting mode, times, etc.

Monitor data may be multidimensional. Good examples are scan monitors
where a monitor value per scan point is expected or
time-of-flight monitors.

.. index::
   plotting; how to find data

.. _Find-Plottable-Data:

Find the plottable data
#######################

:ref:`SimplePlotting` is one of the motivations for the NeXus standard.
To implement *simple plotting*, a mechanism must exist to identify
the default data for visualization (plotting) in any NeXus data file.
Over its history the NIAC has agreed upon a method of applying metadata
to identify the default plottable data.  This metadata has always been
specified as HDF attributes.  With the evolution of the underlying file
formats and the NeXus data standard, the method to identify the default 
plottable data has evolved, undergoing three distinct versions.

:version 1: :ref:`Design-FindPlottable-ByDimNumber`
:version 2: :ref:`Design-FindPlottable-ByName`
:version 3: :ref:`Design-FindPlottable-NIAC2014`

Consult the :ref:`NeXus API <Introduction-NAPI>`
section, which describes the routines available to program these
operations. In the course of time, generic NeXus browsers will
provide this functionality automatically.

For programmers who may encounter NeXus data files written using 
any of these methods, we present the algorithm for each method 
to find the default plottable data.  It is recommended to start 
with the most recent method, :ref:`Find-Plottable-Data-v3`, first.

.. _Find-Plottable-Data-v3:

Version 3
=========

The third (current) method to identify the default 
plottable data is as follows:

#. Start at the top level of the NeXus data file
   (the *root* of the HDF5 hierarchy).

#. Pick the default :ref:`NXentry` group.

   If the *root* has an attribute ``default``, then its value
   is the name of the ``NXentry`` group to be used.  Otherwise,
   pick any ``NXentry`` group.  This is trivial if there is only one 
   ``NXentry`` group.

   .. compound::
   
       .. _fig.flowchart-NXroot-default:
   
       .. figure:: img/flowchart-NXroot-default.png
           :alt: fig.flowchart-NXroot-default
           :width: 60%
   
           Find plottable data: select the ``NXentry`` group

#. Pick the default :ref:`NXdata` group.

   Open the ``NXentry`` group selected above.
   If it has an attribute ``default``, then its value
   is the name of the ``NXdata`` group to be used.  Otherwise,
   pick any ``NXdata`` group.  This is trivial if there is only one 
   ``NXdata`` group.

   .. compound::
   
       .. _fig.flowchart-NXentry-default:
   
       .. figure:: img/flowchart-NXentry-default.png
           :alt: fig.flowchart-NXentry-default
           :width: 60%
   
           Find plottable data: select the ``NXdata`` group

.. index:: signal data

#. Pick the default plottable field (the *signal* data).

   Open the ``NXdata`` group selected above.
   If it has an attribute ``signal``, then its value
   is the name of the field (dataset) to be plotted.
   If no ``signal`` attribute is not present on the 
   ``NXdata`` group, then proceed to try an 
   :ref:`older NeXus method<Find-Plottable-Data-v2>` 
   to find the default plottable data.

   .. compound::
   
       .. _fig.flowchart-NXdata-signal:
   
       .. figure:: img/flowchart-NXdata-signal.png
           :alt: fig.flowchart-NXdata-signal
           :width: 90%
   
           Find plottable data: select the *signal* data
   
   #. Pick the fields with the dimension scales (the *axes*).
   
      If the same ``NXdata`` group has an attribute ``axes``, 
      then its value is a string (*signal* data is 1-D) or 
      string array (*signal* data is 2-D or higher rank) 
      naming the field **in this group** to be used as 
      dimension scales of the default plottable data.  
      The number of values given must be equal to the 
      *rank* of the *signal* data.  These are the *abscissae*
      of the plottable *signal* data.
      
      *If* no field is available to provide a dimension scale
      for a given dimension, then a "``.``" will be used in that position. 
      In such cases, programmers are expected to use an integer 
      sequence starting from 0 for each position along that dimension.
      
   #. Associate the dimension scales with each dimension of the plottable data.
   
      For each field (its name is *AXISNAME*) in ``axes`` that 
      provides a dimension scale, there will be
      an ``NXdata`` group attribute ``AXISNAME_indices`` which
      value is an 
      .. integer or 
      integer array with value of the 
      dimensions of the *signal* data to which this dimension scale applies.
      
      If no ``AXISNAME_indices`` attribute is provided, a programmer is encouraged 
      to make best efforts assuming the intent of this ``NXdata`` group
      to provide a default plot.
      The ``AXISNAME_indices`` attribute is only required when necessary to 
      resolve ambiguity. 
      
      It is possible there may be more than one ``AXISNAME_indices`` attribute
      with the same value or values.  This indicates the possibilty of using
      alternate abscissae along this (these) dimension(s).  The
      field named in the ``axes`` attribute indicates the intention of
      the data file writer as to which field should be used by default.

#. Plot the *signal* data, given *axes* and *AXISNAME_indices*.


When all the ``default`` and ``signal`` attributes are present, this 
Python code will identify directly the default plottable data 
(assuming a ``plot()`` function has been defined by some code::

    root = h5py.File(hdf5_file_name, "r")
    
    default_nxentry_group_name = root.attrs["default"]
    nxentry = root[default_nxentry_group_name]
    
    default_nxdata_group_name = nxentry.attrs["default"]
    nxdata = nxentry[default_nxdata_group_name]
    
    signal_dataset_name = nxdata.attrs["signal"]
    data = nxdata[signal_dataset_name]
    
    plot(data)


.. _Find-Plottable-Data-v2:

Version 2
=========

.. tip:: Try this method for older NeXus data files and :ref:`Find-Plottable-Data-v3` fails..

The second method to identify the default 
plottable data is as follows:

#. Start at the top level of the NeXus data file.

#. Loop through the groups with class ``NXentry`` 
   until the next step succeeds.

   .. compound::
   
       .. _fig.flowchart-v2-NXroot-default:
   
       .. figure:: img/flowchart-v2-NXroot-default.png
           :alt: fig.flowchart-v2-NXroot-default
           :width: 60%
   
           Find plottable data: pick a ``NXentry`` group

#. Open the NXentry group and loop through the subgroups 
   with class ``NXdata`` until the next step succeeds.

   .. compound::
   
       .. _fig.flowchart-v2-NXentry-default:
   
       .. figure:: img/flowchart-v2-NXentry-default.png
           :alt: fig.flowchart-v2-NXentry-default
           :width: 60%
   
           Find plottable data: pick a ``NXdata`` group

#. Open the NXdata group and loop through the fields for the one field 
   with attribute ``signal="1"``.
   Note: There should be *only one* field that matches.

   This is the default plottable data.
   
   If there is no such ``signal="1"`` field,
   proceed to try an 
   :ref:`older NeXus method<Find-Plottable-Data-v1>` 
   to find the default plottable data.

   #. If this field has an attribute ``axes``:

      #. The ``axes`` attribute value contains a colon (or comma)
         delimited list (in the C-order of the data array) with 
         the names of the 
         :index:`dimension scales <dimension scale>`
         associated with the plottable data.
         Such as:  ``axes="polar_angle:time_of_flight"``

      #. Parse ``axes`` and open the datasets to describe your 
         :index:`dimension scales <dimension scale>`

   #. If this field has no attribute ``axes``:

      #. Search for datasets with attributes ``axis=1``, ``axis=2``, etc.

      #. These are the fields describing your axis. There may be
         several fields for any axis, i.e. there may be multiple 
         fields with the attribute ``axis=1``. Among them the 
         field with the attribute ``primary=1`` is the preferred one. 
         All others are alternative :index:`dimension scales <dimension scale>`.

#. Having found the default plottable data and its dimension scales: 
   make the plot.

   .. compound::
   
       .. _fig.flowchart-v2-NXdata-signal:
   
       .. figure:: img/flowchart-v2-NXdata-signal.png
           :alt: fig.flowchart-v2-NXdata-signal
           :width: 98%
   
           Find plottable data: select the *signal* data


.. _Find-Plottable-Data-v1:

Version 1
=========

.. tip:: Try this method for older NeXus data files.

The first method to identify the default 
plottable data is as follows:

#. Open the first top level NeXus group with class
   ``NXentry``.

   .. compound::
   
       .. _fig.flowchart-v1-NXroot-default:
   
       .. figure:: img/flowchart-v1-NXroot-default.png
           :alt: fig.flowchart-v1-NXroot-default
           :width: 60%
   
           Find plottable data: pick the first ``NXentry`` group

#. Open the first NeXus group with class
   ``NXdata``.

   .. compound::
   
       .. _fig.flowchart-v1-NXentry-default:
   
       .. figure:: img/flowchart-v1-NXentry-default.png
           :alt: fig.flowchart-v1-NXentry-default
           :width: 60%
   
           Find plottable data: pick the first ``NXdata`` group

#. Loop through NeXus fields in this group searching for the item
   with attribute
   ``signal="1"``
   indicating this field has the plottable data.

#. Search for the 
   one-dimensional NeXus fields with attribute ``primary=1``.
   These are the dimension scales to label 
   the axes of each dimension of the data.

#. Link each dimension scale
   to the respective data dimension by
   the ``axis`` attribute (``axis=1``, ``axis=2``, 
   ... up to the  :index:`rank <rank>` of the data).

   .. compound::
   
       .. _fig.flowchart-v1-NXdata-signal:
   
       .. figure:: img/flowchart-v1-NXdata-signal.png
           :alt: fig.flowchart-v1-NXdata-signal
           :width: 98%
   
           Find plottable data: select the *signal* data

#. If necessary, close this
   ``NXdata``
   group, search the next ``NXdata`` group, repeating steps 3 to 5.

#. If necessary, close the
   ``NXentry``
   group, search the next ``NXentry`` group, repeating steps 2 to 6.


.. index:: dimension
	!multi-dimensional data
	data; multi-dimensional

.. _multi-dimensional-data:

Associating Multi Dimensional Data with Axis Data
#################################################

NeXus allows for storage of multi dimensional arrays of data.  It is this
data that presents the most challenge for description.  In most cases
it is not sufficient to just have the indices into the array as a label for
the dimensions of the data. Usually the information which physical value
corresponds to an index into a dimension of the multi dimensional data set.
To this purpose a means is needed to locate appropriate data arrays which describe
what each dimension of a multi dimensional data set actually corresponds too.
There is a standard HDF facility to do this: it is called 
:index:`dimension scales <dimension; dimension scales>`.
Unfortunately, when NeXus was first designed, 
there was only one global namespace for dimension scales.
Thus NeXus had to devise its own scheme for locating axis data which is described
here. A side effect of the NeXus scheme is that it is possible to have multiple
mappings of a given dimension to physical data. For example, a TOF data set can have the TOF
dimension as raw TOF or as energy.

There are now three methods of :index:`associating <link>`
each data dimension to its respective dimension scale.
Only the first method is recommended now, the other two (older methods) are now discouraged.

#. :ref:`Design-FindPlottable-NIAC2014`
#. :ref:`Design-FindPlottable-ByName`
#. :ref:`Design-FindPlottable-ByDimNumber`

The recommended method uses the ``axes`` attribute applied to the :ref:`NXdata` group
to specify the names of each 
:index:`dimension scale <dimension; dimension scales>`.
A prerequisite is that the fields describing the axes of the plottable data
are stored together with the plottable data in the same NeXus group. 
If this leads to data duplication, use :ref:`links <Design-Links>`.

-----------

.. _Design-FindPlottable-NIAC2014:

Associating plottable data using attributes applied to the :ref:`NXdata` group
==============================================================================

.. tip:: Recommended:
   This is the "*NIAC2014*" method recommended for all new NeXus data files.

The default data to be plotted (and any associated axes)
is specified using attributes attached to the :ref:`NXdata` group.

:``signal``: 
   Defines the name of the default dataset *in the NXdata group*. 
   A field of this name *must* exist (either as dataset or link to dataset).
         
   It is recommended to use this attribute
   rather than adding a signal attribute to the dataset.  [#]_
   The procedure to identify the default data to be plotted is quite simple. 
   Given any NeXus data file, any ``NXentry``, or any ``NXdata``, 
   follow the chain as it is described from that point. 
   Specifically:
   
   *  The root of the NeXus file may have a ``default`` 
      attribute that names the default :ref:`NXentry` group.
      This attribute may be omitted if there is only one NXentry group.
      If a second NXentry group is later added, the ``default`` attribute 
      must be added then.
   *  Every :ref:`NXentry` group may have a ``default`` 
      attribute that names the default :ref:`NXdata` group.
      This attribute may be omitted if there is only one NXdata group
      or if no NXdata is present.
      If a second NXdata group is later added, the ``default`` attribute 
      must be added then.
   *  Every :ref:`NXdata` group will have a ``signal`` 
      attribute that names the field name to be plotted by default.
      This attribute is required.


:``axes``: 

   String array [#aa]_ that defines the independent data fields used in 
   the default plot for all of the dimensions of the *signal* field. 
   One entry is provided for every dimension in the *signal* field.
   
   The field(s) named as values (known as "axes") of this attribute 
   *must* exist. An axis slice is specified using a field named 
   ``AXISNAME_indices`` as described below (where the text shown here
   as ``AXISNAME`` is to be replaced by the actual field name).
   
   When no default axis is available for a particular dimension 
   of the plottable data, use a "." in that position. 
   
   See examples provided on the NeXus webpage ([#axes]_).
   
   If there are no axes at all (such as with a stack of images), 
   the axes attribute can be omitted.

.. AXISNAME_indices documentation will be repeated in NXdata/@AXISNAME_indices

:``AXISNAME_indices``: 
   Each ``AXISNAME_indices`` attribute indicates the dependency
   relationship of the ``AXISNAME`` field (where ``AXISNAME`` 
   is the name of a field that exists in this ``NXdata`` group) 
   with one or more dimensions of the plottable data.
   
   Integer array [#aa]_ that defines the indices of the *signal* field 
   (that field will be a multidimensional array)
   which need to be used in the ``AXISNAME`` dataset in 
   order to reference the corresponding axis value.
   
   The first index of an array is ``0`` (zero).

   Here, *AXISNAME* is to be replaced by the name of each 
   field described in the ``axes`` attribute.  
   An example with 2-D data, :math:`d(t,P)`, will illustrate::
   
      data_2d:NXdata
          @signal="data"
          @axes=["time","pressure"]
          @time_indices=0
          @pressure_indices=1
          data: float[1000,20]
          time: float[1000]
          pressure: float[20]

   This attribute is to be provided in all situations. 
   However, if the indices attributes are missing 
   (such as for data files written before this specification), 
   file readers are encouraged to make their best efforts 
   to plot the data. 
   Thus the implementation of the 
   ``AXISNAME_indices`` attribute is based on the model of 
   "strict writer, liberal reader". 

.. [#] Summary of the discussion at NIAC2014 to revise how to find default data: 
       https://www.nexusformat.org/2014_How_to_find_default_data.html
.. [#aa]  Note on array attributes:
          Attributes potentially containing multiple values 
          (axes and _indices) are to be written as string or integer arrays, 
          to avoid string parsing in reading applications.
.. [#axes] NIAC2014 proposition: https://www.nexusformat.org/2014_axes_and_uncertainties.html


Examples
++++++++

Several examples are provided to illustrate this method.
More examples are available in the NeXus webpage ([#axes]_).

.. compound::

   .. rubric:: simple 1-D data example showing how to identify the default data (*counts* vs. *mr*)
   
   In the first example, storage of a 1-D data set  (*counts* vs. *mr*) is described.

   .. code-block:: text
         :linenos:
      
         datafile.hdf5:NeXus data file
           @default="entry"
           entry:NXentry
             @default="data"
             data:NXdata
               @signal="counts"
               @axes="mr"
               @mr_indices=0
               counts: float[100]  --> the default dependent data
               mr: float[100]      --> the default independent data

.. compound::

   .. rubric:: 2-D data example showing how to identify the default data and associated dimension scales

   A 2-D data set, *data* as a function of *time* and *pressure* is described.
   By default as indicated by the ``axes`` attribute, 
   *pressure* is to be used.
   The *temperature* array is described as a substitute for *pressure* 
   (so it replaces dimension ``1`` of ``data`` as indicated by the 
   ``temperature_indices`` attribute).  
   
   .. code-block:: text
         :linenos:
      
         datafile.hdf5:NeXus data file
           @default="entry"
           entry:NXentry
             @default="data_2d"
             data_2d:NXdata
               @signal="data"
               @axes=["time","pressure"]
               @pressure_indices=1
               @temperature_indices=1
               @time_indices=0
               data: float[1000,20]
               pressure: float[20]
               temperature: float[20]
               time: float[1000]

-----------


.. _Design-FindPlottable-ByName:

Associating plottable data by name using the ``axes`` attribute
===============================================================

.. warning:: Discouraged:
   See this method: :ref:`Design-FindPlottable-NIAC2014`.

This method defines an attribute of the data field
:index:`called <axes (attribute)>` *axes*.
The ``axes`` attribute contains the names of
each :index:`dimension scale <dimension; dimension scales>`
as a colon (or comma) separated list in the order they appear in C.
For example:

.. compound::

    .. rubric:: denoting axes by name

    .. literalinclude:: examples/axes-byname.xml.txt
        :tab-width: 4
        :linenos:
        :language: text

-----------

.. _Design-FindPlottable-ByDimNumber:

Associating plottable data by dimension number using the ``axis`` attribute
===========================================================================

.. warning:: Discouraged:
   See this method: :ref:`Design-FindPlottable-ByName`

The original method defines an attribute of each dimension
scale field :index:`called <axis>` *axis*.
It is an integer whose value is the number of
the dimension, in order of 
:index:`fastest varying dimension <dimension; fastest varying>`.
That is, if the array being stored is data with elements
``data[j][i]`` in C and
``data(i,j)`` in Fortran, where ``i`` is the
time-of-flight index and ``j`` is
the polar angle index, the ``NXdata`` :index:`group <NXdata (base class)>`
would contain:

.. compound::

    .. rubric:: denoting axes by integer number

    .. literalinclude:: examples/axes-bydimnumber.xml.txt
        :tab-width: 4
        :linenos:
        :language: text

The ``axis`` attribute must
be defined for each dimension scale.
The ``primary`` attribute is unique to this method.

There are limited circumstances in which more
than one :index:`dimension scale <dimension; dimension scales>`
for the same data dimension can be included in the same ``NXdata`` group.
The most common is when the dimension scales are
the three components of an
*(hkl)* scan. In order to
handle this case, we have defined another attribute
of type integer called
``primary`` whose value determines the order
in which the scale is expected to be chosen for :index:`plotting`, i.e.

+ 1st choice: ``primary=1``

+ 2nd choice: ``primary=2``

+ etc.

If there is more than one scale with the same value of the ``axis`` attribute, one
of them must have set ``primary=1``. Defining the ``primary``
attribute for the other scales is optional.

	.. note:: The ``primary`` attribute can only be
	          used with the first method of defining  
             :index:`dimension scales <dimension; dimension scales>`
	          discussed above. In addition to
	          the ``signal`` data, this
	          group could contain a data set of the same  :index:`rank <rank>`
	          and dimensions called ``errors``
	          containing the standard deviations of the data.

.. 2016-01-23,PRJ: not necessary
   Perhaps substitute with the discussion from NIAC2014?
   https://www.nexusformat.org/2014_axes_and_uncertainties.html
   
   .. _Design-Linking-Discussion:
   
   Discussion of the two linking methods
   =====================================
   
   In general the method using the ``axes`` attribute on the multi dimensional
   data set should be preferred. This leaves the actual axis describing data sets
   unannotated and allows them to be used as an axis for other multi dimensional
   data.  This is especially a concern as an axis describing a data set may be linked
   into another group where it may describe a 
   :index:`completely different dimension <dimension; data set>`
   of another data set.
   
   Only when alternative axes definitions are needed, the ``axis`` method
   should be used to specify an axis of a data set.  This is shown in the example above for
   the ``some_other_angle`` field where ``axis=1``
   denotes another possible primary axis for plotting.  The default
   axis for plotting carries the ``primary=1`` attribute.
   
   Both methods of linking data axes will be supported in NeXus
   utilities that identify 
   :index:`dimension scales <dimension; dimension scales>`,
   such as ``NXUfindaxis()``.
