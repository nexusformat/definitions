.. _ClassDefinitions:

Introduction to NeXus definitions
#################################

..
	.. image:: img/NeXus.png

While the design principles of NeXus are explained in the 
:ref:`UserManual`, this Reference Documentation specifies 
all allowed :ref:`base classes <base.class.definitions>` 
and all standardized :ref:`application definitions <application.definitions>`. 
Furthermore, it also contains 
:ref:`contributed definitions <contributed.definitions>` 
of new bases classes or application definitions that 
are currently under review.

Base class definitions and application definitions have basically 
the same structure, but different semantics: 

* Base class definitions define the *complete* set of 
  terms that *might* be used in an instance of that class.  

* Application definitions 
  define the *minimum* set of terms that *must* be used in an instance of that class.  

Base classes and application definitions are specified using a domain-specific XML scheme, the :ref:`NXDL`.

.. _ClassDefinitions-Overview:

Overview of NeXus definitions
*****************************

.. index:: NXDL

For each class definition, the documentation is derived from content
provided in the NXDL specification.

The documentation for each class consists of sections describing
the *Status*, *Description*, table of *Symbols* (if defined),
other NeXus base class *Groups cited*, an annotated *Structure*,
and a link to the *NXDL Source* (XML) file.

.. index:: release; versioning
.. index:: release; tags
.. index:: tags

Each of the NXDL files has its own tag in the version repository.  Such
as `NXcrystal-1.0` is tagged in GiHub and accessible via URL:
https://github.com/nexusformat/definitions/releases/tag/NXcrystal-1.0

Description
===========

General documentation if this NXDL file.

Symbols table
=============

The symbols table describes 
keywords used in this NXDL file to designate array dimensions. 
At present, this list is not guaranteed to be complete 
(some array dimension names appear only in a *Structure* 
description and not here).

Annotated Structure
===================

A representation of the basic structure (groups, fields, 
dimensions, attributes, and links) is prepared for each NXDL 
specification. Indentation shows nested structure. 
Attributes are prepended with the ``@`` symbol. 
Links use the characters ``->`` to represent the 
path to the intended source of the information.

Indentation is used to indicate nesting of subgroups
(a feature common to application definitions).
Within each indentation level, 
NeXus :ref:`fields <Design-Fields>` are listed first
in the order presented in the NXDL file, then
:ref:`groups <Design-Groups>`.  :ref:`Attributes <Design-Attributes>`
are listed after the documentation of each item and
are prefixed with the letter ``@`` (do not use the 
``@`` symbol in the actual attribute name).
The name of each item is in **bold**, followed by either
*optional* or *required* and then the NXDL base class 
name (for groups) or the NeXus data type (for fields).
If units are to be provided with the *field*, the type of the
units is described, such as ``NX_DATE_TIME``.

:ref:`NeXus Links <Design-Links>` (these specifications are typically
present only in application definitions) are described by a local name,
the text `->`, then a suggested path to the source item to be linked 
to the local name.

Names (groups, fields, links, and attributes)
=============================================

Name of the item.
Since ``name`` needs to be restricted to valid
program variable names,
no "``-``" characters can be allowed.
Name must satisfy both 
:index:`HDF <rules; HDF>` and :index:`XML <rules; XML>`
:index:`naming <rules; naming>`.

.. code-block:: text
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
``program_name`` element has the 
``configuration`` (optional) attribute while the
``thumbnail`` element has the
``mime_type`` (optional) attribute.

For groups, the name may not be declared in the NXDL specification.
In such instances, the *value shown in parentheses* in the
*Name and Attributes* column is a suggestion, obtained from the 
group by removing the "NX" prefix.
See :ref:`NXentry` for examples.

.. index:: flexible name

When the name is allowed to be *flexible* (the exact name given
by this NXDL specification is not required but is set
at the time the HDF file is written), the flexible
part of the name will be written in all capital letters.
For example, in the :ref:`NXdata` group, the ``DATA``,
``VARIABLE``, and ``VARIABLE_errors`` fields are *flexible*.

NeXus data type
===============

Type of data to be represented by this variable.
The type is one of those specified in :ref:`NXDL`.
In the case where the variable can take only one value from a known
list, the list of known values is presented, such as in the
``target_material`` field above:
``Ta | W | depleted_U | enriched_U | Hg | Pb | C``.
Selections with included whitespace are surrounded by quotes. See the
example above for usage.

For fields, the data type may not be specified in the NXDL file.
The *default data type* is ``NX_CHAR``.
See :ref:`NXdata` for examples.

Units
=====

:index:`Data units <units>`,
are given as character strings,
must conform to the NeXus :ref:`units standard <nxdl-units>`.
See the :ref:`NeXus units <Design-Units>` section for details.

Description
===========

A simple text description of the field. No markup or formatting
is allowed.


================= ==============  =========
NXDL element type minOccurs       maxOccurs
================= ==============  =========
group             [#minOccurs]_   unbounded
field             [#minOccurs]_   unbounded
attribute         [#minOccurs]_   1
================= ==============  =========

.. [#minOccurs] For NXDL *base classes*, ``minOccurs=0`` is the default, 
    for NXDL *application definitions* and  *contributed definitions*, ``minOccurs=1`` is the default.
    In all cases, the ``minOccurs`` attribute in the NXDL file will override the default
    for that element (group, field, attribute, or link).

.. index:: !choice

Choice
======

The ``choice`` element allows one to create a group with a defined name 
that is one specific NXDL base class from a defined list of possibilities

In some cases when creating an application definition, more than one 
choice of base class might be used to define a particular subgroup.  
For this particular situation, the ``choice`` was added to the NeXus 
NXDL Schema. 

In this example fragment of an NXDL application definition, 
the ``pixel_shape`` could be represented by *either* 
``NXoff_geometry`` or ``NXcylindrical_geometry``.


.. code-block:: xml
    :linenos:

	<choice name="pixel_shape">
	  <group type="NXoff_geometry">
	    <doc>
	      Shape description of each pixel. Use only if all pixels in the detector
	      are of uniform shape.
	    </doc>
	  </group>
	  <group type="NXcylindrical_geometry">
	    <doc>
	      Shape description of each pixel. Use only if all pixels in the detector
	      are of uniform shape and require being described by cylinders.
	    </doc>
	  </group>
	</choice>


The ``@name`` attribute of the ``choice`` element specifies the name that
will appear in the HDF5 data file using one of the groups listed within the choice.
Thus, it is not necessary to specify the name in each group.  (At some point, 
the NXDL Schema may be modified to enforce this rule.)

A ``choice`` element may be used wherever a ``group`` element
is used.  It **must** have at least two groups listed (otherwise, it would
not be useful).
