.. _example.napi.python:

HDF5 in Python with NAPI
########################

A single code example is provided in this section that writes 3-D data
to a NeXus HDF5 file in the Python language using the :ref:`NAPI`.

The data to be written to the file is a simple three-dimensional array (2 x 3 x 4)
of integers.  The single dataset is intended to demonstrate the order in
which each value of the array is stored in a NeXus HDF5 data file.

NAPI Python Example: write simple NeXus file
++++++++++++++++++++++++++++++++++++++++++++

.. literalinclude:: ../simple3D.py
    :tab-width: 4
    :linenos:
    :language: python
