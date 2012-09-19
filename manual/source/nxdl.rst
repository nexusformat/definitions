.. $Id$

.. _NXDL:

.. index::
    !NXDL
    !NeXus Definition Language

===================================
NXDL: The NeXus Definition Language
===================================

.. image:: img/NeXus.png

Information in NeXus data files is arranged by a set of rules.
These rules facilitate the exchange of data between scientists and software
by standardizing common terms such as the way engineering units are described
and the names for common things and the way that arrays are described and stored.

The set of rules for storing information in NeXus data files
is declared using the NeXus Definition Language.
NXDL itself is governed by a set of rules (a *schema*)
that should simplify learning the few terms in NXDL.
In fact, the NXDL rules, written as an XML Schema, are machine-readable
using industry-standard and widely-available software tools for XML files such as
``xsltproc`` and ``xmllint``.
This chapter describes the rules and terms from which NXDL files are constructed.

Introduction
############

NeXus Definition Language (:index:`NXDL`) 
files allow scientists to define the nomenclature and
arrangement of information
in NeXus data files.  These NXDL files can be
specific to a scientific discipline such as
tomography or small-angle scattering,
specific analysis or data reduction software,
or even to define another component (base class)
used to design and build NeXus data files.

In addition to this chapter and the
:ref:`Tutorial <NXDL_Tutorial>` in Volume I, look at the
set of NeXus NXDL files to learn how to read
and write NXDL files.  These files are available from
the NeXus *definitions* repository
and are most easily viewed through the TRAC site:
http://trac.nexusformat.org/definitions/browser/trunk
in the ``base_classes``, ``applications``, and  ``contributed``
directories.  The rules (expressed as XML Schema)
for NXDL files may also be
viewed from this URL.  See the files
``nxdl.xsd`` for the main XML Schema
and ``nxdlTypes.xsd`` for the listings of
allowed data types and categories of units
allowed in NXDL files.

