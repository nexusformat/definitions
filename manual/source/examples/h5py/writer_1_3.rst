.. _Example-writer_1_3:

=====================================================
``h5py`` example writing the simplest NeXus data file
=====================================================

In this example, the 1-D scan data will be written into the simplest
possible NeXus HDF5 data file, containing only the required NeXus components.
NeXus requires at least one :ref:`NXentry` group at the root level of
an HDF5 file.  The ``NXentry`` group contains *all the data and associated
information that comprise a single measurement.*
NeXus also requires that each ``NXentry`` group must contain at least
one :ref:`NXdata` group.  ``NXdata`` is used to describe the
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

.. literalinclude:: writer_1_3_h5py.py
    :tab-width: 4
    :linenos:
    :language: python

We wish to make things a bit simpler for ourselves when creating the common
structures we use in our data files.  To help, we gather together some of the
common concepts such as *create a file*,
*create a NeXus group*,
*create a dataset* and start to build a helper library.
(See :ref:`h5py-example-my_lib` for more details.)
Here, we call it ``my_lib``.  Applying it to the simple example above, our
code only becomes a couple lines shorter!  (Let's hope the library starts to help in larger or
more complicated projects.)  Here's the revision that replaces direct calls to ``numpy``
and ``h5py`` with calls to our library.  It generates the file
``writer_1_3.hdf5``.

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

.. literalinclude:: writer_1_3_h5dump.txt
    :tab-width: 4
    :linenos:
    :language: guess

Since the output of ``h5dump`` is verbose, a tool
(see :ref:`h5py-example-h5toText`)
was created to
print out the structure of HDF5 data files.  This tool provides a simplified view
of the NeXus file.  It is run with a command like this:
``python h5toText.py h5dump writer_1_3.hdf5``.  Here is the output:

.. literalinclude:: writer_1_3_structure.txt
    :tab-width: 4
    :linenos:
    :language: guess

As the data files in these examples become more complex, you will appreciate
the information density provided by the ``h5toText.py`` tool.
