.. index:: rules; NeXus

.. _Rules:

================================================
Rules for Structuring Information in NeXus Files
================================================


All NeXus files contain one or many groups of type ``NXentry`` at root level.
Many files contain only one
``NXentry``
group, then the name is ``entry``.
The NXentry level of hierarchy is there to support the storage of multiple related experiments in one file.
Or to allow the NeXus file to serve as a container for storing a whole scientific workflow from data acquisition to
publication ready data.
Also, ``NXentry`` class
groups can contain raw data or processed data.
For files with more than one ``NXentry`` group, since HDF requires
that no two items at the same level in an HDF file may have the same name,
the NeXus fashion is to
assign :index:`names <rules; naming>` with an incrementing index appended, such as
``entry1``, ``entry2``, ``entry3``, etc.


In order to illustrate what is written in the text, example hierarchies like the one in
figure :ref:`Raw Data <table.RawData>` are provided.

.. _Rules-NXentry-raw-data:

Content of a Raw Data ``NXentry`` Group
#######################################

An example raw data hierarchy is
shown in figure :ref:`Raw Data <table.RawData>`
(only showing the relevant parts of the data hierarchy).
In the example shown, the ``data`` field in the ``NXdata`` group
is linked to the 2-D detector data (a 512x512 array of 32-bit integers).
The attribute ``signal = data`` on the :ref:`NXdata` group marks this
field as the default plottable data of the ``data:NXdata`` group.
The NXdata group attribute ``axes = . .`` declares that both dimensions of
the ``data`` field do not have associated dimension scales (plotting
routines should use integer scaling for each axis).
Note that ``[,]`` represents a 2D array.

	.. compound::
	
	    .. rubric:: NeXus Raw Data Hierarchy
	
	    .. _table.RawData:
	
	    .. literalinclude:: examples/hierarchy-raw.txt
	        :tab-width: 4
	        :linenos:
	        :language: text

An ``NXentry`` describing raw data contains at least a ``NXsample``,
one ``NXmonitor``,
one ``NXdata`` and a ``NXinstrument`` group.
It is good practice to use the names
``sample`` for the ``NXsample`` group,
``control`` for the ``NXmonitor`` group holding the
experiment controlling monitor and
``instrument`` for the ``NXinstrument`` group.
The ``NXinstrument`` group contains further groups describing the individual
components of the instrument as appropriate.

The ``NXdata`` group contains links to all those data items in the ``NXentry`` :index:`hierarchy`
which are required to put up a default plot of the data.
As an example consider a SAXS instrument with a 2D detector.
The ``NXdata`` will then hold a link to the detector image.
If there is only one ``NXdata`` group,
it is good practice to name it ``data``.
Otherwise, the name of the detector bank represented is a good selection.

.. _Rules-NXentry-processed-data:

Content of a processed data ``NXentry`` group
#############################################

Processed data, see figure  :ref:`Processed Data <table.ProcessedData>`,
in this context means the results of a data reduction or
data analysis program. Note that ``[]`` represents a 1D array.

	.. compound::
	
	    .. rubric:: NeXus Processed Data Hierarchy
	
	    .. _table.ProcessedData:
	
	    .. literalinclude:: examples/hierarchy-processed.txt
	        :tab-width: 4
	        :linenos:
	        :language: text

NeXus stores such data in a simplified
``NXentry`` structure. A processed data ``NXentry``
has at minimum a ``NXsample``,
a ``NXdata`` and a ``NXprocess`` group.
Again the preferred name for the ``NXsample``
group is ``sample``.
In the case of processed data, the ``NXdata`` group holds the
result of the processing together with the associated axis data.
The ``NXprocess``
group holds the name and version of the program used for this processing
step and further ``NXparameters`` groups. These groups ought to contain the
parameters used for this data processing step in suitable detail so that
the processing step can be reproduced.

Optionally a processed data ``NXentry``
can hold a ``NXinstrument`` group with
further groups holding relevant information about the instrument. The
preferred name is again ``instrument``. Whereas for a raw data file, NeXus
strives to capture as much data as possible, a ``NXinstrument`` group for
processed data may contain a much-reduced subset.

.. _Rules-Subentry:

``NXsubentry`` or Multi-Method Data
###################################

Especially at synchrotron facilities, there are experiments which perform several different methods
on the sample at the same time. For example, combine a powder diffraction experiment with XAS.
This may happen in the same scan, so the data needs to be grouped together. A suitable ``NXentry``
would need to adhere to two different application definitions. This leads to name clashes which cannot be
resolved easily. In order to solve this issue, the following scheme was implemented in NeXus:

- The complete beamline (all data) is stored in an
  appropriate hierarchy in an ``NXentry``.

- The ``NXentry`` group contains further ``NXsubentry`` groups,
  one for each method. 
  
- Each :ref:`NXsubentry` group is constructed
  like a ``NXentry`` group.
  It contains links to all those data items required to fulfill
  the application definition for the particular. method it represents.

