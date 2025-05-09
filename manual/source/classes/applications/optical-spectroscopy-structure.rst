.. _AppDef-Opt-Spec-Structure:

====================
Optical Spectroscopy
====================

.. index::
   AppDef-Opt-Spec-Ellipsometry
   AppDef-Opt-Spec-Raman
   AppDef-Opt-Spec-Definitions

.. _AppDef-Opt-Spec-Ellipsometry:

Ellipsometry
############

Ellipsometry is an optical characterization method to describe optical properties of interfaces and thickness of films.
The measurements are based on determining how the polarization state of light changes upon transmission and reflection.
Interpretation is based on Fresnel equations and numerical models of the optical properties of the materials.

In the application definition, we provide a minimum set of description elements allowing for a reproducible recording of ellipsometry measurements. 

.. _AppDef-Opt-Spec-Raman:

Raman spectroscopy
############

Raman spectroscopy is a characterization method to analyze vibrational properties for liquids, gases, or solids. 
The measurements is based on the inelastic light scattering due to the material's vibrations.
Interpretation can be done based on peaks, which represent the phonon properties (intensity, center, width).

The application definition contains a minimum of descriptive elements required to understand Raman spectroscopy measurements.

.. _AppDef-Opt-Spec-Definitions:

Application Definitions
-----------------------

    :ref:`NXoptical_spectroscopy`:
       A generic application definition for spectroscopy measurements. This includes in particular ellipsometry and Raman spectroscopy measurements, but also other techniques such as photoluminescence, transmission, and reflection measurements. The requirements are: (i) an incident photon beam, (ii) a detector to measure scattered/emitted photons, and (iii) a sample.

    :ref:`NXellipsometry`:
       An application definition for ellipsometry measurements, including complex systems up to variable angle spectroscopic ellipsometry.

    :ref:`NXraman`:
       An application definition for Raman spectroscopy measurements.

Base classes
#######################

A specific set of base classes which are used in these application definitions can be found :ref:`here &lt;BC-Opt-Spec-Classes&gt;`.