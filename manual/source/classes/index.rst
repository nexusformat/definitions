.. _ClassDefinitions:

=======================
NeXus class definitions
=======================

..
	.. image:: img/NeXus.png

Information is stored in a NeXus data file by grouping together similar parts.
For example, information about the sample could include a descriptive name, the
temperature, and other items.  NeXus specifies the contents of these groupings
using *classes*.  In some parts of this manual, these
classes might be called *group type* or some similar term.
In this section, the NeXus classes are described in detail.  Each class is specified
using :ref:`NXDL`, described in a separate chapter.

There are three types of NeXus class file: base classes, application definitions, 
and contributed definitions.  Base class definitions define the *complete* set of 
terms that *might* be used in an instance of that class.  Application definitions 
define the *minimum* set of terms that *must* be used in an instance of that class.  
Contributed definitions include propositions from the community for NeXus base 
classes or application definitions, as well as other NXDL files for long-term 
archival by NeXus.

NeXus Class Specifications
##########################

.. toctree::
	:maxdepth: 1
	
	overview

.. rubric:: Descriptions of the NeXus classes

.. toctree::
   :maxdepth: 1
   
   base_classes/index
   applications/index
   contributed_definitions/index
