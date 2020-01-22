.. index:: NAPI; examples

.. _NAPI-Examples:

=================================
Example NeXus programs using NAPI
=================================

.. _example.napi.simple.2d.write:

NAPI Simple 2-D Write Example (C, F77, F90)
###########################################

Code examples are provided in this section that write 2-D data
to a NeXus HDF5 file in C, F77, and F90 languages using the NAPI.

The following code reads a two-dimensional set ``counts``
with dimension scales of ``t`` and ``phi`` using
local routines, and then writes a NeXus file containing a single
``NXentry`` group and a single ``NXdata`` group.
This is the simplest data file that conforms to the NeXus standard.
The same code is provided in C, F77, and F90 versions.
Compare these code examples with :ref:`native-HDF5-Examples`.

NAPI C Example: write simple NeXus file
+++++++++++++++++++++++++++++++++++++++

.. note:: This example uses the signal/axes attributes applied to the
   data field, as described in :ref:`Design-FindPlottable-ByName`.
   New code should use the method described in :ref:`Design-FindPlottable-NIAC2014`.

.. literalinclude:: napi-example.c
    :tab-width: 4
    :linenos:
    :language: c

NAPI F77 Example: write simple NeXus file
+++++++++++++++++++++++++++++++++++++++++

.. note:: The F77 interface is no longer being developed.

.. literalinclude:: napi-example.f77
    :tab-width: 4
    :linenos:
    :language: fortran

NAPI F90 Example: write simple NeXus file
+++++++++++++++++++++++++++++++++++++++++

.. note:: This example uses the signal/axes attributes applied to the
   data field, as described in :ref:`Design-FindPlottable-ByName`.
   New code should use the method described in :ref:`Design-FindPlottable-NIAC2014`.

.. literalinclude:: napi-example.f90
    :tab-width: 4
    :linenos:
    :language: fortran


.. _example.napi.simple.3d.write.python:

NAPI Python Simple 3-D Write Example
####################################

A single code example is provided in this section that writes 3-D data
to a NeXus HDF5 file in the Python language using the NAPI.

The data to be written to the file is a simple three-dimensional array (2 x 3 x 4)
of integers.  The single dataset is intended to demonstrate the order in
which each value of the array is stored in a NeXus HDF5 data file.

NAPI Python Example: write simple NeXus file
++++++++++++++++++++++++++++++++++++++++++++

.. literalinclude:: simple3D.py
    :tab-width: 4
    :linenos:
    :language: python

View a NeXus HDF5 file using *h5dump*
#####################################

For the purposes of an example, it is instructive to view the content of the
NeXus HDF5 file produced by the above program.  Since HDF5 is a binary file
format, we cannot show the contents of the file directly in this manual.
Instead, we first we view the content by showing the output from
the ``h5dump`` tool provided as part of the HDF5 tool kit:
``h5dump simple3D.h5``

NAPI Python Example: ``h5dump`` output of NeXus HDF5 file
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. literalinclude:: simple3D.h5dump.txt
    :tab-width: 4
    :linenos:
    :language: text


View a NeXus HDF5 file using *punx tree*
########################################

The output of ``h5dump`` contains a lot of structural information
about the HDF5 file that can distract us from the actual content we added to the file.
Next, we show the output from a custom Python tool (``punx tree``) built for
NeXus data file validation and view. [#]_
The *tree* option of this tool [#]_ was developed to show the actual data content of an
HDF5 file that we create.

.. [#] **punx** : https://punx.readthedocs.io/
.. [#] **punx tree** : https://punx.readthedocs.io/en/latest/source_code/h5tree.html#how-to-use-h5tree

NAPI Python Example: ``punx tree simple3D.h5`` output of NeXus HDF5 file
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. literalinclude:: simple3D.xture.txt
    :tab-width: 4
    :linenos:
    :language: text
    
