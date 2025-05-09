.. _BC-Opt-Spec-Structure:

====================
Optical Spectroscopy
====================

.. index::
   BC-Opt-Spec-Introduction
   Raman-BC
   DispersiveMaterial-BC

.. _BC-Opt-Spec-Introduction:

Introduction
############

These are a set of base classes to describe optical spectroscopy, including :ref:`Ellipsometry &lt;AppDef-Opt-Spec-Ellipsometry&gt;`
and :ref:`Raman spectroscopy &lt;AppDef-Opt-Spec-Raman&gt;`

These base classes are used within the :ref:`application definitions &lt;AppDef-Opt-Spec-Definitions&gt;` related to optical spectroscopy

.. _BC-Opt-Spec-Classes:


Base Classes
------------

This is the set of base classes for describing an optical experiment.


   :ref:`NXbeam`
      Beam properties such as intensity, polarization, wavelength or direction.

   :ref:`NXdetector`
      A detector for signal detection.

   :ref:`NXsource`
      A light source such as laser, lamp or LED.

   :ref:`NXmonochromator`
      A monochromator is often used to energetically disperse the scattered or emitted light.

   :ref:`NXlens_opt`
      Description of an optical lens.
       
   :ref:`NXwaveplate`
      A waveplate or retarder.

   :ref:`NXsensor`
      Specify external parameters that have influenced the sample such as
      varied parameters e.g. temperature, pressure, pH value, beam intensity, etc.


ADD ALL CLASSES HERE