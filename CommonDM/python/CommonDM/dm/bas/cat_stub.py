# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/bas/cat_stub.py
# PyXB bindings for NamespaceModule
# NSM:c307896550940a86ed318a515fbd77694cbd7804
# Generated 2014-03-17 18:50:36.640598 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:a3e7637c-adfc-11e3-9f2e-c4d98710dc86')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import CommonDM.dm.sys_stub
import CommonDM.dm.bas.utd_stub
import CommonDM.dm.sys.sgs_stub
import CommonDM.dm.ins.nis_stub
import CommonDM.dm.bas.img_stub
import CommonDM.dm.bas.dtd_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/cat', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
#ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
#ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a Python instance."""
    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=Namespace.fallbackNamespace(), location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, _fallback_namespace=default_namespace)


# Atomic SimpleTypeDefinition
class catalogFileFormat (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of allowed formats for catalogs stored in file"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogFileFormat')
    _Documentation = u'List of allowed formats for catalogs stored in file'
catalogFileFormat._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=catalogFileFormat, enum_prefix=None)
catalogFileFormat.FITS = catalogFileFormat._CF_enumeration.addEnumeration(unicode_value=u'FITS')
catalogFileFormat.CSV = catalogFileFormat._CF_enumeration.addEnumeration(unicode_value=u'CSV')
catalogFileFormat.gzippedCSV = catalogFileFormat._CF_enumeration.addEnumeration(unicode_value=u'gzippedCSV')
catalogFileFormat.TSV = catalogFileFormat._CF_enumeration.addEnumeration(unicode_value=u'TSV')
catalogFileFormat.VOTable = catalogFileFormat._CF_enumeration.addEnumeration(unicode_value=u'VOTable')
catalogFileFormat._InitializeFacetMap(catalogFileFormat._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'catalogFileFormat', catalogFileFormat)

# Atomic SimpleTypeDefinition
class catalogUCDRecord (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of allowed properties for the catalog"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogUCDRecord')
    _Documentation = u'List of allowed properties for the catalog'
catalogUCDRecord._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=catalogUCDRecord, enum_prefix=None)
catalogUCDRecord.pos_eq_RA = catalogUCDRecord._CF_enumeration.addEnumeration(unicode_value=u'pos.eq.RA')
catalogUCDRecord.pos_eq_DEC = catalogUCDRecord._CF_enumeration.addEnumeration(unicode_value=u'pos.eq.DEC')
catalogUCDRecord._InitializeFacetMap(catalogUCDRecord._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'catalogUCDRecord', catalogUCDRecord)

# Atomic SimpleTypeDefinition
class catalogPropertyType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of allowed properties for the catalog"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogPropertyType')
    _Documentation = u'List of allowed properties for the catalog'
catalogPropertyType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=catalogPropertyType, enum_prefix=None)
catalogPropertyType.double = catalogPropertyType._CF_enumeration.addEnumeration(unicode_value=u'double')
catalogPropertyType.float = catalogPropertyType._CF_enumeration.addEnumeration(unicode_value=u'float')
catalogPropertyType.char100 = catalogPropertyType._CF_enumeration.addEnumeration(unicode_value=u'char100')
catalogPropertyType.int64 = catalogPropertyType._CF_enumeration.addEnumeration(unicode_value=u'int64')
catalogPropertyType.int32 = catalogPropertyType._CF_enumeration.addEnumeration(unicode_value=u'int32')
catalogPropertyType._InitializeFacetMap(catalogPropertyType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'catalogPropertyType', catalogPropertyType)

