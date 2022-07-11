.. _Em-Structure:

==================================
Electron Microscopy Structure
==================================

.. index::
   IntroductionEM
   EmNewAppDef
   EmNewBC
   EmNewCommonBC
   EmDeprecated



.. _IntroductionEM:

Introduction
##############

Set of data storage objects to describe components of an electron microscope and its eventually available focused-ion beam functionalities. The data storage objects were designed from the perspective of how electron microscopes are used by colleagues in the materials-science-branch of electron microscopy. We realize that the biology-/bio-materials/omics-branch of electron microscopy is eventually in an already more mature state of discussion with respect to data management practices. Realizing that we need to start somewhere, though, we focus for now on the condensed-matter physics, chemical physics of solids, and materials science applications of electron microscopy. As many of the components of the electron microscopes used in the bio-materials communities are the same or at least many components very similar to those used and described in materials science, we are confident that the here presented schema definitions can also inspire discussion and exchange with the bio-materials community in the future.

Electron microscopes are functionally very customizable tools: Examples include multi-signal/-modal analyses which are frequently realized as on-the-fly computational analyses, regularly switching between GUI-based instrument control, computational steps, and more and more using high-throughput stream-based processing. Also artificial intelligence methods get increasingly used and become closer interconnected with those classical instrument control and data processing. A challenge in electron microscopy is that these steps are often executed within commercial integrated control and analysis software, which makes it additionally difficult to keep track of workflows and identify. Not only this it is also often challenging to identify what specific quantities in the control software mean and represent in technical detail and how these
quantities can be connected to the development of ontologies for electron microscopy experiments.

.. _EmNewAppDef:

New Application Definitions
############################

We acknowledge that it can be difficult to agree on a single application definition which is generally enough applicable yet remains easy enough and useful across a variety of instruments, vendors, and instrument use cases. Therefore, we conceptualized first the basic components of an electron microscope and the usual workflow how an electron microscope is used. That is scientists place a specimen/sample into the microscope calibrate the instrument take measurements, may perform experiments or prepare their specimens with a focused ion beam, calibrate again and take other measurements. In between virtually all these steps data are being collected which come from different detectors probing different physical mechanisms of the interaction between electrons with the material of the specimen. The session ends with the scientist removing
the specimen from the instrument or parking it so that the next user can take its time at the instrument. Next, we wrote base classes to describe these steps and events.

    :ref:`NXem`:
       A general application definition which explores the possibilities of electron microscopes.

.. _EmNewBC:

New Base Classes
#################

