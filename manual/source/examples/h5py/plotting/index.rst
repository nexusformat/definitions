.. _h5py-example-plotting:

Find plottable data in a NeXus HDF5 file
########################################

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

downloads
=========

The Python code and files related to this section may be downloaded from the following table.

===========================================  =============================================
file                                         description
===========================================  =============================================
:download:`reader_attributes_trail.py`       Read NeXus HDF5 file and find plotaable data
===========================================  =============================================