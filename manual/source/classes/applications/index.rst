.. index::
     ! see: class definitions; application definition
     ! application definition

.. _application.definitions:

Application Definitions
#########################

A description of each NeXus application definition is given.
NeXus application definitions define the *minimum*
set of terms that
*must* be used in an instance of that class.
Application definitions also may define terms that
are optional in the NeXus data file.  The definition, in this case,
reserves the exact term by declaring its spelling and description.
Consider an application definitions as a *contract*
between a data provider (such as the beam line control system) and a 
data consumer (such as a data analysis program for a scientific technique)
that describes the information is certain to be available in a data file.

.. toctree::
    :maxdepth: 1
    :glob:
    
    NX*
