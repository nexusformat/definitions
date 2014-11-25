.. index::
	!validation
	!verification

.. _Verification:

====================================
Verification and validation of files
====================================

..  ++++++++++++++++++++++++++++

The intent of verification and validation of files is to ensure, in an unbiased way, that
a given file conforms to the relevant specifications. NeXus uses various automated tools to
validate files. These tools include conversion of content from HDF to XML and transformation
(via XSLT) from XML format to another such as NXDL, XSD, and Schematron. This chapter will
first provide an overview of the process, then define the terms used in validation, then
describe how multiple base classes or application definitions might apply to a given NeXus
data file, and then describe the various validation techniques in more detail. Validation
does not check that the data content of the file is sensible; this requires scientific
interpretation based on the technique.

Validation is useful to anyone who manipulates or modifies the contents of NeXus files.
This includes scientists/users, instrument staff, software developers, and those who might
mine the files for  :index:`metadata`. 
First, the scientist or user of the data must be certain that the information
in a file can be located reliably. The instrument staff or software developer must be
confident the information they have written to the file has been located and formatted
properly. At some time, the content of the NeXus file may contribute to a larger body of
work such as a metadata catalog for a scientific instrument, a laboratory, or even an entire user facility.

..  ++++++++++++++++++++++++++++

.. _Verification-Overview:

Overview
########

NeXus files adhere to a set of  :index:`rules <rules; NeXus>` and can be tested 
against these rules for compliance. The rules are
implemented using standard tools and can themselves be tested to verify compliance with
the standards for such definitions. Validation includes the testing of both NeXus data
files and the NXDL specifications that describe the rules.

The rules for writing NeXus data files are different than the rules for writing NeXus
class definitions. To validate a NeXus data file, these two rule sets must eventually
merge, as shown in the next figure. The data file (either HDF4, HDF5, or XML) is first
converted into an internal format to facilitate validation, including data types, array
dimensions, naming, and other items. Most of the data is not converted since data
validation is non-trivial. Also note that the units are not validated. All the NXDL
files are converted into a single Schematron file (again, internal use for validation)
only when NXDL revisions are checked into the NeXus definitions repository as NXDL
changes are not so frequent.

..  TODO: Will we describe how validation code can check to see if it is
    using the most recent version of the master Schematron file?

.. compound::

    .. _figure.nxvalidate:

    .. figure:: img/nxvalidate.png
        :alt: figure.nxvalidate
        :width: 80%
        :align: center

        Flowchart of the NeXus validation process.

NeXus data files
    NeXus data files (also known as NeXus data file instances) are validated
    to ensure the various parts of the data file are arranged according to the
    governing NXDL :index:`specifications <rules; NeXus>` used in that file instance. 

	.. note:: 
		Since NeXus has several rules that are quite difficult to apply in
		either XSD or Schematron, direct validation of data files using standard
		tools is not possible. To validate NeXus data files, it is necessary to
		use ``nxvalidate``.
              
	..  *What about the Java tools?*

NeXus Definition Language (NXDL) specification files
    NXDL files are validated to ensure they adhere to the  :index:`rules <rules; NXDL>` 
    for writing NeXus base classes and application definitions.

..  ++++++++++++++++++++++++++++

.. _Verification-Definitions:

Definitions of these terms
##########################

Let's be clear about some terms used in this section.

:HDF:
    :index:`Hierarchical Data Format <HDF>` from The HDF Group.
    NeXus data files using HDF
    may be stored in either version 4 (HDF4) or version 5 (HDF5). New NeXus HDF
    files should only use HDF5. The preferred file extensions
    (but not required) include ``.hdf``, ``.h5``, ``.nxs``, and ``.nx5``.

:NXDL:
    NeXus Definition Language files define the specifications for NeXus base
    classes, application definitions, and contributed classes and definitions.
    It is fully described in the :ref:`NXDL <NXDL>` chapter.

