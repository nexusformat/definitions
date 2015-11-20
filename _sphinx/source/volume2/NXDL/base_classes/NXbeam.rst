..  _NXbeam:

######
NXbeam
######

.. index::  ! . NXDL base_classes; NXbeam

category:
    base_classes

NXDL source:
    NXbeam
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXbeam.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    :ref:`NXdata`

documentation:
    Template of the state of the neutron or X-ray beam at any location. It will be referenced
    by beamline component groups within the NXinstrument group or by the NXsample group. Note
    that variables such as the incident energy could be scalar values or arrays. This group is
    especially valuable in storing the results of instrument simulations in which it is useful
    to specify the beam profile, time distribution etc. at each beamline component. Otherwise,
    its most likely use is in the NXsample group in which it defines the results of the neutron
    scattering by the sample, e.g., energy transfer, polarizations.
    


.. rubric:: Basic Structure of **NXbeam**

.. code-block:: text
    :linenos:
    
    NXbeam (base class, version 1.0)
      distance:NX_FLOAT
      energy_transfer:NX_FLOAT[i]
      final_beam_divergence:NX_FLOAT[2,j]
      final_energy:NX_FLOAT[i]
      final_polarization:NX_FLOAT[2,j]
      final_wavelength:NX_FLOAT[i]
      final_wavelength_spread:NX_FLOAT[i]
      flux:NX_FLOAT[i]
      incident_beam_divergence:NX_FLOAT[2,j]
      incident_energy:NX_FLOAT[i]
      incident_polarization:NX_FLOAT[2,j]
      incident_wavelength:NX_FLOAT[i]
      incident_wavelength_spread:NX_FLOAT[i]
      NXdata
    

.. rubric:: Symbols used in definition of **NXbeam**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXbeam**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