# Complex type catalogCoverage with content type ELEMENT_ONLY
class catalogCoverage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogCoverage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}SpectralCoverage uses Python identifier SpectralCoverage
    __SpectralCoverage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpectralCoverage'), 'SpectralCoverage', '__httpeuclid_esa_orgschemabascat_catalogCoverage_httpeuclid_esa_orgschemabascatSpectralCoverage', False)

    
    SpectralCoverage = property(__SpectralCoverage.value, __SpectralCoverage.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}SpatialCoverage uses Python identifier SpatialCoverage
    __SpatialCoverage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpatialCoverage'), 'SpatialCoverage', '__httpeuclid_esa_orgschemabascat_catalogCoverage_httpeuclid_esa_orgschemabascatSpatialCoverage', False)

    
    SpatialCoverage = property(__SpatialCoverage.value, __SpatialCoverage.set, None, None)


    _ElementMap = {
        __SpectralCoverage.name() : __SpectralCoverage,
        __SpatialCoverage.name() : __SpatialCoverage
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogCoverage', catalogCoverage)


# Complex type catalogContainer with content type ELEMENT_ONLY
class catalogContainer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogContainer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}CatalogMetadata uses Python identifier CatalogMetadata
    __CatalogMetadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CatalogMetadata'), 'CatalogMetadata', '__httpeuclid_esa_orgschemabascat_catalogContainer_httpeuclid_esa_orgschemabascatCatalogMetadata', False)

    
    CatalogMetadata = property(__CatalogMetadata.value, __CatalogMetadata.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}GenericHeader uses Python identifier GenericHeader
    __GenericHeader = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GenericHeader'), 'GenericHeader', '__httpeuclid_esa_orgschemabascat_catalogContainer_httpeuclid_esa_orgschemabascatGenericHeader', False)

    
    GenericHeader = property(__GenericHeader.value, __GenericHeader.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}SourceMetadata uses Python identifier SourceMetadata
    __SourceMetadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceMetadata'), 'SourceMetadata', '__httpeuclid_esa_orgschemabascat_catalogContainer_httpeuclid_esa_orgschemabascatSourceMetadata', False)

    
    SourceMetadata = property(__SourceMetadata.value, __SourceMetadata.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}CatalogStorage uses Python identifier CatalogStorage
    __CatalogStorage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CatalogStorage'), 'CatalogStorage', '__httpeuclid_esa_orgschemabascat_catalogContainer_httpeuclid_esa_orgschemabascatCatalogStorage', False)

    
    CatalogStorage = property(__CatalogStorage.value, __CatalogStorage.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}CatalogID uses Python identifier CatalogID
    __CatalogID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CatalogID'), 'CatalogID', '__httpeuclid_esa_orgschemabascat_catalogContainer_httpeuclid_esa_orgschemabascatCatalogID', False)

    
    CatalogID = property(__CatalogID.value, __CatalogID.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}CatalogCoverage uses Python identifier CatalogCoverage
    __CatalogCoverage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CatalogCoverage'), 'CatalogCoverage', '__httpeuclid_esa_orgschemabascat_catalogContainer_httpeuclid_esa_orgschemabascatCatalogCoverage', False)

    
    CatalogCoverage = property(__CatalogCoverage.value, __CatalogCoverage.set, None, None)


    _ElementMap = {
        __CatalogMetadata.name() : __CatalogMetadata,
        __GenericHeader.name() : __GenericHeader,
        __SourceMetadata.name() : __SourceMetadata,
        __CatalogStorage.name() : __CatalogStorage,
        __CatalogID.name() : __CatalogID,
        __CatalogCoverage.name() : __CatalogCoverage
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogContainer', catalogContainer)


# Complex type catalogPropertyList with content type ELEMENT_ONLY
class catalogPropertyList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogPropertyList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}PropertyList uses Python identifier PropertyList
    __PropertyList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PropertyList'), 'PropertyList', '__httpeuclid_esa_orgschemabascat_catalogPropertyList_httpeuclid_esa_orgschemabascatPropertyList', True)

    
    PropertyList = property(__PropertyList.value, __PropertyList.set, None, None)


    _ElementMap = {
        __PropertyList.name() : __PropertyList
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogPropertyList', catalogPropertyList)


# Complex type catalogProperty with content type ELEMENT_ONLY
class catalogProperty (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogProperty')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}Label uses Python identifier Label
    __Label = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Label'), 'Label', '__httpeuclid_esa_orgschemabascat_catalogProperty_httpeuclid_esa_orgschemabascatLabel', False)

    
    Label = property(__Label.value, __Label.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpeuclid_esa_orgschemabascat_catalogProperty_httpeuclid_esa_orgschemabascatDescription', False)

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Type'), 'Type', '__httpeuclid_esa_orgschemabascat_catalogProperty_httpeuclid_esa_orgschemabascatType', False)

    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}UCD uses Python identifier UCD
    __UCD = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'UCD'), 'UCD', '__httpeuclid_esa_orgschemabascat_catalogProperty_httpeuclid_esa_orgschemabascatUCD', False)

    
    UCD = property(__UCD.value, __UCD.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}NullValue uses Python identifier NullValue
    __NullValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NullValue'), 'NullValue', '__httpeuclid_esa_orgschemabascat_catalogProperty_httpeuclid_esa_orgschemabascatNullValue', False)

    
    NullValue = property(__NullValue.value, __NullValue.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}utype uses Python identifier utype
    __utype = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'utype'), 'utype', '__httpeuclid_esa_orgschemabascat_catalogProperty_httpeuclid_esa_orgschemabascatutype', False)

    
    utype = property(__utype.value, __utype.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemabascat_catalogProperty_httpeuclid_esa_orgschemabascatUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemabascat_catalogProperty_httpeuclid_esa_orgschemabascatName', False)

    
    Name = property(__Name.value, __Name.set, None, None)


    _ElementMap = {
        __Label.name() : __Label,
        __Description.name() : __Description,
        __Type.name() : __Type,
        __UCD.name() : __UCD,
        __NullValue.name() : __NullValue,
        __utype.name() : __utype,
        __Unit.name() : __Unit,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogProperty', catalogProperty)


# Complex type partitioningRange with content type ELEMENT_ONLY
class partitioningRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'partitioningRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}SelectionFilter uses Python identifier SelectionFilter
    __SelectionFilter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SelectionFilter'), 'SelectionFilter', '__httpeuclid_esa_orgschemabascat_partitioningRange_httpeuclid_esa_orgschemabascatSelectionFilter', False)

    
    SelectionFilter = property(__SelectionFilter.value, __SelectionFilter.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}MaxValue uses Python identifier MaxValue
    __MaxValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxValue'), 'MaxValue', '__httpeuclid_esa_orgschemabascat_partitioningRange_httpeuclid_esa_orgschemabascatMaxValue', False)

    
    MaxValue = property(__MaxValue.value, __MaxValue.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}MinValue uses Python identifier MinValue
    __MinValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinValue'), 'MinValue', '__httpeuclid_esa_orgschemabascat_partitioningRange_httpeuclid_esa_orgschemabascatMinValue', False)

    
    MinValue = property(__MinValue.value, __MinValue.set, None, None)


    _ElementMap = {
        __SelectionFilter.name() : __SelectionFilter,
        __MaxValue.name() : __MaxValue,
        __MinValue.name() : __MinValue
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'partitioningRange', partitioningRange)


# Complex type catalogPartitionStorage with content type ELEMENT_ONLY
class catalogPartitionStorage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogPartitionStorage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}DataContainer uses Python identifier DataContainer
    __DataContainer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataContainer'), 'DataContainer', '__httpeuclid_esa_orgschemabascat_catalogPartitionStorage_httpeuclid_esa_orgschemabascatDataContainer', False)

    
    DataContainer = property(__DataContainer.value, __DataContainer.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Range uses Python identifier Range
    __Range = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Range'), 'Range', '__httpeuclid_esa_orgschemabascat_catalogPartitionStorage_httpeuclid_esa_orgschemabascatRange', False)

    
    Range = property(__Range.value, __Range.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemabascat_catalogPartitionStorage_httpeuclid_esa_orgschemabascatId', False)

    
    Id = property(__Id.value, __Id.set, None, None)


    _ElementMap = {
        __DataContainer.name() : __DataContainer,
        __Range.name() : __Range,
        __Id.name() : __Id
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogPartitionStorage', catalogPartitionStorage)


# Complex type catalogSpectralCoverage with content type ELEMENT_ONLY
class catalogSpectralCoverage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogSpectralCoverage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}SpectrumRange uses Python identifier SpectrumRange
    __SpectrumRange = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpectrumRange'), 'SpectrumRange', '__httpeuclid_esa_orgschemabascat_catalogSpectralCoverage_httpeuclid_esa_orgschemabascatSpectrumRange', True)

    
    SpectrumRange = property(__SpectrumRange.value, __SpectrumRange.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemabascat_catalogSpectralCoverage_httpeuclid_esa_orgschemabascatFilter', True)

    
    Filter = property(__Filter.value, __Filter.set, None, None)


    _ElementMap = {
        __SpectrumRange.name() : __SpectrumRange,
        __Filter.name() : __Filter
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogSpectralCoverage', catalogSpectralCoverage)


# Complex type distanceRange with content type ELEMENT_ONLY
class distanceRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'distanceRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemabascat_distanceRange_httpeuclid_esa_orgschemabascatUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}MinDistance uses Python identifier MinDistance
    __MinDistance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinDistance'), 'MinDistance', '__httpeuclid_esa_orgschemabascat_distanceRange_httpeuclid_esa_orgschemabascatMinDistance', False)

    
    MinDistance = property(__MinDistance.value, __MinDistance.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}MaxDistance uses Python identifier MaxDistance
    __MaxDistance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxDistance'), 'MaxDistance', '__httpeuclid_esa_orgschemabascat_distanceRange_httpeuclid_esa_orgschemabascatMaxDistance', False)

    
    MaxDistance = property(__MaxDistance.value, __MaxDistance.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __MinDistance.name() : __MinDistance,
        __MaxDistance.name() : __MaxDistance
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'distanceRange', distanceRange)


# Complex type catalogMetadata with content type ELEMENT_ONLY
class catalogMetadata (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogMetadata')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}RestParameters uses Python identifier RestParameters
    __RestParameters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RestParameters'), 'RestParameters', '__httpeuclid_esa_orgschemabascat_catalogMetadata_httpeuclid_esa_orgschemabascatRestParameters', False)

    
    RestParameters = property(__RestParameters.value, __RestParameters.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}ProcessingParameters uses Python identifier ProcessingParameters
    __ProcessingParameters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessingParameters'), 'ProcessingParameters', '__httpeuclid_esa_orgschemabascat_catalogMetadata_httpeuclid_esa_orgschemabascatProcessingParameters', False)

    
    ProcessingParameters = property(__ProcessingParameters.value, __ProcessingParameters.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}AstrometricParameters uses Python identifier AstrometricParameters
    __AstrometricParameters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AstrometricParameters'), 'AstrometricParameters', '__httpeuclid_esa_orgschemabascat_catalogMetadata_httpeuclid_esa_orgschemabascatAstrometricParameters', False)

    
    AstrometricParameters = property(__AstrometricParameters.value, __AstrometricParameters.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}QualityParameters uses Python identifier QualityParameters
    __QualityParameters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'QualityParameters'), 'QualityParameters', '__httpeuclid_esa_orgschemabascat_catalogMetadata_httpeuclid_esa_orgschemabascatQualityParameters', False)

    
    QualityParameters = property(__QualityParameters.value, __QualityParameters.set, None, None)


    _ElementMap = {
        __RestParameters.name() : __RestParameters,
        __ProcessingParameters.name() : __ProcessingParameters,
        __AstrometricParameters.name() : __AstrometricParameters,
        __QualityParameters.name() : __QualityParameters
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogMetadata', catalogMetadata)


# Complex type boundingBox with content type ELEMENT_ONLY
class boundingBox (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'boundingBox')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}luRA uses Python identifier luRA
    __luRA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'luRA'), 'luRA', '__httpeuclid_esa_orgschemabascat_boundingBox_httpeuclid_esa_orgschemabascatluRA', False)

    
    luRA = property(__luRA.value, __luRA.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}rlDEC uses Python identifier rlDEC
    __rlDEC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rlDEC'), 'rlDEC', '__httpeuclid_esa_orgschemabascat_boundingBox_httpeuclid_esa_orgschemabascatrlDEC', False)

    
    rlDEC = property(__rlDEC.value, __rlDEC.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}ruDEC uses Python identifier ruDEC
    __ruDEC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ruDEC'), 'ruDEC', '__httpeuclid_esa_orgschemabascat_boundingBox_httpeuclid_esa_orgschemabascatruDEC', False)

    
    ruDEC = property(__ruDEC.value, __ruDEC.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}luDEC uses Python identifier luDEC
    __luDEC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'luDEC'), 'luDEC', '__httpeuclid_esa_orgschemabascat_boundingBox_httpeuclid_esa_orgschemabascatluDEC', False)

    
    luDEC = property(__luDEC.value, __luDEC.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}llRA uses Python identifier llRA
    __llRA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'llRA'), 'llRA', '__httpeuclid_esa_orgschemabascat_boundingBox_httpeuclid_esa_orgschemabascatllRA', False)

    
    llRA = property(__llRA.value, __llRA.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}rlRA uses Python identifier rlRA
    __rlRA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rlRA'), 'rlRA', '__httpeuclid_esa_orgschemabascat_boundingBox_httpeuclid_esa_orgschemabascatrlRA', False)

    
    rlRA = property(__rlRA.value, __rlRA.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemabascat_boundingBox_httpeuclid_esa_orgschemabascatUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}llDEC uses Python identifier llDEC
    __llDEC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'llDEC'), 'llDEC', '__httpeuclid_esa_orgschemabascat_boundingBox_httpeuclid_esa_orgschemabascatllDEC', False)

    
    llDEC = property(__llDEC.value, __llDEC.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}ruRA uses Python identifier ruRA
    __ruRA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ruRA'), 'ruRA', '__httpeuclid_esa_orgschemabascat_boundingBox_httpeuclid_esa_orgschemabascatruRA', False)

    
    ruRA = property(__ruRA.value, __ruRA.set, None, None)


    _ElementMap = {
        __luRA.name() : __luRA,
        __rlDEC.name() : __rlDEC,
        __ruDEC.name() : __ruDEC,
        __luDEC.name() : __luDEC,
        __llRA.name() : __llRA,
        __rlRA.name() : __rlRA,
        __Unit.name() : __Unit,
        __llDEC.name() : __llDEC,
        __ruRA.name() : __ruRA
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'boundingBox', boundingBox)