NXDL files can be checked (validated) for syntax and content.
With validation, scientists can be certain their definitions
will be free of syntax errors.  Since NXDL is based
on the XML standard, there are many editing programs [#]_
available to ensure that the files are *well-formed*. [#]_
There are many standard tools such as ``xmllint``
and ``xsltproc`` that can process XML files.
Further, NXDL files are backed by a set of rules
(an *XML Schema*) that define the
language and can be used to check that an NXDL file
is both correct by syntax and valid by the NeXus rules.

NXDL files are machine-readable.
This enables their automated conversion into schema files
that can be used, in combination with other NXDL files,
to validate NeXus data files.  In fact, all of the tables in the
:ref:`Class Definitions <ClassDefinitions>` Chapter
have been generated directly from the NXDL files.

The language of NXDL files is intentionally quite small,
to provide only that which is necessary to describe
scientific data structures (or to establish the
necessary XML structures).  Rather than have scientists
prepare XML Schema files directly, NXDL was designed to
reduce the jargon necessary to define the structure of
data files.  The two principle objects in NXDL files are:
``group`` and ``field``.
Documentation (``doc``) is optional for any NXDL
component.
Either of these objects may have additional
``attributes`` that contribute simple metadata.

The :ref:`Class Definitions <ClassDefinitions>` Chapter
lists the various classes from which a NeXus file is
constructed. These classes provide the glossary of items that
could, in principle, be stored
in a standard-conforming NeXus file (other items may be inserted into the file if
the author wishes, but they won't be part of the standard). If you are going to
include a particular piece of 
:index:`metadata`, refer to the class definitions
for the standard nomenclature.
However, to assist those writing data analysis
software, it is useful to provide more than a glossary; it is important to define
the required contents of NeXus files that contain data from particular classes of
neutron, X-ray, or muon instrument.

..  + + + + + + + + + + +

..  auto-generated: NXDL Elements and Data Types, built from nxdl.xsd by nxdl_desc2docbook.xsl
    xsltproc ../../xslt/nxdl_desc2docbook.xsl ../../nxdlTypes.xsd > nxdl_desc.xml

	.. literalinclude:: nxdl_desc.xml
	    :tab-width: 4
	    :linenos:
	    :language: guess

.. toctree::

	nxdl_desc

..  + + + + + + + + + + +
		
Data Types allowed in NXDL specifications
#########################################

Data Types for use in :index:`NXDL specifications <pair: NXDL; data types>`
describe the expected type of data for a NeXus field. These terms are very
broad. More specific terms are used in actual NeXus data files that describe
size and array dimensions. In addition to the types in the following table, the
``NAPI`` type is defined when one wishes to permit a field
with any of these data types.

..  Generated from ../nxdlTypes.xsd via a custom Python tool
    ../../utils/types2rst.py ../../nxdlTypes.xsd > types.table

.. include:: types.table

..  + + + + + + + + + + +

Unit Categories allowed in NXDL specifications
##############################################

Unit categories in  :index:`NXDL specifications <pair: NXDL; units>`
describe the expected type of units for a NeXus field. They should describe
valid units consistent with the section on
:ref:`NeXus units <Design-Units>` in Volume I.
The values for unit categories are restricted (by
an enumeration) to the following table.

..  Generated from ../nxdlTypes.xsd via a custom Python tool
    ../../utils/units2rst.py ../../nxdlTypes.xsd > units.table

.. include:: units.table

..  + + + + + + + + + + +

Historical notes about the Development of NXDL
##############################################

..  This might be just so much dirty laundry.  Consider removing it.

This section contains a few brief notes about the history of NXDL
and the motivations for its creation.

Previously, the structure of NeXus data files was described using
*Meta-DTD*, an XML format that provided a compact
description. The terse format was not obvious to all and was difficult to
machine-process. NXDL was conceived to be a simpler syntax than Meta-DTD.
The switch to NXDL was not intended to change what was in the data files, just
to provide an easier (and more generic) way of describing data files.

The NeXus Design page lists the group classes from which a NeXus file is
constructed. They provide the glossary of items that could, in principle, be stored
in a standard-conforming NeXus file (other items may be inserted into the file if
the author wishes, but they won't be part of the standard).
When planning to include a particular piece of 
:index:`metadata`, consult the class definitions
to find out what to call it. However, to assist those writing data analysis
software, it is useful to provide more than a glossary; it is important to define
the required contents of NeXus files that contain data from particular classes of
neutron, x-ray, or muon instrument.

As part of the NeXus standard, the NIAC identified a number of generic instruments
that describe an appreciable number of existing instruments around the world.
Although not identical in every detail, they share many common characteristics,
and more importantly, they require sufficiently similar modes of data analysis,
enough to make a standard description useful.
Many of the application definitions were built from these instrument definitions
using the NeXus Definition Language 
(:index:`NXDL`) format.

Class definitions in NeXus prior to 2008 had been in the form of base classes and
instrument definitions. All of these were in the same category. As the development
of NeXus had been led mostly by scientists from neutron sources, this represented
their typical situations.

Both those new to NeXus and also those familiar saw the previous emphasis on
instrument definitions as a deficiency that limited flexibility and possibly usage.
The point was made that NeXus should attempt to describe better reduced data and
also data for analysis since synchrotron instruments are rarely adhering to a fixed
definition.

The design of NeXus is moving towards an object-oriented approach where the base
classes will be the objects and the application definitions will use the objects
to specify the required components as fits some application. Here,
*application* is
very loosely defined to include:

- specification of a scientific instrument (example: TOF-USANS at SNS)

- specification of what is expected for a scientific technique (example:
  small-angle scattering data for common analysis programs)

- specification of generic data acquisition stream (example: TOFRAW - raw
  time-of-flight data from a pulsed neutron source)

- specification of input or output of a specific software program

..  The term <emphasis>the sky is the limit</emphasis> seems to apply.

The point of the
*NeXus Application Definition*
is that all of these start with ``NX`` and all have
been approved by the NIAC.

Those NXDL specifications not yet approved by the NIAC fall into the category of
*NeXus contributed definitions*
for which NeXus has a place in the repository.
Consider the NXDL files in the ``contributed`` directory
as *in incubation*.
This category is the place to put an NXDL (a
candidate for a base class or application definition) for the NIAC to consider
approving.

..  + + + + + + + + + + +

.. rubric:: Footnotes

.. [#] For example *XML Copy Editor* (http://xml-copy-editor.sourceforge.net/)
.. [#] http://en.wikipedia.org/wiki/XML#Well-formedness_and_error-handling
