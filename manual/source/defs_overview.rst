.. _ClassDefinitions-Overview:

=========================
Overview of NeXus classes
=========================

.. TODO: organization could improve here!

.. index:: NXDL

Each of the NeXus classes is described in the subsections below.
The classes are organized by the category [#]_ of class, whether 
:ref:`base class <Design-NeXusClasses>`, 
:ref:`application definition <Design-NeXusApplications>`, 
or :ref:`contributed definition <community.Contributed.Definitions>`.
For each class definition, the documentation is derived from content
provided in the NXDL [#]_ specification.  
The documentation for each class consists of:

#. a short table:

   * the current version of the NXDL specification used for the class
   * the category of the class
   * The  NeXus class extended by this class. 
     Most NeXus base classes only extend the base class definition (NXDL).
   * any other base classes (groups) cited by this class

#. symbol list [#]_
#. the class description
#. a link to a tree outline of the class (or link to the NXDL source)

   .. TODO: make this *always* a link to the source and not a link to the tree outline

#. a tree outline of the class
#. a table of the members of the class
#. supplementary tables of members as needed [#]_


.. [#] The *category* of NXDL, one of these:
    
    + ``base`` (meaning: :ref:`base class <base.class.definitions>`)
    + ``application`` (meaning: :ref:`application definition <application.definitions>`)
    + ``contributed`` (meaning: :ref:`contributed definition <contributed.definitions>`)

.. [#] NXDL (NeXus Definition Language:)

   :ref:`NXDL` is used to describe the components in the NeXus
   Base Classes, as well as application and contributed definitions.
   The intent of NXDL is to provide a
   :index:`rules-based method <rules; NXDL>`
   for defining a NeXus data file that is
   specific to either an instrument (where NeXus has been
   for years) or an area of scientific technique or analysis.
   NXDL replaces the meta-DTD method used previously to
   define the NeXus base classes

.. [#] List of the ``symbols`` (if present) that define mnemonics that
    represent the length of each dimension in a vector or array.
   

.. [#]  For application definitions (such as :ref:`NXsas`)
   as well as some contributed definitions,
   the NXDL specifies members of subgroups.  These specifications are described in
   supplementary tables of members

..

   Each of the NeXus classes is described in several basic ways. First, a short list of
   descriptive information is provided as a header, then a condensed listing of the
   basic structure, then a table providing documentation for the various components
   of the NeXus class.
   
   :category:
       The category of NXDL, one of these:
       
       + ``base`` (meaning: :ref:`base class <base.class.definitions>`)
       + ``application`` (meaning: :ref:`application definition <application.definitions>`)
       + ``contributed`` (meaning: :ref:`contributed definition <contributed.definitions>`)
   
   :NXDL source:
       Name of the NeXus class and a URL to the source listing in the NeXus
       subversion repository.
   
   :version:
       A string that documents this particular
       version of this NXDL.
   
   :SVN Id:
       The SVN ID is now out of date since the version control switched from
       subversion to git.

   .. index:: NXDL
   
   :NeXus Definition Language:
       :ref:`NXDL` is used to describe the components in the NeXus
       Base Classes, as well as application and contributed definitions.
       The intent of NXDL is to provide a
       :index:`rules-based method <rules; NXDL>`
       for defining a NeXus data file that is
       specific to either an instrument (where NeXus has been
       for years) or an area of scientific technique or analysis.
       NXDL replaces the meta-DTD method used previously to
       define the NeXus base classes.
   
   :extends class:
       NeXus class extended by this class. Most NeXus base classes only
       extend the base class definition (NXDL).
   
   :other classes included:
       List (including URLs) of other classes used to define this
       class.
   
   :symbol list:
       List of the ``symbols`` (if present) that define mnemonics that
       represent the length of each dimension in a vector or array.
   
   :documentation:
       Description of the NeXus class. DocBook markup (formatting is
       allowed).


Basic structure of the **class**
--------------------------------

A compact listing of the basic structure
(groups, fields, dimensions, attributes, and links)
is prepared for each NXDL specification.  Indentation shows
nested structure.  Attributes are prepended with the ``@``
symbol while links use the characters ``-->``
to represent the path to the intended source of the information.

The table has columns to describe the basic information about each field or group in
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

In the above example, the fields might appear in a NeXus XML data file as

.. compound::

	.. rubric:: Example fragment of a NeXus XML data file
	
	.. code-block:: xml
	    :linenos:
	
		<program_name version="1.0a" configuration="standard">
		    MaxSAS
		</program_name>
		<NXnote name="thumbnail" mime_type="image/*">
		    <!-- contents of an NXnote would appear here -->
		</NXnote>
		<distance units="mm">125.6</distance>
		<mode> Single Bunch </mode>
		<target_material>depleted_U</target_material>

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

    :index:`Attributes <!attributes>`,
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
