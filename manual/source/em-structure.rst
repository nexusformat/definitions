.. _Em-Structure:

==================================
Electron Microscopy Structure
==================================

.. index::
   IntroductionEM
   EmNewAppDef
   EmNewBC
   EmNewCommonBC



.. _IntroductionEM:

Introduction
##############

Set of data storage objects to describe components of an electron microscope and its eventually available focused-ion beam functionalities. The data storage objects were designed from the perspective of how electron microscopes are used by colleagues in the materials-science-branch of electron microscopy. We realize that the biology-/bio-materials/omics-branch of electron microscopy is eventually in an already more mature state of discussion with respect to data management practices. Realizing that we need to start somewhere, though, we focus for now on the condensed-matter physics, chemical physics of solids, and materials science applications of electron microscopy. As many of the components of the electron microscopes used in the bio-materials communities are the same or at least many components very similar to those used and described in materials science, we are confident the here presented data storage objects can also inspire discussion and exchange with the bio-materials community in the future.

Electron microscopes are functionally very customizable tools: Examples include multi-signal/-modal analyses which are frequently realized as on-the-fly computational analyses, regularly switching between GUI-based instrument control, computational steps, and more and more using high-throughput stream-based processing. Also artificial intelligence methods get increasingly used and become closer interconnected with those classical instrument control and data processing. A challenge in electron microscopy is that these steps are often executed within commercial integrated control and analysis software, which makes it additionally difficult to keep track of workflows and identify what conceptually the specific quantities in the control software display represent and how these can be connected to the development of ontologies for electron microscopy experiments.

.. _EmNewAppDef:

New Application Definitions
############################

We acknowledge that it can be difficult to agree on a single application definition which is generally enough applicable yet remains easy enough and useful across a variety of instruments, vendors, and instrument use cases. Therefore, we conceptualized first the basic components of an electron microscope. Next, we wrote base classes to describe these and then started to work on two fronts to arrive at specific application definitions. For now we focus on NXem_nion:

    :ref:`NXem_nion`:
       A general application definition which explores the possibilities of scanning transmission electron microscopes that use an open instrument control and analysis software. Specifically, we draft the application for users of Nion microscopes. An extension to supporting multi-signal sources is currently explored and will be implemented with the next release of the application definition.

.. _EmNewBC:

New Base Classes
#################

We developed entirely new base classes:

    :ref:`NXcorrector_cs`:
       A base class to describe the instrument components which correct spherical distortions.

    :ref:`NXfib`:
        A base class which represents the components of a focused-ion beam column of an electron microscope as well as serves as a place for storing details of the control software. We envision this base class to be used as an add-on to customize an application definition for an (electron) microscope with focused-ion beam capabilities.

    :ref:`NXlens_em`:
        A base class to detail an electro-magnetic lens. In practice, an electron microscope has many such lenses. The idea of this base class is to use it in an application definition. It is possible to specify as many lenses as necessary to represent eventually each single lens of the microscope and thus describe how the lenses are affecting the electron beam. This can offer opportunities for developers of software tool which strive to model the instrument e.g. to create digital twins of the instrument. We understand there is still a way to go with this to arrive there though. Consequently, we suggest to focus first on which details should be collect for a lens as a component so that developers of application definitions can take immediate advantage of this work.

    :ref:`NXscanbox_em`:
        A base class to represent the component of an electron microscope which realizes a controlled deflection (and eventually shift) of the electron beam to illuminate the specimen in a controlled manner. This can be used to document the scan pattern.

    :ref:`NXstage_lab`:
        As it was mentioned for atom probe microscopy this is a base class to describe the stage/specimen holder which offers place for the documentation of the small-scale laboratory functionalities which modern stages of electron microscopes frequently offer.

.. _EmNewCommonBC:

New Common Base Classes
#######################

We support the proposal of our colleagues from photoemission spectroscopy that the :ref:`NXlens_em`, :ref:`NXlens`, and :ref:`NXxraylens` have similarities. It should be discussed with the NIAC if these classes can be consolidated/harmonized further e.g. eventually become a child class of a more general base class lenses.
