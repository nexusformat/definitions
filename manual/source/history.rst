.. _History:

======================
Brief history of NeXus
======================

Two things to note about the development and history of NeXus:

- All efforts on NeXus have been voluntary except for one year when we had one
  full-time worker.

- The NIAC has already discussed many matters related to the format.

2018-05:
    * `release v2018.5 <https://github.com/nexusformat/definitions/wiki/releasenotes__v2018.5>`
      of NeXus Definitions
    * `#597 <https://github.com/nexusformat/definitions/issues/597>`_
       changed versioning scheme and procedures

2017-07:
    `release 3.3 <https://github.com/nexusformat/definitions/wiki/releasenotes__v3.3>`
    of NeXus Definitions

.. release_3_2: 

2016-10:
    `release 3.2 <https://github.com/nexusformat/definitions/releases/tag/v3.2>`
    of NeXus Definitions

2014-12:
    The NIAC approves a new method to identify the default data to be plotted,
    applying attributes at the group level to the root of the HDF5 tree,
    and the NXentry and NXdata groups. 
    See the description in :ref:`Design-FindPlottable-NIAC2014`
    and the proposal:
    https://www.nexusformat.org/2014_How_to_find_default_data.html

2012-05:
    first release (3.1.0) of NXDL (NeXus Definition Language)

2010-01:
    NXDL presented to ESRF HDF5 workshop on hyperspectral data

2009-09:
    NXDL and draft :index:`NXsas` (base class) presented to canSAS at
    SAS2009 conference

2009-04:
    NeXus API version 4.2.0 is released with additional
    C++, IDL, and python/numpy interfaces.

2008-10:
    :ref:`NXDL` is defined.
    Until now, NeXus used another XML format, meta-DTD, for defining base
    classes and application definitions. There were several problems with meta-DTD,
    the biggest one being that it was not easy to validate against it. NXDL was
    designed to circumvent these problems.  All current base classes and
    application definitions were ported into the NXDL.

2007-10:
    NeXus API version 4.1.0 is released with many bug-fixes.

2007-05:
    NeXus API version 4.0.0 is released with broader support for scripting
    languages and the feature to link with external files.

2005-07:
    The community asked the NeXus team to provide an ASCII based physical file
    format which allows them to edit their scientific results in emacs. This lead to
    the development of a :index:`XML` NeXus physical format. This was released with NeXus API
    version 3.0.0.

2003-10:
    In 2003, NeXus had arrived at a stage where informal gatherings of a group of
    people were no longer good enough to oversee the development of NeXus. This lead
    to the formation of the NeXus International Advisory Committee (:index:`NIAC`) which
    strives to include representatives of all major stake holders in NeXus. A first
    meeting was held at CalTech. Since 2003, the NIAC meets every year to discuss
    all matters NeXus.

2003-06:
    Przemek Klosowski, Ray Osborn, and :index:`Richard Riedel <single: Riedel, Richard>`
    received the only known
    grant explicitly for working on NeXus from  the Systems Integration for Manufacturing
    Applications (SIMA) program of the National Institute of Standards and Technology
    (NIST). The grant funded a person for one year to work on community wide infrastructure
    in NeXus.

2002-09:
    NeXus API version 2.0.0 is released. This version brought support for the new
    version of HDF, :index:`HDF5`, released by the HDF group. HDF4 imposed limits on file
    sizes and the number of objects in a file. These issues were resolved with
    HDF5. The NeXus API abstracted the difference between the two physical file
    formats away form the user.

2001-summer:
    MLNSC at LANL started writing NeXus files to store raw data

1997-07:
    SINQ at PSI started writing NeXus files to store raw data.

1996-10:
    At *SoftNeSS 1996* (at ANL),
    after reviewing the different scientific data formats discussed,
    it was decided to use :index:`HDF4`
    as it provided the best grouping support.
    The basic structure of a NeXus file was agreed upon.
    the various data format proposals were combined into a single document by
    Przemek Klosowski (NIST), Mark Könnecke (then ISIS),
    Jonathan Tischler (ORNL and APS/ANL), and Ray Osborn (IPNS/ANL)
    coauthored the first proposal for the NeXus scientific data
    standard. [#NeXus_Proposal]_

1996-08:
    The HDF-4 API is quite complex. Thus a NeXus Abstract Programmer Interface
    :index:`NAPI`
    was released which simplified reading and writing NeXus files.

1995-09:
    At *SoftNeSS 1995* (at NIST),
    three individual data format proposals by
    :index:`Przemek Klosowski <single: Klosowski, Przemysław>` (NIST),
    Mark Könnecke (then ISIS),
    and Jonathan Tischler (ORNL and APS/ANL)
    were joined to form the basis of the current NeXus format.
    At this workshop, the name *NeXus* was chosen.

1994-10:
    :index:`Ray Osborn <single: Osborn, Raymond>` convened a series of three workshops called
    *SoftNeSS*.
    In the first meeting,
    Mark Könnecke and Jon Tischler were invited to meet with representatives
    from all the major U.S. neutron scattering laboratories
    at Argonne National Laboratory to discuss future software
    development for the analysis and visualization of neutron data.
    One of the main recommendations of *SoftNeSS'94*
    was that a common data format should be developed.

1994-08:
    :index:`Jonathan Tischler <single: Tischler, Jonathan>` (ORNL) proposed an HDF-based format [#aps]_
    as a standard for data storage at APS

1994-06:
    :index:`Mark Könnecke <single: Könnecke, Mark>` (then ISIS, now PSI) made a proposal using netCDF [#netCDF]_
    for the European neutron scattering community while working at ISIS


.. [#NeXus_Proposal] https://www.nexusformat.org/pdfs/NeXus_Proposal.pdf

.. [#aps] https://www.nexusformat.org/pdfs/Proposed_Data_Standard_for_the_APS.pdf

.. [#netCDF] https://www.nexusformat.org/pdfs/European-Formats.pdf


.. comment from here moved to file: history-unpublished-comment.txt
   Keep the file (historical reference) but do not publish.
