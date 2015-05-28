#====================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
# Copyright (C) 2008-2015 NeXus International Advisory Committee (NIAC)
#  
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
# 
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
# 
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free 
#  Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, 
#  MA  02111-1307  USA
#             
#  For further information, see <http://www.nexusformat.org>
#
#
#====================================================================

set(FILES  abbreviated-nexus-file.xml.txt
           array-dimensions1.xml.txt
           array-dimensions2.xml.txt
           array-dimensions3.xml.txt
           array-dimensions.xml.txt
           axes-old.xml.txt
           axes-preferred.xml.txt
           code_napi.rst
           code_native.rst
           complex-hkl-scan.txt
           data-linking.xml.txt
           euler-cif.txt
           examples-prototype.txt
           ex-c-read.c
           ex-c-write.c
           ex-simple.c
           ex-svn-commit-message-syntax.txt
           ex-unix-using-nxbrowse.txt
           frag-c-api-sig-getinfo.c
           frag-c-api-sig-getinfo.java
           h5dump_attribute.txt
           h5dump_field.txt
           h5dump_group.txt
           h5dump_link.txt
           hierarchy-processed.txt
           hierarchy-raw.txt
           hierarchy-subentry.txt
           index.rst
           mapping1.xml.txt
           mapping2.xml.txt
           napi-example.c
           napi-example.f77
           napi-example.f90
           napi-java-datarw1.java
           napi-java-datarw2.java
           napi-java-datarw3.java
           napi-java-inquiry1.java
           napi-java-inquiry2.java
           napi-java-jnexus.bat
           napi-java-jnexus.sh
           napi-java-prog1.java
           nxcollection.txt
           nxdl-doc-fragment-simple.xml
           nxdl-trac6-ex1.xml.txt
           nxdl-trac6-ex2.xml.txt
           nxh5read.c
           nxh5write.c
           NXshellMono.txt
           NXshell.txt
           NX__template__.nxdl.xml
           NXwoni.nxdl.xml
           offset-stride-1d.txt
           offset-stride-2d.txt
           offset-stride-3d.txt
           simple3D.h5
           simple3D.h5dump.txt
           simple3D.py
           simple3D.xture.txt
           simplescanarea.txt
           simplescan.txt
           verysimple.nx5
           verysimple.nxdl.xml
           verysimple.py
           verysimple.txt
           verysimple.xml
           woni-mapping-basic.txt
           woni-mapping-nxdata.txt
           woni-nxdl-data.nxdl
           woni-nxdl-group.nxdl
           xas.txt
          )

add_subdirectory(lrmecs)
add_subdirectory(h5py)

foreach(F ${FILES})
    configure_file(${F} ${F} COPYONLY)
endforeach()
