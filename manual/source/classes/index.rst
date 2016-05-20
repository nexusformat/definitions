.. index::
     ! class definitions

.. _all.class.definitions:

NeXus Class Definitions
#########################

Definitions of NeXus classes. These are split into base_classes (low level objects), 
application definitions (groupings of objects for a particular technique) and 
contributed_definitions (proposed definitions from the community)

:ref:`base classes <base.class.definitions>`
    NeXus base class definitions define the set of terms that
    *might* be used in an instance of that class.
    Consider the base classes as a set of *components*
    that are used to construct a data file.

:ref:`application definitions <application.definitions>`
    NeXus application definitions define the *minimum*
    set of terms that
    *must* be used in an instance of that class.
    Application definitions also may define terms that
    are optional in the NeXus data file.

:ref:`contributed definitions <contributed.definitions>`
    NXDL files in the NeXus contributed definitions include propositions from
    the community for NeXus base classes or application definitions, as well
    as other NXDL files for long-term archival by NeXus.  Consider the contributed
    definitions as either in *incubation* or a special
    case not for general use.

.. toctree::
    :hidden:
    
    base_classes/index
    applications/index
    contributed_definitions/index
