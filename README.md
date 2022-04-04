* NeXus: https://www.nexusformat.org/
* Citation: [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1472392.svg)](https://doi.org/10.5281/zenodo.1472392)
* Documentation: https://manual.nexusformat.org/
* Release Notes: https://github.com/nexusformat/definitions/wiki/Release-Notes
* License: [![License](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
* Continuous Integration: [![Syntax Checking](https://github.com/nexusformat/definitions/actions/workflows/syntax-checks.yml/badge.svg)](https://github.com/nexusformat/definitions/actions/workflows/syntax-checks.yml)
* Continuous Deployment: [![Publish Documentation](https://github.com/nexusformat/definitions/actions/workflows/publish-sphinx.yml/badge.svg)](https://github.com/nexusformat/definitions/actions/workflows/publish-sphinx.yml)

These are the components that define the structure of NeXus data files 
in the development directory.

component                      | description
-------------------------------|------------------------
[BUILDING.rst](BUILDING.rst)   | how to build the documentation
[CHANGES.rst](CHANGES.rst)     | Change History
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
