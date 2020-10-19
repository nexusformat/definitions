.. _NXDL_Tutorial:

====================================================
Constructing NeXus Files and Application Definitions
====================================================

In :ref:`Design`, we discussed the design of the NeXus format in general terms.
In this section a more tutorial style introduction in how to construct a NeXus file is
given. As an example a hypothetical instrument named WONI will be used.

.. note:: 
          If you are looking for a tutorial on reading or writing NeXus data files
          using the NeXus API, consult the :ref:`NAPI` chapter.
          For code examples, refer to :ref:`Examples.NAPI` chapter.
          Alternatively, there are examples in the :ref:`native-HDF5-Examples`
          chapter of writing and reading NeXus data files using the native HDF5 interfaces in C.
          Further, there are also some Python examples using the ``h5py`` package
          in the :ref:`Example-H5py` section.

..  ======================================================
    section: Basic organization within the NeXus hierarchy
    ======================================================

.. _NXDL_Tutorial-WONI:

The WOnderful New Instrument (WONI)
###################################

Consider yourself to be responsible for some hypothetical
:index:`WOnderful New Instrument <WONI>`
:index:`(WONI) <tutorial; WONI>`.
You are tasked to ensure that WONI will record data according to the NeXus standard.
For the sake of simplicity, WONI bears a strong resemblance to a simple
powder diffractometer, but let's pretend that  WONI cannot
use any of the existing NXDL application definitions.

.. compound::

    .. _FigWoniSchematic:

    .. figure:: img/woni-schematic.png
        :alt: FigWoniSchematic
		:width: 90%
		:align: center

        The (fictional) WONI example powder diffractometer

WONI uses collimators and a monochromator to illuminate the
sample with neutrons of a selected wavelength as described in
:ref:`FigWoniSchematic`.  The diffracted beam is collected
in a large, banana-shaped, position sensitive detector. Typical data looks like
:ref:`FigWoniPowderData`.
There is a generous background to the data plus quite a number of diffraction peaks.

.. compound::

    .. _FigWoniPowderData:

    .. figure:: img/woni-powderimage.png
        :alt: FigWoniPowderData
		:width: 90%
		:align: center

        Example Powder Diffraction Plot from (fictional) WONI at HYNES

Constructing a NeXus file for WONI
##################################

The starting point for a NeXus file for WONI will be an 
empty basic NeXus file hierarchy as documented in
the next figure. In order to arrive at a full NeXus file, 
the following steps are required:

#. For each instrument component, decide which parameters need to be stored

#. Map the component parameters to NeXus groups and parameters and add the components to the
   ``NXinstrument`` hierarchy

#. Decide what needs to go into ``NXdata``.  While this group is optional,
   you are urged strongly to provide an ``NXdata`` group to support
   default plotting. 

#. Fill the ``NXsample`` and ``NXmonitor`` groups

.. compound::

    .. rubric:: Basic structure of a NeXus file

    .. _FigShell:

    .. literalinclude:: examples/NXshell.txt
        :tab-width: 4
        :linenos:
        :language: text

Decide which parameters need to be stored
=========================================

Now the various groups of this empty NeXus file shell need to be filled. The next step is to look at a
design drawing of WONI. Identify all the instrument components like collimators, detectors, monochromators etc.
For each component decide which values need to be stored. As NeXus aims to describe the experiment as good as
possible, strive to capture as much information as practical.

Mapping parameters to NeXus
===========================

With the list of parameters to store for each component, consult the reference manual section on the NeXus
base classes. You will find that for each of your instruments components there will be a suitable NeXus base class.
Add this base class together with a name as a group under NXinstrument in your NeXus file hierarchy. Then consult the
possible parameter names in the NeXus base class and match them with the parameters you wish to store for your
instruments components.

As an example, consider the monochromator. You may wish to store: the wavelength, the d-value of the reflection used,
the type of the monochromator and its angle towards the incoming beam. The reference manual tells you that NXcrystal
is the right base class to use. Suitable fields for your parameters can be found in there to. After adding them to
the basic NeXus file, the file looks like in the next figure:

