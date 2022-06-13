.. _h5py-example-plotting:

Read and plot a NeXus HDF5 file
###############################

.. _finding.default.data.python:

Finding the default plottable data
==================================

Let's make a new reader that follows the chain of
attributes (``@default``, ``@signal``, and ``@axes``)
to find the default plottable data.  We'll use the
same data file as the previous example.
Our demo here assumes one-dimensional data.  
(For higher dimensionality data,
we'll need more complexity when handling the 
``@axes`` attribute and we'll to check the
field sizes. See section :ref:`Find-Plottable-Data`, 
subsection :ref:`Find-Plottable-Data-v3`, for the details.)

.. compound::

    .. rubric:: *reader_attributes_trail.py*: Read a NeXus HDF5 file using Python with h5py
    
    .. _Example-H5py-Reader_attributes_trail:

    .. literalinclude:: reader_attributes_trail.py
	    :tab-width: 4
	    :linenos:
	    :language: python

Output from ``reader_attributes_trail.py`` is shown next.

.. compound::

    .. rubric:: Output from ``reader_attributes_trail.py``

    .. literalinclude:: reader_attributes_trail.txt
	    :tab-width: 4
	    :linenos:
	    :language: text

.. _Example-H5py-Plotting:

Plotting the HDF5 file
======================

Now that we are certain our file conforms to the NeXus
standard, let's plot it using the ``NeXpy`` [#]_
client tool.  To help label the plot, we added the
``long_name`` attributes to each of our datasets.
We also added metadata to the root level of our HDF5 file
similar to that written by the NAPI.  It seemed to be a useful addition.
Compare this with :ref:`Example-H5py-Plot`
and note that the horizontal axis of this plot is mirrored from that above.
This is because the data is stored in the file in descending
``mr`` order and ``NeXpy`` has plotted
it that way (in order of appearance) by default.

.. [#] *NeXpy*:    http://nexpy.github.io/nexpy/

.. compound::

    .. _fig-Example-H5py-nexpy-plot:

    .. figure:: nexpy.png
        :alt: fig-Example-H5py-nexpy-plot
        :width: 80%

        plot of our *mr_scan* using NeXpy

downloads
=========

The Python code and files related to this section may be downloaded from the following table.

===========================================  =============================================
file                                         description
===========================================  =============================================
:download:`reader_attributes_trail.py`       Read NeXus HDF5 file and find plotaable data
===========================================  =============================================