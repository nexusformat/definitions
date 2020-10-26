.. index:: h5py

.. _Example-H5py:

==============================
Python Examples using ``h5py``
==============================

One way to gain a quick familiarity with NeXus is to start working with some data. For at least the
first few examples in this section, we have a simple two-column set of 1-D data, collected as part of a
series of alignment scans by the APS USAXS instrument during the time it was stationed at
beam line 32ID. We will show how to write this
data using the Python language and the ``h5py`` package [#]_
(:index:`using <h5py>`  ``h5py`` calls directly rather than using the NeXus NAPI). The
actual data to be written was extracted (elsewhere) from a ``spec`` [#]_ data file 
and read as a text block from a file by the Python source code.
Our examples will start with the simplest case and add only mild complexity with each new case
since these examples are meant for those who are unfamiliar with NeXus.

.. [#] *h5py*: https://www.h5py.org/
.. [#] *SPEC*: http://certif.com/spec.html


The data shown plotted in the next figure will be written to the NeXus HDF5 file
using only two NeXus base classes, ``NXentry`` and ``NXdata``, in the first example
and then minor variations on this structure in the next two examples.  The
data model is identical to the one in the :ref:`Introduction <fig.simple-example>` 
chapter except that the names will be different, as shown below:


.. compound::
	
	.. figure:: ../../img/Simple.png
		:width: 60%
		:alt: simple data structure
		
		data structure, (from Introduction)
	
	.. rubric:: our h5py example
	
	.. literalinclude:: data-model.txt
	    :tab-width: 4
	    :linenos:
	    :language: text
	
	.. _Example-H5py-Plot:
	
	.. figure:: s00008.png
	    :alt: Example-H5py-Plot
	    :width: 80%
	
	    plot of our *mr_scan*
	
	.. rubric:: two-column data for our *mr_scan*
	
	.. literalinclude:: input.dat
	    :tab-width: 4
	    :linenos:
	    :language: text

Writing the simplest data using ``h5py``
########################################

These two examples show how to write the simplest data (above).
One example writes the data directly to the :ref:`NXdata` group 
while the other example writes the data to ``NXinstrument/NXdetector/data``
and then creates a soft link to that data in ``NXdata``.


.. toctree::
	:maxdepth: 1
	
	writer_1_3
	writer_2_1

.. _Example-H5py-complete:

Complete ``h5py`` example writing and reading a NeXus data file
###############################################################

.. _Example-H5py-Writing:

Writing the HDF5 file using **h5py**
====================================

In the main code section of :ref:`BasicWriter.py <Example-H5py-BasicWriter>`, 
a current time stamp
is written in the format of *ISO 8601* (``yyyy-mm-ddTHH:MM:SS``).
For simplicity of this code example, we use a text string for the time, rather than
computing it directly from Python support library calls.  It is easier this way to
see the exact type of string formatting for the time.  When using the Python
``datetime`` package, one way to write the time stamp is:

.. code-block:: python
    :linenos:

    timestamp = "T".join( str( datetime.datetime.now() ).split() )

.. 2016-02-16,PRJ:
   ISO8601 now allows the "T" to be replaced by " " which is more readable
   We won't change now.  Shows a pedantic case, for sure.

The data (``mr`` is similar to "two_theta" and
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

    .. rubric:: *BasicWriter.py*: Write a NeXus HDF5 file using Python with h5py
    
    .. _Example-H5py-BasicWriter:

    .. literalinclude:: BasicWriter.py
	    :tab-width: 4
	    :linenos:
	    :language: python

.. _Example-H5py-Reading:

Reading the HDF5 file using **h5py**
====================================

The file reader, :ref:`BasicReader.py <Example-H5py-Reader>`,
is very simple since the bulk of the work is done by ``h5py``.
Our code opens the HDF5 we wrote above,
prints the HDF5 attributes from the file, reads the two datasets,
and then prints them out as columns.  As simple as that.
Of course, real code might add some error-handling and
extracting other useful stuff from the file.

.. note:: See that we identified each of the two datasets using HDF5 absolute path references
          (just using the group and dataset names). Also, while coding this example, we were reminded
          that HDF5 is sensitive to upper or lowercase. That is, ``I00`` is not the same is
          ``i00``.

.. compound::

    .. rubric:: *BasicReader.py*: Read a NeXus HDF5 file using Python with h5py
    
    .. _Example-H5py-Reader:

    .. literalinclude:: BasicReader.py
	    :tab-width: 4
	    :linenos:
	    :language: python

Output from ``BasicReader.py`` is shown next.

.. compound::

    .. rubric:: Output from ``BasicReader.py``

    .. literalinclude:: output.txt
	    :tab-width: 4
	    :linenos:
	    :language: text

.. _finding.default.data.python:

Finding the default plottable data
----------------------------------

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

.. index:: 
	NeXpy

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



.. _h5py-example-external-links:

Links to Data in External HDF5 Files
####################################

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

source code: externalExample.py
===============================

Here is the complete code of a Python program, using ``h5py``
to write a NeXus-compliant HDF5 file with links to data in other HDF5 files.

.. compound::

    .. rubric:: *externalExample.py*: Write using HDF5 external links
    
    .. _Example-H5py-externalExample:

    .. literalinclude:: externalExample.py
       :tab-width: 4
       :linenos:
       :language: python

       
downloads
=========

The Python code and files related to this section may be downloaded from the following table.

===========================================  =============================================
file                                         description
===========================================  =============================================
:download:`input.dat`                        2-column ASCII data used in this section
:download:`BasicReader.py`                   python code to read example *prj_test.nexus.hdf5*
:download:`BasicWriter.py`                   python code to write example *prj_test.nexus.hdf5*
:download:`external_angles_h5dump.txt`       *h5dump* analysis of *external_angles.hdf5*
:download:`external_angles.hdf5`             HDF5 file written by *externalExample*
:download:`external_angles_structure.txt`    *punx tree* analysis of *external_angles.hdf5*
:download:`external_counts_h5dump.txt`       *h5dump* analysis of *external_counts.hdf5*
:download:`external_counts.hdf5`             HDF5 file written by *externalExample*
:download:`external_counts_structure.txt`    *punx tree* analysis of *external_counts.hdf5*
:download:`externalExample.py`               python code to write external linking examples
:download:`external_master_h5dump.txt`       *h5dump* analysis of *external_master.hdf5*
:download:`external_master.hdf5`             NeXus file written by *externalExample*
:download:`external_master_structure.txt`    *punx tree* analysis of *external_master.hdf5*
:download:`prj_test.nexus_h5dump.txt`        *h5dump* analysis of the NeXus file
:download:`prj_test.nexus.hdf5`              NeXus file written by *BasicWriter*
:download:`prj_test.nexus_structure.txt`     *punx tree* analysis of the NeXus file
===========================================  =============================================
