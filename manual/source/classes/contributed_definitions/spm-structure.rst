.. _Contributed-Spm-Structure:

===============================
Scanning Probe Microscopy
===============================

.. index::
   Contributed-Spm-Application-Definitions
   Contributed-Spm-Base-Classes

.. _Contributed-Spm-Introduction:

Introduction
############

Set of application definition to describe Scanning Probe Microscopy (SPM) experiments, including:

* Atom Force Microscopy (AFM)
* Scanning Tunneling Microscopy (STM)
* Scanning Tunneling Spectroscopy (STS)

.. _Contributed-Spm-Application-Definitions:

Application Definition
######################

    :ref:`NXspm`:
       An application definition for scanning Probe Microscopy experiments. 
       :ref:`NXspm`, which extends :ref:`NXsensor_scan`, contains the a
       general structure for all SPM experiments.
    :ref:`NXsts`:
         The application definition NXsts for Scanning Tunneling Spectroscopy is 
         to be used for STS experiments. It extends the generic application definition
         :ref:`NXspm`.
    :ref:`NXstm`:
         An application definition for Scanning Tunneling Microscopy experiments,
         extends the generic application definition :ref:`NXspm`.
    :ref:`NXafm`:
         An application definition for Atomic Force Microscopy experiments,
         extends the generic application definition :ref:`NXspm`.

.. _Contributed-Spm-Base-Classes:

Base Classes
############

    :ref:`NXlockin`:
    A base class to describe lock-in amplifiers.

    :ref:`NXbias_spectroscopy`:
    A base class to describe bias spectroscopy measurements to measure I/V curves
    in STS experiment.

    :ref:`NXcantilever_spm`:
    A base class to characterize the cantilevers used in AFM experiments.

    :ref:`NXpiezo_config_spm`:
    A base class to describe the piezo configuration in SPM experiments.

    :ref:`NXpiezoelectric_material`:
    A base class to describe the properties of piezoelectric materials used in
    the cantilever tip.

    :ref:`NXpositioner_spm`:
    A base class to describe PID positioners in SPM experiments.

    :ref:`NXscan_control`:
    A base class to characterize the movement of the scan probe in a multi-dimensional phase space. 