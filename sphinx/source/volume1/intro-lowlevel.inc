.. $Id: intro-lowlevel.inc 845 2011-05-19 14:27:12Z Pete Jemian $
  included by introduction.rst

A Set of Low-Level File Formats
---------------------------------------------------------------------

.. _LowLevelFormat:

.. index:: NeXus; low-level file formats

To actually store NeXus files on physical media, different low-level file
formats 
are available, namely HDF4, HDF5, and XML. The NeXus code library may be
configured to support all of them, or any nonempty subset. Applications that
create NeXus files need to decide (or let the user decide) in which low-level
format data shall be stored. Generic data analysis applications should be able
to read any low-level format.  More information is provided in
:ref:`Fileformat`.
