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

NeXus validation tool written in C (not via NAPI).
   
Its dependencies are libxml2 and the HDF5 libraries, version 1.8.9 or
better. Its purpose is to validate HDF5 files against NeXus
application definitions. 

See the program documentation for more details:
https://github.com/nexusformat/cnxvalidate.git



.. _punx:

punx
####

Python Utilities for NeXus HDF5 files

**punx** can validate both NXDL files and NeXus HDF5 data files, as
well as print the structure of any HDF5 file, even non-NeXus files.
   
NOTE: project is under initial construction, not yet released for
public use, but is useful in its present form (version 0.2.5).

**punx** can show the tree structure of any HDF5 file. The output is
more concise than that from *h5dump*.
   
See the program documentation for more details:
https://punx.readthedocs.io