.. compound::

    .. rubric:: Basic structure of a NeXus file with a monochromator added

    .. _FigShellMono:

    .. literalinclude:: examples/NXshellMono.txt
        :tab-width: 4
        :linenos:
        :language: text

If a parameter or even a whole group is missing in order to describe your experiment, do not despair! Contact the
NIAC and suggest to add the group or parameter. Give a little documentation what it is for. The NIAC will check that your
suggestion is no duplicate and sufficiently documented and will then proceed to enhance the base classes with your suggestion.

A more elaborate example of the mapping process is given in the section :ref:`NXDL_Tutorial-CreatingNxdlSpec`.

Decide on ``NXdata``
====================

The ``NXdata/`` group is supposed to contain the data required to put up a quick plot. For WONI this is a plot of counts versus
two theta (polar_angle in NeXus) as can be seen in :ref:`FigWoniPowderData`. Now, in ``NXdata``, create links to the appropriate
data items in the ``NXinstrument`` hierarchy. In the case of WONI, both parameters live in the ``detector:NXdetector`` group.

Fill in auxiliary Information
=============================

Look at the section on ``NXsample`` in the NeXus reference  manual. Choose appropriate parameters to store for
your samples. Probably at least the name will be needed.

In order to normalize various experimental runs against each other it is necessary to know about the
counting conditions and especially the monitor counts of the monitor used for normalization. The NeXus convention
is to store such information in a ``control:NXmonitor`` group at ``NXentry`` level. Consult the reference for ``NXmonitor`` for
field names. If additional monitors exist within your experiment, they will be stored as additional ``NXmonitor`` groups at
entry level.

Consult the documentation for ``NXentry`` in order to find out under which names to store information such as
titles, user names, experiment times etc.

A more elaborate example of this process can be found in the following section on creating an application definition.

..  ======================================
    section: Creating a NXDL Specification
    ======================================

.. _NXDL_Tutorial-CreatingNxdlSpec:

Creating a NXDL Specification
#############################

An NXDL specification for a NeXus file is required if you desire to standardize  NeXus files from
various sources. Another name for a NXDL description is application definition.
A NXDL specification can be used to verify NeXus files to conform to the standard encapsulated
in the application definition. The process for constructing a NXDL specification is similar to the one described
above for the construction of NeXus files.

One easy way to describe how to store data in the NeXus class
structure and to create a NXDL specification is to work through
an example.  Along the way, we will describe some key decisions
that influence our particular choices of :index:`metadata <metadata>`
selection and data organization.  So, on with the example ...

.. _NXDL_Tutorial-Steps:

Application Definition Steps
============================

With all this introductory stuff out of the way,
let us look at the process required
to define an application definition:

#. *Think!* hard about what has to go into the data file.

#. *Map* the required fields into the NeXus 
   :index:`hierarchy <hierarchy>`

#. *Describe* this map in a NXDL file

#. *Standardize* your definition through
   communication with the NIAC

.. _NXDL_Tutorial-Step1:

Step 1: *Think!* hard about data
================================

This is actually the hard bit. There are two things to consider:

#. What has to go into the data file?

#. What is the normal plot for this type of data?

For the first part, one of the NeXus guiding principles gives us - Guidance!
"A NeXus file must contain all the data necessary for standard data         analysis."

Not more and not less for an application definition.
Of course the definition of *standard* data for analysis
or a *standard* plot
depends on the science and the type of data being described. Consult
senior scientists in the field about this is if you are unsure.
Perhaps you must
call an international meeting with domain experts to haggle that out. When
considering this, people tend to put in everything which might come up. This
is not the way to go.

A key test question is: Is this data item necessary for common data analysis?
Only these necessary data items belong in an application definition.

The purpose of an application definition is that an author of upstream software
who consumes the file can expect certain data items to be there at well defined
places. On the other hand if there is a development in your field which analyzes
data in a novel way and requires more data to do it, then it is better to err
towards the side of more data.

