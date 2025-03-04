.. _Em-Structure-APP:

===================
Electron microscopy
===================

.. index::
   IntroductionEm-APP
   EmAppDef-APP


EXAMPLE FOR DOCUMENTATION OF A GROUP OF APPLICATION DEFINITIONS


.. _IntroductionEm-APP:

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

.. _EmAppDef-APP:

Application Definitions
#######################

We acknowledge that it can be difficult to agree on a single application definition which is generally enough applicable yet not unnecessarily complex and useful for applications across a variety of instruments, technology partners, and instrument use cases. In what follows, the proposal conceptualizes first the basic components of an electron microscope and the usual workflow of how an electron microscope is used for collecting data with detectors via probing radiation-specimen-matter interaction mechanisms.

In summary, scientists place a specimen/sample into the microscope, calibrate the instrument, take measurements, and may perform experiments, prepare their specimens with a focused ion beam, calibrate again, and take other measurements, before their session on the instrument ends. In between virtually all of these steps data are collected and stream in from different detectors probing different physical mechanisms of the interaction between electrons or other types of radiation with the specimen.

A microscope session ends with the scientist removing the specimen from the instrument or parking it so that the next user can start a session. Occasionally, service technicians perform calibrations and maintenance which also can be described as a session on the microscope. We have provided base classes to describe these steps and events and an application definition for electron microscopy:

    :ref:`NXem`:
        An application definition which explores the possibilities of electron microscopes.