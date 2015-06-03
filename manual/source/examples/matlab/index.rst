.. index:: !MATLAB; examples

.. TODO: needs a proper write-up using actual MATLAB session and graphics

.. _matlab.examples:

===============
MATLAB Examples
===============

:author: Paul Kienzle, NIST

..	note:: **Editor's Note**:
	These files were copied directly from an older version 
	of the NeXus documentation (DocBook) and have not been checked
	that they will run under current Matlab versions.

==========================	============================================================
file				description
==========================	============================================================
:download:`input.dat`		two-column text data file, also used in other examples
:download:`basic_writer.m`	writes a NeXus HDF5 file using ``input.dat``
:download:`basic_reader.m`	reads the NeXus HDF5 file written by ``basic_writer.m``
:download:`h5link.m`		support module for creating NeXus-style HDF5 hard links
:download:`writer_2_1.m`	like ``basic_writer.m`` but stores data in 
							``/entry/instrument/detector`` 
							and then links to **NXdata** group
==========================	============================================================
