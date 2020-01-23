.. index:: NAPI; java

.. _NAPI-java:

===================
NAPI Java Interface
===================

This section includes installation notes,
instructions for running NeXus for Java programs and a brief
introduction to the API.

The Java API
for NeXus (``jnexus``) was implemented through the
Java Native Interface (JNI) to call on to the native C library.
This has a number of disadvantages over using pure Java, however
the most popular file backend HDF5 is only available using
a JNI wrapper anyway.

.. _NAPI-java-general-acknow:

Acknowledgement
###############

This implementation uses classes and native methods from NCSA's
Java HDF Interface project. Basically all conversions from native
types to Java types is done through code from the NCSA HDF group.
Without this code the implementation of this API would have taken
much longer. See NCSA's copyright for more information.

.. _NAPI-java-general-install:

Installation
############

.. _NAPI-java-general-install-Requirements:

Requirements
============

.. caution:: Documentation is old and may need revision.

For running an application with ``jnexus`` an recent Java runtime environment (JRE) will do.

In order to compile the Java API for NeXus a Java Development Kit is required on top of the
build requirements for the C API.

.. _NAPI-java-general-install-win32:

Installation under Windows
==========================

#. Copy the HDF DLL's and the file
   ``jnexus.dll`` to a directory in your path.
   For instance ``C:\\Windows\\system32``.

#. Copy the ``jnexus.jar`` to the place where
   you usually keep library jar files.

