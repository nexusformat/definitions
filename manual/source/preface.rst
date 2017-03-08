..  _PrefaceChapter:

.. Is this needed now?  Most of this content (commented out here) is presented elsewhere.
	=======
	Preface
	=======

	..
		.. image:: img/NeXus.png

	With revision 3.1 of the manual, NeXus introduced a complete version
	of the documentation of the NeXus standard.  The content from the wiki
	at the time
	was converted, augmented (in some parts significantly), clarified,
	and indexed.  The NeXus Definition Language (NXDL) was introduced 
	to define base classes and application definitions.
	NXDL established a method to define NeXus classes according to one of three classifications:

	#. *base classes* (that represent the components used
	   to build a NeXus data file)

	#. *application definitions* (used to define a minimum
	   set of data for a specific purpose such as scientific data processing
	   or an instrument definition)

	#. *contributed definitions* (definitions and specifications
	   that are in an incubation status before ratification by the NIAC).

	Additional examples have been added to respond to
	inquiries from the users of the NeXus standard about implementation
	and usage.  

	Hopefully, this improved documentation, with
	more examples and the new NXDL, will reduce
	the learning barriers incurred by those new to NeXus.

Representation of data examples
###############################

Most of the examples of data files have been written in a format
intended to show the structure of the file rather than the data content.
In some cases, where it is useful, some of the data is shown.
Consider this prototype example:

.. compound::

    .. rubric:: example of NeXus data file structure

    .. _examples-prototype:

    .. literalinclude:: examples/examples-prototype.txt
        :tab-width: 4
        :linenos:
        :language: text

Some words on the notation:

- Hierarchy is represented by indentation. Objects on the same indentation level
  are in the same group

- The combination ``name:NXclass`` denotes a NeXus group with name ``name``
  and class ``NXclass``.

- A simple name (no following class) denotes a field.
  An equal sign is used to show the value, where this is important to the example.

- Sometimes, a data type is specified and possibly a set of dimensions.
  For example,
  ``energy:NX_NUMBER[NE]`` says
  *energy* is a 1-D array of numbers
  (either integer or floating point)
  of length ``NE``.

- Attributes are noted as @name="value" pairs.
  The ``@`` symbol only indicates this is an attribute
  and is not part of the attribute name.

- Links are shown with a text arrow ``-->`` indicating the
  source of the link (using HDF5 notation listing the sequence of *names*).

Line 1 shows that there is one group at the root level of the file named
``entry``.  This group is of type ``NXentry``
which means it conforms to the specification of the ``NXentry``
NeXus base class.  Using the HDF5 nomenclature, we would refer to this
as the ``/entry`` group.

Lines 2, 8, and 10:
The ``/entry`` group contains three subgroups:
``instrument``, ``sample``, and ``data``.
These groups are of type ``NXinstrument``, ``NXsample``,
and ``NXdata``, respectively.

Line 4: The data of this example is stored in the
``/entry/instrument/detector`` group in the dataset called
``data`` (HDF5 path is ``/entry/instrument/detector/data``).
The indication of ``data:\[]`` says that ``data`` is an
array of unspecified dimension(s).

Line 5:
There is one attribute of ``/entry/instrument/detector/data``:
``long_name``.  This attribute *might* be used by a
plotting program as the axis title.

Line 6 (reading ``bins:\[0, 1, 2, ... 1023]``) shows that
``bins`` is a 1-D array of length presumably 1024.  A small,
representative selection of values are shown.

Line 7: an attribute that shows a descriptive name of
``/entry/instrument/detector/bins``.  This attribute
might be used by a NeXus client while plotting the data.

Line 9 (reading ``name = "zeolite"``) shows
how a string value is represented.

Line 11 says that the default data to be plotted is called ``data``.

Line 12 says that each axis *dimension scale* of ``data`` is described
by the field called ``bins``.

Line 13 says that ``bins`` will be used for axis 0 and axis 1 of ``data``.

Lines 14-15:
The ``/entry/data``) group has two datasets that are actually
linked as shown to data sets in a different group.  
(As you will see later, the ``NXdata`` group
enables NeXus clients to easily determine what to
offer for display on a default plot.)

.. _preface.Class.path.specification:

Class path specification
########################

In some places in this documentation, a path may be shown
using the class types rather than names.  For example::

	/NXentry/NXinstrument/NXcrystal/wavelength

identifies a dataset called ``wavelength`` that is inside a 
group of type ``NXcrystal`` ... 

As it turns out, this syntax is the 
syntax used in NXDL :ref:`link` specifications. This syntax is also 
used when the exact name of each group is either unimportant 
or not specified.

If default names are taken for each class, then the 
above class path is expressed as this equivalent HDF5 path::

	/entry/instrument/crystal/wavelength

In some places in this documentation, where clarity is 
needed to specify both the path and class name, you may 
find this equivalent path::

	/entry:NXentry/instrument:NXinstrument/crystal:NXcrystal/wavelength
