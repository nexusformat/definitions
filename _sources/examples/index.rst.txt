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

.. _Examples.nonNAPI:

Code Examples in Various Languages
##################################

Each example in this section demonstrates either reading NeXus files in
one of the supported storage containers (HDF5 or one of the legacy container formats: HDF4 or XML)
or writing compliant NeXus files in the HDF5 storage containers.
Please be aware that not all exmples are up to date with the latest format recommendations.

.. toctree::
   :maxdepth: 1
   
   code_native
   h5py/index
   matlab/index
   lrmecs/index
   epics/index

.. _Examples.NAPI:

Code Examples that use the NeXus API (NAPI)
###########################################

These examples illustrate the use of the NAPI
:ref:`NAPI`. Please refer to the linked section in the manual for the status of NAPI.

.. toctree::
	:maxdepth: 1
	
	code_napi

