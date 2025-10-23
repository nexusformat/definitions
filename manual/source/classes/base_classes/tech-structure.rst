.. _BC-Tech-Structure:

=========================
Parts of instruments
=========================

.. index::
   BC-Tech-Base-Classes

Data schemas to describe parts, components, or sets of components for building an instrument.

Base Classes
############

:ref:`NXactuator`
    An actuator used to control an external condition.

:ref:`NXaperture`
    A beamline aperture.

:ref:`NXattenuator`
    A device that reduces the intensity of a beam by attenuation.

:ref:`NXbeam_stop`
    A device that blocks the beam completely, usually to protect a detector. 

:ref:`NXbending_magnet`
    A bending magnet

:ref:`NXcapillary`
    A capillary lens to focus the X-ray beam.

:ref:`NXcircuit`
    Base class for documenting circuit devices.

:ref:`NXcollectioncolumn`
    Electron collection column of an electron analyzer.

:ref:`NXcollimator`
    A beamline collimator.

:ref:`NXcomponent`
    Base class for components of an instrument - real ones or simulated ones.

:ref:`NXcorrector_cs`
    Base class for a corrector reducing (spherical) aberrations of an electron optical setup.

:ref:`NXcrystal`
    A crystal monochromator or analyzer. 

:ref:`NXdeflector`
    Component of an electron analyzer that deflects the paths of electrons.
    This includes electrostatic and electromagnetic deflectors.

:ref:`NXdetector`
    A detector, detector bank, or multidetector.

:ref:`NXdetector_channel`
    Description and metadata for a single channel from a multi-channel detector.

:ref:`NXdetector_group`
    Logical grouping of detectors. When used, describes a group of detectors.

:ref:`NXdetector_module`
    Geometry and logical description of a detector module. When used, child group to NXdetector.

:ref:`NXdisk_chopper`
    A device blocking the beam in a temporal periodic pattern.

:ref:`NXebeam_column`
    Base class for a set of components providing a controllable electron beam.

:ref:`NXelectromagnetic_lens`
    Base class for an electro-magnetic lens or a compound lens.

:ref:`NXelectron_detector`
    A subclass of NXdetector for detectors that detect electrons.

:ref:`NXelectronanalyzer`
    Basic class for describing an electron analyzer.

:ref:`NXem_instrument`
    Base class for instrument-related details of a real or simulated electron microscope.

:ref:`NXem_optical_system`
    Base class for qualifying an electron optical system.

:ref:`NXenergydispersion`
    Energy dispersion section of an electron analyzer.

:ref:`NXfabrication`
    Details about a component as it is defined by its manufacturer.

:ref:`NXfermi_chopper`
    A Fermi chopper, possibly with curved slits.

:ref:`NXfilter`
    For band pass beam filters.

:ref:`NXflipper`
    A spin flipper.

:ref:`NXfresnel_zone_plate`
    A fresnel zone plate

:ref:`NXgrating`
    A diffraction grating, as could be used in a soft X-ray monochromator

:ref:`NXguide`
    A neutron optical element to direct the path of the beam.

:ref:`NXibeam_column`
    Base class for a set of components equipping an instrument with FIB capabilities.

:ref:`NXinsertion_device`
    An insertion device, as used in a synchrotron light source.

:ref:`NXinstrument`
    Collection of the components of the instrument or beamline.

:ref:`NXmanipulator`
    Base class to describe the use of manipulators and sample stages.

:ref:`NXmirror`
    A beamline mirror or supermirror.

:ref:`NXmoderator`
    A neutron moderator

:ref:`NXmonitor`
    A monitor of incident beam data. 

:ref:`NXmonochromator`
    A  wavelength defining device.

:ref:`NXoptical_lens`
    Description of an optical lens.

:ref:`NXoptical_window`
    A window of a cryostat, heater, vacuum chamber or a simple glass slide.

:ref:`NXpdb`
    A NeXus transliteration of a PDB file, to be validated only as a PDB

:ref:`NXpid_controller`
    A description of a feedback system in terms of the settings of a proportional-integral-derivative (PID) controller.

:ref:`NXpinhole`
    A simple pinhole.

:ref:`NXpolarizer`
    A spin polarizer.

:ref:`NXpositioner`
    A generic positioner such as a motor or piezo-electric transducer.

:ref:`NXpump`
    Device to reduce an atmosphere to a controlled pressure.

:ref:`NXreflections`
    Reflection data from diffraction experiments

:ref:`NXscan_controller`
    The scan box or scan controller is a component that is used to deflect a

:ref:`NXsensor`
    A sensor used to monitor an external condition 

:ref:`NXslit`
    A simple slit.

:ref:`NXsource`
    Radiation source emitting a beam.

:ref:`NXspindispersion`
    Class to describe spin filters in photoemission experiments.

:ref:`NXvelocity_selector`
    A neutron velocity selector

:ref:`NXwaveplate`
    A waveplate or retarder.

:ref:`NXxraylens`
    An X-ray lens, typically at a synchrotron X-ray beam line.

