# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/pro/vis_stub.py
# PyXB bindings for NamespaceModule
# NSM:d7aad58f46d0f1e4a455ef0880cce8c3de78c0ab
# Generated 2014-03-14 09:43:27.469700 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:b4ece584-ab54-11e3-bd08-c4d98710dc86')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import euclid.dm.bas.img_stub
import euclid.dm.bas_stub
import euclid.dm.bas.cot_stub
import euclid.dm.sys.sgs_stub
import euclid.dm.bas.dtd_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/vis', create_if_missing=True)
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
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.WIDE_SURVEY = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'WIDE SURVEY')
STD_ANON.DEEP_SURVEY = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'DEEP SURVEY')
STD_ANON.CALIBRATION_VIS = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'CALIBRATION VIS')
STD_ANON.EXTRA_MODE = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'EXTRA MODE')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic SimpleTypeDefinition
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.STD = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'STD')
STD_ANON_.EXTRA = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'EXTRA')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Complex type CTD_ANON with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}HealPix uses Python identifier HealPix
    __HealPix = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HealPix'), 'HealPix', '__httpeuclid_esa_orgschemaprovis_CTD_ANON_httpeuclid_esa_orgschemaprovisHealPix', False)

    
    HealPix = property(__HealPix.value, __HealPix.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}DEC uses Python identifier DEC
    __DEC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEC'), 'DEC', '__httpeuclid_esa_orgschemaprovis_CTD_ANON_httpeuclid_esa_orgschemaprovisDEC', False)

    
    DEC = property(__DEC.value, __DEC.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}RA uses Python identifier RA
    __RA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RA'), 'RA', '__httpeuclid_esa_orgschemaprovis_CTD_ANON_httpeuclid_esa_orgschemaprovisRA', False)

    
    RA = property(__RA.value, __RA.set, None, None)


    _ElementMap = {
        __HealPix.name() : __HealPix,
        __DEC.name() : __DEC,
        __RA.name() : __RA
    }
    _AttributeMap = {
        
    }



# Complex type visBaseFrame with content type ELEMENT_ONLY
class visBaseFrame (euclid.dm.bas.img_stub.baseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visBaseFrame')
    # Base type is euclid.dm.bas.img_stub.baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags uses Python identifier VisFitsPixelProcessingFlags
    __VisFitsPixelProcessingFlags = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags'), 'VisFitsPixelProcessingFlags', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisVisFitsPixelProcessingFlags', True)

    
    VisFitsPixelProcessingFlags = property(__VisFitsPixelProcessingFlags.value, __VisFitsPixelProcessingFlags.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/vis}VisPipelineFlags uses Python identifier VisPipelineFlags
    __VisPipelineFlags = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags'), 'VisPipelineFlags', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisVisPipelineFlags', True)

    
    VisPipelineFlags = property(__VisPipelineFlags.value, __VisPipelineFlags.set, None, u'OU VIS flags for the pipeline.  Flags should be set the FITS file is processed in various modules of the OUVIS pipeline.  TBD if the value will need to be shifted or masked off')

    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}ExposureMode uses Python identifier ExposureMode
    __ExposureMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode'), 'ExposureMode', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisExposureMode', False)

    
    ExposureMode = property(__ExposureMode.value, __ExposureMode.set, None, None)

    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}VISErrorCode uses Python identifier VISErrorCode
    __VISErrorCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode'), 'VISErrorCode', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisVISErrorCode', False)

    
    VISErrorCode = property(__VISErrorCode.value, __VISErrorCode.set, None, u'Error Codes given in the OU-VIS pipeline related to the FITS file.  May move moved to a higher level.  TBD the format of the codes')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Position'), 'Position', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisPosition', False)

    
    Position = property(__Position.value, __Position.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExposureTime uses Python identifier ExposureTime
    __ExposureTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime'), 'ExposureTime', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisExposureTime', False)

    
    ExposureTime = property(__ExposureTime.value, __ExposureTime.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}TypeCode uses Python identifier TypeCode
    __TypeCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TypeCode'), 'TypeCode', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisTypeCode', False)

    
    TypeCode = property(__TypeCode.value, __TypeCode.set, None, None)

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Dithering uses Python identifier Dithering
    __Dithering = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Dithering'), 'Dithering', '__httpeuclid_esa_orgschemaprovis_visBaseFrame_httpeuclid_esa_orgschemaprovisDithering', False)

    
    Dithering = property(__Dithering.value, __Dithering.set, None, None)

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = euclid.dm.bas.img_stub.baseFrame._ElementMap.copy()
    _ElementMap.update({
        __Chip.name() : __Chip,
        __VisFitsPixelProcessingFlags.name() : __VisFitsPixelProcessingFlags,
        __TimestampEnd.name() : __TimestampEnd,
        __VisPipelineFlags.name() : __VisPipelineFlags,
        __ExposureMode.name() : __ExposureMode,
        __VISErrorCode.name() : __VISErrorCode,
        __Position.name() : __Position,
        __ExposureTime.name() : __ExposureTime,
        __Filter.name() : __Filter,
        __TypeCode.name() : __TypeCode,
        __TimestampStart.name() : __TimestampStart,
        __Dithering.name() : __Dithering
    })
    _AttributeMap = euclid.dm.bas.img_stub.baseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'visBaseFrame', visBaseFrame)


# Complex type rawFrame with content type ELEMENT_ONLY
class rawFrame (visBaseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawFrame')
    # Base type is visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Ovscx uses Python identifier Ovscx
    __Ovscx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscx'), 'Ovscx', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisOvscx', False)

    
    Ovscx = property(__Ovscx.value, __Ovscx.set, None, u' Number of overscan pixels in the\n                                X direction [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Object uses Python identifier Object
    __Object = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Object'), 'Object', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisObject', False)

    
    Object = property(__Object.value, __Object.set, None, u' Name of target object [None] ')

    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Ovscy uses Python identifier Ovscy
    __Ovscy = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscy'), 'Ovscy', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisOvscy', False)

    
    Ovscy = property(__Ovscy.value, __Ovscy.set, None, u' Number of overscan pixels in the\n                                Y direction [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Date uses Python identifier Date
    __Date = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Date'), 'Date', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisDate', False)

    
    Date = property(__Date.value, __Date.set, None, u' UTC date the original data file\n                                was saved [None] ')

    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}OverscanXStat uses Python identifier OverscanXStat
    __OverscanXStat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanXStat'), 'OverscanXStat', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisOverscanXStat', False)

    
    OverscanXStat = property(__OverscanXStat.value, __OverscanXStat.set, None, u' Statistics of the overscan region\n                                in the X direction [None] ')

    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Prscxpre uses Python identifier Prscxpre
    __Prscxpre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscxpre'), 'Prscxpre', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisPrscxpre', False)

    
    Prscxpre = property(__Prscxpre.value, __Prscxpre.set, None, u' Number of prescan pixels to skip\n                                in the X direction at the edge of the chip\n                                [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Prscypre uses Python identifier Prscypre
    __Prscypre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscypre'), 'Prscypre', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisPrscypre', False)

    
    Prscypre = property(__Prscypre.value, __Prscypre.set, None, u' Number of prescan pixels to skip\n                                in the Y direction at the edge of the chip\n                                [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Ovscxpre uses Python identifier Ovscxpre
    __Ovscxpre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpre'), 'Ovscxpre', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisOvscxpre', False)

    
    Ovscxpre = property(__Ovscxpre.value, __Ovscxpre.set, None, u' Number of overscan pixels to skip\n                                in the X direction at the edge of the chip\n                                [pixel] ')

    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}PrescanYStat uses Python identifier PrescanYStat
    __PrescanYStat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrescanYStat'), 'PrescanYStat', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisPrescanYStat', False)

    
    PrescanYStat = property(__PrescanYStat.value, __PrescanYStat.set, None, u' Statistics of the prescan region\n                                in the Y direction [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}DateObs uses Python identifier DateObs
    __DateObs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), 'DateObs', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisDateObs', False)

    
    DateObs = property(__DateObs.value, __DateObs.set, None, u' UTC date at the start of the\n                                observation [None] ')

    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}MjdObs uses Python identifier MjdObs
    __MjdObs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MjdObs'), 'MjdObs', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisMjdObs', False)

    
    MjdObs = property(__MjdObs.value, __MjdObs.set, None, u' Modified Julian date at the start\n                                of the observation (JD-2400000.5) [day] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}OverscanYStat uses Python identifier OverscanYStat
    __OverscanYStat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanYStat'), 'OverscanYStat', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisOverscanYStat', False)

    
    OverscanYStat = property(__OverscanYStat.value, __OverscanYStat.set, None, u' Statistics of the overscan region\n                                in the Y direction [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Prscxpst uses Python identifier Prscxpst
    __Prscxpst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscxpst'), 'Prscxpst', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisPrscxpst', False)

    
    Prscxpst = property(__Prscxpst.value, __Prscxpst.set, None, u' Number of prescan pixels to skip\n                                in the X direction at the edge of the data\n                                region [pixel] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}Lst uses Python identifier Lst
    __Lst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Lst'), 'Lst', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisLst', False)

    
    Lst = property(__Lst.value, __Lst.set, None, u' Local sidereal time at the start\n                                of the observation expressed as the number of\n                                seconds (a float) since UTC midnight [sec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Prscypst uses Python identifier Prscypst
    __Prscypst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscypst'), 'Prscypst', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisPrscypst', False)

    
    Prscypst = property(__Prscypst.value, __Prscypst.set, None, u' Number of prescan pixels to skip\n                                in the Y direction at the edge of the data\n                                region [pixel] ')

    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Utc uses Python identifier Utc
    __Utc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Utc'), 'Utc', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisUtc', False)

    
    Utc = property(__Utc.value, __Utc.set, None, u' Universal coordinated time at the\n                                start of the observation expressed as the number\n                                of seconds (a float) since UTC midnight [sec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Ovscxpst uses Python identifier Ovscxpst
    __Ovscxpst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpst'), 'Ovscxpst', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisOvscxpst', False)

    
    Ovscxpst = property(__Ovscxpst.value, __Ovscxpst.set, None, u' Number of overscan pixels to skip\n                                in the X direction at the edge of the data\n                                region [pixel] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Ovscypst uses Python identifier Ovscypst
    __Ovscypst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscypst'), 'Ovscypst', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisOvscypst', False)

    
    Ovscypst = property(__Ovscypst.value, __Ovscypst.set, None, u' Number of overscan pixels to skip\n                                in the Y direction at the edge of the data\n                                region [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Ovscypre uses Python identifier Ovscypre
    __Ovscypre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscypre'), 'Ovscypre', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisOvscypre', False)

    
    Ovscypre = property(__Ovscypre.value, __Ovscypre.set, None, u' Number of overscan pixels to skip\n                                in the Y direction at the edge of the chip\n                                [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Extension uses Python identifier Extension
    __Extension = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Extension'), 'Extension', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisExtension', False)

    
    Extension = property(__Extension.value, __Extension.set, None, u' Extension number of this frame to\n                                be extracted from the rawFits container [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Prscy uses Python identifier Prscy
    __Prscy = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscy'), 'Prscy', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisPrscy', False)

    
    Prscy = property(__Prscy.value, __Prscy.set, None, u' Number of prescan pixels in the Y\n                                direction [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Prscx uses Python identifier Prscx
    __Prscx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscx'), 'Prscx', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisPrscx', False)

    
    Prscx = property(__Prscx.value, __Prscx.set, None, u' Number of prescan pixels in the X\n                                direction [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PrescanXStat uses Python identifier PrescanXStat
    __PrescanXStat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrescanXStat'), 'PrescanXStat', '__httpeuclid_esa_orgschemaprovis_rawFrame_httpeuclid_esa_orgschemaprovisPrescanXStat', False)

    
    PrescanXStat = property(__PrescanXStat.value, __PrescanXStat.set, None, u' Statistics of the prescan region\n                                in the X direction [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame

    _ElementMap = visBaseFrame._ElementMap.copy()
    _ElementMap.update({
        __Ovscx.name() : __Ovscx,
        __Object.name() : __Object,
        __Ovscy.name() : __Ovscy,
        __Date.name() : __Date,
        __OverscanXStat.name() : __OverscanXStat,
        __Prscxpre.name() : __Prscxpre,
        __Template.name() : __Template,
        __Prscypre.name() : __Prscypre,
        __Ovscxpre.name() : __Ovscxpre,
        __ObsBlock.name() : __ObsBlock,
        __PrescanYStat.name() : __PrescanYStat,
        __DateObs.name() : __DateObs,
        __MjdObs.name() : __MjdObs,
        __OverscanYStat.name() : __OverscanYStat,
        __Prscxpst.name() : __Prscxpst,
        __Lst.name() : __Lst,
        __Prscypst.name() : __Prscypst,
        __Utc.name() : __Utc,
        __Ovscxpst.name() : __Ovscxpst,
        __Ovscypst.name() : __Ovscypst,
        __Ovscypre.name() : __Ovscypre,
        __Extension.name() : __Extension,
        __Prscy.name() : __Prscy,
        __Prscx.name() : __Prscx,
        __PrescanXStat.name() : __PrescanXStat
    })
    _AttributeMap = visBaseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'rawFrame', rawFrame)


# Complex type rawDarkFrame with content type ELEMENT_ONLY
class rawDarkFrame (rawFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawDarkFrame')
    # Base type is rawFrame
    
    # Element Ovscx ({http://euclid.esa.org/schema/pro/vis}Ovscx) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}ExpTime uses Python identifier ExpTime
    __ExpTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), 'ExpTime', '__httpeuclid_esa_orgschemaprovis_rawDarkFrame_httpeuclid_esa_orgschemaprovisExpTime', False)

    
    ExpTime = property(__ExpTime.value, __ExpTime.set, None, u' Total time of an individual\n                                exposure [sec] ')

    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element PrescanYStat ({http://euclid.esa.org/schema/pro/vis}PrescanYStat) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Ovscy ({http://euclid.esa.org/schema/pro/vis}Ovscy) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Date ({http://euclid.esa.org/schema/pro/vis}Date) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element OverscanXStat ({http://euclid.esa.org/schema/pro/vis}OverscanXStat) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Prscxpre ({http://euclid.esa.org/schema/pro/vis}Prscxpre) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Template ({http://euclid.esa.org/schema/pro/vis}Template) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Object ({http://euclid.esa.org/schema/pro/vis}Object) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Prscypre ({http://euclid.esa.org/schema/pro/vis}Prscypre) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Ovscxpre ({http://euclid.esa.org/schema/pro/vis}Ovscxpre) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ObsBlock ({http://euclid.esa.org/schema/pro/vis}ObsBlock) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element DateObs ({http://euclid.esa.org/schema/pro/vis}DateObs) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element MjdObs ({http://euclid.esa.org/schema/pro/vis}MjdObs) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element OverscanYStat ({http://euclid.esa.org/schema/pro/vis}OverscanYStat) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Prscxpst ({http://euclid.esa.org/schema/pro/vis}Prscxpst) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Lst ({http://euclid.esa.org/schema/pro/vis}Lst) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Utc ({http://euclid.esa.org/schema/pro/vis}Utc) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Ovscxpst ({http://euclid.esa.org/schema/pro/vis}Ovscxpst) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Ovscypst ({http://euclid.esa.org/schema/pro/vis}Ovscypst) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Ovscypre ({http://euclid.esa.org/schema/pro/vis}Ovscypre) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Extension ({http://euclid.esa.org/schema/pro/vis}Extension) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscy ({http://euclid.esa.org/schema/pro/vis}Prscy) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Prscx ({http://euclid.esa.org/schema/pro/vis}Prscx) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element PrescanXStat ({http://euclid.esa.org/schema/pro/vis}PrescanXStat) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Prscypst ({http://euclid.esa.org/schema/pro/vis}Prscypst) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame

    _ElementMap = rawFrame._ElementMap.copy()
    _ElementMap.update({
        __ExpTime.name() : __ExpTime
    })
    _AttributeMap = rawFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'rawDarkFrame', rawDarkFrame)


# Complex type associateListParameters with content type ELEMENT_ONLY
class associateListParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'associateListParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}SearchDistance uses Python identifier SearchDistance
    __SearchDistance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SearchDistance'), 'SearchDistance', '__httpeuclid_esa_orgschemaprovis_associateListParameters_httpeuclid_esa_orgschemaprovisSearchDistance', False)

    
    SearchDistance = property(__SearchDistance.value, __SearchDistance.set, None, u' Radius of search for associates [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SextractorFlagMask uses Python identifier SextractorFlagMask
    __SextractorFlagMask = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SextractorFlagMask'), 'SextractorFlagMask', '__httpeuclid_esa_orgschemaprovis_associateListParameters_httpeuclid_esa_orgschemaprovisSextractorFlagMask', False)

    
    SextractorFlagMask = property(__SextractorFlagMask.value, __SextractorFlagMask.set, None, u' Value of SExtractor flag mask for source\n                        filtering [None]')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SingleOutClosestPairs uses Python identifier SingleOutClosestPairs
    __SingleOutClosestPairs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SingleOutClosestPairs'), 'SingleOutClosestPairs', '__httpeuclid_esa_orgschemaprovis_associateListParameters_httpeuclid_esa_orgschemaprovisSingleOutClosestPairs', False)

    
    SingleOutClosestPairs = property(__SingleOutClosestPairs.value, __SingleOutClosestPairs.set, None, u' Filter to retain only the closest\n                        associations [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_associateListParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaprovis_associateListParameters_httpeuclid_esa_orgschemaprovisSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')


    _ElementMap = {
        __SearchDistance.name() : __SearchDistance,
        __SextractorFlagMask.name() : __SextractorFlagMask,
        __SingleOutClosestPairs.name() : __SingleOutClosestPairs,
        __ExtObjectId.name() : __ExtObjectId,
        __SourceCodeVersion.name() : __SourceCodeVersion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'associateListParameters', associateListParameters)


# Complex type associateListDict with content type ELEMENT_ONLY
class associateListDict (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'associateListDict')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}ALID uses Python identifier ALID
    __ALID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ALID'), 'ALID', '__httpeuclid_esa_orgschemaprovis_associateListDict_httpeuclid_esa_orgschemaprovisALID', False)

    
    ALID = property(__ALID.value, __ALID.set, None, u' Identifier of the associate list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SID uses Python identifier SID
    __SID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SID'), 'SID', '__httpeuclid_esa_orgschemaprovis_associateListDict_httpeuclid_esa_orgschemaprovisSID', False)

    
    SID = property(__SID.value, __SID.set, None, u' Identifier of a source in the source list\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FLAG uses Python identifier FLAG
    __FLAG = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG'), 'FLAG', '__httpeuclid_esa_orgschemaprovis_associateListDict_httpeuclid_esa_orgschemaprovisFLAG', False)

    
    FLAG = property(__FLAG.value, __FLAG.set, None, u' Internal flag indicating the source\n                        list(s) participating in the association [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}AID uses Python identifier AID
    __AID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AID'), 'AID', '__httpeuclid_esa_orgschemaprovis_associateListDict_httpeuclid_esa_orgschemaprovisAID', False)

    
    AID = property(__AID.value, __AID.set, None, u' Identifier of an association in the\n                        associate list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SLID uses Python identifier SLID
    __SLID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SLID'), 'SLID', '__httpeuclid_esa_orgschemaprovis_associateListDict_httpeuclid_esa_orgschemaprovisSLID', False)

    
    SLID = property(__SLID.value, __SLID.set, None, u' Identifier of the source list [None] ')


    _ElementMap = {
        __ALID.name() : __ALID,
        __SID.name() : __SID,
        __FLAG.name() : __FLAG,
        __AID.name() : __AID,
        __SLID.name() : __SLID
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'associateListDict', associateListDict)


# Complex type reducedScienceFrame with content type ELEMENT_ONLY
class reducedScienceFrame (visBaseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reducedScienceFrame')
    # Base type is visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}AirmassStart uses Python identifier AirmassStart
    __AirmassStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AirmassStart'), 'AirmassStart', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisAirmassStart', False)

    
    AirmassStart = property(__AirmassStart.value, __AirmassStart.set, None, u' Airmass at the beginning of the\n                                observation [None] ')

    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Illumination uses Python identifier Illumination
    __Illumination = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), 'Illumination', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisIllumination', False)

    
    Illumination = property(__Illumination.value, __Illumination.set, None, u' Information about the\n                                illumination correction\n                                [None]')

    
    # Element {http://euclid.esa.org/schema/pro/vis}AirmassEnd uses Python identifier AirmassEnd
    __AirmassEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AirmassEnd'), 'AirmassEnd', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisAirmassEnd', False)

    
    AirmassEnd = property(__AirmassEnd.value, __AirmassEnd.set, None, u' Airmass at the ending of the\n                                observation [None] ')

    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Weight uses Python identifier Weight
    __Weight = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Weight'), 'Weight', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisWeight', False)

    
    Weight = property(__Weight.value, __Weight.set, None, u' Information about the detector\n                                pixel weights [None] ')

    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}ScaleFactor uses Python identifier ScaleFactor
    __ScaleFactor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ScaleFactor'), 'ScaleFactor', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisScaleFactor', False)

    
    ScaleFactor = property(__ScaleFactor.value, __ScaleFactor.set, None, u' Detector fringe pattern scaling\n                                factor [None] ')

    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Seeing uses Python identifier Seeing
    __Seeing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), 'Seeing', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisSeeing', False)

    
    Seeing = property(__Seeing.value, __Seeing.set, None, u' Estimate of seeing using the\n                                median FWHM (filtered to isolate most\n                                stellar-like sources) [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}Object uses Python identifier Object
    __Object = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Object'), 'Object', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisObject', False)

    
    Object = property(__Object.value, __Object.set, None, u' Name of target object [None] ')

    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}Raw uses Python identifier Raw
    __Raw = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Raw'), 'Raw', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisRaw', False)

    
    Raw = property(__Raw.value, __Raw.set, None, u' Information about the input raw\n                                science frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExpTime uses Python identifier ExpTime
    __ExpTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), 'ExpTime', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisExpTime', False)

    
    ExpTime = property(__ExpTime.value, __ExpTime.set, None, u' Total time of an individual\n                                exposure [sec] ')

    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Astrom uses Python identifier Astrom
    __Astrom = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Astrom'), 'Astrom', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisAstrom', False)

    
    Astrom = property(__Astrom.value, __Astrom.set, None, u' Basic information about the\n                                astrometry (linear terms only) [None] ')

    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Date uses Python identifier Date
    __Date = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Date'), 'Date', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisDate', False)

    
    Date = property(__Date.value, __Date.set, None, u' UTC date the original data file\n                                was saved [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Bias uses Python identifier Bias
    __Bias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Bias'), 'Bias', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisBias', False)

    
    Bias = property(__Bias.value, __Bias.set, None, u' Information about the detector\n                                bias offset levels [None] ')

    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}DateObs uses Python identifier DateObs
    __DateObs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), 'DateObs', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisDateObs', False)

    
    DateObs = property(__DateObs.value, __DateObs.set, None, u' UTC date at the start of the\n                                observation [None] ')

    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Flat uses Python identifier Flat
    __Flat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flat'), 'Flat', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrame_httpeuclid_esa_orgschemaprovisFlat', False)

    
    Flat = property(__Flat.value, __Flat.set, None, u' Information about the detector\n                                sensitivity variations [None] ')

    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame

    _ElementMap = visBaseFrame._ElementMap.copy()
    _ElementMap.update({
        __AirmassStart.name() : __AirmassStart,
        __Illumination.name() : __Illumination,
        __AirmassEnd.name() : __AirmassEnd,
        __Weight.name() : __Weight,
        __ScaleFactor.name() : __ScaleFactor,
        __Seeing.name() : __Seeing,
        __ObsBlock.name() : __ObsBlock,
        __ProcessParams.name() : __ProcessParams,
        __Object.name() : __Object,
        __Raw.name() : __Raw,
        __ExpTime.name() : __ExpTime,
        __Astrom.name() : __Astrom,
        __Date.name() : __Date,
        __Template.name() : __Template,
        __Bias.name() : __Bias,
        __DateObs.name() : __DateObs,
        __Flat.name() : __Flat
    })
    _AttributeMap = visBaseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'reducedScienceFrame', reducedScienceFrame)


