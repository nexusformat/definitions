.. index::
    ! single: NXDL
    see: NeXus Definition Language; NXDL

.. _NXDL:

===================================
NXDL: The NeXus Definition Language
===================================

..
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
:ref:`Tutorial <NXDL_Tutorial>` chapter, look at the
set of NeXus NXDL files to learn how to read
and write NXDL files.  These files are available from
the NeXus *definitions* repository
and are most easily viewed on GitHub:
https://github.com/nexusformat/definitions
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

.. [#] For example *XML Copy Editor* (http://xml-copy-editor.sourceforge.net/)
.. [#] http://en.wikipedia.org/wiki/XML#Well-formedness_and_error-handling

NXDL files are machine-readable.
This enables their automated conversion into schema files
that can be used, in combination with other NXDL files,
to validate NeXus data files.  In fact, all of the tables in the
:ref:`Class Definitions <ClassDefinitions>` Chapter
have been generated directly from the NXDL files.

.. sidebar:: Writing references and anchors in the documentation.

   .. tip::

      Use the reST anchors when writing documentation in
      NXDL source files.
      Since the anchors have no title or caption associated,
      you will need to supply text with the reference, such as::

          :ref:`this text will appear <anchor>`

      Since these anchors are absolute references, they may be
      used anywhere in the documentation source 
      (that is, within XML ``<doc>`` structures 
      in `.nxdl.xml` files or in ``.rst`` files).

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



..  auto-generated: NXDL Elements and Data Types, built from nxdl.xsd
    ../../utils/nxdl_desc2rst.py ../../nxdl.xsd > nxdl_desc.rst

.. toctree::
	:maxdepth: 3
	
	nxdl_desc
	nxdl-types
