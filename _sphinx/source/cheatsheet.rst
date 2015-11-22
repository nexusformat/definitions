.. $Id$

#################
Sphinx Cheatsheet
#################

This is a sphinx cheat sheet and will be removed later.

Section headings automatically get labels assigned.
For example, see this:  `Demo list-table`_

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


Typesetting Math and Equations
++++++++++++++++++++++++++++++

Enjoy inline math such as: :math:`E=mc^2`
using LaTeX markup.  You will need the ``matplotlib``
package in your Python.  There is also separate math.

.. sidebar:: TODO:
	:subtitle: adjust `conf.py`?

	Sphinx has some inconsistency with this expression::

		.. ! this is a candidate for conditional compilation
		   make html      needs two backslashes while
		   make latexpdf  needs one backslash

		.. math::

			\tilde I(Q) = {2 \over l_o} \ \int_0^\infty I(\sqrt{(q^2+l^2)}) \ dl

	.. tip:: Perhaps some modification of `conf.py` would help?
	
	The Sphinx HTML renderer handles simple math this way but 
	not all LaTeX markup.  The HTML renderer needs two backslashes
	while the LaTeX renderer only needs one.

This was possible with this definition
in `conf.py`::

   extensions = ['sphinx.ext.pngmath', 'sphinx.ext.ifconfig']
   extensions.append( 'matplotlib.sphinxext.mathmpl' )

Other Links
+++++++++++

Here are some links to more help about reStructuredText formatting.

reST home page
	http://docutils.sourceforge.net/rst.html

Docutils
	http://docutils.sourceforge.net/

**Very useful!**
	http://docutils.sourceforge.net/docs/ref/rst/directives.html

Independent Overview
	http://www.siafoo.net/help/reST

Wikipedia
	http://en.wikipedia.org/wiki/ReStructuredText

reST Quick Reference
	http://docutils.sourceforge.net/docs/user/rst/quickref.html

Comparison: text v. reST v. DocBook
	http://www.ibm.com/developerworks/library/x-matters24/

Curious
	http://rst2a.com/


Demo list-table
+++++++++++++++

Does this work?

It was found on this page
	http://docutils.sourceforge.net/docs/ref/rst/directives.html

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

.. Yes, it _does_ work.  
   Use it for the tables in the NXDL description.

Numbered Lists
++++++++++++++

What about automatically numbering a list?

	#. How will the numbering look?
	#. Will it look great?
	
	#. Even more great?
	   What about more than one line of text in the source code?

	8. Made a jump in the numbering.
	   But that started a new list and produced a compile error.
	   What about more than one line of text in the source code?
	   Cannot use multiple paragraphs in a list, it seems.
	   Maybe there is a way.
	#. And another ...

	F. Perhaps we can switch to lettering?
	   Only if we start a new list.
	   But we needed a blank line at the switch.
	#. Another lettered item.

.. Yup, that works. 


About Linking
+++++++++++++

What about a link to :ref:`indirect hyperlinks` on another page?

The reSt documentation says that links can be written as::

	`NeXus: User Manual`_

This works for sphinx, as long as the link target
is in the same ``.rst`` document.  
**But**, when the link is in 
a different document, sphinx requires the citation to use::

	:ref:`NeXus User Manual`

and the target must be a section with an explicit
hyperlink definition, such as on the top page of these docs::

	.. _NeXus User Manual:

	######################
	NeXus: User Manual
	######################

This is the correct link: :ref:`NeXus User Manual`.

Missing Links
+++++++++++++

These sections show up as missing links.

Can you find the `history`_ link below?
What about the history_ link below?  
This works: :ref:`History` (or :ref:`history`).

.. _History:

history (not converted yet)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _Utilities:

utilities (not converted yet)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _nxdl_tutorial-creatingnxdlspec:

nxdl_tutorial-creatingnxdlspec (not converted yet)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _nxdata-structure:

nxdata-structure (not converted yet)

.. _NIAC-link:

NIAC description
^^^^^^^^^^^^^^^^

.. _example.data-linking:

example.data-linking (not converted yet)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _cross-reference example:

Section to cross-reference
--------------------------

This is the text of the section.

It refers to the section itself, see :ref:`cross-reference example`.
What about a section on another page, such as :ref:`footnote references`?
