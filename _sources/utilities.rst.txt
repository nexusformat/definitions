.. _Utilities:

===============
NeXus Utilities
===============

There are many utilities available to read, browse, write, and use NeXus data files. Some
are provided by the NeXus technical group while others are provided by the community. Still,
other tools listed here can read or write one of the low-level file formats used by NeXus (HDF5,
HDF4, or XML).

Furthermore, there are specific examples of code
that can read, write, (or both) NeXus data files, 
given in the section :ref:`language.apis`.


The NIAC welcomes your continued contributions to 
this documentation.

Please note that NeXus maintains a repository of
example data files [#]_ which you may browse and 
download.  There is a cursory analysis [#]_ of every file
in this repository as to whether it can be read as HDF5
or NeXus HDF5.  The analysis code [#]_, which serves as yet
another example reader, is made using python and h5py.

.. [#] https://github.com/nexusformat/exampledata
.. [#] https://github.com/nexusformat/exampledata/blob/master/critique.md
.. [#] https://github.com/nexusformat/exampledata/blob/master/critique.py

..  =============================
    section: Utilities from NeXus
    =============================

.. _Utilities-NeXus:

Utilities supplied with NeXus
#############################

.. index:: utilities
.. index:: programs
.. index:: software

Most of these utility programs are run from the command line. It will be noted if a
program provides a graphical user interface (GUI). Short descriptions are provided here with
links to further information, as available.

.. index:: 
        browser
	nxbrowse (utility)

**nxbrowse**
    NeXus Browser

.. index:: 
        conversion
	nxconvert (utility)

**nxconvert**
    Utility to convert a NeXus file into HDF4/HDF5/XML/...

.. index::
        inspection
	nxdir (utility)

**nxdir**
    ``nxdir`` is a utility for querying 
    a NeXus file about its contents. Full
    documentation can be found by running this command:
    
    .. code-block:: c
    
        nxdir -h

.. index::
        ingestion
	nxingest (utility)

**nxingest**
    ``nxingest`` extracts the metadata from a NeXus file to create an
    XML file according to a mapping file.  The mapping file defines the structure 
    :index:`(names and hierarchy) <hierarchy>` and content (from either the 
    NeXus file, the mapping file or the current time) of the output file. See
    the man page for a description of the mapping file.  This tool uses the  
    :index:`NAPI`.  Thus, any of the supported formats (HDF4, HDF5 and XML)
    can be read.

.. index:: 
	nxsummary 

**nxsummary**
    Use ``nxsummary`` to generate summary of a NeXus file.
    This program relies heavily on a configuration file. Each ``item`` tag
    in the file describes a node to print from the NeXus file. The ``path``
    attribute describes where in the NeXus file to get information from. The
    ``label`` attribute will be printed when showing the value of the
    specified field. The optional ``operation`` attribute provides for certain
    operations to be performed on the data before printing out the result.
    See the source code documentation for more details.

.. index::
	nxtranslate (utility)

**nxtranslate**
    ``nxtranslate`` is
    an anything to NeXus converter. This is accomplished by
    using translation files and a plugin style of architecture where
    ``nxtranslate`` can read from new formats as plugins become available. The
    documentation for ``nxtranslate`` describes its usage by three types of
    individuals:
    
    + the person using existing translation files to create NeXus files
    + the person creating translation files
    + the person writing new *retrievers*
    
    All of these concepts are discussed in detail in the documentation
    provided with the source code.


.. index:: 
   plotting
	NXplot (utility)

**NXplot**
    An extendable utility for plotting any NeXus file.  ``NXplot`` is
    an Eclipse-based GUI project in Java to plot data in NeXus files. (The project was
    started at the first NeXus Code Camp in 2009.)

.. _Utilities-DataAnalysis:

.. index::
   single: software
   single: data analysis software

Validation
##########

The list of applications below are for :ref:`validating <Verification>` NeXus files. 
The list is not intended to be a complete list of all available packages.

.. index::
   validation
   file; validate
   cnxvalidate (utility)

.. _cnxvalidate:

**cnxvalidate**
   NeXus validation tool written in C (not via NAPI).
    
   Its dependencies are libxml2 and the HDF5 libraries, version 1.8.9 or
   better. Its purpose is to validate HDF5 files against NeXus
   application definitions. 

   See the program documentation for more details:
   https://github.com/nexusformat/cnxvalidate.git

.. index::
        validation
   file; validate
   punx (utility)

.. _punx:

**punx**
   Python Utilities for NeXus HDF5 files
   
   **punx** can validate both NXDL files and NeXus HDF5 data files, as
   well as print the structure of any HDF5 file, even non-NeXus files.
    
   NOTE: project is under initial construction, not yet released for
   public use, but is useful in its present form (version 0.2.5).

   **punx** can show the tree structure of any HDF5 file. The output is
   more concise than that from *h5dump*.
    
   See the program documentation for more details:
   https://punx.readthedocs.io

Data Analysis
#############

The list of applications below are some of the utilities that have been 
developed (or modified) to read/write NeXus files
as a data format.  It is not intended to be a complete list of all available packages.

.. index:: 
	DAVE (data analysis software)

**DAVE** (http://www.ncnr.nist.gov/dave/)
    DAVE is an integrated environment for the reduction, visualization and
    analysis of inelastic neutron scattering data. It is built using IDL (Interactive Data
    Language) from ITT Visual Information Solutions.

.. index:: 
	DAWN (data analysis software)

**DAWN** (http://www.dawnsci.org)
    The Data Analysis WorkbeNch (DAWN) project is an eclipse based workbench
    for doing scientific data anaylsis. It offers generic visualisation, 
    and domain specific processing.

.. index:: 
	GDA (data acquisition software)

**GDA** (http://www.opengda.org)
    The GDA project is an open-source framework for creating customised 
    data acquisition software for science facilities such 
    as neutron and X-ray sources. It has elements of the DAWN analysis 
    workbench built in.

.. index:: 
	Gumtree (data analysis software)

**Gumtree** (https://archive.ansto.gov.au/ResearchHub/OurInfrastructure/ACNS/Facilities/Computing/GumTree/index.htm)
    Gumtree  is an open source project, providing a graphical user 
    interface for instrument status and control, data acquisition 
    and data reduction.

.. index:: 
	IDL (data analysis software)

**IDL** (https://www.harrisgeospatial.com/docs/using_idl_home.html)
    IDL is a high-level technical computing language and interactive 
    environment for algorithm development, data visualization, 
    data analysis, and numeric computation.

.. index:: 
	IGOR Pro (data analysis software)

**IgorPro** (http://www.wavemetrics.com/)
    IGOR Pro is an extraordinarily powerful and extensible scientific 
    graphing, data analysis, image processing and programming software 
    tool for scientists and engineers.

.. index:: 
	ISAW (data analysis software)

**ISAW** (ftp://ftp.sns.gov/ISAW/)
    The Integrated Spectral Analysis Workbench software project (ISAW) 
    is a Platform-Independent system Data Reduction/Visualization.
    ISAW can be used to read, manipulate, view, and save neutron 
    scattering data. It reads data from IPNS run files or NeXus files
    and can merge and sort data from separate measurements.

.. index:: 
	LAMP (data analysis software)

**LAMP** (http://www.ill.eu/data_treat/lamp/>)
    LAMP (Large Array Manipulation Program)  is designed for the treatment of 
    data obtained from neutron scattering experiments at the Institut Laue-Langevin. However,
    LAMP is now a more general purpose application which can be seen as 
    a GUI-laboratory for data analysis based on the IDL language.

.. index:: 
	Mantid (data analysis software)

**Mantid** (http://www.mantidproject.org/)
    The Mantid project 
    provides a platform that supports high-performance
    computing on neutron and muon data.  It is being developed as a collaboration between
    Rutherford Appleton Laboratory and Oak Ridge National Laboratory.

.. index:: 
	MATLAB

**MATLAB** (http://www.mathworks.com/)
    MATLAB is a high-level technical computing language and interactive 
    environment for algorithm development, data visualization, 
    data analysis, and numeric computation.

.. index:: 
	NeXpy (data analysis software)

**NeXpy** (http://nexpy.github.io/nexpy/)
    The goal of NeXpy is to provide a simple graphical environment,
    coupled with Python scripting capabilities, for the analysis of X-Ray and
    neutron scattering data.
    (It was decided at the NIAC 2010 meeting that a large portion of this code
    would be adopted in the future by NeXus and be part of the distribution)

.. index:: 
	OpenGENIE (data analysis software)

**OpenGENIE** (http://www.opengenie.org/)
    A general purpose data analysis and visualisation package primarily
    developed at the ISIS Facility, Rutherford Appleton Laboratory.

.. index:: 
	PyMCA (data analysis software)

**PyMCA** (http://pymca.sourceforge.net/)
    PyMca is a ready-to-use, and in many aspects state-of-the-art, 
    set of applications implementing most of the needs
    of X-ray fluorescence data analysis.  It also provides a 
    Python toolkit for visualization and analysis of energy-dispersive
    X-ray fluorescence data.  
    Reads, browses, and plots data from NeXus HDF5 files.

.. index:: 
	spec2nexus

**spec2nexus** (https://spec2nexus.readthedocs.io)
    (Python code) Converts SPEC data files and scans into NeXus HDF5 files.
    (Note the *h5toText* tool mentioned here previously is no longer
    available from the *spec2nexus* project.  The code has been moved
    into the *punx* project: https://punx.readthedocs.io/.)
    
    *spec2nexus* provides libraries:

    * *spec2nexus.spec*: python binding to read SPEC [#]_ data files
    * *spec2nexus.eznx*: (Easy NeXus) supports writing NeXus HDF5 files using h5py

    .. [#] SPEC: http://www.certif.com

.. _HDF-Tools:

HDF Tools
#########

Here are some of the generic tools that are available to work with HDF files.  
In addition to the software listed here there are also
APIs for many programming languages that will allow 
low level programmatic access to the data structures.

.. index:: 
	HDF; tools

**HDF Group command line tools** (http://www.hdfgroup.org/products/hdf5_tools/#h5dist/)
    There are various command line tools that are available from the HDF
    Group, these are usually shipped with the HDF5 kits but are also available for
    download separately.

.. index:: 
	HDFexplorer

**HDFexplorer** (http://www.space-research.org/)
    A data visualization program that reads Hierarchical Data Format 
    files (HDF, HDF-EOS and HDF5) and also netCDF data files.

.. index:: 
	HDFview

**HDFview** (http://www.hdfgroup.org)
    A Java based GUI for browsing (and some basic plotting) of HDF files.

.. _language.apis:

Language APIs for NeXus and HDF5
################################

Collected here are some of the tools identified [#]_ as a result
of a simple question asked at the 2018 Nobugs conference:
*Are there examples of code that reads NeXus data?*
Some of these are very specific to an instrument or application
definition while others are more generic.
The lists below are organized by programming language,
yet some collections span several languages so they are
listed in the section :ref:`language.apis.mixed`.

.. [#] https://github.com/nexusformat/definitions/issues/630

Note these example listed in addition to the many examples described
here in the manual, in section :`Examples`.

.. _language.apis.f77:

Language API: *F77*
+++++++++++++++++++

.. index:: API; F77; POLDI

* **POLDI**: ``poldi.zip`` [#]_ contains:
  - A F77 reading routine using NAPI for POLDI at SINQ PSI
  - an example of a file which it reads

  .. [#] https://github.com/nexusformat/definitions/files/4107360/poldi.zip


.. _language.apis.idl:

Language API: *IDL*
+++++++++++++++++++

.. index:: API; IDL; aXis2000

* **aXis2000** [#]_, with the NeXus-specific IDL code 
  in the ``read_nexus.pro`` [#]_, reads :ref:`NXstxm`

  .. [#] http://unicorn.chemistry.mcmaster.ca/aXis2000.html
  .. [#] ``read_nexus.pro``: http://unicorn.chemistry.mcmaster.ca/axis/aXis2000.zip


.. _language.apis.igorpro:

Language API: *IgorPro*
+++++++++++++++++++++++

.. index:: API; IgorPro; HDF5gateway

* **HDF5gateway** [#]_ makes it easy to read a HDF5 file (including NeXus) into an 
  IgorPro [#]_ folder, including group and dataset attributes, 
  such as a NeXus data file, modify it, and then write 
  the folder structure back out.

  .. [#] https://github.com/prjemian/hdf5gateway
  .. [#] IgorPro: https://wavemetrics.com

.. _language.apis.java:

Language API: *Java*
++++++++++++++++++++

.. index:: API; java; Dawn

* **Dawn** [#]_ has java code to read [#]_ and write [#]_ 
  HDF5 NeXus files (generic NeXus, not tied to 
  specific application definitions). 

  .. [#] https://dawnsci.org/
  .. [#] read: https://github.com/DawnScience/scisoft-core/blob/master/uk.ac.diamond.scisoft.analysis/src/uk/ac/diamond/scisoft/analysis/io/NexusHDF5Loader.java
  .. [#] write: https://github.com/DawnScience/dawnsci/blob/master/org.eclipse.dawnsci.hdf5/src/org/eclipse/dawnsci/hdf5/nexus/NexusFileHDF5.java

.. index:: API; java; NXreader.zip

* ``NXreader.zip`` [#]_ is java code which reads NeXus files into **ImageJ.** 
  It uses the Java-hdf interface to HDF5. It tries to do a good 
  job locating the image dataset by NeXus conventions. 
  But it uses the old style conventions. 

  .. [#] https://github.com/nexusformat/definitions/files/4107439/NXreader.zip


.. _language.apis.python:

Language API: *Python*
++++++++++++++++++++++

.. index:: API; Python; Dials

* **Dials** [#]_ has python (and some C++) code for reading :ref:`NXmx` [#]_

  .. [#] https://dials.github.io/
  .. [#] read: https://github.com/cctbx/dxtbx/blob/master/format/nexus.py

  - *cctbx.xfel* code for writing [#]_ :ref:`NXmx` master files for JF16M at SwissFEL

    .. [#] write: https://github.com/cctbx/cctbx_project/blob/master/xfel/swissfel/jf16m_cxigeom2nexus.py

.. index:: API; Python; h5py

* **h5py** [#]_
	HDF5 for Python (h5py) is a general-purpose Python interface to HDF5.

  .. [#] http://docs.h5py.org

.. index:: API; Python; Mantis

* **Mantis** [#]_, with NeXus-specific python code [#]_, reads :ref:`NXstxm`

  .. [#] Mantis: http://spectromicroscopy.com/
  .. [#] python code: https://bitbucket.org/mlerotic/spectromicroscopy/src/default/

.. index:: API; Python; nexusformat

* **nexusformat** [#]_ NeXus package for Python
    Provides an API to open, create, plot, and manipulate NeXus data.

  .. [#] https://github.com/nexpy/nexusformat

.. index:: API; Python; SasView

* **SasView** [#]_ has python code to read [#]_ and write [#]_ :ref:`NXcanSAS`

  .. [#] https://www.sasview.org/
  .. [#] read: https://github.com/SasView/sasview/blob/master/src/sas/sascalc/dataloader/readers/cansas_reader_HDF5.py
  .. [#] write: https://github.com/SasView/sasview/blob/master/src/sas/sascalc/file_converter/nxcansas_writer.py


.. _language.apis.mixed:

Language API: *mixed*
+++++++++++++++++++++

.. index:: API; mixed; FOCUS

* **FOCUS**: ``focus.zip`` [#]_  contains:

  - An example FOCUS file
  - focusreport: A h5py program which skips through a list of files and prints statistics
  - focusreport.tcl, same as above but in Tcl using the Swig generated binding to NAPI
  - i80.f contains a F77 routine for reading FOCUS files into Ida. The routine is RRT_in_Foc.

  .. [#] https://github.com/nexusformat/definitions/files/4107386/focus.zip

.. index:: API; mixed; ZEBRA

* **ZEBRA**: ``zebra.zip`` [#]_  contains:

  - an example file
  - zebra-to-ascii, a h5py script which dumps a zebra file to ASCII
  - ``TRICSReader.*`` for reading ZEBRA files in C++ using C-NAPI calls

  .. [#] https://github.com/nexusformat/definitions/files/4107416/zebra.zip
