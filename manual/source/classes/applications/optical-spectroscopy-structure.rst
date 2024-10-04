.. _Optical-Spectroscopy-Structure-APP:

====================
Optical Spectroscopy
====================

.. index::
   Ellipsometry-APP
   Raman-APP
   DispersiveMaterial-APP


EXAMPLE FOR DOCUMENTATION OF A GROUP OF APPLICATION DEFINITIONS


.. _Ellipsometry-APP:

Ellipsometry
############

Ellipsometry is an optical characterization method to describe optical properties of interfaces and thickness of films.
The measurements are based on determining how the polarization state of light changes upon transmission and reflection.
Interpretation is based on Fresnel equations and numerical models of the optical properties of the materials.

In the application definition, we provide a minimum set of description elements allowing for a reproducible recording of ellipsometry measurements. 

.. _Raman-APP:

Raman
############

Raman spectroscopy is a characterization method to analyze vibrational properties for liquids, gases, or solids. 
The measurements is based on the inelastic light scattering due to the material's vibrations.
Interpretation can be done based on peaks, which represent the phonon properties (intensity, center, width).

The application definition contains a minimum of descriptive elements required to understand Raman spectroscopy measurements.


Application Definitions
-----------------------

    :ref:`NXoptical_spectroscopy`:
       A generic application definition for spectroscopy measurements. This includes in particular ellipsometry and Raman spectroscopy measurements, but also other techniques such as photoluminescence, transmission, and reflection measurements. The requirements are: (i) an incident photon beam, (ii) a detector to measure scattered/emitted photons, and (iii) a sample.

    :ref:`NXellipsometry`:
       An application definition for ellipsometry measurements, including complex systems up to variable angle spectroscopic ellipsometry.

    :ref:`NXraman`:
       An application definition for Raman spectroscopy measurements.

.. _DispersiveMaterial-APP:

Dispersive Material
###################

A dispersive material is a description for the optical dispersion of materials.
This description may be used to store optical model data from an ellipsometric analysis 
(or any other technique) or to build a database of optical constants for optical properties of materials.

Application Definition
----------------------

    :ref:`NXdispersive_material`:
       An application definition to describe the dispersive properties of a material.
       The material may be isotropic, uniaxial or biaxial. Hence, it may contain up
       to three dispersive functions or tables.