We developed entirely new base classes. Some of them are also used for other techniques of this proposal but mentioned here for completeness:


    :ref:`NXaberration`:
        A base class to describe detailed parameters of optical models for the aberrations of the microscope.

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
        A base class representing a container to hold time-stamped and microscope-state annotated data during a session at an electron microscope.

    :ref:`NXevent_data_em_set`:
        A base class to group all `NXevent_data_em` instances.

    :ref:`NXibeam_column`:
        A base class serving the possibility to group the components relevant for generating and shape an ion beam of an instrument with focused ion beam capabilities.

    :ref:`NXimage_set_em_adf`:
    :ref:`NXimage_set_em_bf`:
    :ref:`NXimage_set_em_bse`:
    :ref:`NXimage_set_em_chamber`:
    :ref:`NXimage_set_em_df`:
    :ref:`NXimage_set_em_diffrac`:
    :ref:`NXimage_set_em_ecci`:
    :ref:`NXimage_set_em_kikuchi`:
    :ref:`NXimage_set_em_ronchigram`:
    :ref:`NXimage_set_em_se`:
        Base classes for storing acquisition details for individual images or stacks images in different imaging modes.
        Adf - annular dark field
        Bf - bright filed
        Bse - backscattered electron
        Chamber - TV camera to monitor the stage and chamber (e. g. to assure that the specimen does not collides with components in the instrument)
        Df - darkfield
        Diffrac - diffraction image
        Ecci - electron channel contrast imaging
        Kikuchi - Kikuchi diffraction images for electron backscattered electron diffraction (EBSD) for orientation microscopy
        Ronchigram - convergent beam diffraction pattern
        Se - secondary electron

    :ref:`NXinteraction_vol_em`:
        A base class to describe details about e.g. the simulated or known volume of interaction of the electrons with the specimen, especially in scanning electron microscopy.

    :ref:`NXion`:
        A base class to describe charged molecular ions with an adjustable number of atoms/isotopes building each ion. Right now the maximum number of atoms supported building a molecular ion 32. Suggestions made in reference `DOI: 10.1017/S1431927621012241 <https://doi.org/10.1017/S1431927621012241>`_ are used to map isotope to hash values with which all possible isotopes can be described.

    :ref:`NXlens_em`:
        A base class to detail an electro-magnetic lens. In practice, an electron microscope has many such lenses. The idea of this base class is to use it in an application definition. It is possible to specify as many lenses as necessary to represent eventually each single lens of the microscope and thus describe how the lenses are affecting the electron beam. This can offer opportunities for developers of software tool which strive to model the instrument e.g. to create digital twins of the instrument. We understand there is still a way to go with this to arrive there though. Consequently, we suggest to focus first on which details should be collect for a lens as a component so that developers of application definitions can take immediate advantage of this work.

    :ref:`NXmanufacturer`:
        A base class to bundle manufacturer/vendor-specific details about a component or device of an instrument.

    :ref:`NXoptical_system_em`:
        A base class to store for now qualitative and quantitative values of frequent interest which are affected by the interplay of the components and state of an electron microscopy.
        Examples are the semiconvergence angle or the depth of field and depth of focus, the magnification, or the camera length.

    :ref:`NXpeak`:
        A base class to describe peaks mathematically so that it can be used to detail how peaks in mass-to-charge-state ratio histograms (aka mass spectra) are defined and labelled as iontypes.

    :ref:`NXpump`:
        A base class to describe details about a pump in an instrument.

    :ref:`NXscanbox_em`:
        A base class to represent the component of an electron microscope which realizes a controlled deflection (and eventually shift) of the electron beam to illuminate the specimen in a controlled manner. This can be used to document the scan pattern.

    :ref:`NXspectrum_set_em_auger`:
    :ref:`NXspectrum_set_em_cathodolum`:
    :ref:`NXspectrum_set_em_eels`:
    :ref:`NXspectrum_set_em_xray`:
        A base classes comparable to NXimage_set_em but for different techniques resulting in spectra like Auger spectroscopy, cathodoluminescence, electron energy loss spectroscopy and X-ray spectroscopy.

    :ref:`NXstage_lab`:
        As it was mentioned for atom probe microscopy this is a base class to describe the stage/specimen holder which offers place for the documentation of the small-scale laboratory functionalities which modern stages of electron microscopes frequently offer.


.. _EmNewCommonBC:

New Common Base Classes
#######################

We support the proposal of our colleagues from photoemission spectroscopy that the :ref:`NXlens_em` and :ref:`NXxraylens` have similarities.
It should be discussed with the NIAC if these classes can be consolidated/harmonized further e.g. eventually become a child class of a more general
base class lenses. We see understand also that the proposed set of NXimage_set_em base classes can benefit from future discussion and consolidation efforts.


.. _EmDeprecated:

Deprecated
##########

With the results of the NeXus 2022.06 Code Camp the following base classes and application definitions are considered deprecated.
Their functionalities has been extended and is replaced specifically as follows:

    :ref:`NXem_nion`:
        An application definition specific for Nion (transmission) electron microscopes. This is replaced by the substantially more general :ref:`NXem` application definition.
    :ref:`NXfib`:
        A base class to describe focused-ion beam capabilities of an (electron) microscope. The base class is replaced by :ref:`NXibeam_column`.