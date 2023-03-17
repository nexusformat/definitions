.. _Apm-Structure:

=========================
B5: Atom-probe tomography
=========================

.. index::
   IntroductionAPM
   ApmNewAppDef
   ApmNewBC
   ApmRemovedBC


.. _IntroductionAPM:

Introduction
##############

Set of data storage objects to describe the acquisition/measurement side, the reconstruction, and the ranging for atom probe microscopy experiments. The data storage objects can be useful as well for field-ion microscopy experiments.

.. _ApmNewAppDef:

Application Definitions
#######################

We created one new application definition whose intention is to serve both the description of atom probe tomography and field-ion microscopy measurements:

    :ref:`NXapm`:
       A general application definition with many detailed places for leaving metadata and computational steps described which are commonly used when reporting the measurement of atom probe data including also detector hit data, as well as how to proceed with reconstructing atom positions from these data, and how to store details about definitions made, which describe how mass-to-charge-state ratio values are mapped to iontypes (ranging).

.. _ApmNewBC:

Base Classes
############

We developed new base classes to structure the application definition into lab experiment and computational steps:

    :ref:`NXchamber`:
        A base class to describe a component of the instrument which houses other components. A chamber may offer a controlled atmosphere to execute an experiment and/or offer functionalities for storing and loading specimens.

    :ref:`NXcoordinate_system_set`
        A base class to describe different coordinate systems used and/or to be harmonized or transformed into one another when interpreting the dataset.

    :ref:`NXion`:
       A base class to describe charged molecular ions with an adjustable number of atoms/isotopes building each ion. Right now the maximum number of atoms supported building a molecular ion is 32. Suggestions made in reference `DOI: 10.1017/S1431927621012241 <https://doi.org/10.1017/S1431927621012241>`_ are used to map isotope to hash values with which all possible isotopes can be described.

    :ref:`NXfabrication`:
        A base class to bundle manufacturer/technology-partner-specific details about a component or device of an instrument.

    :ref:`NXpeak`:
        A base class to describe peaks mathematically so that it can be used to detail how peaks in mass-to-charge-state ratio histograms (aka mass spectra) are defined and labelled as iontypes.

    :ref:`NXpump`:
        A base class to describe details about a pump in an instrument.

    :ref:`NXpulser_apm`:
        A base class to describe the high-voltage and/or laser pulsing capabilities of an atom probe microscope.

    :ref:`NXreflectron`:
        A base class to describe a kinetic-energy-sensitive filtering device for time of flight (ToF).

    :ref:`NXstage_lab`:
        A base class to describe the specimen fixture including the cryo-head. This base class is an example that the so far used :ref:`NXstage_lab` base class is insufficiently detailed to represent the functionalities which modern stages of an
        atom probe microscope or especially an electron microscope offer. Nowadays, these stages represent small-scale laboratory platforms. Hence, there is a need to define their characteristics in more detail, especially in light of in-situ experiments. We see many similarities between a stage in an electron microscope and one in an atom probe instrument, given that both offer fixture functionalities and additional components for applying e.g. stimuli on the specimen. For this reason, we use this base class currently for atom probe and electron microscopy.

Microscopy experiments, not only taking into account those performed on commercial instruments, offer the user usually
a set of frequently on-the-fly processed computational data. For now we represent these steps with specifically named instances of the :ref:`NXprocess` base class.

Removed base classes
####################

We have removed the NXlens_apm base class and replaced it by :ref:`NXreflectron`.
We have renamed NXmanufacturer to NXfabrication.
