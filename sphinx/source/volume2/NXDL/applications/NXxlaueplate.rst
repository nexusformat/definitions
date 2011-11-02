..  _NXxlaueplate:

############
NXxlaueplate
############

.. index::  ! . NXDL applications; NXxlaueplate

category:
    applications

NXDL source:
    NXxlaueplate
    
    (http://svn.nexusformat.org/definitions/trunk/applications/NXxlaueplate.nxdl.xml)

version:
    1.0b

SVN Id:
    $Id$

extends class:
    :ref:`NXxlaue`

other classes included:
    :ref:`NXdetector`, :ref:`NXentry`, :ref:`NXinstrument`

documentation:
    This is the application definition for raw data from a single crystal laue
    camera witha an image plate as a detector. It extends NXxlaue.
    


.. rubric:: Basic Structure of **NXxlaueplate**

.. code-block:: text
    :linenos:
    
    NXxlaueplate (application definition, version 1.0b)
      (overlays NXentry)
      entry:NXentry
        definition:NX_CHAR
        instrument:NXinstrument
          detector:NXdetector
            diameter:NX_FLOAT
    

.. rubric:: Symbols used in definition of **NXxlaueplate**

No symbols are defined in this NXDL file





.. rubric:: Comprehensive Structure of **NXxlaueplate**

+---------------------+----------+-------+-------------------------------+
| Name and Attributes | Type     | Units | Description (and Occurrences) |
+=====================+==========+=======+===============================+
| class               | NX_FLOAT | ..    | ..                            |
+---------------------+----------+-------+-------------------------------+
