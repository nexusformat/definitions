.. $Id$

===================
NeXus Documentation
===================

User Manual and Reference Documentation
---------------------------------------

.. toctree::
	:maxdepth: 1

	frontinfo

.. toctree::
	:maxdepth: 2
	:numbered:

	volume1
	volume2

.. toctree::
	:maxdepth: 1

	authorgroup
	revhistory
	license

This manual built |today|

..  Suggestions for adding to this manual:

    Look for some other "section" such as "introduction.rst" and act similarly.
    Any examples go as text files in the examples/ subdirectory and are pulled into the
    DocBook inside a programlisting using xi:include elements.  Look for the pattern
    or wing it.  If you are game for it, add index entries.  Many examples of the
    constructs you might use are already in the manual.  Please apply these subversion
    properties to the source code files (example shown with hypothetical file 
    ``thing.rst``)::

	    svn propset svn:keywords Id thing.rst
	    svn propset svn:eol-style native thing.rst
