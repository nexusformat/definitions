.. _CC-Xas-Structure:

=============================
X-ray Absorption Spectroscopy
=============================

.. index::
   CC-Xas-Introduction
   CC-Xas-Definitions
   CC-Xas-Base-Classes

.. _CC-Xas-Introduction:

Introduction
############

These are a set of contributed definitions to describe X-ray absorption spectroscopy (XAS) experiments,
in which the absorption coefficient of a sample is measured as a function of the incident photon energy
across one or more absorption edges.

The generic :ref:`NXxas` application definition holds the energy axis and the processed absorption
intensity that are common to every XAS experiment. Technique-specific application definitions extend
:ref:`NXxas` to capture the detection mode and the metadata that a given technique requires.

.. _CC-Xas-Definitions:

Application Definitions
#######################

:ref:`NXxas`
    Generic application definition for X-ray absorption spectroscopy. It stores the incident photon
    energy and the processed absorption intensity, and serves as the base that the technique-specific
    definitions below extend.

:ref:`NXxas_trans`
    X-ray absorption measured in transmission, where the absorption coefficient follows the
    Beer-Lambert law :math:`\mu(E)\,t = -\ln(I/I_0)`.

.. _CC-Xas-Base-Classes:

Base Classes
############

:ref:`NXelement`
    A chemical element of the periodic table.

:ref:`NXabsorption_edge`
    An X-ray absorption edge, which arises from the excitation of an atom to a state with a core
    vacancy: when the incident photon energy reaches the threshold for this excitation, the
    absorption spectrum shows a sharp discontinuity.

:ref:`NXemission_line`
    An emission line, which arises from the radiative decay of an atom with a core vacancy: an
    electron from a higher level fills the vacancy and a photon is emitted with an energy
    characteristic of the element.

:ref:`NXauger_line`
    An Auger line, which arises from the non-radiative decay of an atom with a core vacancy: an
    electron from a higher level fills the vacancy and another electron, the Auger electron, is
    ejected with a kinetic energy characteristic of the element.

