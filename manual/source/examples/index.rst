.. _Examples:

================================================
Examples of writing and reading NeXus data files
================================================
..
	.. image:: ../img/NeXus.png

Simple examples of reading and writing NeXus data files
are provided in the :ref:`Introduction` chapter and also
in the :ref:`NAPI` chapter.  Here, three examples are provided
showing how to write a NeXus data file without using the NAPI.

.. _Examples.NAPI:

Code Examples that use the NAPI
###############################

Various examples are given that show how to read and write NeXus data files using the
:ref:`NAPI`.

.. toctree::
	:maxdepth: 1
	
	code_napi

.. _Examples.nonNAPI:

Code Examples that do not use the NAPI
######################################

Sometimes, for whatever reason, it is necessary to write or read
NeXus files without using the routines provided by the :ref:`NAPI`.
Each example in this section is written to support just one of the low-level file formats
supported by NeXus (HDF4, HDF5, or XML).

.. toctree::
	:maxdepth: 1

	code_native
	h5py/index
	lrmecs/index
