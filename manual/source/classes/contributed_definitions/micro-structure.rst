.. _CC-Micro-Structure:

===================================================
Microstructure Characterization and Representation
===================================================

.. index::
   CC-Micro-Introduction
   CC-Micro-Definitions

.. _CC-Micro-Introduction:

Introduction
##############

The internal structure of a material modeled as crystals and the defect network that connect these.

.. _CC-Micro-Definitions:

Application Definitions
#######################

Base classes
############

:ref:`NXmicrostructure`
    Base class to describe elements of the microstructure of a material.

:ref:`NXmicrostructure_pf`, :ref:`NXmicrostructure_ipf`, :ref:`NXmicrostructure_odf`
    Base classes for describing parameterization, results, and data from texture analysis,
    specifically pole figure (pf), inverse pole figure (ipf),
    and orientation distribution function (odf), respectively.

:ref:`NXmicrostructure_feature`
    Set of topological/spatial features in materials built from atoms, from coarse-grained
    representations of atoms, or from other microstructure features.

:ref:`NXmicrostructure_slip_system`
    Base class for describing a set of crystallographic slip systems.

:ref:`NXmicrostructure_mtex_config`
    Base class for documenting the parameterization of MTex, which is
    a software for analyzing material texture written in MATLAB.

:ref:`NXmicrostructure_score_config`
    Application definition to control a simulation with the SCORE cellular automata simulation tool.

:ref:`NXmicrostructure_score_results`
    Application definition for storing results of the SCORE cellular automata simulation tool.

:ref:`NXmicrostructure_kanapy_results`
    Application definition for storing results of the kanapy microstructure synthesis tool.