# Complex type catalogSpatialCoverage with content type ELEMENT_ONLY
class catalogSpatialCoverage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogSpatialCoverage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}DistanceRange uses Python identifier DistanceRange
    __DistanceRange = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DistanceRange'), 'DistanceRange', '__httpeuclid_esa_orgschemabascat_catalogSpatialCoverage_httpeuclid_esa_orgschemabascatDistanceRange', False)

    
    DistanceRange = property(__DistanceRange.value, __DistanceRange.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'), 'BoundingBox', '__httpeuclid_esa_orgschemabascat_catalogSpatialCoverage_httpeuclid_esa_orgschemabascatBoundingBox', False)

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}HTMList uses Python identifier HTMList
    __HTMList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HTMList'), 'HTMList', '__httpeuclid_esa_orgschemabascat_catalogSpatialCoverage_httpeuclid_esa_orgschemabascatHTMList', False)

    
    HTMList = property(__HTMList.value, __HTMList.set, None, None)


    _ElementMap = {
        __DistanceRange.name() : __DistanceRange,
        __BoundingBox.name() : __BoundingBox,
        __HTMList.name() : __HTMList
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogSpatialCoverage', catalogSpatialCoverage)


# Complex type catalogFileStorage with content type ELEMENT_ONLY
class catalogFileStorage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogFileStorage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}CatalogMetadataStorage uses Python identifier CatalogMetadataStorage
    __CatalogMetadataStorage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CatalogMetadataStorage'), 'CatalogMetadataStorage', '__httpeuclid_esa_orgschemabascat_catalogFileStorage_httpeuclid_esa_orgschemabascatCatalogMetadataStorage', False)

    
    CatalogMetadataStorage = property(__CatalogMetadataStorage.value, __CatalogMetadataStorage.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}FileNumber uses Python identifier FileNumber
    __FileNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FileNumber'), 'FileNumber', '__httpeuclid_esa_orgschemabascat_catalogFileStorage_httpeuclid_esa_orgschemabascatFileNumber', False)

    
    FileNumber = property(__FileNumber.value, __FileNumber.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}FileFormat uses Python identifier FileFormat
    __FileFormat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FileFormat'), 'FileFormat', '__httpeuclid_esa_orgschemabascat_catalogFileStorage_httpeuclid_esa_orgschemabascatFileFormat', False)

    
    FileFormat = property(__FileFormat.value, __FileFormat.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemabascat_catalogFileStorage_httpeuclid_esa_orgschemabascatId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}StorageSpace uses Python identifier StorageSpace
    __StorageSpace = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StorageSpace'), 'StorageSpace', '__httpeuclid_esa_orgschemabascat_catalogFileStorage_httpeuclid_esa_orgschemabascatStorageSpace', True)

    
    StorageSpace = property(__StorageSpace.value, __StorageSpace.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}PartitioningColumn uses Python identifier PartitioningColumn
    __PartitioningColumn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PartitioningColumn'), 'PartitioningColumn', '__httpeuclid_esa_orgschemabascat_catalogFileStorage_httpeuclid_esa_orgschemabascatPartitioningColumn', False)

    
    PartitioningColumn = property(__PartitioningColumn.value, __PartitioningColumn.set, None, None)


    _ElementMap = {
        __CatalogMetadataStorage.name() : __CatalogMetadataStorage,
        __FileNumber.name() : __FileNumber,
        __FileFormat.name() : __FileFormat,
        __Id.name() : __Id,
        __StorageSpace.name() : __StorageSpace,
        __PartitioningColumn.name() : __PartitioningColumn
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogFileStorage', catalogFileStorage)


# Complex type catalogDBStorage with content type ELEMENT_ONLY
class catalogDBStorage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogDBStorage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}StorageDataType uses Python identifier StorageDataType
    __StorageDataType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StorageDataType'), 'StorageDataType', '__httpeuclid_esa_orgschemabascat_catalogDBStorage_httpeuclid_esa_orgschemabascatStorageDataType', False)

    
    StorageDataType = property(__StorageDataType.value, __StorageDataType.set, None, u'Definition of the catalog in Euclid CDM, for example, ext:sourceList')

    
    # Element {http://euclid.esa.org/schema/bas/cat}ConnectionString uses Python identifier ConnectionString
    __ConnectionString = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConnectionString'), 'ConnectionString', '__httpeuclid_esa_orgschemabascat_catalogDBStorage_httpeuclid_esa_orgschemabascatConnectionString', False)

    
    ConnectionString = property(__ConnectionString.value, __ConnectionString.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}IdType uses Python identifier IdType
    __IdType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdType'), 'IdType', '__httpeuclid_esa_orgschemabascat_catalogDBStorage_httpeuclid_esa_orgschemabascatIdType', False)

    
    IdType = property(__IdType.value, __IdType.set, None, u'The column  of the catalog which was used for catalog identification, for example, SLID of ext:sourceList')

    
    # Element {http://euclid.esa.org/schema/bas/cat}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemabascat_catalogDBStorage_httpeuclid_esa_orgschemabascatId', False)

    
    Id = property(__Id.value, __Id.set, None, u'Identification of the catalog object in OU-specific defintion of the catalog, for example, SLID of ext:sourceList')

    
    # Element {http://euclid.esa.org/schema/bas/cat}SelectionRange uses Python identifier SelectionRange
    __SelectionRange = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SelectionRange'), 'SelectionRange', '__httpeuclid_esa_orgschemabascat_catalogDBStorage_httpeuclid_esa_orgschemabascatSelectionRange', False)

    
    SelectionRange = property(__SelectionRange.value, __SelectionRange.set, None, u'The range of attributes or select statement which was used to select subset of objects from already existing catalog')

    
    # Element {http://euclid.esa.org/schema/bas/cat}IndexColumn uses Python identifier IndexColumn
    __IndexColumn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IndexColumn'), 'IndexColumn', '__httpeuclid_esa_orgschemabascat_catalogDBStorage_httpeuclid_esa_orgschemabascatIndexColumn', False)

    
    IndexColumn = property(__IndexColumn.value, __IndexColumn.set, None, u'The column  of the catalog which was used for the subselection if the catalog is subset of already existing catalog, for example, HTM of ext:sourceList')


    _ElementMap = {
        __StorageDataType.name() : __StorageDataType,
        __ConnectionString.name() : __ConnectionString,
        __IdType.name() : __IdType,
        __Id.name() : __Id,
        __SelectionRange.name() : __SelectionRange,
        __IndexColumn.name() : __IndexColumn
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogDBStorage', catalogDBStorage)


# Complex type catalogMetadataStorageElement with content type ELEMENT_ONLY
class catalogMetadataStorageElement (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogMetadataStorageElement')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemabascat_catalogMetadataStorageElement_httpeuclid_esa_orgschemabascatValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Key uses Python identifier Key
    __Key = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Key'), 'Key', '__httpeuclid_esa_orgschemabascat_catalogMetadataStorageElement_httpeuclid_esa_orgschemabascatKey', False)

    
    Key = property(__Key.value, __Key.set, None, u'Key corresponds to Name of catalogProperty from catalogMetatada list of columns for the catalog')


    _ElementMap = {
        __Value.name() : __Value,
        __Key.name() : __Key
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogMetadataStorageElement', catalogMetadataStorageElement)


# Complex type catalogMetadataStorage with content type ELEMENT_ONLY
class catalogMetadataStorage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogMetadataStorage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}CatalogMetadataElement uses Python identifier CatalogMetadataElement
    __CatalogMetadataElement = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CatalogMetadataElement'), 'CatalogMetadataElement', '__httpeuclid_esa_orgschemabascat_catalogMetadataStorage_httpeuclid_esa_orgschemabascatCatalogMetadataElement', True)

    
    CatalogMetadataElement = property(__CatalogMetadataElement.value, __CatalogMetadataElement.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemabascat_catalogMetadataStorage_httpeuclid_esa_orgschemabascatId', False)

    
    Id = property(__Id.value, __Id.set, None, None)


    _ElementMap = {
        __CatalogMetadataElement.name() : __CatalogMetadataElement,
        __Id.name() : __Id
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogMetadataStorage', catalogMetadataStorage)


# Complex type catalogID with content type ELEMENT_ONLY
class catalogID (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogID')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ID'), 'ID', '__httpeuclid_esa_orgschemabascat_catalogID_httpeuclid_esa_orgschemabascatID', False)

    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}NRecords uses Python identifier NRecords
    __NRecords = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NRecords'), 'NRecords', '__httpeuclid_esa_orgschemabascat_catalogID_httpeuclid_esa_orgschemabascatNRecords', False)

    
    NRecords = property(__NRecords.value, __NRecords.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemabascat_catalogID_httpeuclid_esa_orgschemabascatVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpeuclid_esa_orgschemabascat_catalogID_httpeuclid_esa_orgschemabascatDescription', False)

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Keywords uses Python identifier Keywords
    __Keywords = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Keywords'), 'Keywords', '__httpeuclid_esa_orgschemabascat_catalogID_httpeuclid_esa_orgschemabascatKeywords', False)

    
    Keywords = property(__Keywords.value, __Keywords.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemabascat_catalogID_httpeuclid_esa_orgschemabascatName', False)

    
    Name = property(__Name.value, __Name.set, None, None)


    _ElementMap = {
        __ID.name() : __ID,
        __NRecords.name() : __NRecords,
        __Version.name() : __Version,
        __Description.name() : __Description,
        __Keywords.name() : __Keywords,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogID', catalogID)


# Complex type sourceMetadata with content type ELEMENT_ONLY
class sourceMetadata (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceMetadata')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}Column uses Python identifier Column
    __Column = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Column'), 'Column', '__httpeuclid_esa_orgschemabascat_sourceMetadata_httpeuclid_esa_orgschemabascatColumn', True)

    
    Column = property(__Column.value, __Column.set, None, None)


    _ElementMap = {
        __Column.name() : __Column
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sourceMetadata', sourceMetadata)


# Complex type catalogStorage with content type ELEMENT_ONLY
class catalogStorage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogStorage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cat}CatalogDBStorage uses Python identifier CatalogDBStorage
    __CatalogDBStorage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CatalogDBStorage'), 'CatalogDBStorage', '__httpeuclid_esa_orgschemabascat_catalogStorage_httpeuclid_esa_orgschemabascatCatalogDBStorage', False)

    
    CatalogDBStorage = property(__CatalogDBStorage.value, __CatalogDBStorage.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cat}CatalogFileStorage uses Python identifier CatalogFileStorage
    __CatalogFileStorage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CatalogFileStorage'), 'CatalogFileStorage', '__httpeuclid_esa_orgschemabascat_catalogStorage_httpeuclid_esa_orgschemabascatCatalogFileStorage', False)

    
    CatalogFileStorage = property(__CatalogFileStorage.value, __CatalogFileStorage.set, None, None)


    _ElementMap = {
        __CatalogDBStorage.name() : __CatalogDBStorage,
        __CatalogFileStorage.name() : __CatalogFileStorage
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogStorage', catalogStorage)




catalogCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpectralCoverage'), catalogSpectralCoverage, scope=catalogCoverage))

catalogCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpatialCoverage'), catalogSpatialCoverage, scope=catalogCoverage))
catalogCoverage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogCoverage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpatialCoverage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogCoverage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpectralCoverage')), min_occurs=1, max_occurs=1)
    )
catalogCoverage._ContentModel = pyxb.binding.content.ParticleModel(catalogCoverage._GroupModel, min_occurs=1, max_occurs=1)



catalogContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogMetadata'), catalogMetadata, scope=catalogContainer))

catalogContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GenericHeader'), CommonDM.dm.sys_stub.genericHeader, scope=catalogContainer))

catalogContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceMetadata'), sourceMetadata, scope=catalogContainer))

catalogContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogStorage'), catalogStorage, scope=catalogContainer))

catalogContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogID'), catalogID, scope=catalogContainer))

catalogContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogCoverage'), catalogCoverage, scope=catalogContainer))
catalogContainer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GenericHeader')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogCoverage')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogMetadata')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceMetadata')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogStorage')), min_occurs=1, max_occurs=1)
    )
catalogContainer._ContentModel = pyxb.binding.content.ParticleModel(catalogContainer._GroupModel, min_occurs=1, max_occurs=1)



catalogPropertyList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PropertyList'), catalogProperty, scope=catalogPropertyList))
catalogPropertyList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogPropertyList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PropertyList')), min_occurs=1L, max_occurs=None)
    )
catalogPropertyList._ContentModel = pyxb.binding.content.ParticleModel(catalogPropertyList._GroupModel, min_occurs=1, max_occurs=1)



catalogProperty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Label'), pyxb.binding.datatypes.string, scope=catalogProperty))

catalogProperty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), pyxb.binding.datatypes.string, scope=catalogProperty))