# Complex type biasFrame with content type ELEMENT_ONLY
class biasFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'biasFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaprovis_biasFrame_httpeuclid_esa_orgschemaprovisProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ReadNoise uses Python identifier ReadNoise
    __ReadNoise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise'), 'ReadNoise', '__httpeuclid_esa_orgschemaprovis_biasFrame_httpeuclid_esa_orgschemaprovisReadNoise', False)

    
    ReadNoise = property(__ReadNoise.value, __ReadNoise.set, None, u' Information about the detector\n                                readout noise [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}RawBiasFrames uses Python identifier RawBiasFrames
    __RawBiasFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames'), 'RawBiasFrames', '__httpeuclid_esa_orgschemaprovis_biasFrame_httpeuclid_esa_orgschemaprovisRawBiasFrames', True)

    
    RawBiasFrames = property(__RawBiasFrames.value, __RawBiasFrames.set, None, u' List of input raw bias frames\n                                [None] ')


    _ElementMap = {
        __ProcessParams.name() : __ProcessParams,
        __ReadNoise.name() : __ReadNoise,
        __RawBiasFrames.name() : __RawBiasFrames
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'biasFrame', biasFrame)


# Complex type masterFlatFrame with content type ELEMENT_ONLY
class masterFlatFrame (visBaseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'masterFlatFrame')
    # Base type is visBaseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaprovis_masterFlatFrame_httpeuclid_esa_orgschemaprovisProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/vis}Flat uses Python identifier Flat
    __Flat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flat'), 'Flat', '__httpeuclid_esa_orgschemaprovis_masterFlatFrame_httpeuclid_esa_orgschemaprovisFlat', False)

    
    Flat = property(__Flat.value, __Flat.set, None, u' Information about the detector\n                                sensitivity variations [None] ')

    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame

    _ElementMap = visBaseFrame._ElementMap.copy()
    _ElementMap.update({
        __ProcessParams.name() : __ProcessParams,
        __Flat.name() : __Flat
    })
    _AttributeMap = visBaseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'masterFlatFrame', masterFlatFrame)


# Complex type readNoise with content type ELEMENT_ONLY
class readNoise (euclid.dm.bas.img_stub.processTarget):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'readNoise')
    # Base type is euclid.dm.bas.img_stub.processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}ReadNoise uses Python identifier ReadNoise
    __ReadNoise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise'), 'ReadNoise', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisReadNoise', False)

    
    ReadNoise = property(__ReadNoise.value, __ReadNoise.set, None, u' Value of readout noise\n                                measurement [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}RawBiasFrames uses Python identifier RawBiasFrames
    __RawBiasFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames'), 'RawBiasFrames', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisRawBiasFrames', True)

    
    RawBiasFrames = property(__RawBiasFrames.value, __RawBiasFrames.set, None, u' List of input raw bias frames\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MeanDiff uses Python identifier MeanDiff
    __MeanDiff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MeanDiff'), 'MeanDiff', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisMeanDiff', False)

    
    MeanDiff = property(__MeanDiff.value, __MeanDiff.set, None, u' Mean pixel value difference\n                                between biases [ADU] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MedianDiff uses Python identifier MedianDiff
    __MedianDiff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MedianDiff'), 'MedianDiff', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisMedianDiff', False)

    
    MedianDiff = property(__MedianDiff.value, __MedianDiff.set, None, u' Median pixel value difference\n                                between biases [ADU] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaprovis_readNoise_httpeuclid_esa_orgschemaprovisTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = euclid.dm.bas.img_stub.processTarget._ElementMap.copy()
    _ElementMap.update({
        __ReadNoise.name() : __ReadNoise,
        __RawBiasFrames.name() : __RawBiasFrames,
        __TimestampStart.name() : __TimestampStart,
        __Chip.name() : __Chip,
        __MeanDiff.name() : __MeanDiff,
        __ObsBlock.name() : __ObsBlock,
        __Instrument.name() : __Instrument,
        __ProcessParams.name() : __ProcessParams,
        __MedianDiff.name() : __MedianDiff,
        __TimestampEnd.name() : __TimestampEnd,
        __Template.name() : __Template
    })
    _AttributeMap = euclid.dm.bas.img_stub.processTarget._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'readNoise', readNoise)


