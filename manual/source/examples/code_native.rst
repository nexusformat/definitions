.. index:: HDF5; examples

.. _native-HDF5-Examples:

===================================================
Example NeXus C programs using native HDF5 commands
===================================================

C-language code examples are provided for
writing and reading NeXus-compliant files
using the native HDF5 interfaces.  These examples are derived from the simple
NAPI examples for :ref:`writing <fig.ex-c-write>`
and :ref:`reading <fig.ex-c-read>` given in the
:ref:`Introduction <Introduction>` chapter.
Compare these code examples with :ref:`NAPI-Examples`.

.. _code_native.writing:

Writing a simple NeXus file using native HDF5 commands in C
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note:: This example uses the new method described
   in :ref:`Design-FindPlottable-NIAC2014` for indicating plottable data.

.. literalinclude:: nxh5write.c
    :tab-width: 4
    :linenos:
    :language: c

.. _code_native.reading:

Reading a simple NeXus file using native HDF5 commands in C
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. literalinclude:: nxh5read.c
    :tab-width: 4
    :linenos:
    :language: c
    