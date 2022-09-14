.. _example.napi.c:

HDF5 in C with NAPI
###################

Code examples are provided in this section that write 2-D data
to a NeXus HDF5 file in the C language using the :ref:`NAPI`.

The following code reads a two-dimensional set ``counts``
with dimension scales of ``t`` and ``phi`` using
local routines, and then writes a NeXus file containing a single
``NXentry`` group and a single ``NXdata`` group.
This is the simplest data file that conforms to the NeXus standard.

NAPI C Example: write simple NeXus file
+++++++++++++++++++++++++++++++++++++++

.. note:: This example uses the signal/axes attributes applied to the
   data field, as described in :ref:`Design-FindPlottable-ByName`.
   New code should use the method described in :ref:`Design-FindPlottable-NIAC2014`.

.. literalinclude:: napi-example.c
    :tab-width: 4
    :linenos:
    :language: c
