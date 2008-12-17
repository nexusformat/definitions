XML Schema For NeXus
--------------------

This is a first attempt at generating XML schema for NeXus ... it is still work in progress

The structure I'm currently trying is:

* Basic data types (NX_FLOAT32, ISO8601 etc.) are all defined in NeXus.xsd along with enumerations
  such as nx:validShape

* Base classes are each defined in a separate *.xsd file (e.g. NXentry.xsd) 
  These files will include NeXus.xsd and any other NX*.xsd definitions they need
  Using separate files will hopefully make future changes easier for instrument editors etc.  

* Instrument definitions will be created by redefining NXentry (via NXentryType) to change 
  the required components from optional (minOccurs="0") to mandatory (minOccurs="1")
  see PROCESSED.xsd for an example

* Some object-orientated features have been added as they make definition
  writing easier and avoid duplication. For example:
  - an abstract NXchopper.xsd has been created that is inherited by NXdisc_chopper.xsd and NXfermi_chopper.xsd
  - all NeXus object inherit from nx:classBaseType (it just has a "name" attribute that all classes have)
  - beamline components inherit from nx:componentType that contains "distance" and NXgeometry members etc.

The *.html files are auto-generated schema documentation files

testfile.xml is a simple example file that validates against the schema

The working copies of the schema files are stored at http://svn.nexusformat.org/definitions/trunk/schema
These schema files have a xsi:schemaLocation attribute set to reference files in the same directory, which is useful
for developing. After chekin, they are published to http://definition.nexusformat.org/schema/3.0/ with the 
xsi:schemaLocation attribute edited so that they will self include from the web when used for validation purposes. 

The trunk version of the NeXus XML API now adds a XML schema attributes automatically.

To validate a file on the web you can use the following sites:

http://www.w3.org/2001/03/webdata/xsv          - Go to the second section (file to upload), browse and then "upload and get results"

http://tools.decisionsoft.com/schemaValidate/  - Upload file to XML instance (no need to add a schema) and press validate

You can also use the "xmllint" tool, which is part of libxml2. This doesn't seem to pick up the xsi:schemaLocation tag so you
need to give the schema path by hand

    xmllint --schema http://definition.nexusformat.org/schema/1.0/BASE.xsd  my_nexus_file.xml

Freddie Akeroyd
11/07/2008

Update
------

There is now an "nxvalidate" command built as part of the 
nexus-trunk kit from http://download.nexusformat.org/kits/snapshots.shtml

This command will validate a nexus file (HDF or XML) by silently converting it to XML 
with the data stripped and then
- using "xmllint" if it is avaiable locally
- using "wget" to send the file to the nexus web site for validation

Type     nxvalidate -h   for a list of options 

The NXtest.xml file created by running napi_test-xml can be validated using nxvalidate

Freddie Akeroyd
21/08/2008

$Id$
$HeadURL$
