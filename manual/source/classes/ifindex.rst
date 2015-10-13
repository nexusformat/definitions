.. $Id: index.rst 1246 2013-11-20 11:14:52Z Mark Koennecke $

.. _ClassDefinitions:

=========================================================
NeXus class definitions with Interfaces (Experimental)
=========================================================

..
	.. image:: img/NeXus.png


EXPERIMENTAL
-----------------

This section is experimental and is not an accepted part of the NeXus standard. 
It shows how NeXus base classes can be improved by introducing NeXus 
interfaces.  


EXPERIMENTAL
-----------------

Information is stored in a NeXus data file by grouping together similar parts.
For example, information about the sample could include a descriptive name, the
temperature, and other items.  NeXus specifies the contents of these groupings
using *classes*.  In some parts of this manual, these
classes might be called *group type* or some similar term.
In this section, the NeXus classes are described in detail.  Each class is specified
using :ref:`NXDL`, described in a separate chapter.

There are four types of NeXus class file: base classes, interfaces, application definitions, 
and contributed definitions.  Base class definitions define the *complete* set of 
terms that *might* be used in an instance of that class. Base classes can implement interfaces.
Interfaces are used in base class definitions for two purposes:

1. In order to describe fields used by more then one base class. A good example is NXIFbeamline_component 
   which holds the fields necessary to position a component in the beamline. Naturally, many classe need 
   these fields.
2. When a class has become to complex and implements multiple use cases. A prime example is NXdetector which 
   can describe many kinds of detectors. In order to be more specific about detectors, interfaces are used.  
 
Application definitions 
define the *minimum* set of terms that *must* be used in an instance of that class.  
Contributed definitions include propositions from the community for NeXus base 
classes or application definitions, as well as other NXDL files for long-term 
archival by NeXus.




NeXus Class Specifications
##########################

.. toctree::
    :maxdepth: 1
    :glob:
    
    ifbase_classes/index
    interfaces/index

