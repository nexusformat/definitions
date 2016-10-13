.. _IFReferenceDocumentation:

=============================================================
NeXus: Interfaces Reference Documentation (Experimental)
=============================================================

.. image:: img/NeXus.png
    :width: 40%

.. toctree::
    :maxdepth: 1
    :glob:


.. caution:: EXPERIMENTAL
   This section is **experimental and is NOT an accepted part of the NeXus standard**. 
   It shows how NeXus base classes can be improved by introducing NeXus 
   interfaces. 


Introduction
#################

When defining NeXus base classes the NeXus community encountered two reoccurring problems:

1. Some fields, for example for positioning a component in the beam, are shared between many 
   components.
2. Some base classes, for example NXdetector, describe a whole set of different pieces of 
   equimpment and thus have become to complex. 

The classical way to solve this problem would have been to use inheritance. But this would have 
complicated the NeXus hierarchy even further and causes problems with backwards compatability. 
Also there would have been cases of multiple inheritance where things turn really messy. Instead 
the NeXus community decided to solve the problem with interfaces. Interfaces detail the fields 
necessary to describe either a shared or special concept. A set of interfaces are  
defined which a base class can implement. The interfaces which  a
given base class can implements  are stored as a group attribute with
the name **implements**
which becomes a komma separated list of interfaces.   In a real file
the **implements** attribute would hold the information which
interfaces are actually implemented by this isntance of a group.

NeXus interfaces are up to now only used to improve the definition of base classes. 

Information is stored in a NeXus data file by grouping together similar parts.
For example, information about the sample could include a descriptive name, the
temperature, and other items.  NeXus specifies the contents of these groupings
using *classes*.  In some parts of this manual, these
classes might be called *group type* or some similar term.
In this section, the NeXus classes are described in detail.  Each class is specified
using :ref:`NXDL`, described in a separate chapter.


WARNINGS
##############

As this is experimental, some things are not as they should be:

* The base classes used here were derived 2-3 years ago. So, there may be things missing 
  or in need of change. 
* The application definitions are NOT given. They are not affected by interfaces. Though 
  it may be an idea to extend the interfaces idea to application definitions to. Tobias 
  features operate along these lines. 




NeXus Class Specifications
##########################

.. toctree::
    :maxdepth: 1
    :glob:
    
    classes/ifbase_classes/index
    classes/interfaces/index


