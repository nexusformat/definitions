.. _Icme-Structure:

==============================================
Integrated Computational Materials Engineering
==============================================

.. index::
   IcmeMsModels

.. _IcmeMsModels:

Application definitions for ICME models
#######################################

It is important to embrace the large research community of materials engineers
as they are frequent users of electron microscopy and atom probe microscopy.
ICME is an abbreviation for Integrated Computational Materials Engineering, which is
a design strategy and workflow whereby physics-based modelling of microstructure
evolution is used to understand the relations between the microstructure and
its technologically relevant descriptors to understand and tailor properties of materials.

The following application definitions are proposed to support the discussion on how
materials-engineering-specific data schemas can connect to or be mapped on
concepts which are equally modellable with NeXus:

    :ref:`NXmicrostructure`:
        A base class for documenting a snapshot of a reconstructed microstructure.

    :ref:`NXmicrostructure_imm_config`, :ref:`NXmicrostructure_imm_results`:
        A specific example of an application definition for documenting the
        configuration and results respectively of a computer simulation with
        the legacy microstructure synthesizer developed at the Institut für
        Metallkunde und Metallphysik in Aachen.

    :ref:`NXmicrostructure_kanapy_results`:
        A specific example of an application definition for documenting the results
        of a computer simulation with the kanapy microstructure synthesizer
        developed at the ICAMS in Bochum.

    :ref:`NXmicrostructure_score_config`, :ref:`NXmicrostructure_score_results`:
        A specific example of an application definition for documenting the
        configuration and results respectively of a computer simulation with
        the static recrystallization cellular automata model SCORE.

    :ref:`NXmicrostructure_gragles_config`, :ref:`NXmicrostructure_gragles_results`:
        A specific example of an application definition for documenting the
        configuration and results respectively of a computer simulation with
        the grain growth level-set-based model GraGLeS.
