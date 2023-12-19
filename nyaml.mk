BASE_CLASS_DIR := base_classes
CONTRIB_DIR := contributed_definitions
APPDEF_DIR := applications
NYAML_SUBDIR := nyaml
NXDL_BC = $(addprefix $(BASE_CLASS_DIR)/nyaml/,$(notdir $(patsubst %.nxdl.xml,%.yaml,$(wildcard $(BASE_CLASS_DIR)/*.nxdl.xml))))
NXDL_APPDEF = $(addprefix $(APPDEF_DIR)/nyaml/,$(notdir $(patsubst %.nxdl.xml,%.yaml,$(wildcard $(APPDEF_DIR)/*.nxdl.xml))))
NXDL_CONTRIB = $(addprefix $(CONTRIB_DIR)/nyaml/,$(notdir $(patsubst %.nxdl.xml,%.yaml,$(wildcard $(CONTRIB_DIR)/*.nxdl.xml))))

.PHONY: all nyaml

$(BASE_CLASS_DIR)/$(NYAML_SUBDIR)/%.yaml : $(BASE_CLASS_DIR)/%.nxdl.xml
	nyaml2nxdl $< --output-file $@

$(CONTRIB_DIR)/$(NYAML_SUBDIR)/%.yaml : $(CONTRIB_DIR)/%.nxdl.xml
	nyaml2nxdl $< --output-file $@

$(APPDEF_DIR)/$(NYAML_SUBDIR)/%.yaml : $(APPDEF_DIR)/%.nxdl.xml
	nyaml2nxdl $< --output-file $@

nyaml: $(NXDL_BC) $(NXDL_APPDEF) $(NXDL_CONTRIB)

all: nyaml
