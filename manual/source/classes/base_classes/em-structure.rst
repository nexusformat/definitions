.. _Em-Structure-BC:

===================
Electron microscopy
===================

.. index::
   IntroductionEm
   EmAppDef
   EmBC
   EmAnalysisClasses


EXAMPLE FOR DOCUMENTATION OF A GROUP OF BASE CLASSES


.. _IntroductionEm-BC:

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

.. _EmAppDef-BC:

Application Definitions
#######################

We acknowledge that it can be difficult to agree on a single application definition which is generally enough applicable yet not unnecessarily complex and useful for applications across a variety of instruments, technology partners, and instrument use cases. In what follows, the proposal conceptualizes first the basic components of an electron microscope and the usual workflow of how an electron microscope is used for collecting data with detectors via probing radiation-specimen-matter interaction mechanisms.

In summary, scientists place a specimen/sample into the microscope, calibrate the instrument, take measurements, and may perform experiments, prepare their specimens with a focused ion beam, calibrate again, and take other measurements, before their session on the instrument ends. In between virtually all of these steps data are collected and stream in from different detectors probing different physical mechanisms of the interaction between electrons or other types of radiation with the specimen.

A microscope session ends with the scientist removing the specimen from the instrument or parking it so that the next user can start a session. Occasionally, service technicians perform calibrations and maintenance which also can be described as a session on the microscope. We have provided base classes to describe these steps and events and an application definition for electron microscopy:

    :ref:`NXem`:
        An application definition which explores the possibilities of electron microscopes.


.. _EmBC-BC:

Base Classes
############

The following base classes are proposed to support modularizing the storage of pieces of information related to electron microscopy research:



.. _EmAnalysisClasses-BC:

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

