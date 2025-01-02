# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import sys, os, datetime


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# add the abs path to the custom extension for collecting the contributor variables from the rst files
sys.path.insert(0, os.path.abspath("../../../dev_tools/ext"))

# -- Project information -----------------------------------------------------

project = "nexus"
author = "NIAC, https://www.nexusformat.org"
copyright = "1996-{}, {}".format(datetime.datetime.now().year, author)
description = "NeXus: A Common Data Format for Neutron, X-ray, and Muon Science"

# The full version, including alpha/beta/rc tags
version = "unknown NXDL version"
release = "unknown NXDL release"
nxdl_version = open("../../NXDL_VERSION").read().strip()
if nxdl_version is not None:
    version = nxdl_version.split(".")[0]
    release = nxdl_version


# -- General configuration ---------------------------------------------------

# https://github.com/nexusformat/definitions/issues/659#issuecomment-577438319
needs_sphinx = "2.3"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_toolbox.collapse",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx_tabs.tabs",
    "contrib_ext",
    "chios.bolditalic",
    "sphinx_gallery.gen_gallery",
]

# Show `.. todo` directives in the output
# todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinxdoc"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add extra files
html_extra_path = ["CNAME"]

html_sidebars = {
    "**": [
        "localtoc.html",
        "relations.html",
        "sourcelink.html",
        "searchbox.html",
        "google_search.html",
    ],
}


def setup(app):
    app.add_css_file("details_summary_hide.css")


# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "../../../common/favicon.ico"

# Output file base name for HTML help builder.
htmlhelp_basename = "NeXusManualdoc"

html_contexthtml_context = {
    "css_files": [
        "_static/bespoke.css",  # custom CSS styling
        "_static/bolditalic.css",  # bolditalic styling
    ],
}

# -- Options for Latex output -------------------------------------------------
latex_elements = {
    "maxlistdepth": 25,  # some application definitions are deeply nested
    "preamble": r"""
    \usepackage{amsbsy}
    \DeclareUnicodeCharacter{1F517}{X}
    \DeclareUnicodeCharacter{2906}{<=}
    \listfiles""",
}

# -- Options the gallery -------------------------------------------------
sphinx_gallery_conf = {
    "examples_dirs": [
        "../../galleries/nxdata",
    ],  # paths with .py files that generate plots
    "gallery_dirs": [
        "classes/base_classes/data",
    ],  # paths where to save gallery generated output
    "download_all_examples": False,  # disable download buttons
    "write_computation_times": False,  # disable computation time display
    "show_signature": False,  # disable signature
}
