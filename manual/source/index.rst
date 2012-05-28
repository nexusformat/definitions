.. $Id$

===================
NeXus Documentation
===================

User Manual and Reference Documentation
---------------------------------------

.. toctree::
   :maxdepth: 2
   :glob:
   
   volume1
   volume2

This manual built |today|

..  Suggestions for adding to this manual:

    Look for some other "section" such as "introduction.rst" and act similarly.
    Any examples go as text files in the examples/ subdirectory and are pulled into the
    DocBook inside a programlisting using xi:include elements.  Look for the pattern
    or wing it.  If you are game for it, add index entries.  Many examples of the
    constructs you might use are already in the manual.  Please apply::

	    svn propset svn:keywords Id strides.rst
	    svn propset svn:eol-style native strides.rst
