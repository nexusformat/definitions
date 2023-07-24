.. _Apm-Structure1:

=========================
B5: Atom-probe tomography
=========================

.. index::
   IntroductionApm1
   ApmAppDef1


.. _IntroductionApm1:

Introduction
##############

Set of data storage objects to describe the acquisition/measurement side, the reconstruction, and the ranging for atom probe microscopy experiments. The data storage objects can be useful as well for field-ion microscopy experiments.

.. _ApmAppDef1:

Application Definitions
#######################

We created one new application definition whose intention is to serve both the description of atom probe tomography and field-ion microscopy measurements:

    :ref:`NXapm`:
       A general application definition with many detailed places for leaving metadata and computational steps described which are commonly used when reporting the measurement of atom probe data including also detector hit data, as well as how to proceed with reconstructing atom positions from these data, and how to store details about definitions made, which describe how mass-to-charge-state ratio values are mapped to iontypes (ranging).
