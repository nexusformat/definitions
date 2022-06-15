.. _examples.view.h5dump:

View a NeXus HDF5 file using *h5dump*
#####################################

For the purposes of an example, it is instructive to view the content of the
NeXus HDF5 file produced by the above program.  Since HDF5 is a binary file
format, we cannot show the contents of the file directly in this manual.
Instead, we first we view the content by showing the output from
the ``h5dump`` tool provided as part of the HDF5 tool kit:
``h5dump simple3D.h5``

.. literalinclude:: ../simple3D.h5dump.txt
    :tab-width: 4
    :linenos:
    :language: text
