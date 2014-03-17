# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/bas/img_stub.py
# PyXB bindings for NamespaceModule
# NSM:2b04cf6feb6fd3bb861db96b6787e5a2f0416c17
# Generated 2014-03-17 18:50:36.640490 by PyXB version 1.1.2
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
import CommonDM.dm.sys.sgs_stub
import CommonDM.dm.bas_stub
import CommonDM.dm.bas.dtd_stub
import CommonDM.dm.bas.cot_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img', create_if_missing=True)
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


# Complex type obsBlock with content type ELEMENT_ONLY
class obsBlock (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'obsBlock')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/img}Group uses Python identifier Group
    __Group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Group'), 'Group', '__httpeuclid_esa_orgschemabasimg_obsBlock_httpeuclid_esa_orgschemabasimgGroup', False)

    
    Group = property(__Group.value, __Group.set, None, u' Group identifier for linked observational\n                        blocks [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}ProgramId uses Python identifier ProgramId
    __ProgramId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProgramId'), 'ProgramId', '__httpeuclid_esa_orgschemabasimg_obsBlock_httpeuclid_esa_orgschemabasimgProgramId', False)

    
    ProgramId = property(__ProgramId.value, __ProgramId.set, None, u' Observational program identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemabasimg_obsBlock_httpeuclid_esa_orgschemabasimgId', False)

    
    Id = property(__Id.value, __Id.set, None, u' Identifier of the observational block\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}DictionaryId uses Python identifier DictionaryId
    __DictionaryId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DictionaryId'), 'DictionaryId', '__httpeuclid_esa_orgschemabasimg_obsBlock_httpeuclid_esa_orgschemabasimgDictionaryId', False)

    
    DictionaryId = property(__DictionaryId.value, __DictionaryId.set, None, u' Identifier of the observational\n                        dictionary defining the type of observation [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}PI uses Python identifier PI
    __PI = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PI'), 'PI', '__httpeuclid_esa_orgschemabasimg_obsBlock_httpeuclid_esa_orgschemabasimgPI', False)

    
    PI = property(__PI.value, __PI.set, None, u' Information about the investigator(s)\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimg_obsBlock_httpeuclid_esa_orgschemabasimgName', False)

    
    Name = property(__Name.value, __Name.set, None, u' Name of the observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemabasimg_obsBlock_httpeuclid_esa_orgschemabasimgExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Start uses Python identifier Start
    __Start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Start'), 'Start', '__httpeuclid_esa_orgschemabasimg_obsBlock_httpeuclid_esa_orgschemabasimgStart', False)

    
    Start = property(__Start.value, __Start.set, None, u' UTC date the observational block was\n                        started [None] ')


    _ElementMap = {
        __Group.name() : __Group,
        __ProgramId.name() : __ProgramId,
        __Id.name() : __Id,
        __DictionaryId.name() : __DictionaryId,
        __PI.name() : __PI,
        __Name.name() : __Name,
        __ExtObjectId.name() : __ExtObjectId,
        __Start.name() : __Start
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'obsBlock', obsBlock)


# Complex type template with content type ELEMENT_ONLY
class template (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'template')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/img}DictionaryId uses Python identifier DictionaryId
    __DictionaryId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DictionaryId'), 'DictionaryId', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgDictionaryId', False)

    
    DictionaryId = property(__DictionaryId.value, __DictionaryId.set, None, u' Identifier of the observational\n                        dictionary defining the type of observation [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgName', False)

    
    Name = property(__Name.value, __Name.set, None, u' Name of the observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the observational\n                        filter [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Sequencer uses Python identifier Sequencer
    __Sequencer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sequencer'), 'Sequencer', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgSequencer', False)

    
    Sequencer = property(__Sequencer.value, __Sequencer.set, None, u' Observational sequencer script [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgId', False)

    
    Id = property(__Id.value, __Id.set, None, u' Identifier of the observational template\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Type'), 'Type', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgType', False)

    
    Type = property(__Type.value, __Type.set, None, u' Observational template type [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Start uses Python identifier Start
    __Start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Start'), 'Start', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgStart', False)

    
    Start = property(__Start.value, __Start.set, None, u' UTC date the observational template was\n                        started [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Technique uses Python identifier Technique
    __Technique = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Technique'), 'Technique', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgTechnique', False)

    
    Technique = property(__Technique.value, __Technique.set, None, u' Observational template technique [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Exposures uses Python identifier Exposures
    __Exposures = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Exposures'), 'Exposures', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgExposures', False)

    
    Exposures = property(__Exposures.value, __Exposures.set, None, u' Number of exposures within the\n                        observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}ObsId uses Python identifier ObsId
    __ObsId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsId'), 'ObsId', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgObsId', False)

    
    ObsId = property(__ObsId.value, __ObsId.set, None, u' Identifier of the associated\n                        observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgVersion', False)

    
    Version = property(__Version.value, __Version.set, None, u' Version of the observational template\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}ObsStart uses Python identifier ObsStart
    __ObsStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsStart'), 'ObsStart', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgObsStart', False)

    
    ObsStart = property(__ObsStart.value, __ObsStart.set, None, u' UTC date the associated observational\n                        block was started [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Category uses Python identifier Category
    __Category = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Category'), 'Category', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgCategory', False)

    
    Category = property(__Category.value, __Category.set, None, u' Observational template category [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Index uses Python identifier Index
    __Index = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Index'), 'Index', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgIndex', False)

    
    Index = property(__Index.value, __Index.set, None, u' Observational template index within the\n                        associated observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Strategy uses Python identifier Strategy
    __Strategy = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Strategy'), 'Strategy', '__httpeuclid_esa_orgschemabasimg_template_httpeuclid_esa_orgschemabasimgStrategy', False)

    
    Strategy = property(__Strategy.value, __Strategy.set, None, u' Observational template strategy [None] ')


    _ElementMap = {
        __DictionaryId.name() : __DictionaryId,
        __Name.name() : __Name,
        __Filter.name() : __Filter,
        __Sequencer.name() : __Sequencer,
        __Id.name() : __Id,
        __Type.name() : __Type,
        __Start.name() : __Start,
        __Technique.name() : __Technique,
        __Exposures.name() : __Exposures,
        __ExtObjectId.name() : __ExtObjectId,
        __ObsId.name() : __ObsId,
        __Version.name() : __Version,
        __ObsStart.name() : __ObsStart,
        __Category.name() : __Category,
        __Index.name() : __Index,
        __Strategy.name() : __Strategy
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'template', template)


# Complex type filter with content type ELEMENT_ONLY
class filter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'filter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/img}HasFringes uses Python identifier HasFringes
    __HasFringes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HasFringes'), 'HasFringes', '__httpeuclid_esa_orgschemabasimg_filter_httpeuclid_esa_orgschemabasimgHasFringes', False)

    
    HasFringes = property(__HasFringes.value, __HasFringes.set, None, u' Indicates if data in this photometric\n                        band may contain fringes [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemabasimg_filter_httpeuclid_esa_orgschemabasimgExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}MagId uses Python identifier MagId
    __MagId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagId'), 'MagId', '__httpeuclid_esa_orgschemabasimg_filter_httpeuclid_esa_orgschemabasimgMagId', False)

    
    MagId = property(__MagId.value, __MagId.set, None, u' Identifier of the photometric band [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}CentralWavelength uses Python identifier CentralWavelength
    __CentralWavelength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CentralWavelength'), 'CentralWavelength', '__httpeuclid_esa_orgschemabasimg_filter_httpeuclid_esa_orgschemabasimgCentralWavelength', False)

    
    CentralWavelength = property(__CentralWavelength.value, __CentralWavelength.set, None, u' Center wavelength of the photometric band\n                        [angstrom] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimg_filter_httpeuclid_esa_orgschemabasimgName', False)

    
    Name = property(__Name.value, __Name.set, None, u' Name of the observational filter [None] ')


    _ElementMap = {
        __HasFringes.name() : __HasFringes,
        __ExtObjectId.name() : __ExtObjectId,
        __MagId.name() : __MagId,
        __CentralWavelength.name() : __CentralWavelength,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'filter', filter)


# Complex type chip with content type ELEMENT_ONLY
class chip (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'chip')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/img}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimg_chip_httpeuclid_esa_orgschemabasimgName', False)

    
    Name = property(__Name.value, __Name.set, None, u' Name of the chip [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemabasimg_chip_httpeuclid_esa_orgschemabasimgExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __Name.name() : __Name,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'chip', chip)


# Complex type processTarget with content type ELEMENT_ONLY
class processTarget (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'processTarget')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/img}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemabasimg_processTarget_httpeuclid_esa_orgschemabasimgExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}QualityFlags uses Python identifier QualityFlags
    __QualityFlags = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'QualityFlags'), 'QualityFlags', '__httpeuclid_esa_orgschemabasimg_processTarget_httpeuclid_esa_orgschemabasimgQualityFlags', False)

    
    QualityFlags = property(__QualityFlags.value, __QualityFlags.set, None, u' Automatic/internal quality flag [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}IsValid uses Python identifier IsValid
    __IsValid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IsValid'), 'IsValid', '__httpeuclid_esa_orgschemabasimg_processTarget_httpeuclid_esa_orgschemabasimgIsValid', False)

    
    IsValid = property(__IsValid.value, __IsValid.set, None, u' Manual/external flag to disqualify bad\n                        data (SuperFlag) [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), 'CreationDate', '__httpeuclid_esa_orgschemabasimg_processTarget_httpeuclid_esa_orgschemabasimgCreationDate', False)

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, u' UTC date this object was created [None] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __QualityFlags.name() : __QualityFlags,
        __IsValid.name() : __IsValid,
        __CreationDate.name() : __CreationDate
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'processTarget', processTarget)


# Complex type processTargetDataObject with content type ELEMENT_ONLY
class processTargetDataObject (processTarget):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'processTargetDataObject')
    # Base type is processTarget
    
    # Element {http://euclid.esa.org/schema/bas/img}Storage uses Python identifier Storage
    __Storage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Storage'), 'Storage', '__httpeuclid_esa_orgschemabasimg_processTargetDataObject_httpeuclid_esa_orgschemabasimgStorage', False)

    
    Storage = property(__Storage.value, __Storage.set, None, u' Customized storage container for\n                                the data [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = processTarget._ElementMap.copy()
    _ElementMap.update({
        __Storage.name() : __Storage
    })
    _AttributeMap = processTarget._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'processTargetDataObject', processTargetDataObject)


# Complex type baseFrame with content type ELEMENT_ONLY
class baseFrame (processTargetDataObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseFrame')
    # Base type is processTargetDataObject
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/bas/img}Naxis2 uses Python identifier Naxis2
    __Naxis2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Naxis2'), 'Naxis2', '__httpeuclid_esa_orgschemabasimg_baseFrame_httpeuclid_esa_orgschemabasimgNaxis2', False)

    
    Naxis2 = property(__Naxis2.value, __Naxis2.set, None, u' Length of data in axis 2 [pixel] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/bas/img}ImStat uses Python identifier ImStat
    __ImStat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImStat'), 'ImStat', '__httpeuclid_esa_orgschemabasimg_baseFrame_httpeuclid_esa_orgschemabasimgImStat', False)

    
    ImStat = property(__ImStat.value, __ImStat.set, None, u' Information about the statistics\n                                of the image pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Naxis1 uses Python identifier Naxis1
    __Naxis1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Naxis1'), 'Naxis1', '__httpeuclid_esa_orgschemabasimg_baseFrame_httpeuclid_esa_orgschemabasimgNaxis1', False)

    
    Naxis1 = property(__Naxis1.value, __Naxis1.set, None, u' Length of data in axis 1 [pixel] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/bas/img}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemabasimg_baseFrame_httpeuclid_esa_orgschemabasimgInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = processTargetDataObject._ElementMap.copy()
    _ElementMap.update({
        __Naxis2.name() : __Naxis2,
        __ImStat.name() : __ImStat,
        __Naxis1.name() : __Naxis1,
        __Instrument.name() : __Instrument
    })
    _AttributeMap = processTargetDataObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'baseFrame', baseFrame)


# Complex type instrument with content type ELEMENT_ONLY
class instrument (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'instrument')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/img}Longtitude uses Python identifier Longtitude
    __Longtitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Longtitude'), 'Longtitude', '__httpeuclid_esa_orgschemabasimg_instrument_httpeuclid_esa_orgschemabasimgLongtitude', False)

    
    Longtitude = property(__Longtitude.value, __Longtitude.set, None, u' Geographic longitude of a ground-based\n                        instrument [degree] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Timezone uses Python identifier Timezone
    __Timezone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Timezone'), 'Timezone', '__httpeuclid_esa_orgschemabasimg_instrument_httpeuclid_esa_orgschemabasimgTimezone', False)

    
    Timezone = property(__Timezone.value, __Timezone.set, None, u' Timezone of a ground-based instrument\n                        [hour] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimg_instrument_httpeuclid_esa_orgschemabasimgName', False)

    
    Name = property(__Name.value, __Name.set, None, u' Name of the instrument\n                        [None]')

    
    # Element {http://euclid.esa.org/schema/bas/img}Latitude uses Python identifier Latitude
    __Latitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Latitude'), 'Latitude', '__httpeuclid_esa_orgschemabasimg_instrument_httpeuclid_esa_orgschemabasimgLatitude', False)

    
    Latitude = property(__Latitude.value, __Latitude.set, None, u' Geographic latitude of a ground-based\n                        instrument [degree] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}TelescopeName uses Python identifier TelescopeName
    __TelescopeName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TelescopeName'), 'TelescopeName', '__httpeuclid_esa_orgschemabasimg_instrument_httpeuclid_esa_orgschemabasimgTelescopeName', False)

    
    TelescopeName = property(__TelescopeName.value, __TelescopeName.set, None, u' Name of the telescope the instrument is\n                        mounted on [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Elevation uses Python identifier Elevation
    __Elevation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Elevation'), 'Elevation', '__httpeuclid_esa_orgschemabasimg_instrument_httpeuclid_esa_orgschemabasimgElevation', False)

    
    Elevation = property(__Elevation.value, __Elevation.set, None, u' Geographic elevation of a ground-based\n                        instrument [meter] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemabasimg_instrument_httpeuclid_esa_orgschemabasimgExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __Longtitude.name() : __Longtitude,
        __Timezone.name() : __Timezone,
        __Name.name() : __Name,
        __Latitude.name() : __Latitude,
        __TelescopeName.name() : __TelescopeName,
        __Elevation.name() : __Elevation,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'instrument', instrument)


# Complex type imStats with content type ELEMENT_ONLY
class imStats (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'imStats')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/img}XUpper uses Python identifier XUpper
    __XUpper = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XUpper'), 'XUpper', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgXUpper', False)

    
    XUpper = property(__XUpper.value, __XUpper.set, None, u' X position of upper right corner of the\n                        statistics region [pixel] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}MaxX uses Python identifier MaxX
    __MaxX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxX'), 'MaxX', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgMaxX', False)

    
    MaxX = property(__MaxX.value, __MaxX.set, None, u' X position of maximum value [pixel] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Median uses Python identifier Median
    __Median = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Median'), 'Median', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgMedian', False)

    
    Median = property(__Median.value, __Median.set, None, u' Median value of the data [count] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Mean uses Python identifier Mean
    __Mean = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Mean'), 'Mean', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgMean', False)

    
    Mean = property(__Mean.value, __Mean.set, None, u' Mean value of the data [count] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}YUpper uses Python identifier YUpper
    __YUpper = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YUpper'), 'YUpper', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgYUpper', False)

    
    YUpper = property(__YUpper.value, __YUpper.set, None, u' Y position of upper right corner of the\n                        statistics region [pixel] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}MinX uses Python identifier MinX
    __MinX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinX'), 'MinX', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgMinX', False)

    
    MinX = property(__MinX.value, __MinX.set, None, u' X position of minimum value [pixel] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}MaxY uses Python identifier MaxY
    __MaxY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxY'), 'MaxY', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgMaxY', False)

    
    MaxY = property(__MaxY.value, __MaxY.set, None, u' Y position of maximum value [pixel] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Min uses Python identifier Min
    __Min = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Min'), 'Min', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgMin', False)

    
    Min = property(__Min.value, __Min.set, None, u' Minimum value of the data [count] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Stdev uses Python identifier Stdev
    __Stdev = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Stdev'), 'Stdev', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgStdev', False)

    
    Stdev = property(__Stdev.value, __Stdev.set, None, u' Sample standard deviation of the data\n                        [count] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}XLower uses Python identifier XLower
    __XLower = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XLower'), 'XLower', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgXLower', False)

    
    XLower = property(__XLower.value, __XLower.set, None, u' X position of lower left corner of the\n                        statistics region [pixel] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}Max uses Python identifier Max
    __Max = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Max'), 'Max', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgMax', False)

    
    Max = property(__Max.value, __Max.set, None, u' Maximum value of the data [count] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}MinY uses Python identifier MinY
    __MinY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinY'), 'MinY', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgMinY', False)

    
    MinY = property(__MinY.value, __MinY.set, None, u' Y position of minimum value [pixel] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}NPix uses Python identifier NPix
    __NPix = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NPix'), 'NPix', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgNPix', False)

    
    NPix = property(__NPix.value, __NPix.set, None, u' Number of pixels in the data [None] ')

    
    # Element {http://euclid.esa.org/schema/bas/img}YLower uses Python identifier YLower
    __YLower = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YLower'), 'YLower', '__httpeuclid_esa_orgschemabasimg_imStats_httpeuclid_esa_orgschemabasimgYLower', False)

    
    YLower = property(__YLower.value, __YLower.set, None, u' Y position of lower left corner of the\n                        statistics region [pixel] ')


    _ElementMap = {
        __XUpper.name() : __XUpper,
        __MaxX.name() : __MaxX,
        __Median.name() : __Median,
        __Mean.name() : __Mean,
        __YUpper.name() : __YUpper,
        __MinX.name() : __MinX,
        __MaxY.name() : __MaxY,
        __Min.name() : __Min,
        __ExtObjectId.name() : __ExtObjectId,
        __Stdev.name() : __Stdev,
        __XLower.name() : __XLower,
        __Max.name() : __Max,
        __MinY.name() : __MinY,
        __NPix.name() : __NPix,
        __YLower.name() : __YLower
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'imStats', imStats)


# Complex type baseCalFrame with content type ELEMENT_ONLY
class baseCalFrame (baseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseCalFrame')
    # Base type is baseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/bas/img}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemabasimg_baseCalFrame_httpeuclid_esa_orgschemabasimgTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/bas/img}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemabasimg_baseCalFrame_httpeuclid_esa_orgschemabasimgChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/bas/img}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemabasimg_baseCalFrame_httpeuclid_esa_orgschemabasimgTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')


    _ElementMap = baseFrame._ElementMap.copy()
    _ElementMap.update({
        __TimestampEnd.name() : __TimestampEnd,
        __Chip.name() : __Chip,
        __TimestampStart.name() : __TimestampStart
    })
    _AttributeMap = baseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'baseCalFrame', baseCalFrame)


# Complex type baseSciFrame with content type ELEMENT_ONLY
class baseSciFrame (baseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseSciFrame')
    # Base type is baseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/bas/img}Astrom uses Python identifier Astrom
    __Astrom = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Astrom'), 'Astrom', '__httpeuclid_esa_orgschemabasimg_baseSciFrame_httpeuclid_esa_orgschemabasimgAstrom', False)

    
    Astrom = property(__Astrom.value, __Astrom.set, None, u' The (basic) astrometric\n                                parameters (with only linear\n                                terms)')

    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/bas/img}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemabasimg_baseSciFrame_httpeuclid_esa_orgschemabasimgFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/bas/img}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemabasimg_baseSciFrame_httpeuclid_esa_orgschemabasimgTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/bas/img}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemabasimg_baseSciFrame_httpeuclid_esa_orgschemabasimgObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = baseFrame._ElementMap.copy()
    _ElementMap.update({
        __Astrom.name() : __Astrom,
        __Filter.name() : __Filter,
        __Template.name() : __Template,
        __ObsBlock.name() : __ObsBlock
    })
    _AttributeMap = baseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'baseSciFrame', baseSciFrame)




