.. $Id$

.. _Introduction:

==================
NeXus Introduction
==================

In recent years, a community of scientists and computer programmers working in neutron
and synchrotron facilities around the world came to the conclusion that a 
:index:`common data format <NeXus basic motivation; unified format>`
would fulfill a valuable function in the scattering community. As
instrumentation becomes more complex and data visualization become more challenging,
individual scientists, or even institutions, have found it difficult to keep up with new
developments. A common data format makes it easier, both to exchange experimental results
and to exchange ideas about how to analyze them. It promotes greater cooperation in software
development and stimulates the design of more sophisticated visualization tools.
Additional background information is given in the chapter titled :ref:`History`.

This section is designed to give a brief introduction to NeXus, the data format and tools
that have been developed in response to these needs. It explains what a modern data format
such as NeXus is and how to write simple programs to read and write NeXus files.

The programmers who produce intermediate files for
storing analyzed data should agree on simple interchange 
:index:`rules <rules>`.

..  =======================
    section: What is NeXus?
    =======================

.. _WhatIsNeXus:

What is NeXus?
##############

The  :index:`NeXus <!NeXus>` data format has four components:

:ref:`A set of design principles <Introduction-DesignPrinciples>`
    to help people understand what is in the data files.

:ref:`A set of data storage objects <Introduction-DataStorageObjects>`
    (:ref:`base.class.definitions`
    and :ref:`application.definitions`)
    to allow the development of portable analysis software.

:ref:`A set of subroutines <Introduction-SetOfSubroutines>`
    :ref:`Utilities <Utilities>` and :ref:`examples <Examples>` to make it easy
    to read and write NeXus data files.

:ref:`A Scientific Community <Introduction-Community>`
    to provide the scientific data, advice, and continued involvement
    with the NeXus standard. NeXus provides a forum for the scientific
    community to exchange ideas in data storage.

In addition, NeXus relies on a set of low-level file formats to actually
store NeXus files on physical media. Each of these components are described in more
detail in the :ref:`Fileformat` section.

The NeXus Application-Programmer Interface 
:index:`(NAPI) <NAPI>`, which
provides the set of subroutines for reading and writing NeXus data files,
is described briefly in :ref:`Introduction-NAPI`.
(Further details are provided in the :ref:`NAPI <NAPI>` chapter.)

The principles guiding the design and implementation of the NeXus standard
are described in the :ref:`Design` chapter.

Base classes, which comprise the data storage objects used in NeXus data files,
are detailed in the :ref:`base.class.definitions` chapter.

..  With this information, it should be possible to bypass the NAPI and
    read & write NeXus data directly in the low-level file format.

Additionally, a brief list describing the set of NeXus Utilities
available to browse, validate, translate, and visualise
NeXus data files is provided in the :ref:`Utilities` chapter.

.. _Introduction-DesignPrinciples:

A Set of Design Principles
==========================

NeXus :index:`data files <NeXus; Design Principles>`
contain four types of entity:
data groups,
data fields,
attributes, and
links.

:ref:`Design-Groups`
    Data :index:`groups <data objects; groups>`
    are like folders that can contain a number of fields
    and/or other groups.

:ref:`Design-Fields`
    Data :index:`fields <data objects; fields>`
    can be scalar values or multidimensional arrays of a
    variety of sizes (1-byte, 2-byte, 4-byte, 8-byte) and types
    (characters, integers, floats).  In HDF, fields are
    represented as HDF *Scientific Data Sets*
    (also known as SDS).
    
    .. index::
      single: HDF; Scientific Data Sets
      pair:   SDS; Scientific Data Sets
      see:    data objects, fields; Scientific Data Sets
      see:    data objects, fields; HDF
      see:    data objects, fields; SDS

:ref:`Design-Attributes`
    Extra information required to
    describe a particular group or field,
    such as the data 
    :index:`units <units>`,
    can be stored as a :index:`data attribute <pair: attributes; data>`.

:ref:`Design-Links`
    Links are used to reference the 
    :index:`plottable data <NeXus basic motivation; default plot>`
    from ``NXdata``
    when the data is provided in other groups
    such as ``NXmonitor`` :index:`or <link>` ``NXdetector``.

In fact, a NeXus file can be viewed as a computer file system. Just as files
are stored in folders (or subdirectories) to make them easy to locate, so NeXus
fields are stored in groups. The group :index:`hierarchy <hierarchy>`
is designed to make it easy
to navigate a NeXus file.

.. _Introduction-ExampleFile:

Example of a NeXus File
-----------------------

The following diagram shows an example of a NeXus data file represented as a
tree :index:`structure <hierarchy; example NeXus file>`.

	.. compound::
	
		.. _Figure.Example_NeXus_file:
	
	    .. rubric:: Example of a NeXus Data File
	
	    .. image:: img/Hierarchy.png
	        :width: 80%


