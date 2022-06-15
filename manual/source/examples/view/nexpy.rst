.. _example-view-nexpy:

Plot a NeXus HDF5 file with *NeXpy*
###################################

A NeXus HDF5 file with plottable data (see :ref:`h5py-example-plotting`)
can be plotted by ``NeXpy`` [#]_. 

.. [#] *NeXpy*:    http://nexpy.github.io/nexpy/

.. compound::

    .. _fig-Example-nexpy-plot:

    .. figure:: nexpy.png
        :alt: fig-Example-nexpy-plot
        :width: 80%

        plot the simple example using NeXpy

Compare this with :ref:`simple-example-plot` and note that the horizontal axis
of this plot is mirrored from that above. This is because the data is stored
in the file in descending ``mr`` order and ``NeXpy`` has plotted
it that way (in order of appearance) by default.