# Complex type biasFrameParameters with content type ELEMENT_ONLY
class biasFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'biasFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_biasFrameParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumAbsMean uses Python identifier MaximumAbsMean
    __MaximumAbsMean = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumAbsMean'), 'MaximumAbsMean', '__httpeuclid_esa_orgschemaprovis_biasFrameParameters_httpeuclid_esa_orgschemaprovisMaximumAbsMean', False)

    
    MaximumAbsMean = property(__MaximumAbsMean.value, __MaximumAbsMean.set, None, u' QC: Maximum absolute mean value of the\n                        bias levels [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumSubwinFlatness uses Python identifier MaximumSubwinFlatness
    __MaximumSubwinFlatness = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness'), 'MaximumSubwinFlatness', '__httpeuclid_esa_orgschemaprovis_biasFrameParameters_httpeuclid_esa_orgschemaprovisMaximumSubwinFlatness', False)

    
    MaximumSubwinFlatness = property(__MaximumSubwinFlatness.value, __MaximumSubwinFlatness.set, None, u' QC: Maximum difference between median\n                        values of any two sub-windows [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}OverscanCorrection uses Python identifier OverscanCorrection
    __OverscanCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), 'OverscanCorrection', '__httpeuclid_esa_orgschemaprovis_biasFrameParameters_httpeuclid_esa_orgschemaprovisOverscanCorrection', False)

    
    OverscanCorrection = property(__OverscanCorrection.value, __OverscanCorrection.set, None, u' Overscan correction method index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumStdev uses Python identifier MaximumStdev
    __MaximumStdev = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumStdev'), 'MaximumStdev', '__httpeuclid_esa_orgschemaprovis_biasFrameParameters_httpeuclid_esa_orgschemaprovisMaximumStdev', False)

    
    MaximumStdev = property(__MaximumStdev.value, __MaximumStdev.set, None, u' QC: Maximum sample standard deviation\n                        value of the bias levels [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumSubwinStdev uses Python identifier MaximumSubwinStdev
    __MaximumSubwinStdev = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinStdev'), 'MaximumSubwinStdev', '__httpeuclid_esa_orgschemaprovis_biasFrameParameters_httpeuclid_esa_orgschemaprovisMaximumSubwinStdev', False)

    
    MaximumSubwinStdev = property(__MaximumSubwinStdev.value, __MaximumSubwinStdev.set, None, u' QC: Maximum sample standard deviation\n                        value of any sub-window [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SigmaClip uses Python identifier SigmaClip
    __SigmaClip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip'), 'SigmaClip', '__httpeuclid_esa_orgschemaprovis_biasFrameParameters_httpeuclid_esa_orgschemaprovisSigmaClip', False)

    
    SigmaClip = property(__SigmaClip.value, __SigmaClip.set, None, u' Threshold factor for rejecting raw bias\n                        pixel value outliers (sigma is taken as the readout\n                        noise measurement) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumStdevDifference uses Python identifier MaximumStdevDifference
    __MaximumStdevDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumStdevDifference'), 'MaximumStdevDifference', '__httpeuclid_esa_orgschemaprovis_biasFrameParameters_httpeuclid_esa_orgschemaprovisMaximumStdevDifference', False)

    
    MaximumStdevDifference = property(__MaximumStdevDifference.value, __MaximumStdevDifference.set, None, u' QC: Maximum sample standard deviation\n                        difference of the bias levels relative to the previous\n                        version [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaprovis_biasFrameParameters_httpeuclid_esa_orgschemaprovisSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __MaximumAbsMean.name() : __MaximumAbsMean,
        __MaximumSubwinFlatness.name() : __MaximumSubwinFlatness,
        __OverscanCorrection.name() : __OverscanCorrection,
        __MaximumStdev.name() : __MaximumStdev,
        __MaximumSubwinStdev.name() : __MaximumSubwinStdev,
        __SigmaClip.name() : __SigmaClip,
        __MaximumStdevDifference.name() : __MaximumStdevDifference,
        __SourceCodeVersion.name() : __SourceCodeVersion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'biasFrameParameters', biasFrameParameters)


# Complex type baseList with content type ELEMENT_ONLY
class baseList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}Storage uses Python identifier Storage
    __Storage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Storage'), 'Storage', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisStorage', False)

    
    Storage = property(__Storage.value, __Storage.set, None, u' Customized storage container for the data\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}URRa uses Python identifier URRa
    __URRa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'URRa'), 'URRa', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisURRa', False)

    
    URRa = property(__URRa.value, __URRa.set, None, u' Right Ascension of upper right corner\n                        [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}URDec uses Python identifier URDec
    __URDec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'URDec'), 'URDec', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisURDec', False)

    
    URDec = property(__URDec.value, __URDec.set, None, u' Declination of upper right corner [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ULRa uses Python identifier ULRa
    __ULRa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ULRa'), 'ULRa', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisULRa', False)

    
    ULRa = property(__ULRa.value, __ULRa.set, None, u' Right Ascension of upper left corner\n                        [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisName', False)

    
    Name = property(__Name.value, __Name.set, None, u' Name of the list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}LRDec uses Python identifier LRDec
    __LRDec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LRDec'), 'LRDec', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisLRDec', False)

    
    LRDec = property(__LRDec.value, __LRDec.set, None, u' Declination of lower right corner [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}LRRa uses Python identifier LRRa
    __LRRa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LRRa'), 'LRRa', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisLRRa', False)

    
    LRRa = property(__LRRa.value, __LRRa.set, None, u' Right Ascension of lower right corner\n                        [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Object uses Python identifier Object
    __Object = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Object'), 'Object', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisObject', False)

    
    Object = property(__Object.value, __Object.set, None, u' Name of target object [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}IsValid uses Python identifier IsValid
    __IsValid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IsValid'), 'IsValid', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisIsValid', False)

    
    IsValid = property(__IsValid.value, __IsValid.set, None, u' Manual/external flag to disqualify bad\n                        data (SuperFlag) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}LLRa uses Python identifier LLRa
    __LLRa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LLRa'), 'LLRa', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisLLRa', False)

    
    LLRa = property(__LLRa.value, __LLRa.set, None, u' Right Ascension of lower left corner\n                        [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ULDec uses Python identifier ULDec
    __ULDec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ULDec'), 'ULDec', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisULDec', False)

    
    ULDec = property(__ULDec.value, __ULDec.set, None, u' Declination of upper left corner [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), 'CreationDate', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisCreationDate', False)

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, u' UTC date this object was created [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}LLDec uses Python identifier LLDec
    __LLDec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LLDec'), 'LLDec', '__httpeuclid_esa_orgschemaprovis_baseList_httpeuclid_esa_orgschemaprovisLLDec', False)

    
    LLDec = property(__LLDec.value, __LLDec.set, None, u' Declination of lower left corner [deg] ')


    _ElementMap = {
        __Storage.name() : __Storage,
        __URRa.name() : __URRa,
        __URDec.name() : __URDec,
        __ULRa.name() : __ULRa,
        __Name.name() : __Name,
        __LRDec.name() : __LRDec,
        __LRRa.name() : __LRRa,
        __Object.name() : __Object,
        __IsValid.name() : __IsValid,
        __ExtObjectId.name() : __ExtObjectId,
        __LLRa.name() : __LLRa,
        __ULDec.name() : __ULDec,
        __CreationDate.name() : __CreationDate,
        __LLDec.name() : __LLDec
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'baseList', baseList)


# Complex type associateList with content type ELEMENT_ONLY
class associateList (baseList):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'associateList')
    # Base type is baseList
    
    # Element Storage ({http://euclid.esa.org/schema/pro/vis}Storage) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element LRRa ({http://euclid.esa.org/schema/pro/vis}LRRa) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element URRa ({http://euclid.esa.org/schema/pro/vis}URRa) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element LLDec ({http://euclid.esa.org/schema/pro/vis}LLDec) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceLists uses Python identifier SourceLists
    __SourceLists = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceLists'), 'SourceLists', '__httpeuclid_esa_orgschemaprovis_associateList_httpeuclid_esa_orgschemaprovisSourceLists', True)

    
    SourceLists = property(__SourceLists.value, __SourceLists.set, None, u' List of input source lists [None] ')

    
    # Element ULRa ({http://euclid.esa.org/schema/pro/vis}ULRa) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}Associates uses Python identifier Associates
    __Associates = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Associates'), 'Associates', '__httpeuclid_esa_orgschemaprovis_associateList_httpeuclid_esa_orgschemaprovisAssociates', False)

    
    Associates = property(__Associates.value, __Associates.set, None, u' Column definitions of\n                                associations [None] ')

    
    # Element URDec ({http://euclid.esa.org/schema/pro/vis}URDec) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}AssociateListType uses Python identifier AssociateListType
    __AssociateListType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AssociateListType'), 'AssociateListType', '__httpeuclid_esa_orgschemaprovis_associateList_httpeuclid_esa_orgschemaprovisAssociateListType', False)

    
    AssociateListType = property(__AssociateListType.value, __AssociateListType.set, None, u' Type of associate list [None] ')

    
    # Element Name ({http://euclid.esa.org/schema/pro/vis}Name) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}Alid uses Python identifier Alid
    __Alid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Alid'), 'Alid', '__httpeuclid_esa_orgschemaprovis_associateList_httpeuclid_esa_orgschemaprovisAlid', False)

    
    Alid = property(__Alid.value, __Alid.set, None, u' Identifier of the associate list\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}AssociateCount uses Python identifier AssociateCount
    __AssociateCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AssociateCount'), 'AssociateCount', '__httpeuclid_esa_orgschemaprovis_associateList_httpeuclid_esa_orgschemaprovisAssociateCount', False)

    
    AssociateCount = property(__AssociateCount.value, __AssociateCount.set, None, u' Number of associated source\n                                pairings [None] ')

    
    # Element Object ({http://euclid.esa.org/schema/pro/vis}Object) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element CreationDate ({http://euclid.esa.org/schema/pro/vis}CreationDate) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element ULDec ({http://euclid.esa.org/schema/pro/vis}ULDec) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element IsValid ({http://euclid.esa.org/schema/pro/vis}IsValid) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/pro/vis}ExtObjectId) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element LLRa ({http://euclid.esa.org/schema/pro/vis}LLRa) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}InputAssociateList uses Python identifier InputAssociateList
    __InputAssociateList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InputAssociateList'), 'InputAssociateList', '__httpeuclid_esa_orgschemaprovis_associateList_httpeuclid_esa_orgschemaprovisInputAssociateList', False)

    
    InputAssociateList = property(__InputAssociateList.value, __InputAssociateList.set, None, u' Information about the input\n                                associations [None] ')

    
    # Element LRDec ({http://euclid.esa.org/schema/pro/vis}LRDec) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaprovis_associateList_httpeuclid_esa_orgschemaprovisProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')


    _ElementMap = baseList._ElementMap.copy()
    _ElementMap.update({
        __SourceLists.name() : __SourceLists,
        __Associates.name() : __Associates,
        __AssociateListType.name() : __AssociateListType,
        __Alid.name() : __Alid,
        __AssociateCount.name() : __AssociateCount,
        __InputAssociateList.name() : __InputAssociateList,
        __ProcessParams.name() : __ProcessParams
    })
    _AttributeMap = baseList._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'associateList', associateList)


# Complex type rawBiasFrame with content type ELEMENT_ONLY
class rawBiasFrame (rawFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawBiasFrame')
    # Base type is rawFrame
    
    # Element Ovscx ({http://euclid.esa.org/schema/pro/vis}Ovscx) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Object ({http://euclid.esa.org/schema/pro/vis}Object) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Ovscy ({http://euclid.esa.org/schema/pro/vis}Ovscy) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Date ({http://euclid.esa.org/schema/pro/vis}Date) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element OverscanXStat ({http://euclid.esa.org/schema/pro/vis}OverscanXStat) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Prscxpre ({http://euclid.esa.org/schema/pro/vis}Prscxpre) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Template ({http://euclid.esa.org/schema/pro/vis}Template) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscypre ({http://euclid.esa.org/schema/pro/vis}Prscypre) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Ovscxpre ({http://euclid.esa.org/schema/pro/vis}Ovscxpre) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ObsBlock ({http://euclid.esa.org/schema/pro/vis}ObsBlock) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element PrescanYStat ({http://euclid.esa.org/schema/pro/vis}PrescanYStat) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element DateObs ({http://euclid.esa.org/schema/pro/vis}DateObs) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element MjdObs ({http://euclid.esa.org/schema/pro/vis}MjdObs) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element OverscanYStat ({http://euclid.esa.org/schema/pro/vis}OverscanYStat) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Prscxpst ({http://euclid.esa.org/schema/pro/vis}Prscxpst) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Lst ({http://euclid.esa.org/schema/pro/vis}Lst) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Prscypst ({http://euclid.esa.org/schema/pro/vis}Prscypst) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Utc ({http://euclid.esa.org/schema/pro/vis}Utc) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Ovscxpst ({http://euclid.esa.org/schema/pro/vis}Ovscxpst) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Ovscypst ({http://euclid.esa.org/schema/pro/vis}Ovscypst) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Ovscypre ({http://euclid.esa.org/schema/pro/vis}Ovscypre) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Extension ({http://euclid.esa.org/schema/pro/vis}Extension) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Prscy ({http://euclid.esa.org/schema/pro/vis}Prscy) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element Prscx ({http://euclid.esa.org/schema/pro/vis}Prscx) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element PrescanXStat ({http://euclid.esa.org/schema/pro/vis}PrescanXStat) inherited from {http://euclid.esa.org/schema/pro/vis}rawFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame

    _ElementMap = rawFrame._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = rawFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'rawBiasFrame', rawBiasFrame)


# Complex type readNoiseParameters with content type ELEMENT_ONLY
class readNoiseParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'readNoiseParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumReadNoiseDifference uses Python identifier MaximumReadNoiseDifference
    __MaximumReadNoiseDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumReadNoiseDifference'), 'MaximumReadNoiseDifference', '__httpeuclid_esa_orgschemaprovis_readNoiseParameters_httpeuclid_esa_orgschemaprovisMaximumReadNoiseDifference', False)

    
    MaximumReadNoiseDifference = property(__MaximumReadNoiseDifference.value, __MaximumReadNoiseDifference.set, None, u' QC: Maximum difference between readout\n                        noise measurements relative to the previous version\n                        [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}RejectionThreshold uses Python identifier RejectionThreshold
    __RejectionThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold'), 'RejectionThreshold', '__httpeuclid_esa_orgschemaprovis_readNoiseParameters_httpeuclid_esa_orgschemaprovisRejectionThreshold', False)

    
    RejectionThreshold = property(__RejectionThreshold.value, __RejectionThreshold.set, None, u' Threshold for rejecting pixels with\n                        outlying values [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumReadNoise uses Python identifier MaximumReadNoise
    __MaximumReadNoise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumReadNoise'), 'MaximumReadNoise', '__httpeuclid_esa_orgschemaprovis_readNoiseParameters_httpeuclid_esa_orgschemaprovisMaximumReadNoise', False)

    
    MaximumReadNoise = property(__MaximumReadNoise.value, __MaximumReadNoise.set, None, u' QC: Maximum value for the readout noise\n                        [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaprovis_readNoiseParameters_httpeuclid_esa_orgschemaprovisSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumBiasDifference uses Python identifier MaximumBiasDifference
    __MaximumBiasDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumBiasDifference'), 'MaximumBiasDifference', '__httpeuclid_esa_orgschemaprovis_readNoiseParameters_httpeuclid_esa_orgschemaprovisMaximumBiasDifference', False)

    
    MaximumBiasDifference = property(__MaximumBiasDifference.value, __MaximumBiasDifference.set, None, u' QC: Maximum mean pixel value difference\n                        between biases [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumIterations uses Python identifier MaximumIterations
    __MaximumIterations = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations'), 'MaximumIterations', '__httpeuclid_esa_orgschemaprovis_readNoiseParameters_httpeuclid_esa_orgschemaprovisMaximumIterations', False)

    
    MaximumIterations = property(__MaximumIterations.value, __MaximumIterations.set, None, u' Maximum number of iterations for\n                        estimating statistics [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_readNoiseParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __MaximumReadNoiseDifference.name() : __MaximumReadNoiseDifference,
        __RejectionThreshold.name() : __RejectionThreshold,
        __MaximumReadNoise.name() : __MaximumReadNoise,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __MaximumBiasDifference.name() : __MaximumBiasDifference,
        __MaximumIterations.name() : __MaximumIterations,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'readNoiseParameters', readNoiseParameters)


# Complex type illuminationCorrectionFrame with content type ELEMENT_ONLY
class illuminationCorrectionFrame (visBaseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminationCorrectionFrame')
    # Base type is visBaseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}IlluminationCorrection uses Python identifier IlluminationCorrection
    __IlluminationCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IlluminationCorrection'), 'IlluminationCorrection', '__httpeuclid_esa_orgschemaprovis_illuminationCorrectionFrame_httpeuclid_esa_orgschemaprovisIlluminationCorrection', False)

    
    IlluminationCorrection = property(__IlluminationCorrection.value, __IlluminationCorrection.set, None, u' Information about the\n                                illumination correction [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame

    _ElementMap = visBaseFrame._ElementMap.copy()
    _ElementMap.update({
        __IlluminationCorrection.name() : __IlluminationCorrection
    })
    _AttributeMap = visBaseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'illuminationCorrectionFrame', illuminationCorrectionFrame)


# Complex type weightFrame with content type ELEMENT_ONLY
class weightFrame (visBaseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'weightFrame')
    # Base type is visBaseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}Naxis1 uses Python identifier Naxis1_
    __Naxis1_ = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Naxis1'), 'Naxis1_', '__httpeuclid_esa_orgschemaprovis_weightFrame_httpeuclid_esa_orgschemaprovisNaxis1', False)

    
    Naxis1_ = property(__Naxis1_.value, __Naxis1_.set, None, u' Length of data in axis 1 [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Naxis2 uses Python identifier Naxis2_
    __Naxis2_ = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Naxis2'), 'Naxis2_', '__httpeuclid_esa_orgschemaprovis_weightFrame_httpeuclid_esa_orgschemaprovisNaxis2', False)

    
    Naxis2_ = property(__Naxis2_.value, __Naxis2_.set, None, u' Length of data in axis 2 [pixel] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/vis}ImStat uses Python identifier ImStat_
    __ImStat_ = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImStat'), 'ImStat_', '__httpeuclid_esa_orgschemaprovis_weightFrame_httpeuclid_esa_orgschemaprovisImStat', False)

    
    ImStat_ = property(__ImStat_.value, __ImStat_.set, None, u' Information about the statistics\n                                of the image pixels [None] ')

    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame

    _ElementMap = visBaseFrame._ElementMap.copy()
    _ElementMap.update({
        __Naxis1_.name() : __Naxis1_,
        __Naxis2_.name() : __Naxis2_,
        __ImStat_.name() : __ImStat_
    })
    _AttributeMap = visBaseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'weightFrame', weightFrame)


# Complex type CTD_ANON_ with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Location'), 'Location', '__httpeuclid_esa_orgschemaprovis_CTD_ANON__httpeuclid_esa_orgschemaprovisLocation', False)

    
    Location = property(__Location.value, __Location.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemaprovis_CTD_ANON__httpeuclid_esa_orgschemaprovisValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Location.name() : __Location,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_2 with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Location'), 'Location', '__httpeuclid_esa_orgschemaprovis_CTD_ANON_2_httpeuclid_esa_orgschemaprovisLocation', False)

    
    Location = property(__Location.value, __Location.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemaprovis_CTD_ANON_2_httpeuclid_esa_orgschemaprovisValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Location.name() : __Location,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }



# Complex type pixelMap with content type ELEMENT_ONLY
class pixelMap (visBaseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pixelMap')
    # Base type is visBaseFrame
    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = visBaseFrame._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = visBaseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'pixelMap', pixelMap)


# Complex type cosmicMap with content type ELEMENT_ONLY
class cosmicMap (pixelMap):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cosmicMap')
    # Base type is pixelMap
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Illumination uses Python identifier Illumination
    __Illumination = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), 'Illumination', '__httpeuclid_esa_orgschemaprovis_cosmicMap_httpeuclid_esa_orgschemaprovisIllumination', False)

    
    Illumination = property(__Illumination.value, __Illumination.set, None, u' Information about the\n                                illumination correction [None] ')

    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Gain uses Python identifier Gain
    __Gain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Gain'), 'Gain', '__httpeuclid_esa_orgschemaprovis_cosmicMap_httpeuclid_esa_orgschemaprovisGain', False)

    
    Gain = property(__Gain.value, __Gain.set, None, u' Information about the detector\n                                gain [None] ')

    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}Instrument uses Python identifier Instrument_
    __Instrument_ = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument_', '__httpeuclid_esa_orgschemaprovis_cosmicMap_httpeuclid_esa_orgschemaprovisInstrument', False)

    
    Instrument_ = property(__Instrument_.value, __Instrument_.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}Flat uses Python identifier Flat
    __Flat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flat'), 'Flat', '__httpeuclid_esa_orgschemaprovis_cosmicMap_httpeuclid_esa_orgschemaprovisFlat', False)

    
    Flat = property(__Flat.value, __Flat.set, None, u' Information about the detector\n                                sensitivity variations [None] ')

    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaprovis_cosmicMap_httpeuclid_esa_orgschemaprovisProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element {http://euclid.esa.org/schema/pro/vis}CosmicCount uses Python identifier CosmicCount
    __CosmicCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CosmicCount'), 'CosmicCount', '__httpeuclid_esa_orgschemaprovis_cosmicMap_httpeuclid_esa_orgschemaprovisCosmicCount', False)

    
    CosmicCount = property(__CosmicCount.value, __CosmicCount.set, None, u' Number of cosmic ray events (not\n                                affected pixels) [None] ')

    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}Frame uses Python identifier Frame
    __Frame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Frame'), 'Frame', '__httpeuclid_esa_orgschemaprovis_cosmicMap_httpeuclid_esa_orgschemaprovisFrame', False)

    
    Frame = property(__Frame.value, __Frame.set, None, u' Information about the input\n                                reduced science frame [None] ')

    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame

    _ElementMap = pixelMap._ElementMap.copy()
    _ElementMap.update({
        __Illumination.name() : __Illumination,
        __Gain.name() : __Gain,
        __Instrument_.name() : __Instrument_,
        __Flat.name() : __Flat,
        __ProcessParams.name() : __ProcessParams,
        __CosmicCount.name() : __CosmicCount,
        __Frame.name() : __Frame
    })
    _AttributeMap = pixelMap._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'cosmicMap', cosmicMap)


# Complex type gainLinearity with content type ELEMENT_ONLY
class gainLinearity (euclid.dm.bas.img_stub.processTargetDataObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'gainLinearity')
    # Base type is euclid.dm.bas.img_stub.processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/vis}RawFlatFrames uses Python identifier RawFlatFrames
    __RawFlatFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawFlatFrames'), 'RawFlatFrames', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisRawFlatFrames', True)

    
    RawFlatFrames = property(__RawFlatFrames.value, __RawFlatFrames.set, None, u' List of input raw  flat\n                                frames [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExposureTimes uses Python identifier ExposureTimes
    __ExposureTimes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureTimes'), 'ExposureTimes', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisExposureTimes', True)

    
    ExposureTimes = property(__ExposureTimes.value, __ExposureTimes.set, None, u' List of exposure times of the flat frames [second] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/vis}Bias uses Python identifier Bias
    __Bias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Bias'), 'Bias', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisBias', False)

    
    Bias = property(__Bias.value, __Bias.set, None, u' Information about the detector\n                                bias offset levels [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}RmsDiff uses Python identifier RmsDiff
    __RmsDiff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RmsDiff'), 'RmsDiff', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisRmsDiff', True)

    
    RmsDiff = property(__RmsDiff.value, __RmsDiff.set, None, u' List of raw measurements of\n                                sample standard deviation of pixel values of the\n                                subtracted dome flat frames [ADU] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}Gain uses Python identifier Gain
    __Gain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Gain'), 'Gain', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisGain', False)

    
    Gain = property(__Gain.value, __Gain.set, None, u' Value of the gain measurement\n                                (ADU conversion factor) [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}MedianSum uses Python identifier MedianSum
    __MedianSum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MedianSum'), 'MedianSum', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisMedianSum', True)

    
    MedianSum = property(__MedianSum.value, __MedianSum.set, None, u' List of raw measurements of\n                                median pixel values of the added dome flat\n                                frames [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExposureLevels uses Python identifier ExposureLevels
    __ExposureLevels = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureLevels'), 'ExposureLevels', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisExposureLevels', True)

    
    ExposureLevels = property(__ExposureLevels.value, __ExposureLevels.set, None, u' List of exposure levels (median\n                                pixel value of each flat frame) [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaprovis_gainLinearity_httpeuclid_esa_orgschemaprovisTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')


    _ElementMap = euclid.dm.bas.img_stub.processTargetDataObject._ElementMap.copy()
    _ElementMap.update({
        __RawFlatFrames.name() : __RawFlatFrames,
        __ObsBlock.name() : __ObsBlock,
        __Template.name() : __Template,
        __ExposureTimes.name() : __ExposureTimes,
        __TimestampStart.name() : __TimestampStart,
        __Chip.name() : __Chip,
        __Bias.name() : __Bias,
        __Instrument.name() : __Instrument,
        __RmsDiff.name() : __RmsDiff,
        __Gain.name() : __Gain,
        __ProcessParams.name() : __ProcessParams,
        __MedianSum.name() : __MedianSum,
        __ExposureLevels.name() : __ExposureLevels,
        __TimestampEnd.name() : __TimestampEnd
    })
    _AttributeMap = euclid.dm.bas.img_stub.processTargetDataObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'gainLinearity', gainLinearity)


# Complex type gainLinearityParameters with content type ELEMENT_ONLY
class gainLinearityParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'gainLinearityParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}OverscanCorrection uses Python identifier OverscanCorrection
    __OverscanCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), 'OverscanCorrection', '__httpeuclid_esa_orgschemaprovis_gainLinearityParameters_httpeuclid_esa_orgschemaprovisOverscanCorrection', False)

    
    OverscanCorrection = property(__OverscanCorrection.value, __OverscanCorrection.set, None, u' Overscan correction method index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumGainDifference uses Python identifier MaximumGainDifference
    __MaximumGainDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumGainDifference'), 'MaximumGainDifference', '__httpeuclid_esa_orgschemaprovis_gainLinearityParameters_httpeuclid_esa_orgschemaprovisMaximumGainDifference', False)

    
    MaximumGainDifference = property(__MaximumGainDifference.value, __MaximumGainDifference.set, None, u' QC: Maximum gain difference relative to\n                        the previous version [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}RejectionThreshold uses Python identifier RejectionThreshold
    __RejectionThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold'), 'RejectionThreshold', '__httpeuclid_esa_orgschemaprovis_gainLinearityParameters_httpeuclid_esa_orgschemaprovisRejectionThreshold', False)

    
    RejectionThreshold = property(__RejectionThreshold.value, __RejectionThreshold.set, None, u' Threshold for rejecting pixels with\n                        outlying values [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MinimumGain uses Python identifier MinimumGain
    __MinimumGain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinimumGain'), 'MinimumGain', '__httpeuclid_esa_orgschemaprovis_gainLinearityParameters_httpeuclid_esa_orgschemaprovisMinimumGain', False)

    
    MinimumGain = property(__MinimumGain.value, __MinimumGain.set, None, u' QC: Minimum gain [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_gainLinearityParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumIterations uses Python identifier MaximumIterations
    __MaximumIterations = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations'), 'MaximumIterations', '__httpeuclid_esa_orgschemaprovis_gainLinearityParameters_httpeuclid_esa_orgschemaprovisMaximumIterations', False)

    
    MaximumIterations = property(__MaximumIterations.value, __MaximumIterations.set, None, u' Maximum number of iterations for\n                        estimating statistics [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximimGain uses Python identifier MaximimGain
    __MaximimGain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximimGain'), 'MaximimGain', '__httpeuclid_esa_orgschemaprovis_gainLinearityParameters_httpeuclid_esa_orgschemaprovisMaximimGain', False)

    
    MaximimGain = property(__MaximimGain.value, __MaximimGain.set, None, u' QC: Maximum gain [electron / ADU] ')


    _ElementMap = {
        __OverscanCorrection.name() : __OverscanCorrection,
        __MaximumGainDifference.name() : __MaximumGainDifference,
        __RejectionThreshold.name() : __RejectionThreshold,
        __MinimumGain.name() : __MinimumGain,
        __ExtObjectId.name() : __ExtObjectId,
        __MaximumIterations.name() : __MaximumIterations,
        __MaximimGain.name() : __MaximimGain
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'gainLinearityParameters', gainLinearityParameters)


# Complex type cosmicMapParameters with content type ELEMENT_ONLY
class cosmicMapParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cosmicMapParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}DetectionThreshold uses Python identifier DetectionThreshold
    __DetectionThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectionThreshold'), 'DetectionThreshold', '__httpeuclid_esa_orgschemaprovis_cosmicMapParameters_httpeuclid_esa_orgschemaprovisDetectionThreshold', False)

    
    DetectionThreshold = property(__DetectionThreshold.value, __DetectionThreshold.set, None, u' Threshold for detecting pixels with\n                        cosmic ray events [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_cosmicMapParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __DetectionThreshold.name() : __DetectionThreshold,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cosmicMapParameters', cosmicMapParameters)


# Complex type sourceList with content type ELEMENT_ONLY
class sourceList (baseList):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceList')
    # Base type is baseList
    
    # Element URRa ({http://euclid.esa.org/schema/pro/vis}URRa) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}DetectionFrame uses Python identifier DetectionFrame
    __DetectionFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectionFrame'), 'DetectionFrame', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisDetectionFrame', False)

    
    DetectionFrame = property(__DetectionFrame.value, __DetectionFrame.set, None, u' Optional frame used to identify\n                                sources to be extracted (double image mode)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Slid uses Python identifier Slid
    __Slid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Slid'), 'Slid', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisSlid', False)

    
    Slid = property(__Slid.value, __Slid.set, None, u' Identifier of the source list\n                                [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/pro/vis}ExtObjectId) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}AssociateList uses Python identifier AssociateList
    __AssociateList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AssociateList'), 'AssociateList', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisAssociateList', False)

    
    AssociateList = property(__AssociateList.value, __AssociateList.set, None, u' ALID (associate list identifier)\n                                that was used to create this (combined) source\n                                list [None] ')

    
    # Element LLDec ({http://euclid.esa.org/schema/pro/vis}LLDec) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}Frame uses Python identifier Frame
    __Frame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Frame'), 'Frame', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisFrame', False)

    
    Frame = property(__Frame.value, __Frame.set, None, u' Information about the input frame\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Filters uses Python identifier Filters
    __Filters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filters'), 'Filters', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisFilters', False)

    
    Filters = property(__Filters.value, __Filters.set, None, u' Observational filters for which\n                                columns are present in this (combined) source\n                                list [None] ')

    
    # Element Name ({http://euclid.esa.org/schema/pro/vis}Name) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element CreationDate ({http://euclid.esa.org/schema/pro/vis}CreationDate) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element Object ({http://euclid.esa.org/schema/pro/vis}Object) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}SexParam uses Python identifier SexParam
    __SexParam = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexParam'), 'SexParam', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisSexParam', True)

    
    SexParam = property(__SexParam.value, __SexParam.set, None, u' List of parameters derived for\n                                each extracted source [None] ')

    
    # Element ULDec ({http://euclid.esa.org/schema/pro/vis}ULDec) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}CombineMethod uses Python identifier CombineMethod
    __CombineMethod = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CombineMethod'), 'CombineMethod', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisCombineMethod', False)

    
    CombineMethod = property(__CombineMethod.value, __CombineMethod.set, None, u' Method that was used to create\n                                this (combined) source list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/pro/vis}Storage) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element LRRa ({http://euclid.esa.org/schema/pro/vis}LRRa) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element LLRa ({http://euclid.esa.org/schema/pro/vis}LLRa) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceCount uses Python identifier SourceCount
    __SourceCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), 'SourceCount', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisSourceCount', False)

    
    SourceCount = property(__SourceCount.value, __SourceCount.set, None, u' Number of extracted sources\n                                [None] ')

    
    # Element URDec ({http://euclid.esa.org/schema/pro/vis}URDec) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}Sources uses Python identifier Sources
    __Sources = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sources'), 'Sources', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisSources', True)

    
    Sources = property(__Sources.value, __Sources.set, None, u' Column definitions of extracted\n                                sources [None] ')

    
    # Element LRDec ({http://euclid.esa.org/schema/pro/vis}LRDec) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element {http://euclid.esa.org/schema/pro/vis}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaprovis_sourceList_httpeuclid_esa_orgschemaprovisInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element ULRa ({http://euclid.esa.org/schema/pro/vis}ULRa) inherited from {http://euclid.esa.org/schema/pro/vis}baseList
    
    # Element IsValid ({http://euclid.esa.org/schema/pro/vis}IsValid) inherited from {http://euclid.esa.org/schema/pro/vis}baseList

    _ElementMap = baseList._ElementMap.copy()
    _ElementMap.update({
        __DetectionFrame.name() : __DetectionFrame,
        __Chip.name() : __Chip,
        __Slid.name() : __Slid,
        __AssociateList.name() : __AssociateList,
        __Frame.name() : __Frame,
        __Filters.name() : __Filters,
        __SexParam.name() : __SexParam,
        __CombineMethod.name() : __CombineMethod,
        __ProcessParams.name() : __ProcessParams,
        __Filter.name() : __Filter,
        __SourceCount.name() : __SourceCount,
        __Sources.name() : __Sources,
        __Instrument.name() : __Instrument
    })
    _AttributeMap = baseList._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sourceList', sourceList)


