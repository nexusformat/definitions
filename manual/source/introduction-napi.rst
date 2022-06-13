.. _Introduction-NAPI:

=================================================
NAPI: The NeXus Application Programming Interface
=================================================

.. index::
   see: API; NAPI
   file; read and write

The :index:`NeXus API <! NAPI>` consists of routines to read and
write NeXus data files.
It was written to provide a simple to use and consistent common interface for
all supported backends (XML, HDF4 and HDF5) to
scientific programmers and other users of the NeXus Data Standard.

.. note:: It is not necessary to use the NAPI to write or read
	NeXus data files.  The intent of the NAPI is to simplify
	the programming effort to use the HDF programming
	interface.  There are :ref:`Examples` to help you understand.

This section will provide a brief overview of the available functionality.
Further documentation of the NeXus Application Programming Interface
(NAPI) for bindings to specific programming language can be found
in the :ref:`NAPI <NAPI>` chapter and may be downloaded
from the NeXus development site. [#]_

For an even more detailed description of the internal workings of NAPI
see the `NeXus Internals manual <https://manual.nexusformat.org/_static/NeXusIntern.pdf>`_, copied from the NeXus code repository.
That document is written for programmers who want to work on the NAPI itself.
If you are new to NeXus and just want to implement basic file reading or writing
you should not start by reading that.

.. _Introduction-HowToWrite:

How do I write a NeXus file?
============================

.. index:: write file

The NeXus Application Program Interface :index:`(NAPI) <NAPI>`
provides a set of subroutines that make it easy to read and write
NeXus files. These subroutines are available in C, Fortran 77, Fortran 90, Java,
Python, C++, and IDL.

The API uses a very simple *state*
model to navigate through a NeXus file.
(Compare this example with :ref:`example.napi.simple.2d.write`,
in the :ref:`NAPI <NAPI>` chapter, using the native HDF5 commands.)
When you open a file,
the API provides a file *handle*, which stores the
current location, i.e. which group and/or field is currently open. 
Read and write operations then act on the currently open entity.
Following the simple example titled
:ref:`Example structure of a simple data file <fig.simple-example>`,
we walk through a schematic of NeXus program written in C
(without any error checking or real data).

.. compound::
	
	.. _fig.ex-c-write:

    .. rubric:: Writing a simple NeXus file using NAPI

    .. note:: 
       We assume the program can define
       the arrays ``tth`` and ``counts``, each length ``n``.
       This part has been omitted from the example code.

    .. literalinclude:: examples/ex-c-write.c
        :tab-width: 4
        :linenos:
        :language: c

.. compound::

    .. _ex.write.c:

    .. rubric:: program analysis
    
    #. line 7:
        .. _ex.write.open:

        Open the file ``NXfile.nxs`` with *create*
        access (implying write access). NAPI [#]_
        returns a file identifier of type ``NXhandle``.
    #. line 7:
        .. _ex.write.entry.group:

        Next, we create the :ref:`NXentry`
        group to contain the scan using
        ``NXmakegroup()`` and then
        open it for access using ``NXopengroup()``. [#]_
    #. line 10:
        The :index:`plottable data <plotting>`
        is contained within an :ref:`NXdata`
        group, which must also be created and opened.
    #. line 12:
        To create a field, call ``NXmakedata()``, specifying the
        data name, type (``NX_FLOAT32``), :index:`rank <rank>`
        (in this case, ``1``), and length of the array
        (``n``).  Then, it can be opened for writing. [#]_
    #. line 14:
        Write the data using ``NXputdata()``.
    #. line 15:
        With the field still open, we can also add some field
        :index:`attributes <field attribute>`,
        such as the :index:`data units <units>`, [#]_ [#]_
        which are specified as a character string (``type="NX_CHAR"`` [#]_)
        that is 7 bytes long.
    #. line 16:
        Then we close the field before opening another.
        In fact, the API will do this automatically if you
        attempt to open another field, but it is
        better style to close it yourself.
    #. line 17:
        The remaining fields in this group are added in a similar
        fashion. Note that the indentation whenever a new field or
        group are opened is just intended to make the structure of
        the NeXus file more transparent.
    #. line 20:
        Finally, close the groups (``NXdata`` and
        ``NXentry``) before closing the file itself.

.. _Introduction-HowToRead:

How do I read a NeXus file?
===========================

.. index::
   read file

Reading a NeXus file works in the same way by traversing the tree with the handle.

This schematic C code will read the two-theta array
created in the :ref:`example above <fig.ex-c-write>`.
(Again, compare this example with :ref:`code_native.reading`.)

.. compound::
	
	.. _fig.ex-c-read:

    .. rubric:: Reading a simple NeXus file using NAPI

    .. literalinclude:: examples/ex-c-read.c
        :tab-width: 4
        :linenos:
        :language: text

.. _Introduction-HowToBrowse:

How do I browse a NeXus file?
=============================

.. index::
   browser

NeXus files can also be viewed by a command-line browser,
``nxbrowse``, which is included as a helper tool in the
:ref:`NeXus API <Introduction-NAPI>`
distribution. The :ref:`following <fig.nxbrowse>` 
is an example session of :index:`nxbrowse` 
``nxbrowse`` to view a data file.

.. compound::
	
	.. _fig.nxbrowse:

    .. rubric:: Using ``nxbrowse``

    .. literalinclude:: examples/ex-unix-using-nxbrowse.txt
        :tab-width: 4
        :linenos:
        :language: text

    .. _fig.using.nxbrowse:

    .. rubric:: program analysis

    #. line 1:
        Start ``nxbrowse`` from the UNIX command
        line and open file ``lrcs3701.nxs`` from
        IPNS/LRMECS.
    #. line 8:
		List the contents of the current group.
    #. line 11:
        Open the NeXus group ``Histogram1``.
    #. line 23:
        Print the contents of the NeXus data labeled ``title``.
    #. line 41:
        Close the current group.
    #. line 43:
        Quits ``nxbrowse``.

The source code of ``nxbrowse`` [#]_
provides an example of how to write a NeXus reader.
The test programs included in the :ref:`NeXus
API <Introduction-NAPI>` may also be useful to study.


.. [#] https://github.com/nexusformat/code/releases/

.. [#] :ref:`NAPI`

.. [#]
    See the chapter 
    :ref:`base.class.definitions`
    for more information.

.. [#]
    The :ref:`Design-DataTypes`
    section describes the available
    data types, such as ``NX_FLOAT32``
    and ``NX_CHAR``.

.. [#] :ref:`Design-Units`

.. [#]
    The NeXus rule about data units is described in the
    :ref:`Design-Units` section.

.. [#] see :ref:`nxdl-types`

.. [#] https://github.com/nexusformat/code/blob/master/applications/NXbrowse/NXbrowse.c
