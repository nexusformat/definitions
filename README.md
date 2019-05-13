* NeXus: http://www.nexusformat.org/
* citation: [![DOI](https://zenodo.org/badge/19377430.svg)](https://zenodo.org/badge/latestdoi/19377430) (DOI: 10.5281/zenodo.1472392)
* documentation: http://download.nexusformat.org/doc/html/index.html
* Release Notes: https://github.com/nexusformat/definitions/wiki/Release-Notes
* build server: http://build.nexusformat.org/
* travis-ci: syntax check of every NXDL file [![Build Status](https://travis-ci.org/nexusformat/definitions.svg)](https://travis-ci.org/nexusformat/definitions)

These are the components that define the structure of NeXus data files 
in the development directory.

component                      | description
-------------------------------|------------------------
[BUILDING.rst](BUILDING.rst)   | how to build the documentation
[LGPL.txt](LGPL.txt)           | one proposed license model
[NXDL_VERSION](NXDL_VERSION)   | the current NXDL version number
[README.md](README.md)         | this file
applications/                  | NXDL files for applications and instrument defs
base_classes/                  | NXDL files for components
contributed_definitions/       | NXDL files from the community
impatient-guide/               | *NeXus for the Impatient*
jenkins_build                  | configuration for Jenkins continuous integration service
legacy_docs/                   | legacy PDF copies of the NeXus definitions documentation
manual/                        | Sphinx source files for the NeXus documentation
[nxdl.xsd](nxdl.xsd)           | XML Schema for NXDL files
[nxdlTypes.xsd](nxdlTypes.xsd) | called by nxdl.xsd
package/                       | directory for packaging this content
utils/                         | various tools used in the definitions tree
www/                           | launch (home) page of NeXus WWW site
xslt/                          | various XML stylesheet transformations
