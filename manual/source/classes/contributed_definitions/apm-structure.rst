.. _Apm-Structure:

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

.. _IntroductionApm:

Introduction
############

Set of data schemas to describe the acquisition, i.e. measurement side, the extraction of hits from detector raw data,
steps to compute mass-to-charge state ratios from uncorrected time of flight data, the reconstruction, and the ranging, i.e. identification of peaks in the mass-to-charge-state ratio histogram to detect (molecular) ions.
The data schemas can be useful to generate data artifacts also for field-ion microscopy experiments.

.. _ApmAppDef:

Application Definition
######################

    :ref:`NXapm`:
       A general application definition with many detailed places for leaving metadata and computational steps described which are commonly used when reporting the measurement of atom probe data including also detector hit data, as well as how to proceed with reconstructing atom positions from these data, and how to store details about definitions made, which describe how mass-to-charge-state ratio values are mapped to iontypes in a process called ranging. The structure of the schema has been designed to also document a simulation of an atom probe
       experiment. Having a combined schema for the measurement and the simulation is beneficial to document that
       there are many similarities between the measurement and a computer simulation of it.

.. _ApmBC:

Base Classes
############

The following base classes are proposed to support modularizing the storage of pieces of information:

    :ref:`NXcoordinate_system_set`, :ref:`NXcoordinate_system`:
        Base classes to describe different coordinate systems used and/or to be harmonized
        or transformed into one another when interpreting the dataset.

    :ref:`NXion`: (about to become replaced by :ref:`NXatom`)
       A base class to describe molecular ions with an adjustable number of atoms/isotopes building each ion.
       For the usage in atom probe research the maximum number of atoms supported building a molecular ion
       is currently set to a maximum of 32. Suggestions made in reference `DOI: 10.1017/S1431927621012241 <https://doi.org/10.1017/S1431927621012241>`_ are used to map isotope to hash values with
       which all possible nuclides (stable, radioactive, or synthetically generated ones) can be described.

    :ref:`NXfabrication`:
        A base class to bundle manufacturer/technology-partner-specific details about
        a component or device of an instrument.

    :ref:`NXpeak`: (about to become complemented by NXpeak_fitting)
        A base class to describe peaks mathematically to detail how peaks in
        mass-to-charge-state ratio histograms (aka mass spectra) are defined and
        labelled as iontypes.

    :ref:`NXpump`:
        A base class to describe details about pump(s) used as components of an instrument.

    :ref:`NXmanipulator`:
        A base class to describe the specimen fixture including the cryo-head.
        Nowadays, stages of microscopes represent small-scale laboratory platforms.
        Therefore, there is a need to define the characteristics of such stages in more detail,
        especially in light of in-situ experiments. Many similarities exists between a stage
        in an electron microscope and one in an atom probe instrument. Both offer fixture
        functionalities and additional components for applying e.g. stimuli on the specimen.

Microscopy experiments, not only taking into account those performed on commercial instruments, offer users to apply a set of
data processing steps. Some of them are frequently applied on-the-fly. For now we represent these steps with specifically named
instances of the :ref:`NXprocess` base class.

Several instances of NXprocess were defined in NXapm to document processing of atom probe data
including hit finding, voltage-and-bowl correction, combinatorial recovery of charge states, reconstruction,
and ranging definitions. These base classes are examples that substantiate that data processing steps are
essential when transforming atom probe measurements or simulations into knowledge. Consequently, these
steps should be documented to enable reproducible research, if possible even numerical reproducibility
of the results,  and to learn better the workflow. In what follows, an example is presented how an
open-source community software can be modified to use descriptions of these computational steps.

A detailed inspection of spatial and other type of filters frequently used in analysis of atom probe
data revealed that it is better to define atom-probe-agnostic reusable concepts for filters:

    :ref:`NXspatial_filter`:
        A base class proposing how a point cloud can be spatially filtered in a specific yet general manner.
        This base class takes advantage of :ref:`NXcg_ellipsoid_set`, :ref:`NXcg_cylinder_set`,
        and :ref:`NXcg_hexahedron_set` to cater for commonly used geometric primitives in atom probe.
        The primitives are used for defining the shape and extent of a region of interest (ROI).

    :ref:`NXsubsampling_filter`:
        A base class for a filter that can also be used for specifying how entries
        like ions can be filtered via sub-sampling.

    :ref:`NXmatch_filter`:
        A base class for a filter that can also be used for specifying how entries
        like ions can be filtered based on their type or other descriptors like hit multiplicity.

The respective research software here is the `paraprobe-toolbox <https://paraprobe-toolbox.readthedocs.io/>`_
The software is developed by `M. Kühbach et al. <https://arxiv.org/abs/2205.13510>`_.
For atom probe research the proposal can also serve as a blue print how computational steps of other software
tool including commercial ones could be developed further to benefit from NeXus.
