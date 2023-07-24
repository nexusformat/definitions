.. _Em-Structure1:

=======================
B1: Electron microscopy
=======================

.. index::
   IntroductionEm1
   EmAppDef1


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

