.. index::
	! single: NAPI
	see: NeXus Application Programming Interface; NAPI

.. _NAPI:

=====================================================
NAPI: NeXus Application Programmer Interface (frozen)
=====================================================

Status
======

This application program interface (API) was developed to support the 
reading and writing of NeXus files through unified function calls,
regardless of the physical data format (XML, HDF4, HDF5).

In the meantime it has been decided that active development of NeXus
definitions and tools will concentrate on HDF5
as the only supported physical data format.
It is expected that most application developers will use
standard HDF5 tools to read and write NeXus.
Two examples are provided in :ref:`native-HDF5-Examples`.

Therefore, the decision has been taken to freeze the NAPI.
Maintenance is reduced to bug fixes.

Overview
========

The core routines have been written in C but wrappers are available for a 
number of other languages including C++, Fortran 77, Fortran 90, Java, 
Python and IDL. The API makes the reading and writing of NeXus files 
transparent; the user doesn't even need to know the underlying format when 
reading a file since the API calls are the same. 

The NeXus Application 
Programming Interface for the various language backends is available on-line 
from https://github.com/nexusformat/code/

The  NeXusIntern.pdf document 
(https://github.com/nexusformat/code/blob/master/doc/api/NeXusIntern.pdf) describes the 
internal workings of the NeXus-API. You are very welcome to read it, but it 
will not be of much use if all you want is to read and write files using the NAPI. 


The NeXus Application Program Interface 
call routines in the appropriate backend (HDF4, HDF5 or XML) to read and write files
with the correct structure. The API serves a number of purposes:

#. It simplifies the reading and writing of NeXus files.
#. It ensures a certain degree of compliance with the NeXus standard.
#. It hides the implementation details of the format. 
   In particular, the API can read and write HDF4, HDF5, 
   and XML files using the same routines.

	
.. index:: NAPI; core

.. _NAPI-Core:

Core API
========

The core API provides the basic routines for reading, writing 
and navigating NeXus files. Operations are performed using a handle
that keeps a record of its current position in the file hierarchy.
All are read or write requests are then
implicitly performed on the currently *open* entity. This limits
number of parameters that need to be passed to API calls, at the 
cost of forcing a certain mode of operation.
It is very similar 
to navigating a directory hierarchy; NeXus 
groups are the directories, which can contain data sets 
and/or other directories.

The core API comprises the following functional groups:

* General initialization and shutdown: 
  opening and closing the file, 
  creating or opening an existing group or dataset, 
  and closing them.
* Reading and writing data and attributes to previously 
  opened datasets.
* Routines to obtain meta-data and to iterate over component 
  datasets and attributes.
* Handling of linking and group hierarchy.
* Routines to handle memory allocation. (Not required in all language bindings.)


.. toctree::
	:maxdepth: 2
	:glob:
   
	napi-c
	napi-f77
	napi-f90
	napi-java
	napi-idl




.. _NAPI-Utility:

Utility API
===========

The NeXus F90 Utility API provides a number of routines that combine the 
operations of various core API routines in order to simplify the reading 
and writing of NeXus files. At present, they are only available as a 
Fortran 90 module but a C version is in preparation.

The utility API comprises the following functional groups:

* Routines to read or write data.
* Routines to find whether or not groups, data, or attributes exist, and to 
  find data with specific signal or axis attributes, i.e. to identify valid data or axes.
* Routines to open other groups to which ``NXdata`` items are linked, and to return again.

.. rubric:: line required for use with F90 API

Any program using the F90 Utility API needs to put 
the following line near the top of the program::

	use NXUmodule

.. note:: Do not put ``USE`` statements for both 
	``NXmodule`` and ``NXUmodule``.  
	The former is included in the latter


.. _NAPI-UtilityRoutines:

List of F90 Utility Routines
----------------------------

+---------------------------+---------------------------------------------------+
|  name                     | description                                       |
+===========================+===================================================+
| Reading and Writing                                                           |
+---------------------------+---------------------------------------------------+
| ``NXUwriteglobals``       | Writes all the valid global attributes of a file. |
+---------------------------+---------------------------------------------------+
| ``NXUwritegroup``         | Opens a group (creating it if necessary).         |
+---------------------------+---------------------------------------------------+
| ``NXUwritedata``          | Opens a data item (creating it if necessary)      |
|                           | and writes data and its units.                    |
+---------------------------+---------------------------------------------------+
| ``NXUreaddata``           | Opens and reads a data item and its units.        |
+---------------------------+---------------------------------------------------+
| ``NXUwritehistogram``     | Opens one dimensional data item                   |
|                           | (creating it if necessary)                        |
|                           | and writes histogram centers and their units.     |
+---------------------------+---------------------------------------------------+
| ``NXUreadhistogram``      | Opens and reads a one dimensional data item and   |
|                           | converts it to histogram bin boundaries.          |
+---------------------------+---------------------------------------------------+
| ``NXUsetcompress``        | Defines the compression algorithm and minimum     |
|                           | dataset size for subsequent write operations.     |
+---------------------------+---------------------------------------------------+
| Finding Groups, Data, and Attributes                                          |
+---------------------------+---------------------------------------------------+
| ``NXUfindclass``          | Returns the name of a group of the specified      |
|                           | class if it is contained within the currently     |
|                           | open group.                                       |
+---------------------------+---------------------------------------------------+
| ``NXUfinddata``           | Checks whether a data item of the specified name  |
|                           | is contained within the currently open group.     |
+---------------------------+---------------------------------------------------+
| ``NXUfindattr``           | Checks whether the currently open data item has   |
|                           | the specified attribute.                          |
+---------------------------+---------------------------------------------------+
| ``NXUfindsignal``         | Searches the currently open group for a data item |
|                           | with the specified ``SIGNAL`` attribute.          |
+---------------------------+---------------------------------------------------+
| ``NXUfindaxis``           | Searches the currently open group for a data item |
|                           | with the specified ``AXIS`` attribute.            |
+---------------------------+---------------------------------------------------+
| Finding Linked Groups                                                         |
+---------------------------+---------------------------------------------------+
| ``NXUfindlink``           | Finds another link to the specified NeXus data    |
|                           | item and opens the group it is in.                |
+---------------------------+---------------------------------------------------+
| ``NXUresumelink``         | Reopens the original group from which             |
|                           | ``NXUfindlink`` was used.                         |
+---------------------------+---------------------------------------------------+


Currently, the F90 utility API will only write character strings, 
4-byte integers and reals, and 8-byte reals. It can read other 
integer sizes into four-byte integers, but does not differentiate 
between signed and unsigned integers. 



.. _NAPI-Building:

Building Programs
=================

The install kit provides a utility call ``nxbuild``
that can be used to build simple programs::

	nxbuild -o test test.c

This script links in the various libraries for you and reading its 
contents would provide the necessary information for creating a 
separate Makefile. You can also use ``nxbuild`` with the 
example files in the NeXus distribution kit which are installed into 
``/usr/local/nexus/examples``

Note that the executable name is important in this case as the test 
program uses it internally to determine the ``NXACC_CREATE*`` 
argument to pass to ``NXopen``.

.. rubric:: building and running a simple NeXus program

::

	#  builds HDF5 specific test
	nxbuild -o napi_test-hdf5 napi_test.c
	
	# runs the test
	./napi_test-hdf5

NeXus is also set up for pkg-config so the build can be done as::

	gcc `pkg-config --cflags` `pkg-config --libs` -o test test.c




.. _NAPI-Reporting:

Reporting Bugs in the NeXus API
===============================

If you encounter any bugs in the installation or running of the NeXus API, 
please report them online using our Issue Reporting system. 
(https://www.nexusformat.org/IssueReporting.html)
