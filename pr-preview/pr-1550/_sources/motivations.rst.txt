.. _MotivationsForNeXus:

==============================================================
Motivations for the NeXus standard in the Scientific Community
==============================================================

.. index::
   ! motivation
   single: why NeXus?
   see: why NeXus?; motivation
   seealso: motivation; plotting
   seealso: motivation; exchange format
   seealso: motivation; format unification
   seealso: motivation; dictionary of terms

..  Today:
    * Lots of different data formats
    * Time wasted converting data
    * Old formats no longer capable of delivering for new high throughput detectors
    * Difficult to add additional data
    * Often, for DA multiple different files needed
    * Badly documented formats
    Tomorrow, with NeXus:
    * Single, efficient, platform independent data format
    * All information in one file
    * Self-describing
    * Extendable

By the early 1990s, several groups of scientists in the fields of neutron and
X-ray science had recognized a common and troublesome pattern in the data acquired
at various scientific instruments and user facilities.  Each of these instruments
and facilities had a locally defined format for recording experimental data.
With lots of different formats, much of the scientists' time was being wasted in
the task of writing import readers for processing and analysis programs.
As is common, the exact information to be documented from each instrument in a
data file evolves, such as the implementation of new high-throughput detectors.
Many of these formats lacked the generality to extend to the
new data to be stored, thus another new format was devised.  In such environments,
the documentation of each generation of data format is often lacking.

Three parallel developments have led to NeXus:

#. *June 1994*:
   :index:`Mark Könnecke <single: Könnecke, Mark>` (Paul Scherer Institute, Switzerland) made a
   proposal using netCDF for the European neutron scattering
   community while working at the ISIS pulsed neutron facility.

#. *August 1994*:
   :index:`Jon Tischler <single: Tischler, Jonathan>` and
   :index:`Mitch Nelson <single: Nelson, Mitchell>` (Oak Ridge National Laboratory, USA)
   proposed an HDF-based format as a standard for data storage at the
   Advanced Photon Source (Argonne National Laboratory, USA).

#. *October 1996*:
   :index:`Przemek Klosowski <single: Klosowski, Przemysław>`
   (National Institute of Standards and Technology, USA)
   produced a first draft of the NeXus proposal drawing on ideas
   from both sources.

These scientists proposed methods to store data using
a self-describing, extensible format that was already in broad use
in other scientific disciplines.
Their proposals formed the basis for the current design of the NeXus
standard which was developed across three workshops organized by Ray Osborn (ANL),
*SoftNeSS'94* (Argonne Oct. 1994),
*SoftNeSS'95* (NIST Sept. 1995),
and *SoftNeSS'96* (Argonne Oct. 1996),
attended by representatives
of a range of neutron and X-ray facilities.
The NeXus API was released in late 1997.
Basic motivations for this standard were:

#. :ref:`SimplePlotting`

#. :ref:`UnifiedFormat`

#. :ref:`DefinedDictionary`

.. _SimplePlotting:

Simple plotting
###############

.. index:: plotting

An important motivation for the design of NeXus was to simplify the creation
of a default plot view.
While the best representation of a set of observations will vary
depending on various conditions, a good suggestion is often known *a
priori*. This suggestion is described in the :ref:`NXdata`
group so that any program that is used to browse NeXus data files can provide a
*best representation* without request for user input.
A description of how simple plotting is facilitated in NeXus is
shown in the section titled :ref:`Find-Plottable-Data`.

NeXus is about how to find and annotate the data to be plotted 
but not to describe how the data is to be plotted.
(https://www.nexusformat.org/NIAC2018Minutes.html#nxdata-plottype--attribute)


.. _UnifiedFormat:

Unified format for reduction and analysis
#########################################

.. index:: format unification

Another important motivation for NeXus, indeed the *raison
d'etre*, was the community need to analyze data from different user
facilities. A single data format that is in use at a variety of facilities
would provide a major benefit to the scientific community. 
This  should
be capable of describing any type of data from the scientific experiments,
at any step of the process from data acquisition to data reduction and analysis.
This unified format also needs to allow data to be written to storage
as efficiently as possible to enable use with high-speed data acquisition.

..  hit these points: Portable, self describing, extendable, public domain

*Self-description*, combined with a reliance on a
*multi-platform* (and thereby *portable*) data
storage format, are valued components of a data storage format where the longevity of
the data is expected to be longer than the lifetime of the facility at which it is
acquired. As the name implies, self-description within data files is the practice where
the structure of the information contained within the file is evident from the file
itself. A multi-platform data storage format must faithfully represent the data
identically on a variety of computer systems, regardless of the bit order or byte order
or word size native to the computer.

The scientific community continues to grow the various types of data to be expressed
in data files. This practice is expected to continue as part of the investigative
process. To gain broad acceptance in the scientific user community, any data storage
format proposed as a standard would need to be
*extendable* and continue to provide a means to express the
latest notions of scientific data.

The maintenance cost of common data structures meeting the motivations above
(self-describing, portable, and extendable) is not insurmountable but is often
well-beyond the research funding of individual members of the muon, neutron, and X-ray
science communities. Since it is these members that drive the selection of a data
storage format, it is necessary for the user cost to be as minimal as possible. In this
case, experience has shown that the format must be in the
*public-domain* for it to be commonly accepted as a standard. A
benefit of the public-domain aspect is that the source code for the API is open and
accessible, a point which has received notable comment in the scientific literature.

..  PRJ: For example, there was a letter to the editor of J Appl Cryst
    in the late 1970s complaining about the increasingly-common practice
    of withholding the source code.  If we find the reference, we should cite it here.

More recently, NeXus has recognized that many facilities face
increased performance requirements and support for writing HDF5 directly in high level 
languages has become better (for example with h5py for Python). For that reason 
HDF5 has become the default recommended storage format for NeXus and the use of the 
NeXus API for new projects is no longer encouraged.
In NeXus has recently defined encoding of information in ways that are not 
compatible with the existing HDF4 and XML container formats (using attribute 
arrays). The move to HDF5 is strongly advised.

For cases where legacy support of the XML or HDF4 storage backends is required
the NeXus API will still be maintained though and provide an upgrade path via the 
utilities to convert between the different backends. 

.. _DefinedDictionary:

Defined dictionary of terms
###########################

.. index:: dictionary of terms, lexicography

A necessary feature of a standard for the interchange of scientific data is 
a ` *defined dictionary* (or *lexicography*) of
terms. This dictionary declares the expected spelling and meaning of terms when they are
present so that it is not necessary to search for all the variant forms of
*energy* when it is used to describe data (e.g., ``E``, ``e``, ``keV``, ``eV``, ``nrg``, ...).

NeXus recognized that each scientific specialty has developed a unique dictionary and
needs to categorize data using those terms.  NeXus Application Definitions provide
the means to document the lexicography for use in data files of that scientific
specialty.

