.. _Apm-Structure-BC:

=====================
Atom-probe tomography
=====================

.. index::
   IntroductionApm
   ApmAppDef
   ApmBC
   StatusQuoApm
   ApmParaprobeAppDef
   ApmGermanNfdi


EXAMPLE FOR DOCUMENTATION OF A GROUP OF BASE CLASSES


.. _IntroductionApm-BC:

Introduction
############

Set of data schemas to describe the acquisition, i.e. measurement side, the extraction of hits from detector raw data,
steps to compute mass-to-charge state ratios from uncorrected time of flight data, the reconstruction, and the ranging, i.e. identification of peaks in the mass-to-charge-state ratio histogram to detect (molecular) ions.
The data schemas can be useful to generate data artifacts also for field-ion microscopy experiments.

.. _ApmAppDef-BC:

Application Definition
######################

    :ref:`NXapm`:
       A general application definition with many detailed places for leaving metadata and computational steps described which are commonly used when reporting the measurement of atom probe data including also detector hit data, as well as how to proceed with reconstructing atom positions from these data, and how to store details about definitions made, which describe how mass-to-charge-state ratio values are mapped to iontypes in a process called ranging. The structure of the schema has been designed to also document a simulation of an atom probe
       experiment. Having a combined schema for the measurement and the simulation is beneficial to document that
       there are many similarities between the measurement and a computer simulation of it.

.. _ApmBC-BC:

Base Classes
############

The following base classes are proposed to support modularizing the storage of pieces of information:

    :ref:`NXchamber`:
        A base class to describe a component of the instrument which houses other components.
        A chamber may offer a controlled atmosphere to execute an experiment and/or offer functionalities
        for storing and loading specimens.

    :ref:`NXcoordinate_system_set`:
        Base classes to describe different coordinate systems used and/or to be harmonized
        or transformed into one another when interpreting the dataset.

    :ref:`NXion`:
       A base class to describe molecular ions with an adjustable number of atoms/isotopes building each ion.
       For the usage in atom probe research the maximum number of atoms supported building a molecular ion
       is currently set to a maximum of 32. Suggestions made in reference `DOI: 10.1017/S1431927621012241 <https://doi.org/10.1017/S1431927621012241>`_ are used to map isotope to hash values with
       which all possible nuclides (stable, radioactive, or synthetically generated ones) can be described.

    :ref:`NXfabrication`:
        A base class to bundle manufacturer/technology-partner-specific details about
        a component or device of an instrument.


Microscopy experiments, not only taking into account those performed on commercial instruments, offer users to apply a set of
data processing steps. Some of them are frequently applied on-the-fly. For now we represent these steps with specifically named
instances of the :ref:`NXprocess` base class.

Several base classes were defined to document processing of atom probe data with established algorithms:


These base classes are examples that substantiate that data processing steps are essential to transform atom probe measurements or simulations into knowledge. Therefore, these steps should be documented
to enable reproducible research, if possible even numerical reproducibility of the results, 
and learn how pieces of information are connected. In what follows, an example is presented how an
open-source community software can be modified to use descriptions of these computational steps.

A detailed inspection of spatial and other type of filters frequently used in analysis of atom probe
data revealed that it is better to define atom-probe-agnostic reusable concepts for filters:


The respective research software here is the `paraprobe-toolbox <https://paraprobe-toolbox.readthedocs.io/>`_
The software is developed by `M. Kühbach et al. <https://arxiv.org/abs/2205.13510>`_.
For atom probe research the proposal can also serve as a blue print how computational steps of other software
tool including commercial ones could be developed further to benefit from NeXus.

.. _IntroductionApmParaprobe-BC:

apmtools
########

The paraprobe-toolbox is an example of an open-source parallelized software for analyzing
point cloud data, for assessing meshes in 3D continuum space, and for studying the effects of
parameterization on descriptors of micro- and nanoscale structural features (crystal defects)
within materials when characterized and studied with atom probe.

The need for a thorough documentation of the tools in not only the paraprobe-toolbox
was motivated by several needs:

