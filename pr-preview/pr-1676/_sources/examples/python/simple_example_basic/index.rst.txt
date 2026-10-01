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

    Examine the example code below for these key actions to create the structure:

    =====================================   ================================================  ================================================
    action                                  nexusformat function                              h5py function
    =====================================   ================================================  ================================================
    create file & root (``/``) structure    ``with nxopen(fileName, "w") as f:``              ``with h5py.File(fileName, "w") as f:``
    create ``/entry`` group                 ``f["entry"] = NXentry()``                        ``nxentry = f.create_group("entry"); nxentry.attrs["NX_class"] = "NXentry"``
    create ``/entry/mr_scan`` group         ``f["entry/mr_scan"] = NXdata(y, x)``             ``nxdata = nxentry.create_group("mr_scan"); nxdata.attrs["NX_class"] = "NXdata"``
    store ``mr`` data                       ``x = NXfield(mr_arr, units="degrees", ...)``     ``x = nxdata.create_dataset("mr", data=mr_arr); x.attrs["units"] = "degrees"``
    store ``I00`` data                      ``y = NXfield(i00_arr, units="counts", ...)``     ``y = nxdata.create_dataset("I00", data=i00_arr); y.attrs["units"] = "counts"``
    add ``title``                           ``f["entry/title"] = ...``                        ``nxentry.create_dataset("title", ...)``
    =====================================   ================================================  ================================================

The ``title`` string is added to label the default plot.

The data type of  ``mr`` and ``I00``, as represented in ``numpy``, will be recognized
by ``h5py`` and automatically converted to the proper HDF5 type in the file.
Engineering units and other metadata needed by NeXus to provide a default plot of
this data are provided.  The NeXus ``signal="I00"``
attribute on the :ref:`NXdata` group identifies ``I00`` as the default
*y* axis for the plot.  The ``axes="mr"`` attribute on the :ref:`NXdata`
group connects the dataset to be used as the *x* axis.

Since we opened the file with a Python context manager (``with .. as f:``), it
is not necessary to make an explicit call to close the file.  The context manager
will close the file with the context.

.. compound::

    .. rubric:: *simple_example_basic_write.py*: Write a NeXus HDF5 file using Python with h5py

    .. _Example-Python-BasicWriter:

    .. tabs::

        .. tab:: nexusformat

            In the nexusformat version, these attributes are added automatically
            when calling ``NXdata(y, x)`` with the first argument defining the
            signal and the second the axes. With signals of higher rank, the
            second argument would be a list of axes.

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

            The nexusformat version prints the whole file as a tree.

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
    .. tabs::

        .. tab:: nexusformat

            The nexusformat version prints the whole file as a tree.

            .. literalinclude:: nexusformat/output.txt
                :tab-width: 4
                :linenos:
                :language: text

        .. tab:: h5py

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