catalogProperty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Type'), pyxb.binding.datatypes.string, scope=catalogProperty))

catalogProperty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UCD'), catalogUCDRecord, scope=catalogProperty))

catalogProperty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NullValue'), pyxb.binding.datatypes.string, scope=catalogProperty))

catalogProperty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'utype'), pyxb.binding.datatypes.string, scope=catalogProperty))

catalogProperty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=catalogProperty))

catalogProperty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=catalogProperty))
catalogProperty._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogProperty._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogProperty._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Label')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogProperty._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Type')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogProperty._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NullValue')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogProperty._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogProperty._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogProperty._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UCD')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogProperty._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'utype')), min_occurs=0L, max_occurs=1)
    )
catalogProperty._ContentModel = pyxb.binding.content.ParticleModel(catalogProperty._GroupModel, min_occurs=1, max_occurs=1)



partitioningRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SelectionFilter'), pyxb.binding.datatypes.string, scope=partitioningRange))

partitioningRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxValue'), pyxb.binding.datatypes.string, scope=partitioningRange))

partitioningRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinValue'), pyxb.binding.datatypes.string, scope=partitioningRange))
partitioningRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(partitioningRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinValue')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(partitioningRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxValue')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(partitioningRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SelectionFilter')), min_occurs=0L, max_occurs=1)
    )
