.. $Id$

.. _History:

=================================
Brief history of the NeXus format
=================================

Two things to note about the development and history of NeXus:

- All efforts on NeXus have been voluntary except for one year when we had one
  full-time worker.

- The NIAC has already discussed many matters related to the format.

:June 1994:
    Mark Könnecke (then ISIS, now PSI) made a proposal using netCDF [#]_
    for the European neutron scattering community while working at ISIS

:August 1994:
    Jonathan Tischler (ORNL) proposed an HDF-based format [#]_
    as a standard for data storage at APS

:October 1994:
    Ray Osborn convened a series of three workshops called
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
    Przemek Klosowski (NIST),
    Mark Könnecke (then ISIS),
    and Jonathan Tischler (ORNL and APS/ANL)
    were joined to form the basis of the current NeXus format.
    At this workshop, the name *NeXus* was chosen.

:August 1996:
    The HDF-4 API is quite complex. Thus a NeXus Abstract Programmer Interface (NAPI)
    :index:`EDIT_ME <NAPI>`
    was released which simplified reading and writing NeXus files.

:October 1996:
    At *SoftNeSS 1996* (at ANL),
    after reviewing the different scientific data formats discussed,
    it was decided to use HDF-4
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
    version of HDF, HDF-5, released by the HDF group. HDF-4 imposed limits on file
    sizes and the number of objects in a file. These issues were resolved with
    HDF-5. The NeXus API abstracted the difference between the two physical file
    formats away form the user.

:June 2003:
    Przemek Klosowski, Ray Osborn, and Richard Riedel received the only known
    grant explicitly for working on NeXus from  the Systems Integration for Manufacturing
    Applications (SIMA) program of the National Institute of Standards and Technology
    (NIST). The grant funded a person for one year to work on community wide infrastructure
    in NeXus.

:October 2003:
    In 2003, NeXus had arrived at a stage where informal gatherings of a group of
    people were no longer good enough to oversee the development of NeXus. This lead
    to the formation of the NeXus International Advisory Committee (NIAC) which
    strives to include representatives of all major stake holders in NeXus. A first
    meeting was held at CalTech. Since 2003, the NIAC meets every year to discuss
    all matters NeXus.

:July 2005:
    The community asked the NeXus team to provide an ASCII based physical file
    format which allows them to edit their scientific results in emacs. This lead to
    the development of a XML NeXus physical format. This was released with NeXus API
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

:September 2009:
    NXDL and draft ``NXsas`` presented to canSAS at
    SAS2009 conference

:January 2010:
    NXDL presented to ESRF HDF5 workshop on hyperspectral data



.. [#] http://wiki.nexusformat.org/images/b/b8/European-Formats.pdf

.. [#] http://www.neutron.anl.gov/softness

.. [#] http://wiki.nexusformat.org/images/d/d5/Proposed_Data_Standard_for_the_APS.pdf

.. [#] http://wiki.nexusformat.org/images/9/9a/NeXus_Proposal.pdf
