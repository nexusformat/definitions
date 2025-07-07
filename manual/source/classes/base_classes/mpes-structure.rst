.. _BC-Mpes-Structure:

=======================================
Photoemission & core-level spectroscopy
=======================================

.. index::
   BC-Mpes-Introduction
   BC-Mpes-Classes


.. _Mpes-BC-Introduction:

Introduction
############

These are a set of base classes to describe multidimensional photoemission (MPES) experiments including x-ray photoelectron spectroscopy (XPS), ultraviolet photoelectron spectroscopy (UPS),
hard x-ray photoelectron spectroscopy (HAXPES), angle-resolved photoemission spectroscopy (ARPES), two-photon photoemission (2PPE) 
and photoemission electron microscopy (PEEM).

Some of the base classes are specific to MPES (like :ref:`NXelectronanalyzer`), whereas others are used in other techniques as well.

These base clasess are used within the MPES-related :ref:`application definitions &lt;AppDef-Mpes-Definitions&gt;`.

.. _BC-Mpes-Classes:

Base Classes
############

Base classes describing instrument components used in photemission experiments:

:ref:`NXelectronanalyzer`:
   A base class to describe electron kinetic energy analyzers. Contains the collective characteristics of the instrument such as energy resolution, and includes the following classes:

      :ref:`NXcollectioncolumn`:
         Base class to describe the set of electronic lenses in the electron collection column (standard, PEEM, momentum-microscope, etc.).

      :ref:`NXenergydispersion`:
         Base class to describe the energy dispersion system (hemispherical, time-of-flight, etc.).

      :ref:`NXspindispersion`:
         Base class to describe spin filters in photoemission experiments.

      :ref:`NXelectron_detector`:
         Specialization of :ref:`NXdetector` to describe electron detectors used in photoemission experiments.

:ref:`NXmanipulator`:
   A base class to describe the complex manipulators used in photoemission experiments, often with > 4 degrees of freedom, 
   cryogenic cooling and other advanced features.

:ref:`NXlens_em`:
   A class to describe all types of lenses. Includes electrostatic lenses for electron energy analysers.

:ref:`NXdeflector`
   A class to describe all kinds of deflectors, including electrostatic and magnetostatic deflectors for electron energy analysers.

:ref:`NXresolution`:
   Describes the resolution of a physical quantity, e.g. the resolution of the MPES spectrometer.

Base classes (which are subclasses of :ref:`NXprocess`) to describe data (post-)processing:

   :ref:`NXcalibration`:
      Base class to describe the 1D calibration of an axis, with a function mapping a raw data scale to a calibrated scale with the same number of points.

   :ref:`NXdistortion`:
      Base class to describe the 2D distortion correction of an axis, with a matrix mapping a raw data image to a undistorted image.

   :ref:`NXregistration`:
      Base class to describe the rigid transformations that are applied to an image.

   :ref:`NXfit`:
      Base class to describe a fit procedure (e.g., peak fitting in XPS). This comes with its own set of base classes:

      :ref:`NXfit_function`:
         Base class to describe a fit function that is used to fit data to any functional form.

      :ref:`NXpeak`:
         Base class to describe a peak, its functional form, and support values (i.e., the discretization (points) at which the function has been evaluated).