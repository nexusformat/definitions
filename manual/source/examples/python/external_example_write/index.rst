.. _h5py-example-external-links:

Write a NeXuS HDF5 File with links to external data
###################################################

HDF5 files may contain links to data (or groups) in other files.  
This can be used to advantage to refer to data in existing HDF5 files
and create NeXus-compliant data files.  Here, we show such an example, 
using the same ``counts`` v. ``two_theta`` data from the examples above.

We use the *HDF5 external file* links with NeXus data files.

::

  f[local_addr] = h5py.ExternalLink(external_file_name, external_addr)

where ``f`` is an open ``h5py.File()`` object in which we will create the new link,
``local_addr`` is an HDF5 path address, ``external_file_name`` is the name 
(relative or absolute) of an existing HDF5 file, and ``external_addr`` is the
HDF5 path address of the existing data in the ``external_file_name`` to be linked.

file: external_angles.hdf5
==========================

Take for example, the structure of :download:`external_angles.hdf5`, 
a simple HDF5 data file that contains just the ``two_theta``
angles in an HDF5 dataset at the root level of the file.
Although this is a valid HDF5 data file, it is not a valid NeXus data file:

.. code-block:: text
    :linenos:

    angles:float64[31] = [17.926079999999999, '...', 17.92108]
      @units = degrees

file: external_counts.hdf5
==========================

The data in the file ``external_angles.hdf5`` might be referenced from
another HDF5 file (such as :download:`external_counts.hdf5`) 
by an HDF5 external link. [#]_  
Here is an example of the structure:

.. code-block:: text
    :linenos:

    entry:NXentry
      instrument:NXinstrument
      detector:NXdetector
        counts:NX_INT32[31] = [1037, '...', 1321]
          @units = counts
        two_theta --> file="external_angles.hdf5", path="/angles"

.. [#] see these URLs for further guidance on HDF5 external links:
   https://portal.hdfgroup.org/display/HDF5/H5L_CREATE_EXTERNAL, 
   http://docs.h5py.org/en/stable/high/group.html#external-links

file: external_master.hdf5
==========================

A valid NeXus data file could be created that refers to the data in these files
without making a copy of the data files themselves.  

.. note::
   It is necessary for all
   these files to be located together in the same directory for the HDF5 external file 
   links to work properly.`  

To be a valid NeXus file, it must contain a :ref:`NXentry` group.
For the files above, it is simple to make a master file that links to
the data we desire, from structure that we create.  We then add the
group attributes that describe the default plottable data:

.. code-block:: text

    data:NXdata
      @signal = counts
      @axes = "two_theta"
      @two_theta_indices = 0

Here is (the basic structure of) :download:`external_master.hdf5`, an example:

.. code-block:: text
    :linenos:

    entry:NXentry
    @default = data
      instrument --> file="external_counts.hdf5", path="/entry/instrument"
      data:NXdata
      	@signal = counts
      	@axes = "two_theta"
         @two_theta = 0
       	counts --> file="external_counts.hdf5", path="/entry/instrument/detector/counts"
       	two_theta --> file="external_angles.hdf5", path="/angles"

source code: external_example_write.py
======================================

Here is the complete code of a Python program, using ``h5py``
to write a NeXus-compliant HDF5 file with links to data in other HDF5 files.

.. compound::

    .. rubric:: *external_example_write.py*: Write using HDF5 external links
    
    .. _Example-Python-external_example_write:

    .. tabs::

        .. tab:: nexusformat

            .. literalinclude:: nexusformat/external_example_write.py
                :tab-width: 4
                :linenos:
                :language: python

        .. tab:: h5py

            .. literalinclude:: external_example_write.py
                :tab-width: 4
                :linenos:
                :language: python

downloads
=========

The Python code and files related to this section may be downloaded from the following table.

=================================================  ===================================================
file                                               description
=================================================  ===================================================
:download:`external_angles_h5dump.txt`             *h5dump* analysis of *external_angles.hdf5*
:download:`external_angles.hdf5`                   HDF5 file written by *external_example_write*
:download:`external_angles_structure.txt`          *punx tree* analysis of *external_angles.hdf5*
:download:`external_counts_h5dump.txt`             *h5dump* analysis of *external_counts.hdf5*
:download:`external_counts.hdf5`                   HDF5 file written by *external_example_write*
:download:`external_counts_structure.txt`          *punx tree* analysis of *external_counts.hdf5*
:download:`external_example_write.py`              h5py code to write external linking examples
:download:`nexusformat/external_example_write.py`  nexusformat code to write external linking examples
:download:`external_master_h5dump.txt`             *h5dump* analysis of *external_master.hdf5*
:download:`external_master.hdf5`                   NeXus file written by *external_example_write*
:download:`external_master_structure.txt`          *punx tree* analysis of *external_master.hdf5*
=================================================  ===================================================