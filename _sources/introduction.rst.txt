.. _Introduction:

==================
NeXus Introduction
==================

.. index::
   introduction
   motivation

NeXus [#]_ is an effort by an international group of scientists 
:ref:`motivated <MotivationsForNeXus>`
to define a common data exchange format for neutron, X-ray, and muon experiments.  
NeXus is built on top of the scientific data format HDF5 and adds 
domain-specific rules for organizing data within HDF5 files in addition 
to a dictionary of well-defined domain-specific field names. The NeXus 
data format has three purposes:

#. *raw data*:
   NeXus defines a format that can 
   serve as a container for all relevant data associated with a scientific 
   instrument or beamline. This is a very important use case. This includes 
   the case of streaming data acquisition, where time stamped data are logged. 
#. *processed data*:
   NeXus also defines standards for processed data. This is data which has underwent some form of data 
   reduction or data analysis. NeXus allows storing the results of such processing together with 
   documentation about how the processed data was generated. 
#. *standards*:
   NeXus defines standards in 
   the form of *application definitions* for the exchange of data 
   between applications. NeXus provides standards for both raw and processed data.

A community of scientists and computer programmers working in neutron
and synchrotron facilities around the world came to the conclusion that a 
common data format would fulfill a valuable function in the scattering community. As
instrumentation becomes more complex and data visualization becomes more challenging,
individual scientists, or even institutions, find it difficult to keep up with new
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

.. [#] *J. Appl. Cryst.* (2015). **48**, 301-305
   (https://doi.org/10.1107/S1600576714027575)

..  =======================
    section: What is NeXus?
    =======================

.. _WhatIsNeXus:

What is NeXus?
##############

The NeXus data format has four components:

:ref:`A set of design principles <Introduction-DesignPrinciples>`
    to help people understand what is in the data files.

:ref:`A set of data storage objects <Introduction-DataStorageObjects>`
    (:ref:`base.class.definitions`
    and :ref:`application.definitions`)
    to allow the development of portable analysis software.

:ref:`A set of subroutines <Introduction-SetOfSubroutines>`
    (:ref:`Utilities <Utilities>` 
    and :ref:`examples <Examples>`) 
    to make it easy to read and write NeXus data files.

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

.. index:: design principles

NeXus data files contain four types of entity:
groups,
fields,
attributes, and
links.

.. index::
   single: group

:ref:`Design-Groups`
    Groups are like folders that can contain a number of fields
    and/or other groups.

    .. index::
      single: field

:ref:`Design-Fields`
    Fields can be scalar values or multidimensional arrays of a
    variety of sizes (1-byte, 2-byte, 4-byte, 8-byte) and types
    (characters, integers, floats).  Fields are
    represented as HDF5 *datasets*.
    
.. index::
   single: field attribute
   single: group attribute

:ref:`Design-Attributes`
    Extra information required to
    describe a particular group or field,
    such as the data units,
    can be stored as a data attribute.  Attributes can also 
    be given at the file level of an HDF5 file.

.. index::
   link
   plotting
   NXdata (base class); plotting
   NXmonitor (base class); plotting
   NXdetector (base class); plotting
   
:ref:`Design-Links`
    Links are used to reference the plottable data from ``NXdata``
    when the data is provided in other groups
    such as ``NXmonitor`` or ``NXdetector``.

In fact, a NeXus file can be viewed as a computer file system. Just as files
are stored in folders (or subdirectories) to make them easy to locate, so NeXus
fields are stored in groups. The group :index:`hierarchy <hierarchy>`
is designed to make it easy
to navigate a NeXus file.

.. _Introduction-ExampleFile:

Example of a NeXus File
-----------------------

.. index::
   see: tree structure; hierarchy
   single: examples; NeXus file

The following diagram shows an example of a NeXus data file represented as a
tree structure.

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
complete list can be found in the :ref:`Design-NeXusClasses` chapter.
A complete list of *all* NeXus classes may be found in
the :ref:`all.class.definitions` chapter.


.. note:: ``NXentry``
          is the only class required in a valid NeXus data file.

.. index:: NXentry (base class)

:ref:`NXentry`
    *Required:*
    The top level of any NeXus file contains one or more groups with the 
    class ``NXentry``. 
    These contain all the data that is required to
    describe an experimental run or scan. Each
    ``NXentry`` typically contains a number of
    groups describing sample information (class
    ``NXsample``), instrument details (class
    ``NXinstrument``), and monitor counts (class
    ``NXmonitor``).

.. index:: NXdata (base class)

:ref:`NXdata`
    Each ``NXentry`` group may contain one or more ``NXdata`` groups.
    These groups contain the experimental results
    in a self-contained way, i.e., it should be possible to
    generate a sensible :index:`plot <plotting>`
    of the data from the information
    contained in each ``NXdata`` group. That means it
    should contain the axis labels and titles as well as the
    data.

.. index:: NXsample (base class)

:ref:`NXsample`
    A ``NXentry`` group will often contain a group with 
    class ``NXsample``. 
    This group contains information pertaining to
    the sample, such as its chemical composition, mass, and
    environment variables (temperature, pressure, magnetic
    field, etc.).

.. index:: NXinstrument (base class)

:ref:`NXinstrument`
   There might also be a group with 
   class ``NXinstrument``. This is designed to encapsulate all the
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

.. index::
   single: examples; NeXus file; minimal

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
sets. Here is the structure of a very simple NeXus data file
(:download:`examples/verysimple.nx5`):

.. compound::

	.. _fig.verysimple-structure:

   .. rubric:: Structure of a very simple NeXus Data file

   .. literalinclude:: examples/verysimple.txt
      :tab-width: 4
      :linenos:
      :language: text

.. index:: 
   NeXpy

NeXus files are easy to visualize.  Here, this data is plotted using *NeXPy* simply
by opening the NeXus data file and double-clicking the file name in the list:

.. compound::

   .. _fig.verysimple-png:
   
   .. rubric:: Plot of a very simple NeXus HDF5 Data file
   
   .. image:: img/verysimple.png
      :width: 60%

NeXus files are easy to create.  This example NeXus file was created using
a short Python program and the *h5py* package:

.. compound::

   .. _fig.verysimple-py:
   
   .. rubric:: Using Python to write a very simple NeXus HDF5 Data file
   
   .. literalinclude:: examples/verysimple.py
      :tab-width: 4
      :linenos:
      :language: python

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

These instrument definitions are formalized as XML files, using 
:ref:`NXDL <NXDL>`,
to specify the names of fields, and other NeXus data objects.
The following is an example of such a file for
the simple NeXus file shown above.

.. compound::
	
   .. _fig.verysimple.nxdl.xml:
   
   .. rubric:: A very simple NeXus Definition Language (NXDL) file
   
   .. literalinclude:: examples/verysimple.nxdl.xml
      :tab-width: 4
      :linenos:
      :language: xml

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
      :language: c

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
community to exchange ideas in data storage.

The NeXus International Advisory Committee (:index:`NIAC`) supervises the
development and maintenance of the NeXus common data
format for neutron, X-ray, and muon science
through the
NeXus class definitions and oversees the maintenance of the
NeXus Application Programmer Interface (NAPI) as well as the technical infrastructure.


.. toctree::
   :maxdepth: 2
   :glob:
   
   preface
   motivations
   introduction-napi