partitioningRange._ContentModel = pyxb.binding.content.ParticleModel(partitioningRange._GroupModel, min_occurs=1, max_occurs=1)



catalogPartitionStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataContainer'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=catalogPartitionStorage))

catalogPartitionStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Range'), partitioningRange, scope=catalogPartitionStorage))

catalogPartitionStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=catalogPartitionStorage))
catalogPartitionStorage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogPartitionStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogPartitionStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Range')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogPartitionStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
catalogPartitionStorage._ContentModel = pyxb.binding.content.ParticleModel(catalogPartitionStorage._GroupModel, min_occurs=1, max_occurs=1)



catalogSpectralCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpectrumRange'), CommonDM.dm.ins.nis_stub.spectrumRange, scope=catalogSpectralCoverage))

catalogSpectralCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=catalogSpectralCoverage))
catalogSpectralCoverage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogSpectralCoverage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(catalogSpectralCoverage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpectrumRange')), min_occurs=0L, max_occurs=None)
    )
catalogSpectralCoverage._ContentModel = pyxb.binding.content.ParticleModel(catalogSpectralCoverage._GroupModel, min_occurs=1, max_occurs=1)



distanceRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=distanceRange))

distanceRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinDistance'), pyxb.binding.datatypes.double, scope=distanceRange))

distanceRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxDistance'), pyxb.binding.datatypes.double, scope=distanceRange))
distanceRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(distanceRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinDistance')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(distanceRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxDistance')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(distanceRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
distanceRange._ContentModel = pyxb.binding.content.ParticleModel(distanceRange._GroupModel, min_occurs=1, max_occurs=1)



catalogMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RestParameters'), catalogPropertyList, scope=catalogMetadata))

catalogMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessingParameters'), catalogPropertyList, scope=catalogMetadata))

catalogMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AstrometricParameters'), catalogPropertyList, scope=catalogMetadata))

catalogMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QualityParameters'), catalogPropertyList, scope=catalogMetadata))
catalogMetadata._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessingParameters')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QualityParameters')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AstrometricParameters')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RestParameters')), min_occurs=0L, max_occurs=1)
    )
catalogMetadata._ContentModel = pyxb.binding.content.ParticleModel(catalogMetadata._GroupModel, min_occurs=1, max_occurs=1)



boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'luRA'), pyxb.binding.datatypes.double, scope=boundingBox))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rlDEC'), pyxb.binding.datatypes.double, scope=boundingBox))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ruDEC'), pyxb.binding.datatypes.double, scope=boundingBox))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'luDEC'), pyxb.binding.datatypes.double, scope=boundingBox))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'llRA'), pyxb.binding.datatypes.double, scope=boundingBox))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rlRA'), pyxb.binding.datatypes.double, scope=boundingBox))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=boundingBox))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'llDEC'), pyxb.binding.datatypes.double, scope=boundingBox))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ruRA'), pyxb.binding.datatypes.double, scope=boundingBox))
boundingBox._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'luRA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'luDEC')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'llRA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'llDEC')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ruRA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ruDEC')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rlRA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rlDEC')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
boundingBox._ContentModel = pyxb.binding.content.ParticleModel(boundingBox._GroupModel, min_occurs=1, max_occurs=1)



catalogSpatialCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DistanceRange'), distanceRange, scope=catalogSpatialCoverage))

catalogSpatialCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'), boundingBox, scope=catalogSpatialCoverage))

catalogSpatialCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HTMList'), CommonDM.dm.bas.dtd_stub.listOfInteger8, scope=catalogSpatialCoverage))
catalogSpatialCoverage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogSpatialCoverage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogSpatialCoverage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HTMList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogSpatialCoverage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DistanceRange')), min_occurs=0L, max_occurs=1)
    )
catalogSpatialCoverage._ContentModel = pyxb.binding.content.ParticleModel(catalogSpatialCoverage._GroupModel, min_occurs=1, max_occurs=1)



catalogFileStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogMetadataStorage'), catalogMetadataStorage, scope=catalogFileStorage))

catalogFileStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileNumber'), pyxb.binding.datatypes.int, scope=catalogFileStorage))

catalogFileStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileFormat'), catalogFileFormat, scope=catalogFileStorage))

catalogFileStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=catalogFileStorage))

catalogFileStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StorageSpace'), catalogPartitionStorage, scope=catalogFileStorage))

catalogFileStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PartitioningColumn'), catalogProperty, scope=catalogFileStorage))
catalogFileStorage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogFileStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogFileStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PartitioningColumn')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogFileStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogMetadataStorage')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogFileStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileFormat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogFileStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogFileStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StorageSpace')), min_occurs=1L, max_occurs=None)
    )
