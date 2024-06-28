.. _Mpes-Structure-Fairmat:

=======================================
Photoemission & core-level spectroscopy
=======================================

The NXmpes application definition is designed to describe data and metadata obtained from
various multidimensional photoemission spectroscopy (MPES) techniques.
This definition is very flexible and requires just a reasonable amount of
metadata to make the stored data interoperable and reproducible.
The only requirement for the actual data is the existence of an energy axis.

The experimental techniques covered by this application definition are primarily limited
to photon-in photoelectron-out methods. If you are searching for related techniques,
there is a good chance you will find valuable information here.

Example techniques covered by this application definition include:

- X-ray/UV photoelectron spectroscopy (XPS/UPS)
- Angle-resolved photoemission spectroscopy (ARPES)
- Two-photon photoemission (2PPE)
- Photoemission electron microscopy (PEEM)

Additionally, we offer descriptors for specialized applications,
such as spin- and time-resolution, near-ambient pressure conditions, dichroism, and more.

Here's a list of application definitions related to photoemission spectroscopy:

    :ref:`NXmpes`:
       A universal application definition with minimal metadata requirements for describing all photoemission experiments.

    :ref:`NXmpes_arpes`:
       An appdef for angle-resolved photoemission spectroscopy (ARPES) experiments.

      :ref:`NXxps`:
       An application definition for XPS/UPS measurements.