# Complex type CTICorrectionFrame with content type ELEMENT_ONLY
class CTICorrectionFrame (visBaseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CTICorrectionFrame')
    # Base type is visBaseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}CTIParameters uses Python identifier CTIParameters
    __CTIParameters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CTIParameters'), 'CTIParameters', '__httpeuclid_esa_orgschemaprovis_CTICorrectionFrame_httpeuclid_esa_orgschemaprovisCTIParameters', False)

    
    CTIParameters = property(__CTIParameters.value, __CTIParameters.set, None, u' Information about the\n                                illumination correction [None] ')

    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame

    _ElementMap = visBaseFrame._ElementMap.copy()
    _ElementMap.update({
        __CTIParameters.name() : __CTIParameters
    })
    _AttributeMap = visBaseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'CTICorrectionFrame', CTICorrectionFrame)


# Complex type CTICorrectionParameters with content type ELEMENT_ONLY
class CTICorrectionParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CTICorrectionParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}AOCS uses Python identifier AOCS
    __AOCS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AOCS'), 'AOCS', '__httpeuclid_esa_orgschemaprovis_CTICorrectionParameters_httpeuclid_esa_orgschemaprovisAOCS', False)

    
    AOCS = property(__AOCS.value, __AOCS.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}Temperature uses Python identifier Temperature
    __Temperature = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Temperature'), 'Temperature', '__httpeuclid_esa_orgschemaprovis_CTICorrectionParameters_httpeuclid_esa_orgschemaprovisTemperature', False)

    
    Temperature = property(__Temperature.value, __Temperature.set, None, None)


    _ElementMap = {
        __AOCS.name() : __AOCS,
        __Temperature.name() : __Temperature
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CTICorrectionParameters', CTICorrectionParameters)


# Complex type astrometricParameters with content type ELEMENT_ONLY
class astrometricParameters (euclid.dm.bas.img_stub.processTarget):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'astrometricParameters')
    # Base type is euclid.dm.bas.img_stub.processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_5 uses Python identifier PV2_5
    __PV2_5 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_5'), 'PV2_5', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_5', False)

    
    PV2_5 = property(__PV2_5.value, __PV2_5.set, None, u' Non-linear transformation matrix\n                                parameter value d1,5 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_8 uses Python identifier PV1_8
    __PV1_8 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_8'), 'PV1_8', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_8', False)

    
    PV1_8 = property(__PV1_8.value, __PV1_8.set, None, u' Non-linear transformation matrix\n                                parameter value b1,8 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MeanDdecOverlap uses Python identifier MeanDdecOverlap
    __MeanDdecOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MeanDdecOverlap'), 'MeanDdecOverlap', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisMeanDdecOverlap', False)

    
    MeanDdecOverlap = property(__MeanDdecOverlap.value, __MeanDdecOverlap.set, None, u' Average overlap residual in\n                                declination [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}NOverlap uses Python identifier NOverlap
    __NOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NOverlap'), 'NOverlap', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisNOverlap', False)

    
    NOverlap = property(__NOverlap.value, __NOverlap.set, None, u' Number of overlap pairings used\n                                in the astrometric solution [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CRPIX2 uses Python identifier CRPIX2
    __CRPIX2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRPIX2'), 'CRPIX2', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisCRPIX2', False)

    
    CRPIX2 = property(__CRPIX2.value, __CRPIX2.set, None, u' Reference pixel in Y [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_10 uses Python identifier PV1_10
    __PV1_10 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_10'), 'PV1_10', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_10', False)

    
    PV1_10 = property(__PV1_10.value, __PV1_10.set, None, u' Non-linear transformation matrix\n                                parameter value b1,10 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MeanDra uses Python identifier MeanDra
    __MeanDra = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MeanDra'), 'MeanDra', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisMeanDra', False)

    
    MeanDra = property(__MeanDra.value, __MeanDra.set, None, u' Average reference residual in\n                                right ascension [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FitErrors uses Python identifier FitErrors
    __FitErrors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FitErrors'), 'FitErrors', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisFitErrors', True)

    
    FitErrors = property(__FitErrors.value, __FitErrors.set, None, u' Errors on fitted parameters [rad] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CRVAL1 uses Python identifier CRVAL1
    __CRVAL1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRVAL1'), 'CRVAL1', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisCRVAL1', False)

    
    CRVAL1 = property(__CRVAL1.value, __CRVAL1.set, None, u' Physical value of the reference\n                                pixel X [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SigmaDra uses Python identifier SigmaDra
    __SigmaDra = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaDra'), 'SigmaDra', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisSigmaDra', False)

    
    SigmaDra = property(__SigmaDra.value, __SigmaDra.set, None, u' Sample standard deviation of\n                                reference residuals in right ascension [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_2 uses Python identifier PV1_2
    __PV1_2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_2'), 'PV1_2', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_2', False)

    
    PV1_2 = property(__PV1_2.value, __PV1_2.set, None, u' Non-linear transformation matrix\n                                parameter value b1,2 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_6 uses Python identifier PV1_6
    __PV1_6 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_6'), 'PV1_6', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_6', False)

    
    PV1_6 = property(__PV1_6.value, __PV1_6.set, None, u' Non-linear transformation matrix\n                                parameter value b1,6 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_2 uses Python identifier PV2_2
    __PV2_2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_2'), 'PV2_2', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_2', False)

    
    PV2_2 = property(__PV2_2.value, __PV2_2.set, None, u' Non-linear transformation matrix\n                                parameter value d1,2 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CTYPE1 uses Python identifier CTYPE1
    __CTYPE1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CTYPE1'), 'CTYPE1', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisCTYPE1', False)

    
    CTYPE1 = property(__CTYPE1.value, __CTYPE1.set, None, u' Pixel coordinate system and\n                                projection of first axis (X) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_9 uses Python identifier PV2_9
    __PV2_9 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_9'), 'PV2_9', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_9', False)

    
    PV2_9 = property(__PV2_9.value, __PV2_9.set, None, u' Non-linear transformation matrix\n                                parameter value d1,9 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SigmaDdec uses Python identifier SigmaDdec
    __SigmaDdec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaDdec'), 'SigmaDdec', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisSigmaDdec', False)

    
    SigmaDdec = property(__SigmaDdec.value, __SigmaDdec.set, None, u' Sample standard deviation of\n                                reference residuals in declination [arcsec] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_0 uses Python identifier PV1_0
    __PV1_0 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_0'), 'PV1_0', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_0', False)

    
    PV1_0 = property(__PV1_0.value, __PV1_0.set, None, u' Non-linear transformation matrix\n                                parameter value a0 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_9 uses Python identifier PV1_9
    __PV1_9 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_9'), 'PV1_9', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_9', False)

    
    PV1_9 = property(__PV1_9.value, __PV1_9.set, None, u' Non-linear transformation matrix\n                                parameter value b1,9 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CRPIX1 uses Python identifier CRPIX1
    __CRPIX1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRPIX1'), 'CRPIX1', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisCRPIX1', False)

    
    CRPIX1 = property(__CRPIX1.value, __CRPIX1.set, None, u' Reference pixel in X [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_4 uses Python identifier PV1_4
    __PV1_4 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_4'), 'PV1_4', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_4', False)

    
    PV1_4 = property(__PV1_4.value, __PV1_4.set, None, u' Non-linear transformation matrix\n                                parameter value b1,4 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FieldError uses Python identifier FieldError
    __FieldError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FieldError'), 'FieldError', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisFieldError', False)

    
    FieldError = property(__FieldError.value, __FieldError.set, None, u' Global position error [arcsec] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}NRef uses Python identifier NRef
    __NRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NRef'), 'NRef', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisNRef', False)

    
    NRef = property(__NRef.value, __NRef.set, None, u' Number of reference pairings used\n                                in the astrometric solution [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_4 uses Python identifier PV2_4
    __PV2_4 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_4'), 'PV2_4', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_4', False)

    
    PV2_4 = property(__PV2_4.value, __PV2_4.set, None, u' Non-linear transformation matrix\n                                parameter value d1,4 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Rms uses Python identifier Rms
    __Rms = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Rms'), 'Rms', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisRms', False)

    
    Rms = property(__Rms.value, __Rms.set, None, u' Two-dimensional root-mean-square\n                                of reference residuals [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CRVAL2 uses Python identifier CRVAL2
    __CRVAL2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRVAL2'), 'CRVAL2', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisCRVAL2', False)

    
    CRVAL2 = property(__CRVAL2.value, __CRVAL2.set, None, u' Physical value of the reference\n                                pixel Y [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}XError uses Python identifier XError
    __XError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XError'), 'XError', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisXError', False)

    
    XError = property(__XError.value, __XError.set, None, u' Error in polynomial X coefficient\n                                [arcsec] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}RefcatSlid uses Python identifier RefcatSlid
    __RefcatSlid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RefcatSlid'), 'RefcatSlid', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisRefcatSlid', False)

    
    RefcatSlid = property(__RefcatSlid.value, __RefcatSlid.set, None, u' The ID of the source list used\n                                for the reference catalog [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Residuals uses Python identifier Residuals
    __Residuals = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Residuals'), 'Residuals', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisResiduals', False)

    
    Residuals = property(__Residuals.value, __Residuals.set, None, u' Filename of residuals FITS table\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}YyError uses Python identifier YyError
    __YyError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YyError'), 'YyError', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisYyError', False)

    
    YyError = property(__YyError.value, __YyError.set, None, u' Error in polynomial YY\n                                coefficient [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CD1_1 uses Python identifier CD1_1
    __CD1_1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD1_1'), 'CD1_1', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisCD1_1', False)

    
    CD1_1 = property(__CD1_1.value, __CD1_1.set, None, u' Linear transformation matrix\n                                parameter at i,j=1,1 (a1) [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}YError uses Python identifier YError
    __YError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YError'), 'YError', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisYError', False)

    
    YError = property(__YError.value, __YError.set, None, u' Error in polynomial Y coefficient\n                                [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CTYPE2 uses Python identifier CTYPE2
    __CTYPE2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CTYPE2'), 'CTYPE2', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisCTYPE2', False)

    
    CTYPE2 = property(__CTYPE2.value, __CTYPE2.set, None, u' Pixel coordinate system and\n                                projection of second axis (Y) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_7 uses Python identifier PV1_7
    __PV1_7 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_7'), 'PV1_7', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_7', False)

    
    PV1_7 = property(__PV1_7.value, __PV1_7.set, None, u' Non-linear transformation matrix\n                                parameter value b1,7 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Seeing uses Python identifier Seeing
    __Seeing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), 'Seeing', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisSeeing', False)

    
    Seeing = property(__Seeing.value, __Seeing.set, None, u' Estimate of seeing using the\n                                median FWHM (filtered to isolate most\n                                stellar-like sources) [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_7 uses Python identifier PV2_7
    __PV2_7 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_7'), 'PV2_7', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_7', False)

    
    PV2_7 = property(__PV2_7.value, __PV2_7.set, None, u' Non-linear transformation matrix\n                                parameter value d1,7 [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}CD2_1 uses Python identifier CD2_1
    __CD2_1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD2_1'), 'CD2_1', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisCD2_1', False)

    
    CD2_1 = property(__CD2_1.value, __CD2_1.set, None, u' Linear transformation matrix\n                                parameter at i,j=2,1 (b1) [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_3 uses Python identifier PV1_3
    __PV1_3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_3'), 'PV1_3', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_3', False)

    
    PV1_3 = property(__PV1_3.value, __PV1_3.set, None, u' Non-linear transformation matrix\n                                parameter value b1,3 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_1 uses Python identifier PV2_1
    __PV2_1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_1'), 'PV2_1', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_1', False)

    
    PV2_1 = property(__PV2_1.value, __PV2_1.set, None, u' Non-linear transformation matrix\n                                parameter value d1,1 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FitParams uses Python identifier FitParams
    __FitParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FitParams'), 'FitParams', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisFitParams', True)

    
    FitParams = property(__FitParams.value, __FitParams.set, None, u' Degrees of freedom of fitted\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}XyError uses Python identifier XyError
    __XyError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XyError'), 'XyError', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisXyError', False)

    
    XyError = property(__XyError.value, __XyError.set, None, u' Error in polynomial XY\n                                coefficient [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_1 uses Python identifier PV1_1
    __PV1_1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_1'), 'PV1_1', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_1', False)

    
    PV1_1 = property(__PV1_1.value, __PV1_1.set, None, u' Non-linear transformation matrix\n                                parameter value b1,1 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_8 uses Python identifier PV2_8
    __PV2_8 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_8'), 'PV2_8', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_8', False)

    
    PV2_8 = property(__PV2_8.value, __PV2_8.set, None, u' Non-linear transformation matrix\n                                parameter value d1,8 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SigmaDraOverlap uses Python identifier SigmaDraOverlap
    __SigmaDraOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaDraOverlap'), 'SigmaDraOverlap', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisSigmaDraOverlap', False)

    
    SigmaDraOverlap = property(__SigmaDraOverlap.value, __SigmaDraOverlap.set, None, u' Sample standard deviation of\n                                overlap residuals in right ascension [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_6 uses Python identifier PV2_6
    __PV2_6 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_6'), 'PV2_6', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_6', False)

    
    PV2_6 = property(__PV2_6.value, __PV2_6.set, None, u' Non-linear transformation matrix\n                                parameter value d1,6 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Reduced uses Python identifier Reduced
    __Reduced = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Reduced'), 'Reduced', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisReduced', False)

    
    Reduced = property(__Reduced.value, __Reduced.set, None, u' Information about the input\n                                reduced science frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV1_5 uses Python identifier PV1_5
    __PV1_5 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_5'), 'PV1_5', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV1_5', False)

    
    PV1_5 = property(__PV1_5.value, __PV1_5.set, None, u' Non-linear transformation matrix\n                                parameter value b1,5 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SigmaDdecOverlap uses Python identifier SigmaDdecOverlap
    __SigmaDdecOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaDdecOverlap'), 'SigmaDdecOverlap', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisSigmaDdecOverlap', False)

    
    SigmaDdecOverlap = property(__SigmaDdecOverlap.value, __SigmaDdecOverlap.set, None, u' Sample standard deviation of\n                                overlap residuals in declination [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CD2_2 uses Python identifier CD2_2
    __CD2_2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD2_2'), 'CD2_2', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisCD2_2', False)

    
    CD2_2 = property(__CD2_2.value, __CD2_2.set, None, u' Linear transformation matrix\n                                parameter at i,j=2,2 (b2) [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CD1_2 uses Python identifier CD1_2
    __CD1_2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD1_2'), 'CD1_2', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisCD1_2', False)

    
    CD1_2 = property(__CD1_2.value, __CD1_2.set, None, u' Linear transformation matrix\n                                parameter at i,j=1,2 (a2) [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MeanDdec uses Python identifier MeanDdec
    __MeanDdec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MeanDdec'), 'MeanDdec', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisMeanDdec', False)

    
    MeanDdec = property(__MeanDdec.value, __MeanDdec.set, None, u' Average reference residual in\n                                declination [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_3 uses Python identifier PV2_3
    __PV2_3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_3'), 'PV2_3', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_3', False)

    
    PV2_3 = property(__PV2_3.value, __PV2_3.set, None, u' Non-linear transformation matrix\n                                parameter value d1,3 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_0 uses Python identifier PV2_0
    __PV2_0 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_0'), 'PV2_0', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_0', False)

    
    PV2_0 = property(__PV2_0.value, __PV2_0.set, None, u' Non-linear transformation matrix\n                                parameter value c0 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MeanDraOverlap uses Python identifier MeanDraOverlap
    __MeanDraOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MeanDraOverlap'), 'MeanDraOverlap', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisMeanDraOverlap', False)

    
    MeanDraOverlap = property(__MeanDraOverlap.value, __MeanDraOverlap.set, None, u' Average overlap residual in right\n                                ascension [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}XxError uses Python identifier XxError
    __XxError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XxError'), 'XxError', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisXxError', False)

    
    XxError = property(__XxError.value, __XxError.set, None, u' Error in polynomial XX\n                                coefficient [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PV2_10 uses Python identifier PV2_10
    __PV2_10 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_10'), 'PV2_10', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisPV2_10', False)

    
    PV2_10 = property(__PV2_10.value, __PV2_10.set, None, u' Non-linear transformation matrix\n                                parameter value d1,10 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}RmsOverlap uses Python identifier RmsOverlap
    __RmsOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RmsOverlap'), 'RmsOverlap', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisRmsOverlap', False)

    
    RmsOverlap = property(__RmsOverlap.value, __RmsOverlap.set, None, u' Two-dimensional root-mean-square\n                                of overlap residuals [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}NFitParm uses Python identifier NFitParm
    __NFitParm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NFitParm'), 'NFitParm', '__httpeuclid_esa_orgschemaprovis_astrometricParameters_httpeuclid_esa_orgschemaprovisNFitParm', False)

    
    NFitParm = property(__NFitParm.value, __NFitParm.set, None, u' Number of fitted parameters\n                                [None] ')


    _ElementMap = euclid.dm.bas.img_stub.processTarget._ElementMap.copy()
    _ElementMap.update({
        __PV2_5.name() : __PV2_5,
        __PV1_8.name() : __PV1_8,
        __MeanDdecOverlap.name() : __MeanDdecOverlap,
        __NOverlap.name() : __NOverlap,
        __CRPIX2.name() : __CRPIX2,
        __PV1_10.name() : __PV1_10,
        __MeanDra.name() : __MeanDra,
        __FitErrors.name() : __FitErrors,
        __CRVAL1.name() : __CRVAL1,
        __SigmaDra.name() : __SigmaDra,
        __PV1_2.name() : __PV1_2,
        __Template.name() : __Template,
        __PV1_6.name() : __PV1_6,
        __PV2_2.name() : __PV2_2,
        __CTYPE1.name() : __CTYPE1,
        __PV2_9.name() : __PV2_9,
        __Instrument.name() : __Instrument,
        __SigmaDdec.name() : __SigmaDdec,
        __PV1_0.name() : __PV1_0,
        __PV1_9.name() : __PV1_9,
        __CRPIX1.name() : __CRPIX1,
        __PV1_4.name() : __PV1_4,
        __FieldError.name() : __FieldError,
        __NRef.name() : __NRef,
        __PV2_4.name() : __PV2_4,
        __Rms.name() : __Rms,
        __CRVAL2.name() : __CRVAL2,
        __XError.name() : __XError,
        __RefcatSlid.name() : __RefcatSlid,
        __Residuals.name() : __Residuals,
        __YyError.name() : __YyError,
        __CD1_1.name() : __CD1_1,
        __YError.name() : __YError,
        __CTYPE2.name() : __CTYPE2,
        __PV1_7.name() : __PV1_7,
        __Seeing.name() : __Seeing,
        __PV2_7.name() : __PV2_7,
        __CD2_1.name() : __CD2_1,
        __Chip.name() : __Chip,
        __PV1_3.name() : __PV1_3,
        __PV2_1.name() : __PV2_1,
        __FitParams.name() : __FitParams,
        __XyError.name() : __XyError,
        __PV1_1.name() : __PV1_1,
        __PV2_8.name() : __PV2_8,
        __SigmaDraOverlap.name() : __SigmaDraOverlap,
        __PV2_6.name() : __PV2_6,
        __Reduced.name() : __Reduced,
        __ObsBlock.name() : __ObsBlock,
        __PV1_5.name() : __PV1_5,
        __SigmaDdecOverlap.name() : __SigmaDdecOverlap,
        __CD2_2.name() : __CD2_2,
        __CD1_2.name() : __CD1_2,
        __MeanDdec.name() : __MeanDdec,
        __Filter.name() : __Filter,
        __PV2_3.name() : __PV2_3,
        __PV2_0.name() : __PV2_0,
        __MeanDraOverlap.name() : __MeanDraOverlap,
        __XxError.name() : __XxError,
        __PV2_10.name() : __PV2_10,
        __RmsOverlap.name() : __RmsOverlap,
        __NFitParm.name() : __NFitParm
    })
    _AttributeMap = euclid.dm.bas.img_stub.processTarget._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'astrometricParameters', astrometricParameters)


