.. _Em-Structure:

=======================
Electron microscopy
=======================

.. index::
   IntroductionEm
   EmAppDef
   EmBC


.. _IntroductionEm:

Introduction
############


Partner consortia in the German National Research Data Infrastructure are here e.g.
NFDI-MatWerk, NFDI4Ing, NFDI-BioImage, NFDI-Microbiota, NFDI4Health, and e.g. NFDI-Neuro.

Electron microscopes are functionally very customizable tools: Examples include multi-signal/-modal analyses which are frequently realized as on-the-fly computational analyses, regularly switching between GUI-based instrument control, computational steps, and more and more using high-throughput stream-based processing. Also artificial intelligence methods are increasingly used and are becoming more closely interconnected with classical modes of controlling the instrument and perform data processing. A challenge in electron microscopy is that these steps are often executed within commercial integrated control and analysis software. This makes it difficult to keep track of workflows in a technology-partner-agnostic,
i.e. interdisciplinary manner.

.. _EmAppDef:

Application Definitions
#######################

We acknowledge that it can be difficult to agree on a single application definition which is generally enough applicable yet not unnecessarily complex and useful for applications across a variety of instruments, technology partners, and instrument use cases. In what follows, the proposal conceptualizes first the basic components of an electron microscope and the usual workflow of how an electron microscope is used for collecting data with detectors via probing radiation-specimen-matter interaction mechanisms.

In summary, scientists place a specimen/sample into the microscope, calibrate the instrument, take measurements, and may perform experiments, prepare their specimens with a focused ion beam, calibrate again, and take other measurements, before their session on the instrument ends. In between virtually all of these steps data are collected and stream in from different detectors probing different physical mechanisms of the interaction between electrons or other types of radiation with the specimen.

A microscope session ends with the scientist removing the specimen from the instrument or parking it so that the next user can start a session. Occasionally, service technicians perform calibrations and maintenance which also can be described as a session on the microscope. We have provided base classes to describe these steps and events and an application definition for electron microscopy.

    :ref:`NXem`:
        A general application definition which explores the possibilities of electron microscopes.

.. _EmBC:

Base Classes
############

