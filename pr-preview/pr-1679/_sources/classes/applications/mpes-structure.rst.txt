.. _AppDef-Mpes-Structure:

=======================================
Photoemission & core-level spectroscopy
=======================================

.. index::
   AppDef-Mpes-Introduction
   AppDef-Mpes-Definitions


.. _AppDef-Mpes-Introduction:

Introduction
############

These are a set of application definitions to describe multidimensional photoemission (MPES) experiments including x-ray photoelectron spectroscopy (XPS), ultraviolet photoelectron spectroscopy (UPS),
hard x-ray photoelectron spectroscopy (HAXPES), angle-resolved photoemission spectroscopy (ARPES), two-photon photoemission (2PPE) 
and photoemission electron microscopy (PEEM). Also includes descriptors for advanced specializations, such as spin-resolution, time resolution, 
near-ambient pressure conditions, dichroism etc.

.. _AppDef-Mpes-Definitions:

Application Definitions
#######################

:ref:`NXmpes`
   A general application definition with minimalistic metadata requirements,
   apt to describe all photoemission experiments.

:ref:`NXmpes_arpes`
   An application definition for angle-resolved photoemission spectroscopy (ARPES) experiments.

:ref:`NXxps`
   An application definition for X-ray/UV photoelectron spectroscopy (XPS/UPS) experiments.


:ref:`NXarpes`
   An application definition for angular resolved photo emission spectroscopy.
   Note that this application definition is only kept for legacy reasons and
   new NeXus ARPES files should use :ref:`NXmpes_arpes`.

Base classes
#######################

A specific set of base classes which are used in these application definitions can be found  :ref:`here <bc-mpes-classes>`.