# Complex type sourceListDict with content type ELEMENT_ONLY
class sourceListDict (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceListDict')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}SLID uses Python identifier SLID
    __SLID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SLID'), 'SLID', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisSLID', False)

    
    SLID = property(__SLID.value, __SLID.set, None, u' Identifier of the source list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MAG_APER uses Python identifier MAG_APER
    __MAG_APER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_APER'), 'MAG_APER', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisMAG_APER', False)

    
    MAG_APER = property(__MAG_APER.value, __MAG_APER.set, None, u' Fixed aperture magnitude vector [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MAGERR_ISO uses Python identifier MAGERR_ISO
    __MAGERR_ISO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_ISO'), 'MAGERR_ISO', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisMAGERR_ISO', False)

    
    MAGERR_ISO = property(__MAGERR_ISO.value, __MAGERR_ISO.set, None, u' RMS error for isophotal magnitude [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaxVal uses Python identifier MaxVal
    __MaxVal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxVal'), 'MaxVal', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisMaxVal', False)

    
    MaxVal = property(__MaxVal.value, __MaxVal.set, None, u' Peak flux above background [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FLUX_ISO uses Python identifier FLUX_ISO
    __FLUX_ISO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUX_ISO'), 'FLUX_ISO', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisFLUX_ISO', False)

    
    FLUX_ISO = property(__FLUX_ISO.value, __FLUX_ISO.set, None, u' Isophotal flux [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SID uses Python identifier SID
    __SID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SID'), 'SID', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisSID', False)

    
    SID = property(__SID.value, __SID.set, None, u' Identifier of a source in the source list\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MAG_ISO uses Python identifier MAG_ISO
    __MAG_ISO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_ISO'), 'MAG_ISO', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisMAG_ISO', False)

    
    MAG_ISO = property(__MAG_ISO.value, __MAG_ISO.set, None, u' Isophotal magnitude [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ERRA_IMAGE uses Python identifier ERRA_IMAGE
    __ERRA_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ERRA_IMAGE'), 'ERRA_IMAGE', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisERRA_IMAGE', False)

    
    ERRA_IMAGE = property(__ERRA_IMAGE.value, __ERRA_IMAGE.set, None, u' Error on measurement of semi-major axis\n                        of profile [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}RA uses Python identifier RA
    __RA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RA'), 'RA', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisRA', False)

    
    RA = property(__RA.value, __RA.set, None, u' Right Ascension [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Ypos uses Python identifier Ypos
    __Ypos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ypos'), 'Ypos', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisYpos', False)

    
    Ypos = property(__Ypos.value, __Ypos.set, None, u' Source position along Y [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ERRB_IMAGE uses Python identifier ERRB_IMAGE
    __ERRB_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ERRB_IMAGE'), 'ERRB_IMAGE', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisERRB_IMAGE', False)

    
    ERRB_IMAGE = property(__ERRB_IMAGE.value, __ERRB_IMAGE.set, None, u' Error on measurement of semi-minor axis\n                        of profile [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}BackGr uses Python identifier BackGr
    __BackGr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BackGr'), 'BackGr', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisBackGr', False)

    
    BackGr = property(__BackGr.value, __BackGr.set, None, u' Background level around a source [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}DEC uses Python identifier DEC
    __DEC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEC'), 'DEC', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisDEC', False)

    
    DEC = property(__DEC.value, __DEC.set, None, u' Declination [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FLUXERR_ISO uses Python identifier FLUXERR_ISO
    __FLUXERR_ISO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_ISO'), 'FLUXERR_ISO', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisFLUXERR_ISO', False)

    
    FLUXERR_ISO = property(__FLUXERR_ISO.value, __FLUXERR_ISO.set, None, u' RMS error for isophotal flux [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ERRTHETA_IMAGE uses Python identifier ERRTHETA_IMAGE
    __ERRTHETA_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ERRTHETA_IMAGE'), 'ERRTHETA_IMAGE', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisERRTHETA_IMAGE', False)

    
    ERRTHETA_IMAGE = property(__ERRTHETA_IMAGE.value, __ERRTHETA_IMAGE.set, None, u' Error on measurement of ellipse position\n                        angle [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}HTM uses Python identifier HTM
    __HTM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HTM'), 'HTM', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisHTM', False)

    
    HTM = property(__HTM.value, __HTM.set, None, u' Index of HTM (Hierarchical Triangular\n                        Mesh) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SeqNr uses Python identifier SeqNr
    __SeqNr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SeqNr'), 'SeqNr', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisSeqNr', False)

    
    SeqNr = property(__SeqNr.value, __SeqNr.set, None, u' Index of extracted source [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FIELD_POS uses Python identifier FIELD_POS
    __FIELD_POS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FIELD_POS'), 'FIELD_POS', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisFIELD_POS', False)

    
    FIELD_POS = property(__FIELD_POS.value, __FIELD_POS.set, None, u' Observation index for multi-observation\n                        source lists [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Level uses Python identifier Level
    __Level = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Level'), 'Level', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisLevel', False)

    
    Level = property(__Level.value, __Level.set, None, u' Level of detection threshold above\n                        background [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}A uses Python identifier A
    __A = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'A'), 'A', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisA', False)

    
    A = property(__A.value, __A.set, None, u' Semi-major axis of profile [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}XM2 uses Python identifier XM2
    __XM2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XM2'), 'XM2', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisXM2', False)

    
    XM2 = property(__XM2.value, __XM2.set, None, u' Variance along X [pixel**2] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FLAG uses Python identifier FLAG
    __FLAG = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG'), 'FLAG', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisFLAG', False)

    
    FLAG = property(__FLAG.value, __FLAG.set, None, u' Source extraction flags [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MAG_AUTO uses Python identifier MAG_AUTO
    __MAG_AUTO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_AUTO'), 'MAG_AUTO', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisMAG_AUTO', False)

    
    MAG_AUTO = property(__MAG_AUTO.value, __MAG_AUTO.set, None, u' Kron-like elliptical aperture magnitude\n                        [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}B uses Python identifier B
    __B = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'B'), 'B', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisB', False)

    
    B = property(__B.value, __B.set, None, u' Semi-minor axis of profile [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FLUX_APER uses Python identifier FLUX_APER
    __FLUX_APER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUX_APER'), 'FLUX_APER', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisFLUX_APER', False)

    
    FLUX_APER = property(__FLUX_APER.value, __FLUX_APER.set, None, u' Flux vector within fixed circular\n                        aperture(s) [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Xpos uses Python identifier Xpos
    __Xpos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Xpos'), 'Xpos', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisXpos', False)

    
    Xpos = property(__Xpos.value, __Xpos.set, None, u' Source position along X [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}A_WCS uses Python identifier A_WCS
    __A_WCS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'A_WCS'), 'A_WCS', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisA_WCS', False)

    
    A_WCS = property(__A_WCS.value, __A_WCS.set, None, u' Semi-major axis of profile [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MAGERR_APER uses Python identifier MAGERR_APER
    __MAGERR_APER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_APER'), 'MAGERR_APER', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisMAGERR_APER', False)

    
    MAGERR_APER = property(__MAGERR_APER.value, __MAGERR_APER.set, None, u' RMS error vector for fixed aperture\n                        magnitude [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FLUX_AUTO uses Python identifier FLUX_AUTO
    __FLUX_AUTO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUX_AUTO'), 'FLUX_AUTO', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisFLUX_AUTO', False)

    
    FLUX_AUTO = property(__FLUX_AUTO.value, __FLUX_AUTO.set, None, u' Flux within a Kron-like elliptical\n                        aperture [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Corr uses Python identifier Corr
    __Corr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Corr'), 'Corr', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisCorr', False)

    
    Corr = property(__Corr.value, __Corr.set, None, u' Covariance between X and Y [pixel**2] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}B_WCS uses Python identifier B_WCS
    __B_WCS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'B_WCS'), 'B_WCS', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisB_WCS', False)

    
    B_WCS = property(__B_WCS.value, __B_WCS.set, None, u' Semi-minor axis of profile [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FLUXERR_AUTO uses Python identifier FLUXERR_AUTO
    __FLUXERR_AUTO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_AUTO'), 'FLUXERR_AUTO', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisFLUXERR_AUTO', False)

    
    FLUXERR_AUTO = property(__FLUXERR_AUTO.value, __FLUXERR_AUTO.set, None, u' RMS error for AUTO flux [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}YM2 uses Python identifier YM2
    __YM2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YM2'), 'YM2', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisYM2', False)

    
    YM2 = property(__YM2.value, __YM2.set, None, u' Variance along Y [pixel**2] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}PosErr uses Python identifier PosErr
    __PosErr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PosErr'), 'PosErr', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisPosErr', False)

    
    PosErr = property(__PosErr.value, __PosErr.set, None, u' Positional error of extraction (measured\n                        semi-major axis) [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MAGERR_AUTO uses Python identifier MAGERR_AUTO
    __MAGERR_AUTO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_AUTO'), 'MAGERR_AUTO', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisMAGERR_AUTO', False)

    
    MAGERR_AUTO = property(__MAGERR_AUTO.value, __MAGERR_AUTO.set, None, u' RMS error for AUTO magnitude [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}NPIX uses Python identifier NPIX
    __NPIX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NPIX'), 'NPIX', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisNPIX', False)

    
    NPIX = property(__NPIX.value, __NPIX.set, None, u' Isophotal area above analysis threshold\n                        [pixel**2] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FWHM_IMAGE uses Python identifier FWHM_IMAGE
    __FWHM_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FWHM_IMAGE'), 'FWHM_IMAGE', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisFWHM_IMAGE', False)

    
    FWHM_IMAGE = property(__FWHM_IMAGE.value, __FWHM_IMAGE.set, None, u' Full width at half maximum assuming a\n                        gaussian core [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FLUXERR_APER uses Python identifier FLUXERR_APER
    __FLUXERR_APER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_APER'), 'FLUXERR_APER', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisFLUXERR_APER', False)

    
    FLUXERR_APER = property(__FLUXERR_APER.value, __FLUXERR_APER.set, None, u' RMS error vector for aperture flux(es)\n                        [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FLUX_RADIUS uses Python identifier FLUX_RADIUS
    __FLUX_RADIUS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUX_RADIUS'), 'FLUX_RADIUS', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisFLUX_RADIUS', False)

    
    FLUX_RADIUS = property(__FLUX_RADIUS.value, __FLUX_RADIUS.set, None, u' Fraction-of-light radius [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MU_MAX uses Python identifier MU_MAX
    __MU_MAX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MU_MAX'), 'MU_MAX', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisMU_MAX', False)

    
    MU_MAX = property(__MU_MAX.value, __MU_MAX.set, None, u' Peak surface brightness above background\n                        [mag / arcsec**2] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CLASS_STAR uses Python identifier CLASS_STAR
    __CLASS_STAR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CLASS_STAR'), 'CLASS_STAR', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisCLASS_STAR', False)

    
    CLASS_STAR = property(__CLASS_STAR.value, __CLASS_STAR.set, None, u' Star/galaxy classifier index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}POSANG uses Python identifier POSANG
    __POSANG = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'POSANG'), 'POSANG', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisPOSANG', False)

    
    POSANG = property(__POSANG.value, __POSANG.set, None, u' Ellipse position angle [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}THETAWCS uses Python identifier THETAWCS
    __THETAWCS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'THETAWCS'), 'THETAWCS', '__httpeuclid_esa_orgschemaprovis_sourceListDict_httpeuclid_esa_orgschemaprovisTHETAWCS', False)

    
    THETAWCS = property(__THETAWCS.value, __THETAWCS.set, None, u' Ellipse position angle [deg] ')


    _ElementMap = {
        __SLID.name() : __SLID,
        __MAG_APER.name() : __MAG_APER,
        __MAGERR_ISO.name() : __MAGERR_ISO,
        __MaxVal.name() : __MaxVal,
        __FLUX_ISO.name() : __FLUX_ISO,
        __SID.name() : __SID,
        __MAG_ISO.name() : __MAG_ISO,
        __ERRA_IMAGE.name() : __ERRA_IMAGE,
        __RA.name() : __RA,
        __Ypos.name() : __Ypos,
        __ERRB_IMAGE.name() : __ERRB_IMAGE,
        __BackGr.name() : __BackGr,
        __DEC.name() : __DEC,
        __FLUXERR_ISO.name() : __FLUXERR_ISO,
        __ERRTHETA_IMAGE.name() : __ERRTHETA_IMAGE,
        __HTM.name() : __HTM,
        __SeqNr.name() : __SeqNr,
        __FIELD_POS.name() : __FIELD_POS,
        __Level.name() : __Level,
        __A.name() : __A,
        __XM2.name() : __XM2,
        __FLAG.name() : __FLAG,
        __MAG_AUTO.name() : __MAG_AUTO,
        __B.name() : __B,
        __FLUX_APER.name() : __FLUX_APER,
        __Xpos.name() : __Xpos,
        __A_WCS.name() : __A_WCS,
        __MAGERR_APER.name() : __MAGERR_APER,
        __FLUX_AUTO.name() : __FLUX_AUTO,
        __Corr.name() : __Corr,
        __B_WCS.name() : __B_WCS,
        __FLUXERR_AUTO.name() : __FLUXERR_AUTO,
        __YM2.name() : __YM2,
        __PosErr.name() : __PosErr,
        __MAGERR_AUTO.name() : __MAGERR_AUTO,
        __NPIX.name() : __NPIX,
        __FWHM_IMAGE.name() : __FWHM_IMAGE,
        __FLUXERR_APER.name() : __FLUXERR_APER,
        __FLUX_RADIUS.name() : __FLUX_RADIUS,
        __MU_MAX.name() : __MU_MAX,
        __CLASS_STAR.name() : __CLASS_STAR,
        __POSANG.name() : __POSANG,
        __THETAWCS.name() : __THETAWCS
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sourceListDict', sourceListDict)


# Complex type masterFlatFrameParameters with content type ELEMENT_ONLY
class masterFlatFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'masterFlatFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}MirrorYpix uses Python identifier MirrorYpix
    __MirrorYpix = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MirrorYpix'), 'MirrorYpix', '__httpeuclid_esa_orgschemaprovis_masterFlatFrameParameters_httpeuclid_esa_orgschemaprovisMirrorYpix', False)

    
    MirrorYpix = property(__MirrorYpix.value, __MirrorYpix.set, None, u' Number of pixels to mirror beyond the Y\n                        edges of the detector to provide Fourier transform\n                        continuity [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaprovis_masterFlatFrameParameters_httpeuclid_esa_orgschemaprovisSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}DigFilterSize uses Python identifier DigFilterSize
    __DigFilterSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DigFilterSize'), 'DigFilterSize', '__httpeuclid_esa_orgschemaprovis_masterFlatFrameParameters_httpeuclid_esa_orgschemaprovisDigFilterSize', False)

    
    DigFilterSize = property(__DigFilterSize.value, __DigFilterSize.set, None, u' Gaussian Fourier filter size [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MedianFilterSize uses Python identifier MedianFilterSize
    __MedianFilterSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MedianFilterSize'), 'MedianFilterSize', '__httpeuclid_esa_orgschemaprovis_masterFlatFrameParameters_httpeuclid_esa_orgschemaprovisMedianFilterSize', False)

    
    MedianFilterSize = property(__MedianFilterSize.value, __MedianFilterSize.set, None, u' Size of the median cleaning filter\n                        [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MirrorXpix uses Python identifier MirrorXpix
    __MirrorXpix = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MirrorXpix'), 'MirrorXpix', '__httpeuclid_esa_orgschemaprovis_masterFlatFrameParameters_httpeuclid_esa_orgschemaprovisMirrorXpix', False)

    
    MirrorXpix = property(__MirrorXpix.value, __MirrorXpix.set, None, u' Number of pixels to mirror beyond the X\n                        edges of the detector to provide Fourier transform\n                        continuity [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}CombineType uses Python identifier CombineType
    __CombineType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CombineType'), 'CombineType', '__httpeuclid_esa_orgschemaprovis_masterFlatFrameParameters_httpeuclid_esa_orgschemaprovisCombineType', False)

    
    CombineType = property(__CombineType.value, __CombineType.set, None, u' Index for the type of input (some\n                        combination of dome and/or twilight flat frame) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_masterFlatFrameParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __MirrorYpix.name() : __MirrorYpix,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __DigFilterSize.name() : __DigFilterSize,
        __MedianFilterSize.name() : __MedianFilterSize,
        __MirrorXpix.name() : __MirrorXpix,
        __CombineType.name() : __CombineType,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'masterFlatFrameParameters', masterFlatFrameParameters)


# Complex type sourceListParameters with content type ELEMENT_ONLY
class sourceListParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceListParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaprovis_sourceListParameters_httpeuclid_esa_orgschemaprovisSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}HtmDepth uses Python identifier HtmDepth
    __HtmDepth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HtmDepth'), 'HtmDepth', '__httpeuclid_esa_orgschemaprovis_sourceListParameters_httpeuclid_esa_orgschemaprovisHtmDepth', False)

    
    HtmDepth = property(__HtmDepth.value, __HtmDepth.set, None, u' Highest level of HTM indexing [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_sourceListParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __HtmDepth.name() : __HtmDepth,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sourceListParameters', sourceListParameters)


# Complex type illuminationCorrectionRecord with content type ELEMENT_ONLY
class illuminationCorrectionRecord (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminationCorrectionRecord')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}FitParameters uses Python identifier FitParameters
    __FitParameters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FitParameters'), 'FitParameters', '__httpeuclid_esa_orgschemaprovis_illuminationCorrectionRecord_httpeuclid_esa_orgschemaprovisFitParameters', True)

    
    FitParameters = property(__FitParameters.value, __FitParameters.set, None, u' List of fit parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ChipName uses Python identifier ChipName
    __ChipName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ChipName'), 'ChipName', '__httpeuclid_esa_orgschemaprovis_illuminationCorrectionRecord_httpeuclid_esa_orgschemaprovisChipName', False)

    
    ChipName = property(__ChipName.value, __ChipName.set, None, u' Name of the detector chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_illuminationCorrectionRecord_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __FitParameters.name() : __FitParameters,
        __ChipName.name() : __ChipName,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'illuminationCorrectionRecord', illuminationCorrectionRecord)


# Complex type reducedScienceFrameParameters with content type ELEMENT_ONLY
class reducedScienceFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reducedScienceFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}OverscanCorrection uses Python identifier OverscanCorrection
    __OverscanCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), 'OverscanCorrection', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrameParameters_httpeuclid_esa_orgschemaprovisOverscanCorrection', False)

    
    OverscanCorrection = property(__OverscanCorrection.value, __OverscanCorrection.set, None, u' Overscan correction method index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ImageThreshold uses Python identifier ImageThreshold
    __ImageThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImageThreshold'), 'ImageThreshold', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrameParameters_httpeuclid_esa_orgschemaprovisImageThreshold', False)

    
    ImageThreshold = property(__ImageThreshold.value, __ImageThreshold.set, None, u' Pixel value Sigma-clipping threshold to\n                        estimate source-free background for scaling of fringe\n                        frames [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FringeThresholdLow uses Python identifier FringeThresholdLow
    __FringeThresholdLow = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdLow'), 'FringeThresholdLow', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrameParameters_httpeuclid_esa_orgschemaprovisFringeThresholdLow', False)

    
    FringeThresholdLow = property(__FringeThresholdLow.value, __FringeThresholdLow.set, None, u' Lower bound of fringed pixels to include\n                        in scaling [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrameParameters_httpeuclid_esa_orgschemaprovisSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrameParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FringeThresholdHigh uses Python identifier FringeThresholdHigh
    __FringeThresholdHigh = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdHigh'), 'FringeThresholdHigh', '__httpeuclid_esa_orgschemaprovis_reducedScienceFrameParameters_httpeuclid_esa_orgschemaprovisFringeThresholdHigh', False)

    
    FringeThresholdHigh = property(__FringeThresholdHigh.value, __FringeThresholdHigh.set, None, u' Upper bound of fringed pixels to include\n                        in scaling [ADU] ')


    _ElementMap = {
        __OverscanCorrection.name() : __OverscanCorrection,
        __ImageThreshold.name() : __ImageThreshold,
        __FringeThresholdLow.name() : __FringeThresholdLow,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __ExtObjectId.name() : __ExtObjectId,
        __FringeThresholdHigh.name() : __FringeThresholdHigh
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'reducedScienceFrameParameters', reducedScienceFrameParameters)


# Complex type illuminationCorrectionParameters with content type ELEMENT_ONLY
class illuminationCorrectionParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminationCorrectionParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_illuminationCorrectionParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SigmaClippingLevel uses Python identifier SigmaClippingLevel
    __SigmaClippingLevel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel'), 'SigmaClippingLevel', '__httpeuclid_esa_orgschemaprovis_illuminationCorrectionParameters_httpeuclid_esa_orgschemaprovisSigmaClippingLevel', False)

    
    SigmaClippingLevel = property(__SigmaClippingLevel.value, __SigmaClippingLevel.set, None, u' Sigma clipping threshold from the median\n                        zeropoint [None] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __SigmaClippingLevel.name() : __SigmaClippingLevel
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'illuminationCorrectionParameters', illuminationCorrectionParameters)


# Complex type illuminationCorrection with content type ELEMENT_ONLY
class illuminationCorrection (euclid.dm.bas.img_stub.processTargetDataObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminationCorrection')
    # Base type is euclid.dm.bas.img_stub.processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/vis}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Records uses Python identifier Records
    __Records = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Records'), 'Records', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisRecords', True)

    
    Records = property(__Records.value, __Records.set, None, u' List of illumination correction\n                                records [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MagId uses Python identifier MagId
    __MagId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagId'), 'MagId', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisMagId', False)

    
    MagId = property(__MagId.value, __MagId.set, None, u' Identifier for the photometric\n                                band [None]')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}FitCoeffs uses Python identifier FitCoeffs
    __FitCoeffs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FitCoeffs'), 'FitCoeffs', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisFitCoeffs', True)

    
    FitCoeffs = property(__FitCoeffs.value, __FitCoeffs.set, None, u' List of fit coefficients [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaxX uses Python identifier MaxX
    __MaxX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxX'), 'MaxX', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisMaxX', False)

    
    MaxX = property(__MaxX.value, __MaxX.set, None, u' X coordinate of the source with\n                                the highest X position [pixel] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/vis}MinY uses Python identifier MinY
    __MinY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinY'), 'MinY', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisMinY', False)

    
    MinY = property(__MinY.value, __MinY.set, None, u' Y coordinate of the source with\n                                the lowest Y position [pixel] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/vis}MinX uses Python identifier MinX
    __MinX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinX'), 'MinX', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisMinX', False)

    
    MinX = property(__MinX.value, __MinX.set, None, u' X coordinate of the source with\n                                the lowest X position [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaxY uses Python identifier MaxY
    __MaxY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxY'), 'MaxY', '__httpeuclid_esa_orgschemaprovis_illuminationCorrection_httpeuclid_esa_orgschemaprovisMaxY', False)

    
    MaxY = property(__MaxY.value, __MaxY.set, None, u' Y coordinate of the source with\n                                the highest Y position [pixel] ')


    _ElementMap = euclid.dm.bas.img_stub.processTargetDataObject._ElementMap.copy()
    _ElementMap.update({
        __Instrument.name() : __Instrument,
        __TimestampStart.name() : __TimestampStart,
        __Records.name() : __Records,
        __MagId.name() : __MagId,
        __ProcessParams.name() : __ProcessParams,
        __Filter.name() : __Filter,
        __TimestampEnd.name() : __TimestampEnd,
        __FitCoeffs.name() : __FitCoeffs,
        __MaxX.name() : __MaxX,
        __MinY.name() : __MinY,
        __MinX.name() : __MinX,
        __MaxY.name() : __MaxY
    })
    _AttributeMap = euclid.dm.bas.img_stub.processTargetDataObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'illuminationCorrection', illuminationCorrection)


# Complex type rawBiasFrameParameters with content type ELEMENT_ONLY
class rawBiasFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawBiasFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}MaxBiasStdev uses Python identifier MaxBiasStdev
    __MaxBiasStdev = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasStdev'), 'MaxBiasStdev', '__httpeuclid_esa_orgschemaprovis_rawBiasFrameParameters_httpeuclid_esa_orgschemaprovisMaxBiasStdev', False)

    
    MaxBiasStdev = property(__MaxBiasStdev.value, __MaxBiasStdev.set, None, u' QC: Maximum sample standard deviation of\n                        the bias pixel values [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaxBiasFlatness uses Python identifier MaxBiasFlatness
    __MaxBiasFlatness = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasFlatness'), 'MaxBiasFlatness', '__httpeuclid_esa_orgschemaprovis_rawBiasFrameParameters_httpeuclid_esa_orgschemaprovisMaxBiasFlatness', False)

    
    MaxBiasFlatness = property(__MaxBiasFlatness.value, __MaxBiasFlatness.set, None, u' QC: Maximum difference in subwindow\n                        statistics (minimum minus maximum median values of 32\n                        sub-regions) [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_rawBiasFrameParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaxBiasLevel uses Python identifier MaxBiasLevel
    __MaxBiasLevel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasLevel'), 'MaxBiasLevel', '__httpeuclid_esa_orgschemaprovis_rawBiasFrameParameters_httpeuclid_esa_orgschemaprovisMaxBiasLevel', False)

    
    MaxBiasLevel = property(__MaxBiasLevel.value, __MaxBiasLevel.set, None, u' QC: Maximum average bias level (mean of\n                        the bias pixel values) [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaprovis_rawBiasFrameParameters_httpeuclid_esa_orgschemaprovisSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')


    _ElementMap = {
        __MaxBiasStdev.name() : __MaxBiasStdev,
        __MaxBiasFlatness.name() : __MaxBiasFlatness,
        __ExtObjectId.name() : __ExtObjectId,
        __MaxBiasLevel.name() : __MaxBiasLevel,
        __SourceCodeVersion.name() : __SourceCodeVersion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'rawBiasFrameParameters', rawBiasFrameParameters)


# Complex type CTD_ANON_3 with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}width uses Python identifier width
    __width = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'width'), 'width', '__httpeuclid_esa_orgschemaprovis_CTD_ANON_3_httpeuclid_esa_orgschemaproviswidth', False)

    
    width = property(__width.value, __width.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}Flags uses Python identifier Flags
    __Flags = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flags'), 'Flags', '__httpeuclid_esa_orgschemaprovis_CTD_ANON_3_httpeuclid_esa_orgschemaprovisFlags', True)

    
    Flags = property(__Flags.value, __Flags.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}CCDReference uses Python identifier CCDReference
    __CCDReference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CCDReference'), 'CCDReference', '__httpeuclid_esa_orgschemaprovis_CTD_ANON_3_httpeuclid_esa_orgschemaprovisCCDReference', False)

    
    CCDReference = property(__CCDReference.value, __CCDReference.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}QuadrantReference uses Python identifier QuadrantReference
    __QuadrantReference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'QuadrantReference'), 'QuadrantReference', '__httpeuclid_esa_orgschemaprovis_CTD_ANON_3_httpeuclid_esa_orgschemaprovisQuadrantReference', False)

    
    QuadrantReference = property(__QuadrantReference.value, __QuadrantReference.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/vis}height uses Python identifier height
    __height = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'height'), 'height', '__httpeuclid_esa_orgschemaprovis_CTD_ANON_3_httpeuclid_esa_orgschemaprovisheight', False)

    
    height = property(__height.value, __height.set, None, None)


    _ElementMap = {
        __width.name() : __width,
        __Flags.name() : __Flags,
        __CCDReference.name() : __CCDReference,
        __QuadrantReference.name() : __QuadrantReference,
        __height.name() : __height
    }
    _AttributeMap = {
        
    }



