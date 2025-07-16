# File: Makefile

# purpose:
#	build resources in NeXus definitions tree

PYTHON = python3
SPHINX = sphinx-build
BUILD_DIR = build
BASE_CLASS_DIR = base_classes
CONTRIB_DIR = contributed_definitions
APPDEF_DIR = applications
NYAML_SUBDIR = nyaml

YBC_NXDL_TARGETS = $(patsubst %.yaml,%.nxdl.xml,$(subst /nyaml/,/, $(wildcard $(BASE_CLASS_DIR)/nyaml/*.yaml)))
YCONTRIB_NXDL_TARGETS = $(patsubst %.yaml,%.nxdl.xml,$(subst /nyaml/,/, $(wildcard $(CONTRIB_DIR)/nyaml/*.yaml)))
YAPPDEF_NXDL_TARGETS = $(patsubst %.yaml,%.nxdl.xml,$(subst /nyaml/,/, $(wildcard $(APPDEF_DIR)/nyaml/*.yaml)))


.PHONY: help install style autoformat test clean prepare html pdf impatient-guide all local nxdl nyaml

help ::
	@echo ""
	@echo "NeXus: Testing the NXDL files and building the documentation:"
	@echo ""

	@echo "make install            Install all requirements to run tests and builds."
	@echo "make style              Check python coding style."
	@echo "make autoformat         Format all files to the coding style conventions."
	@echo "make test               Run NXDL syntax and documentation tests."
	@echo "make clean              Remove all build files."
	@echo "make spellcheck         Run a spellcheck across all definitions."
	@echo "make prepare            (Re)create all build files."
	@echo "make html               Build HTML version of manual. Requires prepare first."
	@echo "make pdf                Build PDF version of manual. Requires prepare first."
	@echo "make impatient-guide    Build html & PDF versions of the Guide for the Impatient. Requires prepare first."
	@echo "make all                Builds complete web site for the manual (in build directory)."
	@echo "make local              (Developer use) Test, prepare and build the HTML manual."
	@echo "make nxdl               Build NXDL files from NYAML files in nyaml subdirectories."
	@echo "make nyaml              Build NYAML files to nyaml subdirectories from NXDL files."
	@echo ""
	@echo "Note:  All builds of the manual will occur in the 'build/' directory."
	@echo "   For a complete build, run 'make all' in the root directory."
	@echo "   Developers of the NeXus class definitions can use 'make local' to"
	@echo "   confirm the documentation builds."
	@echo ""

install ::
	$(PYTHON) -m pip install -r requirements.txt

style ::
	$(PYTHON) -m black --check dev_tools
	$(PYTHON) -m flake8 dev_tools
	$(PYTHON) -m isort --check dev_tools

autoformat ::
	$(PYTHON) -m black dev_tools
	$(PYTHON) -m isort dev_tools

test ::
	$(PYTHON) -m pytest dev_tools

clean ::
	$(RM) -rf $(BUILD_DIR)
	$(RM) -rf $(BASE_CLASS_DIR)/$(NYAML_SUBDIR)
	$(RM) -rf $(APPDEF_DIR)/$(NYAML_SUBDIR)
	$(RM) -rf $(CONTRIB_DIR)/$(NYAML_SUBDIR)

spellcheck ::
	@command -v cspell >/dev/null 2>&1 || { echo >&2 "cspell is not installed. Install it with: npm install -g cspell"; exit 1; }
	@echo "Running spellcheck with cspell..."
	cspell --config cspell.json "${APPDEF_DIR}/**/*" "${BASE_CLASS_DIR}/**/*" "${CONTRIB_DIR}/**/*"

prepare ::
	$(PYTHON) -m dev_tools manual --prepare --build-root $(BUILD_DIR)
	$(PYTHON) -m dev_tools impatient --prepare --build-root $(BUILD_DIR)

pdf ::
	$(SPHINX) -M latexpdf $(BUILD_DIR)/manual/source/ $(BUILD_DIR)/manual/build
	cp $(BUILD_DIR)/manual/build/latex/nexus.pdf $(BUILD_DIR)/manual/source/_static/NeXusManual.pdf

html ::
	$(SPHINX) -b html -W $(BUILD_DIR)/manual/source/ $(BUILD_DIR)/manual/build/html

impatient-guide ::
	$(SPHINX) -b html -W $(BUILD_DIR)/impatient-guide/ $(BUILD_DIR)/impatient-guide/build/html
	$(SPHINX) -M latexpdf $(BUILD_DIR)/impatient-guide/ $(BUILD_DIR)/impatient-guide/build
	cp $(BUILD_DIR)/impatient-guide/build/latex/NXImpatient.pdf $(BUILD_DIR)/manual/source/_static/NXImpatient.pdf

# for developer's use on local build host
local ::
	$(MAKE) test
	$(MAKE) prepare
	$(MAKE) html

all ::
	$(MAKE) clean
	$(MAKE) prepare
	$(MAKE) impatient-guide
	$(MAKE) pdf
	$(MAKE) html
	@echo "HTML built: `ls -lAFgh $(BUILD_DIR)/impatient-guide/build/html/index.html`"
	@echo "PDF built: `ls -lAFgh $(BUILD_DIR)/impatient-guide/build/latex/NXImpatient.pdf`"
	@echo "HTML built: `ls -lAFgh $(BUILD_DIR)/manual/build/html/index.html`"
	@echo "PDF built: `ls -lAFgh $(BUILD_DIR)/manual/build/latex/nexus.pdf`"

$(BASE_CLASS_DIR)/%.nxdl.xml : $(BASE_CLASS_DIR)/$(NYAML_SUBDIR)/%.yaml
	nyaml2nxdl $< --output-file $@

$(CONTRIB_DIR)/%.nxdl.xml : $(CONTRIB_DIR)/$(NYAML_SUBDIR)/%.yaml
	nyaml2nxdl $< --output-file $@

$(APPDEF_DIR)/%.nxdl.xml : $(APPDEF_DIR)/$(NYAML_SUBDIR)/%.yaml
	nyaml2nxdl $< --output-file $@

nxdl: $(YBC_NXDL_TARGETS) $(YCONTRIB_NXDL_TARGETS) $(YAPPDEF_NXDL_TARGETS)

nyaml:
	$(MAKE) -f nyaml.mk


# NeXus - Neutron and X-ray Common Data Format
#
# Copyright (C) 2008-2024 NeXus International Advisory Committee (NIAC)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For further information, see http://www.nexusformat.org
