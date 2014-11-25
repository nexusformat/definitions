.. _History:

======================
Brief history of NeXus
======================

Two things to note about the development and history of NeXus:

- All efforts on NeXus have been voluntary except for one year when we had one
  full-time worker.

- The NIAC has already discussed many matters related to the format.

:June 1994:
    :index:`Mark Könnecke <single: Könnecke, Mark>` (then ISIS, now PSI) made a proposal using netCDF [#]_
    for the European neutron scattering community while working at ISIS

:August 1994:
    :index:`Jonathan Tischler <single: Tischler, Jonathan>` (ORNL) proposed an HDF-based format [#]_
    as a standard for data storage at APS

:October 1994:
    :index:`Ray Osborn <single: Osborn, Raymond>` convened a series of three workshops called
    *SoftNeSS*. [#]_
    In the first meeting,
    Mark Könnecke and Jon Tischler were invited to meet with representatives
    from all the major U.S. neutron scattering laboratories
    at Argonne National Laboratory to discuss future software
    development for the analysis and visualization of neutron data.
    One of the main recommendations of *SoftNeSS'94*
    was that a common data format should be developed.

:September 1995:
    At *SoftNeSS 1995* (at NIST),
    three individual data format proposals by
    :index:`Przemek Klosowski <single: Klosowski, Przemysław>` (NIST),
    Mark Könnecke (then ISIS),
    and Jonathan Tischler (ORNL and APS/ANL)
    were joined to form the basis of the current NeXus format.
    At this workshop, the name *NeXus* was chosen.

:August 1996:
    The HDF-4 API is quite complex. Thus a NeXus Abstract Programmer Interface
    :index:`NAPI`
    was released which simplified reading and writing NeXus files.

:October 1996:
    At *SoftNeSS 1996* (at ANL),
    after reviewing the different scientific data formats discussed,
    it was decided to use :index:`HDF4`
    as it provided the best grouping support.
    The basic structure of a NeXus file was agreed upon.
    the various data format proposals were combined into a single document by
    Przemek Klosowski (NIST), Mark Könnecke (then ISIS),
    Jonathan Tischler (ORNL and APS/ANL), and Ray Osborn (IPNS/ANL)
    coauthored the first proposal for the NeXus scientific data
    standard. [#]_

:July 1997:
    SINQ at PSI started writing NeXus files to store raw data.

:Summer 2001:
    MLNSC at LANL started writing NeXus files to store raw data

:September 2002:
    NeXus API version 2.0.0 is released. This version brought support for the new
    version of HDF, :index:`HDF5`, released by the HDF group. HDF4 imposed limits on file
    sizes and the number of objects in a file. These issues were resolved with
    HDF5. The NeXus API abstracted the difference between the two physical file
    formats away form the user.

:June 2003:
    Przemek Klosowski, Ray Osborn, and :index:`Richard Riedel <single: Riedel, Richard>`
    received the only known
    grant explicitly for working on NeXus from  the Systems Integration for Manufacturing
    Applications (SIMA) program of the National Institute of Standards and Technology
    (NIST). The grant funded a person for one year to work on community wide infrastructure
    in NeXus.

:October 2003:
    In 2003, NeXus had arrived at a stage where informal gatherings of a group of
    people were no longer good enough to oversee the development of NeXus. This lead
    to the formation of the NeXus International Advisory Committee (:index:`NIAC`) which
    strives to include representatives of all major stake holders in NeXus. A first
    meeting was held at CalTech. Since 2003, the NIAC meets every year to discuss
    all matters NeXus.

:July 2005:
    The community asked the NeXus team to provide an ASCII based physical file
    format which allows them to edit their scientific results in emacs. This lead to
    the development of a :index:`XML` NeXus physical format. This was released with NeXus API
    version 3.0.0.

:May 2007:
    NeXus API version 4.0.0 is released with broader support for scripting
    languages and the feature to link with external files.

:October 2007:
    NeXus API version 4.1.0 is released with many bug-fixes.

:October 2008:
    :ref:`NXDL` is defined.
    Until now, NeXus used another XML format, meta-DTD, for defining base
    classes and application definitions. There were several problems with meta-DTD,
    the biggest one being that it was not easy to validate against it. NXDL was
    designed to circumvent these problems.  All current base classes and
    application definitions were ported into the NXDL.

:April 2009:
    NeXus API version 4.2.0 is released with additional
    C++, IDL, and python/numpy interfaces.

.. index:: NXsas (base class)

:September 2009:
    NXDL and draft ``NXsas`` presented to canSAS at
    SAS2009 conference

:January 2010:
    NXDL presented to ESRF HDF5 workshop on hyperspectral data

:May 2012:
    first release (3.1.0) of NXDL (NeXus Definition Language)


.. [#] http://wiki.nexusformat.org/images/b/b8/European-Formats.pdf

.. [#] http://www.neutron.anl.gov/softness

.. [#] http://wiki.nexusformat.org/images/d/d5/Proposed_Data_Standard_for_the_APS.pdf

.. [#] http://wiki.nexusformat.org/images/9/9a/NeXus_Proposal.pdf



.. 2014-08-19,PRJ: removing from published manual by comment
   .. index::
       NXDL
       NeXus Definition Language

   The NeXus Definition Language NXDL
   -----------------------------

   ..  This might be just so much dirty laundry.  Consider removing it.

   This section contains a few brief notes about the history of NXDL
   and the motivations for its creation.

   Previously, the structure of NeXus data files was described using
   *Meta-DTD*, an XML format that provided a compact
   description. The terse format was not obvious to all and was difficult to
   machine-process. NXDL was conceived to be a simpler syntax than Meta-DTD.
   The switch to NXDL was not intended to change what was in the data files, just
   to provide an easier (and more generic) way of describing data files.

   The NeXus Design page lists the group classes from which a NeXus file is
   constructed. They provide the glossary of items that could, in principle, be stored
   in a standard-conforming NeXus file (other items may be inserted into the file if
   the author wishes, but they won't be part of the standard).
   When planning to include a particular piece of
   :index:`metadata`, consult the class definitions
   to find out what to call it. However, to assist those writing data analysis
   software, it is useful to provide more than a glossary; it is important to define
   the required contents of NeXus files that contain data from particular classes of
   neutron, x-ray, or muon instrument.

   As part of the NeXus standard, the NIAC identified a number of generic instruments
   that describe an appreciable number of existing instruments around the world.
   Although not identical in every detail, they share many common characteristics,
   and more importantly, they require sufficiently similar modes of data analysis,
   enough to make a standard description useful.
   Many of the application definitions were built from these instrument definitions
   using the NeXus Definition Language
   (:index:`NXDL`) format.

   Class definitions in NeXus prior to 2008 had been in the form of base classes and
   instrument definitions. All of these were in the same category. As the development
   of NeXus had been led mostly by scientists from neutron sources, this represented
   their typical situations.

   Both those new to NeXus and also those familiar saw the previous emphasis on
   instrument definitions as a deficiency that limited flexibility and possibly usage.
   The point was made that NeXus should attempt to describe better reduced data and
   also data for analysis since synchrotron instruments are rarely adhering to a fixed
   definition.

   The design of NeXus is moving towards an object-oriented approach where the base
   classes will be the objects and the application definitions will use the objects
   to specify the required components as fits some application. Here,
   *application* is
   very loosely defined to include:

   - specification of a scientific instrument (example: TOF-USANS at SNS)

   - specification of what is expected for a scientific technique (example:
     small-angle scattering data for common analysis programs)

   - specification of generic data acquisition stream (example: TOFRAW - raw
     time-of-flight data from a pulsed neutron source)

   - specification of input or output of a specific software program

   ..  The term *the sky is the limit* seems to apply.

   The point of the
   *NeXus Application Definition*
   is that all of these start with ``NX`` and all have
   been approved by the NIAC.

   Those NXDL specifications not yet approved by the NIAC fall into the category of
   *NeXus contributed definitions*
   for which NeXus has a place in the repository.
   Consider the NXDL files in the ``contributed`` directory
   as *in incubation*.
   This category is the place to put an NXDL (a
   candidate for a base class or application definition) for the NIAC to consider
   approving.