Note that each field is identified by a name, such as ``counts``,
but each group is identified both by a name and, after a colon as a
delimiter, the class type, e.g., ``monitor:NXmonitor``).
The class types, which all begin with
``NX``, define the sort of fields that the group should contain, in this
case, counts from a beamline monitor. The hierarchical design, with data
items nested in groups, makes it easy to identify information if you are
browsing through a file.

.. _Introduction-ImportantClasses:

Important Classes
-----------------

Here are some of the important classes found in nearly all NeXus files. A
complete list can be found in the :ref:`Design` chapter.

.. note:: ``NXentry`` and ``NXdata``
          are the only two classes necessary to store the minimum
          amount of information in a valid NeXus data file.

:ref:`NXentry`
    *Required:*
    The top level of any NeXus file contains one or more
    groups with the :index:`class <base classes; NXentry>` ``NXentry``. 
    These contain all the data that is required to
    describe an experimental run or scan. Each
    ``NXentry`` typically contains a number of
    groups describing sample information (class
    ``NXsample``), instrument details (class
    ``NXinstrument``), and monitor counts (class
    ``NXmonitor``).

:ref:`NXdata`
    *Required:*
    Each ``NXentry`` group contains one or more
    groups with :index:`class <base classes; NXdata>` ``NXdata``. 
    These groups contain the experimental results
    in a self-contained way, i.e., it should be possible to
    generate a sensible :index:`plot <NeXus basic motivation; default plot>`
    of the data from the information
    contained in each ``NXdata`` group. That means it
    should contain the axis labels and titles as well as the
    data.

:ref:`NXsample`
    A ``NXentry`` group will often contain a group
    with :index:`class <base classes; NXsample>` ``NXsample``. 
    This group contains information pertaining to
    the sample, such as its chemical composition, mass, and
    environment variables (temperature, pressure, magnetic
    field, etc.).

:ref:`NXinstrument`
    There might also be a group with 
    :index:`class <base classes; NXinstrument>`
    ``NXinstrument``. This is designed to encapsulate all the
    instrumental information that might be relevant to a
    measurement, such as flight paths, collimation, chopper
    frequencies, etc.

	.. compound::
	
		.. _Figure.NXinstrument_excerpt:
	
	    .. rubric:: ``NXinstrument`` excerpt
	
	    .. image:: img/NXinstrument.png
	        :width: 50%

	Since an instrument can include several beamline components each
	defined by several parameters, the components are each specified by a separate group.
	This hides the complexity from generic file browsers, but makes the
	information available in an intuitively obvious way if it is required.

.. _Introduction-SimpleExample:

Simple Example
--------------

NeXus data files do not need to be complicated.
In fact, the following
diagram shows an extremely simple NeXus file
(in fact, the simple example shows the minimum information necessary
for a NeXus data file)
that could be used to transfer
data between programs. (Later in this section, we show how to write and
read this simple example.)

	.. compound::
	
		.. _fig.simple-example:
	
	    .. rubric:: Example structure of a simple data file
	
	    .. image:: img/Simple.png
	        :width: 60%


This illustrates the fact that the structure of NeXus files is
extremely flexible. It can accommodate very complex instrumental
information, if required, but it can also be used to store very simple data
sets. In the next example, a NeXus data file is shown as XML:

	.. compound::
	
		.. _fig.simple-data-file-xml:
	
	    .. rubric:: A very simple NeXus Data file (in XML)
	
	    .. literalinclude:: examples/verysimple.xml
	        :tab-width: 4
	        :linenos:
	        :language: xml

NeXus files are easy to create.  This example NeXus file was created using
a short Python program and NeXpy:

	.. compound::
	
		.. _fig.simple-data-file-hdf5-nexpy:
	
	    .. rubric:: Using NeXpy to write a very simple NeXus HDF5 Data file
	
	    .. literalinclude:: examples/verysimple.py
	        :tab-width: 4
	        :linenos:
	        :language: guess

.. _Introduction-DataStorageObjects:

A Set of Data Storage Objects
=============================

If the design principles are followed, it will be easy for anyone browsing a
NeXus file to understand what it contains, without any prior information.
However, if you are writing specialized
visualization or analysis software, you will need to
know precisely what specific information is contained
in advance. For that reason, NeXus
provides a way of defining the format for
particular :index:`instrument types <instrument definitions>`,
such as time-of-flight small angle neutron scattering. This requires
some agreement by the relevant communities, but enables the development of
much more portable software.

The set of data storage objects is divided into three parts:
base classes, application definitions, and contributed definitions.
The base classes represent a set of components that define
the dictionary of all possible terms to be used with that component.
The application definitions specify the minimum required information to satisfy
a particular scientific or data analysis software interest.
The contributed definitions have been submitted by the scientific community
for incubation before they are adopted by the NIAC or for availability
to the community.

