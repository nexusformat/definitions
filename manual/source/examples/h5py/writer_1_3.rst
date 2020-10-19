.. _Example-writer_1_3:

``h5py`` example writing the simplest NeXus data file
#####################################################

In this example, the 1-D scan data will be written into the simplest
possible NeXus HDF5 data file, containing only the required NeXus components.
NeXus requires at least one :ref:`NXentry` group at the root level of
an HDF5 file.  The ``NXentry`` group contains *all the data and associated
information that comprise a single measurement.*
``NXdata`` is used to describe the
plottable data in the ``NXentry`` group.  The simplest place to store
data in a NeXus file is directly in the ``NXdata`` group,
as shown in the next figure.

.. compound::

    .. _fig.simple-example-h5py:

    .. figure:: ../../img/ex_writer_1_3.png
        :alt: fig.simple-example-h5py
        :width: 50%

        Simple Example

In the :ref:`above figure <fig.simple-example-h5py>`, 
the data file (``writer_1_3_h5py.hdf5``) contains
a hierarchy of items, starting with an ``NXentry`` named ``entry``.
(The full HDF5 path reference, ``/entry`` in this case, is shown to the right of each
component in the data structure.)  The next ``h5py`` code
example will show how to build an HDF5 data file with this structure.
Starting with the numerical data described above,
the only information
written to the file is the *absolute* minimum information NeXus requires.
In this example, you can see how the HDF5 file is created, how
:ref:`Design-Groups` and datasets (:ref:`Design-Fields`)
are created, and how :ref:`Design-Attributes` are assigned.
Note particularly the ``NX_class`` attribute on each HDF5 group that
describes which of the NeXus :ref:`base.class.definitions` is being used.
When the next Python program (``writer_1_3_h5py.py``) is run from the
command line (and there are no problems), the ``writer_1_3_h5py.hdf5``
file is generated.

.. literalinclude:: writer_1_3.py
    :tab-width: 4
    :linenos:
    :language: python

One of the tools provided with the HDF5 support libraries is
the ``h5dump`` command, a command-line tool to print out the
contents of an HDF5 data file.  With no better tool in place (the
output is verbose), this is a good tool to investigate what has been
written to the HDF5 file.  View this output from the command line
using ``h5dump writer_1_3.hdf5``.  Compare the data contents with
the numbers shown above.  Note that the various HDF5 data types have all been
decided by the ``h5py`` support package.

.. note:: The only difference between this file and one written using the NAPI
          is that the NAPI file will have some additional, optional attributes set at the root
          level of the file that tells the original file name, time it was written, and some version information
          about the software involved.

.. leave this out
   .. literalinclude:: writer_1_3_h5dump.txt
       :tab-width: 4
       :linenos:
       :language: text

Since the output of ``h5dump`` is verbose (see the *Downloads* section below), 
the :ref:`punx tree <punx>` tool [#]_ was used to
print out the structure of HDF5 data files.  This tool provides a simplified view
of the NeXus file.  Here is the output:

.. literalinclude:: writer_1_3_structure.txt
    :tab-width: 4
    :linenos:
    :language: text

As the data files in these examples become more complex, you will appreciate
the information density provided by *punx tree*.

.. [#] *punx tree* : https://punx.readthedocs.io/en/latest/source_code/h5tree.html#how-to-use-h5tree

downloads
*********

The Python code and files related to this section may be downloaded from the following table.

=====================================  =============================================
file                                   description
=====================================  =============================================
:download:`writer_1_3.py`              python code to write example *writer_1_3*
:download:`writer_1_3.hdf5`            NeXus file written by this code
:download:`writer_1_3_h5dump.txt`      *h5dump* analysis of the NeXus file
:download:`writer_1_3_structure.txt`   *punx tree* analysis of the NeXus file
=====================================  =============================================
