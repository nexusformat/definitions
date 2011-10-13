## Process this file with cmake
#====================================================================
#  NeXus - Neutron & X-ray Common Data Format
#  
#  CMakeLists for building the NeXus library and applications.
#
#  Copyright (C) 2011 Stephen Rankin
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

find_program(SPHINXBUILD sphinx-build)

# You can set these variables from the command line.
set(SPHINXOPTS)
set(PAPER)
set(BUILDDIR "build")

# Internal variables.
set(PAPEROPT_a4 "-D latex_paper_size=a4")
set(PAPEROPT_letter "-D latex_paper_size=letter")
set(ALLSPHINXOPTS  "-d ${BUILDDIR}/doctrees ${PAPEROPT_a4} ${SPHINXOPTS} ${CMAKE_SOURCE_DIR}/sphinx/source")

add_custom_command(
    OUTPUT ${BUILDDIR}/html
    COMMAND ${SPHINXBUILD}
    ARGS -b html ${ALLSPHINXOPTS} ${BUILDDIR]/html
    DEPENDS ${CMAKE_SOURCE_DIR}/sphinx/source
    COMMENT   "Generating SPHINX BUILD html pages."
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/dirhtml
    COMMAND ${SPHINXBUILD}
    ARGS -b dirhtml ${ALLSPHINXOPTS} ${BUILDDIR]/dirhtml
    DEPENDS ${BUILDDIR}/html
    COMMENT   "Generating SPHINX BUILD dirhtml pages."
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/singlehtml
    COMMAND ${SPHINXBUILD}
    ARGS -b singlehtml ${ALLSPHINXOPTS} ${BUILDDIR]/singlehtml
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT   "Generating SPHINX BUILD singlehtml pages."
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/pickle
    COMMAND ${SPHINXBUILD}
    ARGS -b pickle ${ALLSPHINXOPTS} ${BUILDDIR]/pickle
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT   "Generating SPHINX BUILD pickle pages."
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/json
    COMMAND ${SPHINXBUILD}
    ARGS -b json ${ALLSPHINXOPTS} ${BUILDDIR]/json
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT   "Generating SPHINX BUILD json pages."
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/htmlhelp
    COMMAND ${SPHINXBUILD}
    ARGS -b htmlhelp ${ALLSPHINXOPTS} ${BUILDDIR]/htmlhelp
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished; now you can run HTML Help Workshop with the .hhp project file in ${BUILDDIR}/htmlhelp."
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/qthelp
    COMMAND ${SPHINXBUILD}
    ARGS -b qthelp ${ALLSPHINXOPTS} ${BUILDDIR]/qthelp
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished; now you can run \"qcollectiongenerator\" with the .qhcp project file in ${BUILDDIR}/qthelp, like this:"
    COMMENT "# qcollectiongenerator ${BUILDDIR}/qthelp/NeXusacommondataformatforneutronx-rayandmuonscience.qhcp"
    COMMENT "To view the help file:"
    COMMENT "# assistant -collectionFile ${BUILDDIR}/qthelp/NeXusacommondataformatforneutronx-rayandmuonscience.qhc"
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/devhelp
    COMMAND ${SPHINXBUILD}
    ARGS -b devhelp ${ALLSPHINXOPTS} ${BUILDDIR]/devhelp
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished."
    COMMENT "To view the help file:"
    COMMENT "# mkdir -p $$HOME/.local/share/devhelp/NeXusacommondataformatforneutronx-rayandmuonscience"
    COMMENT "# ln -s ${BUILDDIR}/devhelp $$HOME/.local/share/devhelp/NeXusacommondataformatforneutronx-rayandmuonscience"
    COMMENT "# devhelp"
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/epub
    COMMAND ${SPHINXBUILD}
    ARGS -b epub ${ALLSPHINXOPTS} ${BUILDDIR]/epub
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished. The epub file is in ${BUILDDIR}/epub."
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/epub
    COMMAND ${SPHINXBUILD}
    ARGS -b epub ${ALLSPHINXOPTS} ${BUILDDIR]/epub
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished. The epub file is in ${BUILDDIR}/epub."
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/latex
    COMMAND ${SPHINXBUILD}
    ARGS -b latex ${ALLSPHINXOPTS} ${BUILDDIR]/latex
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished; the LaTeX files are in ${BUILDDIR}/latex."
    COMMENT "Run make in that directory to run these through (pdf)latex"
    COMMENT "(use make latexpdf here to do that automatically)."
) 

add_custom_command(
    OUTPUT ${BUILDDIR}/latex
    COMMAND ${SPHINXBUILD}
    ARGS -b latex ${ALLSPHINXOPTS} ${BUILDDIR]/latex
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished; the LaTeX files are in ${BUILDDIR}/latex."
    COMMENT "Run make in that directory to run these through (pdf)latex"
    COMMENT "(use make latexpdf here to do that automatically)."
) 

#latexpdf: latex
#	@echo "Running LaTeX files through pdflatex..."
#	make -C $(BUILDDIR)/latex all-pdf
#	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

add_custom_command(
    OUTPUT ${BUILDDIR}/latex
    COMMAND ${SPHINXBUILD}
    ARGS -b latex ${ALLSPHINXOPTS} ${BUILDDIR]/latex
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished; the LaTeX files are in ${BUILDDIR}/latex."
    COMMENT "Run make in that directory to run these through (pdf)latex"
    COMMENT "(use make latexpdf here to do that automatically)."
) 

text:
	$(SPHINXBUILD) -b text ${ALLSPHINXOPTS} ${BUILDDIR}/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

add_custom_command(
    OUTPUT ${BUILDDIR}/latex
    COMMAND ${SPHINXBUILD}
    ARGS -b latex ${ALLSPHINXOPTS} ${BUILDDIR]/latex
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished; the LaTeX files are in ${BUILDDIR}/latex."
    COMMENT "Run make in that directory to run these through (pdf)latex"
    COMMENT "(use make latexpdf here to do that automatically)."
) 

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

add_custom_command(
    OUTPUT ${BUILDDIR}/latex
    COMMAND ${SPHINXBUILD}
    ARGS -b latex ${ALLSPHINXOPTS} ${BUILDDIR]/latex
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished; the LaTeX files are in ${BUILDDIR}/latex."
    COMMENT "Run make in that directory to run these through (pdf)latex"
    COMMENT "(use make latexpdf here to do that automatically)."
) 

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

add_custom_command(
    OUTPUT ${BUILDDIR}/latex
    COMMAND ${SPHINXBUILD}
    ARGS -b latex ${ALLSPHINXOPTS} ${BUILDDIR]/latex
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished; the LaTeX files are in ${BUILDDIR}/latex."
    COMMENT "Run make in that directory to run these through (pdf)latex"
    COMMENT "(use make latexpdf here to do that automatically)."
) 

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

add_custom_command(
    OUTPUT ${BUILDDIR}/latex
    COMMAND ${SPHINXBUILD}
    ARGS -b latex ${ALLSPHINXOPTS} ${BUILDDIR]/latex
    DEPENDS ${BUILDDIR}/dirhtml
    COMMENT "Build finished; the LaTeX files are in ${BUILDDIR}/latex."
    COMMENT "Run make in that directory to run these through (pdf)latex"
    COMMENT "(use make latexpdf here to do that automatically)."
) 

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

