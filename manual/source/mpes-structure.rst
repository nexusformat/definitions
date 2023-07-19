.. _Mpes-Structure1:

==============================================
B2/B3: Photoemission & core-level spectroscopy
==============================================

.. index::
   IntroductionMpes1
   MpesAppDef1
   MpesBC1
   MpesCommonBC1
   MpesExtendedBC1


.. _IntroductionMpes1:

Introduction
############

Set of data storage objects to describe photoemission experiments including x-ray photoelectron spectroscopy (XPS), ultraviolet photoelectron spectroscopy (UPS),
hard x-ray photoelectron spectroscopy (HAXPES), angle-resolved photoemission spectroscopy (ARPES), two-photon photoemission (2PPE) 
and photoemission electron microscopy (PEEM). We also included descriptors for advanced specializations, such as spin-resolution, time resolution, 
near-ambient pressure conditions, dichroism etc.

.. _MpesAppDef1:

Application Definitions
#######################

We created two new application definitions:

    :ref:`NXmpes`:
       A general appdef with minimalistic metadata requirements, apt to describe all photemission experiments.

.. _MpesBC1:

Base Classes
############

We developed entirely new base classes:

    :ref:`NXelectronanalyser`:
       A base class to describe electron kinetic energy analizers. Contains the collective characteristics of the instrument such as energy resolution, and includes the following subclasses:

          :ref:`NXcollectioncolumn`:
             Base class to describe the set of electronic lenses in the electron collection column (standard, PEEM, momentum-microscope, etc.).

          :ref:`NXenergydispersion`:
             Base class to describe the energy dispersion sytem (hemispherical, time-of-flight, etc.).

          :ref:`NXspindispersion`:
             Base class to describe the set of electronic lenses in the electron collection column.

    :ref:`NXmanipulator`:
       A base class to describe the complex manipulators used in photoemission experiments, often with > 4 degrees of freedom, 
       cryogenic cooling and other advanced features.

We developed three base classes to describe data processing, which can be used as subclasses of :ref:`NXprocess` if describing post-processing or as subclasses of :ref:`NXdetector` if describing live, electronics level processing:

    :ref:`NXcalibration`:
       A base class to describe the 1D calibration of an axis, with a function mapping a raw data scale to a calibrated scale with the same number of points.

    :ref:`NXdistortion`:
       A base class to describe the 2D distortion correction of an axis, with a matrix mapping a raw data image to a undistorted image.

    :ref:`NXregistration`:
       A base class to describe the rigid transformations that are applied to an image. May be redundant as they can be described with :ref:`NXtransformations`.

.. _MpesCommonBC1:

Common Base Classes
###################

We developed two classes that are common to other techniques:

    :ref:`NXlens_em`:
       A class to describe all types of lenses. Includes electrostatic lenses for electron energy analysers.

    :ref:`NXdeflector`
       A class to describe all kinds of deflectors, including electrostatic and magnetostatic deflectors for electron energy analysers.  

.. _MpesExtendedBC1:

Base Classes Extended in Application Definitions
################################################

We use existent base classes in application definitions and add descriptors:

    :ref:`NXaperture`
       Added fileds to describe analyser apertures and slits.

    :ref:`NXbeam`
       Adedd fields to describe utrafast laser beams.

    :ref:`NXdetector`
       Added fields to describe electron detectors (MCP+Phospor screen, delay lines etc.).

    :ref:`NXentry`
       Added fields to describe an experiment.

    :ref:`NXprocess`
       Added subclasses and collective processing descriptors.

    :ref:`NXsample`
       Added descriptors specific to photoemission experiments.

    :ref:`NXsource`
       Added descriptors for laboratory sources (X-ray, UV lamps) but mostly for ultrafast lasers with complex time structures.

    :ref:`NXinstrument`
      Added descriptors for the overall resolutions of the experiment (energy, momentum, angular, spatial, temporal).
