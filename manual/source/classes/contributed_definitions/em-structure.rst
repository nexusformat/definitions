.. _Em-Structure:

===================
Electron microscopy
===================

.. index::
   IntroductionEm
   EmAppDef
   EmBC
   EmAnalysisClasses
   EmExamples

.. _IntroductionEm:

Introduction
############

A set of data schemas is proposed to describe components of an electron microscope and its eventually available focused-ion beam functionalities.
The data schemas were designed from the perspective of how electron microscopes are used by colleagues in the materials-science-branch of electron microscopy.
We realize that the biology-/bio-materials/omics-branch of electron microscopy is eventually in an already more mature state of discussion with respect
to data management practices. In what follows, the focus is on the usage of electron microscopy in condensed-matter physics, chemical physics of solids,
and materials engineering applications. As many of the components of electron microscopes used in the bio-materials communities are the same or at least many
components are very similar, it is likely that the here presented schema definitions can also inspire discussion and exchange with the bio-materials community.
Partner consortia in the German National Research Data Infrastructure are here e.g. NFDI-BioImage, NFDI-Microbiota, NFDI4Health, and e.g. NFDI-Neuro.

Electron microscopes are functionally very customizable tools: Examples include multi-signal/-modal analyses which are frequently realized as on-the-fly computational analyses, regularly switching between GUI-based instrument control, computational steps, and more and more using high-throughput stream-based processing. Also artificial intelligence methods are increasingly used and are becoming more closely interconnected with classical modes of controlling the instrument and perform data processing. A challenge in electron microscopy is that these steps are often executed within commercial integrated control and analysis software. This makes it difficult to keep track of workflows in a technology-partner-agnostic, i.e. interdisciplinary manner.

.. _EmAppDef:

Application Definition NXem
###########################

We acknowledge that it can be difficult to agree on a single application definition which is generally enough applicable yet not unnecessarily complex and useful for applications across a variety of instruments, technology partners, and instrument use cases. In what follows, the proposal conceptualizes first the basic components of an electron microscope and the usual workflow of how an electron microscope is used for collecting data with detectors via probing radiation-specimen-matter interaction mechanisms.

In summary, scientists place a specimen/sample into the microscope, calibrate the instrument, take measurements, and may perform experiments, prepare their specimens with a focused ion beam, calibrate again, and take other measurements, before their session on the instrument ends. In between virtually all of these steps data are collected and stream in from different detectors probing different physical mechanisms of the interaction between electrons or other types of radiation with the specimen.

A microscope session ends with the scientist removing the specimen from the instrument or parking it so that the next user can start a session. Occasionally, service technicians perform calibrations and maintenance which also can be described as a session on the microscope. We have provided base classes to describe these steps and events and an application definition for electron microscopy:

    :ref:`NXem`:
        An application definition which explores the possibilities of research on electron-beam matter interaction with (real or simulated) electron microscopes.


.. _EmBC:

Base Classes
############

The following base classes are proposed to support modularizing the storage of pieces of information related to electron microscopy research:

    :ref:`NXcomponent`:
        A base class to describe components aka devices to building an instrument like a microscope irrespective whether that is a real one or a simulated one.

    :ref:`NXfabrication`:
        A base class to bundle manufacturer/technology-partner-specific details about a component or device of an instrument.

    :ref:`NXcircuit`:
        A base class to describe a logical unit of at least one integrated circuit.

    :ref:`NXebeam_column`:
        A base class serving the possibility to group the components relevant for generating
        and shaping the electron beam.

    :ref:`NXibeam_column`:
        A base class serving the possibility to group the components relevant for generating
        and shaping an ion beam of an instrument to offer focused-ion beam (milling) capabilities.

    :ref:`NXelectromagnetic_lens`:
        A base class to detail an electro-magnetic lens. In practice, an electron microscope has many such lenses. It is possible to specify as many lenses as necessary to represent eventually each single lens of the microscope and thus describe how the lenses are affecting the electron beam. This can offer opportunities for developers of software tools which strive to model the instrument e.g. to create digital twins of the instrument. We understand there is still a way to go with this to arrive there though. Consequently, we suggest to focus first on which details should be collected for a lens as a component so that developers of application definitions can take immediate advantage of this work.

    :ref:`NXdeflector`:
        A base class to describe a component to deflect a beam of charged particles.

    :ref:`NXpump`:
        A base class to describe details about pump(s) as components of an electron microscope.

    :ref:`NXcorrector_cs`, :ref:`NXaberration`:
        Base classes to describe procedures and values for the calibration of aberrations based on
        conventions of different companies active in the field of aberration correction including a base class
        to describe details about corrective lens or compound lens devices which reduce
        (spherical) aberrations of an electron beam.

    :ref:`NXscan_controller`:
        A base class to represent the component of an electron microscope which realizes a controlled deflection
        (and eventually shift, blanking, and/or descanning) of the electron beam to illuminate the specimen in a controlled manner
        This base class can be used to document the scan pattern. The base class focuses mostly on the concept idea that there
        is a component in a microscope which controls eventually multiple other components such as beam deflectors to achieve deflection
        and thus a controlled scanning of the beam over the sample/specimen surface.

    :ref:`NXmanipulator`:
        A base class to describe the stage/specimen holder which offers place for the documentation of the small-scale laboratory functionalities
        which modern stages of electron microscopes typically offer.

    :ref:`NXem_instrument`:
        A base class to group the components that make up an electron microscope.

