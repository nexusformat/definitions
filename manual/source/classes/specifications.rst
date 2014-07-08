.. _NeXus.Class.Specifications:

NeXus Class Specifications
##########################

Each of the NeXus classes is described in the subsections below.
The classes are organized by the category of class, whether 
:ref:`base class <Design-NeXusClasses>`, 
:ref:`application definition <Design-NeXusApplications>`, 
or :ref:`contributed definition <community.Contributed.Definitions>`.
For each class definition, the documentation is derived from content
provided in the NXDL specification.  
The documentation for each class consists of:

#. a short table:

   * the current version of the NXDL specification used for the class
   * the category of the class
   * the class from which class this class extends
   * any other base classes (groups) cited by this class

#. the class description
#. a link to a tree outline of the class (or link to the NXDL source)

   .. TODO: make this *always* a link to the source and not a link to the tree outline

#. a tree outline of the class
#. a table of the members of the class [#]_
#. supplementary tables of members as needed [#]_


.. [#]  In the tables, parentheses are used in two cases to indicate default values.
   
   #. For groups, the name may not be declared in the NXDL specification.
      In such instances, the value shown in parentheses in the
      *Name and Attributes* column is a suggestion, obtained from the 
      group by removing the "NX" prefix.
      See :ref:`NXentry` for examples.

   #. For fields, the data type may not be specified in the NXDL file.
      The default data type is NX_CHAR and this is shown in parentheses in the *Type* column.
      See :ref:`NXdata` for examples.
   

.. [#]  For application definitions (such as :ref:`NXsas`)
   as well as some contributed definitions,
   the NXDL specifies members of subgroups.  These specifications are described in
   supplementary tables of members


.. rubric:: Descriptions of the NeXus classes

.. toctree::
	:maxdepth: 1
	
	base_classes/index
	applications/index
	contributed_definitions/index