The following base classes are proposed to support modularizing the storage of pieces of information with a focus on EM:

    :ref:`NXaberration`:
        Base class to describe procedures and values for the calibration of aberrations.

    :ref:`NXcoordinate_system_set`:
        A base class to describe different coordinate systems used and/or to be harmonized
        or transformed into one another when interpreting the dataset.

    :ref:`NXcorrector_cs`:
        A base class to describe details about corrective lens or compound lens devices
        which reduce the aberration of an electron beam.

    :ref:`NXebeam_column`:
        A base class serving the possibility to group the components relevant for generating
        and shaping the electron beam.
    
    :ref:`NXevent_data_em`:
        A base class representing a container to hold time-stamped and microscope-state-
        annotated data during a session at an electron microscope.

    :ref:`NXibeam_column`:
        A base class serving the possibility to group the components relevant for generating
        and shaping an ion beam of an instrument to offer focused-ion beam (milling) capabilities.

    :ref:`NXimage`:
        Base class for storing acquisition details for individual images or stacks of images. Specialized versions can be defined and use controlled vocabulary terms for group name prefixes like **adf** annular dark field, **bf** bright field, **bse** backscattered electron, **chamber** camera to monitor the stage and chamber, **df** darkfield, **diffrac** diffraction, **ecci** electron channeling contrast imaging, **kikuchi** electron backscatter diffraction, **ronchigram** - convergent beam diffraction pattern, or **se** secondary electron.

    :ref:`NXinstrument_em`:
        A base class which defines all modular parts that make up an instrument (real or simulated) for studying
        electron matter interaction. This base class is used in NXem in two places: One that is placed inside an ENTRY.measurement.instrument
        group. This group holds all those (meta)data which do not change during a session, i.e. instrument name, typically identifier of 
        hardware components or version of control software. Another one that is placed inside an ENTRY.measurements.events group.
        This group holds all those (meta)data data change when collecting data during a session.

    :ref:`NXion` about to become replaced by :ref:`NXatom`:
        A base class to describe charged molecular ions with an adjustable number of atoms/isotopes building each ion. Right now the maximum number of atoms supported building a molecular ion is 32. Suggestions made in reference `DOI: 10.1017/S1431927621012241 <https://doi.org/10.1017/S1431927621012241>`_ are used to map isotope to hash values with which all possible isotopes can be described.

    :ref:`NXlens_em`:
        A base class to detail an electro-magnetic lens. In practice, an electron microscope has many such lenses. It is possible to specify as many lenses as necessary to represent eventually each single lens of the microscope and thus describe how the lenses are affecting the electron beam. This can offer opportunities for developers of software tools which strive to model the instrument e.g. to create digital twins of the instrument. We understand there is still a way to go with this to arrive there though. Consequently, we suggest to focus first on which details should be collected for a lens as a component so that developers of application definitions can take immediate advantage of this work.

    :ref:`NXfabrication`:
        A base class to bundle manufacturer/technology-partner-specific details about
        a component or device of an instrument.

    :ref:`NXoptical_system_em`:
        A base class to store for now qualitative and quantitative values of frequent interest
        which are affected by the interplay of the components and state of an electron microscope.
        Examples are the semiconvergence angle or the depth of field and depth of focus, the magnification, or the camera length.

    :ref:`NXpeak`:
        A base class to describe peaks mathematically so that it can be used to detail how peaks in mass-to-charge-state ratio histograms (aka mass spectra) are defined and labelled as iontypes.

    :ref:`NXpump`:
        A base class to describe details about a pump in an instrument.

    :ref:`NXscanbox_em`:
        A base class to represent the component of an electron microscope which realizes a controlled deflection (and eventually shift, blanking, and/or descanning) of the electron beam to illuminate the specimen in a controlled manner. This can be used to document the scan pattern.

    :ref:`NXspectrum`:
        Base class and specializations comparable to NXimage_set but for storing spectra. Specialized base classes should use controlled vocabulary items as prefixes such as **eels** electron energy loss spectroscopy, **xray** X-ray spectroscopy (EDS/STEM, EDX, SEM/EDX, SEM/EDS), **auger** Auger spectroscopy, or **cathodolum** for cathodoluminescence spectra.

Method-specific concepts and their usage in application definitions
###################################################################

It became clear during the design of the electron-microscopy-specific additions to NeXus that there are sets of pieces of information (data and metadata) which are relevant for a given experiment but have usually only few connections to the detailed description of the workflow of processing these data into knowledge, motivating the granularization of these pieces of information in their own application definition. In fact, one limitation of application definitions in NeXus is that they define a set of constraints on their graph of controlled concepts and terms. If we take for example diffraction experiments with an electron microscope it is usually the case that (diffraction) patterns are collected in the session at the microscope but all scientifically relevant conclusions are drawn later, i.e. through post-processing these data. These numerical and algorithmic steps define computational workflows where data from the application definitions such as NXem are used as input but many additional concepts and constraints may apply without any need for changing constraints on fields or groups of NXem. If we were to modify NXem for these cases, NXem would likely combinatorially diverge as every different combination of required constraints would demand having their own but almost similar application definition. For this reason, we propose to define the following base classes:

More consolidation through the use of NXsubentry classes should be considered in the future.

    :ref:`NXem_ebsd`, :ref:`NXem_eds`, :ref:`NXem_eels`, :ref:`NXem_img`:
        Base class providing concepts for specific data acquistion modes and associated analysis used in electron microscopy
        such as collecting and indexing Kikuchi pattern into orientation maps for the two-dimensional, three-, X-ray spectrscopy,
        different imaging modes, or electron energy loss spectroscopy (EELS).
