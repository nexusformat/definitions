.. _Examples:

================================================
Examples of writing and reading NeXus data files
================================================
..
	.. image:: ../img/NeXus.png

Simple examples of reading and writing NeXus data files
are provided in the :ref:`Introduction` chapter and also
in the :ref:`NAPI` chapter.

.. _Examples.code:

Code Examples in Various Languages
##################################

Each example in this section demonstrates writing and reading NeXus compliant files
in various languages with different libraries. Currently all examples are using the
HDF5 file format. Other container formats like the legacy format HDF4 or XML can also
be used to store NeXus compliant data.

Please be aware that not all examples are up to date with the latest format recommendations.

.. toctree::
   :maxdepth: 1

   code_native
   h5py/index
   nexusformat/index
   matlab/index
   napi/c
   napi/fortran
   napi/python

.. _Examples.view:

Visualization tools
###################

Tools to print or visualize NeXus HDF5 files

.. toctree::

   view/h5dump
   view/punx

.. _Examples.instruments:

Examples for Specific Instruments
#################################

.. toctree::
   :maxdepth: 1

   lrmecs/index
   epics

.. _Examples.tools:

Code Projects that work with NeXus data files
#############################################

The number of tools that read NeXus data files,
either for general use or to read a specific
application definition, is growing.  Many of these
are open source and so also serve as code examples. In the section
:ref:`Utilities`, we describe many applications
and software packages that can read, write, browse,
and use NeXus data files. Examples of code (mostly 
from the NeXus community) that 
read NeXus data are listed in section :ref:`language.apis`.

The NIAC welcomes your continued contributions to 
this documentation.
