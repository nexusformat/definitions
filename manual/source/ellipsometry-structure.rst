.. _Ellipsometry-Structure:

=======================
Ellipsometry Structure
=======================

.. index::
   IntroductionEllipsometry
   EllNewAppDef
   EllExtendedBC


.. _IntroductionEllipsometry:

Introduction
##############

Ellipsometry is an optical characterization method to describe optical properties of interfaces and thickness of films. The measurements are based on determining how the polarization state of light changes upon transmission and reflection. Interpretation is based on Fresnel equations and numerical models of the optical properties of the materials.

In the application definition we provide a minimum set of description elements allowing for a reproducible recording of ellipsometry measurements. 

.. _EllNewAppDef:

New Application Definitions
############################

We created one application definition:

    :ref:`NXellipsometry`:
       A general application definition for ellipsometry measurements, including complex systems up to variable angle spectroscopic ellipsometry. 

.. .. _NewBC:

.. EllNew Base Classes
.. ####################

.. We developed entirely new base classes:

..   :ref:`NXelectronanalyser`:
..      A base class to describe...

.. New Common Base Classes
.. #######################

.. We developed two classes that are common to other techniques:

    :ref:`NXlens`:
       A class to describe all types of lenses. Includes electrostatic lenses for electron energy analysers.


.. _ExtendedBC:

Extended Base Classes
#######################

We added descriptors to existing NeXus base classes:

    :ref:`NXinstrument`
       Added fields to add information that is important for an ellipsometry setup, such as the ellipsometer type, the light source, the type of the sample stage, or the angle(s) of incidence, as well as information on calibration, focussing probes, data correction etc. 
              
    :ref:`NXdetector`
       Added fields to describe spectroscopic detection with polarization (e.g. rotating analyzer).
       
    :ref:`NXaperture`
       Added fields to define parameters that describe windows (e.g. windows of a UHV cryostat), such as the thickness and the orientation angle of the window, as well as reference data to calculate window effects.
       
    :ref:`NXsample`
       Added fields to specify the sample and material properties, as well as the sample environment (e.g. refractive index of surrounding medium) and experimental conditions (e.g. temperature, pressure, pH value etc.).

..    :ref:`NXentry`
..       Added fields to describe an ellipsometry experiment.
      
..    :ref:`NXsubentry`
..      Used to describe calibration, sample stage, reference data for a window, and optical excitation. 
