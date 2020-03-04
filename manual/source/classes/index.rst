.. index::
     ! class definitions

.. _all.class.definitions:

NeXus Class Definitions
#######################

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
    not described by the application definition may be added to
    data files that incorporate or adhere to application definitions. 
    
    .. index:: link
    
    Use NeXus links liberally in data files to reduce duplication of data.
    In application definitions involving raw data,
    write the raw data in the :ref:`NXinstrument` tree and then link to it
    from the location(s) defined in the relevant application definition.
    See figure :ref:`NeXus Multi Method Hierarchy <table.NXsubentry>`
    for an example.
    
    .. index:: subentry; NXsubentry, use of, multi-modal data
    
    To write a data file with an application definition, start with either
    a :ref:`NXentry` (or :ref:`NXsubentry`) group [#]_ and write the name of the
    application definition in the ``definition`` field.  Then write data into 
    this group according to the specifications of the application definition.
    
    .. [#] For data files involving just an application definition, use
       the :ref:`NXentry` group.  Such as this structure::
       
         entry:NXentry
            definition="NXsas"
       
       For files that describe multi-modal
       data and require use of two or more application definitions
       (such as :ref:`NXsas` *and* :ref:`NXcanSAS`), you must place each
       application definition in a :ref:`NXsubentry` of the :ref:`NXentry` group.
       Such as this structure::
       
         entry:NXentry
            raw:NXsubentry
               definition="NXsas"
            reduced:NXsubentry
               definition="NXcanSAS"
            fluo:NXsubentry
               definition="NXfluo"
       
       If you anticipate your data file will eventually require an additional
       application definition, you should start with each application definition
       in a :ref:`NXsubentry` group.

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
