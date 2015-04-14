#=============================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
# Copyright (C) 2008-2012 NeXus International Advisory Committee (NIAC)
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
#==============================================================================

add_subdirectory(img)
add_subdirectory(_static)
add_subdirectory(_templates)
add_subdirectory(classes)
add_subdirectory(examples)

set(FILES applying-nexus.rst
          authorgroup.rst
          colophon.rst
          community.rst
          copyright.rst
          datarules.rst
          defs_intro.rst
          design.rst
          docs_about.rst
          faq.rst
          fileformat.rst
          github.rst
          history.rst
          index.rst
          installation.rst
          introduction-napi.rst
          introduction.rst
          issues.rst
          mailinglist.rst
          motivations.rst
          napi-c.rst
          napi-f77.rst
          napi-f90.rst
          napi-idl.rst
          napi-java.rst
          napi-python.rst
          napi.rst
          nexuslogo.png
          niac.rst
          nxdl.rst
          nxdl-types.rst
          preface.rst
          ref_doc.rst
          revhistory.rst
          rules.rst
          strategies.rst
          user_manual.rst
          utilities.rst
          validation.rst
          FDL
          NeXusIntern.pdf
          )

foreach(F ${FILES})
    configure_file(${F} ${F} COPYONLY)
endforeach()

configure_file(conf.py.in conf.py @ONLY)



