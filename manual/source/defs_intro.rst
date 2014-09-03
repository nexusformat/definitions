.. _ClassDefinitions:

=================================
Introduction to NeXus definitions
=================================

..
	.. image:: img/NeXus.png

While the design principles of NeXus are explained in the :ref:`UserManual`, this Reference Documentation specifies all allowed :ref:`base classes <base.class.definitions>` and all standardized :ref:`application definitions <application.definitions>`. Furthermore, it also contains :ref:`contributed definitions <contributed.definitions>` of new bases classes or application definitions that are currently under review.

Base class definitions and application definitions have basically the same structure, but different semantics: Base class definitions define the *complete* set of 
terms that *might* be used in an instance of that class.  Application definitions 
define the *minimum* set of terms that *must* be used in an instance of that class.  

Base classes and application definitions are specified using a domain-specific XML scheme, the :ref:`NXDL`.

.. _ClassDefinitions-Overview:

Overview of NeXus definitions
-----------------------------

.. index:: NXDL

For each class definition, the documentation is derived from content
provided in the NXDL specification.

The documentation for each class consists of:

#. **short table**:

   * the current version of the NXDL specification used for the class
   * the category of the class (base class / application definition / contributed definition)
   * The  NeXus class extended by this class. 
     Most NeXus base classes only extend the base class definition (NXDL).
   * any other base classes (groups) cited by this class

#. **symbol list**:
     keywords used to designate array dimensions. At present, this list is not guaranteed to be complete (some array dimension names appear only in the description column of the class member table, and not here)
#. **source**:
     a link to the authorative NXDL source
#. **tree outline**:
     hierarchical list of members.
#. **member table**:
     list of top-level members with natural-language annotations.
#. **supplementary member tables** as needed:
     member tables of subgroups.


Tree outlines
-------------

A compact listing of the basic structure
(groups, fields, dimensions, attributes, and links)
is prepared for each NXDL specification.  Indentation shows
nested structure.  *Attributes* are prepended with the ``@``
symbol.
*Links* use the characters ``-->`` to represent the path to the intended source of the information.

Member tables
-------------

Member tables provide basic information about each field or group in
the class. An example of the varieties of specifications are given in the following
table using items found in various NeXus base classes.

.. tabularcolumns:: |l|L|l|L|

=================== ========================================================= ========= ================================================================
Name                Type                                                      Units     Description (and Occurrences)
=================== ========================================================= ========= ================================================================
``program_name``    NX_CHAR                                                             Name of program used to generate this file
``@version``        NX_CHAR                                                             Program version number

                                                                                        Occurences: 1 : *default*
``@configuration``  NX_CHAR                                                             configuration of the program
``thumbnail``       :ref:`NXnote`                                                       A small image that is representative of the entry. An example of
                                                                                        this is a 640x480 JPEG image automatically produced by a low
                                                                                        resolution plot of the NXdata.
``@mime_type``      NX_CHAR                                                             expected: *mime_type="image/\*"*

..                  :ref:`NXgeometry`                                                   describe the geometry of this class
``distance``        NX_FLOAT                                                  NX_LENGTH Distance from sample
``mode``            "Single Bunch"                                                      source operating mode
                    | "Multi Bunch"
``target_material`` Ta                                                                  Pulsed source target material
                    | W
                    | depleted_U
                    | enriched_U
                    | Hg
                    | Pb
                    | C
=================== ========================================================= ========= ================================================================

The columns in the table are described as follows:

:Name (and attributes):
    Name of the data field.
    Since ``name`` needs to be restricted to valid
    program variable names,
    no "``-``" characters can be allowed.
    Name must satisfy both 
    :index:`HDF <rules; HDF>` and :index:`XML <rules; XML>`
    :index:`naming <rules; naming>`.

	.. code-block:: guess
	    :linenos:

		NameStartChar ::=  _ | a..z | A..Z
		NameChar      ::=  NameStartChar | 0..9
		Name          ::=  NameStartChar (NameChar)*
		
		Or, as a regular expression:    [_a-zA-Z][_a-zA-Z0-9]*
		equivalent regular expression:  [_a-zA-Z][\w_]*

    :index:`Attributes <! attribute>`,
    identified with a leading "at" symbol (``@``)
    and belong with the preceding field or group,
    are additional metadata used to define this field or group.
    In the example above, the
    ``program_name`` element has two attributes:
    ``version`` (required) and
    ``configuration`` (optional) while the
    ``thumbnail`` element has one attribute:
    ``mime_type`` (optional).
    
    For groups, the name may not be declared in the NXDL specification.
    In such instances, the *value shown in parentheses* in the
    *Name and Attributes* column is a suggestion, obtained from the 
    group by removing the "NX" prefix.
    See :ref:`NXentry` for examples.


:Type:
    Type of data to be represented by this variable.
    The type is one of those specified in :ref:`NXDL`.
    In the case where the variable can take only one value from a known
    list, the list of known values is presented, such as in the
    ``target_material`` field above:
    ``Ta | W | depleted_U | enriched_U | Hg | Pb | C``.
    Selections with included whitespace are surrounded by quotes. See the
    example above for usage.

    For fields, the data type may not be specified in the NXDL file.
    The *default data type* is NX_CHAR and this is *shown in parentheses* in the *Type* column.
    See :ref:`NXdata` for examples.

:Units:
    :index:`Data units <units>`,
    given as character strings,
    must conform to the NeXus units standard.
    See the :ref:`NeXus units <Design-Units>` section for details.

:Description (and Occurrences):
    A simple text description of the data field. No markup or formatting
    is allowed.
    The absence of *Occurrences* in the item
    description signifies that
    both ``minOccurs`` and ``maxOccurs`` have
    the default values.
    If the number of occurrences of an item are specified
    in the NXDL (through ``@minOccurs`` and
    ``@maxOccurs`` attributes), they will be reported in
    the Description column similar to the example shown above.
    Default values for occurrences are shown in the following table. The
    ``NXDL element type`` is either a group (such as a
    NeXus base class), a field (that specifies the name and type of a
    variable), or an attribute of a field or group. The number of times an
    item can appear ranges between ``minOccurs`` and
    ``maxOccurs``. A default ``minOccurs``
    of zero means the item is optional. For attributes,
    ``maxOccurs`` cannot be greater than 1.
    
    ================= ========= =========
    NXDL element type minOccurs maxOccurs
    ================= ========= =========
    group             0         unbounded
    field             0         unbounded
    attribute         0         1
    ================= ========= =========