obsBlock._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Group'), pyxb.binding.datatypes.string, scope=obsBlock, documentation=u' Group identifier for linked observational\n                        blocks [None] '))

obsBlock._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProgramId'), pyxb.binding.datatypes.short, scope=obsBlock, documentation=u' Observational program identifier [None] '))

obsBlock._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.short, scope=obsBlock, documentation=u' Identifier of the observational block\n                        [None] '))

obsBlock._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DictionaryId'), pyxb.binding.datatypes.string, scope=obsBlock, documentation=u' Identifier of the observational\n                        dictionary defining the type of observation [None] '))

obsBlock._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PI'), CommonDM.dm.sys.sgs_stub.curation, scope=obsBlock, documentation=u' Information about the investigator(s)\n                        [None] '))

obsBlock._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=obsBlock, documentation=u' Name of the observational block [None] '))

obsBlock._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=obsBlock, documentation=u' Unique EXT object identifier [None] '))

obsBlock._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Start'), pyxb.binding.datatypes.dateTime, scope=obsBlock, documentation=u' UTC date the observational block was\n                        started [None] '))
obsBlock._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(obsBlock._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(obsBlock._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PI')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(obsBlock._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DictionaryId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(obsBlock._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Group')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(obsBlock._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(obsBlock._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(obsBlock._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProgramId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(obsBlock._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Start')), min_occurs=1, max_occurs=1)
    )
obsBlock._ContentModel = pyxb.binding.content.ParticleModel(obsBlock._GroupModel, min_occurs=1, max_occurs=1)



template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DictionaryId'), pyxb.binding.datatypes.string, scope=template, documentation=u' Identifier of the observational\n                        dictionary defining the type of observation [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=template, documentation=u' Name of the observational template [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), filter, scope=template, documentation=u' Information about the observational\n                        filter [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sequencer'), pyxb.binding.datatypes.string, scope=template, documentation=u' Observational sequencer script [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.short, scope=template, documentation=u' Identifier of the observational template\n                        [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Type'), pyxb.binding.datatypes.string, scope=template, documentation=u' Observational template type [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Start'), pyxb.binding.datatypes.dateTime, scope=template, documentation=u' UTC date the observational template was\n                        started [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Technique'), pyxb.binding.datatypes.string, scope=template, documentation=u' Observational template technique [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Exposures'), pyxb.binding.datatypes.short, scope=template, documentation=u' Number of exposures within the\n                        observational template [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=template, documentation=u' Unique EXT object identifier [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsId'), pyxb.binding.datatypes.short, scope=template, documentation=u' Identifier of the associated\n                        observational block [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), pyxb.binding.datatypes.string, scope=template, documentation=u' Version of the observational template\n                        [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsStart'), pyxb.binding.datatypes.dateTime, scope=template, documentation=u' UTC date the associated observational\n                        block was started [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Category'), pyxb.binding.datatypes.string, scope=template, documentation=u' Observational template category [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Index'), pyxb.binding.datatypes.short, scope=template, documentation=u' Observational template index within the\n                        associated observational block [None] '))

