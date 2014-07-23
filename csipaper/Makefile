# latex makefile by tobias 2014-07-23

MAINDOC=nexus14aip
INCDOCS=

SUBDIRS=

pdf:    subdirs $(MAINDOC).pdf

subdirs:
	for i in $(SUBDIRS) ; do cd $$i ; make ; done

todo:
	pdflatex  $(MAINDOC) 2>&1 | grep '^TODO' | tee /dev/stderr | echo Total number of `wc -l` todos.

undef:
	pdflatex  $(MAINDOC) 2>&1 | grep undefined || echo all defined

$(MAINDOC).aux: $(MAINDOC).tex $(INCDOC)
	-pdflatex $(MAINDOC).tex

$(MAINDOC).bbl: $(MAINDOC).bib $(MAINDOC).aux
	bibtex $(MAINDOC)

$(MAINDOC).ind: $(MAINDOC).idx $(MAINDOC).ist
	makeindex -s $(MAINDOC).ist -g $(MAINDOC).idx

$(MAINDOC).idx: $(MAINDOC).tex
	-pdflatex $(MAINDOC).tex

#$(MAINDOC).bst: $(MAINDOC).dbj
	#-pdflatex $(MAINDOC).dbj

$(MAINDOC).pdf: $(MAINDOC).tex $(MAINDOC).aux $(MAINDOC).bbl
	-pdflatex $(MAINDOC).tex 
	@wc -c $(MAINDOC).pdf

$(MAINDOC).ps: pdf
	pdftops $(MAINDOC).pdf

show:   $(MAINDOC).dvi
	xdvi $(MAINDOC)

force: 
	touch $(MAINDOC).tex
	make
        
spellcheck:
	ispell -C -d american $(MAINDOC).tex

