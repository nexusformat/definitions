.. _Mpes-Structure-BC:

=======================================
Photoemission & core-level spectroscopy
=======================================

.. index::
   IntroductionMpes
   MpesAppDef
   MpesBC
   MpesCommonBC
   MpesExtendedBC



EXAMPLE FOR DOCUMENTATION OF A GROUP OF BASE CLASSES


.. _IntroductionMpes-BC:

Introduction
############

Set of data storage objects to describe multidimensional photoemission (MPES) experiments including x-ray photoelectron spectroscopy (XPS), ultraviolet photoelectron spectroscopy (UPS),
hard x-ray photoelectron spectroscopy (HAXPES), angle-resolved photoemission spectroscopy (ARPES), two-photon photoemission (2PPE) 
and photoemission electron microscopy (PEEM). Also includes descriptors for advanced specializations, such as spin-resolution, time resolution, 
near-ambient pressure conditions, dichroism etc.

.. _MpesBC-BC:

Base Classes
############

:ref:`NXelectronanalyser`:
   A base class to describe electron kinetic energy analizers. Contains the collective characteristics of the instrument such as energy resolution, and includes the following subclasses:

      :ref:`NXcollectioncolumn`:
         Base class to describe the set of electronic lenses in the electron collection column (standard, PEEM, momentum-microscope, etc.).



Four base classes to describe data processing, which can be used as subclasses of :ref:`NXprocess` if describing post-processing or as subclasses of :ref:`NXdetector` if describing live, electronics level processing:


.. _MpesCommonBC-BC:

Common Base Classes
###################

There are related base classes that are common to other techniques:

