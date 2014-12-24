## Process this file with cmake
#====================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
# Copyright (C) 2008-2014 NeXus International Advisory Committee (NIAC)
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

find_package(Sphinx REQUIRED)

# You can set these variables from the command line.
set(SPHINXOPTS)
set(PAPER a4)
set(BUILDDIR "${CMAKE_BINARY_DIR}/manual/build")
set(SOURCEDIR "${CMAKE_BINARY_DIR}/manual/source")

# Internal variables.
set(PAPEROPT_a4 -D latex_paper_size=a4)
set(PAPEROPT_letter -D latex_paper_size=letter)
set(ALLSPHINXOPTS  -d ${BUILDDIR}/doctrees ${PAPEROPT_${PAPER}} ${SPHINXOPTS} ${SOURCEDIR})

add_subdirectory(source)

#	@echo "Please use \`make <target>' where <target> is one of"
#	@echo "  html       to make standalone HTML files"
#	@echo "  dirhtml    to make HTML files named index.html in directories"
#	@echo "  singlehtml to make a single large HTML file"
#	@echo "  pickle     to make pickle files"
#	@echo "  json       to make JSON files"
#	@echo "  htmlhelp   to make HTML files and a HTML help project"
#	@echo "  qthelp     to make HTML files and a qthelp project"
#	@echo "  devhelp    to make HTML files and a Devhelp project"
#	@echo "  epub       to make an epub"
#	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
#	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
#	@echo "  text       to make text files"
#	@echo "  man        to make manual pages"
#	@echo "  changes    to make an overview of all changed/added/deprecated items"
#	@echo "  linkcheck  to check all external links for integrity"
#	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"

set(linkcheck_comment "Link check complete; look for any errors in the above output or in ${BUILDDIR}/linkcheck/output.txt.")
set(changes_comment "The overview file is in ${BUILDDIR}/changes.")
set(doctest_comment "Testing of doctests in the sources finished, look at the results in ${BUILDDIRR}/doctest/output.txt.")
set(htmlhelp_comment "Build finished; now you can run HTML Help Workshop with the .hhp project file in ${BUILDDIR}/htmlhelp.")
set(qthelp_comment "
Build finished; now you can run \"qcollectiongenerator\" with the .qhcp project file in ${BUILDDIR}/qthelp, like this:
# qcollectiongenerator ${BUILDDIR}/qthelp/NeXusacommondataformatforneutronx-rayandmuonscience.qhcp
To view the help file:
# assistant -collectionFile ${BUILDDIR}/qthelp/NeXusacommondataformatforneutronx-rayandmuonscience.qhc
")
set(devhelp_comment "
Build finished.
To view the help file:
# mkdir -p $$HOME/.local/share/devhelp/NeXusacommondataformatforneutronx-rayandmuonscience
# ln -s ${BUILDDIR}/devhelp $$HOME/.local/share/devhelp/NeXusacommondataformatforneutronx-rayandmuonscience
# devhelp
")
set(latex_comment "Build finished; the LaTeX files are in ${BUILDDIR}/latex. Run 'make' in that directory to run these through (pdf)latex (use 'make latexpdf' here to do that automatically).")

# make copy of source tree, this is because we generate some files and need all in same place
if (NOT (${CMAKE_CURRENT_SOURCE_DIR} STREQUAL ${CMAKE_CURRENT_BINARY_DIR}))
    file(COPY source/ DESTINATION source)
endif()
# create conf.py after substituting various CMake @MACRO@ values
configure_file(
    "source/conf.py.in"
    "source/conf.py"
    @ONLY)

# all possible build targets
foreach(VAL html dirhtml singlehtml pickle json htmlhelp qthelp epub latex text man changes linkcheck doctest)
    add_custom_command(
        OUTPUT ${BUILDDIR}/${VAL}
        COMMAND ${SPHINX_EXECUTABLE}
        ARGS -b ${VAL} ${ALLSPHINXOPTS} ${BUILDDIR}/${VAL}
        DEPENDS manual-source
        COMMENT   "${${VAL}_comment}"
    ) 
    add_custom_target(${VAL}-manual DEPENDS manual-source "${BUILDDIR}/${VAL}")
    set_target_properties(${VAL}-manual PROPERTIES OUTPUT_NAME ${VAL})
endforeach(VAL)

SET_DIRECTORY_PROPERTIES(PROPERTIES ADDITIONAL_MAKE_CLEAN_FILES "${BUILDDIR}/doctrees;${BUILDDIR}/latex")


# subset of above targets to build by default
add_custom_target(default-manual ALL)
foreach(VAL complete)
    add_dependencies(default-manual ${VAL}-manual)
endforeach(VAL)

add_custom_target(realclean-manual COMMAND ${CMAKE_COMMAND} -E remove_directory ${BUILDDIR})
set_target_properties(realclean-manual PROPERTIES OUTPUT_NAME realclean)

add_custom_target(rebuild-manual DEPENDS realclean complete)
set_target_properties(rebuild-manual PROPERTIES OUTPUT_NAME rebuild)

add_custom_target(complete-manual
    DEPENDS html-manual latexpdf-manual
    COMMENT "Build finished. The HTML and PDF pages are in ${BUILDDIR}/html."
)
set_target_properties(complete-manual PROPERTIES OUTPUT_NAME complete)

add_custom_target(latexpdf-manual
    COMMAND make -C ${BUILDDIR}/latex all-pdf
    DEPENDS latex-manual
    COMMENT "Running latex through pdflatex"
)
set_target_properties(latexpdf-manual PROPERTIES OUTPUT_NAME latexpdf)

add_custom_command(
    TARGET latexpdf-manual
    POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy ${BUILDDIR}/latex/nexus.pdf ${SOURCEDIR}/nexus.pdf
    DEPENDS latexpdf-manual ${BUILDDIR}/latex/nexus.pdf
    COMMENT "Copy PDF to ${SOURCEDIR}/"
)

install(DIRECTORY ${BUILDDIR}/html DESTINATION ${NEXUS_MANUAL} COMPONENT manual)
install(DIRECTORY ${BUILDDIR}/latex/ DESTINATION ${NEXUS_MANUAL}/pdf COMPONENT manual FILES_MATCHING PATTERN "*.pdf")
