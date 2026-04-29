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

Highlights of each release are described below.  For more details, see our wiki
(https://github.com/nexusformat/definitions/wiki/Release-Notes)
which provides links to the Release Notes (itemized list of changes) for any release.

.. incoming change for next release

  v2026.mm
  ++++++++

  for release sometime in *2026*

v2026.01
++++++++

released *2026-02-19*

This is a patch release and contains new contributions from the
[FAIRmat consortium](https://www.fairmat-nfdi.eu/fairmat/) and the wider NeXus
community.

Summary statistics from the GitHub definitions repository show this activity
since the (previous) v2025.11 release:

=============   ========
activity        quantity
=============   ========
Pull Requests   15
Issues          4
Commits         28
=============   ========

See the wiki for more details:
https://github.com/nexusformat/definitions/wiki/releasenotes__v2026.01

New Features
------------

New contributed application definitions include ``NXspm``, ``NXafm``, ``NXstm``,
and ``NXstm`` accompanied by some new base classes.

The parameter fields in ``NXparameter`` now has some optional attributes to store optimization
metadata and ``NXfit_function`` has been updated to match.

Fixes
-----

Make documentation of deprecated attributes visible. The one year curation
requirement for contributions is now lifted.

Maintenance
-----------

Documentation for some application definitions has been recategorized. Make
tooling work for newer Python. Fix incorrect referencing of inherited nodes of
different tag type.

Deprecations
------------

The ``NXnote`` called ``thumbnail`` in ``NXentry`` has a ``type`` attribute that
is now deprecated in favour of a field of the same name.


v2025.11
++++++++

released *2025-11-13*

This release is the result of [NIAC2024](https://www.nexusformat.org/NIAC2024.html)
and contains substantial contributions from the
[FAIRmat consortium](https://www.fairmat-nfdi.eu/fairmat/) and the wider NeXus
community. It marks the first release of new base classes and application
definitions in the fields of atom probe microscopy, photoemission & core-level
spectroscopy, optical spectroscopy, electron microscopy, and, computational and
constructive solid geometry.

Summary statistics from the GitHub definitions repository show this activity
since the (previous) v2024.02 release:

=============   ========
activity        quantity
=============   ========
Pull Requests   118
Issues          10
Commits         592
=============   ========

See the wiki for more details:
https://github.com/nexusformat/definitions/wiki/releasenotes__v2025.11

New Features
------------

New application definitions include ``NXapm``, ``NXazint1d``, ``NXazint2d``,
``NXem``, ``NXellipsometry``, ``NXmpes``, ``NXmpes_arpes``,
``NXoptical_spectroscopy``, ``NXstress``, and ``NXxps``. Accompanying them are
numerous new base classes.

``NXobject`` now has some optional groups and formalizes field names using the
new partial name types to reserve their accompanying fields. Also new optional
identifier fields have been added. ``NXcomponent`` has been introduced as a
superclass for constituent parts of any instruments and many base classes now
extend that. ``NXcoordinate_system`` allows local coordinate frames to be
specified and used in ``NXtransformations`` chains.


Fixes
-----

In base classes, any field units attribute can be specified as concrete
example units in place of the limited set of NeXus defined categories.
Enumerations can be open allowing new custom values to be used if an
appropriate attribute is set.


Maintenance
-----------

Documentation for ``NXdata`` has been rewritten with new examples of its usage
across data of differing dimensions. ``NeXus_repository`` and ``NeXus_release``
fields have added to ``NXroot``. Rotation fields in ``NXtransformations`` for left handed
coordinate systems has been specified.

Deprecations
------------

Removed remaining pages from previous website. In ``NXdata``,
``scaling_factor`` and ``offset`` have been deprecated. In ``NXroot``,
``NeXus_version`` is no longer of use with the frozen state of the NeXus API.


v2024.02
++++++++

released *2024-02-09*

This release is the result of a NIAC meeting in 2022-09,
NeXus Code Camps in 2022-06 and 2023-06,
and substantial work by the NeXus Community, the FAIRmat consortium and NIAC members.

Summary statistics from the GitHub definitions repository show
this activity since the (previous) v2022.07 release:

=============   ========
activity        quantity
=============   ========
Pull Requests   67
Issues          34
Commits         413
=============   ========

See the wiki for more details:
https://github.com/nexusformat/definitions/wiki/releasenotes__v2024.02

New Features
------------

Add ``h5wasm`` and ``H5Web`` to HDF tools list.

Allow ``recommended`` attribute as alias for ``optional``, but with the
recommendation that this attribute be specified.

NXxas: Added `NXdata/mode` to report detection method.

Add various flux fields to NXbeam.

Add virtual pixel handling to NXdetector.

Add h5py example scripts.

Add equipment_component attribute to NXtransformations.

Add countrate_correction_lookup_table to NXdetector for NXmx.

Allow axis fields to be numbers or strings and add a default_slice attribute to NXdata.

Add new NXdetector_channel base class.

Add favicon to manual web pages.

Add many new contributed definitions from FAIRmat.

Allow NeXus definitions to be created with YAML.

Add recent contributors links to NeXus classes html pages.

Improve link navigation in application definition items and collapse doc strings.


Fixes
-----------

Add missing close parenthesis in rendering of suggested target.

Amend text that mistakenly deprecated NXaperture.

Generalize NXsource type for electron sources.

Maintenance
-----------

NXdata: clarify how errors are described in documentation; remove obsolete dimension
index attribute; clarify that attributes that name other fields must be existing
children of group; improve documentation on axes.

NXmx: clarify pixel size, update NXbeam documentation on incident_wavelength_spectrum,
make countrate_correction_lookup_table optional

NXsas: Various fields and groups changed to optional. Only those deemed
necessary for data reduction are required.

NXtransformations: Add ``equipment_component`` attribute.

NXxas: `data` fields` changed from `NX_INT` to `NX_NUMBER`.

NXxpcs: clarify use of ``entry_identifier``, ``entry_identifier_uuid``, and ``scan_number``;
fix some units.

Clarify how NXbeam can be in NXinstrument groups or NXsample.



Deprecations
------------

NXdata: deprecate `errors` field in favor of `FIELDNAME_errors` for the signal field.

..
  Contributors
  ------------

v2022.07
++++++++

released *2022-08-02*

This is a bugfix release. See notes on wiki: https://github.com/nexusformat/definitions/wiki/releasenotes__v2022.07

v2022.06
++++++++

released *2022-07-05*

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

See the wiki for more details:
https://github.com/nexusformat/definitions/wiki/releasenotes__v2022.06

.. nothing to report here
  Notice
  ------

Breaking Changes
----------------

* Included PDF files moved ``/pdf/`` to ``/_static/``.

* Minimum Python requirement (for testing and building documentation):  3.7

* ``NXsample``: Removed group named ``temperature``.

* ``NXsnsevent`` & ``NXsnshisto``: category changed to ``application`` (was ``base``)

* Publishing workflow completely rebuilt in Python, now in ``/dev_tools/``
  directory (was in ``/utils/``).  All Python code adheres to automated
  code style checking (``black`` and ``flake8``).

New Features
------------

* contributed definitions:

  * atom probe microscopy
  * electron microscopy
  * ellipsometry
  * multidimensional photoemission spectroscopy
  * ``NXregion``
  * X-ray photon correlation spectroscopy

* Full vocabulary (names of all groups, fields, attributes, and links) now built
  and published in the manual.

* ``NX_COMPLEX`` data type to describe complex numbers.

* ``NX_COUNT`` unit type to describe counting events.

Enhancements
------------

* All classes provide a list of reST & HTML anchors to every defined item
  (groups, fields, attributes, & links).

Maintenance
-----------

* Add

  * ``depends_on`` (field) and ``NXtransformations`` (group)
    to more base classes.
  * ``NXdetector``: ``image_key``
  * ``NXdetector``, ``NXmx``: ``countrate_correction_lookup_table``

* Change GitHub default branch to ``main`` (was ``master``).

* Clarify:

  * naming rule of NXDL XML files
  * symbol table in NXDL files
  * ``NXdetector``: ``dimensions``
  * how ``default`` attribute is used to find the plottable data
  * ``NXBeam``: various symbols and polarization fields

* Documentation built and published from GitHub Actions workflow

* Switch repository default branch from master to main.

* Units of flux corrected.

* Various documentation revised:

  * Description of links

Deprecations
------------

* ``incr`` attribute of ``dimensionType``
* ``NXspecdata`` contributed definition withdrawn and removed.

Contributors
------------

In addition to the NIAC members, these people have contributed to this release:

* Advanced Light Source

  * Dylan McReynolds
  * Ron Pandolfi
  * Juliane Reinhardt
  * Padraic Shafer

* Advanced Photon Source

  * Daniel Ching
  * Miaoqi Chu
  * Suresh Narayanan
  * Qingteng Zhang

* Dectris

  * Sophie Hotz
  * Kal Conley

* Diamond Light Source

  * Tim Snow

* FAIRmat

  * Carola Emminger
  * Florian Dobener
  * Markus Kühbach
  * Andrea Albino

* National Synchrotron Light Source II

  * Abby Giles
  * Andi Barbour

v2020.10
++++++++

released *2020-12-08*

    * see Release Notes wiki: https://github.com/nexusformat/definitions/wiki/releasenotes__v2020.10

v2020.1
+++++++

released *2020-01-31*

    * see Release Notes wiki: https://github.com/nexusformat/definitions/wiki/releasenotes__v2020.1
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
