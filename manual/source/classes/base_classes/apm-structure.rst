.. _BC-Apm-Structure:

================================
Atom-probe tomography/microscopy
================================

.. index::
   BC-Apm-Introduction
   BC-Apm-Classes


.. _BC-Apm-Introduction:

Introduction
############

These are a set of base classes to describe atom-probe tomography/microscopy (APT/APM) experiments.

This includes base classes tp describe the acquisition, i.e. measurement side, the extraction of hits from detector raw data,
steps to compute mass-to-charge state ratios from uncorrected time of flight data, the reconstruction, and the ranging,
i.e. identification of peaks in the mass-to-charge-state ratio histogram to detect (molecular) ions.
The base classes can be useful to generate data artifacts also for field-ion microscopy experiments.

Some of the base classes are specific to APM, whereas others are used in other techniques as well.

These base classes are used within the APM-related :ref:`application definitions &lt;AppDef-Apm-Definitions&gt;`

.. _BC-Apm-Classes:

Base Classes
############

    :ref:`NXchamber`:
        A base class to describe a component of the instrument which houses other components.
        A chamber may offer a controlled atmosphere to execute an experiment and/or offer functionalities
        for storing and loading specimens.

    :ref:`NXcoordinate_system`:
        Base class to describe different coordinate systems used and/or to be harmonized
        or transformed into one another when interpreting the dataset.

    :ref:`NXatom`:
       A base class to describe molecular ions with an adjustable number of atoms/isotopes building each ion.
       For the usage in atom probe research the maximum number of atoms supported building a molecular ion
       is currently set to a maximum of 32. Suggestions made in reference `DOI: 10.1017/S1431927621012241 <https://doi.org/10.1017/S1431927621012241>`_ are used to map isotope to hash values with
       which all possible nuclides (stable, radioactive, or synthetically generated ones) can be described.

    :ref:`NXfabrication`:
        A base class to bundle manufacturer/technology-partner-specific details about
        a component or device of an instrument. 

ADD ALL CLASSES HERE