catalogFileStorage._ContentModel = pyxb.binding.content.ParticleModel(catalogFileStorage._GroupModel, min_occurs=1, max_occurs=1)



catalogDBStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StorageDataType'), pyxb.binding.datatypes.string, scope=catalogDBStorage, documentation=u'Definition of the catalog in Euclid CDM, for example, ext:sourceList'))

catalogDBStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConnectionString'), pyxb.binding.datatypes.string, scope=catalogDBStorage))

catalogDBStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdType'), catalogProperty, scope=catalogDBStorage, documentation=u'The column  of the catalog which was used for catalog identification, for example, SLID of ext:sourceList'))

catalogDBStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=catalogDBStorage, documentation=u'Identification of the catalog object in OU-specific defintion of the catalog, for example, SLID of ext:sourceList'))

catalogDBStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SelectionRange'), partitioningRange, scope=catalogDBStorage, documentation=u'The range of attributes or select statement which was used to select subset of objects from already existing catalog'))

catalogDBStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndexColumn'), catalogProperty, scope=catalogDBStorage, documentation=u'The column  of the catalog which was used for the subselection if the catalog is subset of already existing catalog, for example, HTM of ext:sourceList'))
catalogDBStorage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogDBStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogDBStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogDBStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConnectionString')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogDBStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StorageDataType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogDBStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndexColumn')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogDBStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SelectionRange')), min_occurs=0L, max_occurs=1)
    )
catalogDBStorage._ContentModel = pyxb.binding.content.ParticleModel(catalogDBStorage._GroupModel, min_occurs=1, max_occurs=1)



catalogMetadataStorageElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.string, scope=catalogMetadataStorageElement))

catalogMetadataStorageElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Key'), pyxb.binding.datatypes.string, scope=catalogMetadataStorageElement, documentation=u'Key corresponds to Name of catalogProperty from catalogMetatada list of columns for the catalog'))
catalogMetadataStorageElement._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogMetadataStorageElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Key')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogMetadataStorageElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1)
    )
catalogMetadataStorageElement._ContentModel = pyxb.binding.content.ParticleModel(catalogMetadataStorageElement._GroupModel, min_occurs=1, max_occurs=1)



catalogMetadataStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogMetadataElement'), catalogMetadataStorageElement, scope=catalogMetadataStorage))

catalogMetadataStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.int, scope=catalogMetadataStorage))
catalogMetadataStorage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogMetadataStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogMetadataStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogMetadataElement')), min_occurs=1L, max_occurs=None)
    )
catalogMetadataStorage._ContentModel = pyxb.binding.content.ParticleModel(catalogMetadataStorage._GroupModel, min_occurs=1, max_occurs=1)



catalogID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ID'), pyxb.binding.datatypes.integer, scope=catalogID))

catalogID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NRecords'), pyxb.binding.datatypes.integer, scope=catalogID))

catalogID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), pyxb.binding.datatypes.string, scope=catalogID))

catalogID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), pyxb.binding.datatypes.string, scope=catalogID))

catalogID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Keywords'), pyxb.binding.datatypes.string, scope=catalogID))

catalogID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=catalogID))
catalogID._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogID._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogID._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogID._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogID._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogID._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keywords')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogID._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NRecords')), min_occurs=1, max_occurs=1)
    )
catalogID._ContentModel = pyxb.binding.content.ParticleModel(catalogID._GroupModel, min_occurs=1, max_occurs=1)



sourceMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Column'), catalogProperty, scope=sourceMetadata))
sourceMetadata._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sourceMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Column')), min_occurs=1L, max_occurs=None)
    )
sourceMetadata._ContentModel = pyxb.binding.content.ParticleModel(sourceMetadata._GroupModel, min_occurs=1, max_occurs=1)



catalogStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogDBStorage'), catalogDBStorage, scope=catalogStorage))

catalogStorage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogFileStorage'), catalogFileStorage, scope=catalogStorage))
catalogStorage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogFileStorage')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogStorage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogDBStorage')), min_occurs=0L, max_occurs=1)
    )
catalogStorage._ContentModel = pyxb.binding.content.ParticleModel(catalogStorage._GroupModel, min_occurs=1, max_occurs=1)
