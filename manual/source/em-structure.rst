.. _Em-Structure1:

=======================
B1: Electron microscopy
=======================

.. index::
   IntroductionEm1
   EmAppDef1
   EmBC1
   EmCommonBC1
   EmPartnerClasses1
   EmDeprecated1



.. _IntroductionEm1:

Introduction
############

Set of data storage objects to describe components of an electron microscope and its eventually available focused-ion beam functionalities. The data storage objects were designed from the perspective of how electron microscopes are used by colleagues in the materials-science-branch of electron microscopy. We realize that the biology-/bio-materials/omics-branch of electron microscopy is eventually in an already more mature state of discussion with respect to data management practices. Realizing that we need to start somewhere, though, we focus for now on the condensed-matter physics, chemical physics of solids, and materials science applications of electron microscopy. As many of the components of electron microscopes used in the bio-materials communities are the same or at least many components very similar to those used and described in materials science, we are confident that the here presented schema definitions can also inspire discussion and exchange with the bio-materials community in the future. Partner consortia in the German National Research Data Infrastructure are here NFDI-Microbiota, NFDI4Health, and e.g. NFDI-Neuro.

Electron microscopes are functionally very customizable tools: Examples include multi-signal/-modal analyses which are frequently realized as on-the-fly computational analyses, regularly switching between GUI-based instrument control, computational steps, and more and more using high-throughput stream-based processing. Also artificial intelligence methods get increasingly used and become closer interconnected with classical modes of controlling the instrument and perform data processing. A challenge in electron microscopy is that these steps are often executed within commercial integrated control and analysis software. This makes it additionally difficult to keep track of workflows and challenging to identify which specific quantities in the control software mean and represent in technical detail which physical quantity (and how these
quantities can be connected to the development of ontologies for electron microscopy experiments).

.. _EmAppDef1:

Application Definitions
#######################

We acknowledge that it can be difficult to agree on a single application definition which is generally enough applicable yet remains easy enough and useful across a variety of instruments, technology partners, and instrument use cases. Therefore, we conceptualized first the basic components of an electron microscope and the usual workflow how an electron microscope is used. That is scientists place a specimen/sample into the microscope, calibrate the instrument, take measurements, may perform experiments or prepare their specimens with a focused ion beam, calibrate again, and take other measurements, before their session on the instrument ends. In between virtually all these steps data are collected and stream in from different detectors probing different physical mechanisms of the interaction between electrons or other types of radiation with the specimen. The session ends with the scientist removing
the specimen from the instrument or parking it so that the next user can start a session. Occasionally, service technicians perform calibrations and maintenance which also can be described as session on the microscope. Next, we wrote base classes to describe these steps and events.

    :ref:`NXem`:
        A general application definition which explores the possibilities of electron microscopes.

.. _EmBC1:

Base Classes
############

We developed entirely new base classes. Some of them are also used for other techniques of this proposal but mentioned here for the sake of completeness:


    :ref:`NXaberration_model`, :ref:`NXaberration_model_ceos`, :ref:`NXaberration_model_nion`, :ref:`NXaberration`:
        Base classes to describe procedures and values for the calibration of aberrations based on either CEOS or Nion.

    :ref:`NXaperture_em`:
        A base class to describe an aperture.

    :ref:`NXchamber`:
        A base class to describe the chamber as a part of the microscope or storage unit for transferring specimens in-between or within an instrument.

    :ref:`NXcoordinate_system_set`:
        A base class to describe different coordinate systems used and/or to be harmonized or transformed into one another when interpreting the dataset.

    :ref:`NXcorrector_cs`:
        A base class to describe details about corrective lens or compound lens devices which reduce the aberration of an electron beam.

    :ref:`NXebeam_column`:
        A base class serving the possibility to group the components relevant for generating and shaping the electron beam in an electron microscope.
    
    :ref:`NXevent_data_em`:
        A base class representing a container to hold time-stamped and microscope-state-annotated data during a session at an electron microscope.

    :ref:`NXevent_data_em_set`:
        A base class to group all :ref:`NXevent_data_em` instances.

    :ref:`NXibeam_column`:
        A base class serving the possibility to group the components relevant for generating and shaping an ion beam of an instrument to offer focused ion beam (milling) capabilities.

    :ref:`NXimage_set`:
        Base classes for storing acquisition details for individual images or stacks of images. Specialized versions can be defined and use controlled vocabulary terms for group name prefixes like **adf** annular dark field, **bf** bright field, **bse** backscattered electron, **chamber** camera to monitor the stage and chamber, **df** darkfield, **diffrac** diffraction, **ecci** electron channeling contrast imaging, **kikuchi** electron backscatter diffraction, **ronchigram** - convergent beam diffraction pattern, or **se** secondary electron.

    :ref:`NXinteraction_vol_em`:
        A base class to describe details about e.g. the simulated or known volume of interaction of the electrons with the specimen, especially in scanning electron microscopy.

    :ref:`NXion`:
        A base class to describe charged molecular ions with an adjustable number of atoms/isotopes building each ion. Right now the maximum number of atoms supported building a molecular ion is 32. Suggestions made in reference `DOI: 10.1017/S1431927621012241 <https://doi.org/10.1017/S1431927621012241>`_ are used to map isotope to hash values with which all possible isotopes can be described.

    :ref:`NXlens_em`:
        A base class to detail an electro-magnetic lens. In practice, an electron microscope has many such lenses. It is possible to specify as many lenses as necessary to represent eventually each single lens of the microscope and thus describe how the lenses are affecting the electron beam. This can offer opportunities for developers of software tools which strive to model the instrument e.g. to create digital twins of the instrument. We understand there is still a way to go with this to arrive there though. Consequently, we suggest to focus first on which details should be collected for a lens as a component so that developers of application definitions can take immediate advantage of this work.

    :ref:`NXfabrication`:
        A base class to bundle manufacturer/technology-partner-specific details about a component or device of an instrument.

    :ref:`NXoptical_system_em`:
        A base class to store for now qualitative and quantitative values of frequent interest which are affected by the interplay of the components and state of an electron microscope.
        Examples are the semiconvergence angle or the depth of field and depth of focus, the magnification, or the camera length.

    :ref:`NXpeak`:
        A base class to describe peaks mathematically so that it can be used to detail how peaks in mass-to-charge-state ratio histograms (aka mass spectra) are defined and labelled as iontypes.

    :ref:`NXpump`:
        A base class to describe details about a pump in an instrument.

    :ref:`NXscanbox_em`:
        A base class to represent the component of an electron microscope which realizes a controlled deflection (and eventually shift, blanking, and/or descanning) of the electron beam to illuminate the specimen in a controlled manner. This can be used to document the scan pattern.

    :ref:`NXspectrum_set`:
        Base class and specializations comparable to NXimage_set but for storing spectra. Specialized base classes should use controlled vocabulary items as prefixes such as **eels** electron energy loss spectroscopy, **xray** X-ray spectroscopy (EDS/STEM, EDX, SEM/EDX, SEM/EDS), **auger** Auger spectroscopy, or **cathodolum** for cathodoluminescence spectra.

    :ref:`NXstage_lab`:
        As it was mentioned for atom probe microscopy, this is a base class to describe the stage/specimen holder which offers place for the documentation of the small-scale laboratory functionalities which modern stages of electron microscopes frequently offer.

    :ref:`NXcircuit_board`:, :ref:`NXadc`, and :ref:`NXdac`:
        Base classes to describe electronic components of an electron microscope. These base classes need still to be harmonized with those used in the field of low-temperature scanning probe microscopy.

