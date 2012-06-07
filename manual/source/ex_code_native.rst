.. $Id$

.. _native-HDF5-Examples:

.. index:: HDF5; examples

===================================================
Example NeXus C programs using native HDF5 commands
===================================================

C-language code examples are provided for
writing and reading NeXus-compliant files
using the native HDF5 interfaces.  These examples are derived from the simple
NAPI examples for :ref:`writing <ex.simple.write>`
and :ref:`reading <ex.simple.read>` given in the
:ref:`Introduction <Introduction>` chapter.
Compare these code examples with :ref:`NAPI-Examples`.

.. compound::

    .. rubric:: Writing a simple NeXus file using native HDF5 commands

    .. literalinclude:: examples/nxh5write.c
        :tab-width: 4
        :linenos:
        :language: guess

.. compound::

    .. rubric:: Reading a simple NeXus file using native HDF5 commands

    .. literalinclude:: examples/nxh5read.c
        :tab-width: 4
        :linenos:
        :language: guess
    