.. $Id$

.. _Examples:

================================================
Examples of writing and reading NeXus data files
================================================

.. image:: img/NeXus.png

Simple examples of reading and writing NeXus data files
are provided in the :ref:`Introduction` chapter of Volume I and also
in the :ref:`NAPI` chapter of Volume II.  Here, three examples are provided
showing how to write a NeXus data file without using the NAPI.

.. _Examples.NAPI:

Code Examples that use the NAPI
###############################

Various examples are given that show how to read and write NeXus data files using the
:ref:`NAPI`.

.. include:: ex_code_napi.rst

.. _Examples.nonNAPI:

Code Examples that do not use the NAPI
######################################

Sometimes, for whatever reason, it is necessary to write or read
NeXus files without using the routines provided by the :ref:`NAPI`.
Each example in this section is written to support just one of the low-level file formats
supported by NeXus (HDF4, HDF5, or XML).

.. include:: ex_code_native.rst

.. include:: h5py-example.rst

.. include:: lrmecs-example.rst
