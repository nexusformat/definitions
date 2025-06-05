.. _Apm-Structure:

=========================
Atom-probe tomography
=========================

.. index::
   IntroductionApm
   ApmAppDef
   ApmBC


.. _IntroductionApm:

Introduction
##############

Set of data storage objects to describe the acquisition/measurement side, the reconstruction, and the ranging for atom probe microscopy experiments. The data storage objects can be useful as well for field-ion microscopy experiments.

.. _ApmAppDef:

Application Definition
######################

It is proposed to use one application definition to serve atom probe tomography
and field-ion microscopy measurements, i.e. the data collection with the instrument:

    :ref:`NXapm`:
       A general application definition with many detailed places for leaving metadata and computational steps described which are commonly used when reporting the measurement of atom probe data including also detector hit data, as well as how to proceed with reconstructing atom positions from these data, and how to store details about definitions made, which describe how mass-to-charge-state ratio values are mapped to iontypes in a process called ranging.

.. _ApmBC:

Base Classes
############

The following base classes are proposed to support modularizing the storage of pieces of information:

    :ref:`NXcoordinate_system`:
        A base class to describe different coordinate systems used and/or to be harmonized
        or transformed into one another when interpreting the dataset.

    :ref:`NXatom`:
       Base class to describe groups of atoms and charged ions with an adjustable number of atoms/isotopes building each ion.
       Right now the maximum number of atoms supported building a molecular ion is 32.
       Suggestions made in reference `DOI: 10.1017/S1431927621012241 <https://doi.org/10.1017/S1431927621012241>`_ are used
       to map isotope to hash values with which all possible isotopes can be described.

    :ref:`NXchemical_composition`:
       Base class to report the chemical composition of a sample or its parts.

    :ref:`NXcircuit`:
       Base class to describe electronic circuits.

    :ref:`NXinstrument_apm`:
        A base class which defines all modular parts that make up an instrument (real or simulated) for studying
        ion extraction as performed in atom probe and related field-ion microscopy. This base class is used in NXapm in two places:
        One that is placed inside an ENTRY.measurement.instrument
        group. This group holds all those (meta)data which do not change during a session, i.e. instrument name, typically identifier of 
        hardware components or version of control software. Another one that is placed inside an ENTRY.measurements.eventID group.
        This group holds all those (meta)data data change when collecting data during a session.

    :ref:`NXevent_data_apm`:
        A base class representing a container to hold time-stamped and instrument-specific-state-
        annotated data during a session at an electron microscope.

    :ref:`NXroi_process`:
       Base class to report details about results obtained for a specific region of a sample a region-of-interest.

    :ref:`NXcomponent` and :ref:`NXfabrication`:
        Base classes to group frequently used descriptions such as physical parts an is constructed from instrument and
        manufacturing details of it bundling manufacturer/technology-partner-specific details.

    :ref:`NXpeak`:
        A base class to describe peaks mathematically to detail how peaks in
        mass-to-charge-state ratio histograms (aka mass spectra) are
        defined and labelled as iontypes.

    :ref:`NXpump`:
        A base class to describe details about pump(s) of an instrument.

    :ref:`NXmanipulator`:
        A base class to describe the specimen fixture including the cryo-head.
        Nowadays, these stages represent small-scale laboratory platforms.
        Therefore, there is a need to define the characteristics of such stages in more detail,
        especially in light of in-situ experiments. Many similarities exists between a stage
        in an electron microscope and one in an atom probe instrument.
        Both offer fixture functionalities and additional components for applying e.g. stimuli on the specimen.
