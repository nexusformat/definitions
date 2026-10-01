.. _AppDef-Diff-Structure:

===================================
Diffraction & Scattering Techniques
===================================

.. index::
   AppDef-Diff-Introduction
   AppDef-Diff-Definitions

.. _AppDef-Diff-Introduction:

Introduction
############

Application definitions for different diffraction and (small-angle) scattering techniques

.. _AppDef-Diff-Definitions:

Application Definitions
#######################

:ref:`NXiqproc`
    Application definition for any :math:`I(Q)` data.

:ref:`NXlauetof`
    This is the application definition for a TOF laue diffractometer.

:ref:`NXmonopd`
    Monochromatic Neutron and X-Ray Powder diffractometer.

:ref:`NXxbase`
    This definition covers the common parts of all monochromatic single crystal raw data application definitions.

:ref:`NXxeuler`
    Raw data from a :index:`four-circle diffractometer` with an :index:`eulerian cradle`, extends :ref:`NXxbase`.

:ref:`NXxkappa`
    Raw data from a kappa geometry (CAD4) single crystal diffractometer, extends :ref:`NXxbase`.

:ref:`NXxlaue`
    Raw data from a single crystal laue camera, extends :ref:`NXxrot`.

:ref:`NXxlaueplate`
    Raw data from a single crystal Laue camera, extends :ref:`NXxlaue`.

:ref:`NXxnb`
    Raw data from a single crystal diffractometer, extends :ref:`NXxbase`.

:ref:`NXxrot`
    Raw data from a rotation camera, extends :ref:`NXxbase`.

:ref:`NXcanSAS`
    Implementation of the canSAS standard to store reduced small-angle scattering data of any dimension.

:ref:`NXsas`
    Raw, monochromatic 2-D SAS data with an area detector.

:ref:`NXsastof`
    Raw 2-D SAS data with an area detector with a time-of-flight source.