Now for the case of WONI, the standard data analysis is either Rietveld refinement
or profile analysis. For both purposes, the kind of radiation used to probe the
sample (for WONI, neutrons), the wavelength of the radiation,
the monitor (which tells us how long we counted) used to normalize the data,
the counts and the two
theta angle of each detector element are all required. Usually, it is desirable to
know what is being analyzed, so some :index:`metadata <metadata>`
would be nice: a title, the sample
name and the sample temperature. The data typically being plotted is two
theta against counts, as shown in :ref:`FigWoniPowderData` above.
Summarizing, the basic information required from WONI is given next.

.. compound::

	.. _TableWoniBasicInfo:
  
	* *title* of measurement
	* sample *name*
	* sample *temperature*
	* counts from the incident beam *monitor*
	* type of radiation *probe*
	* *wavelength* (:math:`\lambda`) of radiation incident on sample
	* angle (:math:`2\theta` or *two theta*) of detector elements
	* *counts* for each detector element

If you start to worry that this is too little information, hold on, the section
on Using an Application Definition (:ref:`NXDL_Tutorial-UsingNxdl`)
will reveal the secret how to go from an
application definition to a practical file.

.. _NXDL_Tutorial-Step2:

Step 2: *Map* Data into the NeXus Hierarchy
===========================================

This step is actually easier then the first one. We need to map the data items
which were collected in Step 1 into the NeXus :index:`hierarchy <hierarchy>`.
A NeXus file hierarchy
starts with an ``NXentry`` group. At this stage it is advisable to pull up the base
class definition for ``NXentry`` and study it. The first thing you might notice
is that ``NXentry`` contains a field named ``title``. Reading
the documentation, you
quickly realize that this is a good place to store our title. So the first mapping
has been found.

.. code-block:: c

    title = /NXentry/title

.. note:: In this example, the mapping descriptions just contain the path strings
          into the NeXus file hierarchy
          with the class names of the groups to use.  As it turns out, this is
          the syntax used in NXDL link specifications.  How convenient!

Another thing to notice in the ``NXentry`` base class is the existence of a group
of class ``NXsample``. This looks like a great place to store information about the
sample. Studying the ``NXsample`` base class confirms this view and there are two
new mappings:

.. code-block:: c
    :linenos:

    sample name = /NXentry/NXsample/name
    sample temperature = /NXentry/NXsample/temperature

Scanning the ``NXentry`` base class further reveals there can be a
``NXmonitor`` group at this level. Looking up the base class for
``NXmonitor`` reveals
that this is the place to store our monitor information.

.. code-block:: c

    monitor = /NXentry/NXmonitor/data

For the other data items, there seem to be no solutions in ``NXentry``. But
each of these data items describe the instrument in more detail. NeXus stores
instrument descriptions in the ``/NXentry/NXinstrument`` branch of the hierarchy.
Thus, we continue by looking at the definition of the ``NXinstrument`` base class.
In there we find further groups for all possible instrument components. Looking
at the schematic of WONI (:ref:`FigWoniSchematic`),
we realize that there is a source, a monochromator
and a detector. Suitable groups can be found for these components
in ``NXinstrument`` and
further inspection of the appropriate base classes reveals the following further
mappings:

.. literalinclude:: examples/woni-mapping-basic.txt
    :tab-width: 4
    :linenos:
    :language: c

Thus we mapped all our data items into the NeXus hierarchy! What still
needs to be done is to decide upon the content of the ``NXdata``
group in ``NXentry``.
This group describes the data necessary to make a quick plot of the
data. For WONI this is ``counts`` versus ``two theta``.
Thus we add this mapping:

.. literalinclude:: examples/woni-mapping-nxdata.txt
    :tab-width: 4
    :linenos:
    :language: c

The full mapping of WONI data into NeXus is documented in the next table:

