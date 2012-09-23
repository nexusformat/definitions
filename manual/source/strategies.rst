.. $Id$

.. _Strategies:

======================================================
Strategies for storing information in NeXus data files
======================================================

NeXus may appear daunting, at first, to use.  The number of base classes
is quite large as well as is the number of application definitions.  This chapter
describes some of the strategies that have been recommended for
:index:`how to store <strategies>` information in NeXus data files.

When we use the term *storing*, some might be helped if they consider
this as descriptions for how to *classify* their data.

It is intended for this chapter to grow, with the addition of different use cases
as they are presented for suggestions.

..  +++++++++++++++ The simplest case +++++++++++++++++++

.. _Strategies-simplest:

Strategies: The simplest case(s)
################################

Perhaps the :index:`simplest case <strategies; simplest case(s)>`
might be either a step scan with two or more
columns of data.  Another simple case might be a single image acquired
by an area detector.  In either of these hypothetical
cases, the situation is so simple
that there is little addition information available to be described
(for whatever reason).

Step scan with two or more data columns
=======================================

Consider the case where we wish to store the data from a step scan.
This case may involve two or more *related*
1-D arrays of data to be saved, each
having the same length. For our hypothetical case, we'lll
have these positioners as arrays:

======================   ====================================================
positioner arrays        detector arrays
======================   ====================================================
``ar``, ``ay``, ``dy``   ``I0``, ``I00``, ``time``, ``Epoch``, ``photodiode``
======================   ====================================================


..  +++++++++++++++ The next case +++++++++++++++++++

..  TODO ideas for more cases:
    simple instrument, no application definition
    simple instrument, with application definition
    instrument with multiple detectors, no application definition
    instrument with multiple detectors, with application definition
    instrument with multiple, simultaneous application definitions
    instrument with rapidly changing needs

	.. _Strategies-next:
	
Strategies: The next case
#########################
	
	.. this section was new in 2010-10, we are gathering and adding historical cases ...

The :ref:`NIAC` welcomes suggestions for additional sections in this chapter.

.. TODO: There are some strategies listed elsewhere in the manual.  Find them and cross-reference here.