- The name of the application definition is stored in the ``definition``
  field of the :ref:`NXsubentry` group

- Each ``NXsubentry`` group contains a ``NXdata`` group describing
  the default plottable data for that experimental method.  
  To satisfy the NeXus requirement of finding the default
  plottable data from a ``NXentry`` group, the ``NXdata`` group
  from one of these ``NXsubentry`` groups (the fluoresence data) 
  was linked.

See figure :ref:`NeXus Multi Method Hierarchy <table.NXsubentry>` for an example hierarchy.
Note that ``[,]`` represents a 2D array.

	.. compound::
	
	    .. rubric:: NeXus Multi Method Hierarchy
	
	    .. _table.NXsubentry:
	
	    .. literalinclude:: examples/hierarchy-subentry.txt
	        :tab-width: 4
	        :linenos:
	        :language: text

.. _Rules-SpecialCases:

Rules for Special Cases
#######################

.. _Rules-SpecialCases-Scans:

Scans
=====

Scans are difficult to capture because they have great variety. Basically,
any variable can be scanned. Such behaviour cannot be captured in application definitions.
Therefore NeXus solves this difficulty with a set of
rules. In this section, ``NP`` is used as a symbol for the number of scan
points.

- The scan dimension ``NP`` is always the first dimension of any
  multi-dimensional dataset. The reason for this is that HDF allows the first
  dimension of a dataset to be unlimited.
  Which means, that data can be
  appended to the dataset during the scan.

- All data is stored as arrays of dimensions ``NP``, original dimensions
  of the data at the appropriate position in the ``NXentry`` :index:`hierarchy`.

- The ``NXdata`` group has to contain links to all variables varied during
  the scan and the detector data. Thus the ``NXdata`` group  mimics the usual
  tabular representation of a scan.

- The ``NXdata`` group has attributes
  to enable the :index:`default plotting <plotting>`,
  as described in the section titled 
  :ref:`NXdata Facilitates Automatic Plotting <NXdata-facilitates-TheDefaultPlot>`.

Simple scan
-----------

Examples may be in order here. Let us start with a simple case, the sample is
rotated around its rotation axis and data is collected in a single point
detector. See figure :ref:`Simple Scan <table.SimpleScan>` for an overview.
Then we have:

	- A dataset at ``NXentry/NXinstrument/NXdetector/data``
	  of length ``NP`` containing
	  the count data.
	
	- A dataset at ``NXentry/NXsample/rotation_angle``
	  of length ``NP`` containing
	  the positions of ``rotation_angle`` at the various steps of the scan.
	
	- ``NXdata`` contains links to:
	
	  + ``NXentry/NXinstrument/NXdetector/data``
	  + ``NXentry/NXsample/rotation_angle``
	
	- All other fields have their normal dimensions.
	
	.. compound::
	
	    .. rubric:: NeXus Simple Scan Example
	
	    .. _table.SimpleScan:
	
	    .. literalinclude:: examples/simplescan.txt
	        :tab-width: 4
	        :linenos:
	        :language: text

Simple scan with area detector
------------------------------

The next example is the same scan but with an area detector with ``xsize``
times ``ysize`` pixels. The only thing which changes is that
``/NXentry/NXinstrument/NXdetector/data`` will have the dimensions
``NP, xsize, ysize``. See figure :ref:`Simple Scan with Area Detector <fig.SimpleScanArea>` for an overview.

	.. compound::
	
	    .. rubric:: NeXus Simple Scan Example with Area Detector
	
	    .. _fig.SimpleScanArea:
	
	    .. literalinclude:: examples/simplescanarea.txt
	        :tab-width: 4
	        :linenos:
	        :language: text

The ``NXdata`` group attribute ``axes = rotation_angle . .`` declares that only the first
dimension of the plottable ``data`` has a dimension scale (by name, ``rotation_angle``).  
The other two dimensions have no associated dimension scales and should be plotted against
integer bin numbers.

Complex *hkl* scan
------------------

The next example involves a complex movement along the :math:`h` axis in reciprocal
space which requires mutiple motors of a :index:`four-circle diffractometer` to be
varied during the scan. We then have:

- A dataset at ``NXentry/NXinstrument/NXdetector/data`` of length
  ``NP`` containing
  the count data.

- A dataset at ``NXentry/NXinstrument/NXdetector/polar_angle`` of length
  ``NP`` containing
  the positions of the detector's polar_angle at the various steps
  of the scan.

- A dataset at ``NXentry/NXsample/rotation_angle`` of length
  ``NP`` containing
  the positions of ``rotation_angle`` at the various steps of the scan.

- A dataset at ``NXentry/NXsample/chi`` of length ``NP`` containing
  the positions of chi at the various steps of the scan.

- A dataset at ``NXentry/NXsample/phi`` of length ``NP`` containing
  the positions of phi at the various steps of the scan.

