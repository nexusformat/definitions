.. index::
   see: physical file format; file format
   file format
   see: low-level file format; file format
   NAPI; bypassing

.. _Fileformat:

====================
Physical File format
====================

This section describes how NeXus structures are mapped to features of the underlying
physical file format.
This is a guide for people who wish to create NeXus files without
using the NeXus-API.

.. _Fileformat-HDF-Choice:

.. index::
   pair: HDF; file format

Choice of HDF as Underlying File Format
#######################################

At its beginnings, the founders of NeXus identified the
Hierarchical Data Format (HDF) as a capable and efficient multi-platform 
data storage format. HDF was designed for large data sets and already 
had a substantial user community. HDF was developed and maintained
initially by the National Center for Supercomputing Applications (NCSA)
at the University of Illinois at Urbana-Champaign (UIUC) and later spun 
off into its own group called The HDF Group (THG: http://www.hdfgroup.org/). 
Rather then developing its own unique physical file format, the NeXus group 
choose to build NeXus on top of HDF.

HDF (now HDF5) is provided with
software to read and write data (this is the application-programmer interface, or API)
using a large number of computing systems in common use for neutron and
X-ray science. HDF is a binary data file format that supports compression and structured
data.



.. _Fileformat-Mapping-HDF:

Mapping NeXus into HDF
######################

.. index::
   single: field; HDF
   single: group; HDF
   single: attribute; HDF


NeXus data structures map directly to HDF structures.
NeXus *groups* are HDF5 *groups* and
NeXus *fields* (or data sets) are HDF5 *datasets*.
Attributes map directly to HDF group or dataset attributes.
The NeXus class is stored as an attribute to the HDF5 group 
with the name ``NX_class`` with value of the NeXus class name.
(For legacy NeXus data files using HDF4, groups are HDF4 *vgroups*
and fields are HDF4 *SDS (scientific data sets)*.  HDF4 does 
not support group attributes.  HDF4 supports a group class
which is set with the ``Vsetclass()`` call
and read with ``VGetclass()``.)

A NeXus ``link`` directly maps to the HDF hard link mechanisms.

.. note:: **Examples** are provided in the :ref:`Examples` chapter.
          These examples include software to write and read NeXus data files using the NAPI, as
          well as other software examples that use native (non-NAPI) libraries.  In some cases the
          examples show the content of the NeXus data files that are produced.
          Here are links to some of the examples:
          
          - :ref:`Introduction-HowToWrite`
          - :ref:`Introduction-HowToRead`
          - :ref:`example.napi.simple.2d.write`
          - :ref:`code_native.writing`
          - :ref:`code_native.reading`
          - :ref:`Example-H5py-Writing`
          - :ref:`Example-H5py-Reading`

Perhaps the easiest way to view the implementation of NeXus in HDF5 is to view
how the data structures look.  For this, we use the ``h5dump`` command-line
utility provided with the HDF5 support libraries.  Short examples are provided for the
basic NeXus data components:

- :ref:`group <h5dump_group>`:
  created in C NAPI by:
  
  .. code-block:: c

	  NXmakegroup (fileID, "entry", "NXentry");

- :ref:`field <h5dump_field>`:
  created in C NAPI by:
  
  .. code-block:: c

	  NXmakedata (fileID, "two_theta", NX_FLOAT32, 1, &n);
	    NXopendata (fileID, "two_theta");
	  NXputdata (fileID, tth);

- :ref:`attribute <h5dump_attribute>`:
  created in C NAPI by:
  
  .. code-block:: c

	  NXputattr (fileID, "units", "degrees", 7, NX_CHAR);

- :ref:`link <h5dump_link>`
  created in C NAPI by:
  
  .. code-block:: c

     NXmakelink (fileid, &itemid);
     # -or-
     NXmakenamedlink (fileid, "linked_name", &itemid);

See the sections :ref:`example.napi.simple.2d.write`
and  :ref:`example.napi.simple.3d.write.python` in the :ref:`Examples`
chapter for examples that use the native HDF5 calls to write NeXus data files.

.. compound::

    .. rubric:: ``h5dump`` of a NeXus ``NXentry`` group
    
    .. _h5dump_group:

    .. literalinclude:: examples/h5dump_group.txt
        :tab-width: 4
        :linenos:
        :language: text

.. compound::

    .. rubric:: ``h5dump`` of a NeXus field (HDF5 dataset)
    
    .. _h5dump_field:

    .. literalinclude:: examples/h5dump_field.txt
        :tab-width: 4
        :linenos:
        :language: text

.. compound::

    .. rubric:: ``h5dump`` of a NeXus attribute
    
    .. _h5dump_attribute:

    .. literalinclude:: examples/h5dump_attribute.txt
        :tab-width: 4
        :linenos:
        :language: text

.. compound::

    .. rubric:: ``h5dump`` of a NeXus link
    
    .. _h5dump_link:

    .. literalinclude:: examples/h5dump_link.txt
        :tab-width: 4
        :linenos:
        :language: text


..	XML is no longer a supported backend file format
	.. _Fileformat-Mapping-XML:

	Mapping NeXus into XML
	######################

	.. index::
	   pair: file format; XML
	   file attribute
	   NXroot (base class); attributes

	This takes a bit more work than HDF.
	At the root of NeXus XML file
	is a XML element with the name ``NXroot``.
	Further XML attributes to
	``NXroot`` define the NeXus file level attributes.
	An example NeXus XML data file is provided in the
	:ref:`Introduction` chapter as
	Example :ref:`A very simple NeXus Data file (in XML) <fig.simple-data-file-xml>`.

	NeXus groups are encoded into XML as elements with the
	name of the NeXus class and an XML attribute ``name`` which defines the
	NeXus name of the group. Further group attributes become XML attributes. An example:

	.. compound::

		.. rubric:: NeXus group element in XML

		.. literalinclude:: examples/mapping1.xml.txt
			:tab-width: 4
			:linenos:
			:language: xml

	NeXus data sets are encoded as XML elements with
	the name of the data. An attribute ``NAPItype`` defines the type and
	:index:`dimensions <dimension>`
	of the data. The actual data is
	stored as ``PCDATA`` [#PCDATA]_ in the element. Another example:

	.. [#PCDATA]
		``PCDATA`` is the XML term for
		*parsed character data* (see: http://www.w3schools.com/xml/xml_cdata.asp).

	.. compound::

		.. rubric:: NeXus data elements

		.. literalinclude:: examples/mapping2.xml.txt
			:tab-width: 4
			:linenos:
			:language: xml

	.. index::
	   attribute; XML

	Data are printed in appropriate formats and in C storage order.
	The codes understood for ``NAPItype`` are
	all the NeXus data type names. The 
	:index:`dimensions <dimension>`
	are given in square brackets as a comma
	separated list. No dimensions need to be given if
	the data is just a single value.
	Data attributes are represented as XML attributes.
	If the attribute is not a text string, then the
	attribute is given in the form: *type:value*, for example:
	``tth_indices="NX_POSINT:1"``.


	:index:`NeXus links <link>` are stored in XML as XML elements
	with the :index:`name <NAPIlink>`  ``NAPIlink``
	and a XML attribute ``target`` which stores the path to the linked
	entity in the file.  If the item is linked under
	a different name, then this name is specified as a XML attribute name to
	the element ``NAPIlink``.

	The authors of the NeXus API worked with the author of the miniXML XML library to
	create a reasonably efficient way of handling numeric data with XML. Using the NeXus API handling
	something like 400 detectors versus 2000 time channels in XML is not a problem. But you may
	hit limits with XML as the file format when data becomes to large or you try to process NeXus
	XML files with general XML tools. General XML tools are normally ill prepared to process large
	amounts of numbers.

	.. _Fileformat-SpecialAttributes:

	Special Attributes
	##################

	.. index::
	   see: attribute; internal attribute
	   ! single: internal attribute

	NeXus makes use of some special attributes for its internal purposes.
	These attributes are stored as normal group or data set attributes
	in the respective file format. These are:

	.. index::
	   see: target; link target (internal attribute)
	   ! single: link target (internal attribute)

	**target**
		This attribute is automatically created when items get linked.
		The target attribute contains a text string with
		the path to the source of the item linked.

	.. index::
	   ! single: napimount (internal attribute)
	   see: linking (external); napimount (internal attribute)

	**napimount**
		The ``napimount`` attribute is used to implement
		external linking in NeXus.
		The string is a URL to the file and group in the
		external file to link too. The system is meant to be extended.
		But as of now, the only format supported is:
		
		.. code-block:: text
		
			nxfile://path-to-file#path-infile

		This is a NeXus file in the file system at *path-to-file*
		and the group *path-infile* in that NeXus file.

	.. index::
	   ! single: NAPIlink (internal attribute)
	   see: linking (internal); NAPIlink (internal attribute)

	**NAPIlink**
		NeXus supports linking items in another group under another name.
		This is only supported natively in HDF5.
		For HDF-4 and XML a crutch is needed.
		This crutch is a special class name or attribute
		``NAPIlink`` combined with the
		target attribute. For groups, ``NAPILink``
		is the group class, for data items a special attribute
		with the name ``NAPIlink``.