First, users of software would like to better understand and also be able to study for themselves
which individual parameters and settings for each tool exist and how configuring these
affects analyses quantitatively. This stresses the aspect how to improve documentation.

Second, scientific software like paraprobe-toolbox implement numerical/algorithmical
(computational) workflows whereby data coming from multiple input sources
(like previous analysis results) are processed and carried through more involved analyses
within several steps inside the tool. The tool then creates output as files. This
provenance and workflow should be documented.

Individual tools of paraprobe-toolbox are developed in C/C++ and/or Python.
Provenance tracking is useful as it is one component and requirement for making
workflows exactly numerically reproducible and thus to enable reproducibility (the "R"
of the FAIR principles of data stewardship).

For tools of the paraprobe-toolbox each workflow step is a pair or triple of sub-steps:
1. The creation of a configuration file. 
2. The actual analysis using the Python/or C/C++ tools. 
3. The optional analyses/visualization of the results based on data in NeXus/HDF5 files generated by each tool. 

.. _StatusQuoApm-BC:

What has been achieved so far?
##############################

This proposal summarizes work of members of the FAIRmat project, which is part of the `German
National Research Data Infrastructure <https://www.nfdi.de/?lang=en>`_. The here detailed
proposal documents how all tools of the paraprobe-toolbox were modified to generate
only well-defined configuration files as accepted input and yield specifically formatted output
files according to the following NeXus application definitions.

Data and metadata between the tools are exchanged with NeXus/HDF5 files. This means that data
inside HDF5 binary containers are named, formatted, and hierarchically structured according
to application definitions.

For example the application definition NXapm_paraprobe_config_surfacer specifies
how a configuration file for the paraprobe-surfacer tool should be formatted
and which parameters it contains including optionality and cardinality constraints.

Thereby, each config file uses a controlled vocabulary of terms. Furthermore,
the config files store a SHA256 checksum for each input file. This implements a full
provenance tracking on the input files along the workflow.

As an example, a user may first range their reconstruction and then compute spatial
correlation functions. The config file for the ranging tool stores the files
which hold the reconstructed ion position and ranging definitions.
The ranging tool generates a results file with the labels of each molecular ion.
This results file is formatted according to the tool-specific `results`
application definition. The generated results file and the reconstruction is
imported by the spatial statistics tool which again keeps track of all files
and reports its results in a spatial statistics tool results file.

This design makes it possible to rigorously trace which numerical results were achieved
with specific inputs and settings using specifically-versioned tools. Noteworthy
this includes Y-junction on a graph which is where multiple input sources are
combined to generate new results.

We are convinced that defining, documenting, using, and sharing application definitions
is useful and future-proof strategy for software development and data analyses as it enables
automated provenance tracking which happens silently in the background.

Base classes have been defined to group common pieces of information for each tool of the
toolbox. For each tool we define a pair of base classes. One for the configuration (input) side
and one for the results (output) side:


.. _ApmParaprobeAppDef-BC:

Application Definitions
#######################

NXapm_paraprobe application definitions are in fact pairs of application definitions.
One for the configuration (input) side and one for the results (output) side. For each
tool one such pair is proposed:


.. _ApmGermanNfdi-BC:

Joint work German NFDI consortia NFDI-MatWerk and FAIRmat
#######################################################################

Members of the NFDI-MatWerk and the FAIRmat consortium of the German National Research Data Infrastructure
are working together within the Infrastructure Use Case IUC09 of the NFDI-MatWerk project to work on examples
how software tools in both consortia become better documented and interoperable to use. Within this project,
we have also added the `CompositionSpace tool that has been developed at the Max-Planck-Institut für Eisenforschung
GmbH in Düsseldorf <https://github.com/eisenforschung/CompositionSpace>`_ by A. Saxena et al.

Specifically, within the IUC09 we refactored the code base behind the publication `A. Saxena et al. <https://dx.doi.org/10.1093/micmic/ozad086>`_ to better document its configuration, here as an example implemented like for  the above-mentioned paraprobe-toolbox using NeXus:
 