- A dataset at ``NXentry/NXsample/h`` of length ``NP`` containing
  the positions of the reciprocal coordinate :math:`h` at the
  various steps of the scan.

- A dataset at ``NXentry/NXsample/k`` of length ``NP`` containing
  the positions of the reciprocal coordinate :math:`k` at the
  various steps of the scan.

- A dataset at ``NXentry/NXsample/l`` of length ``NP`` containing
  the positions of the reciprocal coordinate :math:`l` at the
  various steps of the scan.

- ``NXdata`` contains links to:
  
  + ``NXentry/NXinstrument/NXdetector/data``
  + ``NXentry/NXinstrument/NXdetector/polar_angle``
  + ``NXentry/NXsample/rotation_angle``
  + ``NXentry/NXsample/chi``
  + ``NXentry/NXsample/phi``
  + ``NXentry/NXsample/h``
  + ``NXentry/NXsample/k``
  + ``NXentry/NXsample/l``
  
  The ``NXdata`` also contains appropriate attributes 
  as described in :ref:`Design-FindPlottable-NIAC2014`.

- All other fields have their normal dimensions.

.. compound::

    .. rubric:: NeXus Complex *hkl* Scan

    .. _table.ComplexScan:

    .. literalinclude:: examples/complex-hkl-scan.txt
        :tab-width: 4
        :linenos:
        :language: text

Multi-parameter scan: XAS
-------------------------

Data can be stored almost anywhere in the NeXus tree.  While the previous examples
showed data arrays in either ``NXdetector`` or ``NXsample``,
this example demonstrates that data can be stored in other places.  Links are used
to reference the data.

The example is for X-ray Absorption Spectroscopy (XAS) data where the monochromator
energy is step-scanned and counts are read back from detectors before (``I0``)
and after (``I``) the sample.  These energy scans are repeated at a sequence
of sample temperatures to map out, for example, a phase transition.  While it is customary
in XAS to plot *log(I0/I)*, we show them separately here
in two different ``NXdata``
groups to demonstrate that such things are possible.
Note that the length of the 1-D energy array is ``NE`` while
the length of the 1-D temperature array is ``NT``

	.. compound::
	
	    .. rubric:: NeXus Multi-parameter scan: XAS
	
	    .. _table.XasScan:
	
	    .. literalinclude:: examples/xas.txt
	        :tab-width: 4
	        :linenos:
	        :language: text

.. _Rules-SpecialCases-Rastering:

Rastering
=========

Rastering is the process of making experiments at various locations in the
sample volume. Again, rasterisation experiments can be variable. Some people
even raster on spirals! Rasterisation experiments are treated the same way as
described above for scans. Just replace ``NP`` with
``P``, the number of raster points.

Special rules apply if a rasterisation happens on a regular grid of size
``xraster, yraster``. Then the variables varied in the rasterisation will be
of dimensions ``xraster, yraster`` and the detector data of dimensions
``xraster, yraster, (orginal dimensions)``
of the detector. For example, an area detector of
size ``xsize, ysize`` then it is stored with
dimensions ``xraster, yraster, xsize, ysize``.

.. warning:: Be warned: if you use the 2D rasterisation method with ``xraster, yraster`` you may end up with
             invalid data if the scan is aborted prematurely. This cannot happen if the first method is used.


Streaming Data Acquisition And Logging
======================================

More and more data is collected in streaming mode. This means that time stamped data is logged for one or more inputs, 
possibly together with detector data. Another use case is the logging of parameters, for example temperature, while a long 
running data collection is in progress. NeXus covers this case too. There is one simple rule for structuring such files:

Just use the standard NeXus raw data file structure, but replace the corresponding data object 
with an :ref:`NXlog` or :ref:`NXevent_data` structure of the same name. 

For example, consider your instrument is streaming detector images against a magnetic_field on the sample. In this case both 
NXsample/magnetic_field and NXdetector/data would become NXlog structures instead of simple arrays i.e. the NXlog structure will 
have the same name as the NeXus field involved.        
 

NXcollection
============

On demand from the community, NeXus introduced a more informal method of
storing information in a NeXus file.  This is the ``NXcollection``
class which can appear anywhere underneath ``NXentry``.
``NXcollection`` is a container for holding other data.
The foreseen use is to document collections of similar data which do not
otherwise fit easily into the ``NXinstrument``
or ``NXsample`` hierarchy, such as the intent to record
*all* motor positions on a synchrotron beamline.
Thus, ``NXcollection`` serves as a quick point of access
to data for an instrument scientist or another expert. NXcollection is 
also a feature for those who are too lazy to build up the complete NeXus 
hierarchy.  An example usage case is documented in figure
:ref:`NXcollection example <table.NXcollection>`.

	.. compound::
	
	    .. rubric:: ``NXcollection`` Example
	
	    .. _table.NXcollection:
	
	    .. literalinclude:: examples/nxcollection.txt
	        :tab-width: 4
	        :linenos:
	        :language: text
