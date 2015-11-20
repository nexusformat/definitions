.. $Id: introduction.rst 881 2011-09-12 01:47:48Z Pete Jemian $

..  _MotivationsForNeXus:

***************************************************************************
Motivations for the NeXus standard in the Scientific Community
***************************************************************************

..
	Today:
		* Lots of different data formats
		* Time wasted converting data
		* Old formats no longer capable of delivering for new high throughput detectors
		* Difficult to add additional data
		* Often, for DA multiple different files needed
		* Badly documented formats
	Tomorrow, with NeXus:
		* Single, efficient, platform independent data format
		* All information in one file
		* Self-describing
		* Extendable

By the early 1990s, several groups of scientists in the fields of neutron 
and X-ray science had recognized a common and troublesome pattern in the 
data acquired at various scientific instruments and user facilities.  Each 
of these instruments and facilities had a locally defined format for 
recording experimental data. With lots of different formats, much of the 
scientists' time was being wasted in the task of writing import readers 
for processing and analysis programs. As is common, the exact information 
to be documented from each instrument in a data file evolves, such as the 
implementation of new high-throughput detectors.  Many of these formats 
lacked the generality to extend to the new data to be stored, thus another 
new format was devised.  In such environments, the documentation of each 
generation of data format is often lacking.

Three parallel developments have led to NeXus:

#. June 1994:
	Mark Koennecke (Paul Scherer Institute, Switzerland) made a 
	proposal using netCDF for the European neutron scattering 
	community while working at the ISIS pulsed neutron facility.

#. August 1994:
	Jon Tischler and Mitch Nelson (Oak Ridge National Laboratory, USA) 
	proposed an HDF-based format as a standard for data storage at the 
	Advanced Photon Source (Argonne National Laboratory, USA).

#. October 1996:
	Przemek Klosowski (National Institute of Standards and Technology, USA) 
	produced a first draft of the NeXus proposal drawing on ideas 
	from both sources.

These scientists proposed methods to store data using a self-describing, 
extensible format that was already in broad use in other scientific 
disciplines. Their proposals formed the basis for the current design of 
the NeXus standard which was developed at two workshops, SoftNeSS'95 (NIST 
Sept. 1995) and SoftNeSS'96 (Argonne Oct. 1996), attended by 
representatives of a range of neutron and x-ray facilities. 

.. _basic.motivations:

Basic motivations for the NeXus standard
------------------------------------------------

.. index:: NeXus basic motivation

The NeXus API was released in late 1997.  
Basic motivations for this standard were:

.. toctree::
	:maxdepth: 1

	plotting
	unified
	dictionary
