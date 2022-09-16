.. _Example-Python-complete:

Getting started
###############

.. _Example-Python-Writing:

Write a NeXus HDF5 File
=======================

In the main code section of :ref:`simple_example_basic_write.py <Example-Python-BasicWriter>`, 
the data (``mr`` is similar to "two_theta" and
``I00`` is similar to "counts") is collated into two Python lists. We use the
**numpy** package to read the file and parse the two-column format.

The new HDF5 file is opened (and created if not already existing) for writing,
setting common NeXus attributes in the same command from our support library.
Proper HDF5+NeXus groups are created for ``/entry:NXentry/mr_scan:NXdata``.
Since we are not using the NAPI, our
support library must create and set the ``NX_class`` attribute on each group.

.. note:: We want to create the desired structure of
          ``/entry:NXentry/mr_scan:NXdata/``. 
          
	  #. First, our support library calls 
             ``f = h5py.File()`` 
             to create the file and root level NeXus structure.
	  #. Then, it calls 
             ``nxentry = f.create_group("entry")`` 
             to create the ``NXentry`` group called
             ``entry`` at the root level. 
	  #. Then, it calls 
             ``nxdata = nxentry.create_group("mr_scan")`` 
             to create the ``NXentry`` group called
             ``entry`` as a child of the ``NXentry`` group.

Next, we create a dataset called ``title`` to hold a title string that can
appear on the default plot.

Next, we create datasets for ``mr`` and ``I00`` using our support library.
The data type of each, as represented in ``numpy``, will be recognized by
``h5py`` and automatically converted to the proper HDF5 type in the file.
A Python dictionary of attributes is given, specifying the engineering units and other
values needed by NeXus to provide a default plot of this data.  By setting ``signal="I00"``
as an attribute on the group, NeXus recognizes ``I00`` as the default
*y* axis for the plot.  The ``axes="mr"`` attribute on the :ref:`NXdata` 
group connects the dataset to be used as the *x* axis.

Finally, we *must* remember to call ``f.close()`` or we might
corrupt the file when the program quits.

.. compound::

    .. rubric:: *simple_example_basic_write.py*: Write a NeXus HDF5 file using Python with h5py
    
    .. _Example-Python-BasicWriter:

    .. tabs::

        .. tab:: nexusformat

            .. literalinclude:: nexusformat/simple_example_basic_write.py
                :tab-width: 4
                :linenos:
                :language: python

        .. tab:: h5py

            .. literalinclude:: simple_example_basic_write.py
	            :tab-width: 4
	            :linenos:
	            :language: python

.. _Example-Python-Reading:

Read a NeXus HDF5 File
======================

The file reader, :ref:`simple_example_basic_read.py <Example-Python-Reader>`,
opens the HDF5 we wrote above,
prints the HDF5 attributes from the file, reads the two datasets,
and then prints them out as columns.  As simple as that.
Of course, real code might add some error-handling and
extracting other useful stuff from the file.

.. note:: See that we identified each of the two datasets using HDF5 absolute path references
          (just using the group and dataset names). Also, while coding this example, we were reminded
          that HDF5 is sensitive to upper or lowercase. That is, ``I00`` is not the same is
          ``i00``.

.. compound::

    .. rubric:: *simple_example_basic_read.py*: Read a NeXus HDF5 file using Python

    .. _Example-Python-Reader:

    .. tabs::

        .. tab:: nexusformat

            .. literalinclude:: nexusformat/simple_example_basic_read.py
                :tab-width: 4
                :linenos:
                :language: python

        .. tab:: h5py

            .. literalinclude:: simple_example_basic_read.py
	            :tab-width: 4
	            :linenos:
	            :language: python

Output from ``simple_example_basic_read.py`` is shown next.

.. compound::

    .. rubric:: Output from ``simple_example_basic_read.py``

    .. literalinclude:: output.txt
	    :tab-width: 4
	    :linenos:
	    :language: text

downloads
=========

The Python code and files related to this section may be downloaded from the following table.

=====================================================  ===================================================================
file                                                   description
=====================================================  ===================================================================
:download:`../simple_example.dat`                      2-column ASCII data used in this section
:download:`simple_example_basic_read.py`               h5py code to read example *simple_example_basic.nexus.hdf5*
:download:`nexusformat/simple_example_basic_read.py`   nexusformat code to read example *simple_example_basic.nexus.hdf5*
:download:`simple_example_basic_write.py`              h5py code to write example *simple_example_basic.nexus.hdf5*
:download:`nexusformat/simple_example_basic_write.py`  nexusformat code to write example *simple_example_basic.nexus.hdf5*
:download:`simple_example_basic.nexus_h5dump.txt`      *h5dump* analysis of the NeXus file
:download:`simple_example_basic.nexus.hdf5`            NeXus file written by *BasicWriter*
:download:`simple_example_basic.nexus_structure.txt`   *punx tree* analysis of the NeXus file
=====================================================  ===================================================================
