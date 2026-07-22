.. _BC-Spm-Structure:

=========================
Scanning Probe Microscopy
=========================

.. index::
   BC-Spm-Introduction
   BC-Spm-Classes

.. _BC-Spm-Introduction:

Introduction
############

These are the base classes to describe components of a scanning probe microscope (SPM)
and its associated experimental configurations. These base classes are used within the
SPM-related :ref:`application definitions <AppDef-Spm-Structure>`, specifically in
:ref:`NXspm`, :ref:`NXstm`, :ref:`NXsts`, and :ref:`NXafm`.

.. _BC-Spm-Classes:

Base Classes
############

:ref:`NXamplifier`:
    A base class to describe an amplifier instrument.

:ref:`NXlockin`:
    A base class to describe a lock-in amplifier instrument.

:ref:`NXphase_lock_loop`:
    A base class to describe a phase lock loop in AFM experiments.

:ref:`NXrcs`:
    A base class to describe a remote control system.

:ref:`NXspm_bias_spectroscopy`:
    A base class to describe bias spectroscopy measurement to measure I/V curves in STS experiments.

:ref:`NXspm_cantilever`:
    A base class to characterize the cantilever used in AFM experiments.

:ref:`NXspm_cantilever_config`:
    A base class to describe cantilever configuration in AFM experiments.

:ref:`NXspm_cantilever_oscillator`:
    A base class to describe the cantilever oscillator in AFM experiments.

:ref:`NXspm_piezo_config`:
    A base class to describe piezo configuration in SPM experiments.

:ref:`NXspm_piezo_sensor`:
    A base class to describe a piezo sensor in SPM experiments.

:ref:`NXspm_piezoelectric_material`:
    A base class to describe piezoelectric material properties used in a cantilever tip.

:ref:`NXspm_positioner`:
    A base class to describe a PID positioner in SPM experiments.

:ref:`NXspm_scan_control`:
    A base class to characterize the movement of a scan probe in a multi-dimensional phase space.

:ref:`NXspm_scan_pattern`:
    A base class to define the pattern of a scan in a given scan region.

:ref:`NXspm_scan_region`:
    A base class to define the phase space or sub-phase space for a scan in SPM experiments.

:ref:`NXspm_temperature_sensor`:
    A base class to describe a temperature sensor in SPM experiments.