:Schematron:
    :index:`Schematron` [#Schematron]_
    is an alternative to XSD and is used to validate the content
    and structure of an XML file.  NeXus uses Schematron internally to
    validate data files.

:Validation:
    File validation is the comparison of file contents, in an unbiased way,
    with the set of rules that define the structure of such files.

:XML:
    The eXtensible Markup Language (:index:`!XML`) [#XML]_
    is a standard business tool for the
    exchange of information. It is broadly supported by a large software library
    in many languages. NeXus uses XML for several purposes: data files, NXDL
    definitions, rules, and XSLT transformations.

:XSD:
    XML files are often defined by a set of rules (or
    *schema*). A common language used to implement these
    rules is XML Schema (:index:`XSD`)  [#XSD]_
    Fundamentally, all XML, XSD, XSLT, and Schematron files are  XML.

:XSLT:
    XML files can be flexible enough to convert from one set of rules to
    another. An example is when one company wishes to exchange catalog or
    production information with another. The XML StyLsheet Transformation
    (:index:`XSLT`) [#XSLT]_
    language is often used to describe each direction of the conversion of the
    XML files between the two rule sets.

.. [#Schematron] http://www.schematron.com
.. [#XML]        http://www.w3schools.com/xml
.. [#XSD]        http://www.w3schools.com/schema
.. [#XSLT]       http://www.w3schools.com/xsl/

..  ++++++++++++++++++++++++++++

.. _Verification-Multipledefs:

NeXus data files may use multiple base classes or application definitions
#########################################################################

NeXus data files may have more than one data set or may have multiple instances of
just about any base class or even application definitions. The NeXus data file
validation is prepared to handle this without any special effort by the provider of the
data file.

..  ++++++++++++++++++++++++++++

.. _Verification-Techniques:

.. index::  validation

Validation techniques
#####################

File validation is the process to determine if a given file is prepared consistent
with a set of guidelines or  :index:`rules`. In NeXus, there are several different types of files. First, of course, is
the data file yet it can be provided in one of several forms: HDF4, HDF5, or XML.
Specifications for data files are provided by one or (usually) more NeXus definition
files (NXDL, for short). These NXDL files are written in XML and validated by the NXDL
specification which is written in the :index:`XML Schema (XSD)` language.  
Thus, automated file verification is available for data files, definition
files, and the rules for definition files.

..  ++++++++++++++++++++++++++++

.. _Verification-Data:

.. index:: validation; NeXus data files

Validation of NeXus data files
==============================

Each NeXus data file can be validated against the NXDL  :index:`rules <rules; NeXus>`. 
(The full suite of NXDL specifications is converted into Schematron
rules by an  :index:`XSLT` transformation and then combined into a single file. It is not allowed
to have a NeXus base class and also an application definition with the same name
since one will override the other in the master Schematron file) The validation is
done using Schematron and the ``NXvalidate`` program. 
:index:`Schematron` was selected, rather than :index:`XML Schema (XSD)`, 
to permit established rules for NeXus files, especially the rule
allowing the nodes within ``NXentry`` to appear in any order.

The validation process is mainly checking file structure (presence or absence of groups/fields)
- it is usually impossible to check the actual data itself,
other than confirm that it is of the correct data type (string, float etc.). The only exception is when
the NXDL specification is either a fixed value or an enumeration - in which case the data
is checked.

During validation, the NeXus data file instance (either HDF or XML) is first converted
into an XML file in a form that facilitates validation (e.g with large numeric data removed).  Then the
XML file is validated by Schematron against the ``schema/all.sch``
file.

..  ++++++++++++++++++++++++++++

.. _Verification-NXDL:

.. index:: validation; NXDL specifications

Validation of NeXus Definition Language (NXDL) specification files
==================================================================

Each NXDL file must be validated against the  :index:`rules <rules; NXDL>` 
that define how NXDL files are to be arranged. The NXDL rules are
specified in the form of :index:`XML Schema (XSD)`.

Standard tools (validating editor or command line or support library) can be used
to validate any NXDL file. Here's an example using ``xmllint``
from a directory that contains ``nxdl.xsd``,
``nxdlTypes.xsd``, and
``applications/NXsas.nxdl.xml``:

.. compound::

    .. rubric:: Use of ``xmllint`` to validate a NXDL specification.

    .. code-block:: guess
    
	    xmllint --noout --schema nxdl.xsd applications/NXsas.nxdl.xml

..  ++++++++++++++++++++++++++++

.. _Verification-NXDL-rules:

.. index:: validation; NXDL rules

Validation of the NXDL rules
============================

NXDL rules are specified using the rules of :index:`XML Schema (XSD)`. 
The XSD syntax of the rules is validated using standard XML file
validation tools: either a validating editor (such as *oXygen*,
*xmlSpy*, or *eclipse*) or common
UNIX/Linux command line tools

.. compound::

    .. rubric:: Use of ``xmllint`` to validate the NXDL rules.

    .. code-block:: guess

	    xmllint --valid  nxdl.xsd

The validating editor method is used by the developers while the
``xmllint`` command line tool is the automated method used by the NeXus
definitions subversion repository.

..  ++++++++++++++++++++++++++++

.. _Verification-XSLT:

.. index:: 
	validation; XSLT files
	XSLT

Validation of XSLT files
========================

XSLT transformations are validated using standard tools
such as a validating editor or xmllint.

..  Care to give an example of validating an XSLT using xmllint or saxon?

..  ++++++++++++++++++++++++++++

.. _Verification-NXDL-to-SCH:

.. index::
	NXDL
	Schematron
	rules; Schematron

Transformation of NXDL files to Schematron
==========================================

Schematron [#Schematron]_ is a rule-based language that allows very specific validation of an XML
document. Its advantages over using XSD schema are that:

- more specific pattern-based rules based on data content can be
  written

- full XSLT/XPath expression syntax available for writing validation
  tests

- error messages can be customised and thus more meaningful

- It is easier to validate documents when entities can occur in any
  order.

XSD does provide a mechanism for defining a class structure and inheritance, so
its usage within NeXus in addition to schematron has not been ruled out. But for a
basic validation of file content, schematron looks best.

The NXDL definition files are converted into a set of Schematron 
:index:`rules <rules; NeXus>` using the ``xslt/nxdl2sch.xsl`` XSLT stylesheet. The NeXus
instance file (either in XML, HDF4, or HDF5)
is turned into a reduced XML validation file.
This file is very similar to a pure NeXus XML file, but with additional metadata for
dimensions and also with most of the actual numeric data removed.

The validation process then compares the set of Schematron rules against the
*reduced XML* validation file. Schematron itself is
implemented as a set of XSLT transforms. NeXus includes the Schematron files, as
well as the Java based XSLT engine ``saxon``.

The java based
``nxvalidate`` GUI can be run to validate files.

Currently, the structure of the file is validated (i.e. valid names are used at
the correct points), but this will be extended to array dimensions
and :index:`link` targets.
Error messages are printed about missing mandatory fields, and informational
messages are printed about fields that are neither optional or mandatory (in case
they are a typing error). Even non-standard names must comply with a set of rules
(e.g. no spaces are allowed in names). Enumerations are checked that they conform to
an allowed value. The data type is checked and the units will also be checked.

