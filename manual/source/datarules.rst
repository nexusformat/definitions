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
  This set may be described by a regular expression 
  syntax :index:`regular expression`
  :ref:`regular expression syntax <RegExpName>`,
  as described below.

* For the class names [#]_ of NeXus *group* items,
  the prefix *NX* is reserved. 
  Thus all NeXus class names start with NX.
  The chapter titled :ref:`ReferenceDocumentation` lists the 
  available NeXus class names as either *base classes*, 
  *application definitions*, or *contributed definitions*.

.. [#] The *class name* is the value assigned to the
   *NX_class* attribute of an HDF5 group in the NeXus data file.
   This *class name* is different than the *name* of the HDF5 group.
   This is important when not using the NAPI to either read or write
   the HDF5 data file.

.. compound::

   .. _RegExpName:
   
   .. rubric:: Regular expression pattern for NXDL group and field names
   
   It is recommended that all group and field names 
   contain only these characters:
   
   * lower case letters
   * digits
   * "_" (underscore character)
   
   and that they begin with a lower case letter.
   This is the regular expression used to check 
   this recommendation.
    
   .. code-block:: guess
       :linenos:
   
       [a-z_][a-z\d_]*
   
   The length should be limited to no more than 
   63 characters (imposed by the HDF5 :index:`rules <rules; HDF5>` for names).
   
   It is recognized that some facilities will construct
   group and field names with upper case letters.  *NeXus data 
   files with upper case characters in the group or field 
   names might not be accepted by all software that reads NeXus 
   data files.*  Hence, group and field names that do not
   pass the regular expression above but pass this
   expression:
   
   .. code-block:: guess
       :linenos:
   
       [A-Za-z_][\w_]*
   
   will be flagged as a warning during data file validation.
	

.. rubric:: Use of underscore in descriptive names

Sometimes it is necessary to combine words in order to build a
descriptive name for a field or a group.
In such cases lowercase words are connected by underscores.

.. code-block:: guess
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


.. _Design-ArrayStorageOrder:

NeXus Array Storage Order
#########################

NeXus stores :index:`multi-dimensional <dimension; storage order>` 
arrays of physical values in C language storage order,
where the last dimension is the fastest varying. This is the rule.
*Good reasons are required to deviate from this rule.*

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
        :language: guess

.. compound::

    .. rubric:: Offset and Stride for 2D Data

    .. literalinclude:: examples/offset-stride-2d.txt
        :tab-width: 4
        :linenos:
        :language: guess

.. compound::

    .. rubric:: Offset and Stride for 3D Data

    .. literalinclude:: examples/offset-stride-3d.txt
        :tab-width: 4
        :linenos:
        :language: guess

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
valid item name  ``^[A-Za-z_][A-Za-z0-9_]*$``
valid class name ``^NX[A-Za-z0-9_]*$``
================ ============================

NeXus supports numeric data as either integer or floating-point
numbers.  A number follows that indicates the number of bits in the word.
The table above shows the regular expressions that
matches the data type specifier.

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

**strings**
    All strings are to be encoded in UTF-8. Since most strings in a
    NeXus file are restricted to a small set of characters and the first 128 characters are standard across encodings,
    the encoding of most of the strings in a NeXus file will be a moot point.
    Where encoding in UTF-8 will be important is when recording peoples names in ``NXuser``
    and text notes in ``NXnotes``.
    Because the few places where encoding is important also have unpredictable content, as well as the way in which
    current operating systems handle character encoding, it is practically impossible to test the encoding used. Hence,
    ``nxvalidate`` provides no messages relating to character encoding.

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
e.g. ``1996-07-31T21:15:22+0600``.
The standard also allows for time intervals in fractional seconds
with *1 or more digits of precision*.
This avoids confusion, e.g. between U.S. and European conventions,
and is appropriate for machine sorting.

.. _ISO 8601: http://www.w3.org/TR/NOTE-datetime
.. [#] ISO 8601: http://www.w3.org/TR/NOTE-datetime


.. compound::

    .. rubric:: strftime() format specifiers for ISO-8601 time

    .. code-block:: guess
    
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

.. _Unidata UDunits: http://www.unidata.ucar.edu/software/udunits/udunits-2.2.14/doc/udunits/udunits2.html#Database
.. [#UDunits]
    The :index:`UDunits`
    specification also includes instructions  for derived units.
    At present, the contents of NeXus ``units`` attributes
    are not validated in data files.

    ..  thus backwards compatible

.. index:: dimension
	!multi-dimensional data
	data; multi-dimensional

.. _multi-dimensional-data:

Linking Multi Dimensional Data with Axis Data
#############################################

NeXus allows to store multi dimensional arrays of data.  In most cases
it is not sufficient to just have the indices into the array as a label for
the dimensions of the data. Usually the information which physical value
corresponds to an index into a dimension of the multi dimensional data set.
To this purpose a means is needed to locate appropriate data arrays which describe
what each dimension of a multi dimensional data set actually corresponds too.
There is a standard HDF facility to do this: it is called 
:index:`dimension scales <dimension; dimension scales>`.
Unfortunately, at a time, there was only one global namespace for dimension scales.
Thus NeXus had to come up with its own scheme for locating axis data which is described
here. A side effect of the NeXus scheme is that it is possible to have multiple
mappings of a given dimension to physical data. For example a TOF data set can have the TOF
dimension as raw TOF or as energy.

There are two methods of 
:index:`linking <link>`
each data dimension to its respective dimension scale.
The preferred method uses the ``axes`` attribute
to specify the names of each 
:index:`dimension scale <dimension; dimension scales>`.
The original method uses the ``axis`` attribute to identify
with an integer the axis whose value is the number of the dimension.
After describing each of these methods, the two methods will be compared.
A prerequisite for both methods is that the fields describing the axis
are stored together with the multi dimensional data set whose axes need to be defined
in the same NeXus group. If this leads to data duplication, use links.

.. _Design-Linking-ByName:

Linking by name using the ``axes`` attribute
============================================

The preferred method is to define an attribute of the data itself
:index:`called <axes (attribute)>` *axes*.
The ``axes`` attribute contains the names of
each :index:`dimension scale <dimension; dimension scales>`
as a colon (or comma) separated list in the order they appear in C.
For example:

.. compound::

    .. rubric:: Preferred way of denoting axes

    .. literalinclude:: examples/axes-preferred.xml.txt
        :tab-width: 4
        :linenos:
        :language: guess

.. _Design-LinkingByDimNumber:

Linking by dimension number using the ``axis`` attribute
========================================================

The original method is to define an attribute of each dimension
scale :index:`called <axis>` *axis*.
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

    .. rubric:: Original way of denoting axes

    .. literalinclude:: examples/axes-old.xml.txt
        :tab-width: 4
        :linenos:
        :language: guess

The ``axis`` attribute must
be defined for each dimension scale.
The ``primary`` attribute is unique to this method of linking.

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
	          used with the first method of defining  :index:`dimension scales <dimension; dimension scales>`
	          discussed above. In addition to
	          the ``signal`` data, this
	          group could contain a data set of the same  :index:`rank <rank>`
	          and dimensions called ``errors``
	          containing the standard deviations of the data.

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
of the experimental probe rather than the
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

Any program whose aim is to identify the default plottable data 
should use the following procedure:

#. Start at the top level of the NeXus data file.

#. Loop through the groups with class ``NXentry`` 
   until the next step succeeds.

#. Open the NXentry group and loop through the subgroups 
   with class ``NXdata`` until the next step succeeds.

#. Open the NXdata group and loop through the fields for the one field 
   with attribute ``signal="1"``.
   Note: There should be *only one* field that matches.

   This is the default plottable data.

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

.. the previous description

	#. Open the first top level NeXus group with class
	   ``NXentry``.

	#. Open the first NeXus group with class
	   ``NXdata``.

	#. Loop through NeXus fields in this group searching for the item
	   with attribute
	   ``signal="1"``
	   indicating this field has the plottable data.

	#. Check to see if this field has an attribute called
	   ``axes``. If so, the attribute value contains a colon (or comma)
	   delimited list (in the C-order of the data array) with the names
	   of the 
	   :index:`dimension scales <dimension scale>`
	   associated with the plottable data. And
	   then you can skip the next two steps.

	#. If the ``axes`` attribute is not defined, search for the 
	   one-dimensional NeXus fields with attribute ``primary=1``.

	#. These are the dimension scales to label 
	   the axes of each dimension of the data.

	#. Link each dimension scale
	   to the respective data dimension by
	   the ``axis`` attribute (``axis=1``, ``axis=2``, 
	   ... up to the  :index:`rank <rank>` of the data).

	#. If necessary, close the
	   ``NXdata``
	   group, open the next one and repeat steps 3 to 6.

	#. If necessary, close the
	   ``NXentry``
	   group, open the next one and repeat steps 2 to 7.

Consult the :ref:`NeXus API <Introduction-NAPI>`
section, which describes the routines available to program these
operations. In the course of time, generic NeXus browsers will
provide this functionality automatically.
