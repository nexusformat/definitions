.. $Id$

.. image:: img/NeXus.png
	:width: 40%

=========================================================
User Manual and Reference Documentation
=========================================================

..
	User Manual and Reference Documentation
	---------------------------------------

http://www.nexusformat.org/

.. toctree::
    :maxdepth: 2
    :numbered: 4

    user_manual
    ref_doc

.. toctree::
    :maxdepth: 1

    authorgroup
    community
    installation
    utilities
    faq
    history
    revhistory
    copyright

-----------

.. rubric:: Publishing Information

This manual built |today|.  

.. seealso:: 

   This document is available in different formats:
   
   :online HTML:
   	http://download.nexusformat.org/doc/html/UserManual.html
   :PDF:
   	:download:`nexus.pdf` :download:`( <nexus.log>`available via online HTML link above)
   :epub:
   	:download:`NeXusManual.epub` (available via online HTML link above)
   
   A very brief overview is also available.
   
   :HTML:
   	http://svn.nexusformat.org/definitions/trunk/misc/impatient/_build/html/index.html


..  Suggestions for adding to this manual:

    Look for some other "section" such as "introduction.rst" and act similarly.
    Any examples go as text files in the examples/ subdirectory and are pulled into 
    Sphinx inside a :directive:`literalcode` directive.  Look for the pattern
    or wing it.  If you are game for it, add index entries.  Many examples of the
    constructs you might use are already in the manual.  Please apply these subversion
    properties to the source code files (example shown with hypothetical file 
    ``thing.rst``)::

	    svn propset svn:keywords Id thing.rst
	    svn propset svn:eol-style native thing.rst