template._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Strategy'), pyxb.binding.datatypes.string, scope=template, documentation=u' Observational template strategy [None] '))
template._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DictionaryId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Start')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Exposures')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sequencer')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Index')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Strategy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Category')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Technique')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Type')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(template._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1)
    )
template._ContentModel = pyxb.binding.content.ParticleModel(template._GroupModel, min_occurs=1, max_occurs=1)



filter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HasFringes'), pyxb.binding.datatypes.int, scope=filter, documentation=u' Indicates if data in this photometric\n                        band may contain fringes [None] '))

filter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=filter, documentation=u' Unique EXT object identifier [None] '))

filter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagId'), CommonDM.dm.bas.dtd_stub.nameRestriction, scope=filter, documentation=u' Identifier of the photometric band [None] '))

filter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CentralWavelength'), pyxb.binding.datatypes.float, scope=filter, documentation=u' Center wavelength of the photometric band\n                        [angstrom] '))

filter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), CommonDM.dm.bas.dtd_stub.nameRestriction, scope=filter, documentation=u' Name of the observational filter [None] '))
filter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(filter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CentralWavelength')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HasFringes')), min_occurs=1, max_occurs=1)
    )
filter._ContentModel = pyxb.binding.content.ParticleModel(filter._GroupModel, min_occurs=1, max_occurs=1)



