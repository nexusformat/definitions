
# Release History

(starting from v3.3)

Note: Issues are referenced by a `#` prefix, specific commits
are referenced by their short hash code, such as `abc1234`.

## v3.3

### Base Classes

#### new additions

* #504, #574: Promote [NXreflections]() to a base class

#### changes

* #546: NXmx use of minOccurs changed to optional
* #547: NXtransformations, add `@vector_units` attribute
* #548: added missing `<dim ...` content to NXtransformations
* #543: removed usage suggestion from NXlog
* #535: removed usage suggestion from NXpositioner

#### work-in-progress
* #562: use consistent terms when names are flexible
#### items removed
* #177: removed NXcharacterization
#### items marked as deprecated

### Application Definitions

#### new additions
#### changes
#### work-in-progress
* #562: use consistent terms when names are flexible
#### items removed
#### items marked as deprecated

### Contributed Definitions

#### new additions
#### changes
#### work-in-progress
#### items removed
#### items marked as deprecated

### NXDL (XML) Schema

#### new additions

* #545: NXtransformations needs new units category: `NX_TRANSFORMATION` -- allows `NX_LENGTH | NX_ANGLE | NX_UNITLESS`
* #546: add `@required` attribute (default=true) to `dimensionsType`
* #548: added `dimensions` element to `attributeType` 

#### changes

* #555: `anyUnitsAttr` definition rearranged
* #556: allow declarations of dimensions for data values in attributes
* #571: `@rank` attribute type remains `NX_CHAR`, documentation changed


#### work-in-progress
#### items removed
#### items marked as deprecated

### Documentation

#### new additions

* #169: documentation - brief description of new validation tools: cnxvalidate and punx
* #581: documentation - NeXus link structure documented
* #582: documentation - use of NXsubentry described
* #584: documentation - document the `@napimount` attribute

#### changes
* #486: documentation - main WWW page revised
* #536: documentation - ensure index entries are comprehensive
* #560: documentation - NXsas documentation revised
#### work-in-progress
#### items removed
#### items marked as deprecated

### Other

#### new additions
#### changes
#### work-in-progress
#### items removed
#### items marked as deprecated