These instrument definitions are formalized as XML files, using NXDL,
(as described in the :ref:`NXDL <NXDL>` chapter)
to specify the names of data fields, and other NeXus data objects.
The following is an example of such a file for
the simple NeXus file shown above.

.. compound::
	
	.. _fig.verysimple.nxdl.xml:

    .. rubric:: A very simple NeXus Definition Language (NXDL) file

    .. literalinclude:: examples/verysimple.nxdl.xml
        :tab-width: 4
        :linenos:
        :language: guess

Complete examples of reading and writing NeXus data files are 
provided :ref:`later <Examples>`.
This chapter has several examples of writing and reading NeXus data files.
If you want to define the format of a particular type of NeXus file
for your own use, e.g. as the standard output from a program, you are encouraged
to *publish* the format using this XML format.
An example of how to do this is shown in the
:ref:`NXDL_Tutorial-CreatingNxdlSpec` section.

.. _Introduction-SetOfSubroutines:

A Set of Subroutines
====================

NeXus data files are high-level so the user only needs to
know how the data are referenced in the file but does not
need to be concerned where the data are stored in the file.  Thus, the data
are most easily accessed using a subroutine library tuned to the
specifics of the data format.

In the past, a data format was defined by a document
describing the precise location of every item in the data file,
either as row and column numbers in an ASCII file, or as record
and byte numbers in a binary file. It is the job of the subroutine
library to retrieve the data.  This subroutine library is commonly
called an application-programmer interface or API.

For example, in NeXus, a program to read in the wavelength of an experiment
would contain lines similar to the following:

.. compound::
	
	.. _fig.ex-simple.c:

    .. rubric:: Simple example of reading data using the NeXus API

    .. literalinclude:: examples/ex-simple.c
        :tab-width: 4
        :linenos:
        :language: guess

In this example, the program requests the value of the data that has
the label ``wavelength``, storing the result in the variable lambda.
``fileID`` is a file identifier that is provided by NeXus when the
file is opened.

We shall provide a more complete example when we have discussed the contents
of the NeXus files.


.. _Introduction-Community:

Scientific Community
====================

NeXus began as a group of scientists with the goal of defining a
common data storage format
to exchange experimental results
and to exchange ideas about how to analyze them.

The :ref:`Community`
provides the scientific data, advice, and continued involvement
with the NeXus standard. NeXus provides a forum for the scientific
community to exchange ideas in data storage through the NeXus wiki.

The NeXus International Advisory Committee supervises the
development and maintenance of the NeXus common data
format for neutron, X-ray, and muon science.
The :ref:`NIAC` supervises a technical committee to oversee the
:ref:`NAPI` and the :ref:`ClassDefinitions`.


.. toctree::
   :maxdepth: 2
   :glob:
   
   motivations

..  =====================================
    section: NeXus Motivations
    =====================================

	.. include:: motivations.rst

..  ================================================
    section: NeXus Application Programming Interface
    ================================================

..  section: API

.. _Introduction-NAPI:

NAPI: The NeXus Application Programming Interface
#################################################

The :index:`NeXus API <! NAPI>` consists of routines to read and
write NeXus data files.
It was written to provide a simple to use and consistent common interface for
all supported backends (XML, HDF4 and HDF5) to
scientific programmers and other users of the NeXus Data Standard.

.. note:: It is not necessary to use the NAPI to write or read
	NeXus data files.  The intent of the NAPI is to simplify
	the programming effort to use the HDF programming
	interface.  There are :ref:`Examples` to help you understand.