chip._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), CommonDM.dm.bas.dtd_stub.nameRestriction, scope=chip, documentation=u' Name of the chip [None] '))

chip._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=chip, documentation=u' Unique EXT object identifier [None] '))
chip._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(chip._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(chip._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1)
    )
chip._ContentModel = pyxb.binding.content.ParticleModel(chip._GroupModel, min_occurs=1, max_occurs=1)



processTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=processTarget, documentation=u' Unique EXT object identifier [None] '))

processTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QualityFlags'), pyxb.binding.datatypes.int, scope=processTarget, documentation=u' Automatic/internal quality flag [None] '))

processTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IsValid'), pyxb.binding.datatypes.int, scope=processTarget, documentation=u' Manual/external flag to disqualify bad\n                        data (SuperFlag) [None] '))

processTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), pyxb.binding.datatypes.dateTime, scope=processTarget, documentation=u' UTC date this object was created [None] '))
processTarget._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(processTarget._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(processTarget._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(processTarget._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(processTarget._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1)
    )
processTarget._ContentModel = pyxb.binding.content.ParticleModel(processTarget._GroupModel, min_occurs=1, max_occurs=1)



processTargetDataObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Storage'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=processTargetDataObject, documentation=u' Customized storage container for\n                                the data [None] '))
processTargetDataObject._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(processTargetDataObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(processTargetDataObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(processTargetDataObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(processTargetDataObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1)
    )
processTargetDataObject._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(processTargetDataObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1)
    )
processTargetDataObject._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(processTargetDataObject._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(processTargetDataObject._GroupModel_2, min_occurs=1, max_occurs=1)
    )
processTargetDataObject._ContentModel = pyxb.binding.content.ParticleModel(processTargetDataObject._GroupModel, min_occurs=1, max_occurs=1)



baseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Naxis2'), pyxb.binding.datatypes.int, scope=baseFrame, documentation=u' Length of data in axis 2 [pixel] '))

baseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImStat'), imStats, scope=baseFrame, documentation=u' Information about the statistics\n                                of the image pixels [None] '))

baseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Naxis1'), pyxb.binding.datatypes.int, scope=baseFrame, documentation=u' Length of data in axis 1 [pixel] '))

baseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), instrument, scope=baseFrame, documentation=u' Information about the acquisition\n                                instrument [None] '))
baseFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1)
    )
baseFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1)
    )
baseFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFrame._GroupModel_3, min_occurs=1, max_occurs=1)
    )
baseFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImStat')), min_occurs=1, max_occurs=1)
    )
baseFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
baseFrame._ContentModel = pyxb.binding.content.ParticleModel(baseFrame._GroupModel, min_occurs=1, max_occurs=1)



instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Longtitude'), pyxb.binding.datatypes.float, scope=instrument, documentation=u' Geographic longitude of a ground-based\n                        instrument [degree] '))

instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Timezone'), pyxb.binding.datatypes.float, scope=instrument, documentation=u' Timezone of a ground-based instrument\n                        [hour] '))

instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), CommonDM.dm.bas.dtd_stub.nameRestriction, scope=instrument, documentation=u' Name of the instrument\n                        [None]'))

instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Latitude'), pyxb.binding.datatypes.float, scope=instrument, documentation=u' Geographic latitude of a ground-based\n                        instrument [degree] '))

instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TelescopeName'), CommonDM.dm.bas.dtd_stub.nameRestriction, scope=instrument, documentation=u' Name of the telescope the instrument is\n                        mounted on [None] '))

instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Elevation'), pyxb.binding.datatypes.float, scope=instrument, documentation=u' Geographic elevation of a ground-based\n                        instrument [meter] '))

instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=instrument, documentation=u' Unique EXT object identifier [None] '))
instrument._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(instrument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(instrument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(instrument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TelescopeName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(instrument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Longtitude')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(instrument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Latitude')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(instrument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Elevation')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(instrument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Timezone')), min_occurs=1, max_occurs=1)
    )
instrument._ContentModel = pyxb.binding.content.ParticleModel(instrument._GroupModel, min_occurs=1, max_occurs=1)



imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XUpper'), pyxb.binding.datatypes.int, scope=imStats, documentation=u' X position of upper right corner of the\n                        statistics region [pixel] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxX'), pyxb.binding.datatypes.int, scope=imStats, documentation=u' X position of maximum value [pixel] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Median'), pyxb.binding.datatypes.double, scope=imStats, documentation=u' Median value of the data [count] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Mean'), pyxb.binding.datatypes.double, scope=imStats, documentation=u' Mean value of the data [count] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YUpper'), pyxb.binding.datatypes.int, scope=imStats, documentation=u' Y position of upper right corner of the\n                        statistics region [pixel] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinX'), pyxb.binding.datatypes.int, scope=imStats, documentation=u' X position of minimum value [pixel] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxY'), pyxb.binding.datatypes.int, scope=imStats, documentation=u' Y position of maximum value [pixel] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Min'), pyxb.binding.datatypes.double, scope=imStats, documentation=u' Minimum value of the data [count] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=imStats, documentation=u' Unique EXT object identifier [None] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Stdev'), pyxb.binding.datatypes.double, scope=imStats, documentation=u' Sample standard deviation of the data\n                        [count] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XLower'), pyxb.binding.datatypes.int, scope=imStats, documentation=u' X position of lower left corner of the\n                        statistics region [pixel] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Max'), pyxb.binding.datatypes.double, scope=imStats, documentation=u' Maximum value of the data [count] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinY'), pyxb.binding.datatypes.int, scope=imStats, documentation=u' Y position of minimum value [pixel] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NPix'), pyxb.binding.datatypes.long, scope=imStats, documentation=u' Number of pixels in the data [None] '))