# Complex type photometricParametersParameters with content type ELEMENT_ONLY
class photometricParametersParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photometricParametersParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}SigmaClippingLevel uses Python identifier SigmaClippingLevel
    __SigmaClippingLevel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel'), 'SigmaClippingLevel', '__httpeuclid_esa_orgschemaprovis_photometricParametersParameters_httpeuclid_esa_orgschemaprovisSigmaClippingLevel', False)

    
    SigmaClippingLevel = property(__SigmaClippingLevel.value, __SigmaClippingLevel.set, None, u' Sigma clipping threshold factor for raw\n                        zeropoints [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaxError uses Python identifier MaxError
    __MaxError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxError'), 'MaxError', '__httpeuclid_esa_orgschemaprovis_photometricParametersParameters_httpeuclid_esa_orgschemaprovisMaxError', False)

    
    MaxError = property(__MaxError.value, __MaxError.set, None, u' QC: Maximum allowable error in the\n                        zeropoint [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MinSourceCount uses Python identifier MinSourceCount
    __MinSourceCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinSourceCount'), 'MinSourceCount', '__httpeuclid_esa_orgschemaprovis_photometricParametersParameters_httpeuclid_esa_orgschemaprovisMinSourceCount', False)

    
    MinSourceCount = property(__MinSourceCount.value, __MinSourceCount.set, None, u' QC: Minimum number of sources used in\n                        zeropoint determination [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaprovis_photometricParametersParameters_httpeuclid_esa_orgschemaprovisSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_photometricParametersParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __SigmaClippingLevel.name() : __SigmaClippingLevel,
        __MaxError.name() : __MaxError,
        __MinSourceCount.name() : __MinSourceCount,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'photometricParametersParameters', photometricParametersParameters)


# Complex type coaddedRegriddedFrameParameters with content type ELEMENT_ONLY
class coaddedRegriddedFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coaddedRegriddedFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/vis}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaprovis_coaddedRegriddedFrameParameters_httpeuclid_esa_orgschemaprovisSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}MaximumPSFDifference uses Python identifier MaximumPSFDifference
    __MaximumPSFDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumPSFDifference'), 'MaximumPSFDifference', '__httpeuclid_esa_orgschemaprovis_coaddedRegriddedFrameParameters_httpeuclid_esa_orgschemaprovisMaximumPSFDifference', False)

    
    MaximumPSFDifference = property(__MaximumPSFDifference.value, __MaximumPSFDifference.set, None, u' QC: Maximum fractional difference between\n                        average psf_radius of input regridded frames and the\n                        coadded regridded frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/vis}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaprovis_coaddedRegriddedFrameParameters_httpeuclid_esa_orgschemaprovisExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __MaximumPSFDifference.name() : __MaximumPSFDifference,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'coaddedRegriddedFrameParameters', coaddedRegriddedFrameParameters)


# Complex type coaddedRegriddedFrame with content type ELEMENT_ONLY
class coaddedRegriddedFrame (visBaseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coaddedRegriddedFrame')
    # Base type is visBaseFrame
    
    # Element Chip ({http://euclid.esa.org/schema/pro/vis}Chip) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element VisFitsPixelProcessingFlags ({http://euclid.esa.org/schema/pro/vis}VisFitsPixelProcessingFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/vis}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element VisPipelineFlags ({http://euclid.esa.org/schema/pro/vis}VisPipelineFlags) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExposureMode ({http://euclid.esa.org/schema/pro/vis}ExposureMode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element VISErrorCode ({http://euclid.esa.org/schema/pro/vis}VISErrorCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Position ({http://euclid.esa.org/schema/pro/vis}Position) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/vis}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Filter ({http://euclid.esa.org/schema/pro/vis}Filter) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element TypeCode ({http://euclid.esa.org/schema/pro/vis}TypeCode) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/vis}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element Dithering ({http://euclid.esa.org/schema/pro/vis}Dithering) inherited from {http://euclid.esa.org/schema/pro/vis}visBaseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = visBaseFrame._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = visBaseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'coaddedRegriddedFrame', coaddedRegriddedFrame)




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HealPix'), pyxb.binding.datatypes.int, scope=CTD_ANON))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEC'), pyxb.binding.datatypes.float, scope=CTD_ANON))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RA'), pyxb.binding.datatypes.float, scope=CTD_ANON))
CTD_ANON._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEC')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HealPix')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON._GroupModel, min_occurs=1, max_occurs=1)



visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), euclid.dm.bas.img_stub.chip, scope=visBaseFrame, documentation=u' Information about the detector\n                                chip [None] '))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags'), CTD_ANON_3, scope=visBaseFrame))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=visBaseFrame, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags'), pyxb.binding.datatypes.int, scope=visBaseFrame, documentation=u'OU VIS flags for the pipeline.  Flags should be set the FITS file is processed in various modules of the OUVIS pipeline.  TBD if the value will need to be shifted or masked off'))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode'), STD_ANON, scope=visBaseFrame))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode'), pyxb.binding.datatypes.int, scope=visBaseFrame, documentation=u'Error Codes given in the OU-VIS pipeline related to the FITS file.  May move moved to a higher level.  TBD the format of the codes'))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Position'), CTD_ANON, scope=visBaseFrame))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime'), pyxb.binding.datatypes.float, scope=visBaseFrame))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), euclid.dm.bas.img_stub.filter, scope=visBaseFrame, documentation=u' Information about the\n                                observational filter [None] '))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TypeCode'), pyxb.binding.datatypes.short, scope=visBaseFrame))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=visBaseFrame, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

visBaseFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Dithering'), STD_ANON_, scope=visBaseFrame))
visBaseFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
visBaseFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
visBaseFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visBaseFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
visBaseFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
visBaseFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visBaseFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
visBaseFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
visBaseFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visBaseFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visBaseFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
visBaseFrame._ContentModel = pyxb.binding.content.ParticleModel(visBaseFrame._GroupModel, min_occurs=1, max_occurs=1)



rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscx'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels in the\n                                X direction [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Object'), euclid.dm.bas_stub.objectName, scope=rawFrame, documentation=u' Name of target object [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscy'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels in the\n                                Y direction [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Date'), pyxb.binding.datatypes.dateTime, scope=rawFrame, documentation=u' UTC date the original data file\n                                was saved [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanXStat'), euclid.dm.bas.img_stub.imStats, scope=rawFrame, documentation=u' Statistics of the overscan region\n                                in the X direction [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscxpre'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels to skip\n                                in the X direction at the edge of the chip\n                                [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), euclid.dm.bas.img_stub.template, scope=rawFrame, documentation=u' Information about the\n                                observational template [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscypre'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels to skip\n                                in the Y direction at the edge of the chip\n                                [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpre'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels to skip\n                                in the X direction at the edge of the chip\n                                [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), euclid.dm.bas.img_stub.obsBlock, scope=rawFrame, documentation=u' Information about the\n                                observational block [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrescanYStat'), euclid.dm.bas.img_stub.imStats, scope=rawFrame, documentation=u' Statistics of the prescan region\n                                in the Y direction [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), pyxb.binding.datatypes.dateTime, scope=rawFrame, documentation=u' UTC date at the start of the\n                                observation [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MjdObs'), pyxb.binding.datatypes.float, scope=rawFrame, documentation=u' Modified Julian date at the start\n                                of the observation (JD-2400000.5) [day] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanYStat'), euclid.dm.bas.img_stub.imStats, scope=rawFrame, documentation=u' Statistics of the overscan region\n                                in the Y direction [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscxpst'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels to skip\n                                in the X direction at the edge of the data\n                                region [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Lst'), pyxb.binding.datatypes.float, scope=rawFrame, documentation=u' Local sidereal time at the start\n                                of the observation expressed as the number of\n                                seconds (a float) since UTC midnight [sec] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscypst'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels to skip\n                                in the Y direction at the edge of the data\n                                region [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Utc'), pyxb.binding.datatypes.float, scope=rawFrame, documentation=u' Universal coordinated time at the\n                                start of the observation expressed as the number\n                                of seconds (a float) since UTC midnight [sec] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpst'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels to skip\n                                in the X direction at the edge of the data\n                                region [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscypst'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels to skip\n                                in the Y direction at the edge of the data\n                                region [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscypre'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels to skip\n                                in the Y direction at the edge of the chip\n                                [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Extension'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Extension number of this frame to\n                                be extracted from the rawFits container [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscy'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels in the Y\n                                direction [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscx'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels in the X\n                                direction [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrescanXStat'), euclid.dm.bas.img_stub.imStats, scope=rawFrame, documentation=u' Statistics of the prescan region\n                                in the X direction [None] '))
rawFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extension')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Date')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MjdObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Lst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Utc')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanYStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanYStat')), min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
rawFrame._ContentModel = pyxb.binding.content.ParticleModel(rawFrame._GroupModel, min_occurs=1, max_occurs=1)



rawDarkFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), pyxb.binding.datatypes.float, scope=rawDarkFrame, documentation=u' Total time of an individual\n                                exposure [sec] '))
rawDarkFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_5, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_9 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extension')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Date')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MjdObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Lst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Utc')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanYStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanYStat')), min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_9, min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_10 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpTime')), min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_10, min_occurs=1, max_occurs=1)
    )
rawDarkFrame._ContentModel = pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel, min_occurs=1, max_occurs=1)



associateListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SearchDistance'), pyxb.binding.datatypes.float, scope=associateListParameters, documentation=u' Radius of search for associates [arcsec] '))

associateListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SextractorFlagMask'), pyxb.binding.datatypes.int, scope=associateListParameters, documentation=u' Value of SExtractor flag mask for source\n                        filtering [None]'))

associateListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleOutClosestPairs'), pyxb.binding.datatypes.int, scope=associateListParameters, documentation=u' Filter to retain only the closest\n                        associations [None] '))

associateListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=associateListParameters, documentation=u' Unique EXT object identifier [None] '))

associateListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=associateListParameters, documentation=u' Version of the source code [None] '))
associateListParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(associateListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SearchDistance')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SingleOutClosestPairs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SextractorFlagMask')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
associateListParameters._ContentModel = pyxb.binding.content.ParticleModel(associateListParameters._GroupModel, min_occurs=1, max_occurs=1)



associateListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ALID'), pyxb.binding.datatypes.int, scope=associateListDict, documentation=u' Identifier of the associate list [None] '))

associateListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SID'), pyxb.binding.datatypes.int, scope=associateListDict, documentation=u' Identifier of a source in the source list\n                        [None] '))

associateListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG'), pyxb.binding.datatypes.int, scope=associateListDict, documentation=u' Internal flag indicating the source\n                        list(s) participating in the association [None] '))

associateListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AID'), pyxb.binding.datatypes.int, scope=associateListDict, documentation=u' Identifier of an association in the\n                        associate list [None] '))

associateListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLID'), pyxb.binding.datatypes.int, scope=associateListDict, documentation=u' Identifier of the source list [None] '))
associateListDict._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(associateListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ALID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SLID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLAG')), min_occurs=1, max_occurs=1)
    )
associateListDict._ContentModel = pyxb.binding.content.ParticleModel(associateListDict._GroupModel, min_occurs=1, max_occurs=1)



reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AirmassStart'), pyxb.binding.datatypes.float, scope=reducedScienceFrame, documentation=u' Airmass at the beginning of the\n                                observation [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), illuminationCorrectionFrame, scope=reducedScienceFrame, documentation=u' Information about the\n                                illumination correction\n                                [None]'))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AirmassEnd'), pyxb.binding.datatypes.float, scope=reducedScienceFrame, documentation=u' Airmass at the ending of the\n                                observation [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Weight'), weightFrame, scope=reducedScienceFrame, documentation=u' Information about the detector\n                                pixel weights [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ScaleFactor'), pyxb.binding.datatypes.float, scope=reducedScienceFrame, documentation=u' Detector fringe pattern scaling\n                                factor [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), pyxb.binding.datatypes.float, scope=reducedScienceFrame, documentation=u' Estimate of seeing using the\n                                median FWHM (filtered to isolate most\n                                stellar-like sources) [arcsec] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), euclid.dm.bas.img_stub.obsBlock, scope=reducedScienceFrame, documentation=u' Information about the\n                                observational block [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), reducedScienceFrameParameters, scope=reducedScienceFrame, documentation=u' Processing and verification\n                                parameters [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Object'), pyxb.binding.datatypes.string, scope=reducedScienceFrame, documentation=u' Name of target object [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Raw'), visBaseFrame, scope=reducedScienceFrame, documentation=u' Information about the input raw\n                                science frame [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), pyxb.binding.datatypes.float, scope=reducedScienceFrame, documentation=u' Total time of an individual\n                                exposure [sec] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Astrom'), euclid.dm.bas.cot_stub.astrom, scope=reducedScienceFrame, documentation=u' Basic information about the\n                                astrometry (linear terms only) [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Date'), pyxb.binding.datatypes.dateTime, scope=reducedScienceFrame, documentation=u' UTC date the original data file\n                                was saved [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), euclid.dm.bas.img_stub.template, scope=reducedScienceFrame, documentation=u' Information about the\n                                observational template [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bias'), biasFrame, scope=reducedScienceFrame, documentation=u' Information about the detector\n                                bias offset levels [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), pyxb.binding.datatypes.dateTime, scope=reducedScienceFrame, documentation=u' UTC date at the start of the\n                                observation [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flat'), masterFlatFrame, scope=reducedScienceFrame, documentation=u' Information about the detector\n                                sensitivity variations [None] '))
reducedScienceFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Raw')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Astrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bias')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Illumination')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Weight')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ScaleFactor')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Date')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AirmassStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AirmassEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Seeing')), min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._ContentModel = pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel, min_occurs=1, max_occurs=1)



biasFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), biasFrameParameters, scope=biasFrame, documentation=u' Processing and verification\n                                parameters [None] '))

biasFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise'), readNoise, scope=biasFrame, documentation=u' Information about the detector\n                                readout noise [None] '))

biasFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames'), rawBiasFrame, scope=biasFrame, documentation=u' List of input raw bias frames\n                                [None] '))
biasFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames')), min_occurs=3L, max_occurs=None),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
biasFrame._ContentModel = pyxb.binding.content.ParticleModel(biasFrame._GroupModel, min_occurs=1, max_occurs=1)



masterFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), masterFlatFrameParameters, scope=masterFlatFrame, documentation=u' Processing and verification\n                                parameters [None] '))

masterFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flat'), masterFlatFrame, scope=masterFlatFrame, documentation=u' Information about the detector\n                                sensitivity variations [None] '))
masterFlatFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flat')), min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
masterFlatFrame._ContentModel = pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel, min_occurs=1, max_occurs=1)



readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise'), pyxb.binding.datatypes.float, scope=readNoise, documentation=u' Value of readout noise\n                                measurement [ADU] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames'), rawBiasFrame, scope=readNoise, documentation=u' List of input raw bias frames\n                                [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=readNoise, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), euclid.dm.bas.img_stub.chip, scope=readNoise, documentation=u' Information about the detector\n                                chip [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MeanDiff'), pyxb.binding.datatypes.float, scope=readNoise, documentation=u' Mean pixel value difference\n                                between biases [ADU] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), euclid.dm.bas.img_stub.obsBlock, scope=readNoise, documentation=u' Information about the\n                                observational block [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), euclid.dm.bas.img_stub.instrument, scope=readNoise, documentation=u' Information about the acquisition\n                                instrument [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), readNoiseParameters, scope=readNoise, documentation=u' Processing and verification\n                                parameters [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MedianDiff'), pyxb.binding.datatypes.float, scope=readNoise, documentation=u' Median pixel value difference\n                                between biases [ADU] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=readNoise, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), euclid.dm.bas.img_stub.template, scope=readNoise, documentation=u' Information about the\n                                observational template [None] '))
readNoise._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
readNoise._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MeanDiff')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MedianDiff')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames')), min_occurs=2L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
readNoise._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(readNoise._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoise._GroupModel_2, min_occurs=1, max_occurs=1)
    )
readNoise._ContentModel = pyxb.binding.content.ParticleModel(readNoise._GroupModel, min_occurs=1, max_occurs=1)



biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=biasFrameParameters, documentation=u' Unique EXT object identifier [None] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumAbsMean'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' QC: Maximum absolute mean value of the\n                        bias levels [ADU] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' QC: Maximum difference between median\n                        values of any two sub-windows [ADU] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), pyxb.binding.datatypes.int, scope=biasFrameParameters, documentation=u' Overscan correction method index [None] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumStdev'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' QC: Maximum sample standard deviation\n                        value of the bias levels [ADU] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinStdev'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' QC: Maximum sample standard deviation\n                        value of any sub-window [ADU] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' Threshold factor for rejecting raw bias\n                        pixel value outliers (sigma is taken as the readout\n                        noise measurement) [None] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumStdevDifference'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' QC: Maximum sample standard deviation\n                        difference of the bias levels relative to the previous\n                        version [ADU] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=biasFrameParameters, documentation=u' Version of the source code [None] '))
biasFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumAbsMean')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumStdev')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumStdevDifference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinStdev')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
biasFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(biasFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Storage'), euclid.dm.sys.sgs_stub.dataContainer, scope=baseList, documentation=u' Customized storage container for the data\n                        [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URRa'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Right Ascension of upper right corner\n                        [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URDec'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Declination of upper right corner [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ULRa'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Right Ascension of upper left corner\n                        [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=baseList, documentation=u' Name of the list [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LRDec'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Declination of lower right corner [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LRRa'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Right Ascension of lower right corner\n                        [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Object'), pyxb.binding.datatypes.string, scope=baseList, documentation=u' Name of target object [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IsValid'), pyxb.binding.datatypes.int, scope=baseList, documentation=u' Manual/external flag to disqualify bad\n                        data (SuperFlag) [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=baseList, documentation=u' Unique EXT object identifier [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LLRa'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Right Ascension of lower left corner\n                        [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ULDec'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Declination of upper left corner [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), pyxb.binding.datatypes.dateTime, scope=baseList, documentation=u' UTC date this object was created [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LLDec'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Declination of lower left corner [deg] '))
baseList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LLRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LLDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LRRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LRDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ULRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ULDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1)
    )
baseList._ContentModel = pyxb.binding.content.ParticleModel(baseList._GroupModel, min_occurs=1, max_occurs=1)



associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceLists'), sourceList, scope=associateList, documentation=u' List of input source lists [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Associates'), associateListDict, scope=associateList, documentation=u' Column definitions of\n                                associations [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociateListType'), pyxb.binding.datatypes.int, scope=associateList, documentation=u' Type of associate list [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Alid'), pyxb.binding.datatypes.int, scope=associateList, documentation=u' Identifier of the associate list\n                                [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociateCount'), pyxb.binding.datatypes.int, scope=associateList, documentation=u' Number of associated source\n                                pairings [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InputAssociateList'), associateList, scope=associateList, documentation=u' Information about the input\n                                associations [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), associateListParameters, scope=associateList, documentation=u' Processing and verification\n                                parameters [None] '))
associateList._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LLRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LLDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LRRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LRDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ULRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ULDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1)
    )
associateList._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceLists')), min_occurs=2L, max_occurs=None),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InputAssociateList')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AssociateListType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AssociateCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Associates')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Alid')), min_occurs=1, max_occurs=1)
    )
associateList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(associateList._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateList._GroupModel_2, min_occurs=1, max_occurs=1)
    )
associateList._ContentModel = pyxb.binding.content.ParticleModel(associateList._GroupModel, min_occurs=1, max_occurs=1)


rawBiasFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
rawBiasFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
rawBiasFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
rawBiasFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
rawBiasFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
rawBiasFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
rawBiasFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
rawBiasFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extension')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Date')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MjdObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Lst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Utc')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanYStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanYStat')), min_occurs=1, max_occurs=1)
    )
rawBiasFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
rawBiasFrame._ContentModel = pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel, min_occurs=1, max_occurs=1)



readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumReadNoiseDifference'), pyxb.binding.datatypes.float, scope=readNoiseParameters, documentation=u' QC: Maximum difference between readout\n                        noise measurements relative to the previous version\n                        [ADU] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold'), pyxb.binding.datatypes.float, scope=readNoiseParameters, documentation=u' Threshold for rejecting pixels with\n                        outlying values [None] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumReadNoise'), pyxb.binding.datatypes.float, scope=readNoiseParameters, documentation=u' QC: Maximum value for the readout noise\n                        [ADU] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=readNoiseParameters, documentation=u' Version of the source code [None] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumBiasDifference'), pyxb.binding.datatypes.float, scope=readNoiseParameters, documentation=u' QC: Maximum mean pixel value difference\n                        between biases [ADU] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations'), pyxb.binding.datatypes.int, scope=readNoiseParameters, documentation=u' Maximum number of iterations for\n                        estimating statistics [None] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=readNoiseParameters, documentation=u' Unique EXT object identifier [None] '))
readNoiseParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(readNoiseParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoiseParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoiseParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoiseParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumReadNoise')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoiseParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumBiasDifference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoiseParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumReadNoiseDifference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readNoiseParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
readNoiseParameters._ContentModel = pyxb.binding.content.ParticleModel(readNoiseParameters._GroupModel, min_occurs=1, max_occurs=1)



illuminationCorrectionFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IlluminationCorrection'), illuminationCorrection, scope=illuminationCorrectionFrame, documentation=u' Information about the\n                                illumination correction [None] '))
illuminationCorrectionFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IlluminationCorrection')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._ContentModel = pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel, min_occurs=1, max_occurs=1)



weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Naxis1'), pyxb.binding.datatypes.int, scope=weightFrame, documentation=u' Length of data in axis 1 [pixel] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Naxis2'), pyxb.binding.datatypes.int, scope=weightFrame, documentation=u' Length of data in axis 2 [pixel] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImStat'), euclid.dm.bas.img_stub.imStats, scope=weightFrame, documentation=u' Information about the statistics\n                                of the image pixels [None] '))
weightFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImStat')), min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
weightFrame._ContentModel = pyxb.binding.content.ParticleModel(weightFrame._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Location'), pyxb.binding.datatypes.int, scope=CTD_ANON_))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.float, scope=CTD_ANON_))
CTD_ANON_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Location')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Location'), pyxb.binding.datatypes.int, scope=CTD_ANON_2))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.float, scope=CTD_ANON_2))
CTD_ANON_2._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Location')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_2._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_2._GroupModel, min_occurs=1, max_occurs=1)


pixelMap._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
pixelMap._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
pixelMap._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._GroupModel_4, min_occurs=1, max_occurs=1)
    )
pixelMap._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
pixelMap._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._GroupModel_5, min_occurs=1, max_occurs=1)
    )
pixelMap._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
pixelMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._GroupModel_6, min_occurs=1, max_occurs=1)
    )
pixelMap._ContentModel = pyxb.binding.content.ParticleModel(pixelMap._GroupModel, min_occurs=1, max_occurs=1)



cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), illuminationCorrectionFrame, scope=cosmicMap, documentation=u' Information about the\n                                illumination correction [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Gain'), gainLinearity, scope=cosmicMap, documentation=u' Information about the detector\n                                gain [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), euclid.dm.bas.img_stub.instrument, scope=cosmicMap, documentation=u' Information about the acquisition\n                                instrument [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flat'), masterFlatFrame, scope=cosmicMap, documentation=u' Information about the detector\n                                sensitivity variations [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), cosmicMapParameters, scope=cosmicMap, documentation=u' Processing and verification\n                                parameters [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CosmicCount'), pyxb.binding.datatypes.int, scope=cosmicMap, documentation=u' Number of cosmic ray events (not\n                                affected pixels) [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Frame'), euclid.dm.bas.img_stub.baseFrame, scope=cosmicMap, documentation=u' Information about the input\n                                reduced science frame [None] '))
cosmicMap._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_5, min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_6, min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_7, min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Illumination')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Gain')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CosmicCount')), min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_8, min_occurs=1, max_occurs=1)
    )
cosmicMap._ContentModel = pyxb.binding.content.ParticleModel(cosmicMap._GroupModel, min_occurs=1, max_occurs=1)



gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawFlatFrames'), rawFrame, scope=gainLinearity, documentation=u' List of input raw  flat\n                                frames [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), euclid.dm.bas.img_stub.obsBlock, scope=gainLinearity, documentation=u' Information about the\n                                observational block [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), euclid.dm.bas.img_stub.template, scope=gainLinearity, documentation=u' Information about the\n                                observational template [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureTimes'), pyxb.binding.datatypes.float, scope=gainLinearity, documentation=u' List of exposure times of the flat frames [second] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=gainLinearity, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), euclid.dm.bas.img_stub.chip, scope=gainLinearity, documentation=u' Information about the detector\n                                chip [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bias'), biasFrame, scope=gainLinearity, documentation=u' Information about the detector\n                                bias offset levels [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), euclid.dm.bas.img_stub.instrument, scope=gainLinearity, documentation=u' Information about the acquisition\n                                instrument [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RmsDiff'), pyxb.binding.datatypes.float, scope=gainLinearity, documentation=u' List of raw measurements of\n                                sample standard deviation of pixel values of the\n                                subtracted dome flat frames [ADU] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Gain'), pyxb.binding.datatypes.float, scope=gainLinearity, documentation=u' Value of the gain measurement\n                                (ADU conversion factor) [electron / ADU] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), gainLinearityParameters, scope=gainLinearity, documentation=u' Processing and verification\n                                parameters [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MedianSum'), pyxb.binding.datatypes.float, scope=gainLinearity, documentation=u' List of raw measurements of\n                                median pixel values of the added dome flat\n                                frames [ADU] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureLevels'), pyxb.binding.datatypes.float, scope=gainLinearity, documentation=u' List of exposure levels (median\n                                pixel value of each flat frame) [ADU] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=gainLinearity, documentation=u' UTC date of the ending of the\n                                valid period [None] '))
gainLinearity._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
gainLinearity._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
gainLinearity._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(gainLinearity._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._GroupModel_3, min_occurs=1, max_occurs=1)
    )
gainLinearity._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Gain')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RmsDiff')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MedianSum')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTimes')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureLevels')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawFlatFrames')), min_occurs=2L, max_occurs=None),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bias')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
gainLinearity._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(gainLinearity._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._GroupModel_4, min_occurs=1, max_occurs=1)
    )
gainLinearity._ContentModel = pyxb.binding.content.ParticleModel(gainLinearity._GroupModel, min_occurs=1, max_occurs=1)



gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), pyxb.binding.datatypes.int, scope=gainLinearityParameters, documentation=u' Overscan correction method index [None] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumGainDifference'), pyxb.binding.datatypes.float, scope=gainLinearityParameters, documentation=u' QC: Maximum gain difference relative to\n                        the previous version [electron / ADU] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold'), pyxb.binding.datatypes.float, scope=gainLinearityParameters, documentation=u' Threshold for rejecting pixels with\n                        outlying values [None] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinimumGain'), pyxb.binding.datatypes.float, scope=gainLinearityParameters, documentation=u' QC: Minimum gain [electron / ADU] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=gainLinearityParameters, documentation=u' Unique EXT object identifier [None] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations'), pyxb.binding.datatypes.int, scope=gainLinearityParameters, documentation=u' Maximum number of iterations for\n                        estimating statistics [None] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximimGain'), pyxb.binding.datatypes.float, scope=gainLinearityParameters, documentation=u' QC: Maximum gain [electron / ADU] '))
gainLinearityParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(gainLinearityParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearityParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearityParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearityParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearityParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumGainDifference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearityParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinimumGain')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearityParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximimGain')), min_occurs=1, max_occurs=1)
    )
gainLinearityParameters._ContentModel = pyxb.binding.content.ParticleModel(gainLinearityParameters._GroupModel, min_occurs=1, max_occurs=1)



cosmicMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectionThreshold'), pyxb.binding.datatypes.float, scope=cosmicMapParameters, documentation=u' Threshold for detecting pixels with\n                        cosmic ray events [None] '))

cosmicMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=cosmicMapParameters, documentation=u' Unique EXT object identifier [None] '))
cosmicMapParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectionThreshold')), min_occurs=1, max_occurs=1)
    )
cosmicMapParameters._ContentModel = pyxb.binding.content.ParticleModel(cosmicMapParameters._GroupModel, min_occurs=1, max_occurs=1)



sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectionFrame'), euclid.dm.bas.img_stub.baseFrame, scope=sourceList, documentation=u' Optional frame used to identify\n                                sources to be extracted (double image mode)\n                                [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), euclid.dm.bas.img_stub.chip, scope=sourceList, documentation=u' Information about the detector\n                                chip [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Slid'), pyxb.binding.datatypes.int, scope=sourceList, documentation=u' Identifier of the source list\n                                [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociateList'), pyxb.binding.datatypes.int, scope=sourceList, documentation=u' ALID (associate list identifier)\n                                that was used to create this (combined) source\n                                list [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Frame'), euclid.dm.bas.img_stub.baseFrame, scope=sourceList, documentation=u' Information about the input frame\n                                [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filters'), pyxb.binding.datatypes.string, scope=sourceList, documentation=u' Observational filters for which\n                                columns are present in this (combined) source\n                                list [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexParam'), pyxb.binding.datatypes.string, scope=sourceList, documentation=u' List of parameters derived for\n                                each extracted source [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CombineMethod'), pyxb.binding.datatypes.int, scope=sourceList, documentation=u' Method that was used to create\n                                this (combined) source list [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), sourceListParameters, scope=sourceList, documentation=u' Processing and verification\n                                parameters [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), euclid.dm.bas.img_stub.filter, scope=sourceList, documentation=u' Information about the\n                                observational filter [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), pyxb.binding.datatypes.int, scope=sourceList, documentation=u' Number of extracted sources\n                                [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sources'), sourceListDict, scope=sourceList, documentation=u' Column definitions of extracted\n                                sources [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), euclid.dm.bas.img_stub.instrument, scope=sourceList, documentation=u' Information about the acquisition\n                                instrument [None] '))
sourceList._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LLRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LLDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LRRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LRDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ULRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ULDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URRa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URDec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1)
    )
sourceList._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectionFrame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexParam')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Slid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sources')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AssociateList')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filters')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CombineMethod')), min_occurs=1, max_occurs=1)
    )
sourceList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sourceList._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._GroupModel_2, min_occurs=1, max_occurs=1)
    )
sourceList._ContentModel = pyxb.binding.content.ParticleModel(sourceList._GroupModel, min_occurs=1, max_occurs=1)



CTICorrectionFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CTIParameters'), CTICorrectionParameters, scope=CTICorrectionFrame, documentation=u' Information about the\n                                illumination correction [None] '))
CTICorrectionFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
CTICorrectionFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
CTICorrectionFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
CTICorrectionFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
CTICorrectionFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
CTICorrectionFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
CTICorrectionFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
CTICorrectionFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CTIParameters')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
CTICorrectionFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
CTICorrectionFrame._ContentModel = pyxb.binding.content.ParticleModel(CTICorrectionFrame._GroupModel, min_occurs=1, max_occurs=1)



CTICorrectionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AOCS'), CTD_ANON_, scope=CTICorrectionParameters))

CTICorrectionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Temperature'), CTD_ANON_2, scope=CTICorrectionParameters))
CTICorrectionParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTICorrectionParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AOCS')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTICorrectionParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Temperature')), min_occurs=1, max_occurs=1)
    )
CTICorrectionParameters._ContentModel = pyxb.binding.content.ParticleModel(CTICorrectionParameters._GroupModel, min_occurs=1, max_occurs=1)



astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_5'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,5 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_8'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,8 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MeanDdecOverlap'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Average overlap residual in\n                                declination [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NOverlap'), pyxb.binding.datatypes.int, scope=astrometricParameters, documentation=u' Number of overlap pairings used\n                                in the astrometric solution [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRPIX2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Reference pixel in Y [pixel] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_10'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,10 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MeanDra'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Average reference residual in\n                                right ascension [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitErrors'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Errors on fitted parameters [rad] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRVAL1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Physical value of the reference\n                                pixel X [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaDra'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Sample standard deviation of\n                                reference residuals in right ascension [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,2 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), euclid.dm.bas.img_stub.template, scope=astrometricParameters, documentation=u' Information about the\n                                observational template [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_6'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,6 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,2 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CTYPE1'), pyxb.binding.datatypes.string, scope=astrometricParameters, documentation=u' Pixel coordinate system and\n                                projection of first axis (X) [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_9'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,9 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), euclid.dm.bas.img_stub.instrument, scope=astrometricParameters, documentation=u' Information about the acquisition\n                                instrument [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaDdec'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Sample standard deviation of\n                                reference residuals in declination [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_0'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value a0 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_9'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,9 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRPIX1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Reference pixel in X [pixel] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_4'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,4 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FieldError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Global position error [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NRef'), pyxb.binding.datatypes.int, scope=astrometricParameters, documentation=u' Number of reference pairings used\n                                in the astrometric solution [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_4'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,4 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Rms'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Two-dimensional root-mean-square\n                                of reference residuals [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRVAL2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Physical value of the reference\n                                pixel Y [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Error in polynomial X coefficient\n                                [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RefcatSlid'), pyxb.binding.datatypes.int, scope=astrometricParameters, documentation=u' The ID of the source list used\n                                for the reference catalog [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Residuals'), pyxb.binding.datatypes.string, scope=astrometricParameters, documentation=u' Filename of residuals FITS table\n                                [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YyError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Error in polynomial YY\n                                coefficient [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD1_1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Linear transformation matrix\n                                parameter at i,j=1,1 (a1) [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Error in polynomial Y coefficient\n                                [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CTYPE2'), pyxb.binding.datatypes.string, scope=astrometricParameters, documentation=u' Pixel coordinate system and\n                                projection of second axis (Y) [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_7'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,7 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Estimate of seeing using the\n                                median FWHM (filtered to isolate most\n                                stellar-like sources) [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_7'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,7 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD2_1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Linear transformation matrix\n                                parameter at i,j=2,1 (b1) [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), euclid.dm.bas.img_stub.chip, scope=astrometricParameters, documentation=u' Information about the detector\n                                chip [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_3'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,3 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,1 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitParams'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Degrees of freedom of fitted\n                                parameters [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XyError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Error in polynomial XY\n                                coefficient [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,1 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_8'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,8 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaDraOverlap'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Sample standard deviation of\n                                overlap residuals in right ascension [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_6'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,6 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reduced'), euclid.dm.bas.img_stub.baseFrame, scope=astrometricParameters, documentation=u' Information about the input\n                                reduced science frame [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), euclid.dm.bas.img_stub.obsBlock, scope=astrometricParameters, documentation=u' Information about the\n                                observational block [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_5'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,5 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaDdecOverlap'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Sample standard deviation of\n                                overlap residuals in declination [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD2_2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Linear transformation matrix\n                                parameter at i,j=2,2 (b2) [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD1_2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Linear transformation matrix\n                                parameter at i,j=1,2 (a2) [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MeanDdec'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Average reference residual in\n                                declination [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), euclid.dm.bas.img_stub.filter, scope=astrometricParameters, documentation=u' Information about the\n                                observational filter [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_3'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,3 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_0'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value c0 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MeanDraOverlap'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Average overlap residual in right\n                                ascension [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XxError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Error in polynomial XX\n                                coefficient [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_10'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,10 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RmsOverlap'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Two-dimensional root-mean-square\n                                of overlap residuals [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NFitParm'), pyxb.binding.datatypes.int, scope=astrometricParameters, documentation=u' Number of fitted parameters\n                                [None] '))
astrometricParameters._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
astrometricParameters._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RefcatSlid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reduced')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Seeing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CTYPE1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CRVAL1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CRPIX1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CTYPE2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CRVAL2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CRPIX2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CD1_1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CD1_2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CD2_1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CD2_2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_0')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_3')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_4')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_5')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_6')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_7')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_8')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_9')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV1_10')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_0')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_3')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_4')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_5')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_6')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_7')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_8')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_9')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PV2_10')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MeanDra')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MeanDdec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaDra')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaDdec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Rms')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NRef')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NFitParm')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FitParams')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FitErrors')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MeanDraOverlap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MeanDdecOverlap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaDraOverlap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaDdecOverlap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RmsOverlap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NOverlap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XxError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XyError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YyError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FieldError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Residuals')), min_occurs=1, max_occurs=1)
    )
astrometricParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astrometricParameters._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._GroupModel_2, min_occurs=1, max_occurs=1)
    )
astrometricParameters._ContentModel = pyxb.binding.content.ParticleModel(astrometricParameters._GroupModel, min_occurs=1, max_occurs=1)



sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLID'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Identifier of the source list [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_APER'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Fixed aperture magnitude vector [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_ISO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error for isophotal magnitude [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxVal'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Peak flux above background [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUX_ISO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Isophotal flux [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SID'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Identifier of a source in the source list\n                        [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_ISO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Isophotal magnitude [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ERRA_IMAGE'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Error on measurement of semi-major axis\n                        of profile [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RA'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Right Ascension [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ypos'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Source position along Y [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ERRB_IMAGE'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Error on measurement of semi-minor axis\n                        of profile [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BackGr'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Background level around a source [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEC'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Declination [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_ISO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error for isophotal flux [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ERRTHETA_IMAGE'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Error on measurement of ellipse position\n                        angle [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HTM'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Index of HTM (Hierarchical Triangular\n                        Mesh) [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SeqNr'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Index of extracted source [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FIELD_POS'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Observation index for multi-observation\n                        source lists [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Level'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Level of detection threshold above\n                        background [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'A'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Semi-major axis of profile [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XM2'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Variance along X [pixel**2] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Source extraction flags [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_AUTO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Kron-like elliptical aperture magnitude\n                        [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'B'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Semi-minor axis of profile [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUX_APER'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Flux vector within fixed circular\n                        aperture(s) [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Xpos'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Source position along X [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'A_WCS'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Semi-major axis of profile [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_APER'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error vector for fixed aperture\n                        magnitude [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUX_AUTO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Flux within a Kron-like elliptical\n                        aperture [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Corr'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Covariance between X and Y [pixel**2] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'B_WCS'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Semi-minor axis of profile [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_AUTO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error for AUTO flux [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YM2'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Variance along Y [pixel**2] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PosErr'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Positional error of extraction (measured\n                        semi-major axis) [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_AUTO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error for AUTO magnitude [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NPIX'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Isophotal area above analysis threshold\n                        [pixel**2] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FWHM_IMAGE'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Full width at half maximum assuming a\n                        gaussian core [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_APER'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error vector for aperture flux(es)\n                        [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUX_RADIUS'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Fraction-of-light radius [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MU_MAX'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Peak surface brightness above background\n                        [mag / arcsec**2] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CLASS_STAR'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Star/galaxy classifier index [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'POSANG'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Ellipse position angle [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'THETAWCS'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Ellipse position angle [deg] '))
sourceListDict._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SLID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEC')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HTM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'A')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'B')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'A_WCS')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'B_WCS')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BackGr')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CLASS_STAR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Corr')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ERRA_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ERRB_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ERRTHETA_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FIELD_POS')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLAG')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLUX_APER')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLUX_AUTO')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLUX_ISO')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLUX_RADIUS')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_APER')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_AUTO')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_ISO')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FWHM_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Level')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAG_APER')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAG_AUTO')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAG_ISO')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_APER')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_AUTO')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_ISO')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxVal')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MU_MAX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NPIX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'POSANG')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PosErr')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SeqNr')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'THETAWCS')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XM2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YM2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Xpos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ypos')), min_occurs=1, max_occurs=1)
    )
sourceListDict._ContentModel = pyxb.binding.content.ParticleModel(sourceListDict._GroupModel, min_occurs=1, max_occurs=1)



masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MirrorYpix'), pyxb.binding.datatypes.int, scope=masterFlatFrameParameters, documentation=u' Number of pixels to mirror beyond the Y\n                        edges of the detector to provide Fourier transform\n                        continuity [pixel] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=masterFlatFrameParameters, documentation=u' Version of the source code [None] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DigFilterSize'), pyxb.binding.datatypes.float, scope=masterFlatFrameParameters, documentation=u' Gaussian Fourier filter size [None] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MedianFilterSize'), pyxb.binding.datatypes.int, scope=masterFlatFrameParameters, documentation=u' Size of the median cleaning filter\n                        [pixel] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MirrorXpix'), pyxb.binding.datatypes.int, scope=masterFlatFrameParameters, documentation=u' Number of pixels to mirror beyond the X\n                        edges of the detector to provide Fourier transform\n                        continuity [pixel] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CombineType'), pyxb.binding.datatypes.int, scope=masterFlatFrameParameters, documentation=u' Index for the type of input (some\n                        combination of dome and/or twilight flat frame) [None] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=masterFlatFrameParameters, documentation=u' Unique EXT object identifier [None] '))
masterFlatFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DigFilterSize')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MirrorXpix')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MirrorYpix')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MedianFilterSize')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CombineType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
masterFlatFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(masterFlatFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



sourceListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=sourceListParameters, documentation=u' Version of the source code [None] '))

sourceListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HtmDepth'), pyxb.binding.datatypes.int, scope=sourceListParameters, documentation=u' Highest level of HTM indexing [None] '))

sourceListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=sourceListParameters, documentation=u' Unique EXT object identifier [None] '))
sourceListParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sourceListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HtmDepth')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
sourceListParameters._ContentModel = pyxb.binding.content.ParticleModel(sourceListParameters._GroupModel, min_occurs=1, max_occurs=1)



illuminationCorrectionRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitParameters'), pyxb.binding.datatypes.float, scope=illuminationCorrectionRecord, documentation=u' List of fit parameters [None] '))

illuminationCorrectionRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ChipName'), pyxb.binding.datatypes.string, scope=illuminationCorrectionRecord, documentation=u' Name of the detector chip [None] '))

illuminationCorrectionRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=illuminationCorrectionRecord, documentation=u' Unique EXT object identifier [None] '))
illuminationCorrectionRecord._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ChipName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FitParameters')), min_occurs=1L, max_occurs=None)
    )
illuminationCorrectionRecord._ContentModel = pyxb.binding.content.ParticleModel(illuminationCorrectionRecord._GroupModel, min_occurs=1, max_occurs=1)



reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), pyxb.binding.datatypes.int, scope=reducedScienceFrameParameters, documentation=u' Overscan correction method index [None] '))

reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImageThreshold'), pyxb.binding.datatypes.float, scope=reducedScienceFrameParameters, documentation=u' Pixel value Sigma-clipping threshold to\n                        estimate source-free background for scaling of fringe\n                        frames [None] '))

reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdLow'), pyxb.binding.datatypes.float, scope=reducedScienceFrameParameters, documentation=u' Lower bound of fringed pixels to include\n                        in scaling [ADU] '))

reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=reducedScienceFrameParameters, documentation=u' Version of the source code [None] '))

reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=reducedScienceFrameParameters, documentation=u' Unique EXT object identifier [None] '))

reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdHigh'), pyxb.binding.datatypes.float, scope=reducedScienceFrameParameters, documentation=u' Upper bound of fringed pixels to include\n                        in scaling [ADU] '))
reducedScienceFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdLow')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdHigh')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImageThreshold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
reducedScienceFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



illuminationCorrectionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=illuminationCorrectionParameters, documentation=u' Unique EXT object identifier [None] '))

illuminationCorrectionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel'), pyxb.binding.datatypes.float, scope=illuminationCorrectionParameters, documentation=u' Sigma clipping threshold from the median\n                        zeropoint [None] '))
illuminationCorrectionParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionParameters._ContentModel = pyxb.binding.content.ParticleModel(illuminationCorrectionParameters._GroupModel, min_occurs=1, max_occurs=1)



illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), euclid.dm.bas.img_stub.instrument, scope=illuminationCorrection, documentation=u' Information about the acquisition\n                                instrument [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=illuminationCorrection, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Records'), illuminationCorrectionRecord, scope=illuminationCorrection, documentation=u' List of illumination correction\n                                records [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagId'), euclid.dm.bas.dtd_stub.nameRestriction, scope=illuminationCorrection, documentation=u' Identifier for the photometric\n                                band [None]'))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), illuminationCorrectionParameters, scope=illuminationCorrection, documentation=u' Processing and verification\n                                parameters [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), euclid.dm.bas.img_stub.filter, scope=illuminationCorrection, documentation=u' Information about the\n                                observational filter [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=illuminationCorrection, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitCoeffs'), pyxb.binding.datatypes.float, scope=illuminationCorrection, documentation=u' List of fit coefficients [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxX'), pyxb.binding.datatypes.float, scope=illuminationCorrection, documentation=u' X coordinate of the source with\n                                the highest X position [pixel] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinY'), pyxb.binding.datatypes.float, scope=illuminationCorrection, documentation=u' Y coordinate of the source with\n                                the lowest Y position [pixel] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinX'), pyxb.binding.datatypes.float, scope=illuminationCorrection, documentation=u' X coordinate of the source with\n                                the lowest X position [pixel] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxY'), pyxb.binding.datatypes.float, scope=illuminationCorrection, documentation=u' Y coordinate of the source with\n                                the highest Y position [pixel] '))
illuminationCorrection._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
illuminationCorrection._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
illuminationCorrection._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrection._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._GroupModel_3, min_occurs=1, max_occurs=1)
    )
illuminationCorrection._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Records')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FitCoeffs')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinY')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxY')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
illuminationCorrection._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrection._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrection._GroupModel_4, min_occurs=1, max_occurs=1)
    )
illuminationCorrection._ContentModel = pyxb.binding.content.ParticleModel(illuminationCorrection._GroupModel, min_occurs=1, max_occurs=1)



rawBiasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasStdev'), pyxb.binding.datatypes.float, scope=rawBiasFrameParameters, documentation=u' QC: Maximum sample standard deviation of\n                        the bias pixel values [ADU] '))

rawBiasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasFlatness'), pyxb.binding.datatypes.float, scope=rawBiasFrameParameters, documentation=u' QC: Maximum difference in subwindow\n                        statistics (minimum minus maximum median values of 32\n                        sub-regions) [ADU] '))

rawBiasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=rawBiasFrameParameters, documentation=u' Unique EXT object identifier [None] '))

rawBiasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasLevel'), pyxb.binding.datatypes.float, scope=rawBiasFrameParameters, documentation=u' QC: Maximum average bias level (mean of\n                        the bias pixel values) [ADU] '))

rawBiasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=rawBiasFrameParameters, documentation=u' Version of the source code [None] '))
rawBiasFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasStdev')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasLevel')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasFlatness')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
rawBiasFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(rawBiasFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'width'), pyxb.binding.datatypes.int, scope=CTD_ANON_3))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flags'), pyxb.binding.datatypes.int, scope=CTD_ANON_3))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CCDReference'), pyxb.binding.datatypes.int, scope=CTD_ANON_3))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuadrantReference'), pyxb.binding.datatypes.int, scope=CTD_ANON_3))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'height'), pyxb.binding.datatypes.int, scope=CTD_ANON_3))
CTD_ANON_3._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QuadrantReference')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CCDReference')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'width')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'height')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flags')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_3._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_3._GroupModel, min_occurs=1, max_occurs=1)



photometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel'), pyxb.binding.datatypes.float, scope=photometricParametersParameters, documentation=u' Sigma clipping threshold factor for raw\n                        zeropoints [None] '))

photometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxError'), pyxb.binding.datatypes.float, scope=photometricParametersParameters, documentation=u' QC: Maximum allowable error in the\n                        zeropoint [mag] '))

photometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinSourceCount'), pyxb.binding.datatypes.int, scope=photometricParametersParameters, documentation=u' QC: Minimum number of sources used in\n                        zeropoint determination [None] '))

photometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=photometricParametersParameters, documentation=u' Version of the source code [None] '))

photometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=photometricParametersParameters, documentation=u' Unique EXT object identifier [None] '))
photometricParametersParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinSourceCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
photometricParametersParameters._ContentModel = pyxb.binding.content.ParticleModel(photometricParametersParameters._GroupModel, min_occurs=1, max_occurs=1)



coaddedRegriddedFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=coaddedRegriddedFrameParameters, documentation=u' Version of the source code [None] '))

coaddedRegriddedFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumPSFDifference'), pyxb.binding.datatypes.float, scope=coaddedRegriddedFrameParameters, documentation=u' QC: Maximum fractional difference between\n                        average psf_radius of input regridded frames and the\n                        coadded regridded frame [None] '))

coaddedRegriddedFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=coaddedRegriddedFrameParameters, documentation=u' Unique EXT object identifier [None] '))
coaddedRegriddedFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumPSFDifference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(coaddedRegriddedFrameParameters._GroupModel, min_occurs=1, max_occurs=1)


coaddedRegriddedFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TypeCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisPipelineFlags')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VISErrorCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VisFitsPixelProcessingFlags')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dithering')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._ContentModel = pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel, min_occurs=1, max_occurs=1)
