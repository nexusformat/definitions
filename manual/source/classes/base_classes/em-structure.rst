.. _BC-Em-Structure:

===================
Electron microscopy
===================

.. index::
   BC-Em-Introduction
   BC-Em-Classes
   BC-Em-Classes-Methods:

.. _BC-Em-Introduction:

Introduction
############

These are a set of base classes to describe components of an electron microscope and its focused-ion beam functionalities,
as well as the associated data analysis.

Some of the base classes are specific to EM, whereas others are used in other techniques as well.

These base classes are used within the EM-related :ref:`application definitions &lt;AppDef-Em-Definitions&gt;`.

.. _BC-Em-Classes:

Base Classes
############

The following base classes are proposed to support modularizing the storage of pieces of information related to electron microscopy research:

   :ref:`NXaberration`:
      Base class to describe procedures and values for the calibration of aberrations.
   
   :ref:`NXatom`:
      A base class to describe charged molecular ions with an adjustable number of atoms/isotopes building each ion. Right now the maximum number of atoms supported building a molecular ion is 32. Suggestions made in reference `DOI: 10.1017/S1431927621012241 <https://doi.org/10.1017/S1431927621012241>`_ are used to map isotope to hash values with which all possible isotopes can be described.

   :ref:`NXcoordinate_system_set`:
      A base class to describe different coordinate systems used and/or to be harmonized
      or transformed into one another when interpreting the dataset.

   :ref:`NXcorrector_cs`:
      A base class to describe details about corrective lens or compound lens devices
      which reduce the aberration of an electron beam.

   :ref:`NXebeam_column`:
      A base class serving the possibility to group the components relevant for generating
      and shaping the electron beam.
    
   :ref:`NXevent_data_em`:
      A base class representing a container to hold time-stamped and microscope-state-
      annotated data during a session at an electron microscope.

   :ref:`NXibeam_column`:
      A base class serving the possibility to group the components relevant for generating
      and shaping an ion beam of an instrument to offer focused-ion beam (milling) capabilities.

   :ref:`NXimage`:
      Base class for storing acquisition details for individual images or stacks of images. Specialized versions can be defined and use controlled vocabulary terms for group name prefixes like **adf** annular dark field, **bf** bright field, **bse** backscattered electron, **chamber** camera to monitor the stage and chamber, **df** darkfield, **diffrac** diffraction, **ecci** electron channeling contrast imaging, **kikuchi** electron backscatter diffraction, **ronchigram** - convergent beam diffraction pattern, or **se** secondary electron.

   :ref:`NXinstrument_em`:
      A base class which defines all modular parts that make up an instrument (real or simulated) for studying
      electron matter interaction. This base class is used in NXem in two places: One that is placed inside an ENTRY.measurement.instrument
      group. This group holds all those (meta)data which do not change during a session, i.e. instrument name, typically identifier of 
      hardware components or version of control software. Another one that is placed inside an ENTRY.measurements.events group.
      This group holds all those (meta)data data change when collecting data during a session.

   :ref:`NXlens_em`:
      A base class to detail an electro-magnetic lens. In practice, an electron microscope has many such lenses. It is possible to specify as many lenses as necessary to represent eventually each single lens of the microscope and thus describe how the lenses are affecting the electron beam. This can offer opportunities for developers of software tools which strive to model the instrument e.g. to create digital twins of the instrument. We understand there is still a way to go with this to arrive there though. Consequently, we suggest to focus first on which details should be collected for a lens as a component so that developers of application definitions can take immediate advantage of this work.

   :ref:`NXfabrication`:
      A base class to bundle manufacturer/technology-partner-specific details about
      a component or device of an instrument.

   :ref:`NXoptical_system_em`:
      A base class to store for now qualitative and quantitative values of frequent interest
      which are affected by the interplay of the components and state of an electron microscope.
      Examples are the semiconvergence angle or the depth of field and depth of focus, the magnification, or the camera length.

   :ref:`NXpeak`:
      A base class to describe peaks mathematically so that it can be used to detail how peaks in mass-to-charge-state ratio histograms (aka mass spectra) are defined and labelled as iontypes.

   :ref:`NXpump`:
      A base class to describe details about a pump in an instrument.

   :ref:`NXscanbox_em`:
      A base class to represent the component of an electron microscope which realizes a controlled deflection (and eventually shift, blanking, and/or descanning) of the electron beam to illuminate the specimen in a controlled manner. This can be used to document the scan pattern.

   :ref:`NXspectrum`:
      Base class and specializations comparable to NXimage_set but for storing spectra. Specialized base classes should use controlled vocabulary items as prefixes such as **eels** electron energy loss spectroscopy, **xray** X-ray spectroscopy (EDS/STEM, EDX, SEM/EDX, SEM/EDS), **auger** Auger spectroscopy, or **cathodolum** for cathodoluminescence spectra.

.. _BC-Em-Classes-Methods:

Method-specific concepts and their usage in application definitions
###################################################################

   :ref:`NXem_ebsd`, :ref:`NXem_eds`, :ref:`NXem_eels`, :ref:`NXem_img`:
      Base class providing concepts for specific data acquistion modes and associated analysis used in electron microscopy
      such as collecting and indexing Kikuchi pattern into orientation maps for the two-dimensional, three-, X-ray spectrscopy,
      different imaging modes, or electron energy loss spectroscopy (EELS).


.. _BC-Em-Classes-Analysis:

.. We provide specific base classes which granularize frequently collected or analyzed quantities in specific application fields of electron microscopy to deal
.. with the situation that there are cases were logical connections between generated data artifacts mainly exist for the fact that the data artifacts were
.. collected during a workflow of electron microscopy research (e.g. taking measurements and then performing method-specific analyses generating new data and conclusions).
.. We see a value in granularizing out these pieces of information into own classes. In fact, one limitation of application definitions in NeXus, exactly as it applies for serialization
.. of information also more generally, is currently that they define a set of constraints on their graph of controlled concepts and terms.

.. If we take for example diffraction experiments performed with an electron microscope, it is usually the case that (diffraction) patterns are collected in the session at the microscope.
.. However, all scientifically relevant conclusions are typically drawn later, i.e. through post-processing the collected diffraction (raw) data. These numerical and algorithmic steps
.. define computational workflows were data from an instance of an application definition such as NXem are used as input but many additional concepts, constraints, and assumptions
.. are applied without that these demand necessarily changes in the constraints on fields or groups of NXem. If we were to modify NXem for these cases,
.. NXem would combinatorially diverge as every different combination of required constraints demands having an own but almost similar application definition.
.. For this reason, method-specific base classes are used which granularize out how specific pieces of information are processed further to eventually enable their
.. storage (i.e. serialization) using NeXus.