imStats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YLower'), pyxb.binding.datatypes.int, scope=imStats, documentation=u' Y position of lower left corner of the\n                        statistics region [pixel] '))
imStats._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Min')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Max')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Mean')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Stdev')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Median')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinY')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxY')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NPix')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XLower')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YLower')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XUpper')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(imStats._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YUpper')), min_occurs=1, max_occurs=1)
    )
imStats._ContentModel = pyxb.binding.content.ParticleModel(imStats._GroupModel, min_occurs=1, max_occurs=1)



baseCalFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=baseCalFrame, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

baseCalFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), chip, scope=baseCalFrame, documentation=u' Information about the detector\n                                chip [None] '))

baseCalFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=baseCalFrame, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))
baseCalFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1)
    )
baseCalFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1)
    )
baseCalFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseCalFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
baseCalFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImStat')), min_occurs=1, max_occurs=1)
    )
baseCalFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseCalFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
baseCalFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
baseCalFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseCalFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseCalFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
baseCalFrame._ContentModel = pyxb.binding.content.ParticleModel(baseCalFrame._GroupModel, min_occurs=1, max_occurs=1)



baseSciFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Astrom'), CommonDM.dm.bas.cot_stub.astrom, scope=baseSciFrame, documentation=u' The (basic) astrometric\n                                parameters (with only linear\n                                terms)'))

baseSciFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), filter, scope=baseSciFrame, documentation=u' Information about the\n                                observational filter [None] '))

baseSciFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), template, scope=baseSciFrame, documentation=u' Information about the\n                                observational template [None] '))

baseSciFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), obsBlock, scope=baseSciFrame, documentation=u' Information about the\n                                observational block [None] '))
baseSciFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1)
    )
baseSciFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1)
    )
baseSciFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseSciFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
baseSciFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImStat')), min_occurs=1, max_occurs=1)
    )
baseSciFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseSciFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
baseSciFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Astrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1)
    )
baseSciFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseSciFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseSciFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
baseSciFrame._ContentModel = pyxb.binding.content.ParticleModel(baseSciFrame._GroupModel, min_occurs=1, max_occurs=1)