============================================== ================================================
WONI data                                      NeXus path
============================================== ================================================
*title* of measurement                         ``/NXentry/title``
sample *name*                                  ``/NXentry/NXsample/name``
sample *temperature*                           ``/NXentry/NXsample/temperature``
*monitor*                                      ``/NXentry/NXmonitor/data``
type of radiation *probe*                      ``/NXentry/MXinstrument/NXsource/probe``
*wavelength* of radiation incident on sample   ``/NXentry/MXinstrument/NXcrystal/wavelength``
*two theta* of detector elements               ``/NXentry/NXinstrument/NXdetector/polar_angle``
*counts* for each detector element             ``/NXentry/NXinstrument/NXdetector/data``
*two theta* of detector elements               ``/NXentry/NXdata/polar_angle``
*counts* for each detector element             ``/NXentry/NXdata/data``
============================================== ================================================

Looking at this table, one might get concerned that the two theta and counts data
is stored in two places and thus duplicated. Stop worrying, this problem is
solved at the NeXus API level.
Typically ``NXdata`` will only hold links to the
corresponding data items in ``/NXentry/NXinstrument/NXdetector``.

In this step problems might occur. The first is that the base class definitions
contain a bewildering number of parameters. This is on purpose: the base
classes serve as dictionaries which define names for most things which possibly
can occur. You do not have to give all that information.
Keep it simple and  only require data that is needed for typical data analysis 
for this type of application.

Another problem which can occur is that you require to store information for which 
there is no name in one of the existing base classes or you have a new instrument 
component for which there is no base class altogether. New fields and base classes 
can be introduced if necessary.

In any case please feel free to contact the NIAC via the mailing list with
questions or suggestions.

.. _NXDL_Tutorial-Step3:

Step 3: *Describe* this map in a NXDL file
==========================================

This is even easier. Some XML editing is necessary. Fire up your XML editor
of choice and open a file. If your XML editor supports XML schema while editing XML, it is worth
to load ``nxdl.xsd``. Now your XML editor can help you to create a proper NXDL
file. As always, the start is an empty template file. This looks like the XML code below.

.. note:: This is just the basic XML for a NXDL definition. 
	It is advisable to change
	some of the documentation strings.

.. compound::

    .. rubric:: NXDL template file

    .. literalinclude:: examples/NX__template__.nxdl.xml
        :tab-width: 4
        :linenos:
        :language: xml

.. index::
   ! single: NXDL template file
   see: template; NXDL template file
   single: definition (NXDL element)
   single: category (NXDL attribute)
   single: name (NXDL attribute)
   single: extends (NXDL attribute)
   single: type (NXDL attribute)
   single: xmlns (NXDL attribute)
   single: xsi:schemaLocation (NXDL attribute)

For example, copy and rename the file to ``NXwoni.nxdl.xml``.
Then, locate the XML root element ``definition`` and change the
``name attribute`` (the XML shorthand for this attribute is
``/definition/@name``) to ``NXwoni``.
Change the ``doc`` as well.

The next thing which needs to be done is adding groups into the definition.
A group is defined by some XML, as in this example:

.. literalinclude:: examples/woni-nxdl-group.nxdl
    :tab-width: 4
    :linenos:
    :language: xml

.. index::
   single: group (NXDL element)
   single: type (NXDL attribute)

The type is the actual NeXus base class this group belongs to. Optionally a
``name`` attribute may be given (default is ``data``).

Next, one needs to include data items, too. The XML for such a data item
looks similar to this:

.. literalinclude:: examples/woni-nxdl-data.nxdl
	:tab-width: 4
	:linenos:
	:language: text

.. index::
   single: doc (NXDL element)
   single: dim (NXDL element)
   single: dimensions (NXDL element)
   single: field (NXDL element)
   single: index (NXDL attribute)
   single: name (NXDL attribute)
   single: rank (NXDL attribute)
   single: type (NXDL attribute)
   single: units (NXDL attribute)
   single: value (NXDL attribute)

The meaning of the ``name`` attribute is intuitive, the ``type`` can be looked 
up in the relevant base class definition. A ``field`` definition can optionally
contain a ``doc`` element which contains a description of the data item. The 
``dimensions`` entry specifies the dimensions of the data set.
The ``size`` attribute in the dimensions
tag sets the :index:`rank <rank>`
of the data, in this example: ``rank="1"``. In the ``dimensions`` group there
must be *rank* ``dim`` fields. Each ``dim`` tag holds two attributes:
``index`` determines
to which dimension this tag belongs, the ``1`` means the first dimension.
The ``value`` attribute then describes the size of the dimension. These can be plain integers,
variables, such as in the example ``ndet`` or even expressions like ``tof+1``.

