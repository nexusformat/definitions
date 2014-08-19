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

.. [#] *h5py*: http://code.google.com/p/h5py
.. [#] *SPEC*: http://certif.com/spec.html


The data shown plotted in the next figure will be written to the NeXus HDF5 file
using the only two required NeXus objects ``NXentry`` and ``NXdata`` in the first example
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
	    :language: guess
	
	.. _Example-H5py-Plot:
	
	.. figure:: s00008.png
	    :alt: Example-H5py-Plot
	    :width: 80%
	
	    plot of our *mr_scan*
	
	.. rubric:: two-column data for our *mr_scan*
	
	.. literalinclude:: input.dat
	    :tab-width: 4
	    :linenos:
	    :language: guess

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
==========================================

In the main code section of :ref:`BasicWriter.py <Example-H5py-BasicWriter>`, a current time stamp
is written in the format of *ISO 8601*.
For simplicity of this code example, we use a text string for the time, rather than
computing it directly from Python support library calls.  It is easier this way to
see the exact type of string formatting for the time.  When using the Python
``datatime`` package, one way to write the time stamp is:

.. code-block:: python
    :linenos:

    timestamp = "T".join( str( datetime.datetime.now() ).split() )

The data (``mr`` is similar to "two_theta" and
``I00`` is similar to "counts") is collated into two Python lists. We use our ``my_lib``
support to read the file and parse the two-column format.

The new HDF5 file is opened (and created if not already existing) for writing,
setting common NeXus attributes in the same command from our support library.
Proper HDF5+NeXus groups are created for ``/entry:NXentry/mr_scan:NXdata``.
Since we are not using the NAPI, our
support library must create and set the ``NX_class`` attribute on each group.

.. note:: We want to create the desired structure of
          ``/entry:NXentry/mr_scan:NXdata/``. 
          First, our support library calls 
          ``nxentry = f.create_group("entry")`` 
          to create the ``NXentry`` group called
          ``entry`` at the root level. Then, it calls 
          ``nxdata = nxentry.create_group("mr_scan")`` 
          to create the ``NXentry`` group called
          ``entry`` as a child of the ``NXentry`` group.

Next, we create a dataset called ``title`` to hold a title string that can
appear on the default plot.

Next, we create datasets for ``mr`` and ``I00`` using our support library.
The data type of each, as represented in ``numpy``, will be recognized by
``h5py`` and automatically converted to the proper HDF5 type in the file.
A Python dictionary of attributes is given, specifying the engineering units and other
values needed by NeXus to provide a default plot of this data.  By setting ``signal=1``
as an attribute on ``I00``, NeXus recognizes ``I00`` as the default
*y* axis for the plot.  The ``axes="mr"`` connects the dataset
to be used as the *x* axis.

Finally, we *must* remember to call ``f.close()`` or we might
corrupt the file when the program quits.

.. compound::

    .. rubric:: *BasicWriter.py*: Write a NeXus HDF5 file using Python with h5py
    
    .. _Example-H5py-BasicWriter:

    .. literalinclude:: BasicWriter.py
	    :tab-width: 4
	    :linenos:
	    :language: guess

.. _Example-H5py-Reading:

Reading the HDF5 file using **h5py**
==========================================

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
	    :language: guess

Output from ``BasicReader.py`` is shown next.

.. compound::

    .. rubric:: Output from ``BasicReader.py``

    .. literalinclude:: output.txt
	    :tab-width: 4
	    :linenos:
	    :language: text

.. _Example-H5py-Validation:

Validating the HDF5 file
========================

Now we have an HDF5 file that contains our data.  What makes
this different from a NeXus data file?  A NeXus file
has a specific arrangement of groups and datasets
in an HDF5 file.

To test that our HDF5 file conforms to the NeXus standard,
we use the :ref:`Java-version of NXvalidate <NXvalidate-java>`.  
Referring to the next figure,
we compare our HDF5 file with the rules for
generic [#]_ data files (``all.nxdl.xml``).  The only items that have
been flagged are the "non-standard field names" *mr* and
*I00*.  Neither of these two names is
specifically named in the NeXus NXDL definition for
the ``NXdata`` base class.  As we'll see shortly,
this is not a problem.

.. [#]
    generic NeXus data files: NeXus data
    files for which no application-specific NXDL
    applies

.. compound::

    .. _fig-Example-H5py-Validation:

    .. figure:: nxvalidate.png
        :alt: fig-Example-H5py-Validation
        :width: 80%

        NeXus validation of our HDF5 file

.. note:: Note that ``NXvalidate`` shows
          only the first data field for *mr* and
          *I00*.


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
Compare this with
:ref:`Example-H5py-Plot`
and note that the horizontal axis of this plot is mirrored from that above.
This is because the data is stored in the file in descending
``mr`` order and ``NeXpy`` has plotted
it that way by default.

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

file: external_angles.hdf5
=================================

Take for example, the structure of :download:`external_angles.hdf5`, 
a simple HDF5 data file that contains just the ``two_theta``
angles in an HDF5 dataset at the root level of the file.
Although this is a valid HDF5 data file, it is not a valid NeXus data file:

.. code-block:: guess
    :linenos:

	angles:float64[31] = [17.926079999999999, '...', 17.92108]
	  @units = degrees

file: external_counts.hdf5
=================================

The data in the file ``external_angles.hdf5`` might be referenced from
another HDF5 file (such as :download:`external_counts.hdf5`) 
by an HDF5 external link. [#]_  
Here is an example of the structure

.. code-block:: guess
    :linenos:

	entry:NXentry
	  instrument:NXinstrument
	    detector:NXdetector
	      counts:NX_INT32[31] = [1037, '...', 1321]
	        @units = counts
	        @signal = 1
	        @axes = two_theta
	      two_theta --> file="external_angles.hdf5", path="/angles"

.. note:: The file ``external_counts.hdf5`` is not a complete NeXus file since it does not 
   contain an NXdata group containing a dataset with ``signal=1`` attribute.

.. [#] see these URLs for further guidance on HDF5 external links:
   http://www.hdfgroup.org/HDF5/doc/RM/RM_H5L.html#Link-CreateExternal, 
   http://www.h5py.org/docs-1.3/guide/group.html#external-links

file: external_master.hdf5
=================================

A valid NeXus data file could be created that refers to the data in these files
without making a copy of the data files themselves.  

.. note::
   It is necessary for all
   these files to be located together in the same directory for the HDF5 external file 
   links to work properly.`  

To be a valid NeXus file, it must contain a :ref:`NXentry` group containing a 
:ref:`NXdata` group containing only one dataset with the aatribute ``signal=1``.
For the files above, it is simple to make a master file that links to
the data we desire, from structure that we create.  In ``external_counts.hdf5`` above,
see that the required attribute ``signal=1`` is already present.
Here is :download:`external_master.hdf5`, an example:

.. code-block:: guess
    :linenos:

	entry:NXentry
	  instrument --> file="external_counts.hdf5", path="/entry/instrument"
	  data:NXdata
	    counts --> file="external_counts.hdf5", path="/entry/instrument/detector/counts"
	    two_theta --> file="external_angles.hdf5", path="/angles"

source code: externalExample.py
=================================

Here is the complete code of a Python program, using ``h5py``
to write a NeXus-compliant HDF5 file with links to data in other HDF5 files.

.. compound::

    .. rubric:: *externalExample.py*: Write using HDF5 external links
    
    .. _Example-H5py-externalExample:

    .. literalinclude:: externalExample.py
	    :tab-width: 4
	    :linenos:
	    :language: guess



.. _h5py-example-helpers:

Python Helper Modules for ``h5py`` Examples
###########################################

Two additional Python modules were used to describe these ``h5py`` examples.
The source code for each is given here.  The first is a library we wrote that helps us
create standard NeXus components using ``h5py``.  The second is a tool that helps
us inspect the content and structure of HDF5 files.

.. _h5py-example-my_lib:

``mylib`` support module
========================

The examples in this section make use of
a small helper library that calls ``h5py`` to create the
various NeXus data components of
:ref:`Design-Groups`,
:ref:`Design-Fields`,
:ref:`Design-Attributes`, and
:ref:`Design-Links`.
In a smaller sense, this subroutine library (``my_lib``) fills the role of the NAPI for writing
the data using h5py.

.. literalinclude:: my_lib.py
    :tab-width: 4
    :linenos:
    :language: python

.. _h5py-example-h5toText:

``h5toText`` support module
===========================

The module ``h5toText`` reads an HDF5 data file and prints out the
structure of the groups, datasets, attributes, and links in that file.
There is a command-line option to print out more or less of the data
in the dataset arrays.

.. literalinclude:: h5toText.py
    :tab-width: 4
    :linenos:
    :language: python

