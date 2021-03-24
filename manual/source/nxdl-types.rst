==========================
NXDL Field Types and Units
==========================

.. index::
    see: type; data type
    ! single: data type

.. _nxdl-types:
		
Field Types allowed in NXDL specifications
##########################################

Field types for use in NXDL
describe the expected type of data for a NeXus field. These terms are very
broad. More specific terms are used in actual NeXus data files that describe
size and array dimensions. In addition to the types in the following table, the
``NAPI`` type is defined when one wishes to permit a field
with any of these data types. The default type ``NX_CHAR`` is applied in cases 
where a field or attribute is defined in an NXDL specification without explicit assignment of a ``type``.

..  Generated from ../nxdlTypes.xsd via a custom Python tool
    ../../utils/types2rst.py ../../nxdlTypes.xsd > types.table

.. index::
   seealso: binary data; NX_BINARY

.. include:: types.table



.. index::
   ! single: unit category

.. _nxdl-units:

Unit Categories allowed in NXDL specifications
##############################################

Unit categories in NXDL specifications
describe the expected type of units for a NeXus field. They should describe
valid units consistent with the :ref:`NeXus units <Design-Units>` section.
The values for unit categories are restricted (by
an enumeration) to the following table.

..  Generated from ../nxdlTypes.xsd via a custom Python tool
    ../../utils/units2rst.py ../../nxdlTypes.xsd > units.table

.. include:: units.table
