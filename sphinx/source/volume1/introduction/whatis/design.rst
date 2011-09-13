.. $Id$


.. _Introduction-DesignPrinciples:

A Set of Design Principles
---------------------------------------------------------------------

.. index:: NeXus; Design Principles

NeXus data files contain four types of entity: 
data groups, data fields, attributes, and links. 
See :ref:`Design-Groups` for more details.

1. Data Groups
	*Data groups* are like folders that can contain 
	a number of fields and/or other groups.

.. index:: data objects; groups

2. Data Fields
	*Data fields*
	can be scalar values or multidimensional arrays of a
	variety of sizes (1-byte, 2-byte, 4-byte, 8-byte) and types
	(characters, integers, floats).  In HDF, fields are
	represented as HDF *Scientific Data Sets*
	(also known as SDS).

.. index:: data objects; fields
.. index:: HDF; Scientific Data Sets
.. see also - data objects, fields
.. index:: Scientific Data Sets
.. see also - data objects, fields
.. index:SDS
.. see also - data objects, fields

3. Data Attributes
	Extra information required to
	describe a particular group or field, 
	such as the data units,
	can be stored as a data attribute.

.. index:: units
.. index:: attributes; data
.. index:: data objects; attributes

4. Links
	Links are used to reference the plottable data
	from ``NXdata`` when the data is provided in 
	other groups such as ``NXmonitor`` or ``NXdetector``.

.. index:: NeXus basic motivation; default plot
.. index:: link

In fact, a NeXus file can be viewed as a computer file system. Just as files
are stored in folders (or subdirectories) to make them easy to locate, so NeXus
fields are stored in groups. The group hierarchy
is designed to make it easy to navigate a NeXus file.

.. index:: hierarchy


.. _Introduction-ExampleFile:

Example of a NeXus File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following diagram shows an example of a NeXus data file 
represented as a tree structure.

.. index:: hierarchy; example NeXus data file

.. figure:: ../../../manual/img/Hierarchy.png
	:width: 300 pt
	:alt: example NeXus data file hierarchy

	Example of a NeXus data file

Note that each field is identified by a name, such as ``counts``,
but each group is identified both by a name and, after a colon as a 
delimiter, the class type, e.g., ``monitor:NXmonitor``). 
The class types, which all begin with ``NX``, 
define the sort of fields that the group should contain, in this
case, counts from a beamline monitor. The hierarchical design, with data
items nested in groups, makes it easy to identify information if you are
browsing through a file. 


.. _Introduction-ImportantClasses:

Important Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here are some of the important classes found in nearly all NeXus files. A
complete list can be found in the NeXus Design section (:ref:`NeXus-Design`).

.. note:: ``NXentry`` and ``NXdata``
	are the only two classes **required** in a valid NeXus data file.

.. index:: classes; base class: NXentry

``NXentry``
	(**Required:**)
	The top level of any NeXus file contains one or more
	groups with the class ``NXentry``.
	These contain all the data that is required to
	describe an experimental run or scan. Each
	``NXentry`` typically contains a number of
	groups describing sample information (class
	``NXsample``), instrument details (class
	``NXinstrument``), and monitor counts (class
	``NXmonitor``).  

.. index:: classes; base class: NXdata
.. index:: NeXus basic motivation; default plot

``NXdata``
	(**Required:**)
	Each ``NXentry`` group contains one or more
	groups with class ``NXdata``. 
	These groups contain the experimental results
	in a self-contained way, i.e., it should be possible to
	generate a sensible plot of the data
	from the information
	contained in each ``NXdata`` group. That means it
	should contain the axis labels and titles as well as the
	data.

.. index:: classes; base class: NXsample

``NXsample``
	A ``NXentry`` group will often contain a group
	with class ``NXsample``. 
	This group contains information pertaining to
	the sample, such as its chemical composition, mass, and
	environment variables (temperature, pressure, magnetic
	field, etc.).

.. index:: classes; base class: NXinstrument

``NXinstrument``
	There might also be a group with class
	``NXinstrument``.
	This is designed to encapsulate all the
	instrumental information that might be relevant to a
	measurement, such as flight paths, collimations, chopper
	frequencies, etc.

.. figure:: ../../../manual/img/NXinstrument.png
	:width: 200 pt
	:alt: example NeXus data file hierarchy

	NXinstrument excerpt

Since an instrument can comprise several beamline components each
defined by several parameters, they are each specified by a separate group.
This hides the complexity from generic file browsers, but makes the
information available in an intuitively obvious way if it is required.


.. _Introduction-SimpleExample:

Simple Data File Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NeXus data files do not need to be complicated. 
In fact, the following diagram shows an extremely simple NeXus file
(in fact, the simple example shows the minimum information necessary
for a NeXus data file) that could be used to transfer
data between programs. (Later in this section, we show how to write and 
read this simple example.)

.. _fig.simple-example:

.. figure:: ../../../manual/img/Simple.png
	:width: 250 pt
	:alt: Simple Data File Example figure

	Simple Data File Example
 
This illustrates the fact that the structure of NeXus files is
extremely flexible. It can accommodate very complex instrumental
information, if required, but it can also be used to store very simple data
sets.  In the next example, a NeXus data file is shown as XML:

.. _ex.verysimple.xml:

``verysimple.xml``: A very simple NeXus Data file (in XML)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml
	:linenos: 

	<?xml version="1.0" encoding="UTF-8"?>
	  <NXroot NeXus_version="4.3.0" XML_version="mxml"
		file_name="verysimple.xml"
		xmlns="http://definition.nexusformat.org/schema/3.1"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xsi:schemaLocation="http://definition.nexusformat.org/schema/3.1 
		                    http://definition.nexusformat.org/schema/3.1/BASE.xsd"
		file_time="2010-11-12T12:40:17-06:00">
		<NXentry name="entry">
		  <NXdata name="data">
			<counts 
			  NAPItype="NX_INT64[15]" 
			  long_name="photodiode counts" 
			  signal="NX_INT32:1" 
			  axes="two_theta">
				   1193       4474 
				  53220     274310 
				 515430     827880 
				1227100    1434640 
				1330280    1037070 
				 598720     316460 
				  56677       1000 
				   1000 
			</counts>
			<two_theta 
			  NAPItype="NX_FLOAT64[15]" 
			  units="degrees" 
			  long_name="two_theta (degrees)">
				18.90940         18.90960         18.90980         18.91000 
				18.91020         18.91040         18.91060         18.91080 
				18.91100         18.91120         18.91140         18.91160 
				18.91180         18.91200         18.91220 
			</two_theta>
		  </NXdata>
		</NXentry>
	  </NXroot>

.. index:: example; very simple

NeXus files are easy to create.  This example NeXus file was created using
a short Python program and NeXpy:

.. _ex.verysimple.py:

``verysimple.py``: Using NeXpy to write a very simple NeXus Data file (in HDF5)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. index:: example; very simple
.. literalinclude:: ../../../../manual/examples/verysimple.py
	:linenos: 
	:tab-width: 4
