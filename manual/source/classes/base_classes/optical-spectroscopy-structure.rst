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

These are a set of base classes to describe optical spectroscopy, including :ref:`Ellipsometry <appdef-opt-spec-ellipsometry>`
and :ref:`Raman spectroscopy <appdef-opt-spec-raman>`

These base classes are used within the :ref:`application definitions <appdef-opt-spec-definitions>` related to optical spectroscopy.

.. _BC-Opt-Spec-Classes:

Base Classes
------------

The  application definitions for optical spectroscopy use several existent base class and add edits and additions of some concepts to
make these base classes applicable for the field of optical spectroscopy (:ref:`NXactuator`, :ref:`NXbeam`, :ref:`NXcalibration`, 
:ref:`NXcomponent`, :ref:`NXcoordinate_system`, :ref:`NXdata`, :ref:`NXdetector`, :ref:`NXenvironment`, :ref:`NXfabrication`,
:ref:`NXhistory`, :ref:`NXinstrument`, :ref:`NXmanipulator`, :ref:`NXmonochromator`,  :ref:`NXpid_controller`, :ref:`NXprocess`,
:ref:`NXprogram`, :ref:`NXresolution`, :ref:`NXsample`, :ref:`NXsensor`, :ref:`NXsource`, :ref:`NXtransformations`, and :ref:`NXuser`).

In addition, there exists a set of base classes to define concepts that are specific for electron microscopy:

   :ref:`NXbeam_transfer_matrix_table`
      Used to relate physical properties of two beams (:ref:`NXbeam`) which have one common optical component (:ref:`NXcomponent`)
      inbetween.

   :ref:`NXoptical_lens`
      Description of an optical lens.

   :ref:`NXoptical_window`
      Description of an optical window.

   :ref:`NXwaveplate`
      A waveplate or retarder.