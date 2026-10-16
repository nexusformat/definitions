.. _BC-Em-Structure:

===================
Electron Microscopy
===================

.. index::
   BC-Em-Introduction
   BC-Em-Classes

.. _BC-Em-Introduction:

Introduction
############

These are the base classes to describe components of an electron microscope and its focused-ion beam capabilities,
as well as the associated data analyses. These base classes are used within the EM-related :ref:`application definitions <appdef-em-definitions>`, specifically in NXem.
Some of the base classes are specific to EM, whereas others are used in other techniques as well.

.. _BC-Em-Classes:

Base Classes
############

The design of NXem uses several existent base class and added concepts to existent base classes to make these
applicable for electron microscopy (:ref:`NXactuator`, :ref:`NXaperture`, :ref:`NXbeam`, :ref:`NXcite`,
:ref:`NXcollection`, :ref:`NXcomponent`, :ref:`NXcoordinate_system`, :ref:`NXdata`, :ref:`NXdeflector`, :ref:`NXdetector`,
:ref:`NXfabrication`, :ref:`NXmanipulator`, :ref:`NXmonochromator`, :ref:`NXnote`, :ref:`NXparameters`, :ref:`NXprocess`,
:ref:`NXsample`, :ref:`NXsensor`, :ref:`NXsource`, and :ref:`NXuser`).

Many design decisions of the application definitions :ref:`NXem` and :ref:`NXapm` are aligned. Examples are the use of base 
classes for instrument-specific events :ref:`NXem_event_data`, the grouping of measurements :ref:`NXem_measurement` and simulations
:ref:`NXem_simulation`, and the encapsulating of :ref:`NXparameters` and :ref:`NXdata` in :ref:`NXprocess` instances to describe
workflows of processing. The base classes :ref:`NXatom`, :ref:`NXunit_cell`, and :ref:`NXphase` were introduced to document sets
of atoms, the spatial arrangement of atoms, and offer concepts for documenting when regions-of-interest :ref:`NXroi_process` in a material represent
thermodynamic phases.

In addition to these considerations, there exist base classes to define concepts that are specific for electron microscopy:

:ref:`NXaberration`:
    A base class to describe procedures and values for the calibration of aberrations.

:ref:`NXcorrector_cs`:
    A base class to describe a corrective lens or compound lens sets to reduce the aberration of an electron beam.

:ref:`NXebeam_column`:
    A base class to group the components relevant for generating and shaping an electron beam.

:ref:`NXibeam_column`:
    A base class to group the components relevant for generating and shaping an ion beam.

:ref:`NXimage`:
    A base class to store individual images or stacks of images.

:ref:`NXem_instrument`:
    A base class to document all components that make up an instrument (real or simulated) when using it for studying
    electron matter interaction. This base class is used in NXem in two places:
    Firstly, inside an ENTRY/measurement/instrument group. This group holds all those (meta)data which do not change
    during a session, i.e. instrument name, typically identifier of hardware components or version of control software.
    Secondly, inside ENTRY/measurement/eventID groups; these hold all those (meta)data data that change during a session.

:ref:`NXroi_process` and specialization :ref:`NXem_interaction_volume`:
    A base class to document the region-of-interest within an area or volume of material.
    The region of material where the electron beam interacts with the sample is called the interaction volume.  

:ref:`NXelectromagnetic_lens`:
    A base class to describe an electro-magnetic lens. In practice, an electron microscope has many such lenses.
    It is possible to specify as many lenses as necessary to represent eventually each single lens of the microscope
    and thus describe how the lenses are affecting the electron beam. This can offer opportunities for developers of
    software tools which strive to model the instrument e.g. to create digital twins of the instrument.

:ref:`NXem_optical_system`:
    A base class to store for now qualitative and quantitative values of frequent interest
    which are affected by the interplay of the components and state of an electron microscope.
    Examples are the semiconvergence angle, the magnification, or the camera length.

:ref:`NXpump`:
    A base class to describe details about a pump in an instrument.

:ref:`NXscan_controller`:
    A base class to represent a component that is used to deflect a beam of charged particles in a controlled manner.
    This can be used to document the scan pattern.

:ref:`NXspectrum`:
    A base class to store individual spectra and stacks of spectra.
        
Method-specific concepts and their usage in application definitions
###################################################################

It became clear during the design of the electron-microscopy-specific additions to NeXus that many data and metadata which are relevant for
a given experiment have usually only few connections to the detailed description of the instrument. Instead, these are steps of
data analysis and data processing workflows. This motivated a granularization of these concepts into own method-specific base classes:

:ref:`NXem_ebsd`, :ref:`NXem_eds`, :ref:`NXem_eels`, :ref:`NXem_img`:
    These base classes provide concepts for specific data acquisition modes and associated analyses as are used in electron microscopy
    such as for collecting and indexing Kikuchi diffraction patterns into orientation maps for two-dimensional, three-dimensional point
    cloud data, reporting X-ray spectroscopy (EDS/EDXS), different imaging modes, or documenting electron energy loss spectroscopy (EELS).
    A substantial further number of such base class could be designed that can build on the ideas and principles that are
    suggested via these four base classes.

