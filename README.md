* NeXus: https://www.nexusformat.org/
* Citation: [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1472392.svg)](https://doi.org/10.5281/zenodo.1472392)
* Documentation: https://manual.nexusformat.org/
* Release Notes: https://github.com/nexusformat/definitions/wiki/Release-Notes
* License: [![License](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
* Test, Build and Deploy: [![CI](https://github.com/nexusformat/definitions/actions/workflows/ci.yaml/badge.svg)](https://github.com/nexusformat/definitions/actions/workflows/ci.yaml)

## NeXus definition developers

First install the test and build requirements with this command (only run once)

    make install

Then verify syntax and build the HTML manual with this command

    make local

Open the HTML manual in a web brower for visual verification

    firefox build/manual/build/html/index.html

Convenient editing of definitions is available in nyaml format. For this, definitions need to be converted first from xml to yaml format by the command

    make nyaml

After editing the definitions in nyaml format in the nyaml subdirectories, the following command can be used to update the definitions in nxdl.xml format:

    make nxdl

> [!WARNING]  
> Please be aware that your nyaml files might be out of sync with the nxdl files when you update your repo. So it's best practice to stash your changes to the nyaml files and regenerate the files with `make nyaml` before adding any changes.

### HTML pages with contributor information

To build the html pages that contains contributor information on the sidebar set a github access token to an environment variable called GH_TOKEN.

Note: If set this will increase the build time of the documentation by approximately a factor of 4.

    setenv GH_TOKEN <access token>

### Working with nyaml files

There exists a simplified format of nxdl, which is called nyaml.
There is a [tool](https://github.com/FAIRmat-NFDI/nyaml) (`nyaml2nxdl`) available to convert between nxdl and nyaml.
This tool is already installed when you installed the requirements for this repository and it is conveniently available from the make command.

You can build nyaml files for all nxdl files with invoking

    make nyaml

which will created `.yaml` files in a subfolder called `nyaml` in the respective directory.

From this you can do your changes and create nxdl files with

    make nxdl

from the yaml files.

## Repository content

These are the components that define the structure of NeXus data files 
in the development directory.

component                      | description
-------------------------------|------------------------
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
dev_tools/                     | developer tools for testing and building
