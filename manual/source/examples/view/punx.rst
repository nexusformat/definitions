.. _examples.view.punx:


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

.. literalinclude:: ../simple3D.xture.txt
    :tab-width: 4
    :linenos:
    :language: text
