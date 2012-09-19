.. $Id$

TODO items
----------

* Should we produce two or more separate books?
* Build User Guide and Reference Documentation 
  as separate but related sphinx documents
  
  * share common labels
  * point to common URL as documentation start
  * print as separate PDF documents
  * probably need a third document to coordinate them

* Rendering of tables in NXDL classes is not done yet
* fix math source formatting between html and pdf

  * see examples at http://theoretical-physics.net/dev/src/math/integration.html

* tables, examples, and figures: treat them consistently with titles, captions, and cross-references
* stop the section numbering for very deep subsections (2.1.4.1.2.1.3.1.4.5.1.4.1... is just ridiculous)
* Convert NXDL doc strings into ReST
   
   * Can the indentation be preserved using CDATA blocks?
   * Yes.  See: http://www.w3schools.com/xml/xml_cdata.asp

* note there is a figure number extension: https://bitbucket.org/arjones6/sphinx-numfig/wiki/Home


NeXus home page
---------------

We've had a request for examples to improve the NeXus home page.
Here are some examples that use sphinx in one way or another:

* http://doc.openerp.com/v6.0/
* https://docs.djangoproject.com/en/1.3/

Suggestion
----------

Use a container directive to build a table and specify a name
for the container that can be used by  CSS spec to decorate the
table appropriately.  Perhaps with this starting point:



.. container:: formatted-table

  ==================================  ==================================
  left                                right
  ==================================  ==================================
  left side                           
  ==================================  ==================================

  .. csv-table:: Frozen Delights!
     :header: "Treat", "Quantity", "Description"
     :widths: 15, 10, 30

     "Albatross", 2.99, "On a stick!"
     "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
     crunchy, now would it?"
     "Gannet Ripple", 1.99, "On a stick!"

Something Else
-----------------

.. figure:: nexuslogo.png
    :width: 200px
    :align: center
    :height: 100px
    :alt: alternate text
    :figclass: align-center

    figure are like images but with a caption

    and whatever else you wish to add

    .. code-block:: python

        import image



Fun with the Index
----------------------

This is a paragraph where we have some :index:`fun <!item1; item2>` with the index.

.. index::
    single: item3, item4

You can even combine separate index entries under one directive.

.. index::
    pair:     item6;  item7
    pair:     item8;  item9
    single:   item1;  item5
    see:      item11; item12
    seealso:  item13; item14
    see:      item8;  item6
    see:      item4;  item8;  item6

Emphasize an **item** in the index with a preceding bang (!).

.. index:: !item0

There are index entries that appear on a :index:`single <index1, index2>` line.
Sometimes, they have some :index:`hierarchy <!index3; index4>`.
It is possible to :index:`coordinate <pair: index5; index6>` entries,
even with some complexity.

What about the :index:`tertiary, inline Docbook index <i primary; i secondary; i tertiary>` entry?
This is not the way to handle the *seealso* :index:`element <single: index7, index8; pair: i four; i five>`.
Instead, use :index:`two <single: index7s, index8s>` :index:`separate <see: i four S; i five S>` index roles.
