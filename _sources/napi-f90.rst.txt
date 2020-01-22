.. index:: NAPI; f90

.. _NAPI-Core-f90:

==========================================
NAPI Fortran 90 Interface
==========================================


The Fortran 90 interface is a wrapper to the C interface with nearly 
identical routine definitions. As with the Fortran 77 interface, it is 
necessary to reverse the order of indices in multidimensional arrays, 
compared to an equivalent C program, so that data are stored in the 
same order in the NeXus file.

Any program using the F90 API needs to put the following line at 
the top (after the ``PROGRAM`` statement)::

	use NXmodule

Use the following table to convert from the C data types 
listed with each routine to the Fortran 90 data types.

============================= =======================================================
C data type                   F90 data type
============================= =======================================================
``int, int``                  ``integer``
``char*``                     ``character(len=*)``
``NXhandle, NXhandle*``       ``type(NXhandle)``
``NXstatus``                  ``integer``
``int[]``                     ``integer(:)``
``void*``                     ``real(:)`` or ``integer(:)`` or ``character(len=*)``
``NXlink a``, ``NXlink* a``   ``type(NXlink)``
============================= =======================================================

The parameters in the next table,
defined in ``NXmodule``, may be used in defining variables.

=================  ======================================  ============================
Name               Description                             Value
=================  ======================================  ============================
``NX_MAXRANK``     Maximum number of dimensions            ``32``
``NX_MAXNAMELEN``  Maximum length of NeXus name            ``64``
``NXi1``           Kind parameter for a 1-byte integer     ``selected_int_kind(2)``
``NXi2``           Kind parameter for a 2-byte integer     ``selected_int_kind(4)``
``NXi4``           Kind parameter for a 4-byte integer     ``selected_int_kind(8)``
``NXr4``           Kind parameter for a 4-byte real        ``kind(1.0)``
``NXr8``           Kind parameter for an 8-byte real       ``kind(1.0D0)``
=================  ======================================  ============================

The bindings are listed at https://github.com/nexusformat/code/tree/master/bindings/f90 and can be built as part of the API distribution https://github.com/nexusformat/code/releases
