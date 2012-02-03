cmake is now used to generate the initial "Makefile" (or whatever other build system you wish to use) and to package files. For example on unix you could type from the top source directory:

    cmake .
    make
    make install  #  or   make install DESTDIR=/some/where    for testing
    make package  #  build install kit

cmake can be used for "out of source" building, and this is recommended as it keeps source and generated files separate, so e.g.

    mkdir /some/where/else
    cd /some/where/else
    cmake /path/to/nexus/definitions/source
    make

To see what options can be configured, or to use another builder, type:

    cmake-gui

the choose the source and build directories, press "configure" and then "generate"

To see options etc. from the command line, type

    cmake -L # or  cmake -LH  to see help too

These values can be set in the gui or from the command line e.g.
in the top of the build directory run

    cmake -DBUILD_SPHINX=ON .  # set BUILD_SPHINX option for subsequent "make"
