.. _BC-Apm-Structure:

==================================
Atom Probe Microscopy / Tomography
==================================

.. index::
   BC-Apm-Introduction
   BC-Apm-Classes

.. _BC-Apm-Introduction:

Introduction
############

The :ref:`NXapm` application definition uses base classes that describe the acquisition, i.e., the measurement side, the extraction of hits
from detector raw data, processing steps to compute mass-to-charge-state ratios from uncorrected time of flight data, the reconstruction,
and the ranging, i.e., identification of peaks in the mass-to-charge-state ratio histogram to detect (molecular) ions.
The base classes can be useful to generate data artifacts also for field-ion microscopy experiments.

.. _BC-Apm-Classes:

Base Classes
############

:ref:`NXapm_charge_state_analysis`
    Base class to document the parameters, configuration, and results of a processing for recovering

:ref:`NXapm_event_data`
    Base class to store state and (meta)data of events over the course of an atom probe experiment.

:ref:`NXapm_instrument`
    Base class for instrument-related details of a real or simulated

:ref:`NXapm_measurement`
    Base class for collecting a run with a real or a simulated atom probe or field-ion microscope.

:ref:`NXapm_ranging`
    Base class for the configuration and results of ranging definitions.

:ref:`NXapm_reconstruction`
    Base class for the configuration and results of a reconstruction algorithm.

:ref:`NXapm_simulation`
    Base class for simulation of ion extraction from matter via laser and/or voltage

To see a full list of all base classes which NXapm uses, inspect the **Groups cited**
section the :ref:`NXapm` application definition. Consider also the alignment between
the design of the atom-probe- and electron-microscopy-specific definitions that is detailed in :ref:`BC-Em-Structure`.
