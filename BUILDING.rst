The documentation relies on Sphinx (a Python package) for its organization. The
GNU ``make`` program and Python are used to build the NeXus documentation.  The
default build assembles the HTML version.  You have the choice to build the
documentation in two places:

* in the source tree
* out of the source tree

Out-of-Tree documentation
=========================

There are two ways to build out-of-source.

Outside the source tree
-----------------------

To build the NeXus documentation outside the
source tree, 

#. create the target directory for the documentation to be built::

    mkdir /some/where/else

#. note the definitions source directory 
   (the directory where this README file is located)::

    export SOURCE_DIR=/path/to/nexus/definitions

#. copy the source to the target using this NeXus Python tool::

    cd /some/where/else
    python $(SOURCE_DIR)/utils/build_preparation.py $(SOURCE_DIR)

#. build the documentation::

    make clean
    make

The HTML documentation is located in this folder::

    /some/where/else/manual/build/html/


Inside the source tree, in a temporary directory
------------------------------------------------

Alternatively, as is a common practice with `cmake <https://cmake.org/>`_,
you can build *out-of-source* (sort of) in a temporary
``$(SOURCE_DIR)/build`` directory.  For this, the *Makefile*
has the *builddir* rule::

    export SOURCE_DIR=/path/to/nexus/definitions
    cd $(SOURCE_DIR)
    make builddir
    cd build
    make clean
    make

This is all done with one make command::

    export SOURCE_DIR=/path/to/nexus/definitions
    cd $(SOURCE_DIR)
    make makebuilddir

The HTML documentation is located in this folder::

    $(SOURCE_DIR)/build/manual/build/html/

In-Tree documentation
=====================

To build the NeXus documentation within the
source tree, go to the root directory
(the directory where this README file is located),
and type::

    make clean
    make

The HTML documentation is located in this folder::

    ./manual/build/html/