Thus a NXDL file can be constructed. The full NXDL file for the WONI
example is given in :ref:`NXDL_Tutorial-WoniNxdl`.
Clever readers may have noticed the strong similarity between
our working example ``NXwoni``
and ``NXmonopd`` since they are essentially identical.  Give yourselves
a cookie if you spotted this.

.. _NXDL_Tutorial-Step4:

Step 4: *Standardize* with the NIAC
===================================

Basically you are done. Your first application definition for NeXus is constructed.
In order to make your work a standard for that particular application
type, some more steps are required:

- Send your application definition to the NIAC for review

- Correct your definition per the comments of the NIAC

- Cure and use the definition for a year

- After a final review, it becomes the standard

The NIAC must review an application definition before it is accepted as a
standard. The one year curation period is in place in order to gain practical
experience with the definition and to sort out bugs from Step 1. In this period,
data shall be written and analyzed using the new application definition.

.. _NXDL_Tutorial-WoniNxdl:

Full listing of the WONI Application Definition
===============================================

.. FIXME: can we drop the font size for this example?

.. literalinclude:: classes/applications/NXmonopd.nxdl.xml
    :tab-width: 4
    :linenos:
    :language: xml

.. _NXDL_Tutorial-UsingNxdl:

Using an Application Definition
===============================

The application definition is like an interface for your data file. In practice files
will contain far more information. For this, the extendable capability of NeXus
comes in handy. More data can be added, and upstream software relying on
the interface defined by the application definition can still retrieve the necessary
information without any changes to their code.

NeXus application definitions only standardize classes. You are free to decide
upon names of groups, subject to them matching regular expression for NeXus
name attributes (see the :ref:`regular expression
pattern for NXDL group and field names <RegExpName>`
in the :ref:`Design-Naming` section).
Note the length limit of 63 characters imposed by HDF5.
Please use sensible, descriptive names and separate
multi worded names with underscores.

Something most people wish to add is more :index:`metadata <metadata>`,
for example in order
to index files into a database of some sort. Go ahead, do so, if applicable, scan
the NeXus base classes for standardized names. For metadata, consider to use
the ``NXarchive`` definition. In this context, it is worth to mention that a practical
NeXus file might adhere to more then one application definition. For example,
WONI data files may adhere to both the ``NXmonopd`` and ``NXarchive`` definitions. The
first for data analysis, the second for indexing into the database.

Often, instrument scientists want to store the complete state of their instrument
in data files in order to be able to find out what went wrong if the data is
unsatisfactory. Go ahead, do so, please use names from the NeXus base classes.

Site policy might require you to store the names of all your bosses up to the
current head of state in data files. Go ahead, add as many ``NXuser`` classes as
required to store that information.  Knock yourselves silly over this.

Your Scientific Accounting Department (SAD) may ask of you the preposterous;
to store billing information
into data files. Go ahead, do so if your judgment allows.  Just do not expect the NIAC to
provide base classes for this and do not use the prefix NX for your classes.

In most cases, NeXus files will just have one ``NXentry`` class group. But it
may be required to store multiple related data sets of the results of data analysis
into the same data file. In this case create more entries. Each entry should be
interpretable standalone, i.e. contain all the information of a complete ``NXentry``
class. Please keep in mind that groups or data items which stay constant across
entries can always be linked in.

..  =======================
    section: Processed Data
    =======================

.. _ProcessedData:

Processed Data
##############

.. index::
   NXprocess
   Processed Data

Data reduction and analysis programs are encouraged to store their results in
NeXus data files. As far as the necessary, the normal NeXus 
:index:`hierarchy <hierarchy>`
is to be implemented. In addition, processed data files
must contain a :ref:`NXprocess`
group. This group, that documents and preserves data provenance,
contains the name of the data processing program and the
parameters used to run this program in order to achieve the results stored in
this entry. Multiple processing steps must have a separate entry each.