Contextualizing and defining definitions of reference frames and transformations of these and rotations and orientations defined within such reference frames:

    :ref:`NXcoordinate_system`, :ref:`NXtransformations`:
        Base classes to describe different coordinate systems used and/or to be harmonized
        or transformed into one another and respective transformations.

    :ref:`NXem_event_data`:
        A base class representing a container to hold time-stamped and microscope-state-annotated
        data during a session at an electron microscope.

    :ref:`NXimage`:
        Base classes for storing acquisition details for individual images or stacks of images.

    :ref:`NXspectrum`:
        A base class and specializations comparable to :ref:`NXimage` but for storing spectra.

    :ref:`NXatom`:
        A base class to elements, ions, and clusters of atoms be these charged or not.

    :ref:`NXem_optical_system`:
        A base class to store for now qualitative and quantitative values of frequent interest
        which are affected by the interplay of the components and state of an electron microscope.
        Examples are the semiconvergence angle or the depth of field and depth of focus, the magnification, or the camera length.

    :ref:`NXpeak`:
        A base class to describe peaks mathematically.


.. _EmAnalysisClasses:

Storage of event-base data and results of post-processing
#########################################################

We provide specific base classes which granularize frequently collected or analyzed quantities in specific application fields of electron microscopy to deal
with the situation that there are cases were logical connections between generated data artifacts mainly exist for the fact that the data artifacts were
collected during a workflow of electron microscopy research (e.g. taking measurements and then performing method-specific analyses generating new data and conclusions).
We see a value in granularizing out these pieces of information into own classes. In fact, one limitation of application definitions in NeXus, exactly as it applies for serialization
of information also more generally, is currently that they define a set of constraints on their graph of controlled concepts and terms.

If we take for example diffraction experiments performed with an electron microscope, it is usually the case that (diffraction) patterns are collected in the session at the microscope.
However, all scientifically relevant conclusions are typically drawn later, i.e. through post-processing the collected diffraction (raw) data. These numerical and algorithmic steps
define computational workflows were data from an instance of an application definition such as NXem are used as input but many additional concepts, constraints, and assumptions
are applied without that these demand necessarily changes in the constraints on fields or groups of NXem. If we were to modify NXem for these cases,
NXem would combinatorially diverge as every different combination of required constraints demands having an own but almost similar application definition.
For this reason, method-specific base classes are used which granularize out how specific pieces of information are processed further to eventually enable their
storage (i.e. serialization) using NeXus.

More consolidation through the use of NXsubentry classes should be considered in the future. For now we use an approach whereby base classes are combined to reuse vocabulary and a hierarchical organization of pieces of information with specific constraints which are relevant only for specific usage of such data by specific tools used by an eventually smaller circle of users.

    :ref:`NXem_ebsd`, :ref:`NXem_eds`, :ref:`NXem_eels`, :ref:`NXem_img`:
        Base classes with method-specific details especially when it comes to reporting post-processed data within electron microscopy.

    :ref:`NXphase`, :ref:`NXunit_cell`, :ref:`NXatom`:
        Base classes to store crystal structure specific details e.g. to support simulation of and post-processing of diffraction patterns.

    :ref:`NXcg_roi`:
        A base class to granularize information collected and relevant for the characterization of a region-of-interest.


.. _EMExamples:

Domain-specific data analysis
#############################

    :ref:`NXem_calorimetry`:
        Example together with the IKZ in Berlin and FAIRmat, in-situ (transmission) electron microscopy with a heating stage.
