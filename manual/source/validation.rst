.. index::
	!validation
	!verification

.. _Verification:

====================================
Verification and validation of files
====================================

..  ++++++++++++++++++++++++++++

The intent of verification and validation of files is to ensure, in an unbiased way, that
a given file conforms to the relevant specifications.
Validation
does not check that the data content of the file is sensible; this requires scientific
interpretation based on the technique.

Validation is useful to anyone who manipulates or modifies the contents of NeXus files.
This includes scientists/users, instrument staff, software developers, and those who might
mine the files for  :index:`metadata`. 
First, the scientist or user of the data must be certain that the information
in a file can be located reliably. The instrument staff or software developer must be
confident the information they have written to the file has been located and formatted
properly. At some time, the content of the NeXus file may contribute to a larger body of
work such as a metadata catalog for a scientific instrument, 
a laboratory, or even an entire user facility.

.. index::
   nxvalidate


.. TODO

   Chapter should describe how data files are verified (validated) 
   for conformance to the NeXus standard. 
   
   Additional expectation for this chapter 
   is a description of how validation works.

.. _nxvalidate:

nxvalidate
##########

The :ref:`cnxvalidate <nxvalidate>` utility [#]_, 
new in 2016, is available for testing.
Refer to the GitHub location for the most recent information. 

This utility only works on HDF5 files and is aimed 
to be faster, simpler, more portable and robust than 
previous programmes for NeXus file validation.

.. [#] :ref:`cnxvalidate <nxvalidate>`: from https://github.com/nexusformat/cnxvalidate



.. _punx:

punx
####

Python Utilities for NeXus HDF5 files

**punx** can validate
both NXDL files and NeXus HDF5 data files, as well as print
the structure of any HDF5 file, even non-NeXus files.
 
NOTE: project is under initial construction, 
not yet released for public use, but is useful in its 
present form (version 0.0.9).  
 
See the program documentation for more details:
https://punx.readthedocs.io
