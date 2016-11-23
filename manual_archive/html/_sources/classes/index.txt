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
    
    Base class definitions are permissive rather than restrictive.
    While the terms defined aim to cover most possible use cases,
    and to codify the spelling and meaning of such terms,
    the class specifications cannot list all acceptable groups and fields.
    To be able to progress the NeXus standard, additional data
    (groups, fields, attributes) are acceptable in NeXus HDF5 data files.

    Users are encouraged to find the best *defined* location in which 
    to place their information.  It is understood there is not a 
    predefined place for all possible data.
    
    Validation procedures should treat such additional items 
    (not covered by a base class specification) as notes or warnings
    rather than errors.  

:ref:`application definitions <application.definitions>`
    NeXus application definitions define the *minimum*
    set of terms that
    *must* be used in an instance of that class.
    Application definitions also may define terms that
    are optional in the NeXus data file.
    
    As in base classes (see above), additional terms that are
    not described by the application definition, may be added to
    data files that incorporate or adhere to application definitions.

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
