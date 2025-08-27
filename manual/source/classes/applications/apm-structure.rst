.. _AppDef-Apm-Structure:

==================================
Atom Probe Microscopy / Tomography
==================================

.. index::
   AppDef-Apm-Introduction
   AppDef-Apm-Definitions

.. _AppDef-Apm-Introduction:

Introduction
############

Set of data schemas to describe the acquisition, i.e. measurement side, the extraction of hits from detector raw data,
steps to compute mass-to-charge state ratios from uncorrected time of flight data, the reconstruction, and the ranging, i.e. identification of peaks in the mass-to-charge-state ratio histogram to detect (molecular) ions.
The data schemas can be useful to generate data artifacts also for field-ion microscopy experiments.

.. _AppDef-Apm-Definitions:

Application Definition
######################

There exists a single application definition to serve atom probe tomography
and field-ion microscopy measurements, i.e. the data collection with the instrument:

    :ref:`NXapm`:
      A general application definition with many detailed places for leaving metadata
      and computational steps described which are commonly used when reporting the
      measurement of atom probe data including also detector hit data, as well as how
      to proceed with reconstructing atom positions from these data, and how to store
      details about definitions made, which describe how mass-to-charge-state ratio
      values are mapped to iontypes in a process called ranging.

Base classes
#######################

A specific set of base classes which are used in the application definition can be found :ref:`here <bc-apm-classes>`.