.. _AppDef-Em-Structure:

===================
Electron microscopy
===================

.. index::
   AppDef-Em-Introduction
   AppDef-Em-Definitions

.. _AppDef-Em-Introduction:

Introduction
############

A set of data schemas is available to describe components of an electron microscope (EM) and its potentially available focused-ion beam
functionalities.

Electron microscopes are functionally very customizable tools: Examples include multi-signal/-modal analyses which are frequently realized as
on-the-fly computational analyses, regularly switching between GUI-based instrument control, computational steps, and more and more using
high-throughput stream-based processing. Also artificial intelligence methods are increasingly used and are becoming more closely
interconnected with classical modes of controlling the instrument and perform data processing. A challenge in electron microscopy
is that these steps are often executed within commercial integrated control and analysis software. This makes it difficult to keep
track of workflows in a technology-partner-agnostic, i.e. interdisciplinary manner.

The application definitions and associated base classes were designed from the perspective of how electron microscopes are used in the
materials-science-branch of electron microscopy. Therefore, the focus is on the usage of electron microscopy in condensed-matter physics,
chemical physics of solids, and materials engineering applications.

The biology-/bio-materials/omics-branch of electron microscopy (which also has a mature state of discussion with respect to data
management practices) was not the focus of the original design of the applcation definition. However, as many of the components of electron
microscopes used in the bio-materials communities are the same or at least many components are very similar, it is likely that the application
definition can also inspire discussion and exchange with the bio-materials community.

It is acknowledged that it can be difficult to agree on a single application definition which is generally enough applicable, yet not
unnecessarily complex and useful for applications across a variety of instruments, technology partners, and instrument use cases.

.. _AppDef-Em-Definitions:

Application Definitions
#######################

There currently exists a single application definitions for describing EM experiments:

    :ref:`NXem`:
        An application definition which explores the possibilities of electron microscopes.

The application definition conceptualizes first the basic components of an electron microscope and the usual workflow of how an electron
microscope is used for collecting data with detectors via probing radiation-specimen-matter interaction mechanisms.

In summary, scientists place a specimen/sample into the microscope, calibrate the instrument, take measurements, and may perform experiments,
prepare their specimens with a focused ion beam, calibrate again, and take other measurements, before their session on the instrument ends.
In between almost all of these steps data are collected and stream in from different detectors probing different physical mechanisms of
the interaction between electrons or other types of radiation with the specimen.

A microscope session ends with the scientist removing the specimen from the instrument or parking it so that the next user can start a session.
Occasionally, service technicians perform calibrations and maintenance which also can be described as a session on the microscope.
We have provided base classes to describe these steps and events and an application definition for electron microscopy:


Base classes
#######################

A specific set of base classes which are used in these applcation definitions can be found :ref:`here &lt;BC-EM-Classes&gt;`.