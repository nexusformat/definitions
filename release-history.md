
# Release History

(starting from v3.3)

**`#`** (prefix): issue or pull request

**hash tag**: a specific set of changes, such as `abc1234`

**WIP**: work in progress, not closed at time of release

## v3.3

### Pull Requests
* #540 (merged) issue #539
* #542 (merged) NXmx multimodule and dectris changes
* #549 (closed) fixes #545 - units type AXISUNITS
* #550 (merged) Issue 546 minOccurs=0 to required=false
* #551 (merged) fixes #547: defines ``vector_units`` attribute for NXtransformations
* #554 (merged) Geometry docs #397
* #558 (merged) Schema update #555
* #561 (merged) fixes #560: changes to documentation only
* #565 (closed) Adds missin nComp dimensions
* #566 (closed) remove NXcontainer duplicates
* #568 (merged) Updates from NIAC2016
* #569 (closed) NXstage contributed class
* #578 (merged) fixes #571
* #579 (merged) Update NXdetector.nxdl.xml
* #580 (closed) NXexperiment and NXexperimentdata

### Issues (selected)
* #169: documentation - brief description of new validation tools: cnxvalidate and punx
* #177: base class - removed NXcharacterization
* #486: documentation - main WWW page revised
* #504: duplicate of #574
* #535: base class - removed usage suggestion from NXpositioner
* #536: documentation - ensure index entries are comprehensive
* #543: base class - removed usage suggestion from NXlog
* #545: NXDL Schema - NXtransformations needs new units category: `NX_TRANSFORMATION` -- allows `NX_LENGTH | NX_ANGLE | NX_UNITLESS`
* #546: base class - NXmx use of minOccurs changed to optional
* #546: NXDL Schema - add `@required` attribute (default=true) to `dimensionsType`
* #547: base class - NXtransformations, add `@vector_units` attribute
* #548: base class - added missing `<dim ...` content to NXtransformations
* #548: NXDL Schema - added `dimensions` element to `attributeType` 
* #555: NXDL Schema - `anyUnitsAttr` definition rearranged
* #556: NXDL Schema - allow declarations of dimensions for data values in attributes
* #560: documentation - NXsas documentation revised
* #562: application definition (WIP) - use consistent terms when names are flexible
* #562: base class (WIP) - use consistent terms when names are flexible
* #571: NXDL Schema - `@rank` attribute type remains `NX_CHAR`, documentation changed
* #574: base class - Promote NXreflections to a base class
* #581: documentation - NeXus link structure documented
* #582: documentation - use of NXsubentry described
* #584: documentation - document the `@napimount` attribute

