First attempt at generating XML schema for NeXus ... work in progress and much to do as I'm still learning

The structure I'm currently trying is:

* Basic data types (NX_FLOAT32, ISO8601 etc.) are all defined in NeXus.xsd

* Base classes are each defined in a separate *.xsd file (e.g. NXentry.xsd) 
  These files will include NeXus.xsd and any other NX*.xsd definitions they need

* Instrument definitions will be created by redefining NXentry (via NXentryType) to change 
  the required components from optional (minOccurs="0") to mandatory (minOccurs="1")
  see PROCESSED.xsd for an example

The *.html files are auto-generated schema documentation files
testfile.xml is a simple example file that validates against the schema

The subversion checked-in files are available from http://definition.nexusformat.org/schema/1.0/
These files have the schemaLocation attribute editied so that they will self include from the
web when used for validation purposes. The trunk version of the NeXus XML API now adds a schema
attribute automatically.

To validate a file on the web you can use the following sites:

http://www.w3.org/2001/03/webdata/xsv          - Go to the second section (file to upload), browse and then "upload and get results"

http://tools.decisionsoft.com/schemaValidate/  - Upload file to XML instance (no need to add a schema) and press validate

Freddie Akeroyd
11/07/2008
