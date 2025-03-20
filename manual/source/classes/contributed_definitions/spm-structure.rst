.. _Spm-Structure:

===============================
Scanning Probe Microscopy
===============================

.. index::
   SpmAppDef

.. _SpmAppDef:

Application Definition
######################

    :ref:`NXspm`:
       An application definition for scanning Probe Microscopy domain experiments. 
       The :ref:`NXspm` in herited from the :ref:`NXsensor_scan` is considered as
       a as general structure for all SPM experiments.
    :ref:`NXsts`:
         The application definition NXsts for Scanning Tunneling Spectroscopy is 
         proxy to be used for STS experiments and it is inherited from the :ref:`NXspm`.
         The :ref:`NXsts` is an alias of the :ref:`NXspm` application definition.
    :ref:`NXstm`:
         An application definition for Scanning Tunneling Microscopy experiments 
         inherited from the :ref:`NXspm`.
    :ref:`NXafm`:
         An application definition for Atomic Force Microscopy experiments inherited
         from the :ref:`NXspm`.

.. _SpmNewBC:

Base Classes
############

    :ref:`NXlockin`:
    A base class to describe lock-in amplifier instrument.

    :ref:`NXbias_spectroscopy`:
    A base class to describe bias spectroscopy measurement to measure I/V curve in STS expriment.

    :ref:`NXbias_sweep`:
    A base class to describe bias sweep (a linear voltage vs current scan) step in 
    bias spectroscopy measurement.

    :ref:`NXcantilever_spm`:
    A base class to characterize cantilever used in AFM experiments.

    :ref:`NXpiezo_config_spm`:
    A base class to describe piezo configuration in SPM experiments.

    :ref:`NXpiezoelectric_material`:
    A base class to draw piezoelectric material properties used in cantilever tip.

    :ref:`NXpositioner_spm`:
    A base class to describe PID positioner in SPM experiments.

    :ref:`NXscan_control`:
    A base class to characterize the movement of scan probe in a multi-dimensional phase space. 
