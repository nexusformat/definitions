..
  This file describes user-visible changes between the versions.

  Highlights from the Change History, especially new releases,
  should be added to manual/history.rst.

  subsections could include these headings (in this order), omit if no content

    Notice
    Breaking Changes
    New Features and/or Enhancements
    Fixes
    Maintenance
    Deprecations
    Contributors

Change History
##############

v2022.06
++++++++

expected release *2022-07-01*

This release is the result of
a virtual NIAC meeting in 2022-03,
NeXus Code Camps in 2021-03 and 2022-06,
and substantial work by both the NeXus Community and NIAC members.

Summary statistics from the GitHub definitions repository show
this activity since the (previous) v2020.10 release:

=============   ========
activity        quantity
=============   ========
Pull Requests   134
Issues          101
Commits         250
=============   ========

Notice
------

Breaking Changes
----------------

* Included PDF files moved `/pdf/` to `/_static/`.

* Minimum Python requirement (for testing and building documentation):  3.7

* ``NXsnsevent`` & ``NXsnshisto`` category changed to ``application`` (was ``base``)

* ``NXspecdata`` contributed definition withdrawn and removed.

* Publishing workflow completely rebuilt in Python now in ``/dev_tools/``
  directory (was in ``/utils/``).  All Python code adheres to automated
  code style checking (``black`` and ``flake8``).

New Features / Enhancements
---------------------------

* New contributed definitions for electron microscopy, X-ray ptychography.

* All classes provide a list of reST & HTML anchors to every defined item
  (groups, fields, attributes, & links).

* Full vocabulary (names of all groups, fields, attributes, and links) now built
  and published in the manual.

* new ``NX_COMPLEX`` datatype to describe complex numbers.

Maintenance
-----------

* Add ``depends_on`` (field) and ``NXtransformations`` (group) to more base classes.

* Various documentation revised:

  * Description of links

* Documentation built and published from GitHub Actions workflow

* Switch repository default branch from master to main.

Deprecations
------------

Contributors
------------

In addition to the NIAC members, these people have made contributions
to this release:

* 

v2020.10
++++++++

released *2020-12-08*

    * see Release Notes wiki: https://github.com/nexusformat/definitions/wiki/releasenotes_v2020.10

v2020.1
+++++++

released *2020-01-31*

    * see Release Notes wiki: https://github.com/nexusformat/definitions/wiki/releasenotes_v2020.1
    * The manual is now published through GitHub Pages: https://manual.nexusformat.org
    * We have a DOI (with zenodo https://zenodo.org/record/3629571) that updates with each release of the definitions repository.  The DOI link is noted on our GitHub home page.

v2018.5
++++++++

released *2018-05-15*

    * `v2018.5 <https://github.com/nexusformat/definitions/releases/tag/v2018.5>`_
       see release notes: https://github.com/nexusformat/definitions/wiki/releasenotes__v2018.5
    * `#597 <https://github.com/nexusformat/definitions/issues/597>`_
       changed versioning scheme and procedures

Releases before v2018.5
+++++++++++++++++++++++

    * 3.3
    * 3.2
    * see Release Notes wiki: https://github.com/nexusformat/definitions/wiki/Release-Notes