Note that the location or the naming of these files in the binary Nexus distributions 
have changed over the years. 
In the Nexus 4.3.0 Windows 64-bit distribution (see Assets in https://github.com/nexusformat/code/releases/tag/4.3.0), 
By default, the DLL is at: ``C:\Program Files\NeXus Data Format\bin\libjnexus-0.dll``. 
Please rename this file to ``jnexus.dll`` before making it available in your path. 
This is important, otherwise, JVM runtime will not be able to locate this file. 
   
For the same distribution, the location of ``jnexus.jar`` is at: ``C:\Program Files\NeXus Data Format\share\java``.

.. _NAPI-java-general-install-unix:

Installation under Unix
=======================

The ``jnexus.so`` shared library as well as all required file backend
``.so`` libraries are required as well as the ``jnexus.jar``
file holding the required Java classes. Copy them wherever you like
and see below for instructions how to run programs using ``jnexus``.

.. _NAPI-java-general-Running:

Running Programs with the NeXus API for Java
############################################

In order to successfully run a program with
``jnexus``, the Java runtime systems needs
to locate two items:

#. The shared library implementing the native methods.

#. The ``nexus.jar`` file in order to find the Java classes.

.. _NAPI-java-general-Running-shared:

Locating the shared libraries
=============================

The methods for locating a shared library differ
between systems. Under Windows32 systems the best method
is to copy the ``jnexus.dll`` and the HDF4, HDF5 and/or XML-library
DLL files into a directory in your path.

On a UNIX system, the problem can be solved in three different ways:

#. Make your system administrator copy the ``jnexus.so``
   file into the systems default shared library directory
   (usually ``/usr/lib`` or ``/usr/local/lib``).

#. Put the ``jnexus.so`` file wherever you see fit and
   set the ``LD_LIBRARY_PATH`` environment variable to
   point to the directory of your choice.

#. Specify the full pathname of the jnexus shared library on
   the java command line with the
   ``-Dorg.nexusformat.JNEXUSLIB=full-path-2-shared-library``
   option.

.. _NAPI-java-general-Running-jnexus:

Locating ``jnexus.jar``
=======================

This is easier, just add the the full pathname to
``jnexus.jar`` to the classpath when starting java.
Here are examples for a UNIX shell and the Windows shell.

.. compound::

    .. rubric:: UNIX example shell script to start ``jnexus.jar``

    .. literalinclude:: examples/napi-java-jnexus.sh
        :tab-width: 4
        :linenos:
        :language: sh

.. compound::

    .. rubric:: Windows 32 example batch file to start ``jnexus.jar``

    .. literalinclude:: examples/napi-java-jnexus.bat
        :tab-width: 4
        :linenos:
        :language: bat

.. _NAPI-java-general-Programming:

Programming with the NeXus API for Java
#######################################

The NeXus C-API is good enough but for Java a few adaptions of
the API have been made in order to match the API better to the
idioms used by Java programmers. In order to understand the
Java-API, it is useful to study the NeXus C-API because many
methods work in the same way as their C equivalents.
A full API documentation is available in Java documentation format.
For full reference look especially at:

- The interface ``NeXusFileInterface`` first.
  It gives an uncluttered view of the API.

- The implementation ``NexusFile`` which gives more details about constructors and
  constants. However this documentation is interspersed with information about
  native methods which should not be called by an application programmer as they
  are not part of the standard and might change in future.

See the following code example for opening a file,
opening a vGroup and closing the file again in order
to get a feeling for the API:

.. compound::

    .. rubric:: fragment for opening and closing

    .. literalinclude:: examples/napi-java-prog1.java
        :tab-width: 4
        :linenos:
        :language: java

Some notes on this little example:

- Each NeXus file is represented by a ``NexusFile`` object which
  is created through the constructor.

- The ``NexusFile`` object takes care of all file handles for you.
  So there is no need to pass in a handle anymore to each
  method as in the C language API.

- All error handling is done through the Java exception
  handling mechanism. This saves all the code checking
  return values in the C language API. Most API functions
  return void.

- Closing files is tricky. The Java garbage collector is
  supposed to call the finalize method for each object it
  decides to delete. In order to enable this mechanism,
  the ``NXclose()`` function was replaced by
  the ``finalize()`` method. In practice it seems
  not to be guaranteed that the garbage collector calls the
  ``finalize()`` method. It is safer to call
  ``finalize()`` yourself in order to properly
  close a file. Multiple calls to the ``finalize()``
  method for the same object are safe and do no harm.

.. _NAPI-java-general-datarw:

Data Writing and Reading
########################

Again a code sample which shows how this looks like:

.. compound::

    .. rubric:: fragment for writing and reading

    .. literalinclude:: examples/napi-java-datarw1.java
        :tab-width: 4
        :linenos:
        :language: java

The dataset is created as usual with ``makedata()`` and opened
with ``putdata()``. The trick is in ``putdata()``.
Java is meant to be type safe. One would think then that a
``putdata()`` method would be required for each Java data type.
In order to avoid this, the data to ``write()`` is passed into
``putdata()`` as type ``Object``.
Then the API proceeds to analyze this object through the
Java introspection API and convert the data to a byte stream for writing
through the native method call. This is an elegant solution with one drawback:
An array is needed at all times. Even if only a single data value is
written (or read) an array of length one and an appropriate type
is the required argument.

Another issue are strings. Strings are first class objects in Java.
HDF (and NeXus) sees them as dumb arrays of bytes. Thus strings have to be
converted to and from bytes when reading string data. See a writing example:

.. compound::

    .. rubric:: String writing

    .. literalinclude:: examples/napi-java-datarw2.java
        :tab-width: 4
        :linenos:
        :language: java

And reading:

.. compound::

    .. rubric:: String reading

    .. literalinclude:: examples/napi-java-datarw2.java
        :tab-width: 4
        :linenos:
        :language: java

The aforementioned holds for all strings written as SDS content or as an
attribute. SDS or vGroup names do not need this treatment.

.. _NAPI-java-general-datarw-inquiry:

Inquiry Routines
################

Let us compare the C-API and Java-API signatures of the
``getinfo()`` routine (C) or method (Java):

.. compound::

    .. rubric:: C API signature of ``getinfo()``

    .. literalinclude:: examples/frag-c-api-sig-getinfo.c
        :tab-width: 4
        :linenos:
        :language: c

.. compound::

    .. rubric:: Java API signature of ``getinfo()``

    .. literalinclude:: examples/frag-c-api-sig-getinfo.java
        :tab-width: 4
        :linenos:
        :language: java

The problem is that Java passes arguments only by value, which means they cannot
be modified by the method. Only array arguments can be modified.
Thus ``args`` in the ``getinfo()`` method holds the
rank and datatype information passed in separate items in the C-API version.
For resolving which one is which, consult a debugger or the API-reference.

The attribute and vGroup search routines have been simplified
using Hashtables. The ``Hashtable`` returned by ``groupdir()``
holds the name of the item as a key and the classname or the string SDS as the
stored object for the key. Thus the code for a vGroup search looks like this:

.. compound::

    .. rubric:: vGroup search

    .. literalinclude:: examples/napi-java-inquiry1.java
        :tab-width: 4
        :linenos:
        :language: java

For an attribute search both at global or SDS level the returned Hashtable
will hold the name as the key and a little class holding the type and size
information as value. Thus an attribute search looks like this in the Java-API:

.. compound::

    .. rubric:: attribute search

    .. literalinclude:: examples/napi-java-inquiry2.java
        :tab-width: 4
        :linenos:
        :language: java

For more information about the usage of the API routines see the reference
or the NeXus C-API reference pages. Another good source of information is
the source code of the test program which exercises each API routine.

.. _NAPI-java-general-knownproblems:

Known Problems
##############

These are a couple of known problems which you might run into:

Memory
    As the Java API for NeXus has to convert between native
    and Java number types a copy of the data must be made
    in the process. This means that if you want to read or
    write 200MB of data your memory requirement will be 400MB!
    This can be reduced by using multiple
    ``getslab()``/``putslab()`` to perform data
    transfers in smaller chunks.

``Java.lang.OutOfMemoryException``
    By default the Java runtime has a low default value for
    the maximum amount of memory it will use.
    This ceiling can be increased through the ``-mxXXm``
    option to the Java runtime. An example:
    ``java -mx512m ...`` starts the Java runtime
    with a memory ceiling of 512MB.

Maximum 8192 files open
    The NeXus API for Java has a fixed buffer for file
    handles which allows only 8192 NeXus files to be
    open at the same time. If you ever hit this limit,
    increase the ``MAXHANDLE`` define in
    ``native/handle.h`` and recompile everything.

.. _NAPI-java-online:

On-line Documentation
#####################

The following documentation is browsable online:

#. `The API source code <https://github.com/nexusformat/code/blob/master/bindings/java/>`_

#. A verbose tutorial for the NeXus for Java API.

#. The API Reference.

#. Finally, the source code for the test driver for the API
   which also serves as a documented usage example.

