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
    XAS measured in transmission, where the absorption coefficient follows the Beer-Lambert law
    :math:`\mu(E)\,t = -\ln(I/I_0)`.

.. _CC-Xas-Base-Classes:

Base Classes
############

:ref:`NXelement`
    A chemical element of the periodic table, identified by its atomic number as a species and not as
    a specific isotope.

:ref:`NXabsorption_edge`
    Description of an X-ray absorption edge, the sharp discontinuity in the absorption spectrum that
    occurs when the incident photon energy reaches the threshold for exciting an atom from its neutral
    ground state to a core-vacancy state.

:ref:`NXemission_line`
    An emission line, which arises from the radiative decay of an atom with a core hole: an electron
    from a higher level fills the hole and a photon is emitted with an energy characteristic of the
    atom.

:ref:`NXauger_line`
    An Auger line, which arises from the non-radiative decay of an atom with a core hole: an electron
    from a higher level fills the hole and another electron, the Auger electron, is ejected with a
    kinetic energy characteristic of the atom.