--------

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
### Issues
### Commits (selected)
* ebdf2c9c (HEAD -> master) #577, #580 link to main README
* 115f9393 #577, #580 start a history file
* d1ac9876 (origin/master, origin/HEAD) #562
* bcc37a59 fixes #526
* 98f420d5 #526 needs proofreading before closing issue
* 9b6a8476 #526 one TODO remains
* 412b1138 fixes #584
* fb03c275 Merge pull request #561 from nexusformat/NXsas-documentation
* 25e963ba Merge pull request #579 from jacobfilik/detector_serial_number
* 6b8a3488 refs #580
* ffb1654e #580 add URL to NX5nativeexternallink
* 715b11a6 #580
* 9aa01a0e fixes #582
* d68b35d7 #388
* 15a2eb3f fixes #388 - relocate these words
* 9e7162fc fixes #388
* b719564d highlight with a subsection title
* 024c5091 reST syntax
* 8158833f make new paragraph
* d7cf404c copied from ``design.rst``
* e21ea830 remove extra text
* 33b59e20 fixes #581 highlight target attribute in index (refs #580), steps to create a NeXus link
* 2a2c2bcc #581 improve example of NeXus link
* e1b33a16 #581 resolve TODO item
* 2e5bd7d1 Update NXdetector.nxdl.xml
* e519bd3a Merge pull request #578 from nexusformat/NX_UINT_571
* 7dfb0ac3 fixes #571
* 7455d334 Merge pull request #554 from nexusformat/geometry_docs_397
* b79a976b fixes #567
* d5dc391a testing #567 with Sphinx 1.6.3
* a279d6dc #567 turn off the jenkins PDF build again
* da0bb758 turn off travis-ci build of PDF for now
* 77e7133e fixes #576
* edecbe25 #567 restore build(s) of PDF manual
* 89c22fde document about vairable length strings
* db55a5b7 (origin/geometry_docs_397) float -> number as in nxdl
* 336e2bf1 some tlc
* 4964082c Merge branch 'master' into geometry_docs_397
* a31e8489 typo
* 7ee1609b footnote format
* d0c89201 #537 indentation
* 263a2a30 #537 resolve footnote reference
* 02bf0453 #537 diagnose extra footnote cited in NXentry
* 80c10520 #537 skip PDF for now on travis-ci
* fb19c531 #537 try PDF manual now
* 7a9f596b #537 location
* fab9c643 #537 resolve py3 Sphinx warnings
* 3d47de24 #537 can we access the tarball?
* 2de23e41 #537 try again with corrected path
* 093ec7ef #537 need to study before proceeding with publishing
* 7e065a24 #537 prepare a tarball
* edeaf536 #537 python3-ism
* c683848c #537 sphinx is now a dependency
* bc0860f2 #537 pre-processing step worked, try Sphinx next
* b1a052c9 #537 try *building* the manual if tests succeed
* 41b660fc #574
* 449b403c #570 turn off PDF manual for now
* 99e45b4d fixes #574
* 34360e7f fixes #573
* f76479fe test #573
* 50487fd9 #573 restore to previous
* 79c22dd8 tests #573
* bbaf17ed fixes #572: in NXDL, "dimensions" before "attribute"
* f7fecce1 Add dimension n to most fields. Add new dimension m for the experiments field, as it links sets of reflections back to an NXmx entry.
* 6b6e1287 #568 add symbols table for bounding_box[n, 6]
* 685efde4 #568 correct ReST indentation errors, split long doc lines
* aeb9816c Merge pull request #568 from nexusformat/nxreflections_niac2016
* e1d87e88 (origin/nxreflections_niac2016) NXreflections changes following Jun7 2017 Telco
* 18c727e4 Updates from NIAC 2016
* 68abbc7c remove artifacts from python's print()
* 4aa42155 (tag: Schema-3.3) Merge pull request #558 from nexusformat/schema_update_555
* b459b661 (origin/schema_update_555) #555, #558: bumping NXDL version number to 3.3
* 264117ce remove stray character
* 28ca93a6 corrects: section title too short
* d5fdf77c correct indentation
* cfc31efe Added ub_matrix to NXsample as discussed on the 26.04.2017 NeXus teleconference Refs #559
* 25245408 (origin/NXsas-documentation, NXsas-documentation) fixes #560
* 07eb8db1 fixes #555
* 84c8576c refs #555 : docs build with units described
* 818324b2 refs #555 Sphinx
* 0bd6729f refs #555 : Sphinx
* d1635e7f fixes #548
* 62abb9e5 fixes #545
* 55333239 refs #555 XML Schema changed, python code needs to be updated
* 33710029 fixes #556
* 10ae9182 fixes #552
* 3280bce3 Merge pull request #550 from nexusformat/issue_546_minOccurs_not_allowed_here
* 485df904 Merge pull request #551 from nexusformat/issue_547_vector_units_attribute
* 2a7008e0 clarify documentation
* dcda1447 remove vector_units
* 258b3913 fixes #547: defines ``vector_units`` attribute
* a1563420 fixes #546: change ``minOccurs`` to new ``required`` attribute
* 5272154f refs #546
* 18fb1844 (issue_548_attribute_shape) fix indentation
* a1b97e93 Merge pull request #542 from nexusformat/NXmx_multimodule_and_dectris_changes
* 433fb8fc express documented time reference in iso8601
* 29d2ecce spelling and formatting
* 5a6164f1 remove adverising of NXcollection for official use
* 6cb97234 really restore old versions
* 45709d2a Merge branch 'master' into nxmx
* 92dba800 revert changes to application definitions without agreement
* 9b8777e1 adapt to new web page
* d9e75710 preserve unpublished comment in version control
* 100ceddf remove statement advertising NXcollection
* 2bc51db2 Merge pull request #540 from nexusformat/issue_539
* 7c215802 refs #539: make WWW root directory an environment variable
* 35c8133f refs #539: cross-references
* c5b9b753 refs #539, update URLS, reST autoformatting
* fde3a65a refs #539, note the recent 3.2 release tag
* 6819719a refs #539, fixes #169 brief description of cnxvalidate and punx
* 1b4457d2 Merge branch 'master' of github.com:nexusformat/definitions
* dd57eb45 refs #486
* 41b19a1f another index cross-reference
* 015eb0ba Clarified the beam_center_x,y documentation regarding length. As agreed upon at the February, 20, 2017 hangout.
* 7a92f7b8 fixes #536
* 12e36520 fixes #177
* 5fa79106 Merge continued
* c617690c Rebase continued
* e9212d49 Further merge
* 876fb36f Emphasize relationship of depends_on and NXtransformations in NXsample
* a0148806 typo spotted by Peter Chang
* 3db824b5 remove and ignore .DS_Store
* 7bcfb8a3 Clarify rank and units issues for NXmx and NXtransformations
* 85a6952d Resolved conflicts
* 85d31b49 Merge with current version -- HJB Merge remote-tracking branch 'origin/master' into NXmx_multimodule_and_dectris_changes
* 3e3a0831 Remove prohibition of use of pixel units in beam centers -- HJB
* f320d383 As per discussion in NIAC 13 Oct 14, remove redundant point-by-point range specification and change _average_range to _increment_set.
* 97ce82ea Emphasize relationship of depends_on and NXtransformations in NXsample
* f9ae4e67 Make section of coordinate transformation less repetitous and format style consistently too
* 92b607b6 Shrink coordinate system figures a little
* 2c3989a1 typo spotted by Peter Chang
* 2a64adda Merge branch 'master' into nxmx
* 5f56a8f0 remove and ignore .DS_Store
* ab9249c2 Clarify rank and units issues for NXmx and NXtransformations
* 9f082210 Draft changes for NIAC 2016
