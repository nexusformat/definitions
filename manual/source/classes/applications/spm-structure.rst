.. _AppDef-Spm-Structure:

===============================
Scanning Probe Microscopy
===============================

.. index::
   CC-SpmAppDef
   CC-SpmNewBC

.. _CC-SpmAppDef:

Scanning probe microscopy (SPM) is a branch of microscopes that forms images of surfaces using a physical probe that scans the specimen.
Using proper instrument setup, SPM can be used to measure various properties of the material surface, such as its topography, magnetic and 
electric properties, and chemical composition.


.. compound::

    .. _STS_STM_instrument_settings:

    .. figure:: ../../img/STS_STM_instrument_settings.png
        :alt: STS_STM_instrument_settings
	   :width: 50%
	   :align: center

        A schematic diagram of Scanning Tunneling Microscopy (STM) and Spectroscopy (STS) setup generate topography image and I/V curve.

The application definition NXspm provides a shared structural framework for capturing essential components such as the instrument configuration, 
experimental, and sample environments, scan data acquired during measurements, and other relevant metadata. The current version aims to ensure that 
fundamental technical elements are inherited consistently across specific experiment types like STM, STS, and AFM.


.. compound::

    .. _SPM-inheritance:

    .. figure:: ../../img/SPM-inheritance.png
        :alt: SPM-inheritance
	   :width: 50%
	   :align: center

        Inheritance relationship among SPM application definitions.

Application Definition
######################

    :ref:`NXspm`:
        An application definition for scanning Probe Microscopy domain experiments.
        The :ref:`NXspm` in herited from the :ref:`NXsensor_scan` is considered as
        a generic structure for all SPM experiments. The App. Def. :ref:`NXsts` is also capable
        to handle :ref:`NXsts` application definition considering STS as a fundamental
        experiment of SPM family.
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

.. _CC-SpmNewBC:

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
