.. NeXus: a common data format for neutron, x-ray, and muon science documentation master file, created by
   $Id$

.. :title-reference:`NeXus Documentation: User Manual and Reference Documentation`

##############################################################################
NeXus: a common data format for neutron, x-ray, and muon science
##############################################################################

.. image:: ../../manual/img/NeXus.png
	:width: 2in
	:alt: NeXus logo

`A PDF version of this manual is available. 
<http://jemian.org/nexus-sphinx/latex/nexus.pdf>`_

Contents:

.. toctree::
   :maxdepth: 2
   
   self
   volume1/preface

.. toctree::
   :maxdepth: 2
   
   volume1/index
   volume2/index
   authors


Symbols to mark Sections
========================================================================

.. sidebar:: Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   This is a demo of a sidebar.
   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.

Enjoy inline math such as: :math:`E=mc^2`
using LaTeX markup.  You will need the ``matplotlib``
package in your Python.
This was possible with this definition
in `conf.py`::

   extensions = ['sphinx.ext.pngmath', 'sphinx.ext.ifconfig']
   extensions.append( 'matplotlib.sphinxext.mathmpl' )

This is a cheat sheet and will be removed later.

======   =================================================
symbol   description
======   =================================================
`#`      with overline, for parts
`*`      with overline, for chapters
`=`      for sections
`-`      for subsections
`^`      for subsubsections
`"`      for paragraphs
======   =================================================



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
