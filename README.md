* NeXus: http://www.nexusformat.org/
* documentation: http://download.nexusformat.org/doc/html/index.html
* build server: http://build.nexusformat.org/
* travis-ci: syntax check of every NXDL file [![Build Status](https://travis-ci.org/nexusformat/definitions.svg)](https://travis-ci.org/nexusformat/definitions)

These are the components that define the structure of NeXus data files 
in the development directory.

component                   | description
----------------------------|------------------------
LGPL.txt                    | one proposed license model
NXDL_VERSION                | the current NXDL version number
README.txt                  | README file
README.make.txt             | how to build the documentation
applications/               | NXDL files for applications and instrument defs
base_classes/               | NXDL files for components
contributed_definitions/    | NXDL files from the community
impatient-guide/            | *NeXus for the Impatient*
jenkins_build               | configuration for Jenkins continuous integration service
manual/                     | Sphinx source files for the NeXus documentation
manual_archive/             | historical copy of the NeXus documentation
nxdl.xsd                    | XML Schema for NXDL files
nxdlTypes.xsd               | called by nxdl.xsd
package/                    | directory for packaging this content
utils/                      | various tools used in the definitions tree
www/                        | launch (home) page of NeXus WWW site
xslt/                       | various XML stylesheet transformations

See README.make.txt for how to build the documentation
