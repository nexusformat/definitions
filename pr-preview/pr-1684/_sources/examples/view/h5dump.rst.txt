.. _examples.view.h5dump:

View a NeXus HDF5 file with *h5dump*
####################################

The ``h5dump`` tool [#]_ provided as part of the HDF5 tool kit [#]_ can be used
to print the content of an HDF5 file. As an example we show the result
of the command ``h5dump simple3D.h5`` on the result of :ref:`example.napi.python`

.. [#] **h5dump** : https://support.hdfgroup.org/HDF5/doc/RM/Tools.html#Tools-Dump
.. [#] **HDF5 tools** : https://support.hdfgroup.org/products/hdf5_tools/

.. literalinclude:: ../simple3D.h5dump.txt
    :tab-width: 4
    :linenos:
    :language: text