This section will provide a brief overview of the available functionality.
Further documentation of the NeXus Application Programming Interface
(NAPI) for bindings to specific programming language can be found
in the :ref:`NAPI <NAPI>` chapter and may be downloaded
from the NeXus development site. [#]_

For an even more detailed description of the internal workings of NAPI
see :download:`NeXusIntern.pdf`, copied from the NeXus code repository.
That document is written for programmers who want to work on the NAPI itself.
If you are new to NeXus and just want to implement basic file reading or writing
you should not start by reading that.

.. _Introduction-HowToWrite:

How do I write a NeXus file?
============================

.. index:: file; write

The NeXus Application Program Interface :index:`(NAPI) <NAPI>`
provides a set of subroutines that make it easy to read and write
NeXus files. These subroutines are available in C, Fortran 77, Fortran 90, Java,
Python, C++, and IDL.

The API uses a very simple *state*
model to navigate through a NeXus file.
(Compare this example with :ref:`example.napi.simple.2d.write`,
in the :ref:`NAPI <NAPI>` chapter, using the native HDF5 commands.)
When you open a file,
the API provides a file *handle*, which stores the
current location, i.e. which group and/or field is currently open. 
Read and write operations then act on the currently open entity.
Following the simple example titled
:ref:`Example structure of a simple data file <fig.simple-example>`,
we walk through a schematic of NeXus program written in C
(without any error checking or real data).

.. compound::
	
	.. _fig.ex-c-write:

    .. rubric:: Writing a simple NeXus file using NAPI

    .. literalinclude:: examples/ex-c-write.c
        :tab-width: 4
        :linenos:
        :language: c

.. compound::

    .. _ex.write.c:

    .. rubric:: program analysis

    #. line 6:
        .. _ex.write.open:

        Open the file ``NXfile.nxs`` with *create*
        access (implying write access). NAPI [#]_
        returns a file identifier of type ``NXhandle``.
    #. line 7:
        .. _ex.write.entry.group:

        Next, we create the :ref:`NXentry`
        group to contain the scan using
        ``NXmakegroup()`` and then
        open it for access using ``NXopengroup()``. [#]_
    #. line 9:
        The :index:`plottable data <NeXus basic motivation; default plot>`
        is contained within an :ref:`NXdata`
        group, which must also be created and opened.
    #. line 12:
        To create a field, call ``NXmakedata()``, specifying the
        data name, type (``NX_FLOAT32``), :index:`rank <rank>`
        (in this case, ``1``), and length of the array
        (``n``).  Then, it can be opened for writing. [#]_
    #. line 14:
        Write the data using ``NXputdata()``.
    #. line 15:
        With the field still open, we can also add some data 
        :index:`attributes <attributes; data>`,
        such as the :index:`data units <units>`, [#]_ [#]_
        which are specified as a character string (``type="NX_CHAR"`` [#]_)
        that is 7 bytes long.
    #. line 16:
        Then we close the field before opening another.
        In fact, the API will do this automatically if you
        attempt to open another field, but it is
        better style to close it yourself.
    #. line 17:
        The remaining fields in this group are added in a similar
        fashion. Note that the indentation whenever a new field or
        group are opened is just intended to make the structure of
        the NeXus file more transparent.
    #. line 20:
        Finally, close the groups (``NXdata`` and
        ``NXentry``) before closing the file itself.

.. _Introduction-HowToRead:

How do I read a NeXus file?
===========================

.. index:: file; read

Reading a NeXus file works in the same way by traversing the tree with the handle.

This schematic C code will read the two-theta array
created in the :ref:`example above <fig.ex-c-write>`.
(Again, compare this example with :ref:`code_native.reading`.)

.. compound::
	
	.. _fig.ex-c-read:

    .. rubric:: Reading a simple NeXus file using NAPI

    .. literalinclude:: examples/ex-c-read.c
        :tab-width: 4
        :linenos:
        :language: guess

.. _Introduction-HowToBrowse:

How do I browse a NeXus file?
=============================

.. index:: file; browse

NeXus files can also be viewed by a command-line browser,
``nxbrowse``, which is included as a helper tool in the
:ref:`NeXus API <Introduction-NAPI>`
distribution. The :ref:`following <fig.nxbrowse>` 
is an example session of :index:`using <utility; nxbrowse>` 
``nxbrowse`` to view a data file.

.. compound::
	
	.. _fig.nxbrowse:

    .. rubric:: Using ``nxbrowse``

    .. literalinclude:: examples/ex-unix-using-nxbrowse.txt
        :tab-width: 4
        :linenos:
        :language: guess

    .. _fig.using.nxbrowse:

    .. rubric:: program analysis

    #. line 1:
        Start ``nxbrowse`` from the UNIX command
        line and open file ``lrcs3701.nxs`` from
        IPNS/LRMECS.
    #. line 8:
		List the contents of the current group.
    #. line 11:
        Open the NeXus group ``Histogram1``.
    #. line 23:
        Print the contents of the NeXus data labeled ``title``.
    #. line 41:
        Close the current group.
    #. line 43:
        Quits ``nxbrowse``.

The source code of ``nxbrowse`` [#]_
provides an example of how to write a NeXus reader.
The test programs included in the :ref:`NeXus
API <Introduction-NAPI>` may also be useful to study.


.. [#] http://download.nexusformat.org

.. [#] :ref:`NAPI`

.. [#]
    See the chapter 
    :ref:`base.class.definitions`
    for more information.

.. [#]
    The :ref:`Design-DataTypes`
    section describes the available
    data types, such as ``NX_FLOAT32``
    and ``NX_CHAR``.

.. [#] :ref:`Design-Units`

.. [#]
    The NeXus rule about data units is described in the
    :ref:`Design-Units` section.

.. [#] see :ref:`nxdl-types`

.. [#] https://svn.nexusformat.org/code/trunk/applications/NXbrowse/NXbrowse.c
