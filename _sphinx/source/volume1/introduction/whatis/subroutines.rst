.. $Id$

.. _Introduction-SetOfSubroutines:

A Set of Subroutines
---------------------------------------------------------------------

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

.. _ex.simple.c:

Simple example of reading data using the NeXus API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: example; simple
.. code-block:: c
	:linenos: 

	NXopendata (fileID, "wavelength");
	NXgetdata (fileID, lambda);
	NXclosedata (fileID);

In this example, the program requests the value of the data that has
the label ``wavelength``, storing the result in the variable lambda.
``fileID`` is a file identifier that is provided by NeXus when the
file is opened. 

We shall provide a more complete example when we have 
discussed the contents of the NeXus files.

.. introduction: low-level routines was dropped form the manual in 2011
.. .. include:: intro-lowlevel.inc
