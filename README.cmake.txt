cmake is now used to generate the initial "Makefile" (or whatever other build system you wish to use) and to package files. It is advised to do the build in an "out of source" directory such as a "build" directory.  For example on unix you could type from the top source directory:

    mkdir build
    cd build
    cmake ..
    make
    make install  #  or   make install DESTDIR=/some/where    for testing
    make package  #  build install kit

To see a list of makefile targets, type:

	make help
	
If you get an error saying something like:

> CMake Error at CMakeLists.txt:29 (cmake_minimum_required):
> CMake 2.8.4 or higher is required. You are running version 2.8.3

Then you either meed to install a later version of cmake or could try changing the cmake_minimum_required() line in CMakeLists.txt 
to a lower number; however it possible that necessary features/behaviour is missing in the lower version  
	
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

But this is just an example.  The sphinx version of the manual is not ready to use cmake.

