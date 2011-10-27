..  _NXuser:

######
NXuser
######

.. index::  ! . NXDL base_classes; NXuser

category:
    base_classes

NXDL source:
    NXuser
    
    (http://svn.nexusformat.org/definitions/trunk/base_classes/NXuser.nxdl.xml)

version:
    1.0

SVN Id:
    $Id$

extends class:
    :ref:`NXobject`

other classes included:
    none

documentation:
    Template of user's contact information.  The format allows more
    than one user with the same affiliation and contact information,
    but a second NXuser group should be used if they have different
    affiliations, etc.
    


.. rubric:: Basic Structure of **NXuser**

.. code-block:: text
    :linenos:
    
    NXuser (base class, version 1.0)
      address:NX_CHAR
      affiliation:NX_CHAR
      email:NX_CHAR
      facility_user_id:NX_CHAR
      fax_number:NX_CHAR
      name:NX_CHAR
      role:NX_CHAR
      telephone_number:NX_CHAR
    

.. rubric:: Symbols used in definition of **NXuser**

No symbols are defined in this NXDL file



.. rubric:: Comprehensive Structure of **NXuser**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
