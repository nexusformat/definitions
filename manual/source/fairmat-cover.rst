.. _FairmatCover:

=======================
FAIRmat-NeXus Proposal
=======================

.. index::
   IntroductionCover
   OurScope
   Outreach
   WhichData
   WhatIsNew

Aim
#########################

Experiments nowadays create a set of very often voluminous and diverse numerical data and metadata.
These pieces of information represent entities of what is effectively a graph of materials data.
This graph can have a very large number of nodes and edges representing the large variety of
relations which scientists ideally want to identify and master
when transforming experimental research into knowledge.

Experimentalists face the challenge that these pieces of information come at different levels
of granularity and format, of which many need to be better documented. You have very likely experienced
yourself how file and data formats are routinely encountered tasks to master in your daily
research practice and you might have questioned how these formats are currently handled
when you want to produce FAIR research data and publications.

The NeXus-FAIRmat proposal is an interdisciplinary data science activity initiated by scientists of the
condensed-matter physics community which strives to develop community-maintained open file and data formats
for describing specific experimental techniques, their numerical data and metadata,
and strategies how to exchange these pieces of information.

.. _IntroductionCover:

The FAIRmat proposal to NeXus is an effort by the community of scientists of the `FAIRmat consortium <https://www.fairmat-nfdi.eu/fairmat/about-fairmat/consortium-fairmat>`_
to refine and expand the structure of NeXus. As a project which aims at creating an infrastructure
for experimental data to be findable, accessible, interoperable, and reusable (FAIR) in the fields of
condensed-matter physics and the chemical physics of solids, FAIRmat has adopted NeXus as the common format.

`NeXus <https://www.nexusformat.org/>`_ is a common data exchange format which has its origin in the community of
scientists performing neutron, x-ray, and muon experiments. The development of NeXus is coordinated by the 
NeXus International Advisory Committee (NIAC).
NeXus defines a schema of data entries with a controlled vocabulary and defined relations between the entries.
NeXus offers not only tools to document these schema definitions in a version-controlled manner but
also tools to check and verify how and if specific instances of NeXus schemata comply with the intended
schema definition when the data are written to files. Although, the Hierarchical Data Format (HDF5) is the
most commonly used file format to write NeXus file to, NeXus can also be used with other file formats.

NeXus defines domain-specific rules for organizing data in e.g. HDF5 files (:ref:`application.definitions`)
and defines a dictionary of well-defined domain-specific (a vocabulary) of terms (:ref:`base.class.definitions`).
The meta- and numerical data in a NeXus file represent a hierarchical graph which encodes a specifically
granularized representation of relevant pieces of information and results that should be stored with
an experiment.

Base classes and application definitions are two key components of the NeXus data model.
A base class represents a set of numerical data and metadata which specify details about
scientists, projects, instruments, and other physical devices, including the numerical data
and metadata which are deemed relevant for their description and the associated
computational analyses. Application definitions are constructed from combining such experiment-
and research-question-specifically customized base classes. 

In this combination, an application definition is a data contract between 
a producer and a consumer of these scientific data.

This design has sufficient flexibility to cover any experimental technique and instrumentation, while
ensuring rigorous, application-specific structures that can be processed in an automated manner.

In cases where base classes or application definitions have not yet been proposed advantage of NeXus can be taken
if the respective scientific community explicitly designs, implements, uses, and continuously evolves
these classes and definitions. Here the role of the NIAC is to support the community with
data modeling and data science technical expertise, thus taking an important role of
cross-disciplinary review.

The NeXus-FAIRmat proposal represents the results of this development for experiments and use cases which have not yet used NeXus.
Specifically, the proposal includes cases in the materials-science-branch of electron microscopy (EM), photo-emission spectroscopy, 
ellipsometry, and the field of atom probe tomography and related field-ion microscopy, here jointly referred to as atom probe microscopy.


The documentation available here includes parts of the contents of the NeXus User Manual (also available `here <https://manual.nexusformat.org/user_manual.html>`_),
reported here for the convenience of the user, but is restricted to the parts most pertinent to the our proposal.

For more extensive information, please visit the original manual.

.. _OurScope:

Our scope and perspective
#########################

Thanks to a cooperative approach across a wide variety of experimental techniques,
the NeXus-FAIRmat proposal of the FAIRmat project has an opportunity
to expand the set of data/metadata accurately described via NeXus.

With a closely-connected team of domain experts, we will develop such expansion while at the same time maintaining
a consistent structure across different techniques and methods, striving for the maximum simplicity of use.

Achieving a standardized and FAIR data structure has a wide spectrum of advantages, ranging from radical
progress in scientific transparency to the development of new, far-reaching tools that can be shared across
the whole scientific community. The convenience of such tools can range from guaranteeing data reusability within 
a single lab, to enabling open-source availability of ready-to-use advanced analysis software.

Perhaps the greatest resource, however, is the inclusion of experimental datasets in the `NOMAD Laboratory <https://nomad-lab.eu/about/scope>`_:
a data infrastructure that already hosts the largest computational material science repository in the world, representing a
homogeneous and machine-readable archive, a human-accessible encyclopedia of materials data
with tools for automated artificial intelligence analyses and data access.

.. _Outreach:

Outreach to the community
##########################

A data infrastructure is not effective if it does not integrate seamlessly in the day-to-day workflow of a laboratory.
For this reason, we approach our newly developed NeXus proposal as a community-driven development.
We have drafted an accurate and consistent expansion of NeXus capabilities for a number of lab-based techniques,
but need extensive testing and tweaking of its characteristics by the community.

If your data is generated with these techniques and you are interested in producing FAIR data and accessing the FAIRmat tools, we
invite you to try out our proposed structure. If you find any conflicts or inconsistencies, please raise them to us using the
comment section. These comments are implemented with `Hypothesis <https://web.hypothes.is/>`_, a modern web annotation
tool from the journalism community. The commenting function for each page of the proposal enable you to contribute to the
creation of a more consistent and practical NeXus structure which, in our firm belief, can serve your community and beyond.

If you do not find your specific experimental technique but would be interested in participating in the development
of a standard using NeXus, feel also very much invited to contact us directly at the `FAIRmat-Team <https://www.fair-di.eu/fairmat/about-fairmat/team-fairmat>`_.

.. _WhichData:

Which data should I convert?
############################

You are free to choose at which point in the workflow you wish to convert the data to NeXus, as its flexibility allows to
describe raw data, pre-processed data and fully processed data. As an entry step, we suggest to use a test dataset
that is fully processed and already published (or, alternatively, of negligible scientific content). These datasets, indeed, require often the most 
extensive metadata description, but are most easily converted to NeXus, with minimal to no impact on the data processing pipeline.

In fact, a low barrier (but high yield!) way to participate to FAIRmat consists in converting only fully processed datasets that 
are used for a publication, and publishing them via FAIRmat only when your manuscript is in press. This makes the task of 
converting to NeXus much more sporadic than fairifying raw data, to the point that it may be even acceptable not to automate it. At the same time, 
it guarantees full control on the data until publication. We are confident that if you take this approach, more appetite will come with eating,
and you will be naturally inclined to gradually integrate FAIRmat structures and tools further in your workflow. 


.. _WhatIsNew:

.. What is New?
.. ##############
