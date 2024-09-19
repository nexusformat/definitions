.. _Mpes-Structure-APP:

=======================================
Photoemission & core-level spectroscopy
=======================================

.. index::
   IntroductionMpes
   MpesAppDef
   MpesBC
   MpesCommonBC
   MpesExtendedBC


.. _IntroductionMpes-APP:

Introduction
############

Set of data storage objects to describe multidimensional photoemission (MPES) experiments including x-ray photoelectron spectroscopy (XPS), ultraviolet photoelectron spectroscopy (UPS),
hard x-ray photoelectron spectroscopy (HAXPES), angle-resolved photoemission spectroscopy (ARPES), two-photon photoemission (2PPE) 
and photoemission electron microscopy (PEEM). Also includes descriptors for advanced specializations, such as spin-resolution, time resolution, 
near-ambient pressure conditions, dichroism etc.

.. _MpesAppDef-APP:

Application Definitions
#######################

:ref:`NXmpes`:
   A general application definition with minimalistic metadata requirements, apt to describe all photoemission experiments.

:ref:`NXmpes_arpes`:
   An application definition for angle-resolved photoemission spectroscopy (ARPES) experiments.

:ref:`NXxps`:
   An application definition for X-ray/ultraviolet photoelectron spectroscopy (XPS/UPS) measurements.

:ref:`NXarpes`:
   An application definition for angle-resolved photoemission spectroscopy (ARPES) experiments. This definition is a legacy 
   support for older NXarpes experiments. For newer experiments, the user is advised to use :ref:`NXmpes_arpes`:.”