### Commits (selected)
* 9f082210 Draft changes for NIAC 2016
* ab9249c2 Clarify rank and units issues for NXmx and NXtransformations
* 92b607b6 Shrink coordinate system figures a little
* f9ae4e67 Make section of coordinate transformation less repetitous and format style consistently too
* f320d383 As per discussion in NIAC 13 Oct 14, remove redundant point-by-point range specification and change _average_range to _increment_set.
* 3e3a0831 Remove prohibition of use of pixel units in beam centers -- HJB
* 7bcfb8a3 Clarify rank and units issues for NXmx and NXtransformations
* 3db824b5 remove and ignore .DS_Store
* a0148806 typo spotted by Peter Chang
* 876fb36f Emphasize relationship of depends_on and NXtransformations in NXsample
* 12e36520 fixes #177
* 7a92f7b8 fixes #536
* 015eb0ba Clarified the beam_center_x,y documentation regarding length. As agreed upon at the February, 20, 2017 hangout.
* dd57eb45 refs #486
* 6819719a refs #539, fixes #169 brief description of cnxvalidate and punx
* fde3a65a refs #539, note the recent 3.2 release tag
* c5b9b753 refs #539, update URLS, reST autoformatting
* 7c215802 refs #539: make WWW root directory an environment variable
* 2bc51db2 Merge pull request #540 from nexusformat/issue_539
* 100ceddf remove statement advertising NXcollection
* d9e75710 preserve unpublished comment in version control
* 9b8777e1 adapt to new web page
* 92dba800 revert changes to application definitions without agreement
* 5a6164f1 remove (more) advertising of NXcollection for official use
* 433fb8fc express documented time reference in iso8601
* a1b97e93 Merge pull request #542 from nexusformat/NXmx_multimodule_and_dectris_changes
* 5272154f refs #546
* a1563420 fixes #546: change ``minOccurs`` to new ``required`` attribute
* 258b3913 fixes #547: defines ``vector_units`` attribute
* dcda1447 remove vector_units
* 485df904 Merge pull request #551 from nexusformat/issue_547_vector_units_attribute
* 3280bce3 Merge pull request #550 from nexusformat/issue_546_minOccurs_not_allowed_here
* 10ae9182 fixes #552
* 33710029 fixes #556
* 55333239 refs #555 XML Schema changed, python code needs to be updated
* 62abb9e5 fixes #545
* d1635e7f fixes #548
* 0bd6729f refs #555 : Sphinx
* 818324b2 refs #555 Sphinx
* 84c8576c refs #555 : docs build with units described
* 07eb8db1 fixes #555
* 25245408 (origin/NXsas-documentation, NXsas-documentation) fixes #560
* cfc31efe Added ub_matrix to NXsample as discussed on the 26.04.2017 NeXus teleconference Refs #559
* b459b661 (origin/schema_update_555) #555, #558: bumping NXDL version number to 3.3
* 4aa42155 (tag: Schema-3.3) Merge pull request #558 from nexusformat/schema_update_555
* 68abbc7c remove artifacts from python's print()
* 18c727e4 Updates from NIAC 2016
* e1d87e88 (origin/nxreflections_niac2016) NXreflections changes following Jun7 2017 Telco
* aeb9816c Merge pull request #568 from nexusformat/nxreflections_niac2016
* 685efde4 #568 correct ReST indentation errors, split long doc lines
* b6e1287 #568 add symbols table for bounding_box[n, 6]
* f7fecce1 Add dimension n to most fields. Add new dimension m for the experiments field, as it links sets of reflections back to an NXmx entry.
* bbaf17ed fixes #572: in NXDL, "dimensions" before "attribute"
* 79c22dd8 tests #573
* 50487fd9 #573 restore to previous
* f76479fe test #573
* 34360e7f fixes #573
* 99e45b4d fixes #574
* 449b403c #570 turn off PDF manual for now
* 41b660fc #574
* b1a052c9 #537 try *building* the manual if tests succeed
* bc0860f2 #537 pre-processing step worked, try Sphinx next
* c683848c #537 sphinx is now a dependency
* edeaf536 #537 python3-ism
* 7e065a24 #537 prepare a tarball
* 093ec7ef #537 need to study before proceeding with publishing
* 2de23e41 #537 try again with corrected path
* 3d47de24 #537 can we access the tarball?
* fab9c643 #537 resolve py3 Sphinx warnings
* 7a9f596b #537 location
* fb19c531 #537 try PDF manual now
* 80c10520 #537 skip PDF for now on travis-ci
* 02bf0453 #537 diagnose extra footnote cited in NXentry
* 263a2a30 #537 resolve footnote reference
* d0c89201 #537 indentation
* 4964082c Merge branch 'master' into geometry_docs_397
* db55a5b7 (origin/geometry_docs_397) float -> number as in nxdl
* 89c22fde document about vairable length strings
* edecbe25 #567 restore build(s) of PDF manual
* 77e7133e fixes #576
* d5dc391a testing #567 with Sphinx 1.6.3
* b79a976b fixes #567
* 7455d334 Merge pull request #554 from nexusformat/geometry_docs_397
* 7dfb0ac3 fixes #571
* e519bd3a Merge pull request #578 from nexusformat/NX_UINT_571
* 2e5bd7d1 Update NXdetector.nxdl.xml
* e1b33a16 #581 resolve TODO item
* 2a2c2bcc #581 improve example of NeXus link
* 33b59e20 fixes #581 highlight target attribute in index (refs #580), steps to create a NeXus link
* d7cf404c copied from ``design.rst``
* b719564d highlight with a subsection title
* 9e7162fc fixes #388
* d68b35d7 #388
* 9aa01a0e fixes #582
* 715b11a6 #580
* ffb1654e #580 add URL to NX5nativeexternallink
* 6b8a3488 refs #580
* 25e963ba Merge pull request #579 from jacobfilik/detector_serial_number
* fb03c275 Merge pull request #561 from nexusformat/NXsas-documentation
* 412b1138 fixes #584
* bcc37a59 fixes #526
* d1ac9876 (origin/master, origin/HEAD) #562
* 115f9393 #577, #580 start a history file
* ebdf2c9c (HEAD -> master) #577, #580 link to main README