.. _EmCommonBC1:

Common Base Classes
###################

We support the proposal of our colleagues from photoemission spectroscopy that the :ref:`NXlens_em` and :ref:`NXxraylens` have similarities.
It should be discussed with the NIAC if these classes can be consolidated/harmonized further e.g. eventually become a child class of a more general
base class lenses. We understand also that the proposed set of NXimage_set_em base classes can benefit from future discussion and consolidation efforts.

The first result of such consolidations is the NXem_ebsd partner application definition.

.. _EmPartnerClasses1:

Partner application definitions
###############################

A partner application definition is considered an application definition which stores data and metadata which are relevant for a given experiment but have usually only few connections to the detailed description of the workflow and experiment which motivates to granularize these pieces of information in an own application definition. In fact, one limitation of application definitions in NeXus is that they define a set of constraints on their graph of controlled concepts and terms. If we take for example diffraction experiments with an electron microscope it is usually the case that the pattern are collected in the session at the microscope but all scientifically relevant conclusions are drawn later, i.e. in post-processing of these data. These numerical and algorithmic steps define computational workflows were data from the application definitions such as NXem are used as input but many additional concepts and constraints may apply without any need for changing constraints on fields or groups of NXem. If we were to modify NXem for these cases, NXem would likely combinatorially diverge as every different combination of required constraints trigger the need for having an own but almost similar application definition. For this reason we use the concept of partner application definition which have fields/links where specifically relevant sources of information are connected to e.g. NXem.

The first partner application definition is NXem_ebsd.

    :ref:`NXem_ebsd`:
        Application definition for collecting and indexing Kikuchi pattern into orientation maps for the two-dimensional, three- and four-dimensional case.

Several new base classes are used by this application definition.

    :ref:`NXem_ebsd_conventions`:
        A collection of reference frames and rotation conventions necessary to interpret the alignment and orientation data.

    :ref:`NXem_ebsd_crystal_structure_model`:
        A description of a crystalline phase/structure used for a forward simulation using kinetic or dynamic diffraction theory to generate simulated diffraction pattern against which measured pattern can be indexed.


.. _EmDeprecated1:

Deprecated
##########

In April/May 2023, we refactored the design of the NXimage_set and NXspectrum set base classes. Therefore, the following base classes should not longer be used:
NXimage_set_em_bf, NXimage_set_em_bse, NXimage_set_em_chamber, NXimage_set_em_df, NXimage_set_em_diffrac, NXimage_set_em_ecci, NXimage_set_em_kikuchi, NXimage_set_em_ronchigram, NXimage_set_em_se, NXimage_set_em, NXspectrum_set_em_eels, NXspectrum_set_em_xray, NXspectrum_set_em_auger, NXspectrum_set_em_cathodolum.

With the NeXus 2022.06 Code Camp, we refactored the NXem application definition. Therefore, the following base classes and application definitions should no longer be used:
NXem_nion (replaced by :ref:`NXem`), NXfib (replaced by :ref:`NXibeam_column`).
