.. $Id$

.. _WhatIsNeXus:

=====================================================================
What is NeXus?
=====================================================================

The NeXus data format has four components: 

.. index:: NeXus

#.	:ref:`Introduction-DesignPrinciples`
	to help people understand what is in the data files.
#.	:ref:`Introduction-DataStorageObjects`
	(base classes and application definitions) to allow 
	the development of more portable analysis software.
#.	:ref:`Introduction-SetOfSubroutines`
	(utilities) to make it easy to read and write NeXus data files.
#.	:ref:`Scientific_Community`
	provides the scientific data, advice, and continued involvement
	with the NeXus standard. NeXus provides a forum for the scientific
	community to exchange ideas in data storage.

.. description of the low-level formats was pulled from the intro in 2011
   In addition, NeXus relies on a set of low-level file formats to actually 
   store NeXus files on physical media. Each of these components are described 
   in more detail in :ref:`Fileformat`. 

.. index:: NAPI 
           
The NeXus Application-Programmer Interface (NAPI), which
provides the set of subroutines for reading and writing NeXus data files,
is described briefly in :ref:`Introduction-NAPI`.
(Further details are provided in the NAPI chapter of Volume II of this
documentation.)

The principles guiding the design and implementation of the NeXus standard
are described in :ref:`NeXus-Design`.

Base classes and applications,
which comprise the data storage objects used in NeXus data files,
are detailed in the *Class Definitions* chapter of 
Volume II of this documentation.
            
.. With this information, it should be possible to bypass the NAPI and
	read & write NeXus data directly in the low-level file format.

Additionally, a brief list describing the set of NeXus Utilities 
available to browse, validate, translate, and visualise
NeXus data files is provided in :ref:`Utilities`.


.. toctree::

    whatis/design
    whatis/objects
    whatis/subroutines
    whatis/community
