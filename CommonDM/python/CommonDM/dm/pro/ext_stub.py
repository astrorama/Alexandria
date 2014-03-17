# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/pro/ext_stub.py
# PyXB bindings for NamespaceModule
# NSM:7474af2c8703d853f14e344b701d79c49bcd3cd8
# Generated 2014-03-17 18:50:36.642440 by PyXB version 1.1.2
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
import CommonDM.dm.bas.img_stub
import pyxb.binding.datatypes
import CommonDM.dm.bas_stub
import CommonDM.dm.sys.sgs_stub
import CommonDM.dm.bas.dtd_stub
import CommonDM.dm.bas.cot_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/ext', create_if_missing=True)
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


# Complex type rawFrame with content type ELEMENT_ONLY
class rawFrame (CommonDM.dm.bas.img_stub.baseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawFrame')
    # Base type is CommonDM.dm.bas.img_stub.baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Ovscy uses Python identifier Ovscy
    __Ovscy = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscy'), 'Ovscy', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextOvscy', False)

    
    Ovscy = property(__Ovscy.value, __Ovscy.set, None, u' Number of overscan pixels in the\n                                Y direction [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Ovscypst uses Python identifier Ovscypst
    __Ovscypst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscypst'), 'Ovscypst', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextOvscypst', False)

    
    Ovscypst = property(__Ovscypst.value, __Ovscypst.set, None, u' Number of overscan pixels to skip\n                                in the Y direction at the edge of the data\n                                region [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}OverscanXStat uses Python identifier OverscanXStat
    __OverscanXStat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanXStat'), 'OverscanXStat', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextOverscanXStat', False)

    
    OverscanXStat = property(__OverscanXStat.value, __OverscanXStat.set, None, u' Statistics of the overscan region\n                                in the X direction [None] ')

    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Prscxpre uses Python identifier Prscxpre
    __Prscxpre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscxpre'), 'Prscxpre', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextPrscxpre', False)

    
    Prscxpre = property(__Prscxpre.value, __Prscxpre.set, None, u' Number of prescan pixels to skip\n                                in the X direction at the edge of the chip\n                                [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Object uses Python identifier Object
    __Object = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Object'), 'Object', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextObject', False)

    
    Object = property(__Object.value, __Object.set, None, u' Name of target object [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PrescanYStat uses Python identifier PrescanYStat
    __PrescanYStat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrescanYStat'), 'PrescanYStat', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextPrescanYStat', False)

    
    PrescanYStat = property(__PrescanYStat.value, __PrescanYStat.set, None, u' Statistics of the prescan region\n                                in the Y direction [None] ')

    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Prscypre uses Python identifier Prscypre
    __Prscypre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscypre'), 'Prscypre', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextPrscypre', False)

    
    Prscypre = property(__Prscypre.value, __Prscypre.set, None, u' Number of prescan pixels to skip\n                                in the Y direction at the edge of the chip\n                                [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Date uses Python identifier Date
    __Date = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Date'), 'Date', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextDate', False)

    
    Date = property(__Date.value, __Date.set, None, u' UTC date the original data file\n                                was saved [None] ')

    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}OverscanYStat uses Python identifier OverscanYStat
    __OverscanYStat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanYStat'), 'OverscanYStat', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextOverscanYStat', False)

    
    OverscanYStat = property(__OverscanYStat.value, __OverscanYStat.set, None, u' Statistics of the overscan region\n                                in the Y direction [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Ovscxpre uses Python identifier Ovscxpre
    __Ovscxpre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpre'), 'Ovscxpre', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextOvscxpre', False)

    
    Ovscxpre = property(__Ovscxpre.value, __Ovscxpre.set, None, u' Number of overscan pixels to skip\n                                in the X direction at the edge of the chip\n                                [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DateObs uses Python identifier DateObs
    __DateObs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), 'DateObs', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextDateObs', False)

    
    DateObs = property(__DateObs.value, __DateObs.set, None, u' UTC date at the start of the\n                                observation [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Ovscypre uses Python identifier Ovscypre
    __Ovscypre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscypre'), 'Ovscypre', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextOvscypre', False)

    
    Ovscypre = property(__Ovscypre.value, __Ovscypre.set, None, u' Number of overscan pixels to skip\n                                in the Y direction at the edge of the chip\n                                [pixel] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}MjdObs uses Python identifier MjdObs
    __MjdObs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MjdObs'), 'MjdObs', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextMjdObs', False)

    
    MjdObs = property(__MjdObs.value, __MjdObs.set, None, u' Modified Julian date at the start\n                                of the observation (JD-2400000.5) [day] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Extension uses Python identifier Extension
    __Extension = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Extension'), 'Extension', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextExtension', False)

    
    Extension = property(__Extension.value, __Extension.set, None, u' Extension number of this frame to\n                                be extracted from the rawFits container [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Prscxpst uses Python identifier Prscxpst
    __Prscxpst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscxpst'), 'Prscxpst', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextPrscxpst', False)

    
    Prscxpst = property(__Prscxpst.value, __Prscxpst.set, None, u' Number of prescan pixels to skip\n                                in the X direction at the edge of the data\n                                region [pixel] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Lst uses Python identifier Lst
    __Lst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Lst'), 'Lst', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextLst', False)

    
    Lst = property(__Lst.value, __Lst.set, None, u' Local sidereal time at the start\n                                of the observation expressed as the number of\n                                seconds (a float) since UTC midnight [sec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RawFits uses Python identifier RawFits
    __RawFits = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawFits'), 'RawFits', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextRawFits', False)

    
    RawFits = property(__RawFits.value, __RawFits.set, None, u' Information about the original\n                                raw image data (multi-extension FITS) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PrescanXStat uses Python identifier PrescanXStat
    __PrescanXStat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrescanXStat'), 'PrescanXStat', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextPrescanXStat', False)

    
    PrescanXStat = property(__PrescanXStat.value, __PrescanXStat.set, None, u' Statistics of the prescan region\n                                in the X direction [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Utc uses Python identifier Utc
    __Utc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Utc'), 'Utc', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextUtc', False)

    
    Utc = property(__Utc.value, __Utc.set, None, u' Universal coordinated time at the\n                                start of the observation expressed as the number\n                                of seconds (a float) since UTC midnight [sec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Ovscxpst uses Python identifier Ovscxpst
    __Ovscxpst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpst'), 'Ovscxpst', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextOvscxpst', False)

    
    Ovscxpst = property(__Ovscxpst.value, __Ovscxpst.set, None, u' Number of overscan pixels to skip\n                                in the X direction at the edge of the data\n                                region [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Prscx uses Python identifier Prscx
    __Prscx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscx'), 'Prscx', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextPrscx', False)

    
    Prscx = property(__Prscx.value, __Prscx.set, None, u' Number of prescan pixels in the X\n                                direction [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Prscy uses Python identifier Prscy
    __Prscy = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscy'), 'Prscy', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextPrscy', False)

    
    Prscy = property(__Prscy.value, __Prscy.set, None, u' Number of prescan pixels in the Y\n                                direction [pixel] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Observer uses Python identifier Observer
    __Observer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Observer'), 'Observer', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextObserver', False)

    
    Observer = property(__Observer.value, __Observer.set, None, u' Information about the observer\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Ovscx uses Python identifier Ovscx
    __Ovscx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ovscx'), 'Ovscx', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextOvscx', False)

    
    Ovscx = property(__Ovscx.value, __Ovscx.set, None, u' Number of overscan pixels in the\n                                X direction [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Prscypst uses Python identifier Prscypst
    __Prscypst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Prscypst'), 'Prscypst', '__httpeuclid_esa_orgschemaproext_rawFrame_httpeuclid_esa_orgschemaproextPrscypst', False)

    
    Prscypst = property(__Prscypst.value, __Prscypst.set, None, u' Number of prescan pixels to skip\n                                in the Y direction at the edge of the data\n                                region [pixel] ')


    _ElementMap = CommonDM.dm.bas.img_stub.baseFrame._ElementMap.copy()
    _ElementMap.update({
        __ObsBlock.name() : __ObsBlock,
        __Ovscy.name() : __Ovscy,
        __Ovscypst.name() : __Ovscypst,
        __OverscanXStat.name() : __OverscanXStat,
        __Prscxpre.name() : __Prscxpre,
        __Object.name() : __Object,
        __PrescanYStat.name() : __PrescanYStat,
        __Prscypre.name() : __Prscypre,
        __Date.name() : __Date,
        __OverscanYStat.name() : __OverscanYStat,
        __Ovscxpre.name() : __Ovscxpre,
        __DateObs.name() : __DateObs,
        __Ovscypre.name() : __Ovscypre,
        __MjdObs.name() : __MjdObs,
        __Extension.name() : __Extension,
        __Prscxpst.name() : __Prscxpst,
        __Lst.name() : __Lst,
        __RawFits.name() : __RawFits,
        __PrescanXStat.name() : __PrescanXStat,
        __Utc.name() : __Utc,
        __Ovscxpst.name() : __Ovscxpst,
        __Prscx.name() : __Prscx,
        __Template.name() : __Template,
        __Chip.name() : __Chip,
        __Prscy.name() : __Prscy,
        __Observer.name() : __Observer,
        __Ovscx.name() : __Ovscx,
        __Prscypst.name() : __Prscypst
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.baseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'rawFrame', rawFrame)


# Complex type saturatedPixelMapParameters with content type ELEMENT_ONLY
class saturatedPixelMapParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'saturatedPixelMapParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ThresholdLow uses Python identifier ThresholdLow
    __ThresholdLow = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ThresholdLow'), 'ThresholdLow', '__httpeuclid_esa_orgschemaproext_saturatedPixelMapParameters_httpeuclid_esa_orgschemaproextThresholdLow', False)

    
    ThresholdLow = property(__ThresholdLow.value, __ThresholdLow.set, None, u' Lower threshold for rejecting pixels with\n                        outlying values [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ThresholdHigh uses Python identifier ThresholdHigh
    __ThresholdHigh = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ThresholdHigh'), 'ThresholdHigh', '__httpeuclid_esa_orgschemaproext_saturatedPixelMapParameters_httpeuclid_esa_orgschemaproextThresholdHigh', False)

    
    ThresholdHigh = property(__ThresholdHigh.value, __ThresholdHigh.set, None, u' Upper threshold for rejecting pixels with\n                        outlying values [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_saturatedPixelMapParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __ThresholdLow.name() : __ThresholdLow,
        __ThresholdHigh.name() : __ThresholdHigh,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'saturatedPixelMapParameters', saturatedPixelMapParameters)


# Complex type pixelMap with content type ELEMENT_ONLY
class pixelMap (CommonDM.dm.bas.img_stub.processTargetDataObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pixelMap')
    # Base type is CommonDM.dm.bas.img_stub.processTargetDataObject
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Count uses Python identifier Count
    __Count = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Count'), 'Count', '__httpeuclid_esa_orgschemaproext_pixelMap_httpeuclid_esa_orgschemaproextCount', False)

    
    Count = property(__Count.value, __Count.set, None, u' Number of pixels marked as bad\n                                (flagged) [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = CommonDM.dm.bas.img_stub.processTargetDataObject._ElementMap.copy()
    _ElementMap.update({
        __Count.name() : __Count
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.processTargetDataObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'pixelMap', pixelMap)


# Complex type saturatedPixelMap with content type ELEMENT_ONLY
class saturatedPixelMap (pixelMap):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'saturatedPixelMap')
    # Base type is pixelMap
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_saturatedPixelMap_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Count ({http://euclid.esa.org/schema/pro/ext}Count) inherited from {http://euclid.esa.org/schema/pro/ext}pixelMap
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}Raw uses Python identifier Raw
    __Raw = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Raw'), 'Raw', '__httpeuclid_esa_orgschemaproext_saturatedPixelMap_httpeuclid_esa_orgschemaproextRaw', False)

    
    Raw = property(__Raw.value, __Raw.set, None, u' Information about the input raw\n                                science frame [None] ')


    _ElementMap = pixelMap._ElementMap.copy()
    _ElementMap.update({
        __ProcessParams.name() : __ProcessParams,
        __Raw.name() : __Raw
    })
    _AttributeMap = pixelMap._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'saturatedPixelMap', saturatedPixelMap)


# Complex type hotPixelMap with content type ELEMENT_ONLY
class hotPixelMap (pixelMap):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hotPixelMap')
    # Base type is pixelMap
    
    # Element {http://euclid.esa.org/schema/pro/ext}Bias uses Python identifier Bias
    __Bias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Bias'), 'Bias', '__httpeuclid_esa_orgschemaproext_hotPixelMap_httpeuclid_esa_orgschemaproextBias', False)

    
    Bias = property(__Bias.value, __Bias.set, None, u' Information about the detector\n                                bias offset levels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_hotPixelMap_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element Count ({http://euclid.esa.org/schema/pro/ext}Count) inherited from {http://euclid.esa.org/schema/pro/ext}pixelMap
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}SexConfig uses Python identifier SexConfig
    __SexConfig = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), 'SexConfig', '__httpeuclid_esa_orgschemaproext_hotPixelMap_httpeuclid_esa_orgschemaproextSexConfig', False)

    
    SexConfig = property(__SexConfig.value, __SexConfig.set, None, u' SExtractor configuration for\n                                background determination [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_hotPixelMap_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_hotPixelMap_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_hotPixelMap_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_hotPixelMap_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_hotPixelMap_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_hotPixelMap_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')


    _ElementMap = pixelMap._ElementMap.copy()
    _ElementMap.update({
        __Bias.name() : __Bias,
        __ObsBlock.name() : __ObsBlock,
        __SexConfig.name() : __SexConfig,
        __Template.name() : __Template,
        __Chip.name() : __Chip,
        __ProcessParams.name() : __ProcessParams,
        __TimestampStart.name() : __TimestampStart,
        __Instrument.name() : __Instrument,
        __TimestampEnd.name() : __TimestampEnd
    })
    _AttributeMap = pixelMap._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'hotPixelMap', hotPixelMap)


# Complex type coldPixelMap with content type ELEMENT_ONLY
class coldPixelMap (pixelMap):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coldPixelMap')
    # Base type is pixelMap
    
    # Element {http://euclid.esa.org/schema/pro/ext}Flat uses Python identifier Flat
    __Flat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flat'), 'Flat', '__httpeuclid_esa_orgschemaproext_coldPixelMap_httpeuclid_esa_orgschemaproextFlat', False)

    
    Flat = property(__Flat.value, __Flat.set, None, u' Information about the detector\n                                sensitivity variations [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}SexConfig uses Python identifier SexConfig
    __SexConfig = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), 'SexConfig', '__httpeuclid_esa_orgschemaproext_coldPixelMap_httpeuclid_esa_orgschemaproextSexConfig', False)

    
    SexConfig = property(__SexConfig.value, __SexConfig.set, None, u' SExtractor configuration for\n                                background determination [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_coldPixelMap_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_coldPixelMap_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Count ({http://euclid.esa.org/schema/pro/ext}Count) inherited from {http://euclid.esa.org/schema/pro/ext}pixelMap
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_coldPixelMap_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_coldPixelMap_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_coldPixelMap_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_coldPixelMap_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_coldPixelMap_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_coldPixelMap_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = pixelMap._ElementMap.copy()
    _ElementMap.update({
        __Flat.name() : __Flat,
        __SexConfig.name() : __SexConfig,
        __Filter.name() : __Filter,
        __TimestampEnd.name() : __TimestampEnd,
        __ProcessParams.name() : __ProcessParams,
        __Instrument.name() : __Instrument,
        __Template.name() : __Template,
        __TimestampStart.name() : __TimestampStart,
        __Chip.name() : __Chip,
        __ObsBlock.name() : __ObsBlock
    })
    _AttributeMap = pixelMap._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'coldPixelMap', coldPixelMap)


# Complex type baseFlatFrame with content type ELEMENT_ONLY
class baseFlatFrame (CommonDM.dm.bas.img_stub.baseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseFlatFrame')
    # Base type is CommonDM.dm.bas.img_stub.baseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_baseFlatFrame_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_baseFlatFrame_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_baseFlatFrame_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_baseFlatFrame_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = CommonDM.dm.bas.img_stub.baseFrame._ElementMap.copy()
    _ElementMap.update({
        __TimestampStart.name() : __TimestampStart,
        __Filter.name() : __Filter,
        __TimestampEnd.name() : __TimestampEnd,
        __Chip.name() : __Chip
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.baseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'baseFlatFrame', baseFlatFrame)


# Complex type masterFlatFrame with content type ELEMENT_ONLY
class masterFlatFrame (baseFlatFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'masterFlatFrame')
    # Base type is baseFlatFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Hot uses Python identifier Hot
    __Hot = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Hot'), 'Hot', '__httpeuclid_esa_orgschemaproext_masterFlatFrame_httpeuclid_esa_orgschemaproextHot', False)

    
    Hot = property(__Hot.value, __Hot.set, None, u' Information about the detector\n                                hot pixels [None] ')

    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/ext}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Filter ({http://euclid.esa.org/schema/pro/ext}Filter) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}TwilightFlat uses Python identifier TwilightFlat
    __TwilightFlat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TwilightFlat'), 'TwilightFlat', '__httpeuclid_esa_orgschemaproext_masterFlatFrame_httpeuclid_esa_orgschemaproextTwilightFlat', False)

    
    TwilightFlat = property(__TwilightFlat.value, __TwilightFlat.set, None, u' Information about the input\n                                twilight flat frame [None] ')

    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Cold uses Python identifier Cold
    __Cold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cold'), 'Cold', '__httpeuclid_esa_orgschemaproext_masterFlatFrame_httpeuclid_esa_orgschemaproextCold', False)

    
    Cold = property(__Cold.value, __Cold.set, None, u' Information about the detector\n                                cold pixels [None] ')

    
    # Element Chip ({http://euclid.esa.org/schema/pro/ext}Chip) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}DomeFlat uses Python identifier DomeFlat
    __DomeFlat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DomeFlat'), 'DomeFlat', '__httpeuclid_esa_orgschemaproext_masterFlatFrame_httpeuclid_esa_orgschemaproextDomeFlat', False)

    
    DomeFlat = property(__DomeFlat.value, __DomeFlat.set, None, u' Information about the input dome\n                                flat frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}NightSkyFlat uses Python identifier NightSkyFlat
    __NightSkyFlat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NightSkyFlat'), 'NightSkyFlat', '__httpeuclid_esa_orgschemaproext_masterFlatFrame_httpeuclid_esa_orgschemaproextNightSkyFlat', False)

    
    NightSkyFlat = property(__NightSkyFlat.value, __NightSkyFlat.set, None, u' Information about the input\n                                night-sky flat frame [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/ext}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_masterFlatFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = baseFlatFrame._ElementMap.copy()
    _ElementMap.update({
        __Hot.name() : __Hot,
        __TwilightFlat.name() : __TwilightFlat,
        __Cold.name() : __Cold,
        __DomeFlat.name() : __DomeFlat,
        __NightSkyFlat.name() : __NightSkyFlat,
        __ProcessParams.name() : __ProcessParams
    })
    _AttributeMap = baseFlatFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'masterFlatFrame', masterFlatFrame)


# Complex type illuminationCorrectionFrame with content type ELEMENT_ONLY
class illuminationCorrectionFrame (CommonDM.dm.bas.img_stub.baseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminationCorrectionFrame')
    # Base type is CommonDM.dm.bas.img_stub.baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}IlluminationCorrection uses Python identifier IlluminationCorrection
    __IlluminationCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IlluminationCorrection'), 'IlluminationCorrection', '__httpeuclid_esa_orgschemaproext_illuminationCorrectionFrame_httpeuclid_esa_orgschemaproextIlluminationCorrection', False)

    
    IlluminationCorrection = property(__IlluminationCorrection.value, __IlluminationCorrection.set, None, u' Information about the\n                                illumination correction [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_illuminationCorrectionFrame_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_illuminationCorrectionFrame_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_illuminationCorrectionFrame_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_illuminationCorrectionFrame_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = CommonDM.dm.bas.img_stub.baseFrame._ElementMap.copy()
    _ElementMap.update({
        __IlluminationCorrection.name() : __IlluminationCorrection,
        __Filter.name() : __Filter,
        __TimestampStart.name() : __TimestampStart,
        __Chip.name() : __Chip,
        __TimestampEnd.name() : __TimestampEnd
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.baseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'illuminationCorrectionFrame', illuminationCorrectionFrame)


# Complex type baseAtmosphericExtinction with content type ELEMENT_ONLY
class baseAtmosphericExtinction (CommonDM.dm.bas.img_stub.processTarget):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseAtmosphericExtinction')
    # Base type is CommonDM.dm.bas.img_stub.processTarget
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_baseAtmosphericExtinction_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtinctionCurve uses Python identifier ExtinctionCurve
    __ExtinctionCurve = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtinctionCurve'), 'ExtinctionCurve', '__httpeuclid_esa_orgschemaproext_baseAtmosphericExtinction_httpeuclid_esa_orgschemaproextExtinctionCurve', False)

    
    ExtinctionCurve = property(__ExtinctionCurve.value, __ExtinctionCurve.set, None, u' Information about the atmospheric\n                                extinction curve [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemaproext_baseAtmosphericExtinction_httpeuclid_esa_orgschemaproextValue', False)

    
    Value = property(__Value.value, __Value.set, None, u' Value of the atmospheric\n                                extinction [mag / airmass]')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_baseAtmosphericExtinction_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Error uses Python identifier Error
    __Error = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Error'), 'Error', '__httpeuclid_esa_orgschemaproext_baseAtmosphericExtinction_httpeuclid_esa_orgschemaproextError', False)

    
    Error = property(__Error.value, __Error.set, None, u' Error on atmospheric extinction\n                                [mag / airmass]')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MagId uses Python identifier MagId
    __MagId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagId'), 'MagId', '__httpeuclid_esa_orgschemaproext_baseAtmosphericExtinction_httpeuclid_esa_orgschemaproextMagId', False)

    
    MagId = property(__MagId.value, __MagId.set, None, u' Identifier for the photometric\n                                band [None]')


    _ElementMap = CommonDM.dm.bas.img_stub.processTarget._ElementMap.copy()
    _ElementMap.update({
        __Instrument.name() : __Instrument,
        __ExtinctionCurve.name() : __ExtinctionCurve,
        __Value.name() : __Value,
        __Filter.name() : __Filter,
        __Error.name() : __Error,
        __MagId.name() : __MagId
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.processTarget._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'baseAtmosphericExtinction', baseAtmosphericExtinction)


# Complex type atmosphericExtinction with content type ELEMENT_ONLY
class atmosphericExtinction (baseAtmosphericExtinction):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'atmosphericExtinction')
    # Base type is baseAtmosphericExtinction
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_atmosphericExtinction_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element ExtinctionCurve ({http://euclid.esa.org/schema/pro/ext}ExtinctionCurve) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Value ({http://euclid.esa.org/schema/pro/ext}Value) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction
    
    # Element {http://euclid.esa.org/schema/pro/ext}Polar uses Python identifier Polar
    __Polar = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Polar'), 'Polar', '__httpeuclid_esa_orgschemaproext_atmosphericExtinction_httpeuclid_esa_orgschemaproextPolar', True)

    
    Polar = property(__Polar.value, __Polar.set, None, u' List of input photometric source\n                                catalogs [none] ')

    
    # Element Filter ({http://euclid.esa.org/schema/pro/ext}Filter) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Error ({http://euclid.esa.org/schema/pro/ext}Error) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction
    
    # Element MagId ({http://euclid.esa.org/schema/pro/ext}MagId) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction
    
    # Element Instrument ({http://euclid.esa.org/schema/pro/ext}Instrument) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction

    _ElementMap = baseAtmosphericExtinction._ElementMap.copy()
    _ElementMap.update({
        __ProcessParams.name() : __ProcessParams,
        __Polar.name() : __Polar
    })
    _AttributeMap = baseAtmosphericExtinction._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'atmosphericExtinction', atmosphericExtinction)


# Complex type reducedScienceFrameParameters with content type ELEMENT_ONLY
class reducedScienceFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reducedScienceFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_reducedScienceFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FringeThresholdHigh uses Python identifier FringeThresholdHigh
    __FringeThresholdHigh = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdHigh'), 'FringeThresholdHigh', '__httpeuclid_esa_orgschemaproext_reducedScienceFrameParameters_httpeuclid_esa_orgschemaproextFringeThresholdHigh', False)

    
    FringeThresholdHigh = property(__FringeThresholdHigh.value, __FringeThresholdHigh.set, None, u' Upper bound of fringed pixels to include\n                        in scaling [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}OverscanCorrection uses Python identifier OverscanCorrection
    __OverscanCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), 'OverscanCorrection', '__httpeuclid_esa_orgschemaproext_reducedScienceFrameParameters_httpeuclid_esa_orgschemaproextOverscanCorrection', False)

    
    OverscanCorrection = property(__OverscanCorrection.value, __OverscanCorrection.set, None, u' Overscan correction method index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ImageThreshold uses Python identifier ImageThreshold
    __ImageThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImageThreshold'), 'ImageThreshold', '__httpeuclid_esa_orgschemaproext_reducedScienceFrameParameters_httpeuclid_esa_orgschemaproextImageThreshold', False)

    
    ImageThreshold = property(__ImageThreshold.value, __ImageThreshold.set, None, u' Pixel value Sigma-clipping threshold to\n                        estimate source-free background for scaling of fringe\n                        frames [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FringeThresholdLow uses Python identifier FringeThresholdLow
    __FringeThresholdLow = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdLow'), 'FringeThresholdLow', '__httpeuclid_esa_orgschemaproext_reducedScienceFrameParameters_httpeuclid_esa_orgschemaproextFringeThresholdLow', False)

    
    FringeThresholdLow = property(__FringeThresholdLow.value, __FringeThresholdLow.set, None, u' Lower bound of fringed pixels to include\n                        in scaling [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_reducedScienceFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __FringeThresholdHigh.name() : __FringeThresholdHigh,
        __OverscanCorrection.name() : __OverscanCorrection,
        __ImageThreshold.name() : __ImageThreshold,
        __FringeThresholdLow.name() : __FringeThresholdLow,
        __SourceCodeVersion.name() : __SourceCodeVersion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'reducedScienceFrameParameters', reducedScienceFrameParameters)


# Complex type zeroPoint with content type ELEMENT_ONLY
class zeroPoint (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'zeroPoint')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemaproext_zeroPoint_httpeuclid_esa_orgschemaproextValue', False)

    
    Value = property(__Value.value, __Value.set, None, u' Value of the photometric zeropoint [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Error uses Python identifier Error
    __Error = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Error'), 'Error', '__httpeuclid_esa_orgschemaproext_zeroPoint_httpeuclid_esa_orgschemaproextError', False)

    
    Error = property(__Error.value, __Error.set, None, u' Error on the value of the photometric\n                        zeropoint [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_zeroPoint_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __Value.name() : __Value,
        __Error.name() : __Error,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'zeroPoint', zeroPoint)


# Complex type rawTwilightFlatFrameParameters with content type ELEMENT_ONLY
class rawTwilightFlatFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawTwilightFlatFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_rawTwilightFlatFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxFlatMean uses Python identifier MaxFlatMean
    __MaxFlatMean = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxFlatMean'), 'MaxFlatMean', '__httpeuclid_esa_orgschemaproext_rawTwilightFlatFrameParameters_httpeuclid_esa_orgschemaproextMaxFlatMean', False)

    
    MaxFlatMean = property(__MaxFlatMean.value, __MaxFlatMean.set, None, u' QC: Maximum level of the flat (mean of\n                        the flat pixel values) [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MinFlatMean uses Python identifier MinFlatMean
    __MinFlatMean = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinFlatMean'), 'MinFlatMean', '__httpeuclid_esa_orgschemaproext_rawTwilightFlatFrameParameters_httpeuclid_esa_orgschemaproextMinFlatMean', False)

    
    MinFlatMean = property(__MinFlatMean.value, __MinFlatMean.set, None, u' QC: Minimum level of the flat (mean of\n                        the flat pixel values) [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_rawTwilightFlatFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __MaxFlatMean.name() : __MaxFlatMean,
        __MinFlatMean.name() : __MinFlatMean,
        __SourceCodeVersion.name() : __SourceCodeVersion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'rawTwilightFlatFrameParameters', rawTwilightFlatFrameParameters)


# Complex type illuminationCorrectionRecord with content type ELEMENT_ONLY
class illuminationCorrectionRecord (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminationCorrectionRecord')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ChipName uses Python identifier ChipName
    __ChipName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ChipName'), 'ChipName', '__httpeuclid_esa_orgschemaproext_illuminationCorrectionRecord_httpeuclid_esa_orgschemaproextChipName', False)

    
    ChipName = property(__ChipName.value, __ChipName.set, None, u' Name of the detector chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FitParameters uses Python identifier FitParameters
    __FitParameters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FitParameters'), 'FitParameters', '__httpeuclid_esa_orgschemaproext_illuminationCorrectionRecord_httpeuclid_esa_orgschemaproextFitParameters', True)

    
    FitParameters = property(__FitParameters.value, __FitParameters.set, None, u' List of fit parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_illuminationCorrectionRecord_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __ChipName.name() : __ChipName,
        __FitParameters.name() : __FitParameters,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'illuminationCorrectionRecord', illuminationCorrectionRecord)


# Complex type photRefCatalog with content type ELEMENT_ONLY
class photRefCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photRefCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}Storage uses Python identifier Storage
    __Storage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Storage'), 'Storage', '__httpeuclid_esa_orgschemaproext_photRefCatalog_httpeuclid_esa_orgschemaproextStorage', False)

    
    Storage = property(__Storage.value, __Storage.set, None, u' Customized storage container for the data\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), 'CreationDate', '__httpeuclid_esa_orgschemaproext_photRefCatalog_httpeuclid_esa_orgschemaproextCreationDate', False)

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, u' UTC date this object was created [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_photRefCatalog_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __Storage.name() : __Storage,
        __CreationDate.name() : __CreationDate,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'photRefCatalog', photRefCatalog)


# Complex type astrometricParameters with content type ELEMENT_ONLY
class astrometricParameters (CommonDM.dm.bas.img_stub.processTarget):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'astrometricParameters')
    # Base type is CommonDM.dm.bas.img_stub.processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_4 uses Python identifier PV1_4
    __PV1_4 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_4'), 'PV1_4', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_4', False)

    
    PV1_4 = property(__PV1_4.value, __PV1_4.set, None, u' Non-linear transformation matrix\n                                parameter value b1,4 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}AstromConfig uses Python identifier AstromConfig
    __AstromConfig = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AstromConfig'), 'AstromConfig', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextAstromConfig', False)

    
    AstromConfig = property(__AstromConfig.value, __AstromConfig.set, None, u' LDAC.astrom configuration [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}CRVAL2 uses Python identifier CRVAL2
    __CRVAL2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRVAL2'), 'CRVAL2', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextCRVAL2', False)

    
    CRVAL2 = property(__CRVAL2.value, __CRVAL2.set, None, u' Physical value of the reference\n                                pixel Y [deg] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}SigmaDdecOverlap uses Python identifier SigmaDdecOverlap
    __SigmaDdecOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaDdecOverlap'), 'SigmaDdecOverlap', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextSigmaDdecOverlap', False)

    
    SigmaDdecOverlap = property(__SigmaDdecOverlap.value, __SigmaDdecOverlap.set, None, u' Sample standard deviation of\n                                overlap residuals in declination [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_0 uses Python identifier PV2_0
    __PV2_0 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_0'), 'PV2_0', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_0', False)

    
    PV2_0 = property(__PV2_0.value, __PV2_0.set, None, u' Non-linear transformation matrix\n                                parameter value c0 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_7 uses Python identifier PV2_7
    __PV2_7 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_7'), 'PV2_7', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_7', False)

    
    PV2_7 = property(__PV2_7.value, __PV2_7.set, None, u' Non-linear transformation matrix\n                                parameter value d1,7 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Gastrom uses Python identifier Gastrom
    __Gastrom = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Gastrom'), 'Gastrom', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextGastrom', False)

    
    Gastrom = property(__Gastrom.value, __Gastrom.set, None, u' Information about the global\n                                astrometric solution [None]')

    
    # Element {http://euclid.esa.org/schema/pro/ext}XError uses Python identifier XError
    __XError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XError'), 'XError', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextXError', False)

    
    XError = property(__XError.value, __XError.set, None, u' Error in polynomial X coefficient\n                                [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CTYPE1 uses Python identifier CTYPE1
    __CTYPE1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CTYPE1'), 'CTYPE1', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextCTYPE1', False)

    
    CTYPE1 = property(__CTYPE1.value, __CTYPE1.set, None, u' Pixel coordinate system and\n                                projection of first axis (X) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_5 uses Python identifier PV1_5
    __PV1_5 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_5'), 'PV1_5', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_5', False)

    
    PV1_5 = property(__PV1_5.value, __PV1_5.set, None, u' Non-linear transformation matrix\n                                parameter value b1,5 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}NRef uses Python identifier NRef
    __NRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NRef'), 'NRef', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextNRef', False)

    
    NRef = property(__NRef.value, __NRef.set, None, u' Number of reference pairings used\n                                in the astrometric solution [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_6 uses Python identifier PV2_6
    __PV2_6 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_6'), 'PV2_6', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_6', False)

    
    PV2_6 = property(__PV2_6.value, __PV2_6.set, None, u' Non-linear transformation matrix\n                                parameter value d1,6 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_3 uses Python identifier PV1_3
    __PV1_3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_3'), 'PV1_3', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_3', False)

    
    PV1_3 = property(__PV1_3.value, __PV1_3.set, None, u' Non-linear transformation matrix\n                                parameter value b1,3 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}AssociateConfig uses Python identifier AssociateConfig
    __AssociateConfig = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AssociateConfig'), 'AssociateConfig', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextAssociateConfig', False)

    
    AssociateConfig = property(__AssociateConfig.value, __AssociateConfig.set, None, u' LDAC.associate configuration\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_2 uses Python identifier PV2_2
    __PV2_2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_2'), 'PV2_2', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_2', False)

    
    PV2_2 = property(__PV2_2.value, __PV2_2.set, None, u' Non-linear transformation matrix\n                                parameter value d1,2 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}NFitParm uses Python identifier NFitParm
    __NFitParm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NFitParm'), 'NFitParm', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextNFitParm', False)

    
    NFitParm = property(__NFitParm.value, __NFitParm.set, None, u' Number of fitted parameters\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CD1_2 uses Python identifier CD1_2
    __CD1_2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD1_2'), 'CD1_2', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextCD1_2', False)

    
    CD1_2 = property(__CD1_2.value, __CD1_2.set, None, u' Linear transformation matrix\n                                parameter at i,j=1,2 (a2) [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_6 uses Python identifier PV1_6
    __PV1_6 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_6'), 'PV1_6', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_6', False)

    
    PV1_6 = property(__PV1_6.value, __PV1_6.set, None, u' Non-linear transformation matrix\n                                parameter value b1,6 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FitParams uses Python identifier FitParams
    __FitParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FitParams'), 'FitParams', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextFitParams', True)

    
    FitParams = property(__FitParams.value, __FitParams.set, None, u' Degrees of freedom of fitted\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_4 uses Python identifier PV2_4
    __PV2_4 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_4'), 'PV2_4', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_4', False)

    
    PV2_4 = property(__PV2_4.value, __PV2_4.set, None, u' Non-linear transformation matrix\n                                parameter value d1,4 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CD2_1 uses Python identifier CD2_1
    __CD2_1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD2_1'), 'CD2_1', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextCD2_1', False)

    
    CD2_1 = property(__CD2_1.value, __CD2_1.set, None, u' Linear transformation matrix\n                                parameter at i,j=2,1 (b1) [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_9 uses Python identifier PV2_9
    __PV2_9 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_9'), 'PV2_9', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_9', False)

    
    PV2_9 = property(__PV2_9.value, __PV2_9.set, None, u' Non-linear transformation matrix\n                                parameter value d1,9 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CTYPE2 uses Python identifier CTYPE2
    __CTYPE2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CTYPE2'), 'CTYPE2', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextCTYPE2', False)

    
    CTYPE2 = property(__CTYPE2.value, __CTYPE2.set, None, u' Pixel coordinate system and\n                                projection of second axis (Y) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_9 uses Python identifier PV1_9
    __PV1_9 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_9'), 'PV1_9', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_9', False)

    
    PV1_9 = property(__PV1_9.value, __PV1_9.set, None, u' Non-linear transformation matrix\n                                parameter value b1,9 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FitErrors uses Python identifier FitErrors
    __FitErrors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FitErrors'), 'FitErrors', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextFitErrors', True)

    
    FitErrors = property(__FitErrors.value, __FitErrors.set, None, u' Errors on fitted parameters [rad] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CD2_2 uses Python identifier CD2_2
    __CD2_2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD2_2'), 'CD2_2', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextCD2_2', False)

    
    CD2_2 = property(__CD2_2.value, __CD2_2.set, None, u' Linear transformation matrix\n                                parameter at i,j=2,2 (b2) [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CD1_1 uses Python identifier CD1_1
    __CD1_1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD1_1'), 'CD1_1', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextCD1_1', False)

    
    CD1_1 = property(__CD1_1.value, __CD1_1.set, None, u' Linear transformation matrix\n                                parameter at i,j=1,1 (a1) [deg] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}FieldError uses Python identifier FieldError
    __FieldError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FieldError'), 'FieldError', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextFieldError', False)

    
    FieldError = property(__FieldError.value, __FieldError.set, None, u' Global position error [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SexConfig uses Python identifier SexConfig
    __SexConfig = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), 'SexConfig', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextSexConfig', False)

    
    SexConfig = property(__SexConfig.value, __SexConfig.set, None, u' SExtractor configuration for\n                                source extraction [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_10 uses Python identifier PV1_10
    __PV1_10 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_10'), 'PV1_10', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_10', False)

    
    PV1_10 = property(__PV1_10.value, __PV1_10.set, None, u' Non-linear transformation matrix\n                                parameter value b1,10 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MeanDraOverlap uses Python identifier MeanDraOverlap
    __MeanDraOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MeanDraOverlap'), 'MeanDraOverlap', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextMeanDraOverlap', False)

    
    MeanDraOverlap = property(__MeanDraOverlap.value, __MeanDraOverlap.set, None, u' Average overlap residual in right\n                                ascension [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_10 uses Python identifier PV2_10
    __PV2_10 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_10'), 'PV2_10', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_10', False)

    
    PV2_10 = property(__PV2_10.value, __PV2_10.set, None, u' Non-linear transformation matrix\n                                parameter value d1,10 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_1 uses Python identifier PV1_1
    __PV1_1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_1'), 'PV1_1', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_1', False)

    
    PV1_1 = property(__PV1_1.value, __PV1_1.set, None, u' Non-linear transformation matrix\n                                parameter value b1,1 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_8 uses Python identifier PV1_8
    __PV1_8 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_8'), 'PV1_8', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_8', False)

    
    PV1_8 = property(__PV1_8.value, __PV1_8.set, None, u' Non-linear transformation matrix\n                                parameter value b1,8 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_8 uses Python identifier PV2_8
    __PV2_8 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_8'), 'PV2_8', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_8', False)

    
    PV2_8 = property(__PV2_8.value, __PV2_8.set, None, u' Non-linear transformation matrix\n                                parameter value d1,8 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}NOverlap uses Python identifier NOverlap
    __NOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NOverlap'), 'NOverlap', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextNOverlap', False)

    
    NOverlap = property(__NOverlap.value, __NOverlap.set, None, u' Number of overlap pairings used\n                                in the astrometric solution [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MeanDdecOverlap uses Python identifier MeanDdecOverlap
    __MeanDdecOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MeanDdecOverlap'), 'MeanDdecOverlap', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextMeanDdecOverlap', False)

    
    MeanDdecOverlap = property(__MeanDdecOverlap.value, __MeanDdecOverlap.set, None, u' Average overlap residual in\n                                declination [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SigmaDra uses Python identifier SigmaDra
    __SigmaDra = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaDra'), 'SigmaDra', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextSigmaDra', False)

    
    SigmaDra = property(__SigmaDra.value, __SigmaDra.set, None, u' Sample standard deviation of\n                                reference residuals in right ascension [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MeanDra uses Python identifier MeanDra
    __MeanDra = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MeanDra'), 'MeanDra', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextMeanDra', False)

    
    MeanDra = property(__MeanDra.value, __MeanDra.set, None, u' Average reference residual in\n                                right ascension [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CRVAL1 uses Python identifier CRVAL1
    __CRVAL1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRVAL1'), 'CRVAL1', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextCRVAL1', False)

    
    CRVAL1 = property(__CRVAL1.value, __CRVAL1.set, None, u' Physical value of the reference\n                                pixel X [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CRPIX2 uses Python identifier CRPIX2
    __CRPIX2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRPIX2'), 'CRPIX2', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextCRPIX2', False)

    
    CRPIX2 = property(__CRPIX2.value, __CRPIX2.set, None, u' Reference pixel in Y [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}YyError uses Python identifier YyError
    __YyError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YyError'), 'YyError', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextYyError', False)

    
    YyError = property(__YyError.value, __YyError.set, None, u' Error in polynomial YY\n                                coefficient [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SigmaDdec uses Python identifier SigmaDdec
    __SigmaDdec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaDdec'), 'SigmaDdec', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextSigmaDdec', False)

    
    SigmaDdec = property(__SigmaDdec.value, __SigmaDdec.set, None, u' Sample standard deviation of\n                                reference residuals in declination [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}YError uses Python identifier YError
    __YError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YError'), 'YError', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextYError', False)

    
    YError = property(__YError.value, __YError.set, None, u' Error in polynomial Y coefficient\n                                [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SigmaDraOverlap uses Python identifier SigmaDraOverlap
    __SigmaDraOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaDraOverlap'), 'SigmaDraOverlap', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextSigmaDraOverlap', False)

    
    SigmaDraOverlap = property(__SigmaDraOverlap.value, __SigmaDraOverlap.set, None, u' Sample standard deviation of\n                                overlap residuals in right ascension [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Rms uses Python identifier Rms
    __Rms = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Rms'), 'Rms', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextRms', False)

    
    Rms = property(__Rms.value, __Rms.set, None, u' Two-dimensional root-mean-square\n                                of reference residuals [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_1 uses Python identifier PV2_1
    __PV2_1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_1'), 'PV2_1', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_1', False)

    
    PV2_1 = property(__PV2_1.value, __PV2_1.set, None, u' Non-linear transformation matrix\n                                parameter value d1,1 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_2 uses Python identifier PV1_2
    __PV1_2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_2'), 'PV1_2', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_2', False)

    
    PV1_2 = property(__PV1_2.value, __PV1_2.set, None, u' Non-linear transformation matrix\n                                parameter value b1,2 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_0 uses Python identifier PV1_0
    __PV1_0 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_0'), 'PV1_0', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_0', False)

    
    PV1_0 = property(__PV1_0.value, __PV1_0.set, None, u' Non-linear transformation matrix\n                                parameter value a0 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}XxError uses Python identifier XxError
    __XxError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XxError'), 'XxError', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextXxError', False)

    
    XxError = property(__XxError.value, __XxError.set, None, u' Error in polynomial XX\n                                coefficient [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV1_7 uses Python identifier PV1_7
    __PV1_7 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV1_7'), 'PV1_7', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV1_7', False)

    
    PV1_7 = property(__PV1_7.value, __PV1_7.set, None, u' Non-linear transformation matrix\n                                parameter value b1,7 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Seeing uses Python identifier Seeing
    __Seeing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), 'Seeing', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextSeeing', False)

    
    Seeing = property(__Seeing.value, __Seeing.set, None, u' Estimate of seeing using the\n                                median FWHM (filtered to isolate most\n                                stellar-like sources) [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_3 uses Python identifier PV2_3
    __PV2_3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_3'), 'PV2_3', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_3', False)

    
    PV2_3 = property(__PV2_3.value, __PV2_3.set, None, u' Non-linear transformation matrix\n                                parameter value d1,3 [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CRPIX1 uses Python identifier CRPIX1
    __CRPIX1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRPIX1'), 'CRPIX1', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextCRPIX1', False)

    
    CRPIX1 = property(__CRPIX1.value, __CRPIX1.set, None, u' Reference pixel in X [pixel] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}MeanDdec uses Python identifier MeanDdec
    __MeanDdec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MeanDdec'), 'MeanDdec', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextMeanDdec', False)

    
    MeanDdec = property(__MeanDdec.value, __MeanDdec.set, None, u' Average reference residual in\n                                declination [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RefcatSlid uses Python identifier RefcatSlid
    __RefcatSlid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RefcatSlid'), 'RefcatSlid', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextRefcatSlid', False)

    
    RefcatSlid = property(__RefcatSlid.value, __RefcatSlid.set, None, u' The ID of the source list used\n                                for the reference catalog [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PreastromConfig uses Python identifier PreastromConfig
    __PreastromConfig = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PreastromConfig'), 'PreastromConfig', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPreastromConfig', False)

    
    PreastromConfig = property(__PreastromConfig.value, __PreastromConfig.set, None, u' LDAC.preastrom configuration\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}XyError uses Python identifier XyError
    __XyError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XyError'), 'XyError', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextXyError', False)

    
    XyError = property(__XyError.value, __XyError.set, None, u' Error in polynomial XY\n                                coefficient [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Reduced uses Python identifier Reduced
    __Reduced = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Reduced'), 'Reduced', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextReduced', False)

    
    Reduced = property(__Reduced.value, __Reduced.set, None, u' Information about the input\n                                reduced science frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RmsOverlap uses Python identifier RmsOverlap
    __RmsOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RmsOverlap'), 'RmsOverlap', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextRmsOverlap', False)

    
    RmsOverlap = property(__RmsOverlap.value, __RmsOverlap.set, None, u' Two-dimensional root-mean-square\n                                of overlap residuals [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Residuals uses Python identifier Residuals
    __Residuals = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Residuals'), 'Residuals', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextResiduals', False)

    
    Residuals = property(__Residuals.value, __Residuals.set, None, u' Filename of residuals FITS table\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PV2_5 uses Python identifier PV2_5
    __PV2_5 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PV2_5'), 'PV2_5', '__httpeuclid_esa_orgschemaproext_astrometricParameters_httpeuclid_esa_orgschemaproextPV2_5', False)

    
    PV2_5 = property(__PV2_5.value, __PV2_5.set, None, u' Non-linear transformation matrix\n                                parameter value d1,5 [None] ')


    _ElementMap = CommonDM.dm.bas.img_stub.processTarget._ElementMap.copy()
    _ElementMap.update({
        __PV1_4.name() : __PV1_4,
        __AstromConfig.name() : __AstromConfig,
        __CRVAL2.name() : __CRVAL2,
        __SigmaDdecOverlap.name() : __SigmaDdecOverlap,
        __PV2_0.name() : __PV2_0,
        __PV2_7.name() : __PV2_7,
        __Gastrom.name() : __Gastrom,
        __XError.name() : __XError,
        __CTYPE1.name() : __CTYPE1,
        __Template.name() : __Template,
        __PV1_5.name() : __PV1_5,
        __NRef.name() : __NRef,
        __Filter.name() : __Filter,
        __PV2_6.name() : __PV2_6,
        __PV1_3.name() : __PV1_3,
        __AssociateConfig.name() : __AssociateConfig,
        __PV2_2.name() : __PV2_2,
        __NFitParm.name() : __NFitParm,
        __CD1_2.name() : __CD1_2,
        __PV1_6.name() : __PV1_6,
        __ObsBlock.name() : __ObsBlock,
        __FitParams.name() : __FitParams,
        __PV2_4.name() : __PV2_4,
        __CD2_1.name() : __CD2_1,
        __PV2_9.name() : __PV2_9,
        __CTYPE2.name() : __CTYPE2,
        __PV1_9.name() : __PV1_9,
        __Instrument.name() : __Instrument,
        __FitErrors.name() : __FitErrors,
        __CD2_2.name() : __CD2_2,
        __CD1_1.name() : __CD1_1,
        __FieldError.name() : __FieldError,
        __SexConfig.name() : __SexConfig,
        __PV1_10.name() : __PV1_10,
        __MeanDraOverlap.name() : __MeanDraOverlap,
        __PV2_10.name() : __PV2_10,
        __PV1_1.name() : __PV1_1,
        __PV1_8.name() : __PV1_8,
        __PV2_8.name() : __PV2_8,
        __NOverlap.name() : __NOverlap,
        __MeanDdecOverlap.name() : __MeanDdecOverlap,
        __SigmaDra.name() : __SigmaDra,
        __ProcessParams.name() : __ProcessParams,
        __MeanDra.name() : __MeanDra,
        __CRVAL1.name() : __CRVAL1,
        __CRPIX2.name() : __CRPIX2,
        __YyError.name() : __YyError,
        __SigmaDdec.name() : __SigmaDdec,
        __YError.name() : __YError,
        __SigmaDraOverlap.name() : __SigmaDraOverlap,
        __Rms.name() : __Rms,
        __PV2_1.name() : __PV2_1,
        __PV1_2.name() : __PV1_2,
        __PV1_0.name() : __PV1_0,
        __XxError.name() : __XxError,
        __PV1_7.name() : __PV1_7,
        __Seeing.name() : __Seeing,
        __PV2_3.name() : __PV2_3,
        __CRPIX1.name() : __CRPIX1,
        __MeanDdec.name() : __MeanDdec,
        __Chip.name() : __Chip,
        __RefcatSlid.name() : __RefcatSlid,
        __PreastromConfig.name() : __PreastromConfig,
        __XyError.name() : __XyError,
        __Reduced.name() : __Reduced,
        __RmsOverlap.name() : __RmsOverlap,
        __Residuals.name() : __Residuals,
        __PV2_5.name() : __PV2_5
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.processTarget._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'astrometricParameters', astrometricParameters)


# Complex type cosmicMap with content type ELEMENT_ONLY
class cosmicMap (pixelMap):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cosmicMap')
    # Base type is pixelMap
    
    # Element {http://euclid.esa.org/schema/pro/ext}Hot uses Python identifier Hot
    __Hot = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Hot'), 'Hot', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextHot', False)

    
    Hot = property(__Hot.value, __Hot.set, None, u' Information about the detector\n                                hot pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Frame uses Python identifier Frame
    __Frame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Frame'), 'Frame', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextFrame', False)

    
    Frame = property(__Frame.value, __Frame.set, None, u' Information about the input\n                                reduced science frame [None] ')

    
    # Element Count ({http://euclid.esa.org/schema/pro/ext}Count) inherited from {http://euclid.esa.org/schema/pro/ext}pixelMap
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Gain uses Python identifier Gain
    __Gain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Gain'), 'Gain', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextGain', False)

    
    Gain = property(__Gain.value, __Gain.set, None, u' Information about the detector\n                                gain [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Cold uses Python identifier Cold
    __Cold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cold'), 'Cold', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextCold', False)

    
    Cold = property(__Cold.value, __Cold.set, None, u' Information about the detector\n                                cold pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Saturated uses Python identifier Saturated
    __Saturated = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Saturated'), 'Saturated', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextSaturated', False)

    
    Saturated = property(__Saturated.value, __Saturated.set, None, u' Information about saturated\n                                pixels [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Flat uses Python identifier Flat
    __Flat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flat'), 'Flat', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextFlat', False)

    
    Flat = property(__Flat.value, __Flat.set, None, u' Information about the detector\n                                sensitivity variations [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CosmicCount uses Python identifier CosmicCount
    __CosmicCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CosmicCount'), 'CosmicCount', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextCosmicCount', False)

    
    CosmicCount = property(__CosmicCount.value, __CosmicCount.set, None, u' Number of cosmic ray events (not\n                                affected pixels) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Illumination uses Python identifier Illumination
    __Illumination = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), 'Illumination', '__httpeuclid_esa_orgschemaproext_cosmicMap_httpeuclid_esa_orgschemaproextIllumination', False)

    
    Illumination = property(__Illumination.value, __Illumination.set, None, u' Information about the\n                                illumination correction [None] ')


    _ElementMap = pixelMap._ElementMap.copy()
    _ElementMap.update({
        __Hot.name() : __Hot,
        __ProcessParams.name() : __ProcessParams,
        __Frame.name() : __Frame,
        __Gain.name() : __Gain,
        __Cold.name() : __Cold,
        __Instrument.name() : __Instrument,
        __Saturated.name() : __Saturated,
        __Chip.name() : __Chip,
        __Flat.name() : __Flat,
        __CosmicCount.name() : __CosmicCount,
        __Filter.name() : __Filter,
        __Illumination.name() : __Illumination
    })
    _AttributeMap = pixelMap._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'cosmicMap', cosmicMap)


# Complex type gainLinearity with content type ELEMENT_ONLY
class gainLinearity (CommonDM.dm.bas.img_stub.processTargetDataObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'gainLinearity')
    # Base type is CommonDM.dm.bas.img_stub.processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}Gain uses Python identifier Gain
    __Gain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Gain'), 'Gain', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextGain', False)

    
    Gain = property(__Gain.value, __Gain.set, None, u' Value of the gain measurement\n                                (ADU conversion factor) [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Bias uses Python identifier Bias
    __Bias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Bias'), 'Bias', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextBias', False)

    
    Bias = property(__Bias.value, __Bias.set, None, u' Information about the detector\n                                bias offset levels [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExposureTimes uses Python identifier ExposureTimes
    __ExposureTimes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureTimes'), 'ExposureTimes', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextExposureTimes', True)

    
    ExposureTimes = property(__ExposureTimes.value, __ExposureTimes.set, None, u' List of exposure times of the\n                                dome flat frames [second] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RawDomeFlatFrames uses Python identifier RawDomeFlatFrames
    __RawDomeFlatFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawDomeFlatFrames'), 'RawDomeFlatFrames', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextRawDomeFlatFrames', True)

    
    RawDomeFlatFrames = property(__RawDomeFlatFrames.value, __RawDomeFlatFrames.set, None, u' List of input raw dome flat\n                                frames [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RmsDiff uses Python identifier RmsDiff
    __RmsDiff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RmsDiff'), 'RmsDiff', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextRmsDiff', True)

    
    RmsDiff = property(__RmsDiff.value, __RmsDiff.set, None, u' List of raw measurements of\n                                sample standard deviation of pixel values of the\n                                subtracted dome flat frames [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExposureLevels uses Python identifier ExposureLevels
    __ExposureLevels = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureLevels'), 'ExposureLevels', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextExposureLevels', True)

    
    ExposureLevels = property(__ExposureLevels.value, __ExposureLevels.set, None, u' List of exposure levels (median\n                                pixel value of each dome flat frame) [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MedianSum uses Python identifier MedianSum
    __MedianSum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MedianSum'), 'MedianSum', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextMedianSum', True)

    
    MedianSum = property(__MedianSum.value, __MedianSum.set, None, u' List of raw measurements of\n                                median pixel values of the added dome flat\n                                frames [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_gainLinearity_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')


    _ElementMap = CommonDM.dm.bas.img_stub.processTargetDataObject._ElementMap.copy()
    _ElementMap.update({
        __Gain.name() : __Gain,
        __Template.name() : __Template,
        __Chip.name() : __Chip,
        __TimestampStart.name() : __TimestampStart,
        __Bias.name() : __Bias,
        __ExposureTimes.name() : __ExposureTimes,
        __TimestampEnd.name() : __TimestampEnd,
        __RawDomeFlatFrames.name() : __RawDomeFlatFrames,
        __RmsDiff.name() : __RmsDiff,
        __ObsBlock.name() : __ObsBlock,
        __ExposureLevels.name() : __ExposureLevels,
        __Instrument.name() : __Instrument,
        __MedianSum.name() : __MedianSum,
        __ProcessParams.name() : __ProcessParams
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.processTargetDataObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'gainLinearity', gainLinearity)


# Complex type fringeFrameParameters with content type ELEMENT_ONLY
class fringeFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fringeFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_fringeFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}OverscanCorrection uses Python identifier OverscanCorrection
    __OverscanCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), 'OverscanCorrection', '__httpeuclid_esa_orgschemaproext_fringeFrameParameters_httpeuclid_esa_orgschemaproextOverscanCorrection', False)

    
    OverscanCorrection = property(__OverscanCorrection.value, __OverscanCorrection.set, None, u' Overscan correction method index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_fringeFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __OverscanCorrection.name() : __OverscanCorrection,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'fringeFrameParameters', fringeFrameParameters)


# Complex type cosmicMapSexParameters with content type ELEMENT_ONLY
class cosmicMapSexParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cosmicMapSexParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_cosmicMapSexParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DetectionThreshold uses Python identifier DetectionThreshold
    __DetectionThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectionThreshold'), 'DetectionThreshold', '__httpeuclid_esa_orgschemaproext_cosmicMapSexParameters_httpeuclid_esa_orgschemaproextDetectionThreshold', False)

    
    DetectionThreshold = property(__DetectionThreshold.value, __DetectionThreshold.set, None, u' Threshold for detecting pixels with\n                        cosmic ray events [None] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __DetectionThreshold.name() : __DetectionThreshold
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cosmicMapSexParameters', cosmicMapSexParameters)


# Complex type sourceListParameters with content type ELEMENT_ONLY
class sourceListParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceListParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}HtmDepth uses Python identifier HtmDepth
    __HtmDepth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HtmDepth'), 'HtmDepth', '__httpeuclid_esa_orgschemaproext_sourceListParameters_httpeuclid_esa_orgschemaproextHtmDepth', False)

    
    HtmDepth = property(__HtmDepth.value, __HtmDepth.set, None, u' Highest level of HTM indexing [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_sourceListParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_sourceListParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __HtmDepth.name() : __HtmDepth,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sourceListParameters', sourceListParameters)


# Complex type sourceListDict with content type ELEMENT_ONLY
class sourceListDict (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceListDict')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}B uses Python identifier B
    __B = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'B'), 'B', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextB', False)

    
    B = property(__B.value, __B.set, None, u' Semi-minor axis of profile [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MAG_AUTO uses Python identifier MAG_AUTO
    __MAG_AUTO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_AUTO'), 'MAG_AUTO', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextMAG_AUTO', False)

    
    MAG_AUTO = property(__MAG_AUTO.value, __MAG_AUTO.set, None, u' Kron-like elliptical aperture magnitude\n                        [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}THETAWCS uses Python identifier THETAWCS
    __THETAWCS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'THETAWCS'), 'THETAWCS', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextTHETAWCS', False)

    
    THETAWCS = property(__THETAWCS.value, __THETAWCS.set, None, u' Ellipse position angle [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}A_WCS uses Python identifier A_WCS
    __A_WCS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'A_WCS'), 'A_WCS', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextA_WCS', False)

    
    A_WCS = property(__A_WCS.value, __A_WCS.set, None, u' Semi-major axis of profile [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FIELD_POS uses Python identifier FIELD_POS
    __FIELD_POS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FIELD_POS'), 'FIELD_POS', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextFIELD_POS', False)

    
    FIELD_POS = property(__FIELD_POS.value, __FIELD_POS.set, None, u' Observation index for multi-observation\n                        source lists [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}XM2 uses Python identifier XM2
    __XM2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XM2'), 'XM2', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextXM2', False)

    
    XM2 = property(__XM2.value, __XM2.set, None, u' Variance along X [pixel**2] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MAGERR_APER uses Python identifier MAGERR_APER
    __MAGERR_APER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_APER'), 'MAGERR_APER', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextMAGERR_APER', False)

    
    MAGERR_APER = property(__MAGERR_APER.value, __MAGERR_APER.set, None, u' RMS error vector for fixed aperture\n                        magnitude [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}B_WCS uses Python identifier B_WCS
    __B_WCS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'B_WCS'), 'B_WCS', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextB_WCS', False)

    
    B_WCS = property(__B_WCS.value, __B_WCS.set, None, u' Semi-minor axis of profile [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLUXERR_AUTO uses Python identifier FLUXERR_AUTO
    __FLUXERR_AUTO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_AUTO'), 'FLUXERR_AUTO', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextFLUXERR_AUTO', False)

    
    FLUXERR_AUTO = property(__FLUXERR_AUTO.value, __FLUXERR_AUTO.set, None, u' RMS error for AUTO flux [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLUX_ISO uses Python identifier FLUX_ISO
    __FLUX_ISO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUX_ISO'), 'FLUX_ISO', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextFLUX_ISO', False)

    
    FLUX_ISO = property(__FLUX_ISO.value, __FLUX_ISO.set, None, u' Isophotal flux [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BackGr uses Python identifier BackGr
    __BackGr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BackGr'), 'BackGr', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextBackGr', False)

    
    BackGr = property(__BackGr.value, __BackGr.set, None, u' Background level around a source [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MAGERR_ISO uses Python identifier MAGERR_ISO
    __MAGERR_ISO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_ISO'), 'MAGERR_ISO', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextMAGERR_ISO', False)

    
    MAGERR_ISO = property(__MAGERR_ISO.value, __MAGERR_ISO.set, None, u' RMS error for isophotal magnitude [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLUX_RADIUS uses Python identifier FLUX_RADIUS
    __FLUX_RADIUS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUX_RADIUS'), 'FLUX_RADIUS', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextFLUX_RADIUS', False)

    
    FLUX_RADIUS = property(__FLUX_RADIUS.value, __FLUX_RADIUS.set, None, u' Fraction-of-light radius [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DEC uses Python identifier DEC
    __DEC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEC'), 'DEC', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextDEC', False)

    
    DEC = property(__DEC.value, __DEC.set, None, u' Declination [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CLASS_STAR uses Python identifier CLASS_STAR
    __CLASS_STAR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CLASS_STAR'), 'CLASS_STAR', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextCLASS_STAR', False)

    
    CLASS_STAR = property(__CLASS_STAR.value, __CLASS_STAR.set, None, u' Star/galaxy classifier index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLUX_APER uses Python identifier FLUX_APER
    __FLUX_APER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUX_APER'), 'FLUX_APER', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextFLUX_APER', False)

    
    FLUX_APER = property(__FLUX_APER.value, __FLUX_APER.set, None, u' Flux vector within fixed circular\n                        aperture(s) [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLUXERR_APER uses Python identifier FLUXERR_APER
    __FLUXERR_APER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_APER'), 'FLUXERR_APER', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextFLUXERR_APER', False)

    
    FLUXERR_APER = property(__FLUXERR_APER.value, __FLUXERR_APER.set, None, u' RMS error vector for aperture flux(es)\n                        [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SeqNr uses Python identifier SeqNr
    __SeqNr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SeqNr'), 'SeqNr', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextSeqNr', False)

    
    SeqNr = property(__SeqNr.value, __SeqNr.set, None, u' Index of extracted source [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Corr uses Python identifier Corr
    __Corr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Corr'), 'Corr', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextCorr', False)

    
    Corr = property(__Corr.value, __Corr.set, None, u' Covariance between X and Y [pixel**2] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}A uses Python identifier A
    __A = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'A'), 'A', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextA', False)

    
    A = property(__A.value, __A.set, None, u' Semi-major axis of profile [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SID uses Python identifier SID
    __SID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SID'), 'SID', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextSID', False)

    
    SID = property(__SID.value, __SID.set, None, u' Identifier of a source in the source list\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}YM2 uses Python identifier YM2
    __YM2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YM2'), 'YM2', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextYM2', False)

    
    YM2 = property(__YM2.value, __YM2.set, None, u' Variance along Y [pixel**2] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MU_MAX uses Python identifier MU_MAX
    __MU_MAX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MU_MAX'), 'MU_MAX', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextMU_MAX', False)

    
    MU_MAX = property(__MU_MAX.value, __MU_MAX.set, None, u' Peak surface brightness above background\n                        [mag / arcsec**2] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MAG_ISO uses Python identifier MAG_ISO
    __MAG_ISO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_ISO'), 'MAG_ISO', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextMAG_ISO', False)

    
    MAG_ISO = property(__MAG_ISO.value, __MAG_ISO.set, None, u' Isophotal magnitude [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLUXERR_ISO uses Python identifier FLUXERR_ISO
    __FLUXERR_ISO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_ISO'), 'FLUXERR_ISO', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextFLUXERR_ISO', False)

    
    FLUXERR_ISO = property(__FLUXERR_ISO.value, __FLUXERR_ISO.set, None, u' RMS error for isophotal flux [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ERRB_IMAGE uses Python identifier ERRB_IMAGE
    __ERRB_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ERRB_IMAGE'), 'ERRB_IMAGE', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextERRB_IMAGE', False)

    
    ERRB_IMAGE = property(__ERRB_IMAGE.value, __ERRB_IMAGE.set, None, u' Error on measurement of semi-minor axis\n                        of profile [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SLID uses Python identifier SLID
    __SLID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SLID'), 'SLID', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextSLID', False)

    
    SLID = property(__SLID.value, __SLID.set, None, u' Identifier of the source list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FWHM_IMAGE uses Python identifier FWHM_IMAGE
    __FWHM_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FWHM_IMAGE'), 'FWHM_IMAGE', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextFWHM_IMAGE', False)

    
    FWHM_IMAGE = property(__FWHM_IMAGE.value, __FWHM_IMAGE.set, None, u' Full width at half maximum assuming a\n                        gaussian core [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MAGERR_AUTO uses Python identifier MAGERR_AUTO
    __MAGERR_AUTO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_AUTO'), 'MAGERR_AUTO', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextMAGERR_AUTO', False)

    
    MAGERR_AUTO = property(__MAGERR_AUTO.value, __MAGERR_AUTO.set, None, u' RMS error for AUTO magnitude [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ERRTHETA_IMAGE uses Python identifier ERRTHETA_IMAGE
    __ERRTHETA_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ERRTHETA_IMAGE'), 'ERRTHETA_IMAGE', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextERRTHETA_IMAGE', False)

    
    ERRTHETA_IMAGE = property(__ERRTHETA_IMAGE.value, __ERRTHETA_IMAGE.set, None, u' Error on measurement of ellipse position\n                        angle [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Ypos uses Python identifier Ypos
    __Ypos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ypos'), 'Ypos', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextYpos', False)

    
    Ypos = property(__Ypos.value, __Ypos.set, None, u' Source position along Y [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RA uses Python identifier RA
    __RA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RA'), 'RA', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextRA', False)

    
    RA = property(__RA.value, __RA.set, None, u' Right Ascension [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}HTM uses Python identifier HTM
    __HTM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HTM'), 'HTM', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextHTM', False)

    
    HTM = property(__HTM.value, __HTM.set, None, u' Index of HTM (Hierarchical Triangular\n                        Mesh) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ERRA_IMAGE uses Python identifier ERRA_IMAGE
    __ERRA_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ERRA_IMAGE'), 'ERRA_IMAGE', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextERRA_IMAGE', False)

    
    ERRA_IMAGE = property(__ERRA_IMAGE.value, __ERRA_IMAGE.set, None, u' Error on measurement of semi-major axis\n                        of profile [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}POSANG uses Python identifier POSANG
    __POSANG = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'POSANG'), 'POSANG', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextPOSANG', False)

    
    POSANG = property(__POSANG.value, __POSANG.set, None, u' Ellipse position angle [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PosErr uses Python identifier PosErr
    __PosErr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PosErr'), 'PosErr', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextPosErr', False)

    
    PosErr = property(__PosErr.value, __PosErr.set, None, u' Positional error of extraction (measured\n                        semi-major axis) [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxVal uses Python identifier MaxVal
    __MaxVal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxVal'), 'MaxVal', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextMaxVal', False)

    
    MaxVal = property(__MaxVal.value, __MaxVal.set, None, u' Peak flux above background [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MAG_APER uses Python identifier MAG_APER
    __MAG_APER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_APER'), 'MAG_APER', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextMAG_APER', False)

    
    MAG_APER = property(__MAG_APER.value, __MAG_APER.set, None, u' Fixed aperture magnitude vector [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Level uses Python identifier Level
    __Level = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Level'), 'Level', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextLevel', False)

    
    Level = property(__Level.value, __Level.set, None, u' Level of detection threshold above\n                        background [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLAG uses Python identifier FLAG
    __FLAG = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG'), 'FLAG', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextFLAG', False)

    
    FLAG = property(__FLAG.value, __FLAG.set, None, u' Source extraction flags [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLUX_AUTO uses Python identifier FLUX_AUTO
    __FLUX_AUTO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLUX_AUTO'), 'FLUX_AUTO', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextFLUX_AUTO', False)

    
    FLUX_AUTO = property(__FLUX_AUTO.value, __FLUX_AUTO.set, None, u' Flux within a Kron-like elliptical\n                        aperture [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Xpos uses Python identifier Xpos
    __Xpos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Xpos'), 'Xpos', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextXpos', False)

    
    Xpos = property(__Xpos.value, __Xpos.set, None, u' Source position along X [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}NPIX uses Python identifier NPIX
    __NPIX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NPIX'), 'NPIX', '__httpeuclid_esa_orgschemaproext_sourceListDict_httpeuclid_esa_orgschemaproextNPIX', False)

    
    NPIX = property(__NPIX.value, __NPIX.set, None, u' Isophotal area above analysis threshold\n                        [pixel**2] ')


    _ElementMap = {
        __B.name() : __B,
        __MAG_AUTO.name() : __MAG_AUTO,
        __THETAWCS.name() : __THETAWCS,
        __A_WCS.name() : __A_WCS,
        __FIELD_POS.name() : __FIELD_POS,
        __XM2.name() : __XM2,
        __MAGERR_APER.name() : __MAGERR_APER,
        __B_WCS.name() : __B_WCS,
        __FLUXERR_AUTO.name() : __FLUXERR_AUTO,
        __FLUX_ISO.name() : __FLUX_ISO,
        __BackGr.name() : __BackGr,
        __MAGERR_ISO.name() : __MAGERR_ISO,
        __FLUX_RADIUS.name() : __FLUX_RADIUS,
        __DEC.name() : __DEC,
        __CLASS_STAR.name() : __CLASS_STAR,
        __FLUX_APER.name() : __FLUX_APER,
        __FLUXERR_APER.name() : __FLUXERR_APER,
        __SeqNr.name() : __SeqNr,
        __Corr.name() : __Corr,
        __A.name() : __A,
        __SID.name() : __SID,
        __YM2.name() : __YM2,
        __MU_MAX.name() : __MU_MAX,
        __MAG_ISO.name() : __MAG_ISO,
        __FLUXERR_ISO.name() : __FLUXERR_ISO,
        __ERRB_IMAGE.name() : __ERRB_IMAGE,
        __SLID.name() : __SLID,
        __FWHM_IMAGE.name() : __FWHM_IMAGE,
        __MAGERR_AUTO.name() : __MAGERR_AUTO,
        __ERRTHETA_IMAGE.name() : __ERRTHETA_IMAGE,
        __Ypos.name() : __Ypos,
        __RA.name() : __RA,
        __HTM.name() : __HTM,
        __ERRA_IMAGE.name() : __ERRA_IMAGE,
        __POSANG.name() : __POSANG,
        __PosErr.name() : __PosErr,
        __MaxVal.name() : __MaxVal,
        __MAG_APER.name() : __MAG_APER,
        __Level.name() : __Level,
        __FLAG.name() : __FLAG,
        __FLUX_AUTO.name() : __FLUX_AUTO,
        __Xpos.name() : __Xpos,
        __NPIX.name() : __NPIX
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sourceListDict', sourceListDict)


# Complex type config with content type ELEMENT_ONLY
class config (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'config')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_config_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'config', config)


# Complex type sextractorConfig with content type ELEMENT_ONLY
class sextractorConfig (config):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sextractorConfig')
    # Base type is config
    
    # Element {http://euclid.esa.org/schema/pro/ext}FILTER_NAME uses Python identifier FILTER_NAME
    __FILTER_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FILTER_NAME'), 'FILTER_NAME', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextFILTER_NAME', False)

    
    FILTER_NAME = property(__FILTER_NAME.value, __FILTER_NAME.set, None, u' Name of file contianing the\n                                filter definition [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CHECKIMAGE_NAME uses Python identifier CHECKIMAGE_NAME
    __CHECKIMAGE_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_NAME'), 'CHECKIMAGE_NAME', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextCHECKIMAGE_NAME', False)

    
    CHECKIMAGE_NAME = property(__CHECKIMAGE_NAME.value, __CHECKIMAGE_NAME.set, None, u' Filename for the check-image\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}VERBOSE_TYPE uses Python identifier VERBOSE_TYPE
    __VERBOSE_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE'), 'VERBOSE_TYPE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextVERBOSE_TYPE', False)

    
    VERBOSE_TYPE = property(__VERBOSE_TYPE.value, __VERBOSE_TYPE.set, None, u' Verbosity level (QUIET, NORMAL,\n                                EXTRA_WARNINGS, FULL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CLEAN_PARAM uses Python identifier CLEAN_PARAM
    __CLEAN_PARAM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CLEAN_PARAM'), 'CLEAN_PARAM', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextCLEAN_PARAM', False)

    
    CLEAN_PARAM = property(__CLEAN_PARAM.value, __CLEAN_PARAM.set, None, u' Efficiency of cleaning [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PHOT_AUTOPARAMS uses Python identifier PHOT_AUTOPARAMS
    __PHOT_AUTOPARAMS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOPARAMS'), 'PHOT_AUTOPARAMS', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextPHOT_AUTOPARAMS', True)

    
    PHOT_AUTOPARAMS = property(__PHOT_AUTOPARAMS.value, __PHOT_AUTOPARAMS.set, None, u' List of MAG_AUTO controls\n                                (scaling parameter k of the first order moment\n                                and minimum R_min in units of A and B) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ANALYSIS_THRESH uses Python identifier ANALYSIS_THRESH
    __ANALYSIS_THRESH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ANALYSIS_THRESH'), 'ANALYSIS_THRESH', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextANALYSIS_THRESH', False)

    
    ANALYSIS_THRESH = property(__ANALYSIS_THRESH.value, __ANALYSIS_THRESH.set, None, u' Threshold at which CLASS_STAR and\n                                FWHM_ operate [mag / arcsec^2] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLAG_TYPE uses Python identifier FLAG_TYPE
    __FLAG_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG_TYPE'), 'FLAG_TYPE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextFLAG_TYPE', False)

    
    FLAG_TYPE = property(__FLAG_TYPE.value, __FLAG_TYPE.set, None, u' Combination method for flags on\n                                the same object (OR, AND, MIN, MAX, MOST) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SEEING_FWHM uses Python identifier SEEING_FWHM
    __SEEING_FWHM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SEEING_FWHM'), 'SEEING_FWHM', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextSEEING_FWHM', False)

    
    SEEING_FWHM = property(__SEEING_FWHM.value, __SEEING_FWHM.set, None, u' FWHM of stellar sources (for\n                                star/galaxy separation only) [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CLEAN uses Python identifier CLEAN
    __CLEAN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CLEAN'), 'CLEAN', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextCLEAN', False)

    
    CLEAN = property(__CLEAN.value, __CLEAN.set, None, u' Clean the catalog before writing\n                                to disk (Y, N) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CHECKIMAGE_TYPE uses Python identifier CHECKIMAGE_TYPE
    __CHECKIMAGE_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_TYPE'), 'CHECKIMAGE_TYPE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextCHECKIMAGE_TYPE', False)

    
    CHECKIMAGE_TYPE = property(__CHECKIMAGE_TYPE.value, __CHECKIMAGE_TYPE.set, None, u' Type of information to put in the\n                                check-image (NONE, IDENTICAL, BACKGROUND,\n                                BACKGROUND_RMS, MINIBACKGROUND, MINIBACK_RMS,\n                                -BACKGROUND, FILTERED, OBJECTS, -OBJECTS,\n                                APERTURES, SEGMENTATION) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BACK_FILTERSIZE uses Python identifier BACK_FILTERSIZE
    __BACK_FILTERSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE'), 'BACK_FILTERSIZE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextBACK_FILTERSIZE', False)

    
    BACK_FILTERSIZE = property(__BACK_FILTERSIZE.value, __BACK_FILTERSIZE.set, None, u' Size of background filtering mask\n                                [background mesh] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BACKPHOTO_THICK uses Python identifier BACKPHOTO_THICK
    __BACKPHOTO_THICK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_THICK'), 'BACKPHOTO_THICK', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextBACKPHOTO_THICK', False)

    
    BACKPHOTO_THICK = property(__BACKPHOTO_THICK.value, __BACKPHOTO_THICK.set, None, u' Thickness of the background LOCAL\n                                annulus [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PIXEL_SCALE uses Python identifier PIXEL_SCALE
    __PIXEL_SCALE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE'), 'PIXEL_SCALE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextPIXEL_SCALE', False)

    
    PIXEL_SCALE = property(__PIXEL_SCALE.value, __PIXEL_SCALE.set, None, u' Pixel size [arcsec / pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}THRESH_TYPE uses Python identifier THRESH_TYPE
    __THRESH_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'THRESH_TYPE'), 'THRESH_TYPE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextTHRESH_TYPE', False)

    
    THRESH_TYPE = property(__THRESH_TYPE.value, __THRESH_TYPE.set, None, u' Meaning of DETECT_THRESH and\n                                ANALYSIS_THRESH parameters (RELATIVE, ABSOLUTE)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MAG_GAMMA uses Python identifier MAG_GAMMA
    __MAG_GAMMA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_GAMMA'), 'MAG_GAMMA', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextMAG_GAMMA', False)

    
    MAG_GAMMA = property(__MAG_GAMMA.value, __MAG_GAMMA.set, None, u' Gamma of the emulsion (when\n                                DETECT_TYPE is PHOTO) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BACK_SIZE uses Python identifier BACK_SIZE
    __BACK_SIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE'), 'BACK_SIZE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextBACK_SIZE', False)

    
    BACK_SIZE = property(__BACK_SIZE.value, __BACK_SIZE.set, None, u' Size of a background mesh [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SATUR_LEVEL uses Python identifier SATUR_LEVEL
    __SATUR_LEVEL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SATUR_LEVEL'), 'SATUR_LEVEL', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextSATUR_LEVEL', False)

    
    SATUR_LEVEL = property(__SATUR_LEVEL.value, __SATUR_LEVEL.set, None, u' Pixel value above which it is\n                                considered saturated [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BACKPHOTO_TYPE uses Python identifier BACKPHOTO_TYPE
    __BACKPHOTO_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_TYPE'), 'BACKPHOTO_TYPE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextBACKPHOTO_TYPE', False)

    
    BACKPHOTO_TYPE = property(__BACKPHOTO_TYPE.value, __BACKPHOTO_TYPE.set, None, u' Background used to compute\n                                magnitudes (GLOBAL, LOCAL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}WEIGHT_TYPE uses Python identifier WEIGHT_TYPE
    __WEIGHT_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE'), 'WEIGHT_TYPE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextWEIGHT_TYPE', False)

    
    WEIGHT_TYPE = property(__WEIGHT_TYPE.value, __WEIGHT_TYPE.set, None, u' Weighting scheme for weight-image\n                                (NONE, BACKGROUND, MAP_RMS, MAP_VAR, MAP_WEIGHT)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DEBLEND_NTHRESH uses Python identifier DEBLEND_NTHRESH
    __DEBLEND_NTHRESH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_NTHRESH'), 'DEBLEND_NTHRESH', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextDEBLEND_NTHRESH', False)

    
    DEBLEND_NTHRESH = property(__DEBLEND_NTHRESH.value, __DEBLEND_NTHRESH.set, None, u' Number of deblending\n                                sub-thresholds [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PHOT_AUTOAPERS uses Python identifier PHOT_AUTOAPERS
    __PHOT_AUTOAPERS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOAPERS'), 'PHOT_AUTOAPERS', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextPHOT_AUTOAPERS', True)

    
    PHOT_AUTOAPERS = property(__PHOT_AUTOAPERS.value, __PHOT_AUTOAPERS.set, None, u' List of MAG_AUTO minimum circular\n                                aperture diameters (estimation disk, measurement\n                                disk) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MASK_TYPE uses Python identifier MASK_TYPE
    __MASK_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MASK_TYPE'), 'MASK_TYPE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextMASK_TYPE', False)

    
    MASK_TYPE = property(__MASK_TYPE.value, __MASK_TYPE.set, None, u' Method of masking of neighbors\n                                for photometry (NONE, BLANK, CORRECT) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLAG_IMAGE uses Python identifier FLAG_IMAGE
    __FLAG_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG_IMAGE'), 'FLAG_IMAGE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextFLAG_IMAGE', False)

    
    FLAG_IMAGE = property(__FLAG_IMAGE.value, __FLAG_IMAGE.set, None, u' Filename of the flag-image [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DETECT_MINAREA uses Python identifier DETECT_MINAREA
    __DETECT_MINAREA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DETECT_MINAREA'), 'DETECT_MINAREA', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextDETECT_MINAREA', False)

    
    DETECT_MINAREA = property(__DETECT_MINAREA.value, __DETECT_MINAREA.set, None, u' Minimum number of pixels above\n                                threshold triggering detection [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MEMORY_BUFSIZE uses Python identifier MEMORY_BUFSIZE
    __MEMORY_BUFSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_BUFSIZE'), 'MEMORY_BUFSIZE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextMEMORY_BUFSIZE', False)

    
    MEMORY_BUFSIZE = property(__MEMORY_BUFSIZE.value, __MEMORY_BUFSIZE.set, None, u' Number of scan-lines in the image\n                                buffer [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DEBLEND_MINCONT uses Python identifier DEBLEND_MINCONT
    __DEBLEND_MINCONT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_MINCONT'), 'DEBLEND_MINCONT', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextDEBLEND_MINCONT', False)

    
    DEBLEND_MINCONT = property(__DEBLEND_MINCONT.value, __DEBLEND_MINCONT.set, None, u' Minimum contrast parameter for\n                                deblending [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DETECT_THRESH uses Python identifier DETECT_THRESH
    __DETECT_THRESH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DETECT_THRESH'), 'DETECT_THRESH', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextDETECT_THRESH', False)

    
    DETECT_THRESH = property(__DETECT_THRESH.value, __DETECT_THRESH.set, None, u' Detection threshold relative to\n                                background RMS (when THRESH_TYPE is RELATIVE)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}GAIN uses Python identifier GAIN
    __GAIN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GAIN'), 'GAIN', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextGAIN', False)

    
    GAIN = property(__GAIN.value, __GAIN.set, None, u' Conversion factor used for error\n                                estimates of CCD magnitudes [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MEMORY_OBJSTACK uses Python identifier MEMORY_OBJSTACK
    __MEMORY_OBJSTACK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_OBJSTACK'), 'MEMORY_OBJSTACK', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextMEMORY_OBJSTACK', False)

    
    MEMORY_OBJSTACK = property(__MEMORY_OBJSTACK.value, __MEMORY_OBJSTACK.set, None, u' Maximum number of objects that\n                                the object-stack can contain [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BACK_VALUE uses Python identifier BACK_VALUE
    __BACK_VALUE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_VALUE'), 'BACK_VALUE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextBACK_VALUE', True)

    
    BACK_VALUE = property(__BACK_VALUE.value, __BACK_VALUE.set, None, u' List of constant values to be\n                                subtracted from the images if BACK_TYPE is\n                                MANUAL [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}STARNNW_NAME uses Python identifier STARNNW_NAME
    __STARNNW_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'STARNNW_NAME'), 'STARNNW_NAME', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextSTARNNW_NAME', False)

    
    STARNNW_NAME = property(__STARNNW_NAME.value, __STARNNW_NAME.set, None, u' Name of the file containing the\n                                neural-network weights for star/galaxy\n                                separation [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DETECT_TYPE uses Python identifier DETECT_TYPE
    __DETECT_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DETECT_TYPE'), 'DETECT_TYPE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextDETECT_TYPE', False)

    
    DETECT_TYPE = property(__DETECT_TYPE.value, __DETECT_TYPE.set, None, u' Type of device that produced the\n                                image (CCD, PHOTO) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PHOT_APERTURES uses Python identifier PHOT_APERTURES
    __PHOT_APERTURES = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PHOT_APERTURES'), 'PHOT_APERTURES', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextPHOT_APERTURES', False)

    
    PHOT_APERTURES = property(__PHOT_APERTURES.value, __PHOT_APERTURES.set, None, u' MAG_APER aperture diameter\n                                [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CATALOG_NAME uses Python identifier CATALOG_NAME
    __CATALOG_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_NAME'), 'CATALOG_NAME', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextCATALOG_NAME', False)

    
    CATALOG_NAME = property(__CATALOG_NAME.value, __CATALOG_NAME.set, None, u' Name of the output catalog [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MAG_ZEROPOINT uses Python identifier MAG_ZEROPOINT
    __MAG_ZEROPOINT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_ZEROPOINT'), 'MAG_ZEROPOINT', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextMAG_ZEROPOINT', False)

    
    MAG_ZEROPOINT = property(__MAG_ZEROPOINT.value, __MAG_ZEROPOINT.set, None, u' Zero-point offset to be applied\n                                to magnitudes [mag] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/pro/ext}ExtObjectId) inherited from {http://euclid.esa.org/schema/pro/ext}config
    
    # Element {http://euclid.esa.org/schema/pro/ext}FILTER uses Python identifier FILTER
    __FILTER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FILTER'), 'FILTER', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextFILTER', False)

    
    FILTER = property(__FILTER.value, __FILTER.set, None, u' Apply filtering to the data\n                                before extraction (Y, N) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}WEIGHT_IMAGE uses Python identifier WEIGHT_IMAGE
    __WEIGHT_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE'), 'WEIGHT_IMAGE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextWEIGHT_IMAGE', False)

    
    WEIGHT_IMAGE = property(__WEIGHT_IMAGE.value, __WEIGHT_IMAGE.set, None, u' Filename of the detection and\n                                measurement weight-image [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CATALOG_TYPE uses Python identifier CATALOG_TYPE
    __CATALOG_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_TYPE'), 'CATALOG_TYPE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextCATALOG_TYPE', False)

    
    CATALOG_TYPE = property(__CATALOG_TYPE.value, __CATALOG_TYPE.set, None, u' Format of the output catalog\n                                (ASCII, ASCII_HEAD, ASCII_SKYCAT, ASCII_VOTABLE,\n                                FITS_1.0, FITS_LDAC) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MEMORY_PIXSTACK uses Python identifier MEMORY_PIXSTACK
    __MEMORY_PIXSTACK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_PIXSTACK'), 'MEMORY_PIXSTACK', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextMEMORY_PIXSTACK', False)

    
    MEMORY_PIXSTACK = property(__MEMORY_PIXSTACK.value, __MEMORY_PIXSTACK.set, None, u' Maximum number of pixels that the\n                                pixel-stack can contain [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PARAMETERS_NAME uses Python identifier PARAMETERS_NAME
    __PARAMETERS_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PARAMETERS_NAME'), 'PARAMETERS_NAME', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextPARAMETERS_NAME', False)

    
    PARAMETERS_NAME = property(__PARAMETERS_NAME.value, __PARAMETERS_NAME.set, None, u' Name of the file containing the\n                                list of parameters that will be computed and put\n                                into the catalog for each object [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BACK_TYPE uses Python identifier BACK_TYPE
    __BACK_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE'), 'BACK_TYPE', '__httpeuclid_esa_orgschemaproext_sextractorConfig_httpeuclid_esa_orgschemaproextBACK_TYPE', False)

    
    BACK_TYPE = property(__BACK_TYPE.value, __BACK_TYPE.set, None, u' Type of background subtracted\n                                from the images (AUTO, MANUAL) [None] ')


    _ElementMap = config._ElementMap.copy()
    _ElementMap.update({
        __FILTER_NAME.name() : __FILTER_NAME,
        __CHECKIMAGE_NAME.name() : __CHECKIMAGE_NAME,
        __VERBOSE_TYPE.name() : __VERBOSE_TYPE,
        __CLEAN_PARAM.name() : __CLEAN_PARAM,
        __PHOT_AUTOPARAMS.name() : __PHOT_AUTOPARAMS,
        __ANALYSIS_THRESH.name() : __ANALYSIS_THRESH,
        __FLAG_TYPE.name() : __FLAG_TYPE,
        __SEEING_FWHM.name() : __SEEING_FWHM,
        __CLEAN.name() : __CLEAN,
        __CHECKIMAGE_TYPE.name() : __CHECKIMAGE_TYPE,
        __BACK_FILTERSIZE.name() : __BACK_FILTERSIZE,
        __BACKPHOTO_THICK.name() : __BACKPHOTO_THICK,
        __PIXEL_SCALE.name() : __PIXEL_SCALE,
        __THRESH_TYPE.name() : __THRESH_TYPE,
        __MAG_GAMMA.name() : __MAG_GAMMA,
        __BACK_SIZE.name() : __BACK_SIZE,
        __SATUR_LEVEL.name() : __SATUR_LEVEL,
        __BACKPHOTO_TYPE.name() : __BACKPHOTO_TYPE,
        __WEIGHT_TYPE.name() : __WEIGHT_TYPE,
        __DEBLEND_NTHRESH.name() : __DEBLEND_NTHRESH,
        __PHOT_AUTOAPERS.name() : __PHOT_AUTOAPERS,
        __MASK_TYPE.name() : __MASK_TYPE,
        __FLAG_IMAGE.name() : __FLAG_IMAGE,
        __DETECT_MINAREA.name() : __DETECT_MINAREA,
        __MEMORY_BUFSIZE.name() : __MEMORY_BUFSIZE,
        __DEBLEND_MINCONT.name() : __DEBLEND_MINCONT,
        __DETECT_THRESH.name() : __DETECT_THRESH,
        __GAIN.name() : __GAIN,
        __MEMORY_OBJSTACK.name() : __MEMORY_OBJSTACK,
        __BACK_VALUE.name() : __BACK_VALUE,
        __STARNNW_NAME.name() : __STARNNW_NAME,
        __DETECT_TYPE.name() : __DETECT_TYPE,
        __PHOT_APERTURES.name() : __PHOT_APERTURES,
        __CATALOG_NAME.name() : __CATALOG_NAME,
        __MAG_ZEROPOINT.name() : __MAG_ZEROPOINT,
        __FILTER.name() : __FILTER,
        __WEIGHT_IMAGE.name() : __WEIGHT_IMAGE,
        __CATALOG_TYPE.name() : __CATALOG_TYPE,
        __MEMORY_PIXSTACK.name() : __MEMORY_PIXSTACK,
        __PARAMETERS_NAME.name() : __PARAMETERS_NAME,
        __BACK_TYPE.name() : __BACK_TYPE
    })
    _AttributeMap = config._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sextractorConfig', sextractorConfig)


# Complex type gridTarget with content type ELEMENT_ONLY
class gridTarget (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'gridTarget')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_gridTarget_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PixelScale uses Python identifier PixelScale
    __PixelScale = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PixelScale'), 'PixelScale', '__httpeuclid_esa_orgschemaproext_gridTarget_httpeuclid_esa_orgschemaproextPixelScale', False)

    
    PixelScale = property(__PixelScale.value, __PixelScale.set, None, u' Pixel scale of the grid [arcsec / pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Dec uses Python identifier Dec
    __Dec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Dec'), 'Dec', '__httpeuclid_esa_orgschemaproext_gridTarget_httpeuclid_esa_orgschemaproextDec', False)

    
    Dec = property(__Dec.value, __Dec.set, None, u' Declination of target reference pixel\n                        [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Ra uses Python identifier Ra
    __Ra = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ra'), 'Ra', '__httpeuclid_esa_orgschemaproext_gridTarget_httpeuclid_esa_orgschemaproextRa', False)

    
    Ra = property(__Ra.value, __Ra.set, None, u' Right Ascension of target reference pixel\n                        [deg] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __PixelScale.name() : __PixelScale,
        __Dec.name() : __Dec,
        __Ra.name() : __Ra
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'gridTarget', gridTarget)


# Complex type swarpConfig with content type ELEMENT_ONLY
class swarpConfig (config):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'swarpConfig')
    # Base type is config
    
    # Element {http://euclid.esa.org/schema/pro/ext}SUBTRACT_BACK uses Python identifier SUBTRACT_BACK
    __SUBTRACT_BACK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SUBTRACT_BACK'), 'SUBTRACT_BACK', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextSUBTRACT_BACK', False)

    
    SUBTRACT_BACK = property(__SUBTRACT_BACK.value, __SUBTRACT_BACK.set, None, u' Background-subtract images prior\n                                to resampling [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}OVERSAMPLING uses Python identifier OVERSAMPLING
    __OVERSAMPLING = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OVERSAMPLING'), 'OVERSAMPLING', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextOVERSAMPLING', False)

    
    OVERSAMPLING = property(__OVERSAMPLING.value, __OVERSAMPLING.set, None, u' Amount of oversampling in each\n                                dimension [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}WEIGHT_TYPE uses Python identifier WEIGHT_TYPE
    __WEIGHT_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE'), 'WEIGHT_TYPE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextWEIGHT_TYPE', False)

    
    WEIGHT_TYPE = property(__WEIGHT_TYPE.value, __WEIGHT_TYPE.set, None, u' Type of input weight map (NONE,\n                                MAP_WEIGHT, MAP_VARIANCE, MAP_RMS) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CELESTIAL_TYPE uses Python identifier CELESTIAL_TYPE
    __CELESTIAL_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CELESTIAL_TYPE'), 'CELESTIAL_TYPE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextCELESTIAL_TYPE', False)

    
    CELESTIAL_TYPE = property(__CELESTIAL_TYPE.value, __CELESTIAL_TYPE.set, None, u' Celestial coordinate system in\n                                output (NATIVE, PIXEL, EQUATORIAL, GALACTIC,\n                                ECLIPTIC) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PROJECTION_TYPE uses Python identifier PROJECTION_TYPE
    __PROJECTION_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PROJECTION_TYPE'), 'PROJECTION_TYPE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextPROJECTION_TYPE', False)

    
    PROJECTION_TYPE = property(__PROJECTION_TYPE.value, __PROJECTION_TYPE.set, None, u' Projection system used in output\n                                in standard WCS notation (AZP, TAN, STG, SIN,\n                                ARC, ZPN, ZEA, AIR, CYP, CEA, CAR, MER, COP,\n                                COE, COD, COO, BON, PCO, GLS, PAR, MOL, AIT,\n                                TCS, CSC, QSC) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RESAMPLE_SUFFIX uses Python identifier RESAMPLE_SUFFIX
    __RESAMPLE_SUFFIX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLE_SUFFIX'), 'RESAMPLE_SUFFIX', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextRESAMPLE_SUFFIX', False)

    
    RESAMPLE_SUFFIX = property(__RESAMPLE_SUFFIX.value, __RESAMPLE_SUFFIX.set, None, u' Extension of the resampled images\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}IMAGEOUT_NAME uses Python identifier IMAGEOUT_NAME
    __IMAGEOUT_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IMAGEOUT_NAME'), 'IMAGEOUT_NAME', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextIMAGEOUT_NAME', False)

    
    IMAGEOUT_NAME = property(__IMAGEOUT_NAME.value, __IMAGEOUT_NAME.set, None, u' Filename of output image [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CENTER_TYPE uses Python identifier CENTER_TYPE
    __CENTER_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CENTER_TYPE'), 'CENTER_TYPE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextCENTER_TYPE', False)

    
    CENTER_TYPE = property(__CENTER_TYPE.value, __CENTER_TYPE.set, None, u' The way the output frame is\n                                centered (ALL, MOST, MANUAL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}VMEM_DIR uses Python identifier VMEM_DIR
    __VMEM_DIR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VMEM_DIR'), 'VMEM_DIR', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextVMEM_DIR', False)

    
    VMEM_DIR = property(__VMEM_DIR.value, __VMEM_DIR.set, None, u' Path of the directory where\n                                virtual-memory and other temporary files are\n                                written [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FSCALASTRO_TYPE uses Python identifier FSCALASTRO_TYPE
    __FSCALASTRO_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FSCALASTRO_TYPE'), 'FSCALASTRO_TYPE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextFSCALASTRO_TYPE', False)

    
    FSCALASTRO_TYPE = property(__FSCALASTRO_TYPE.value, __FSCALASTRO_TYPE.set, None, u' How to compute the astrometric\n                                part of the flux scaling (NONE, FIXED) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CENTER uses Python identifier CENTER
    __CENTER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CENTER'), 'CENTER', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextCENTER', True)

    
    CENTER = property(__CENTER.value, __CENTER.set, None, u' List of positions of center in\n                                CENTER_TYPE MANUAL mode [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PIXELSCALE_TYPE uses Python identifier PIXELSCALE_TYPE
    __PIXELSCALE_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PIXELSCALE_TYPE'), 'PIXELSCALE_TYPE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextPIXELSCALE_TYPE', False)

    
    PIXELSCALE_TYPE = property(__PIXELSCALE_TYPE.value, __PIXELSCALE_TYPE.set, None, u' How the output pixel size is set\n                                (MEDIAN, MIN, MAX, MANUAL, FIT) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}HEADER_ONLY uses Python identifier HEADER_ONLY
    __HEADER_ONLY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HEADER_ONLY'), 'HEADER_ONLY', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextHEADER_ONLY', False)

    
    HEADER_ONLY = property(__HEADER_ONLY.value, __HEADER_ONLY.set, None, u' Only create the header in the\n                                combined image (Y, N) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}WEIGHTOUT_NAME uses Python identifier WEIGHTOUT_NAME
    __WEIGHTOUT_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WEIGHTOUT_NAME'), 'WEIGHTOUT_NAME', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextWEIGHTOUT_NAME', False)

    
    WEIGHTOUT_NAME = property(__WEIGHTOUT_NAME.value, __WEIGHTOUT_NAME.set, None, u' Filename of the output weight-map\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MEM_MAX uses Python identifier MEM_MAX
    __MEM_MAX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MEM_MAX'), 'MEM_MAX', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextMEM_MAX', False)

    
    MEM_MAX = property(__MEM_MAX.value, __MEM_MAX.set, None, u' Maximum amount of megabytes\n                                allowed for RAM storage [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FSCALE_DEFAULT uses Python identifier FSCALE_DEFAULT
    __FSCALE_DEFAULT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FSCALE_DEFAULT'), 'FSCALE_DEFAULT', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextFSCALE_DEFAULT', True)

    
    FSCALE_DEFAULT = property(__FSCALE_DEFAULT.value, __FSCALE_DEFAULT.set, None, u' List of default flux scales to\n                                adopt if FSCALE_KEYWORD nonexistent [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}IMAGE_SIZE uses Python identifier IMAGE_SIZE
    __IMAGE_SIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IMAGE_SIZE'), 'IMAGE_SIZE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextIMAGE_SIZE', False)

    
    IMAGE_SIZE = property(__IMAGE_SIZE.value, __IMAGE_SIZE.set, None, u' Dimensions of the output image\n                                [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RESAMPLE_DIR uses Python identifier RESAMPLE_DIR
    __RESAMPLE_DIR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLE_DIR'), 'RESAMPLE_DIR', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextRESAMPLE_DIR', False)

    
    RESAMPLE_DIR = property(__RESAMPLE_DIR.value, __RESAMPLE_DIR.set, None, u' Path of the directory where the\n                                resampled images are written [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PIXEL_SCALE uses Python identifier PIXEL_SCALE
    __PIXEL_SCALE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE'), 'PIXEL_SCALE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextPIXEL_SCALE', False)

    
    PIXEL_SCALE = property(__PIXEL_SCALE.value, __PIXEL_SCALE.set, None, u' Step between pixels in each\n                                dimension [arcsec / pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}HEADER_SUFFIX uses Python identifier HEADER_SUFFIX
    __HEADER_SUFFIX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HEADER_SUFFIX'), 'HEADER_SUFFIX', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextHEADER_SUFFIX', False)

    
    HEADER_SUFFIX = property(__HEADER_SUFFIX.value, __HEADER_SUFFIX.set, None, u' Extension of the replacement\n                                header files [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}GAIN_KEYWORD uses Python identifier GAIN_KEYWORD
    __GAIN_KEYWORD = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GAIN_KEYWORD'), 'GAIN_KEYWORD', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextGAIN_KEYWORD', False)

    
    GAIN_KEYWORD = property(__GAIN_KEYWORD.value, __GAIN_KEYWORD.set, None, u' FITS keyword containing the gain\n                                in input images [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/pro/ext}ExtObjectId) inherited from {http://euclid.esa.org/schema/pro/ext}config
    
    # Element {http://euclid.esa.org/schema/pro/ext}DELETE_TMPFILES uses Python identifier DELETE_TMPFILES
    __DELETE_TMPFILES = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DELETE_TMPFILES'), 'DELETE_TMPFILES', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextDELETE_TMPFILES', False)

    
    DELETE_TMPFILES = property(__DELETE_TMPFILES.value, __DELETE_TMPFILES.set, None, u' Delete temporary image files\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}GAIN_DEFAULT uses Python identifier GAIN_DEFAULT
    __GAIN_DEFAULT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GAIN_DEFAULT'), 'GAIN_DEFAULT', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextGAIN_DEFAULT', False)

    
    GAIN_DEFAULT = property(__GAIN_DEFAULT.value, __GAIN_DEFAULT.set, None, u' Default gain to adopt if\n                                GAIN_KEYWORD nonexistent [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BACK_FILTERSIZE uses Python identifier BACK_FILTERSIZE
    __BACK_FILTERSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE'), 'BACK_FILTERSIZE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextBACK_FILTERSIZE', False)

    
    BACK_FILTERSIZE = property(__BACK_FILTERSIZE.value, __BACK_FILTERSIZE.set, None, u' Size of background filtering mask\n                                in factors of BACK_SIZE [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BACK_DEFAULT uses Python identifier BACK_DEFAULT
    __BACK_DEFAULT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_DEFAULT'), 'BACK_DEFAULT', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextBACK_DEFAULT', False)

    
    BACK_DEFAULT = property(__BACK_DEFAULT.value, __BACK_DEFAULT.set, None, u' Default background to be\n                                subtracted in BACK_TYPE MANUAL mode [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RESAMPLE uses Python identifier RESAMPLE
    __RESAMPLE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLE'), 'RESAMPLE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextRESAMPLE', False)

    
    RESAMPLE = property(__RESAMPLE.value, __RESAMPLE.set, None, u' Resample the input images (Y, N)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}NTHREADS uses Python identifier NTHREADS
    __NTHREADS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NTHREADS'), 'NTHREADS', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextNTHREADS', False)

    
    NTHREADS = property(__NTHREADS.value, __NTHREADS.set, None, u' Number of threads to run\n                                simultaneously during resampling (0 is\n                                automatic) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}WEIGHT_IMAGE uses Python identifier WEIGHT_IMAGE
    __WEIGHT_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE'), 'WEIGHT_IMAGE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextWEIGHT_IMAGE', False)

    
    WEIGHT_IMAGE = property(__WEIGHT_IMAGE.value, __WEIGHT_IMAGE.set, None, u' List of filenames of input weight\n                                maps [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}VMEM_MAX uses Python identifier VMEM_MAX
    __VMEM_MAX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VMEM_MAX'), 'VMEM_MAX', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextVMEM_MAX', False)

    
    VMEM_MAX = property(__VMEM_MAX.value, __VMEM_MAX.set, None, u' Maximum amount of megabytes\n                                allowed for virtual-memory storage [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}WRITE_FILEINFO uses Python identifier WRITE_FILEINFO
    __WRITE_FILEINFO = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WRITE_FILEINFO'), 'WRITE_FILEINFO', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextWRITE_FILEINFO', False)

    
    WRITE_FILEINFO = property(__WRITE_FILEINFO.value, __WRITE_FILEINFO.set, None, u' Write extended information from\n                                input images to output images [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}COMBINE uses Python identifier COMBINE
    __COMBINE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'COMBINE'), 'COMBINE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextCOMBINE', False)

    
    COMBINE = property(__COMBINE.value, __COMBINE.set, None, u' Combine resampled images (Y, N)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}INTERPOLATE uses Python identifier INTERPOLATE
    __INTERPOLATE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'INTERPOLATE'), 'INTERPOLATE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextINTERPOLATE', False)

    
    INTERPOLATE = property(__INTERPOLATE.value, __INTERPOLATE.set, None, u' Interpolate upon resampling (Y,\n                                N) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}WEIGHT_SUFFIX uses Python identifier WEIGHT_SUFFIX
    __WEIGHT_SUFFIX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_SUFFIX'), 'WEIGHT_SUFFIX', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextWEIGHT_SUFFIX', False)

    
    WEIGHT_SUFFIX = property(__WEIGHT_SUFFIX.value, __WEIGHT_SUFFIX.set, None, u' Extension of the input weight\n                                maps [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BACK_TYPE uses Python identifier BACK_TYPE
    __BACK_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE'), 'BACK_TYPE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextBACK_TYPE', False)

    
    BACK_TYPE = property(__BACK_TYPE.value, __BACK_TYPE.set, None, u' Type of background to subtract\n                                (AUTO, MANUAL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}VERBOSE_TYPE uses Python identifier VERBOSE_TYPE
    __VERBOSE_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE'), 'VERBOSE_TYPE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextVERBOSE_TYPE', False)

    
    VERBOSE_TYPE = property(__VERBOSE_TYPE.value, __VERBOSE_TYPE.set, None, u' Verbosity level (QUIET, NORMAL,\n                                FULL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}COMBINE_BUFSIZE uses Python identifier COMBINE_BUFSIZE
    __COMBINE_BUFSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'COMBINE_BUFSIZE'), 'COMBINE_BUFSIZE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextCOMBINE_BUFSIZE', False)

    
    COMBINE_BUFSIZE = property(__COMBINE_BUFSIZE.value, __COMBINE_BUFSIZE.set, None, u' Amount of megabytes of buffer\n                                memory used for coaddition [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}COMBINE_TYPE uses Python identifier COMBINE_TYPE
    __COMBINE_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'COMBINE_TYPE'), 'COMBINE_TYPE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextCOMBINE_TYPE', False)

    
    COMBINE_TYPE = property(__COMBINE_TYPE.value, __COMBINE_TYPE.set, None, u' Image combination method (MEDIAN,\n                                AVERAGE, MIN, MAX, WEIGHTED, CHI2, SUM) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FSCALE_KEYWORD uses Python identifier FSCALE_KEYWORD
    __FSCALE_KEYWORD = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FSCALE_KEYWORD'), 'FSCALE_KEYWORD', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextFSCALE_KEYWORD', False)

    
    FSCALE_KEYWORD = property(__FSCALE_KEYWORD.value, __FSCALE_KEYWORD.set, None, u' FITS keyword containing flux\n                                scale in input images [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RESAMPLING_TYPE uses Python identifier RESAMPLING_TYPE
    __RESAMPLING_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLING_TYPE'), 'RESAMPLING_TYPE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextRESAMPLING_TYPE', False)

    
    RESAMPLING_TYPE = property(__RESAMPLING_TYPE.value, __RESAMPLING_TYPE.set, None, u' Resampling method (NEAREST,\n                                BILINEAR, LANCZOS2, LANCZOS3, LANCZOS4) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BACK_SIZE uses Python identifier BACK_SIZE
    __BACK_SIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE'), 'BACK_SIZE', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextBACK_SIZE', False)

    
    BACK_SIZE = property(__BACK_SIZE.value, __BACK_SIZE.set, None, u' Size of a background mesh [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}COPY_KEYWORDS uses Python identifier COPY_KEYWORDS
    __COPY_KEYWORDS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'COPY_KEYWORDS'), 'COPY_KEYWORDS', '__httpeuclid_esa_orgschemaproext_swarpConfig_httpeuclid_esa_orgschemaproextCOPY_KEYWORDS', False)

    
    COPY_KEYWORDS = property(__COPY_KEYWORDS.value, __COPY_KEYWORDS.set, None, u' String containing comma-separated\n                                FITS keywords to copy to output images [None] ')


    _ElementMap = config._ElementMap.copy()
    _ElementMap.update({
        __SUBTRACT_BACK.name() : __SUBTRACT_BACK,
        __OVERSAMPLING.name() : __OVERSAMPLING,
        __WEIGHT_TYPE.name() : __WEIGHT_TYPE,
        __CELESTIAL_TYPE.name() : __CELESTIAL_TYPE,
        __PROJECTION_TYPE.name() : __PROJECTION_TYPE,
        __RESAMPLE_SUFFIX.name() : __RESAMPLE_SUFFIX,
        __IMAGEOUT_NAME.name() : __IMAGEOUT_NAME,
        __CENTER_TYPE.name() : __CENTER_TYPE,
        __VMEM_DIR.name() : __VMEM_DIR,
        __FSCALASTRO_TYPE.name() : __FSCALASTRO_TYPE,
        __CENTER.name() : __CENTER,
        __PIXELSCALE_TYPE.name() : __PIXELSCALE_TYPE,
        __HEADER_ONLY.name() : __HEADER_ONLY,
        __WEIGHTOUT_NAME.name() : __WEIGHTOUT_NAME,
        __MEM_MAX.name() : __MEM_MAX,
        __FSCALE_DEFAULT.name() : __FSCALE_DEFAULT,
        __IMAGE_SIZE.name() : __IMAGE_SIZE,
        __RESAMPLE_DIR.name() : __RESAMPLE_DIR,
        __PIXEL_SCALE.name() : __PIXEL_SCALE,
        __HEADER_SUFFIX.name() : __HEADER_SUFFIX,
        __GAIN_KEYWORD.name() : __GAIN_KEYWORD,
        __DELETE_TMPFILES.name() : __DELETE_TMPFILES,
        __GAIN_DEFAULT.name() : __GAIN_DEFAULT,
        __BACK_FILTERSIZE.name() : __BACK_FILTERSIZE,
        __BACK_DEFAULT.name() : __BACK_DEFAULT,
        __RESAMPLE.name() : __RESAMPLE,
        __NTHREADS.name() : __NTHREADS,
        __WEIGHT_IMAGE.name() : __WEIGHT_IMAGE,
        __VMEM_MAX.name() : __VMEM_MAX,
        __WRITE_FILEINFO.name() : __WRITE_FILEINFO,
        __COMBINE.name() : __COMBINE,
        __INTERPOLATE.name() : __INTERPOLATE,
        __WEIGHT_SUFFIX.name() : __WEIGHT_SUFFIX,
        __BACK_TYPE.name() : __BACK_TYPE,
        __VERBOSE_TYPE.name() : __VERBOSE_TYPE,
        __COMBINE_BUFSIZE.name() : __COMBINE_BUFSIZE,
        __COMBINE_TYPE.name() : __COMBINE_TYPE,
        __FSCALE_KEYWORD.name() : __FSCALE_KEYWORD,
        __RESAMPLING_TYPE.name() : __RESAMPLING_TYPE,
        __BACK_SIZE.name() : __BACK_SIZE,
        __COPY_KEYWORDS.name() : __COPY_KEYWORDS
    })
    _AttributeMap = config._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'swarpConfig', swarpConfig)


# Complex type weightFrame with content type ELEMENT_ONLY
class weightFrame (CommonDM.dm.bas.img_stub.processTargetDataObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'weightFrame')
    # Base type is CommonDM.dm.bas.img_stub.processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}Naxis2 uses Python identifier Naxis2
    __Naxis2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Naxis2'), 'Naxis2', '__httpeuclid_esa_orgschemaproext_weightFrame_httpeuclid_esa_orgschemaproextNaxis2', False)

    
    Naxis2 = property(__Naxis2.value, __Naxis2.set, None, u' Length of data in axis 2 [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Hot uses Python identifier Hot
    __Hot = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Hot'), 'Hot', '__httpeuclid_esa_orgschemaproext_weightFrame_httpeuclid_esa_orgschemaproextHot', False)

    
    Hot = property(__Hot.value, __Hot.set, None, u' Information about the detector\n                                hot pixels [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ImStat uses Python identifier ImStat
    __ImStat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImStat'), 'ImStat', '__httpeuclid_esa_orgschemaproext_weightFrame_httpeuclid_esa_orgschemaproextImStat', False)

    
    ImStat = property(__ImStat.value, __ImStat.set, None, u' Information about the statistics\n                                of the image pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Satellite uses Python identifier Satellite
    __Satellite = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Satellite'), 'Satellite', '__httpeuclid_esa_orgschemaproext_weightFrame_httpeuclid_esa_orgschemaproextSatellite', False)

    
    Satellite = property(__Satellite.value, __Satellite.set, None, u' Information about pixels affected\n                                by satellite tracks [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Saturated uses Python identifier Saturated
    __Saturated = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Saturated'), 'Saturated', '__httpeuclid_esa_orgschemaproext_weightFrame_httpeuclid_esa_orgschemaproextSaturated', False)

    
    Saturated = property(__Saturated.value, __Saturated.set, None, u' Information about saturated\n                                pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Cold uses Python identifier Cold
    __Cold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cold'), 'Cold', '__httpeuclid_esa_orgschemaproext_weightFrame_httpeuclid_esa_orgschemaproextCold', False)

    
    Cold = property(__Cold.value, __Cold.set, None, u' Information about the detector\n                                cold pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Naxis1 uses Python identifier Naxis1
    __Naxis1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Naxis1'), 'Naxis1', '__httpeuclid_esa_orgschemaproext_weightFrame_httpeuclid_esa_orgschemaproextNaxis1', False)

    
    Naxis1 = property(__Naxis1.value, __Naxis1.set, None, u' Length of data in axis 1 [pixel] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Flat uses Python identifier Flat
    __Flat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flat'), 'Flat', '__httpeuclid_esa_orgschemaproext_weightFrame_httpeuclid_esa_orgschemaproextFlat', False)

    
    Flat = property(__Flat.value, __Flat.set, None, u' Information about the detector\n                                sensitivity variations [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Cosmic uses Python identifier Cosmic
    __Cosmic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cosmic'), 'Cosmic', '__httpeuclid_esa_orgschemaproext_weightFrame_httpeuclid_esa_orgschemaproextCosmic', False)

    
    Cosmic = property(__Cosmic.value, __Cosmic.set, None, u' Information about pixels affected\n                                by cosmic ray events [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Illumination uses Python identifier Illumination
    __Illumination = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), 'Illumination', '__httpeuclid_esa_orgschemaproext_weightFrame_httpeuclid_esa_orgschemaproextIllumination', False)

    
    Illumination = property(__Illumination.value, __Illumination.set, None, u' Information about the\n                                illumination correction [None] ')


    _ElementMap = CommonDM.dm.bas.img_stub.processTargetDataObject._ElementMap.copy()
    _ElementMap.update({
        __Naxis2.name() : __Naxis2,
        __Hot.name() : __Hot,
        __ImStat.name() : __ImStat,
        __Satellite.name() : __Satellite,
        __Saturated.name() : __Saturated,
        __Cold.name() : __Cold,
        __Naxis1.name() : __Naxis1,
        __Flat.name() : __Flat,
        __Cosmic.name() : __Cosmic,
        __Illumination.name() : __Illumination
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.processTargetDataObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'weightFrame', weightFrame)


# Complex type rawBiasFrame with content type ELEMENT_ONLY
class rawBiasFrame (rawFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawBiasFrame')
    # Base type is rawFrame
    
    # Element ObsBlock ({http://euclid.esa.org/schema/pro/ext}ObsBlock) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_rawBiasFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Ovscy ({http://euclid.esa.org/schema/pro/ext}Ovscy) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscypst ({http://euclid.esa.org/schema/pro/ext}Ovscypst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element OverscanXStat ({http://euclid.esa.org/schema/pro/ext}OverscanXStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscxpre ({http://euclid.esa.org/schema/pro/ext}Prscxpre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Object ({http://euclid.esa.org/schema/pro/ext}Object) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element PrescanYStat ({http://euclid.esa.org/schema/pro/ext}PrescanYStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscypre ({http://euclid.esa.org/schema/pro/ext}Prscypre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Date ({http://euclid.esa.org/schema/pro/ext}Date) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element OverscanYStat ({http://euclid.esa.org/schema/pro/ext}OverscanYStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscxpre ({http://euclid.esa.org/schema/pro/ext}Ovscxpre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element DateObs ({http://euclid.esa.org/schema/pro/ext}DateObs) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Ovscypre ({http://euclid.esa.org/schema/pro/ext}Ovscypre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element MjdObs ({http://euclid.esa.org/schema/pro/ext}MjdObs) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Extension ({http://euclid.esa.org/schema/pro/ext}Extension) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscxpst ({http://euclid.esa.org/schema/pro/ext}Prscxpst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Lst ({http://euclid.esa.org/schema/pro/ext}Lst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element RawFits ({http://euclid.esa.org/schema/pro/ext}RawFits) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element PrescanXStat ({http://euclid.esa.org/schema/pro/ext}PrescanXStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Utc ({http://euclid.esa.org/schema/pro/ext}Utc) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscxpst ({http://euclid.esa.org/schema/pro/ext}Ovscxpst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscx ({http://euclid.esa.org/schema/pro/ext}Prscx) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Template ({http://euclid.esa.org/schema/pro/ext}Template) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Chip ({http://euclid.esa.org/schema/pro/ext}Chip) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscy ({http://euclid.esa.org/schema/pro/ext}Prscy) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Observer ({http://euclid.esa.org/schema/pro/ext}Observer) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscx ({http://euclid.esa.org/schema/pro/ext}Ovscx) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscypst ({http://euclid.esa.org/schema/pro/ext}Prscypst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame

    _ElementMap = rawFrame._ElementMap.copy()
    _ElementMap.update({
        __ProcessParams.name() : __ProcessParams
    })
    _AttributeMap = rawFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'rawBiasFrame', rawBiasFrame)


# Complex type readNoise with content type ELEMENT_ONLY
class readNoise (CommonDM.dm.bas.img_stub.processTarget):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'readNoise')
    # Base type is CommonDM.dm.bas.img_stub.processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}MedianDiff uses Python identifier MedianDiff
    __MedianDiff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MedianDiff'), 'MedianDiff', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextMedianDiff', False)

    
    MedianDiff = property(__MedianDiff.value, __MedianDiff.set, None, u' Median pixel value difference\n                                between biases [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MeanDiff uses Python identifier MeanDiff
    __MeanDiff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MeanDiff'), 'MeanDiff', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextMeanDiff', False)

    
    MeanDiff = property(__MeanDiff.value, __MeanDiff.set, None, u' Mean pixel value difference\n                                between biases [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ReadNoise uses Python identifier ReadNoise
    __ReadNoise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise'), 'ReadNoise', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextReadNoise', False)

    
    ReadNoise = property(__ReadNoise.value, __ReadNoise.set, None, u' Value of readout noise\n                                measurement [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RawBiasFrames uses Python identifier RawBiasFrames
    __RawBiasFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames'), 'RawBiasFrames', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextRawBiasFrames', True)

    
    RawBiasFrames = property(__RawBiasFrames.value, __RawBiasFrames.set, None, u' List of input raw bias frames\n                                [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_readNoise_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')


    _ElementMap = CommonDM.dm.bas.img_stub.processTarget._ElementMap.copy()
    _ElementMap.update({
        __MedianDiff.name() : __MedianDiff,
        __MeanDiff.name() : __MeanDiff,
        __Template.name() : __Template,
        __ReadNoise.name() : __ReadNoise,
        __RawBiasFrames.name() : __RawBiasFrames,
        __Chip.name() : __Chip,
        __ObsBlock.name() : __ObsBlock,
        __ProcessParams.name() : __ProcessParams,
        __TimestampStart.name() : __TimestampStart,
        __Instrument.name() : __Instrument,
        __TimestampEnd.name() : __TimestampEnd
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.processTarget._AttributeMap.copy()
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
    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumStdevDifference uses Python identifier MaximumStdevDifference
    __MaximumStdevDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumStdevDifference'), 'MaximumStdevDifference', '__httpeuclid_esa_orgschemaproext_biasFrameParameters_httpeuclid_esa_orgschemaproextMaximumStdevDifference', False)

    
    MaximumStdevDifference = property(__MaximumStdevDifference.value, __MaximumStdevDifference.set, None, u' QC: Maximum sample standard deviation\n                        difference of the bias levels relative to the previous\n                        version [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_biasFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumAbsMean uses Python identifier MaximumAbsMean
    __MaximumAbsMean = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumAbsMean'), 'MaximumAbsMean', '__httpeuclid_esa_orgschemaproext_biasFrameParameters_httpeuclid_esa_orgschemaproextMaximumAbsMean', False)

    
    MaximumAbsMean = property(__MaximumAbsMean.value, __MaximumAbsMean.set, None, u' QC: Maximum absolute mean value of the\n                        bias levels [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumSubwinFlatness uses Python identifier MaximumSubwinFlatness
    __MaximumSubwinFlatness = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness'), 'MaximumSubwinFlatness', '__httpeuclid_esa_orgschemaproext_biasFrameParameters_httpeuclid_esa_orgschemaproextMaximumSubwinFlatness', False)

    
    MaximumSubwinFlatness = property(__MaximumSubwinFlatness.value, __MaximumSubwinFlatness.set, None, u' QC: Maximum difference between median\n                        values of any two sub-windows [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}OverscanCorrection uses Python identifier OverscanCorrection
    __OverscanCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), 'OverscanCorrection', '__httpeuclid_esa_orgschemaproext_biasFrameParameters_httpeuclid_esa_orgschemaproextOverscanCorrection', False)

    
    OverscanCorrection = property(__OverscanCorrection.value, __OverscanCorrection.set, None, u' Overscan correction method index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumStdev uses Python identifier MaximumStdev
    __MaximumStdev = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumStdev'), 'MaximumStdev', '__httpeuclid_esa_orgschemaproext_biasFrameParameters_httpeuclid_esa_orgschemaproextMaximumStdev', False)

    
    MaximumStdev = property(__MaximumStdev.value, __MaximumStdev.set, None, u' QC: Maximum sample standard deviation\n                        value of the bias levels [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumSubwinStdev uses Python identifier MaximumSubwinStdev
    __MaximumSubwinStdev = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinStdev'), 'MaximumSubwinStdev', '__httpeuclid_esa_orgschemaproext_biasFrameParameters_httpeuclid_esa_orgschemaproextMaximumSubwinStdev', False)

    
    MaximumSubwinStdev = property(__MaximumSubwinStdev.value, __MaximumSubwinStdev.set, None, u' QC: Maximum sample standard deviation\n                        value of any sub-window [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SigmaClip uses Python identifier SigmaClip
    __SigmaClip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip'), 'SigmaClip', '__httpeuclid_esa_orgschemaproext_biasFrameParameters_httpeuclid_esa_orgschemaproextSigmaClip', False)

    
    SigmaClip = property(__SigmaClip.value, __SigmaClip.set, None, u' Threshold factor for rejecting raw bias\n                        pixel value outliers (sigma is taken as the readout\n                        noise measurement) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_biasFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __MaximumStdevDifference.name() : __MaximumStdevDifference,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __MaximumAbsMean.name() : __MaximumAbsMean,
        __MaximumSubwinFlatness.name() : __MaximumSubwinFlatness,
        __OverscanCorrection.name() : __OverscanCorrection,
        __MaximumStdev.name() : __MaximumStdev,
        __MaximumSubwinStdev.name() : __MaximumSubwinStdev,
        __SigmaClip.name() : __SigmaClip,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'biasFrameParameters', biasFrameParameters)


# Complex type associateConfig with content type ELEMENT_ONLY
class associateConfig (config):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'associateConfig')
    # Base type is config
    
    # Element {http://euclid.esa.org/schema/pro/ext}ISO_COLOR_TOL uses Python identifier ISO_COLOR_TOL
    __ISO_COLOR_TOL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ISO_COLOR_TOL'), 'ISO_COLOR_TOL', '__httpeuclid_esa_orgschemaproext_associateConfig_httpeuclid_esa_orgschemaproextISO_COLOR_TOL', False)

    
    ISO_COLOR_TOL = property(__ISO_COLOR_TOL.value, __ISO_COLOR_TOL.set, None, u' Factor with which the object\n                                dimensions (second order moments) are multiplied\n                                to search for overlap between objects within the\n                                same input catalog [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}VERBOSE uses Python identifier VERBOSE
    __VERBOSE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE'), 'VERBOSE', '__httpeuclid_esa_orgschemaproext_associateConfig_httpeuclid_esa_orgschemaproextVERBOSE', False)

    
    VERBOSE = property(__VERBOSE.value, __VERBOSE.set, None, u' Verbosity level (NONE, NORMAL,\n                                VERBOSE, DEBUG) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MASK uses Python identifier MASK
    __MASK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MASK'), 'MASK', '__httpeuclid_esa_orgschemaproext_associateConfig_httpeuclid_esa_orgschemaproextMASK', False)

    
    MASK = property(__MASK.value, __MASK.set, None, u' SExtractor mask to select objects\n                                for astrometric pairing: Flag and FLAG_MASK\n                                [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/pro/ext}ExtObjectId) inherited from {http://euclid.esa.org/schema/pro/ext}config
    
    # Element {http://euclid.esa.org/schema/pro/ext}INTER_COLOR_TOL uses Python identifier INTER_COLOR_TOL
    __INTER_COLOR_TOL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'INTER_COLOR_TOL'), 'INTER_COLOR_TOL', '__httpeuclid_esa_orgschemaproext_associateConfig_httpeuclid_esa_orgschemaproextINTER_COLOR_TOL', False)

    
    INTER_COLOR_TOL = property(__INTER_COLOR_TOL.value, __INTER_COLOR_TOL.set, None, u' Factor with which the object\n                                dimensions (second order moments) are multiplied\n                                to search for overlap between objects of\n                                different input catalogs [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PAIR_COLS uses Python identifier PAIR_COLS
    __PAIR_COLS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PAIR_COLS'), 'PAIR_COLS', '__httpeuclid_esa_orgschemaproext_associateConfig_httpeuclid_esa_orgschemaproextPAIR_COLS', False)

    
    PAIR_COLS = property(__PAIR_COLS.value, __PAIR_COLS.set, None, u' Enable the output of the PAIRS\n                                association column [None] ')


    _ElementMap = config._ElementMap.copy()
    _ElementMap.update({
        __ISO_COLOR_TOL.name() : __ISO_COLOR_TOL,
        __VERBOSE.name() : __VERBOSE,
        __MASK.name() : __MASK,
        __INTER_COLOR_TOL.name() : __INTER_COLOR_TOL,
        __PAIR_COLS.name() : __PAIR_COLS
    })
    _AttributeMap = config._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'associateConfig', associateConfig)


# Complex type astromConfig with content type ELEMENT_ONLY
class astromConfig (config):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'astromConfig')
    # Base type is config
    
    # Element {http://euclid.esa.org/schema/pro/ext}NITER uses Python identifier NITER
    __NITER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NITER'), 'NITER', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextNITER', False)

    
    NITER = property(__NITER.value, __NITER.set, None, u' Number of iterations during\n                                solving [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}YMIN uses Python identifier YMIN
    __YMIN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YMIN'), 'YMIN', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextYMIN', False)

    
    YMIN = property(__YMIN.value, __YMIN.set, None, u' Minimum Y coordinate of useful\n                                pixel plane [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}THRESHFRAC uses Python identifier THRESHFRAC
    __THRESHFRAC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'THRESHFRAC'), 'THRESHFRAC', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextTHRESHFRAC', False)

    
    THRESHFRAC = property(__THRESHFRAC.value, __THRESHFRAC.set, None, u' Fraction of the maximum threshold\n                                below which the iteration is allowed to\n                                threshold [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}XMIN uses Python identifier XMIN
    __XMIN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XMIN'), 'XMIN', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextXMIN', False)

    
    XMIN = property(__XMIN.value, __XMIN.set, None, u' Minimum X coordinate of useful\n                                pixel plane [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FDEG uses Python identifier FDEG
    __FDEG = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FDEG'), 'FDEG', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextFDEG', True)

    
    FDEG = property(__FDEG.value, __FDEG.set, None, u' List of degrees of freedom of\n                                Chebychev polynomials [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}YMAX uses Python identifier YMAX
    __YMAX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YMAX'), 'YMAX', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextYMAX', False)

    
    YMAX = property(__YMAX.value, __YMAX.set, None, u' Maximum Y coordinate of useful\n                                pixel plane [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}VERBOSE uses Python identifier VERBOSE
    __VERBOSE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE'), 'VERBOSE', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextVERBOSE', False)

    
    VERBOSE = property(__VERBOSE.value, __VERBOSE.set, None, u' Verbosity level (QUIET, NORMAL,\n                                EXTRA_WARNINGS, FULL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}XPIXSIZE uses Python identifier XPIXSIZE
    __XPIXSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XPIXSIZE'), 'XPIXSIZE', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextXPIXSIZE', False)

    
    XPIXSIZE = property(__XPIXSIZE.value, __XPIXSIZE.set, None, u' Scaling of pixels with which\n                                CDELT1 is multiplied [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}XMAX uses Python identifier XMAX
    __XMAX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XMAX'), 'XMAX', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextXMAX', False)

    
    XMAX = property(__XMAX.value, __XMAX.set, None, u' Maximum X coordinate of useful\n                                pixel plane [pixel] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/pro/ext}ExtObjectId) inherited from {http://euclid.esa.org/schema/pro/ext}config
    
    # Element {http://euclid.esa.org/schema/pro/ext}PDEG uses Python identifier PDEG
    __PDEG = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PDEG'), 'PDEG', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextPDEG', False)

    
    PDEG = property(__PDEG.value, __PDEG.set, None, u' Degrees of freedom for plate\n                                polynomials [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}YPIXSIZE uses Python identifier YPIXSIZE
    __YPIXSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YPIXSIZE'), 'YPIXSIZE', '__httpeuclid_esa_orgschemaproext_astromConfig_httpeuclid_esa_orgschemaproextYPIXSIZE', False)

    
    YPIXSIZE = property(__YPIXSIZE.value, __YPIXSIZE.set, None, u' Scaling of pixels with which\n                                CDELT2 is multiplied [None] ')


    _ElementMap = config._ElementMap.copy()
    _ElementMap.update({
        __NITER.name() : __NITER,
        __YMIN.name() : __YMIN,
        __THRESHFRAC.name() : __THRESHFRAC,
        __XMIN.name() : __XMIN,
        __FDEG.name() : __FDEG,
        __YMAX.name() : __YMAX,
        __VERBOSE.name() : __VERBOSE,
        __XPIXSIZE.name() : __XPIXSIZE,
        __XMAX.name() : __XMAX,
        __PDEG.name() : __PDEG,
        __YPIXSIZE.name() : __YPIXSIZE
    })
    _AttributeMap = config._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'astromConfig', astromConfig)


# Complex type lamp with content type ELEMENT_ONLY
class lamp (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lamp')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemaproext_lamp_httpeuclid_esa_orgschemaproextName', False)

    
    Name = property(__Name.value, __Name.set, None, u' Name of the lamp [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Position'), 'Position', '__httpeuclid_esa_orgschemaproext_lamp_httpeuclid_esa_orgschemaproextPosition', False)

    
    Position = property(__Position.value, __Position.set, None, u' Position of the lamp [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemaproext_lamp_httpeuclid_esa_orgschemaproextIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u' ID of the lamp [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_lamp_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DateFit uses Python identifier DateFit
    __DateFit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DateFit'), 'DateFit', '__httpeuclid_esa_orgschemaproext_lamp_httpeuclid_esa_orgschemaproextDateFit', False)

    
    DateFit = property(__DateFit.value, __DateFit.set, None, u' Date the lamp was fitted [None] ')


    _ElementMap = {
        __Name.name() : __Name,
        __Position.name() : __Position,
        __Identifier.name() : __Identifier,
        __ExtObjectId.name() : __ExtObjectId,
        __DateFit.name() : __DateFit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'lamp', lamp)


# Complex type illuminationCorrectionParameters with content type ELEMENT_ONLY
class illuminationCorrectionParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminationCorrectionParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}SigmaClippingLevel uses Python identifier SigmaClippingLevel
    __SigmaClippingLevel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel'), 'SigmaClippingLevel', '__httpeuclid_esa_orgschemaproext_illuminationCorrectionParameters_httpeuclid_esa_orgschemaproextSigmaClippingLevel', False)

    
    SigmaClippingLevel = property(__SigmaClippingLevel.value, __SigmaClippingLevel.set, None, u' Sigma clipping threshold from the median\n                        zeropoint [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_illuminationCorrectionParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __SigmaClippingLevel.name() : __SigmaClippingLevel,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'illuminationCorrectionParameters', illuminationCorrectionParameters)


# Complex type photSrcCatalogParameters with content type ELEMENT_ONLY
class photSrcCatalogParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photSrcCatalogParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_photSrcCatalogParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxMagDiff uses Python identifier MaxMagDiff
    __MaxMagDiff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxMagDiff'), 'MaxMagDiff', '__httpeuclid_esa_orgschemaproext_photSrcCatalogParameters_httpeuclid_esa_orgschemaproextMaxMagDiff', False)

    
    MaxMagDiff = property(__MaxMagDiff.value, __MaxMagDiff.set, None, u' Maximum difference of a standard star\n                        magnitude with respect to the median\n                        [mag]')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FluxType uses Python identifier FluxType
    __FluxType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FluxType'), 'FluxType', '__httpeuclid_esa_orgschemaproext_photSrcCatalogParameters_httpeuclid_esa_orgschemaproextFluxType', False)

    
    FluxType = property(__FluxType.value, __FluxType.set, None, u' Type of the measured flux (SExtractor\n                        parameter name) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_photSrcCatalogParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __MaxMagDiff.name() : __MaxMagDiff,
        __FluxType.name() : __FluxType,
        __SourceCodeVersion.name() : __SourceCodeVersion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'photSrcCatalogParameters', photSrcCatalogParameters)


# Complex type readNoiseParameters with content type ELEMENT_ONLY
class readNoiseParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'readNoiseParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumBiasDifference uses Python identifier MaximumBiasDifference
    __MaximumBiasDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumBiasDifference'), 'MaximumBiasDifference', '__httpeuclid_esa_orgschemaproext_readNoiseParameters_httpeuclid_esa_orgschemaproextMaximumBiasDifference', False)

    
    MaximumBiasDifference = property(__MaximumBiasDifference.value, __MaximumBiasDifference.set, None, u' QC: Maximum mean pixel value difference\n                        between biases [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumIterations uses Python identifier MaximumIterations
    __MaximumIterations = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations'), 'MaximumIterations', '__httpeuclid_esa_orgschemaproext_readNoiseParameters_httpeuclid_esa_orgschemaproextMaximumIterations', False)

    
    MaximumIterations = property(__MaximumIterations.value, __MaximumIterations.set, None, u' Maximum number of iterations for\n                        estimating statistics [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumReadNoiseDifference uses Python identifier MaximumReadNoiseDifference
    __MaximumReadNoiseDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumReadNoiseDifference'), 'MaximumReadNoiseDifference', '__httpeuclid_esa_orgschemaproext_readNoiseParameters_httpeuclid_esa_orgschemaproextMaximumReadNoiseDifference', False)

    
    MaximumReadNoiseDifference = property(__MaximumReadNoiseDifference.value, __MaximumReadNoiseDifference.set, None, u' QC: Maximum difference between readout\n                        noise measurements relative to the previous version\n                        [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_readNoiseParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumReadNoise uses Python identifier MaximumReadNoise
    __MaximumReadNoise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumReadNoise'), 'MaximumReadNoise', '__httpeuclid_esa_orgschemaproext_readNoiseParameters_httpeuclid_esa_orgschemaproextMaximumReadNoise', False)

    
    MaximumReadNoise = property(__MaximumReadNoise.value, __MaximumReadNoise.set, None, u' QC: Maximum value for the readout noise\n                        [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_readNoiseParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RejectionThreshold uses Python identifier RejectionThreshold
    __RejectionThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold'), 'RejectionThreshold', '__httpeuclid_esa_orgschemaproext_readNoiseParameters_httpeuclid_esa_orgschemaproextRejectionThreshold', False)

    
    RejectionThreshold = property(__RejectionThreshold.value, __RejectionThreshold.set, None, u' Threshold for rejecting pixels with\n                        outlying values [None] ')


    _ElementMap = {
        __MaximumBiasDifference.name() : __MaximumBiasDifference,
        __MaximumIterations.name() : __MaximumIterations,
        __MaximumReadNoiseDifference.name() : __MaximumReadNoiseDifference,
        __ExtObjectId.name() : __ExtObjectId,
        __MaximumReadNoise.name() : __MaximumReadNoise,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __RejectionThreshold.name() : __RejectionThreshold
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'readNoiseParameters', readNoiseParameters)


# Complex type photExtinctionCurve with content type ELEMENT_ONLY
class photExtinctionCurve (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photExtinctionCurve')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}WavelengthIncrement uses Python identifier WavelengthIncrement
    __WavelengthIncrement = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WavelengthIncrement'), 'WavelengthIncrement', '__httpeuclid_esa_orgschemaproext_photExtinctionCurve_httpeuclid_esa_orgschemaproextWavelengthIncrement', False)

    
    WavelengthIncrement = property(__WavelengthIncrement.value, __WavelengthIncrement.set, None, u' Wavelength increment [angstrom] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Storage uses Python identifier Storage
    __Storage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Storage'), 'Storage', '__httpeuclid_esa_orgschemaproext_photExtinctionCurve_httpeuclid_esa_orgschemaproextStorage', False)

    
    Storage = property(__Storage.value, __Storage.set, None, u' Customized storage container for the data\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), 'CreationDate', '__httpeuclid_esa_orgschemaproext_photExtinctionCurve_httpeuclid_esa_orgschemaproextCreationDate', False)

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, u' UTC date this object was created [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_photExtinctionCurve_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtinctionPointList uses Python identifier ExtinctionPointList
    __ExtinctionPointList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtinctionPointList'), 'ExtinctionPointList', '__httpeuclid_esa_orgschemaproext_photExtinctionCurve_httpeuclid_esa_orgschemaproextExtinctionPointList', True)

    
    ExtinctionPointList = property(__ExtinctionPointList.value, __ExtinctionPointList.set, None, u' List of input atmospheric extinction\n                        points [None] ')


    _ElementMap = {
        __WavelengthIncrement.name() : __WavelengthIncrement,
        __Storage.name() : __Storage,
        __CreationDate.name() : __CreationDate,
        __ExtObjectId.name() : __ExtObjectId,
        __ExtinctionPointList.name() : __ExtinctionPointList
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'photExtinctionCurve', photExtinctionCurve)


# Complex type rawScienceFrame with content type ELEMENT_ONLY
class rawScienceFrame (rawFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawScienceFrame')
    # Base type is rawFrame
    
    # Element ObsBlock ({http://euclid.esa.org/schema/pro/ext}ObsBlock) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Ovscy ({http://euclid.esa.org/schema/pro/ext}Ovscy) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscypst ({http://euclid.esa.org/schema/pro/ext}Ovscypst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element OverscanXStat ({http://euclid.esa.org/schema/pro/ext}OverscanXStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscxpre ({http://euclid.esa.org/schema/pro/ext}Prscxpre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element OverscanYStat ({http://euclid.esa.org/schema/pro/ext}OverscanYStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element PrescanYStat ({http://euclid.esa.org/schema/pro/ext}PrescanYStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscypre ({http://euclid.esa.org/schema/pro/ext}Prscypre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Date ({http://euclid.esa.org/schema/pro/ext}Date) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Object ({http://euclid.esa.org/schema/pro/ext}Object) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscxpre ({http://euclid.esa.org/schema/pro/ext}Ovscxpre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element DateObs ({http://euclid.esa.org/schema/pro/ext}DateObs) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_rawScienceFrame_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element Ovscypre ({http://euclid.esa.org/schema/pro/ext}Ovscypre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element MjdObs ({http://euclid.esa.org/schema/pro/ext}MjdObs) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Astrom uses Python identifier Astrom
    __Astrom = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Astrom'), 'Astrom', '__httpeuclid_esa_orgschemaproext_rawScienceFrame_httpeuclid_esa_orgschemaproextAstrom', False)

    
    Astrom = property(__Astrom.value, __Astrom.set, None, u' Basic information about the\n                                astrometry (linear terms only) [None] ')

    
    # Element Extension ({http://euclid.esa.org/schema/pro/ext}Extension) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscxpst ({http://euclid.esa.org/schema/pro/ext}Prscxpst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Lst ({http://euclid.esa.org/schema/pro/ext}Lst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExpTime uses Python identifier ExpTime
    __ExpTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), 'ExpTime', '__httpeuclid_esa_orgschemaproext_rawScienceFrame_httpeuclid_esa_orgschemaproextExpTime', False)

    
    ExpTime = property(__ExpTime.value, __ExpTime.set, None, u' Total time of an individual\n                                exposure [sec] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Prscypst ({http://euclid.esa.org/schema/pro/ext}Prscypst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element PrescanXStat ({http://euclid.esa.org/schema/pro/ext}PrescanXStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Utc ({http://euclid.esa.org/schema/pro/ext}Utc) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}AirmassStart uses Python identifier AirmassStart
    __AirmassStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AirmassStart'), 'AirmassStart', '__httpeuclid_esa_orgschemaproext_rawScienceFrame_httpeuclid_esa_orgschemaproextAirmassStart', False)

    
    AirmassStart = property(__AirmassStart.value, __AirmassStart.set, None, u' Airmass at the beginning of the\n                                observation [None] ')

    
    # Element Ovscxpst ({http://euclid.esa.org/schema/pro/ext}Ovscxpst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscx ({http://euclid.esa.org/schema/pro/ext}Prscx) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Template ({http://euclid.esa.org/schema/pro/ext}Template) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}AirmassEnd uses Python identifier AirmassEnd
    __AirmassEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AirmassEnd'), 'AirmassEnd', '__httpeuclid_esa_orgschemaproext_rawScienceFrame_httpeuclid_esa_orgschemaproextAirmassEnd', False)

    
    AirmassEnd = property(__AirmassEnd.value, __AirmassEnd.set, None, u' Airmass at the ending of the\n                                observation [None] ')

    
    # Element Chip ({http://euclid.esa.org/schema/pro/ext}Chip) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscy ({http://euclid.esa.org/schema/pro/ext}Prscy) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Observer ({http://euclid.esa.org/schema/pro/ext}Observer) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscx ({http://euclid.esa.org/schema/pro/ext}Ovscx) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element RawFits ({http://euclid.esa.org/schema/pro/ext}RawFits) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame

    _ElementMap = rawFrame._ElementMap.copy()
    _ElementMap.update({
        __Filter.name() : __Filter,
        __Astrom.name() : __Astrom,
        __ExpTime.name() : __ExpTime,
        __AirmassStart.name() : __AirmassStart,
        __AirmassEnd.name() : __AirmassEnd
    })
    _AttributeMap = rawFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'rawScienceFrame', rawScienceFrame)


# Complex type gAstrometric with content type ELEMENT_ONLY
class gAstrometric (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'gAstrometric')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}Residuals uses Python identifier Residuals
    __Residuals = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Residuals'), 'Residuals', '__httpeuclid_esa_orgschemaproext_gAstrometric_httpeuclid_esa_orgschemaproextResiduals', False)

    
    Residuals = property(__Residuals.value, __Residuals.set, None, u' Filename of residuals FITS table [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}GasSList uses Python identifier GasSList
    __GasSList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GasSList'), 'GasSList', '__httpeuclid_esa_orgschemaproext_gAstrometric_httpeuclid_esa_orgschemaproextGasSList', False)

    
    GasSList = property(__GasSList.value, __GasSList.set, None, u' Information about the global astrometry\n                        associate list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_gAstrometric_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __Residuals.name() : __Residuals,
        __GasSList.name() : __GasSList,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'gAstrometric', gAstrometric)


# Complex type photSrcSource with content type ELEMENT_ONLY
class photSrcSource (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photSrcSource')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}RA uses Python identifier RA
    __RA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RA'), 'RA', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextRA', False)

    
    RA = property(__RA.value, __RA.set, None, u' Right ascension of the source [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MagErr uses Python identifier MagErr
    __MagErr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagErr'), 'MagErr', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextMagErr', False)

    
    MagErr = property(__MagErr.value, __MagErr.set, None, u' Measurement error of the magnitude error\n                        [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Index uses Python identifier Index
    __Index = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Index'), 'Index', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextIndex', False)

    
    Index = property(__Index.value, __Index.set, None, u' Index of the source [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DEC uses Python identifier DEC
    __DEC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEC'), 'DEC', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextDEC', False)

    
    DEC = property(__DEC.value, __DEC.set, None, u' Declination of the source [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}InstrumentalMag uses Python identifier InstrumentalMag
    __InstrumentalMag = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InstrumentalMag'), 'InstrumentalMag', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextInstrumentalMag', False)

    
    InstrumentalMag = property(__InstrumentalMag.value, __InstrumentalMag.set, None, u' Instrumental magnitude of the source\n                        [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}YPosition uses Python identifier YPosition
    __YPosition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YPosition'), 'YPosition', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextYPosition', False)

    
    YPosition = property(__YPosition.value, __YPosition.set, None, u' Detector Y position of the source [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}XPosition uses Python identifier XPosition
    __XPosition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XPosition'), 'XPosition', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextXPosition', False)

    
    XPosition = property(__XPosition.value, __XPosition.set, None, u' Detector X position of the source [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Mag uses Python identifier Mag
    __Mag = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Mag'), 'Mag', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextMag', False)

    
    Mag = property(__Mag.value, __Mag.set, None, u' Magnitude of the source [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}InstrumentalMagErr uses Python identifier InstrumentalMagErr
    __InstrumentalMagErr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InstrumentalMagErr'), 'InstrumentalMagErr', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextInstrumentalMagErr', False)

    
    InstrumentalMagErr = property(__InstrumentalMagErr.value, __InstrumentalMagErr.set, None, u' Measurement error of the instrumental\n                        magnitude [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Origin uses Python identifier Origin
    __Origin = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Origin'), 'Origin', '__httpeuclid_esa_orgschemaproext_photSrcSource_httpeuclid_esa_orgschemaproextOrigin', False)

    
    Origin = property(__Origin.value, __Origin.set, None, u' Origin of the source [None] ')


    _ElementMap = {
        __RA.name() : __RA,
        __MagErr.name() : __MagErr,
        __Index.name() : __Index,
        __DEC.name() : __DEC,
        __ExtObjectId.name() : __ExtObjectId,
        __InstrumentalMag.name() : __InstrumentalMag,
        __YPosition.name() : __YPosition,
        __XPosition.name() : __XPosition,
        __Mag.name() : __Mag,
        __InstrumentalMagErr.name() : __InstrumentalMagErr,
        __Origin.name() : __Origin
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'photSrcSource', photSrcSource)


# Complex type atmosphericExtinctionParameters with content type ELEMENT_ONLY
class atmosphericExtinctionParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'atmosphericExtinctionParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}SigclipLevel uses Python identifier SigclipLevel
    __SigclipLevel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigclipLevel'), 'SigclipLevel', '__httpeuclid_esa_orgschemaproext_atmosphericExtinctionParameters_httpeuclid_esa_orgschemaproextSigclipLevel', False)

    
    SigclipLevel = property(__SigclipLevel.value, __SigclipLevel.set, None, u' QC: Sigma clipping threshold factor\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxError uses Python identifier MaxError
    __MaxError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxError'), 'MaxError', '__httpeuclid_esa_orgschemaproext_atmosphericExtinctionParameters_httpeuclid_esa_orgschemaproextMaxError', False)

    
    MaxError = property(__MaxError.value, __MaxError.set, None, u' QC: Maximum relative (fractional) error\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_atmosphericExtinctionParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __SigclipLevel.name() : __SigclipLevel,
        __MaxError.name() : __MaxError,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'atmosphericExtinctionParameters', atmosphericExtinctionParameters)


# Complex type rawDomeFlatFrame with content type ELEMENT_ONLY
class rawDomeFlatFrame (rawFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawDomeFlatFrame')
    # Base type is rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_rawDomeFlatFrame_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element ObsBlock ({http://euclid.esa.org/schema/pro/ext}ObsBlock) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element MjdObs ({http://euclid.esa.org/schema/pro/ext}MjdObs) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Lamp uses Python identifier Lamp
    __Lamp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Lamp'), 'Lamp', '__httpeuclid_esa_orgschemaproext_rawDomeFlatFrame_httpeuclid_esa_orgschemaproextLamp', False)

    
    Lamp = property(__Lamp.value, __Lamp.set, None, u' Information about the dome flat\n                                lamp [None] ')

    
    # Element Ovscypst ({http://euclid.esa.org/schema/pro/ext}Ovscypst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element OverscanXStat ({http://euclid.esa.org/schema/pro/ext}OverscanXStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExpTime uses Python identifier ExpTime
    __ExpTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), 'ExpTime', '__httpeuclid_esa_orgschemaproext_rawDomeFlatFrame_httpeuclid_esa_orgschemaproextExpTime', False)

    
    ExpTime = property(__ExpTime.value, __ExpTime.set, None, u' Total time of an individual\n                                exposure [sec] ')

    
    # Element Prscxpre ({http://euclid.esa.org/schema/pro/ext}Prscxpre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Object ({http://euclid.esa.org/schema/pro/ext}Object) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element PrescanYStat ({http://euclid.esa.org/schema/pro/ext}PrescanYStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscypre ({http://euclid.esa.org/schema/pro/ext}Prscypre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Date ({http://euclid.esa.org/schema/pro/ext}Date) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element OverscanYStat ({http://euclid.esa.org/schema/pro/ext}OverscanYStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscxpre ({http://euclid.esa.org/schema/pro/ext}Ovscxpre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element DateObs ({http://euclid.esa.org/schema/pro/ext}DateObs) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscypre ({http://euclid.esa.org/schema/pro/ext}Ovscypre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Extension ({http://euclid.esa.org/schema/pro/ext}Extension) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscxpst ({http://euclid.esa.org/schema/pro/ext}Prscxpst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Lst ({http://euclid.esa.org/schema/pro/ext}Lst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscy ({http://euclid.esa.org/schema/pro/ext}Ovscy) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element RawFits ({http://euclid.esa.org/schema/pro/ext}RawFits) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element PrescanXStat ({http://euclid.esa.org/schema/pro/ext}PrescanXStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Utc ({http://euclid.esa.org/schema/pro/ext}Utc) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_rawDomeFlatFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Ovscxpst ({http://euclid.esa.org/schema/pro/ext}Ovscxpst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscx ({http://euclid.esa.org/schema/pro/ext}Prscx) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Template ({http://euclid.esa.org/schema/pro/ext}Template) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Chip ({http://euclid.esa.org/schema/pro/ext}Chip) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscy ({http://euclid.esa.org/schema/pro/ext}Prscy) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Observer ({http://euclid.esa.org/schema/pro/ext}Observer) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscx ({http://euclid.esa.org/schema/pro/ext}Ovscx) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscypst ({http://euclid.esa.org/schema/pro/ext}Prscypst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame

    _ElementMap = rawFrame._ElementMap.copy()
    _ElementMap.update({
        __Filter.name() : __Filter,
        __Lamp.name() : __Lamp,
        __ExpTime.name() : __ExpTime,
        __ProcessParams.name() : __ProcessParams
    })
    _AttributeMap = rawFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'rawDomeFlatFrame', rawDomeFlatFrame)


# Complex type biasFrame with content type ELEMENT_ONLY
class biasFrame (CommonDM.dm.bas.img_stub.baseCalFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'biasFrame')
    # Base type is CommonDM.dm.bas.img_stub.baseCalFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/bas/img}TimestampEnd) inherited from {http://euclid.esa.org/schema/bas/img}baseCalFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}RawBiasFrames uses Python identifier RawBiasFrames
    __RawBiasFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames'), 'RawBiasFrames', '__httpeuclid_esa_orgschemaproext_biasFrame_httpeuclid_esa_orgschemaproextRawBiasFrames', True)

    
    RawBiasFrames = property(__RawBiasFrames.value, __RawBiasFrames.set, None, u' List of input raw bias frames\n                                [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element TimestampStart ({http://euclid.esa.org/schema/bas/img}TimestampStart) inherited from {http://euclid.esa.org/schema/bas/img}baseCalFrame
    
    # Element Chip ({http://euclid.esa.org/schema/bas/img}Chip) inherited from {http://euclid.esa.org/schema/bas/img}baseCalFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ReadNoise uses Python identifier ReadNoise
    __ReadNoise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise'), 'ReadNoise', '__httpeuclid_esa_orgschemaproext_biasFrame_httpeuclid_esa_orgschemaproextReadNoise', False)

    
    ReadNoise = property(__ReadNoise.value, __ReadNoise.set, None, u' Information about the detector\n                                readout noise [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_biasFrame_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_biasFrame_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_biasFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')


    _ElementMap = CommonDM.dm.bas.img_stub.baseCalFrame._ElementMap.copy()
    _ElementMap.update({
        __RawBiasFrames.name() : __RawBiasFrames,
        __ReadNoise.name() : __ReadNoise,
        __Template.name() : __Template,
        __ObsBlock.name() : __ObsBlock,
        __ProcessParams.name() : __ProcessParams
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.baseCalFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'biasFrame', biasFrame)


# Complex type associateListParameters with content type ELEMENT_ONLY
class associateListParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'associateListParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}SearchDistance uses Python identifier SearchDistance
    __SearchDistance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SearchDistance'), 'SearchDistance', '__httpeuclid_esa_orgschemaproext_associateListParameters_httpeuclid_esa_orgschemaproextSearchDistance', False)

    
    SearchDistance = property(__SearchDistance.value, __SearchDistance.set, None, u' Radius of search for associates [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SextractorFlagMask uses Python identifier SextractorFlagMask
    __SextractorFlagMask = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SextractorFlagMask'), 'SextractorFlagMask', '__httpeuclid_esa_orgschemaproext_associateListParameters_httpeuclid_esa_orgschemaproextSextractorFlagMask', False)

    
    SextractorFlagMask = property(__SextractorFlagMask.value, __SextractorFlagMask.set, None, u' Value of SExtractor flag mask for source\n                        filtering [None]')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SingleOutClosestPairs uses Python identifier SingleOutClosestPairs
    __SingleOutClosestPairs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SingleOutClosestPairs'), 'SingleOutClosestPairs', '__httpeuclid_esa_orgschemaproext_associateListParameters_httpeuclid_esa_orgschemaproextSingleOutClosestPairs', False)

    
    SingleOutClosestPairs = property(__SingleOutClosestPairs.value, __SingleOutClosestPairs.set, None, u' Filter to retain only the closest\n                        associations [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_associateListParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_associateListParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __SearchDistance.name() : __SearchDistance,
        __SextractorFlagMask.name() : __SextractorFlagMask,
        __SingleOutClosestPairs.name() : __SingleOutClosestPairs,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'associateListParameters', associateListParameters)


# Complex type baseList with content type ELEMENT_ONLY
class baseList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextName', False)

    
    Name = property(__Name.value, __Name.set, None, u' Name of the list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Object uses Python identifier Object
    __Object = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Object'), 'Object', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextObject', False)

    
    Object = property(__Object.value, __Object.set, None, u' Name of target object [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}URDec uses Python identifier URDec
    __URDec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'URDec'), 'URDec', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextURDec', False)

    
    URDec = property(__URDec.value, __URDec.set, None, u' Declination of upper right corner [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}LLRa uses Python identifier LLRa
    __LLRa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LLRa'), 'LLRa', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextLLRa', False)

    
    LLRa = property(__LLRa.value, __LLRa.set, None, u' Right Ascension of lower left corner\n                        [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), 'CreationDate', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextCreationDate', False)

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, u' UTC date this object was created [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}LRDec uses Python identifier LRDec
    __LRDec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LRDec'), 'LRDec', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextLRDec', False)

    
    LRDec = property(__LRDec.value, __LRDec.set, None, u' Declination of lower right corner [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}IsValid uses Python identifier IsValid
    __IsValid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IsValid'), 'IsValid', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextIsValid', False)

    
    IsValid = property(__IsValid.value, __IsValid.set, None, u' Manual/external flag to disqualify bad\n                        data (SuperFlag) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}URRa uses Python identifier URRa
    __URRa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'URRa'), 'URRa', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextURRa', False)

    
    URRa = property(__URRa.value, __URRa.set, None, u' Right Ascension of upper right corner\n                        [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ULDec uses Python identifier ULDec
    __ULDec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ULDec'), 'ULDec', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextULDec', False)

    
    ULDec = property(__ULDec.value, __ULDec.set, None, u' Declination of upper left corner [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}LRRa uses Python identifier LRRa
    __LRRa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LRRa'), 'LRRa', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextLRRa', False)

    
    LRRa = property(__LRRa.value, __LRRa.set, None, u' Right Ascension of lower right corner\n                        [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}LLDec uses Python identifier LLDec
    __LLDec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LLDec'), 'LLDec', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextLLDec', False)

    
    LLDec = property(__LLDec.value, __LLDec.set, None, u' Declination of lower left corner [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ULRa uses Python identifier ULRa
    __ULRa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ULRa'), 'ULRa', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextULRa', False)

    
    ULRa = property(__ULRa.value, __ULRa.set, None, u' Right Ascension of upper left corner\n                        [deg] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Storage uses Python identifier Storage
    __Storage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Storage'), 'Storage', '__httpeuclid_esa_orgschemaproext_baseList_httpeuclid_esa_orgschemaproextStorage', False)

    
    Storage = property(__Storage.value, __Storage.set, None, u' Customized storage container for the data\n                        [None] ')


    _ElementMap = {
        __Name.name() : __Name,
        __Object.name() : __Object,
        __URDec.name() : __URDec,
        __ExtObjectId.name() : __ExtObjectId,
        __LLRa.name() : __LLRa,
        __CreationDate.name() : __CreationDate,
        __LRDec.name() : __LRDec,
        __IsValid.name() : __IsValid,
        __URRa.name() : __URRa,
        __ULDec.name() : __ULDec,
        __LRRa.name() : __LRRa,
        __LLDec.name() : __LLDec,
        __ULRa.name() : __ULRa,
        __Storage.name() : __Storage
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
    
    # Element LRDec ({http://euclid.esa.org/schema/pro/ext}LRDec) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element Name ({http://euclid.esa.org/schema/pro/ext}Name) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element ULDec ({http://euclid.esa.org/schema/pro/ext}ULDec) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element LRRa ({http://euclid.esa.org/schema/pro/ext}LRRa) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element URDec ({http://euclid.esa.org/schema/pro/ext}URDec) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element ULRa ({http://euclid.esa.org/schema/pro/ext}ULRa) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/pro/ext}ExtObjectId) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceLists uses Python identifier SourceLists
    __SourceLists = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceLists'), 'SourceLists', '__httpeuclid_esa_orgschemaproext_associateList_httpeuclid_esa_orgschemaproextSourceLists', True)

    
    SourceLists = property(__SourceLists.value, __SourceLists.set, None, u' List of input source lists [None] ')

    
    # Element LLRa ({http://euclid.esa.org/schema/pro/ext}LLRa) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}InputAssociateList uses Python identifier InputAssociateList
    __InputAssociateList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InputAssociateList'), 'InputAssociateList', '__httpeuclid_esa_orgschemaproext_associateList_httpeuclid_esa_orgschemaproextInputAssociateList', False)

    
    InputAssociateList = property(__InputAssociateList.value, __InputAssociateList.set, None, u' Information about the input\n                                associations [None] ')

    
    # Element LLDec ({http://euclid.esa.org/schema/pro/ext}LLDec) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}Associates uses Python identifier Associates
    __Associates = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Associates'), 'Associates', '__httpeuclid_esa_orgschemaproext_associateList_httpeuclid_esa_orgschemaproextAssociates', False)

    
    Associates = property(__Associates.value, __Associates.set, None, u' Column definitions of\n                                associations [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/pro/ext}IsValid) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_associateList_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/pro/ext}Storage) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element CreationDate ({http://euclid.esa.org/schema/pro/ext}CreationDate) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element URRa ({http://euclid.esa.org/schema/pro/ext}URRa) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}AssociateListType uses Python identifier AssociateListType
    __AssociateListType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AssociateListType'), 'AssociateListType', '__httpeuclid_esa_orgschemaproext_associateList_httpeuclid_esa_orgschemaproextAssociateListType', False)

    
    AssociateListType = property(__AssociateListType.value, __AssociateListType.set, None, u' Type of associate list [None] ')

    
    # Element Object ({http://euclid.esa.org/schema/pro/ext}Object) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}Alid uses Python identifier Alid
    __Alid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Alid'), 'Alid', '__httpeuclid_esa_orgschemaproext_associateList_httpeuclid_esa_orgschemaproextAlid', False)

    
    Alid = property(__Alid.value, __Alid.set, None, u' Identifier of the associate list\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}AssociateCount uses Python identifier AssociateCount
    __AssociateCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AssociateCount'), 'AssociateCount', '__httpeuclid_esa_orgschemaproext_associateList_httpeuclid_esa_orgschemaproextAssociateCount', False)

    
    AssociateCount = property(__AssociateCount.value, __AssociateCount.set, None, u' Number of associated source\n                                pairings [None] ')


    _ElementMap = baseList._ElementMap.copy()
    _ElementMap.update({
        __SourceLists.name() : __SourceLists,
        __InputAssociateList.name() : __InputAssociateList,
        __Associates.name() : __Associates,
        __ProcessParams.name() : __ProcessParams,
        __AssociateListType.name() : __AssociateListType,
        __Alid.name() : __Alid,
        __AssociateCount.name() : __AssociateCount
    })
    _AttributeMap = baseList._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'associateList', associateList)


# Complex type nightSkyFlatFrameParameters with content type ELEMENT_ONLY
class nightSkyFlatFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nightSkyFlatFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}OverscanCorrection uses Python identifier OverscanCorrection
    __OverscanCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), 'OverscanCorrection', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrameParameters_httpeuclid_esa_orgschemaproextOverscanCorrection', False)

    
    OverscanCorrection = property(__OverscanCorrection.value, __OverscanCorrection.set, None, u' Overscan correction method index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __OverscanCorrection.name() : __OverscanCorrection,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nightSkyFlatFrameParameters', nightSkyFlatFrameParameters)


# Complex type domeFlatFrameParameters with content type ELEMENT_ONLY
class domeFlatFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'domeFlatFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}SigmaClip uses Python identifier SigmaClip
    __SigmaClip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip'), 'SigmaClip', '__httpeuclid_esa_orgschemaproext_domeFlatFrameParameters_httpeuclid_esa_orgschemaproextSigmaClip', False)

    
    SigmaClip = property(__SigmaClip.value, __SigmaClip.set, None, u' Threshold factor for rejecting raw dome\n                        flat pixel value outliers (sigma is taken as the scaled\n                        gain measurement) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_domeFlatFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_domeFlatFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumSubwinFlatness uses Python identifier MaximumSubwinFlatness
    __MaximumSubwinFlatness = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness'), 'MaximumSubwinFlatness', '__httpeuclid_esa_orgschemaproext_domeFlatFrameParameters_httpeuclid_esa_orgschemaproextMaximumSubwinFlatness', False)

    
    MaximumSubwinFlatness = property(__MaximumSubwinFlatness.value, __MaximumSubwinFlatness.set, None, u' QC: Maximum difference between median\n                        values of any two sub-windows [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}OverscanCorrection uses Python identifier OverscanCorrection
    __OverscanCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), 'OverscanCorrection', '__httpeuclid_esa_orgschemaproext_domeFlatFrameParameters_httpeuclid_esa_orgschemaproextOverscanCorrection', False)

    
    OverscanCorrection = property(__OverscanCorrection.value, __OverscanCorrection.set, None, u' Overscan correction method index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumSubwinDiff uses Python identifier MaximumSubwinDiff
    __MaximumSubwinDiff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinDiff'), 'MaximumSubwinDiff', '__httpeuclid_esa_orgschemaproext_domeFlatFrameParameters_httpeuclid_esa_orgschemaproextMaximumSubwinDiff', False)

    
    MaximumSubwinDiff = property(__MaximumSubwinDiff.value, __MaximumSubwinDiff.set, None, u' QC: Difference in MaximumSubwinFlatness\n                        relative to the previous version [ADU] ')


    _ElementMap = {
        __SigmaClip.name() : __SigmaClip,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __ExtObjectId.name() : __ExtObjectId,
        __MaximumSubwinFlatness.name() : __MaximumSubwinFlatness,
        __OverscanCorrection.name() : __OverscanCorrection,
        __MaximumSubwinDiff.name() : __MaximumSubwinDiff
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'domeFlatFrameParameters', domeFlatFrameParameters)


# Complex type associateListDict with content type ELEMENT_ONLY
class associateListDict (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'associateListDict')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}SID uses Python identifier SID
    __SID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SID'), 'SID', '__httpeuclid_esa_orgschemaproext_associateListDict_httpeuclid_esa_orgschemaproextSID', False)

    
    SID = property(__SID.value, __SID.set, None, u' Identifier of a source in the source list\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SLID uses Python identifier SLID
    __SLID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SLID'), 'SLID', '__httpeuclid_esa_orgschemaproext_associateListDict_httpeuclid_esa_orgschemaproextSLID', False)

    
    SLID = property(__SLID.value, __SLID.set, None, u' Identifier of the source list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ALID uses Python identifier ALID
    __ALID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ALID'), 'ALID', '__httpeuclid_esa_orgschemaproext_associateListDict_httpeuclid_esa_orgschemaproextALID', False)

    
    ALID = property(__ALID.value, __ALID.set, None, u' Identifier of the associate list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}AID uses Python identifier AID
    __AID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AID'), 'AID', '__httpeuclid_esa_orgschemaproext_associateListDict_httpeuclid_esa_orgschemaproextAID', False)

    
    AID = property(__AID.value, __AID.set, None, u' Identifier of an association in the\n                        associate list [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLAG uses Python identifier FLAG
    __FLAG = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG'), 'FLAG', '__httpeuclid_esa_orgschemaproext_associateListDict_httpeuclid_esa_orgschemaproextFLAG', False)

    
    FLAG = property(__FLAG.value, __FLAG.set, None, u' Internal flag indicating the source\n                        list(s) participating in the association [None] ')


    _ElementMap = {
        __SID.name() : __SID,
        __SLID.name() : __SLID,
        __ALID.name() : __ALID,
        __AID.name() : __AID,
        __FLAG.name() : __FLAG
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'associateListDict', associateListDict)


# Complex type photometricParametersParameters with content type ELEMENT_ONLY
class photometricParametersParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photometricParametersParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_photometricParametersParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MinSourceCount uses Python identifier MinSourceCount
    __MinSourceCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinSourceCount'), 'MinSourceCount', '__httpeuclid_esa_orgschemaproext_photometricParametersParameters_httpeuclid_esa_orgschemaproextMinSourceCount', False)

    
    MinSourceCount = property(__MinSourceCount.value, __MinSourceCount.set, None, u' QC: Minimum number of sources used in\n                        zeropoint determination [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_photometricParametersParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SigmaClippingLevel uses Python identifier SigmaClippingLevel
    __SigmaClippingLevel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel'), 'SigmaClippingLevel', '__httpeuclid_esa_orgschemaproext_photometricParametersParameters_httpeuclid_esa_orgschemaproextSigmaClippingLevel', False)

    
    SigmaClippingLevel = property(__SigmaClippingLevel.value, __SigmaClippingLevel.set, None, u' Sigma clipping threshold factor for raw\n                        zeropoints [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxError uses Python identifier MaxError
    __MaxError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxError'), 'MaxError', '__httpeuclid_esa_orgschemaproext_photometricParametersParameters_httpeuclid_esa_orgschemaproextMaxError', False)

    
    MaxError = property(__MaxError.value, __MaxError.set, None, u' QC: Maximum allowable error in the\n                        zeropoint [mag] ')


    _ElementMap = {
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __MinSourceCount.name() : __MinSourceCount,
        __ExtObjectId.name() : __ExtObjectId,
        __SigmaClippingLevel.name() : __SigmaClippingLevel,
        __MaxError.name() : __MaxError
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'photometricParametersParameters', photometricParametersParameters)


# Complex type baseRegriddedFrame with content type ELEMENT_ONLY
class baseRegriddedFrame (CommonDM.dm.bas.img_stub.baseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseRegriddedFrame')
    # Base type is CommonDM.dm.bas.img_stub.baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}GridTarget uses Python identifier GridTarget
    __GridTarget = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GridTarget'), 'GridTarget', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextGridTarget', False)

    
    GridTarget = property(__GridTarget.value, __GridTarget.set, None, u' Grid target for the regridding\n                                operation [None] ')

    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Object uses Python identifier Object
    __Object = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Object'), 'Object', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextObject', False)

    
    Object = property(__Object.value, __Object.set, None, u' Name of target object [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Astrom uses Python identifier Astrom
    __Astrom = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Astrom'), 'Astrom', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextAstrom', False)

    
    Astrom = property(__Astrom.value, __Astrom.set, None, u' Basic information about the\n                                astrometry (linear terms only) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Seeing uses Python identifier Seeing
    __Seeing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), 'Seeing', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextSeeing', False)

    
    Seeing = property(__Seeing.value, __Seeing.set, None, u' Estimate of seeing using the\n                                median FWHM (filtered to isolate most\n                                stellar-like sources) [arcsec] ')

    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}SwarpConf uses Python identifier SwarpConf
    __SwarpConf = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SwarpConf'), 'SwarpConf', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextSwarpConf', False)

    
    SwarpConf = property(__SwarpConf.value, __SwarpConf.set, None, u' SWarp configuration [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Weight uses Python identifier Weight
    __Weight = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Weight'), 'Weight', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextWeight', False)

    
    Weight = property(__Weight.value, __Weight.set, None, u' Information about the detector\n                                pixel weights [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ZeroPoint uses Python identifier ZeroPoint
    __ZeroPoint = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint'), 'ZeroPoint', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextZeroPoint', False)

    
    ZeroPoint = property(__ZeroPoint.value, __ZeroPoint.set, None, u' Value of the photometric\n                                zeropoint [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ZeroPointError uses Python identifier ZeroPointError
    __ZeroPointError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ZeroPointError'), 'ZeroPointError', '__httpeuclid_esa_orgschemaproext_baseRegriddedFrame_httpeuclid_esa_orgschemaproextZeroPointError', False)

    
    ZeroPointError = property(__ZeroPointError.value, __ZeroPointError.set, None, u' Error on the value of the\n                                photometric zeropoint [mag] ')


    _ElementMap = CommonDM.dm.bas.img_stub.baseFrame._ElementMap.copy()
    _ElementMap.update({
        __GridTarget.name() : __GridTarget,
        __Object.name() : __Object,
        __Astrom.name() : __Astrom,
        __Seeing.name() : __Seeing,
        __SwarpConf.name() : __SwarpConf,
        __Weight.name() : __Weight,
        __Filter.name() : __Filter,
        __ZeroPoint.name() : __ZeroPoint,
        __ObsBlock.name() : __ObsBlock,
        __Template.name() : __Template,
        __ZeroPointError.name() : __ZeroPointError
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.baseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'baseRegriddedFrame', baseRegriddedFrame)


# Complex type regriddedFrame with content type ELEMENT_ONLY
class regriddedFrame (baseRegriddedFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'regriddedFrame')
    # Base type is baseRegriddedFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}AstromParams uses Python identifier AstromParams
    __AstromParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AstromParams'), 'AstromParams', '__httpeuclid_esa_orgschemaproext_regriddedFrame_httpeuclid_esa_orgschemaproextAstromParams', False)

    
    AstromParams = property(__AstromParams.value, __AstromParams.set, None, u' Advanced information about the\n                                derived astrometry (with higher-order terms)\n                                [None] ')

    
    # Element Astrom ({http://euclid.esa.org/schema/pro/ext}Astrom) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element ObsBlock ({http://euclid.esa.org/schema/pro/ext}ObsBlock) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_regriddedFrame_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element Filter ({http://euclid.esa.org/schema/pro/ext}Filter) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}DateObs uses Python identifier DateObs
    __DateObs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), 'DateObs', '__httpeuclid_esa_orgschemaproext_regriddedFrame_httpeuclid_esa_orgschemaproextDateObs', False)

    
    DateObs = property(__DateObs.value, __DateObs.set, None, u' UTC date at the start of the\n                                observation [None] ')

    
    # Element Seeing ({http://euclid.esa.org/schema/pro/ext}Seeing) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element GridTarget ({http://euclid.esa.org/schema/pro/ext}GridTarget) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}FluxScale uses Python identifier FluxScale
    __FluxScale = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FluxScale'), 'FluxScale', '__httpeuclid_esa_orgschemaproext_regriddedFrame_httpeuclid_esa_orgschemaproextFluxScale', False)

    
    FluxScale = property(__FluxScale.value, __FluxScale.set, None, u' Derived flux scale\n                                [None]')

    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_regriddedFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Template ({http://euclid.esa.org/schema/pro/ext}Template) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Object ({http://euclid.esa.org/schema/pro/ext}Object) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element SwarpConf ({http://euclid.esa.org/schema/pro/ext}SwarpConf) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element Weight ({http://euclid.esa.org/schema/pro/ext}Weight) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Reduced uses Python identifier Reduced
    __Reduced = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Reduced'), 'Reduced', '__httpeuclid_esa_orgschemaproext_regriddedFrame_httpeuclid_esa_orgschemaproextReduced', False)

    
    Reduced = property(__Reduced.value, __Reduced.set, None, u' Information about the input\n                                reduced science frame [None] ')

    
    # Element ZeroPoint ({http://euclid.esa.org/schema/pro/ext}ZeroPoint) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Gain uses Python identifier Gain
    __Gain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Gain'), 'Gain', '__httpeuclid_esa_orgschemaproext_regriddedFrame_httpeuclid_esa_orgschemaproextGain', False)

    
    Gain = property(__Gain.value, __Gain.set, None, u' Information about the detector\n                                gain [None] ')

    
    # Element ZeroPointError ({http://euclid.esa.org/schema/pro/ext}ZeroPointError) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}PhotomParams uses Python identifier PhotomParams
    __PhotomParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PhotomParams'), 'PhotomParams', '__httpeuclid_esa_orgschemaproext_regriddedFrame_httpeuclid_esa_orgschemaproextPhotomParams', False)

    
    PhotomParams = property(__PhotomParams.value, __PhotomParams.set, None, u' Information about the photometry\n                                [None]')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame

    _ElementMap = baseRegriddedFrame._ElementMap.copy()
    _ElementMap.update({
        __AstromParams.name() : __AstromParams,
        __Chip.name() : __Chip,
        __DateObs.name() : __DateObs,
        __FluxScale.name() : __FluxScale,
        __ProcessParams.name() : __ProcessParams,
        __Reduced.name() : __Reduced,
        __Gain.name() : __Gain,
        __PhotomParams.name() : __PhotomParams
    })
    _AttributeMap = baseRegriddedFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'regriddedFrame', regriddedFrame)


# Complex type photometricParameters with content type ELEMENT_ONLY
class photometricParameters (CommonDM.dm.bas.img_stub.processTargetDataObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photometricParameters')
    # Base type is CommonDM.dm.bas.img_stub.processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Extinction uses Python identifier Extinction
    __Extinction = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Extinction'), 'Extinction', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextExtinction', False)

    
    Extinction = property(__Extinction.value, __Extinction.set, None, u' Information about the atmospheric\n                                extinction [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCount uses Python identifier SourceCount
    __SourceCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), 'SourceCount', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextSourceCount', False)

    
    SourceCount = property(__SourceCount.value, __SourceCount.set, None, u' Number of sources used in\n                                zeropoint determination [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}PhotCat uses Python identifier PhotCat
    __PhotCat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PhotCat'), 'PhotCat', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextPhotCat', False)

    
    PhotCat = property(__PhotCat.value, __PhotCat.set, None, u' Information about the input\n                                photometric sources [None]')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}ZeroPoint uses Python identifier ZeroPoint
    __ZeroPoint = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint'), 'ZeroPoint', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextZeroPoint', False)

    
    ZeroPoint = property(__ZeroPoint.value, __ZeroPoint.set, None, u' Information about the photometric\n                                zeropoint [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}MagId uses Python identifier MagId
    __MagId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagId'), 'MagId', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextMagId', False)

    
    MagId = property(__MagId.value, __MagId.set, None, u' Identifier for the photometric\n                                band [None]')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_photometricParameters_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = CommonDM.dm.bas.img_stub.processTargetDataObject._ElementMap.copy()
    _ElementMap.update({
        __Template.name() : __Template,
        __Instrument.name() : __Instrument,
        __Extinction.name() : __Extinction,
        __TimestampStart.name() : __TimestampStart,
        __SourceCount.name() : __SourceCount,
        __Filter.name() : __Filter,
        __TimestampEnd.name() : __TimestampEnd,
        __PhotCat.name() : __PhotCat,
        __Chip.name() : __Chip,
        __ObsBlock.name() : __ObsBlock,
        __ZeroPoint.name() : __ZeroPoint,
        __MagId.name() : __MagId,
        __ProcessParams.name() : __ProcessParams
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.processTargetDataObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'photometricParameters', photometricParameters)


# Complex type regriddedFrameParameters with content type ELEMENT_ONLY
class regriddedFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'regriddedFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_regriddedFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_regriddedFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumPsfDifference uses Python identifier MaximumPsfDifference
    __MaximumPsfDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumPsfDifference'), 'MaximumPsfDifference', '__httpeuclid_esa_orgschemaproext_regriddedFrameParameters_httpeuclid_esa_orgschemaproextMaximumPsfDifference', False)

    
    MaximumPsfDifference = property(__MaximumPsfDifference.value, __MaximumPsfDifference.set, None, u' QC: Maximum fractional difference between\n                        average psf_radius of input reduced science frame and\n                        the regridded frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}BackgroundSubstractionType uses Python identifier BackgroundSubstractionType
    __BackgroundSubstractionType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BackgroundSubstractionType'), 'BackgroundSubstractionType', '__httpeuclid_esa_orgschemaproext_regriddedFrameParameters_httpeuclid_esa_orgschemaproextBackgroundSubstractionType', False)

    
    BackgroundSubstractionType = property(__BackgroundSubstractionType.value, __BackgroundSubstractionType.set, None, u' Index of the type of background\n                        subtraction [None] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __MaximumPsfDifference.name() : __MaximumPsfDifference,
        __BackgroundSubstractionType.name() : __BackgroundSubstractionType
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'regriddedFrameParameters', regriddedFrameParameters)


# Complex type gainLinearityParameters with content type ELEMENT_ONLY
class gainLinearityParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'gainLinearityParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumGainDifference uses Python identifier MaximumGainDifference
    __MaximumGainDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumGainDifference'), 'MaximumGainDifference', '__httpeuclid_esa_orgschemaproext_gainLinearityParameters_httpeuclid_esa_orgschemaproextMaximumGainDifference', False)

    
    MaximumGainDifference = property(__MaximumGainDifference.value, __MaximumGainDifference.set, None, u' QC: Maximum gain difference relative to\n                        the previous version [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RejectionThreshold uses Python identifier RejectionThreshold
    __RejectionThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold'), 'RejectionThreshold', '__httpeuclid_esa_orgschemaproext_gainLinearityParameters_httpeuclid_esa_orgschemaproextRejectionThreshold', False)

    
    RejectionThreshold = property(__RejectionThreshold.value, __RejectionThreshold.set, None, u' Threshold for rejecting pixels with\n                        outlying values [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MinimumGain uses Python identifier MinimumGain
    __MinimumGain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinimumGain'), 'MinimumGain', '__httpeuclid_esa_orgschemaproext_gainLinearityParameters_httpeuclid_esa_orgschemaproextMinimumGain', False)

    
    MinimumGain = property(__MinimumGain.value, __MinimumGain.set, None, u' QC: Minimum gain [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_gainLinearityParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumIterations uses Python identifier MaximumIterations
    __MaximumIterations = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations'), 'MaximumIterations', '__httpeuclid_esa_orgschemaproext_gainLinearityParameters_httpeuclid_esa_orgschemaproextMaximumIterations', False)

    
    MaximumIterations = property(__MaximumIterations.value, __MaximumIterations.set, None, u' Maximum number of iterations for\n                        estimating statistics [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximimGain uses Python identifier MaximimGain
    __MaximimGain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximimGain'), 'MaximimGain', '__httpeuclid_esa_orgschemaproext_gainLinearityParameters_httpeuclid_esa_orgschemaproextMaximimGain', False)

    
    MaximimGain = property(__MaximimGain.value, __MaximimGain.set, None, u' QC: Maximum gain [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}OverscanCorrection uses Python identifier OverscanCorrection
    __OverscanCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), 'OverscanCorrection', '__httpeuclid_esa_orgschemaproext_gainLinearityParameters_httpeuclid_esa_orgschemaproextOverscanCorrection', False)

    
    OverscanCorrection = property(__OverscanCorrection.value, __OverscanCorrection.set, None, u' Overscan correction method index [None] ')


    _ElementMap = {
        __MaximumGainDifference.name() : __MaximumGainDifference,
        __RejectionThreshold.name() : __RejectionThreshold,
        __MinimumGain.name() : __MinimumGain,
        __ExtObjectId.name() : __ExtObjectId,
        __MaximumIterations.name() : __MaximumIterations,
        __MaximimGain.name() : __MaximimGain,
        __OverscanCorrection.name() : __OverscanCorrection
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'gainLinearityParameters', gainLinearityParameters)


# Complex type catalog with content type ELEMENT_ONLY
class catalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ZeroPoint uses Python identifier ZeroPoint
    __ZeroPoint = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint'), 'ZeroPoint', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextZeroPoint', False)

    
    ZeroPoint = property(__ZeroPoint.value, __ZeroPoint.set, None, u' Value of the photometric zeropoint [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SexConfig uses Python identifier SexConfig
    __SexConfig = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), 'SexConfig', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextSexConfig', False)

    
    SexConfig = property(__SexConfig.value, __SexConfig.set, None, u' SExtractor configuration for source\n                        extraction [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Weight uses Python identifier Weight
    __Weight = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Weight'), 'Weight', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextWeight', False)

    
    Weight = property(__Weight.value, __Weight.set, None, u' Information about the detector pixel\n                        weights [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Threshold uses Python identifier Threshold
    __Threshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Threshold'), 'Threshold', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextThreshold', False)

    
    Threshold = property(__Threshold.value, __Threshold.set, None, u' SExtractor detection threshold [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Frame uses Python identifier Frame
    __Frame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Frame'), 'Frame', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextFrame', False)

    
    Frame = property(__Frame.value, __Frame.set, None, u' Information about the input frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Storage uses Python identifier Storage
    __Storage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Storage'), 'Storage', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextStorage', False)

    
    Storage = property(__Storage.value, __Storage.set, None, u' Customized storage container for the data\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Seeing uses Python identifier Seeing
    __Seeing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), 'Seeing', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextSeeing', False)

    
    Seeing = property(__Seeing.value, __Seeing.set, None, u' Estimate of seeing using the median FWHM\n                        (filtered to isolate most stellar-like sources) [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCount uses Python identifier SourceCount
    __SourceCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), 'SourceCount', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextSourceCount', False)

    
    SourceCount = property(__SourceCount.value, __SourceCount.set, None, u' Number of extracted sources [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SexParam uses Python identifier SexParam
    __SexParam = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexParam'), 'SexParam', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextSexParam', True)

    
    SexParam = property(__SexParam.value, __SexParam.set, None, u' List of parameters derived for each\n                        extracted source [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}WeightScale uses Python identifier WeightScale
    __WeightScale = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WeightScale'), 'WeightScale', '__httpeuclid_esa_orgschemaproext_catalog_httpeuclid_esa_orgschemaproextWeightScale', False)

    
    WeightScale = property(__WeightScale.value, __WeightScale.set, None, u' Weight scale [None] ')


    _ElementMap = {
        __ZeroPoint.name() : __ZeroPoint,
        __ExtObjectId.name() : __ExtObjectId,
        __SexConfig.name() : __SexConfig,
        __Weight.name() : __Weight,
        __Threshold.name() : __Threshold,
        __Frame.name() : __Frame,
        __Storage.name() : __Storage,
        __Seeing.name() : __Seeing,
        __SourceCount.name() : __SourceCount,
        __SexParam.name() : __SexParam,
        __WeightScale.name() : __WeightScale
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalog', catalog)


# Complex type photSrcCatalog with content type ELEMENT_ONLY
class photSrcCatalog (catalog):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photSrcCatalog')
    # Base type is catalog
    
    # Element ZeroPoint ({http://euclid.esa.org/schema/pro/ext}ZeroPoint) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element Threshold ({http://euclid.esa.org/schema/pro/ext}Threshold) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element SourceCount ({http://euclid.esa.org/schema/pro/ext}SourceCount) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/pro/ext}ExtObjectId) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element WeightScale ({http://euclid.esa.org/schema/pro/ext}WeightScale) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element SexConfig ({http://euclid.esa.org/schema/pro/ext}SexConfig) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}IsValid uses Python identifier IsValid
    __IsValid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IsValid'), 'IsValid', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextIsValid', False)

    
    IsValid = property(__IsValid.value, __IsValid.set, None, u' Manual/external flag to\n                                disqualify bad data (SuperFlag) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PhotSourceList uses Python identifier PhotSourceList
    __PhotSourceList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PhotSourceList'), 'PhotSourceList', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextPhotSourceList', True)

    
    PhotSourceList = property(__PhotSourceList.value, __PhotSourceList.set, None, u' List of input photometric sources\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element SexParam ({http://euclid.esa.org/schema/pro/ext}SexParam) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element {http://euclid.esa.org/schema/pro/ext}MagId uses Python identifier MagId
    __MagId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagId'), 'MagId', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextMagId', False)

    
    MagId = property(__MagId.value, __MagId.set, None, u' Identifier for the photometric\n                                band [None]')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DateObs uses Python identifier DateObs
    __DateObs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), 'DateObs', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextDateObs', False)

    
    DateObs = property(__DateObs.value, __DateObs.set, None, u' UTC date at the start of the\n                                observation [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/pro/ext}Storage) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element {http://euclid.esa.org/schema/pro/ext}Airmass uses Python identifier Airmass
    __Airmass = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Airmass'), 'Airmass', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextAirmass', False)

    
    Airmass = property(__Airmass.value, __Airmass.set, None, u' Average airmass of the\n                                observation [None] ')

    
    # Element Frame ({http://euclid.esa.org/schema/pro/ext}Frame) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element {http://euclid.esa.org/schema/pro/ext}Refcat uses Python identifier Refcat
    __Refcat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Refcat'), 'Refcat', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextRefcat', False)

    
    Refcat = property(__Refcat.value, __Refcat.set, None, u' Information about the photometric\n                                reference catalog [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), 'CreationDate', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextCreationDate', False)

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, u' UTC date this object was created\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Transform uses Python identifier Transform
    __Transform = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Transform'), 'Transform', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextTransform', False)

    
    Transform = property(__Transform.value, __Transform.set, None, u' Information about the photometric\n                                transformation between bands [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SkyBackground uses Python identifier SkyBackground
    __SkyBackground = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SkyBackground'), 'SkyBackground', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextSkyBackground', False)

    
    SkyBackground = property(__SkyBackground.value, __SkyBackground.set, None, u' Median flux value of the detector\n                                pixel values [count / sec / arcsec**2] ')

    
    # Element Seeing ({http://euclid.esa.org/schema/pro/ext}Seeing) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element Weight ({http://euclid.esa.org/schema/pro/ext}Weight) inherited from {http://euclid.esa.org/schema/pro/ext}catalog
    
    # Element {http://euclid.esa.org/schema/pro/ext}AstromParams uses Python identifier AstromParams
    __AstromParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AstromParams'), 'AstromParams', '__httpeuclid_esa_orgschemaproext_photSrcCatalog_httpeuclid_esa_orgschemaproextAstromParams', False)

    
    AstromParams = property(__AstromParams.value, __AstromParams.set, None, u' Advanced information about the\n                                derived astrometry (with higher-order terms)\n                                [None] ')


    _ElementMap = catalog._ElementMap.copy()
    _ElementMap.update({
        __ObsBlock.name() : __ObsBlock,
        __Template.name() : __Template,
        __Instrument.name() : __Instrument,
        __Filter.name() : __Filter,
        __IsValid.name() : __IsValid,
        __PhotSourceList.name() : __PhotSourceList,
        __Chip.name() : __Chip,
        __MagId.name() : __MagId,
        __DateObs.name() : __DateObs,
        __Airmass.name() : __Airmass,
        __Refcat.name() : __Refcat,
        __CreationDate.name() : __CreationDate,
        __ProcessParams.name() : __ProcessParams,
        __Transform.name() : __Transform,
        __SkyBackground.name() : __SkyBackground,
        __AstromParams.name() : __AstromParams
    })
    _AttributeMap = catalog._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'photSrcCatalog', photSrcCatalog)


# Complex type rawFits with content type ELEMENT_ONLY
class rawFits (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawFits')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}Object uses Python identifier Object
    __Object = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Object'), 'Object', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextObject', False)

    
    Object = property(__Object.value, __Object.set, None, u' Name of target object [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Lst uses Python identifier Lst
    __Lst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Lst'), 'Lst', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextLst', False)

    
    Lst = property(__Lst.value, __Lst.set, None, u' Local sidereal time at the start of the\n                        observation expressed as the number of seconds (a float)\n                        since UTC midnight [sec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Observer uses Python identifier Observer
    __Observer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Observer'), 'Observer', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextObserver', False)

    
    Observer = property(__Observer.value, __Observer.set, None, u' Information about the observer [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Utc uses Python identifier Utc
    __Utc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Utc'), 'Utc', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextUtc', False)

    
    Utc = property(__Utc.value, __Utc.set, None, u' Universal coordinated time at the start\n                        of the observation expressed as the number of seconds (a\n                        float) since UTC midnight [sec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the observational block\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DateObs uses Python identifier DateObs
    __DateObs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), 'DateObs', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextDateObs', False)

    
    DateObs = property(__DateObs.value, __DateObs.set, None, u' UTC date at the start of the observation\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Date uses Python identifier Date
    __Date = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Date'), 'Date', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextDate', False)

    
    Date = property(__Date.value, __Date.set, None, u' UTC date the original data file was saved\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                        instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExpTime uses Python identifier ExpTime
    __ExpTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), 'ExpTime', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextExpTime', False)

    
    ExpTime = property(__ExpTime.value, __ExpTime.set, None, u' Total time of an individual exposure\n                        [sec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}OrigFilename uses Python identifier OrigFilename
    __OrigFilename = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OrigFilename'), 'OrigFilename', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextOrigFilename', False)

    
    OrigFilename = property(__OrigFilename.value, __OrigFilename.set, None, u' Archive file name [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Storage uses Python identifier Storage
    __Storage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Storage'), 'Storage', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextStorage', False)

    
    Storage = property(__Storage.value, __Storage.set, None, u' Customized storage container for the data\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MjdObs uses Python identifier MjdObs
    __MjdObs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MjdObs'), 'MjdObs', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextMjdObs', False)

    
    MjdObs = property(__MjdObs.value, __MjdObs.set, None, u' Modified Julian date at the start of the\n                        observation (JD-2400000.5) [day] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the observational\n                        filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_rawFits_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the observational\n                        template [None] ')


    _ElementMap = {
        __Object.name() : __Object,
        __Lst.name() : __Lst,
        __Observer.name() : __Observer,
        __Utc.name() : __Utc,
        __ObsBlock.name() : __ObsBlock,
        __DateObs.name() : __DateObs,
        __Date.name() : __Date,
        __ExtObjectId.name() : __ExtObjectId,
        __Instrument.name() : __Instrument,
        __ExpTime.name() : __ExpTime,
        __OrigFilename.name() : __OrigFilename,
        __Storage.name() : __Storage,
        __MjdObs.name() : __MjdObs,
        __Filter.name() : __Filter,
        __Template.name() : __Template
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'rawFits', rawFits)


# Complex type rawTwilightFlatFrame with content type ELEMENT_ONLY
class rawTwilightFlatFrame (rawFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawTwilightFlatFrame')
    # Base type is rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_rawTwilightFlatFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element ObsBlock ({http://euclid.esa.org/schema/pro/ext}ObsBlock) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Ovscy ({http://euclid.esa.org/schema/pro/ext}Ovscy) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscypst ({http://euclid.esa.org/schema/pro/ext}Ovscypst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Template ({http://euclid.esa.org/schema/pro/ext}Template) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExpTime uses Python identifier ExpTime
    __ExpTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), 'ExpTime', '__httpeuclid_esa_orgschemaproext_rawTwilightFlatFrame_httpeuclid_esa_orgschemaproextExpTime', False)

    
    ExpTime = property(__ExpTime.value, __ExpTime.set, None, u' Total time of an individual\n                                exposure [sec] ')

    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscxpre ({http://euclid.esa.org/schema/pro/ext}Prscxpre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element OverscanYStat ({http://euclid.esa.org/schema/pro/ext}OverscanYStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_rawTwilightFlatFrame_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscypre ({http://euclid.esa.org/schema/pro/ext}Prscypre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Date ({http://euclid.esa.org/schema/pro/ext}Date) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Object ({http://euclid.esa.org/schema/pro/ext}Object) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscxpre ({http://euclid.esa.org/schema/pro/ext}Ovscxpre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element DateObs ({http://euclid.esa.org/schema/pro/ext}DateObs) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscypre ({http://euclid.esa.org/schema/pro/ext}Ovscypre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element MjdObs ({http://euclid.esa.org/schema/pro/ext}MjdObs) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Extension ({http://euclid.esa.org/schema/pro/ext}Extension) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscxpst ({http://euclid.esa.org/schema/pro/ext}Prscxpst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Lst ({http://euclid.esa.org/schema/pro/ext}Lst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element RawFits ({http://euclid.esa.org/schema/pro/ext}RawFits) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element PrescanXStat ({http://euclid.esa.org/schema/pro/ext}PrescanXStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element PrescanYStat ({http://euclid.esa.org/schema/pro/ext}PrescanYStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Utc ({http://euclid.esa.org/schema/pro/ext}Utc) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscxpst ({http://euclid.esa.org/schema/pro/ext}Ovscxpst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscx ({http://euclid.esa.org/schema/pro/ext}Prscx) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element OverscanXStat ({http://euclid.esa.org/schema/pro/ext}OverscanXStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Chip ({http://euclid.esa.org/schema/pro/ext}Chip) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscy ({http://euclid.esa.org/schema/pro/ext}Prscy) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Observer ({http://euclid.esa.org/schema/pro/ext}Observer) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscx ({http://euclid.esa.org/schema/pro/ext}Ovscx) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscypst ({http://euclid.esa.org/schema/pro/ext}Prscypst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame

    _ElementMap = rawFrame._ElementMap.copy()
    _ElementMap.update({
        __ProcessParams.name() : __ProcessParams,
        __ExpTime.name() : __ExpTime,
        __Filter.name() : __Filter
    })
    _AttributeMap = rawFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'rawTwilightFlatFrame', rawTwilightFlatFrame)


# Complex type photExtinctionPoint with content type ELEMENT_ONLY
class photExtinctionPoint (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photExtinctionPoint')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}Extinction uses Python identifier Extinction
    __Extinction = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Extinction'), 'Extinction', '__httpeuclid_esa_orgschemaproext_photExtinctionPoint_httpeuclid_esa_orgschemaproextExtinction', False)

    
    Extinction = property(__Extinction.value, __Extinction.set, None, u' Atmospheric extinction [mag / airmass] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), 'Wavelength', '__httpeuclid_esa_orgschemaproext_photExtinctionPoint_httpeuclid_esa_orgschemaproextWavelength', False)

    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, u' Wavelength [angstrom] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_photExtinctionPoint_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __Extinction.name() : __Extinction,
        __Wavelength.name() : __Wavelength,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'photExtinctionPoint', photExtinctionPoint)


# Complex type twilightFlatFrameParameters with content type ELEMENT_ONLY
class twilightFlatFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'twilightFlatFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumNumberOfOutliers uses Python identifier MaximumNumberOfOutliers
    __MaximumNumberOfOutliers = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumNumberOfOutliers'), 'MaximumNumberOfOutliers', '__httpeuclid_esa_orgschemaproext_twilightFlatFrameParameters_httpeuclid_esa_orgschemaproextMaximumNumberOfOutliers', False)

    
    MaximumNumberOfOutliers = property(__MaximumNumberOfOutliers.value, __MaximumNumberOfOutliers.set, None, u' QC: Maximum number of outliers [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_twilightFlatFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumSubwinFlatness uses Python identifier MaximumSubwinFlatness
    __MaximumSubwinFlatness = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness'), 'MaximumSubwinFlatness', '__httpeuclid_esa_orgschemaproext_twilightFlatFrameParameters_httpeuclid_esa_orgschemaproextMaximumSubwinFlatness', False)

    
    MaximumSubwinFlatness = property(__MaximumSubwinFlatness.value, __MaximumSubwinFlatness.set, None, u' QC: Maximum difference between median\n                        values of any two sub-windows [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_twilightFlatFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}OverscanCorrection uses Python identifier OverscanCorrection
    __OverscanCorrection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), 'OverscanCorrection', '__httpeuclid_esa_orgschemaproext_twilightFlatFrameParameters_httpeuclid_esa_orgschemaproextOverscanCorrection', False)

    
    OverscanCorrection = property(__OverscanCorrection.value, __OverscanCorrection.set, None, u' Overscan correction method index [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumSubwinDiff uses Python identifier MaximumSubwinDiff
    __MaximumSubwinDiff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinDiff'), 'MaximumSubwinDiff', '__httpeuclid_esa_orgschemaproext_twilightFlatFrameParameters_httpeuclid_esa_orgschemaproextMaximumSubwinDiff', False)

    
    MaximumSubwinDiff = property(__MaximumSubwinDiff.value, __MaximumSubwinDiff.set, None, u' QC: Difference in MaximumSubwinFlatness\n                        relative to the previous version [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SigmaClip uses Python identifier SigmaClip
    __SigmaClip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip'), 'SigmaClip', '__httpeuclid_esa_orgschemaproext_twilightFlatFrameParameters_httpeuclid_esa_orgschemaproextSigmaClip', False)

    
    SigmaClip = property(__SigmaClip.value, __SigmaClip.set, None, u' Threshold factor for rejecting raw\n                        twilight flat pixel value outliers (sigma is taken as\n                        the scaled gain measurement) [None] ')


    _ElementMap = {
        __MaximumNumberOfOutliers.name() : __MaximumNumberOfOutliers,
        __ExtObjectId.name() : __ExtObjectId,
        __MaximumSubwinFlatness.name() : __MaximumSubwinFlatness,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __OverscanCorrection.name() : __OverscanCorrection,
        __MaximumSubwinDiff.name() : __MaximumSubwinDiff,
        __SigmaClip.name() : __SigmaClip
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'twilightFlatFrameParameters', twilightFlatFrameParameters)


# Complex type coaddedRegriddedFrameParameters with content type ELEMENT_ONLY
class coaddedRegriddedFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coaddedRegriddedFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_coaddedRegriddedFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumPSFDifference uses Python identifier MaximumPSFDifference
    __MaximumPSFDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumPSFDifference'), 'MaximumPSFDifference', '__httpeuclid_esa_orgschemaproext_coaddedRegriddedFrameParameters_httpeuclid_esa_orgschemaproextMaximumPSFDifference', False)

    
    MaximumPSFDifference = property(__MaximumPSFDifference.value, __MaximumPSFDifference.set, None, u' QC: Maximum fractional difference between\n                        average psf_radius of input regridded frames and the\n                        coadded regridded frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_coaddedRegriddedFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __MaximumPSFDifference.name() : __MaximumPSFDifference,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'coaddedRegriddedFrameParameters', coaddedRegriddedFrameParameters)


# Complex type astrometricParametersParameters with content type ELEMENT_ONLY
class astrometricParametersParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'astrometricParametersParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxSigmaOverlap uses Python identifier MaxSigmaOverlap
    __MaxSigmaOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxSigmaOverlap'), 'MaxSigmaOverlap', '__httpeuclid_esa_orgschemaproext_astrometricParametersParameters_httpeuclid_esa_orgschemaproextMaxSigmaOverlap', False)

    
    MaxSigmaOverlap = property(__MaxSigmaOverlap.value, __MaxSigmaOverlap.set, None, u' QC: Maximum value of SigmaDraOverlap or\n                        SigmaDdecOverlap [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxNref uses Python identifier MaxNref
    __MaxNref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxNref'), 'MaxNref', '__httpeuclid_esa_orgschemaproext_astrometricParametersParameters_httpeuclid_esa_orgschemaproextMaxNref', False)

    
    MaxNref = property(__MaxNref.value, __MaxNref.set, None, u' QC: Maximum number of reference pairings\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MinNOverlap uses Python identifier MinNOverlap
    __MinNOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinNOverlap'), 'MinNOverlap', '__httpeuclid_esa_orgschemaproext_astrometricParametersParameters_httpeuclid_esa_orgschemaproextMinNOverlap', False)

    
    MinNOverlap = property(__MinNOverlap.value, __MinNOverlap.set, None, u' QC: Minimum number of overlap pairings\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxRmsOverlap uses Python identifier MaxRmsOverlap
    __MaxRmsOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxRmsOverlap'), 'MaxRmsOverlap', '__httpeuclid_esa_orgschemaproext_astrometricParametersParameters_httpeuclid_esa_orgschemaproextMaxRmsOverlap', False)

    
    MaxRmsOverlap = property(__MaxRmsOverlap.value, __MaxRmsOverlap.set, None, u' QC: Maximum (internal) RMS of overlap\n                        residuals [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_astrometricParametersParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxSigma uses Python identifier MaxSigma
    __MaxSigma = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxSigma'), 'MaxSigma', '__httpeuclid_esa_orgschemaproext_astrometricParametersParameters_httpeuclid_esa_orgschemaproextMaxSigma', False)

    
    MaxSigma = property(__MaxSigma.value, __MaxSigma.set, None, u' QC: Maximum value of SigmaDra or\n                        SigmaDdec [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxNOverlap uses Python identifier MaxNOverlap
    __MaxNOverlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxNOverlap'), 'MaxNOverlap', '__httpeuclid_esa_orgschemaproext_astrometricParametersParameters_httpeuclid_esa_orgschemaproextMaxNOverlap', False)

    
    MaxNOverlap = property(__MaxNOverlap.value, __MaxNOverlap.set, None, u' QC: Maximum number of overlap pairings\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_astrometricParametersParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MinNref uses Python identifier MinNref
    __MinNref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinNref'), 'MinNref', '__httpeuclid_esa_orgschemaproext_astrometricParametersParameters_httpeuclid_esa_orgschemaproextMinNref', False)

    
    MinNref = property(__MinNref.value, __MinNref.set, None, u' QC: Minimum number of reference pairings\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxRms uses Python identifier MaxRms
    __MaxRms = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxRms'), 'MaxRms', '__httpeuclid_esa_orgschemaproext_astrometricParametersParameters_httpeuclid_esa_orgschemaproextMaxRms', False)

    
    MaxRms = property(__MaxRms.value, __MaxRms.set, None, u' QC: Maximum (external) RMS of reference\n                        residuals [arcsec] ')


    _ElementMap = {
        __MaxSigmaOverlap.name() : __MaxSigmaOverlap,
        __MaxNref.name() : __MaxNref,
        __MinNOverlap.name() : __MinNOverlap,
        __MaxRmsOverlap.name() : __MaxRmsOverlap,
        __ExtObjectId.name() : __ExtObjectId,
        __MaxSigma.name() : __MaxSigma,
        __MaxNOverlap.name() : __MaxNOverlap,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __MinNref.name() : __MinNref,
        __MaxRms.name() : __MaxRms
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'astrometricParametersParameters', astrometricParametersParameters)


# Complex type illuminationCorrection with content type ELEMENT_ONLY
class illuminationCorrection (CommonDM.dm.bas.img_stub.processTargetDataObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminationCorrection')
    # Base type is CommonDM.dm.bas.img_stub.processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxY uses Python identifier MaxY
    __MaxY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxY'), 'MaxY', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextMaxY', False)

    
    MaxY = property(__MaxY.value, __MaxY.set, None, u' Y coordinate of the source with\n                                the highest Y position [pixel] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxX uses Python identifier MaxX
    __MaxX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxX'), 'MaxX', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextMaxX', False)

    
    MaxX = property(__MaxX.value, __MaxX.set, None, u' X coordinate of the source with\n                                the highest X position [pixel] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FitCoeffs uses Python identifier FitCoeffs
    __FitCoeffs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FitCoeffs'), 'FitCoeffs', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextFitCoeffs', True)

    
    FitCoeffs = property(__FitCoeffs.value, __FitCoeffs.set, None, u' List of fit coefficients [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MinY uses Python identifier MinY
    __MinY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinY'), 'MinY', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextMinY', False)

    
    MinY = property(__MinY.value, __MinY.set, None, u' Y coordinate of the source with\n                                the lowest Y position [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MagId uses Python identifier MagId
    __MagId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagId'), 'MagId', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextMagId', False)

    
    MagId = property(__MagId.value, __MagId.set, None, u' Identifier for the photometric\n                                band [None]')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PhotCats uses Python identifier PhotCats
    __PhotCats = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PhotCats'), 'PhotCats', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextPhotCats', True)

    
    PhotCats = property(__PhotCats.value, __PhotCats.set, None, u' List of input photometric source\n                                catalogs [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MinX uses Python identifier MinX
    __MinX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinX'), 'MinX', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextMinX', False)

    
    MinX = property(__MinX.value, __MinX.set, None, u' X coordinate of the source with\n                                the lowest X position [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Records uses Python identifier Records
    __Records = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Records'), 'Records', '__httpeuclid_esa_orgschemaproext_illuminationCorrection_httpeuclid_esa_orgschemaproextRecords', True)

    
    Records = property(__Records.value, __Records.set, None, u' List of illumination correction\n                                records [None] ')


    _ElementMap = CommonDM.dm.bas.img_stub.processTargetDataObject._ElementMap.copy()
    _ElementMap.update({
        __TimestampStart.name() : __TimestampStart,
        __MaxY.name() : __MaxY,
        __MaxX.name() : __MaxX,
        __TimestampEnd.name() : __TimestampEnd,
        __FitCoeffs.name() : __FitCoeffs,
        __ProcessParams.name() : __ProcessParams,
        __MinY.name() : __MinY,
        __Filter.name() : __Filter,
        __MagId.name() : __MagId,
        __PhotCats.name() : __PhotCats,
        __Instrument.name() : __Instrument,
        __MinX.name() : __MinX,
        __Records.name() : __Records
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.processTargetDataObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'illuminationCorrection', illuminationCorrection)


# Complex type fringeFrame with content type ELEMENT_ONLY
class fringeFrame (CommonDM.dm.bas.img_stub.baseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fringeFrame')
    # Base type is CommonDM.dm.bas.img_stub.baseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_fringeFrame_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RawScienceFrames uses Python identifier RawScienceFrames
    __RawScienceFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawScienceFrames'), 'RawScienceFrames', '__httpeuclid_esa_orgschemaproext_fringeFrame_httpeuclid_esa_orgschemaproextRawScienceFrames', True)

    
    RawScienceFrames = property(__RawScienceFrames.value, __RawScienceFrames.set, None, u' List of input raw science frames\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Bias uses Python identifier Bias
    __Bias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Bias'), 'Bias', '__httpeuclid_esa_orgschemaproext_fringeFrame_httpeuclid_esa_orgschemaproextBias', False)

    
    Bias = property(__Bias.value, __Bias.set, None, u' Information about the detector\n                                bias offset levels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Hot uses Python identifier Hot
    __Hot = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Hot'), 'Hot', '__httpeuclid_esa_orgschemaproext_fringeFrame_httpeuclid_esa_orgschemaproextHot', False)

    
    Hot = property(__Hot.value, __Hot.set, None, u' Information about the detector\n                                hot pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Cold uses Python identifier Cold
    __Cold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cold'), 'Cold', '__httpeuclid_esa_orgschemaproext_fringeFrame_httpeuclid_esa_orgschemaproextCold', False)

    
    Cold = property(__Cold.value, __Cold.set, None, u' Information about the detector\n                                cold pixels [None] ')

    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_fringeFrame_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_fringeFrame_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Flat uses Python identifier Flat
    __Flat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flat'), 'Flat', '__httpeuclid_esa_orgschemaproext_fringeFrame_httpeuclid_esa_orgschemaproextFlat', False)

    
    Flat = property(__Flat.value, __Flat.set, None, u' Information about the detector\n                                sensitivity variations [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_fringeFrame_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_fringeFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')


    _ElementMap = CommonDM.dm.bas.img_stub.baseFrame._ElementMap.copy()
    _ElementMap.update({
        __Filter.name() : __Filter,
        __RawScienceFrames.name() : __RawScienceFrames,
        __Bias.name() : __Bias,
        __Hot.name() : __Hot,
        __Cold.name() : __Cold,
        __TimestampStart.name() : __TimestampStart,
        __Chip.name() : __Chip,
        __Flat.name() : __Flat,
        __TimestampEnd.name() : __TimestampEnd,
        __ProcessParams.name() : __ProcessParams
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.baseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'fringeFrame', fringeFrame)


# Complex type reducedScienceFrame with content type ELEMENT_ONLY
class reducedScienceFrame (CommonDM.dm.bas.img_stub.baseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reducedScienceFrame')
    # Base type is CommonDM.dm.bas.img_stub.baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}AirmassEnd uses Python identifier AirmassEnd
    __AirmassEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AirmassEnd'), 'AirmassEnd', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextAirmassEnd', False)

    
    AirmassEnd = property(__AirmassEnd.value, __AirmassEnd.set, None, u' Airmass at the ending of the\n                                observation [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Weight uses Python identifier Weight
    __Weight = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Weight'), 'Weight', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextWeight', False)

    
    Weight = property(__Weight.value, __Weight.set, None, u' Information about the detector\n                                pixel weights [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Seeing uses Python identifier Seeing
    __Seeing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), 'Seeing', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextSeeing', False)

    
    Seeing = property(__Seeing.value, __Seeing.set, None, u' Estimate of seeing using the\n                                median FWHM (filtered to isolate most\n                                stellar-like sources) [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ScaleFactor uses Python identifier ScaleFactor
    __ScaleFactor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ScaleFactor'), 'ScaleFactor', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextScaleFactor', False)

    
    ScaleFactor = property(__ScaleFactor.value, __ScaleFactor.set, None, u' Detector fringe pattern scaling\n                                factor [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Raw uses Python identifier Raw
    __Raw = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Raw'), 'Raw', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextRaw', False)

    
    Raw = property(__Raw.value, __Raw.set, None, u' Information about the input raw\n                                science frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Astrom uses Python identifier Astrom
    __Astrom = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Astrom'), 'Astrom', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextAstrom', False)

    
    Astrom = property(__Astrom.value, __Astrom.set, None, u' Basic information about the\n                                astrometry (linear terms only) [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Bias uses Python identifier Bias
    __Bias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Bias'), 'Bias', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextBias', False)

    
    Bias = property(__Bias.value, __Bias.set, None, u' Information about the detector\n                                bias offset levels [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExpTime uses Python identifier ExpTime
    __ExpTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), 'ExpTime', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextExpTime', False)

    
    ExpTime = property(__ExpTime.value, __ExpTime.set, None, u' Total time of an individual\n                                exposure [sec] ')

    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Flat uses Python identifier Flat
    __Flat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flat'), 'Flat', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextFlat', False)

    
    Flat = property(__Flat.value, __Flat.set, None, u' Information about the detector\n                                sensitivity variations [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Object uses Python identifier Object
    __Object = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Object'), 'Object', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextObject', False)

    
    Object = property(__Object.value, __Object.set, None, u' Name of target object [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Hot uses Python identifier Hot
    __Hot = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Hot'), 'Hot', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextHot', False)

    
    Hot = property(__Hot.value, __Hot.set, None, u' Information about the detector\n                                hot pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Date uses Python identifier Date
    __Date = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Date'), 'Date', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextDate', False)

    
    Date = property(__Date.value, __Date.set, None, u' UTC date the original data file\n                                was saved [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Cold uses Python identifier Cold
    __Cold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cold'), 'Cold', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextCold', False)

    
    Cold = property(__Cold.value, __Cold.set, None, u' Information about the detector\n                                cold pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DateObs uses Python identifier DateObs
    __DateObs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), 'DateObs', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextDateObs', False)

    
    DateObs = property(__DateObs.value, __DateObs.set, None, u' UTC date at the start of the\n                                observation [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Fringe uses Python identifier Fringe
    __Fringe = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Fringe'), 'Fringe', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextFringe', False)

    
    Fringe = property(__Fringe.value, __Fringe.set, None, u' Information about the detector\n                                fringe pattern [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}AirmassStart uses Python identifier AirmassStart
    __AirmassStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AirmassStart'), 'AirmassStart', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextAirmassStart', False)

    
    AirmassStart = property(__AirmassStart.value, __AirmassStart.set, None, u' Airmass at the beginning of the\n                                observation [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}Illumination uses Python identifier Illumination
    __Illumination = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), 'Illumination', '__httpeuclid_esa_orgschemaproext_reducedScienceFrame_httpeuclid_esa_orgschemaproextIllumination', False)

    
    Illumination = property(__Illumination.value, __Illumination.set, None, u' Information about the\n                                illumination correction\n                                [None]')

    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame

    _ElementMap = CommonDM.dm.bas.img_stub.baseFrame._ElementMap.copy()
    _ElementMap.update({
        __AirmassEnd.name() : __AirmassEnd,
        __Weight.name() : __Weight,
        __Seeing.name() : __Seeing,
        __Template.name() : __Template,
        __ScaleFactor.name() : __ScaleFactor,
        __Raw.name() : __Raw,
        __ObsBlock.name() : __ObsBlock,
        __Filter.name() : __Filter,
        __Astrom.name() : __Astrom,
        __ProcessParams.name() : __ProcessParams,
        __Bias.name() : __Bias,
        __ExpTime.name() : __ExpTime,
        __Flat.name() : __Flat,
        __Object.name() : __Object,
        __Hot.name() : __Hot,
        __Date.name() : __Date,
        __Cold.name() : __Cold,
        __DateObs.name() : __DateObs,
        __Fringe.name() : __Fringe,
        __AirmassStart.name() : __AirmassStart,
        __Illumination.name() : __Illumination
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.baseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'reducedScienceFrame', reducedScienceFrame)


# Complex type coldPixelMapParameters with content type ELEMENT_ONLY
class coldPixelMapParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coldPixelMapParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_coldPixelMapParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumColdPixelCount uses Python identifier MaximumColdPixelCount
    __MaximumColdPixelCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumColdPixelCount'), 'MaximumColdPixelCount', '__httpeuclid_esa_orgschemaproext_coldPixelMapParameters_httpeuclid_esa_orgschemaproextMaximumColdPixelCount', False)

    
    MaximumColdPixelCount = property(__MaximumColdPixelCount.value, __MaximumColdPixelCount.set, None, u' QC: Maximum number of hot pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ThresholdLow uses Python identifier ThresholdLow
    __ThresholdLow = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ThresholdLow'), 'ThresholdLow', '__httpeuclid_esa_orgschemaproext_coldPixelMapParameters_httpeuclid_esa_orgschemaproextThresholdLow', False)

    
    ThresholdLow = property(__ThresholdLow.value, __ThresholdLow.set, None, u' Lower threshold for rejecting pixels with\n                        outlying values [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumColdPixelCountDifference uses Python identifier MaximumColdPixelCountDifference
    __MaximumColdPixelCountDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumColdPixelCountDifference'), 'MaximumColdPixelCountDifference', '__httpeuclid_esa_orgschemaproext_coldPixelMapParameters_httpeuclid_esa_orgschemaproextMaximumColdPixelCountDifference', False)

    
    MaximumColdPixelCountDifference = property(__MaximumColdPixelCountDifference.value, __MaximumColdPixelCountDifference.set, None, u' QC: Maximum number of new cold pixels\n                        relative to the previous version [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ThresholdHigh uses Python identifier ThresholdHigh
    __ThresholdHigh = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ThresholdHigh'), 'ThresholdHigh', '__httpeuclid_esa_orgschemaproext_coldPixelMapParameters_httpeuclid_esa_orgschemaproextThresholdHigh', False)

    
    ThresholdHigh = property(__ThresholdHigh.value, __ThresholdHigh.set, None, u' Upper threshold for rejecting pixels with\n                        outlying values [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_coldPixelMapParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __MaximumColdPixelCount.name() : __MaximumColdPixelCount,
        __ThresholdLow.name() : __ThresholdLow,
        __MaximumColdPixelCountDifference.name() : __MaximumColdPixelCountDifference,
        __ThresholdHigh.name() : __ThresholdHigh,
        __SourceCodeVersion.name() : __SourceCodeVersion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'coldPixelMapParameters', coldPixelMapParameters)


# Complex type satelliteMapParameters with content type ELEMENT_ONLY
class satelliteMapParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'satelliteMapParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}DetectionThreshold uses Python identifier DetectionThreshold
    __DetectionThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectionThreshold'), 'DetectionThreshold', '__httpeuclid_esa_orgschemaproext_satelliteMapParameters_httpeuclid_esa_orgschemaproextDetectionThreshold', False)

    
    DetectionThreshold = property(__DetectionThreshold.value, __DetectionThreshold.set, None, u' Minimum SNR for pixels to enter line\n                        detection routine [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}HoughThreshold uses Python identifier HoughThreshold
    __HoughThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HoughThreshold'), 'HoughThreshold', '__httpeuclid_esa_orgschemaproext_satelliteMapParameters_httpeuclid_esa_orgschemaproextHoughThreshold', False)

    
    HoughThreshold = property(__HoughThreshold.value, __HoughThreshold.set, None, u' Minimum number of pixels on a line, i.e.\n                        the minimum pixel value in the Hough image [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_satelliteMapParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')


    _ElementMap = {
        __DetectionThreshold.name() : __DetectionThreshold,
        __HoughThreshold.name() : __HoughThreshold,
        __ExtObjectId.name() : __ExtObjectId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'satelliteMapParameters', satelliteMapParameters)


# Complex type sourceList with content type ELEMENT_ONLY
class sourceList (baseList):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceList')
    # Base type is baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}SexParam uses Python identifier SexParam
    __SexParam = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexParam'), 'SexParam', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextSexParam', True)

    
    SexParam = property(__SexParam.value, __SexParam.set, None, u' List of parameters derived for\n                                each extracted source [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}AstromParams uses Python identifier AstromParams
    __AstromParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AstromParams'), 'AstromParams', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextAstromParams', False)

    
    AstromParams = property(__AstromParams.value, __AstromParams.set, None, u' Advanced information about the\n                                derived astrometry (with higher-order terms)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Slid uses Python identifier Slid
    __Slid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Slid'), 'Slid', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextSlid', False)

    
    Slid = property(__Slid.value, __Slid.set, None, u' Identifier of the source list\n                                [None] ')

    
    # Element LRRa ({http://euclid.esa.org/schema/pro/ext}LRRa) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCount uses Python identifier SourceCount
    __SourceCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), 'SourceCount', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextSourceCount', False)

    
    SourceCount = property(__SourceCount.value, __SourceCount.set, None, u' Number of extracted sources\n                                [None] ')

    
    # Element ULRa ({http://euclid.esa.org/schema/pro/ext}ULRa) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element URRa ({http://euclid.esa.org/schema/pro/ext}URRa) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}Sources uses Python identifier Sources
    __Sources = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sources'), 'Sources', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextSources', True)

    
    Sources = property(__Sources.value, __Sources.set, None, u' Column definitions of extracted\n                                sources [None] ')

    
    # Element URDec ({http://euclid.esa.org/schema/pro/ext}URDec) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}DetectionFrame uses Python identifier DetectionFrame
    __DetectionFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectionFrame'), 'DetectionFrame', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextDetectionFrame', False)

    
    DetectionFrame = property(__DetectionFrame.value, __DetectionFrame.set, None, u' Optional frame used to identify\n                                sources to be extracted (double image mode)\n                                [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/pro/ext}ExtObjectId) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/pro/ext}CreationDate) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}Frame uses Python identifier Frame
    __Frame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Frame'), 'Frame', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextFrame', False)

    
    Frame = property(__Frame.value, __Frame.set, None, u' Information about the input frame\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SexConfig uses Python identifier SexConfig
    __SexConfig = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), 'SexConfig', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextSexConfig', False)

    
    SexConfig = property(__SexConfig.value, __SexConfig.set, None, u' SExtractor configuration for\n                                source extraction [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/pro/ext}IsValid) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}AssociateList uses Python identifier AssociateList
    __AssociateList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AssociateList'), 'AssociateList', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextAssociateList', False)

    
    AssociateList = property(__AssociateList.value, __AssociateList.set, None, u' ALID (associate list identifier)\n                                that was used to create this (combined) source\n                                list [None] ')

    
    # Element Name ({http://euclid.esa.org/schema/pro/ext}Name) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element Object ({http://euclid.esa.org/schema/pro/ext}Object) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element LRDec ({http://euclid.esa.org/schema/pro/ext}LRDec) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element LLRa ({http://euclid.esa.org/schema/pro/ext}LLRa) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filters uses Python identifier Filters
    __Filters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filters'), 'Filters', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextFilters', False)

    
    Filters = property(__Filters.value, __Filters.set, None, u' Observational filters for which\n                                columns are present in this (combined) source\n                                list [None] ')

    
    # Element ULDec ({http://euclid.esa.org/schema/pro/ext}ULDec) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element LLDec ({http://euclid.esa.org/schema/pro/ext}LLDec) inherited from {http://euclid.esa.org/schema/pro/ext}baseList
    
    # Element {http://euclid.esa.org/schema/pro/ext}CombineMethod uses Python identifier CombineMethod
    __CombineMethod = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CombineMethod'), 'CombineMethod', '__httpeuclid_esa_orgschemaproext_sourceList_httpeuclid_esa_orgschemaproextCombineMethod', False)

    
    CombineMethod = property(__CombineMethod.value, __CombineMethod.set, None, u' Method that was used to create\n                                this (combined) source list [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/pro/ext}Storage) inherited from {http://euclid.esa.org/schema/pro/ext}baseList

    _ElementMap = baseList._ElementMap.copy()
    _ElementMap.update({
        __SexParam.name() : __SexParam,
        __Instrument.name() : __Instrument,
        __AstromParams.name() : __AstromParams,
        __ProcessParams.name() : __ProcessParams,
        __Chip.name() : __Chip,
        __Slid.name() : __Slid,
        __SourceCount.name() : __SourceCount,
        __Sources.name() : __Sources,
        __DetectionFrame.name() : __DetectionFrame,
        __Filter.name() : __Filter,
        __Frame.name() : __Frame,
        __SexConfig.name() : __SexConfig,
        __AssociateList.name() : __AssociateList,
        __Filters.name() : __Filters,
        __CombineMethod.name() : __CombineMethod
    })
    _AttributeMap = baseList._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sourceList', sourceList)


# Complex type atmosphericExtinctionCoefficient with content type ELEMENT_ONLY
class atmosphericExtinctionCoefficient (baseAtmosphericExtinction):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'atmosphericExtinctionCoefficient')
    # Base type is baseAtmosphericExtinction
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/pro/ext}Instrument) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction
    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_atmosphericExtinctionCoefficient_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] [none] ')

    
    # Element ExtinctionCurve ({http://euclid.esa.org/schema/pro/ext}ExtinctionCurve) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Value ({http://euclid.esa.org/schema/pro/ext}Value) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction
    
    # Element Filter ({http://euclid.esa.org/schema/pro/ext}Filter) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_atmosphericExtinctionCoefficient_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Error ({http://euclid.esa.org/schema/pro/ext}Error) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_atmosphericExtinctionCoefficient_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element MagId ({http://euclid.esa.org/schema/pro/ext}MagId) inherited from {http://euclid.esa.org/schema/pro/ext}baseAtmosphericExtinction

    _ElementMap = baseAtmosphericExtinction._ElementMap.copy()
    _ElementMap.update({
        __Chip.name() : __Chip,
        __TimestampStart.name() : __TimestampStart,
        __TimestampEnd.name() : __TimestampEnd
    })
    _AttributeMap = baseAtmosphericExtinction._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'atmosphericExtinctionCoefficient', atmosphericExtinctionCoefficient)


# Complex type rawBiasFrameParameters with content type ELEMENT_ONLY
class rawBiasFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawBiasFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxBiasLevel uses Python identifier MaxBiasLevel
    __MaxBiasLevel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasLevel'), 'MaxBiasLevel', '__httpeuclid_esa_orgschemaproext_rawBiasFrameParameters_httpeuclid_esa_orgschemaproextMaxBiasLevel', False)

    
    MaxBiasLevel = property(__MaxBiasLevel.value, __MaxBiasLevel.set, None, u' QC: Maximum average bias level (mean of\n                        the bias pixel values) [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxBiasFlatness uses Python identifier MaxBiasFlatness
    __MaxBiasFlatness = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasFlatness'), 'MaxBiasFlatness', '__httpeuclid_esa_orgschemaproext_rawBiasFrameParameters_httpeuclid_esa_orgschemaproextMaxBiasFlatness', False)

    
    MaxBiasFlatness = property(__MaxBiasFlatness.value, __MaxBiasFlatness.set, None, u' QC: Maximum difference in subwindow\n                        statistics (minimum minus maximum median values of 32\n                        sub-regions) [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_rawBiasFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxBiasStdev uses Python identifier MaxBiasStdev
    __MaxBiasStdev = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasStdev'), 'MaxBiasStdev', '__httpeuclid_esa_orgschemaproext_rawBiasFrameParameters_httpeuclid_esa_orgschemaproextMaxBiasStdev', False)

    
    MaxBiasStdev = property(__MaxBiasStdev.value, __MaxBiasStdev.set, None, u' QC: Maximum sample standard deviation of\n                        the bias pixel values [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_rawBiasFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')


    _ElementMap = {
        __MaxBiasLevel.name() : __MaxBiasLevel,
        __MaxBiasFlatness.name() : __MaxBiasFlatness,
        __ExtObjectId.name() : __ExtObjectId,
        __MaxBiasStdev.name() : __MaxBiasStdev,
        __SourceCodeVersion.name() : __SourceCodeVersion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'rawBiasFrameParameters', rawBiasFrameParameters)


# Complex type hotPixelMapParameters with content type ELEMENT_ONLY
class hotPixelMapParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hotPixelMapParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumIterations uses Python identifier MaximumIterations
    __MaximumIterations = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations'), 'MaximumIterations', '__httpeuclid_esa_orgschemaproext_hotPixelMapParameters_httpeuclid_esa_orgschemaproextMaximumIterations', False)

    
    MaximumIterations = property(__MaximumIterations.value, __MaximumIterations.set, None, u' Maximum number of iterations for\n                        estimating statistics [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_hotPixelMapParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_hotPixelMapParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumHotPixelCount uses Python identifier MaximumHotPixelCount
    __MaximumHotPixelCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumHotPixelCount'), 'MaximumHotPixelCount', '__httpeuclid_esa_orgschemaproext_hotPixelMapParameters_httpeuclid_esa_orgschemaproextMaximumHotPixelCount', False)

    
    MaximumHotPixelCount = property(__MaximumHotPixelCount.value, __MaximumHotPixelCount.set, None, u' QC: Maximum number of hot pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RejectionThreshold uses Python identifier RejectionThreshold
    __RejectionThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold'), 'RejectionThreshold', '__httpeuclid_esa_orgschemaproext_hotPixelMapParameters_httpeuclid_esa_orgschemaproextRejectionThreshold', False)

    
    RejectionThreshold = property(__RejectionThreshold.value, __RejectionThreshold.set, None, u' Threshold for rejecting pixels with\n                        outlying values [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumHotPixelCountDifference uses Python identifier MaximumHotPixelCountDifference
    __MaximumHotPixelCountDifference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumHotPixelCountDifference'), 'MaximumHotPixelCountDifference', '__httpeuclid_esa_orgschemaproext_hotPixelMapParameters_httpeuclid_esa_orgschemaproextMaximumHotPixelCountDifference', False)

    
    MaximumHotPixelCountDifference = property(__MaximumHotPixelCountDifference.value, __MaximumHotPixelCountDifference.set, None, u' QC: Maximum number of new hot pixels\n                        relative to the previous version [None] ')


    _ElementMap = {
        __MaximumIterations.name() : __MaximumIterations,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __ExtObjectId.name() : __ExtObjectId,
        __MaximumHotPixelCount.name() : __MaximumHotPixelCount,
        __RejectionThreshold.name() : __RejectionThreshold,
        __MaximumHotPixelCountDifference.name() : __MaximumHotPixelCountDifference
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'hotPixelMapParameters', hotPixelMapParameters)


# Complex type rawDarkFrame with content type ELEMENT_ONLY
class rawDarkFrame (rawFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawDarkFrame')
    # Base type is rawFrame
    
    # Element PrescanYStat ({http://euclid.esa.org/schema/pro/ext}PrescanYStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Ovscy ({http://euclid.esa.org/schema/pro/ext}Ovscy) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscypst ({http://euclid.esa.org/schema/pro/ext}Ovscypst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element OverscanXStat ({http://euclid.esa.org/schema/pro/ext}OverscanXStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscxpre ({http://euclid.esa.org/schema/pro/ext}Prscxpre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Object ({http://euclid.esa.org/schema/pro/ext}Object) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ObsBlock ({http://euclid.esa.org/schema/pro/ext}ObsBlock) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Prscypre ({http://euclid.esa.org/schema/pro/ext}Prscypre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Date ({http://euclid.esa.org/schema/pro/ext}Date) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element OverscanYStat ({http://euclid.esa.org/schema/pro/ext}OverscanYStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscxpre ({http://euclid.esa.org/schema/pro/ext}Ovscxpre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element DateObs ({http://euclid.esa.org/schema/pro/ext}DateObs) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscypre ({http://euclid.esa.org/schema/pro/ext}Ovscypre) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element MjdObs ({http://euclid.esa.org/schema/pro/ext}MjdObs) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Extension ({http://euclid.esa.org/schema/pro/ext}Extension) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscxpst ({http://euclid.esa.org/schema/pro/ext}Prscxpst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Lst ({http://euclid.esa.org/schema/pro/ext}Lst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element RawFits ({http://euclid.esa.org/schema/pro/ext}RawFits) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element PrescanXStat ({http://euclid.esa.org/schema/pro/ext}PrescanXStat) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Utc ({http://euclid.esa.org/schema/pro/ext}Utc) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExpTime uses Python identifier ExpTime
    __ExpTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), 'ExpTime', '__httpeuclid_esa_orgschemaproext_rawDarkFrame_httpeuclid_esa_orgschemaproextExpTime', False)

    
    ExpTime = property(__ExpTime.value, __ExpTime.set, None, u' Total time of an individual\n                                exposure [sec] ')

    
    # Element Ovscxpst ({http://euclid.esa.org/schema/pro/ext}Ovscxpst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscx ({http://euclid.esa.org/schema/pro/ext}Prscx) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Template ({http://euclid.esa.org/schema/pro/ext}Template) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Chip ({http://euclid.esa.org/schema/pro/ext}Chip) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscy ({http://euclid.esa.org/schema/pro/ext}Prscy) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Observer ({http://euclid.esa.org/schema/pro/ext}Observer) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Ovscx ({http://euclid.esa.org/schema/pro/ext}Ovscx) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame
    
    # Element Prscypst ({http://euclid.esa.org/schema/pro/ext}Prscypst) inherited from {http://euclid.esa.org/schema/pro/ext}rawFrame

    _ElementMap = rawFrame._ElementMap.copy()
    _ElementMap.update({
        __ExpTime.name() : __ExpTime
    })
    _AttributeMap = rawFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'rawDarkFrame', rawDarkFrame)


# Complex type domeFlatFrame with content type ELEMENT_ONLY
class domeFlatFrame (baseFlatFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'domeFlatFrame')
    # Base type is baseFlatFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Lamp uses Python identifier Lamp
    __Lamp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Lamp'), 'Lamp', '__httpeuclid_esa_orgschemaproext_domeFlatFrame_httpeuclid_esa_orgschemaproextLamp', False)

    
    Lamp = property(__Lamp.value, __Lamp.set, None, u' Information about the dome flat\n                                lamp [None] ')

    
    # Element Filter ({http://euclid.esa.org/schema/pro/ext}Filter) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Chip ({http://euclid.esa.org/schema/pro/ext}Chip) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}RawDomeFlatFrames uses Python identifier RawDomeFlatFrames
    __RawDomeFlatFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawDomeFlatFrames'), 'RawDomeFlatFrames', '__httpeuclid_esa_orgschemaproext_domeFlatFrame_httpeuclid_esa_orgschemaproextRawDomeFlatFrames', True)

    
    RawDomeFlatFrames = property(__RawDomeFlatFrames.value, __RawDomeFlatFrames.set, None, u' List of input raw dome flat\n                                frames [None] ')

    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/ext}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Bias uses Python identifier Bias
    __Bias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Bias'), 'Bias', '__httpeuclid_esa_orgschemaproext_domeFlatFrame_httpeuclid_esa_orgschemaproextBias', False)

    
    Bias = property(__Bias.value, __Bias.set, None, u' Information about the detector\n                                bias offset levels [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Gain uses Python identifier Gain
    __Gain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Gain'), 'Gain', '__httpeuclid_esa_orgschemaproext_domeFlatFrame_httpeuclid_esa_orgschemaproextGain', False)

    
    Gain = property(__Gain.value, __Gain.set, None, u' Information about the detector\n                                gain [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Hot uses Python identifier Hot
    __Hot = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Hot'), 'Hot', '__httpeuclid_esa_orgschemaproext_domeFlatFrame_httpeuclid_esa_orgschemaproextHot', False)

    
    Hot = property(__Hot.value, __Hot.set, None, u' Information about the detector\n                                hot pixels [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Cold uses Python identifier Cold
    __Cold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cold'), 'Cold', '__httpeuclid_esa_orgschemaproext_domeFlatFrame_httpeuclid_esa_orgschemaproextCold', False)

    
    Cold = property(__Cold.value, __Cold.set, None, u' Information about the detector\n                                cold pixels [None] ')

    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/ext}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_domeFlatFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_domeFlatFrame_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_domeFlatFrame_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')


    _ElementMap = baseFlatFrame._ElementMap.copy()
    _ElementMap.update({
        __Lamp.name() : __Lamp,
        __RawDomeFlatFrames.name() : __RawDomeFlatFrames,
        __Bias.name() : __Bias,
        __Gain.name() : __Gain,
        __Hot.name() : __Hot,
        __Cold.name() : __Cold,
        __ProcessParams.name() : __ProcessParams,
        __ObsBlock.name() : __ObsBlock,
        __Template.name() : __Template
    })
    _AttributeMap = baseFlatFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'domeFlatFrame', domeFlatFrame)


# Complex type twilightFlatFrame with content type ELEMENT_ONLY
class twilightFlatFrame (baseFlatFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'twilightFlatFrame')
    # Base type is baseFlatFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Gain uses Python identifier Gain
    __Gain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Gain'), 'Gain', '__httpeuclid_esa_orgschemaproext_twilightFlatFrame_httpeuclid_esa_orgschemaproextGain', False)

    
    Gain = property(__Gain.value, __Gain.set, None, u' Information about the detector\n                                gain [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Hot uses Python identifier Hot
    __Hot = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Hot'), 'Hot', '__httpeuclid_esa_orgschemaproext_twilightFlatFrame_httpeuclid_esa_orgschemaproextHot', False)

    
    Hot = property(__Hot.value, __Hot.set, None, u' Information about the detector\n                                hot pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ObsBlock uses Python identifier ObsBlock
    __ObsBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), 'ObsBlock', '__httpeuclid_esa_orgschemaproext_twilightFlatFrame_httpeuclid_esa_orgschemaproextObsBlock', False)

    
    ObsBlock = property(__ObsBlock.value, __ObsBlock.set, None, u' Information about the\n                                observational block [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}RawTwilightFlatFrames uses Python identifier RawTwilightFlatFrames
    __RawTwilightFlatFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawTwilightFlatFrames'), 'RawTwilightFlatFrames', '__httpeuclid_esa_orgschemaproext_twilightFlatFrame_httpeuclid_esa_orgschemaproextRawTwilightFlatFrames', True)

    
    RawTwilightFlatFrames = property(__RawTwilightFlatFrames.value, __RawTwilightFlatFrames.set, None, u' List of input raw twilight flat\n                                frames [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Filter ({http://euclid.esa.org/schema/pro/ext}Filter) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element TimestampEnd ({http://euclid.esa.org/schema/pro/ext}TimestampEnd) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemaproext_twilightFlatFrame_httpeuclid_esa_orgschemaproextTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, u' Information about the\n                                observational template [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Cold uses Python identifier Cold
    __Cold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cold'), 'Cold', '__httpeuclid_esa_orgschemaproext_twilightFlatFrame_httpeuclid_esa_orgschemaproextCold', False)

    
    Cold = property(__Cold.value, __Cold.set, None, u' Information about the detector\n                                cold pixels [None] ')

    
    # Element TimestampStart ({http://euclid.esa.org/schema/pro/ext}TimestampStart) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Bias uses Python identifier Bias
    __Bias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Bias'), 'Bias', '__httpeuclid_esa_orgschemaproext_twilightFlatFrame_httpeuclid_esa_orgschemaproextBias', False)

    
    Bias = property(__Bias.value, __Bias.set, None, u' Information about the detector\n                                bias offset levels [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Chip ({http://euclid.esa.org/schema/pro/ext}Chip) inherited from {http://euclid.esa.org/schema/pro/ext}baseFlatFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_twilightFlatFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame

    _ElementMap = baseFlatFrame._ElementMap.copy()
    _ElementMap.update({
        __Gain.name() : __Gain,
        __Hot.name() : __Hot,
        __ObsBlock.name() : __ObsBlock,
        __RawTwilightFlatFrames.name() : __RawTwilightFlatFrames,
        __Template.name() : __Template,
        __Cold.name() : __Cold,
        __Bias.name() : __Bias,
        __ProcessParams.name() : __ProcessParams
    })
    _AttributeMap = baseFlatFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'twilightFlatFrame', twilightFlatFrame)


# Complex type nightSkyFlatFrame with content type ELEMENT_ONLY
class nightSkyFlatFrame (CommonDM.dm.bas.img_stub.baseFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nightSkyFlatFrame')
    # Base type is CommonDM.dm.bas.img_stub.baseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrame_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Hot uses Python identifier Hot
    __Hot = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Hot'), 'Hot', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrame_httpeuclid_esa_orgschemaproextHot', False)

    
    Hot = property(__Hot.value, __Hot.set, None, u' Information about the detector\n                                hot pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Bias uses Python identifier Bias
    __Bias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Bias'), 'Bias', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrame_httpeuclid_esa_orgschemaproextBias', False)

    
    Bias = property(__Bias.value, __Bias.set, None, u' Information about the detector\n                                bias offset levels [None] ')

    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrame_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}Flat uses Python identifier Flat
    __Flat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flat'), 'Flat', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrame_httpeuclid_esa_orgschemaproextFlat', False)

    
    Flat = property(__Flat.value, __Flat.set, None, u' Information about the detector\n                                sensitivity variations [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Cold uses Python identifier Cold
    __Cold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cold'), 'Cold', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrame_httpeuclid_esa_orgschemaproextCold', False)

    
    Cold = property(__Cold.value, __Cold.set, None, u' Information about the detector\n                                cold pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}RawScienceFrames uses Python identifier RawScienceFrames
    __RawScienceFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawScienceFrames'), 'RawScienceFrames', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrame_httpeuclid_esa_orgschemaproextRawScienceFrames', True)

    
    RawScienceFrames = property(__RawScienceFrames.value, __RawScienceFrames.set, None, u' List of input raw science frames\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrame_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_nightSkyFlatFrame_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')


    _ElementMap = CommonDM.dm.bas.img_stub.baseFrame._ElementMap.copy()
    _ElementMap.update({
        __Filter.name() : __Filter,
        __Hot.name() : __Hot,
        __Bias.name() : __Bias,
        __TimestampEnd.name() : __TimestampEnd,
        __Flat.name() : __Flat,
        __Cold.name() : __Cold,
        __ProcessParams.name() : __ProcessParams,
        __RawScienceFrames.name() : __RawScienceFrames,
        __Chip.name() : __Chip,
        __TimestampStart.name() : __TimestampStart
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.baseFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'nightSkyFlatFrame', nightSkyFlatFrame)


# Complex type masterFlatFrameParameters with content type ELEMENT_ONLY
class masterFlatFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'masterFlatFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_masterFlatFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}CombineType uses Python identifier CombineType
    __CombineType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CombineType'), 'CombineType', '__httpeuclid_esa_orgschemaproext_masterFlatFrameParameters_httpeuclid_esa_orgschemaproextCombineType', False)

    
    CombineType = property(__CombineType.value, __CombineType.set, None, u' Index for the type of input (some\n                        combination of dome and/or twilight flat frame) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_masterFlatFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MirrorYpix uses Python identifier MirrorYpix
    __MirrorYpix = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MirrorYpix'), 'MirrorYpix', '__httpeuclid_esa_orgschemaproext_masterFlatFrameParameters_httpeuclid_esa_orgschemaproextMirrorYpix', False)

    
    MirrorYpix = property(__MirrorYpix.value, __MirrorYpix.set, None, u' Number of pixels to mirror beyond the Y\n                        edges of the detector to provide Fourier transform\n                        continuity [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaximumSubwinDiff uses Python identifier MaximumSubwinDiff
    __MaximumSubwinDiff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinDiff'), 'MaximumSubwinDiff', '__httpeuclid_esa_orgschemaproext_masterFlatFrameParameters_httpeuclid_esa_orgschemaproextMaximumSubwinDiff', False)

    
    MaximumSubwinDiff = property(__MaximumSubwinDiff.value, __MaximumSubwinDiff.set, None, u' QC: Difference in MaximumSubwinFlatness\n                        relative to the previous version [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}DigFilterSize uses Python identifier DigFilterSize
    __DigFilterSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DigFilterSize'), 'DigFilterSize', '__httpeuclid_esa_orgschemaproext_masterFlatFrameParameters_httpeuclid_esa_orgschemaproextDigFilterSize', False)

    
    DigFilterSize = property(__DigFilterSize.value, __DigFilterSize.set, None, u' Gaussian Fourier filter size [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MedianFilterSize uses Python identifier MedianFilterSize
    __MedianFilterSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MedianFilterSize'), 'MedianFilterSize', '__httpeuclid_esa_orgschemaproext_masterFlatFrameParameters_httpeuclid_esa_orgschemaproextMedianFilterSize', False)

    
    MedianFilterSize = property(__MedianFilterSize.value, __MedianFilterSize.set, None, u' Size of the median cleaning filter\n                        [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MirrorXpix uses Python identifier MirrorXpix
    __MirrorXpix = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MirrorXpix'), 'MirrorXpix', '__httpeuclid_esa_orgschemaproext_masterFlatFrameParameters_httpeuclid_esa_orgschemaproextMirrorXpix', False)

    
    MirrorXpix = property(__MirrorXpix.value, __MirrorXpix.set, None, u' Number of pixels to mirror beyond the X\n                        edges of the detector to provide Fourier transform\n                        continuity [pixel] ')


    _ElementMap = {
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __CombineType.name() : __CombineType,
        __ExtObjectId.name() : __ExtObjectId,
        __MirrorYpix.name() : __MirrorYpix,
        __MaximumSubwinDiff.name() : __MaximumSubwinDiff,
        __DigFilterSize.name() : __DigFilterSize,
        __MedianFilterSize.name() : __MedianFilterSize,
        __MirrorXpix.name() : __MirrorXpix
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'masterFlatFrameParameters', masterFlatFrameParameters)


# Complex type satelliteMap with content type ELEMENT_ONLY
class satelliteMap (pixelMap):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'satelliteMap')
    # Base type is pixelMap
    
    # Element {http://euclid.esa.org/schema/pro/ext}Chip uses Python identifier Chip
    __Chip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Chip'), 'Chip', '__httpeuclid_esa_orgschemaproext_satelliteMap_httpeuclid_esa_orgschemaproextChip', False)

    
    Chip = property(__Chip.value, __Chip.set, None, u' Information about the detector\n                                chip [None] ')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Cold uses Python identifier Cold
    __Cold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cold'), 'Cold', '__httpeuclid_esa_orgschemaproext_satelliteMap_httpeuclid_esa_orgschemaproextCold', False)

    
    Cold = property(__Cold.value, __Cold.set, None, u' Information about the detector\n                                cold pixels [None] ')

    
    # Element Count ({http://euclid.esa.org/schema/pro/ext}Count) inherited from {http://euclid.esa.org/schema/pro/ext}pixelMap
    
    # Element {http://euclid.esa.org/schema/pro/ext}Frame uses Python identifier Frame
    __Frame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Frame'), 'Frame', '__httpeuclid_esa_orgschemaproext_satelliteMap_httpeuclid_esa_orgschemaproextFrame', False)

    
    Frame = property(__Frame.value, __Frame.set, None, u' Information about the input\n                                reduced science frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_satelliteMap_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_satelliteMap_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Saturated uses Python identifier Saturated
    __Saturated = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Saturated'), 'Saturated', '__httpeuclid_esa_orgschemaproext_satelliteMap_httpeuclid_esa_orgschemaproextSaturated', False)

    
    Saturated = property(__Saturated.value, __Saturated.set, None, u' Information about saturated\n                                pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Flat uses Python identifier Flat
    __Flat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flat'), 'Flat', '__httpeuclid_esa_orgschemaproext_satelliteMap_httpeuclid_esa_orgschemaproextFlat', False)

    
    Flat = property(__Flat.value, __Flat.set, None, u' Information about the detector\n                                sensitivity variations [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_satelliteMap_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element {http://euclid.esa.org/schema/pro/ext}Hot uses Python identifier Hot
    __Hot = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Hot'), 'Hot', '__httpeuclid_esa_orgschemaproext_satelliteMap_httpeuclid_esa_orgschemaproextHot', False)

    
    Hot = property(__Hot.value, __Hot.set, None, u' Information about the detector\n                                hot pixels [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Illumination uses Python identifier Illumination
    __Illumination = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), 'Illumination', '__httpeuclid_esa_orgschemaproext_satelliteMap_httpeuclid_esa_orgschemaproextIllumination', False)

    
    Illumination = property(__Illumination.value, __Illumination.set, None, u' Information about the\n                                illumination correction [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget

    _ElementMap = pixelMap._ElementMap.copy()
    _ElementMap.update({
        __Chip.name() : __Chip,
        __Cold.name() : __Cold,
        __Frame.name() : __Frame,
        __Instrument.name() : __Instrument,
        __ProcessParams.name() : __ProcessParams,
        __Saturated.name() : __Saturated,
        __Flat.name() : __Flat,
        __Filter.name() : __Filter,
        __Hot.name() : __Hot,
        __Illumination.name() : __Illumination
    })
    _AttributeMap = pixelMap._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'satelliteMap', satelliteMap)


# Complex type photTransformation with content type ELEMENT_ONLY
class photTransformation (CommonDM.dm.bas.img_stub.processTarget):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photTransformation')
    # Base type is CommonDM.dm.bas.img_stub.processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampEnd uses Python identifier TimestampEnd
    __TimestampEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), 'TimestampEnd', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextTimestampEnd', False)

    
    TimestampEnd = property(__TimestampEnd.value, __TimestampEnd.set, None, u' UTC date of the ending of the\n                                valid period [None] ')

    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}ColorTermError uses Python identifier ColorTermError
    __ColorTermError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ColorTermError'), 'ColorTermError', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextColorTermError', False)

    
    ColorTermError = property(__ColorTermError.value, __ColorTermError.set, None, u' Error on color term [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MagId uses Python identifier MagId
    __MagId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagId'), 'MagId', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextMagId', False)

    
    MagId = property(__MagId.value, __MagId.set, None, u' Identifier for the photometric\n                                band [None]')

    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}CoefficientError uses Python identifier CoefficientError
    __CoefficientError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CoefficientError'), 'CoefficientError', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextCoefficientError', False)

    
    CoefficientError = property(__CoefficientError.value, __CoefficientError.set, None, u' Error on additional offset [mag] ')

    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}Coefficient uses Python identifier Coefficient
    __Coefficient = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Coefficient'), 'Coefficient', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextCoefficient', False)

    
    Coefficient = property(__Coefficient.value, __Coefficient.set, None, u' Additional offset [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Instrument uses Python identifier Instrument
    __Instrument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), 'Instrument', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextInstrument', False)

    
    Instrument = property(__Instrument.value, __Instrument.set, None, u' Information about the acquisition\n                                instrument [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SecondaryBand uses Python identifier SecondaryBand
    __SecondaryBand = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SecondaryBand'), 'SecondaryBand', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextSecondaryBand', False)

    
    SecondaryBand = property(__SecondaryBand.value, __SecondaryBand.set, None, u' Magnitude ID of secondary filter\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TimestampStart uses Python identifier TimestampStart
    __TimestampStart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), 'TimestampStart', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextTimestampStart', False)

    
    TimestampStart = property(__TimestampStart.value, __TimestampStart.set, None, u' UTC date of the beginning of the\n                                valid period [None] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element {http://euclid.esa.org/schema/pro/ext}PrimaryBand uses Python identifier PrimaryBand
    __PrimaryBand = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrimaryBand'), 'PrimaryBand', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextPrimaryBand', False)

    
    PrimaryBand = property(__PrimaryBand.value, __PrimaryBand.set, None, u' Magnitude ID of primary filter\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}TertiaryBand uses Python identifier TertiaryBand
    __TertiaryBand = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TertiaryBand'), 'TertiaryBand', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextTertiaryBand', False)

    
    TertiaryBand = property(__TertiaryBand.value, __TertiaryBand.set, None, u' Magnitude ID of tertiary filter\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, u' Information about the\n                                observational filter [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}ColorTerm uses Python identifier ColorTerm
    __ColorTerm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ColorTerm'), 'ColorTerm', '__httpeuclid_esa_orgschemaproext_photTransformation_httpeuclid_esa_orgschemaproextColorTerm', False)

    
    ColorTerm = property(__ColorTerm.value, __ColorTerm.set, None, u' Color term [mag] ')


    _ElementMap = CommonDM.dm.bas.img_stub.processTarget._ElementMap.copy()
    _ElementMap.update({
        __TimestampEnd.name() : __TimestampEnd,
        __ColorTermError.name() : __ColorTermError,
        __MagId.name() : __MagId,
        __CoefficientError.name() : __CoefficientError,
        __Coefficient.name() : __Coefficient,
        __Instrument.name() : __Instrument,
        __SecondaryBand.name() : __SecondaryBand,
        __TimestampStart.name() : __TimestampStart,
        __PrimaryBand.name() : __PrimaryBand,
        __TertiaryBand.name() : __TertiaryBand,
        __Filter.name() : __Filter,
        __ColorTerm.name() : __ColorTerm
    })
    _AttributeMap = CommonDM.dm.bas.img_stub.processTarget._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'photTransformation', photTransformation)


# Complex type rawDomeFlatFrameParameters with content type ELEMENT_ONLY
class rawDomeFlatFrameParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rawDomeFlatFrameParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/ext}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemaproext_rawDomeFlatFrameParameters_httpeuclid_esa_orgschemaproextExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SourceCodeVersion uses Python identifier SourceCodeVersion
    __SourceCodeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), 'SourceCodeVersion', '__httpeuclid_esa_orgschemaproext_rawDomeFlatFrameParameters_httpeuclid_esa_orgschemaproextSourceCodeVersion', False)

    
    SourceCodeVersion = property(__SourceCodeVersion.value, __SourceCodeVersion.set, None, u' Version of the source code [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MaxFlatMean uses Python identifier MaxFlatMean
    __MaxFlatMean = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxFlatMean'), 'MaxFlatMean', '__httpeuclid_esa_orgschemaproext_rawDomeFlatFrameParameters_httpeuclid_esa_orgschemaproextMaxFlatMean', False)

    
    MaxFlatMean = property(__MaxFlatMean.value, __MaxFlatMean.set, None, u' QC: Maximum level of the flat (mean of\n                        the flat pixel values) [ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MinFlatMean uses Python identifier MinFlatMean
    __MinFlatMean = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinFlatMean'), 'MinFlatMean', '__httpeuclid_esa_orgschemaproext_rawDomeFlatFrameParameters_httpeuclid_esa_orgschemaproextMinFlatMean', False)

    
    MinFlatMean = property(__MinFlatMean.value, __MinFlatMean.set, None, u' QC: Minimum level of the flat (mean of\n                        the flat pixel values) [ADU] ')


    _ElementMap = {
        __ExtObjectId.name() : __ExtObjectId,
        __SourceCodeVersion.name() : __SourceCodeVersion,
        __MaxFlatMean.name() : __MaxFlatMean,
        __MinFlatMean.name() : __MinFlatMean
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'rawDomeFlatFrameParameters', rawDomeFlatFrameParameters)


# Complex type coaddedRegriddedFrame with content type ELEMENT_ONLY
class coaddedRegriddedFrame (baseRegriddedFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coaddedRegriddedFrame')
    # Base type is baseRegriddedFrame
    
    # Element Seeing ({http://euclid.esa.org/schema/pro/ext}Seeing) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}RegriddedFrames uses Python identifier RegriddedFrames
    __RegriddedFrames = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RegriddedFrames'), 'RegriddedFrames', '__httpeuclid_esa_orgschemaproext_coaddedRegriddedFrame_httpeuclid_esa_orgschemaproextRegriddedFrames', True)

    
    RegriddedFrames = property(__RegriddedFrames.value, __RegriddedFrames.set, None, u' List of regridded frames to be\n                                coadded [None] ')

    
    # Element ObsBlock ({http://euclid.esa.org/schema/pro/ext}ObsBlock) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element Filter ({http://euclid.esa.org/schema/pro/ext}Filter) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Astrom ({http://euclid.esa.org/schema/pro/ext}Astrom) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element Template ({http://euclid.esa.org/schema/pro/ext}Template) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Object ({http://euclid.esa.org/schema/pro/ext}Object) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element GridTarget ({http://euclid.esa.org/schema/pro/ext}GridTarget) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element SwarpConf ({http://euclid.esa.org/schema/pro/ext}SwarpConf) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element Weight ({http://euclid.esa.org/schema/pro/ext}Weight) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}ProcessParams uses Python identifier ProcessParams
    __ProcessParams = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), 'ProcessParams', '__httpeuclid_esa_orgschemaproext_coaddedRegriddedFrame_httpeuclid_esa_orgschemaproextProcessParams', False)

    
    ProcessParams = property(__ProcessParams.value, __ProcessParams.set, None, u' Processing and verification\n                                parameters [None] ')

    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element ZeroPointError ({http://euclid.esa.org/schema/pro/ext}ZeroPointError) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element ZeroPoint ({http://euclid.esa.org/schema/pro/ext}ZeroPoint) inherited from {http://euclid.esa.org/schema/pro/ext}baseRegriddedFrame
    
    # Element {http://euclid.esa.org/schema/pro/ext}PsfRadiiPerDetector uses Python identifier PsfRadiiPerDetector
    __PsfRadiiPerDetector = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PsfRadiiPerDetector'), 'PsfRadiiPerDetector', '__httpeuclid_esa_orgschemaproext_coaddedRegriddedFrame_httpeuclid_esa_orgschemaproextPsfRadiiPerDetector', True)

    
    PsfRadiiPerDetector = property(__PsfRadiiPerDetector.value, __PsfRadiiPerDetector.set, None, u' List of stellar FWHM in\n                                subsections of the coadd [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}Detectors uses Python identifier Detectors
    __Detectors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Detectors'), 'Detectors', '__httpeuclid_esa_orgschemaproext_coaddedRegriddedFrame_httpeuclid_esa_orgschemaproextDetectors', True)

    
    Detectors = property(__Detectors.value, __Detectors.set, None, u' List of detector names of which\n                                input is present in the output frame [None] ')


    _ElementMap = baseRegriddedFrame._ElementMap.copy()
    _ElementMap.update({
        __RegriddedFrames.name() : __RegriddedFrames,
        __ProcessParams.name() : __ProcessParams,
        __PsfRadiiPerDetector.name() : __PsfRadiiPerDetector,
        __Detectors.name() : __Detectors
    })
    _AttributeMap = baseRegriddedFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'coaddedRegriddedFrame', coaddedRegriddedFrame)


# Complex type preastromConfig with content type ELEMENT_ONLY
class preastromConfig (config):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'preastromConfig')
    # Base type is config
    
    # Element {http://euclid.esa.org/schema/pro/ext}VERBOSE uses Python identifier VERBOSE
    __VERBOSE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE'), 'VERBOSE', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextVERBOSE', False)

    
    VERBOSE = property(__VERBOSE.value, __VERBOSE.set, None, u' Verbosity level (QUIET, NORMAL,\n                                EXTRA_WARNINGS, FULL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MIN_OBJ uses Python identifier MIN_OBJ
    __MIN_OBJ = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MIN_OBJ'), 'MIN_OBJ', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextMIN_OBJ', False)

    
    MIN_OBJ = property(__MIN_OBJ.value, __MIN_OBJ.set, None, u' Minimum number of reference\n                                objects required to determine affine\n                                transformation [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MIN_PHOTS uses Python identifier MIN_PHOTS
    __MIN_PHOTS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MIN_PHOTS'), 'MIN_PHOTS', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextMIN_PHOTS', False)

    
    MIN_PHOTS = property(__MIN_PHOTS.value, __MIN_PHOTS.set, None, u' List of photometric parameter\n                                limits for pairing with reference objects [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}YPIXSIZE uses Python identifier YPIXSIZE
    __YPIXSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YPIXSIZE'), 'YPIXSIZE', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextYPIXSIZE', False)

    
    YPIXSIZE = property(__YPIXSIZE.value, __YPIXSIZE.set, None, u' Scaling of pixels with which\n                                CDELT2 is multiplied [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}FLAG_MASK uses Python identifier FLAG_MASK
    __FLAG_MASK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG_MASK'), 'FLAG_MASK', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextFLAG_MASK', False)

    
    FLAG_MASK = property(__FLAG_MASK.value, __FLAG_MASK.set, None, u' SExtractor mask to select objects\n                                for astrometric pairing: Flag and FLAG_MASK\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}RMS_TOL uses Python identifier RMS_TOL
    __RMS_TOL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RMS_TOL'), 'RMS_TOL', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextRMS_TOL', False)

    
    RMS_TOL = property(__RMS_TOL.value, __RMS_TOL.set, None, u' RMS tolerenace for triangulation\n                                matching [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}XMIN uses Python identifier XMIN
    __XMIN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XMIN'), 'XMIN', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextXMIN', False)

    
    XMIN = property(__XMIN.value, __XMIN.set, None, u' Minimum X coordinate allowed in\n                                pairing [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}SEL_MIN uses Python identifier SEL_MIN
    __SEL_MIN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SEL_MIN'), 'SEL_MIN', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextSEL_MIN', False)

    
    SEL_MIN = property(__SEL_MIN.value, __SEL_MIN.set, None, u' Minumim number of objects used in\n                                triangulation method [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}MAX_OFFSET uses Python identifier MAX_OFFSET
    __MAX_OFFSET = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAX_OFFSET'), 'MAX_OFFSET', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextMAX_OFFSET', False)

    
    MAX_OFFSET = property(__MAX_OFFSET.value, __MAX_OFFSET.set, None, u' Maximum allowed offset between\n                                extracted and reference objects [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}AFFINE_PARS uses Python identifier AFFINE_PARS
    __AFFINE_PARS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AFFINE_PARS'), 'AFFINE_PARS', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextAFFINE_PARS', True)

    
    AFFINE_PARS = property(__AFFINE_PARS.value, __AFFINE_PARS.set, None, u' List of Parameters for the affine\n                                transformation (a0, a1, a2, b0, b1, b2) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}PHOT uses Python identifier PHOT
    __PHOT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PHOT'), 'PHOT', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextPHOT', False)

    
    PHOT = property(__PHOT.value, __PHOT.set, None, u' Name of the table column\n                                containing object flux measures [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}YMAX uses Python identifier YMAX
    __YMAX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YMAX'), 'YMAX', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextYMAX', False)

    
    YMAX = property(__YMAX.value, __YMAX.set, None, u' Maximum Y coordinate allowed in\n                                pairing [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}YMIN uses Python identifier YMIN
    __YMIN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YMIN'), 'YMIN', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextYMIN', False)

    
    YMIN = property(__YMIN.value, __YMIN.set, None, u' Minimum Y coordinate allowed in\n                                pairing [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}POS_ERROR uses Python identifier POS_ERROR
    __POS_ERROR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'POS_ERROR'), 'POS_ERROR', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextPOS_ERROR', False)

    
    POS_ERROR = property(__POS_ERROR.value, __POS_ERROR.set, None, u' Positional error between\n                                extracted and reference objects [pixel] ')

    
    # Element ExtObjectId ({http://euclid.esa.org/schema/pro/ext}ExtObjectId) inherited from {http://euclid.esa.org/schema/pro/ext}config
    
    # Element {http://euclid.esa.org/schema/pro/ext}XMAX uses Python identifier XMAX
    __XMAX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XMAX'), 'XMAX', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextXMAX', False)

    
    XMAX = property(__XMAX.value, __XMAX.set, None, u' Maximum X coordinate allowed in\n                                pairing [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/ext}XPIXSIZE uses Python identifier XPIXSIZE
    __XPIXSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XPIXSIZE'), 'XPIXSIZE', '__httpeuclid_esa_orgschemaproext_preastromConfig_httpeuclid_esa_orgschemaproextXPIXSIZE', False)

    
    XPIXSIZE = property(__XPIXSIZE.value, __XPIXSIZE.set, None, u' Scaling of pixels with which\n                                CDELT1 is multiplied [None] ')


    _ElementMap = config._ElementMap.copy()
    _ElementMap.update({
        __VERBOSE.name() : __VERBOSE,
        __MIN_OBJ.name() : __MIN_OBJ,
        __MIN_PHOTS.name() : __MIN_PHOTS,
        __YPIXSIZE.name() : __YPIXSIZE,
        __FLAG_MASK.name() : __FLAG_MASK,
        __RMS_TOL.name() : __RMS_TOL,
        __XMIN.name() : __XMIN,
        __SEL_MIN.name() : __SEL_MIN,
        __MAX_OFFSET.name() : __MAX_OFFSET,
        __AFFINE_PARS.name() : __AFFINE_PARS,
        __PHOT.name() : __PHOT,
        __YMAX.name() : __YMAX,
        __YMIN.name() : __YMIN,
        __POS_ERROR.name() : __POS_ERROR,
        __XMAX.name() : __XMAX,
        __XPIXSIZE.name() : __XPIXSIZE
    })
    _AttributeMap = config._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'preastromConfig', preastromConfig)




rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=rawFrame, documentation=u' Information about the\n                                observational block [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscy'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels in the\n                                Y direction [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscypst'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels to skip\n                                in the Y direction at the edge of the data\n                                region [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanXStat'), CommonDM.dm.bas.img_stub.imStats, scope=rawFrame, documentation=u' Statistics of the overscan region\n                                in the X direction [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscxpre'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels to skip\n                                in the X direction at the edge of the chip\n                                [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Object'), CommonDM.dm.bas_stub.objectName, scope=rawFrame, documentation=u' Name of target object [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrescanYStat'), CommonDM.dm.bas.img_stub.imStats, scope=rawFrame, documentation=u' Statistics of the prescan region\n                                in the Y direction [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscypre'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels to skip\n                                in the Y direction at the edge of the chip\n                                [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Date'), pyxb.binding.datatypes.dateTime, scope=rawFrame, documentation=u' UTC date the original data file\n                                was saved [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanYStat'), CommonDM.dm.bas.img_stub.imStats, scope=rawFrame, documentation=u' Statistics of the overscan region\n                                in the Y direction [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpre'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels to skip\n                                in the X direction at the edge of the chip\n                                [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), pyxb.binding.datatypes.dateTime, scope=rawFrame, documentation=u' UTC date at the start of the\n                                observation [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscypre'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels to skip\n                                in the Y direction at the edge of the chip\n                                [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MjdObs'), pyxb.binding.datatypes.float, scope=rawFrame, documentation=u' Modified Julian date at the start\n                                of the observation (JD-2400000.5) [day] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Extension'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Extension number of this frame to\n                                be extracted from the rawFits container [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscxpst'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels to skip\n                                in the X direction at the edge of the data\n                                region [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Lst'), pyxb.binding.datatypes.float, scope=rawFrame, documentation=u' Local sidereal time at the start\n                                of the observation expressed as the number of\n                                seconds (a float) since UTC midnight [sec] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawFits'), rawFits, scope=rawFrame, documentation=u' Information about the original\n                                raw image data (multi-extension FITS) [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrescanXStat'), CommonDM.dm.bas.img_stub.imStats, scope=rawFrame, documentation=u' Statistics of the prescan region\n                                in the X direction [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Utc'), pyxb.binding.datatypes.float, scope=rawFrame, documentation=u' Universal coordinated time at the\n                                start of the observation expressed as the number\n                                of seconds (a float) since UTC midnight [sec] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpst'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels to skip\n                                in the X direction at the edge of the data\n                                region [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscx'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels in the X\n                                direction [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=rawFrame, documentation=u' Information about the\n                                observational template [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=rawFrame, documentation=u' Information about the detector\n                                chip [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscy'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels in the Y\n                                direction [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Observer'), CommonDM.dm.sys.sgs_stub.curation, scope=rawFrame, documentation=u' Information about the observer\n                                [None] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ovscx'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of overscan pixels in the\n                                X direction [pixel] '))

rawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Prscypst'), pyxb.binding.datatypes.int, scope=rawFrame, documentation=u' Number of prescan pixels to skip\n                                in the Y direction at the edge of the data\n                                region [pixel] '))
rawFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
rawFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawFits')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extension')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observer')), min_occurs=1, max_occurs=1),
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
    pyxb.binding.content.ParticleModel(rawFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
rawFrame._ContentModel = pyxb.binding.content.ParticleModel(rawFrame._GroupModel, min_occurs=1, max_occurs=1)



saturatedPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ThresholdLow'), pyxb.binding.datatypes.float, scope=saturatedPixelMapParameters, documentation=u' Lower threshold for rejecting pixels with\n                        outlying values [None] '))

saturatedPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ThresholdHigh'), pyxb.binding.datatypes.float, scope=saturatedPixelMapParameters, documentation=u' Upper threshold for rejecting pixels with\n                        outlying values [None] '))

saturatedPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=saturatedPixelMapParameters, documentation=u' Unique EXT object identifier [None] '))
saturatedPixelMapParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(saturatedPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(saturatedPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ThresholdLow')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(saturatedPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ThresholdHigh')), min_occurs=1, max_occurs=1)
    )
saturatedPixelMapParameters._ContentModel = pyxb.binding.content.ParticleModel(saturatedPixelMapParameters._GroupModel, min_occurs=1, max_occurs=1)



pixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Count'), pyxb.binding.datatypes.int, scope=pixelMap, documentation=u' Number of pixels marked as bad\n                                (flagged) [None] '))
pixelMap._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
pixelMap._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
pixelMap._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._GroupModel_3, min_occurs=1, max_occurs=1)
    )
pixelMap._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Count')), min_occurs=1, max_occurs=1)
    )
pixelMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelMap._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelMap._GroupModel_4, min_occurs=1, max_occurs=1)
    )
pixelMap._ContentModel = pyxb.binding.content.ParticleModel(pixelMap._GroupModel, min_occurs=1, max_occurs=1)



saturatedPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), saturatedPixelMapParameters, scope=saturatedPixelMap, documentation=u' Processing and verification\n                                parameters [None] '))

saturatedPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Raw'), rawFrame, scope=saturatedPixelMap, documentation=u' Information about the input raw\n                                science frame [None] '))
saturatedPixelMap._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(saturatedPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(saturatedPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(saturatedPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(saturatedPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
saturatedPixelMap._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(saturatedPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
saturatedPixelMap._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(saturatedPixelMap._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(saturatedPixelMap._GroupModel_4, min_occurs=1, max_occurs=1)
    )
saturatedPixelMap._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(saturatedPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Count')), min_occurs=1, max_occurs=1)
    )
saturatedPixelMap._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(saturatedPixelMap._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(saturatedPixelMap._GroupModel_5, min_occurs=1, max_occurs=1)
    )
saturatedPixelMap._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(saturatedPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Raw')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(saturatedPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
saturatedPixelMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(saturatedPixelMap._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(saturatedPixelMap._GroupModel_6, min_occurs=1, max_occurs=1)
    )
saturatedPixelMap._ContentModel = pyxb.binding.content.ParticleModel(saturatedPixelMap._GroupModel, min_occurs=1, max_occurs=1)



hotPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bias'), biasFrame, scope=hotPixelMap, documentation=u' Information about the detector\n                                bias offset levels [None] '))

hotPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=hotPixelMap, documentation=u' Information about the\n                                observational block [None] '))

hotPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), sextractorConfig, scope=hotPixelMap, documentation=u' SExtractor configuration for\n                                background determination [None] '))

hotPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=hotPixelMap, documentation=u' Information about the\n                                observational template [None] '))

hotPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=hotPixelMap, documentation=u' Information about the detector\n                                chip [None] '))

hotPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), hotPixelMapParameters, scope=hotPixelMap, documentation=u' Processing and verification\n                                parameters [None] '))

hotPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=hotPixelMap, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

hotPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=hotPixelMap, documentation=u' Information about the acquisition\n                                instrument [None] '))

hotPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=hotPixelMap, documentation=u' UTC date of the ending of the\n                                valid period [None] '))
hotPixelMap._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
hotPixelMap._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
hotPixelMap._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hotPixelMap._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._GroupModel_4, min_occurs=1, max_occurs=1)
    )
hotPixelMap._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Count')), min_occurs=1, max_occurs=1)
    )
hotPixelMap._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hotPixelMap._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._GroupModel_5, min_occurs=1, max_occurs=1)
    )
hotPixelMap._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bias')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexConfig')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
hotPixelMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hotPixelMap._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMap._GroupModel_6, min_occurs=1, max_occurs=1)
    )
hotPixelMap._ContentModel = pyxb.binding.content.ParticleModel(hotPixelMap._GroupModel, min_occurs=1, max_occurs=1)



coldPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flat'), baseFlatFrame, scope=coldPixelMap, documentation=u' Information about the detector\n                                sensitivity variations [None] '))

coldPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), sextractorConfig, scope=coldPixelMap, documentation=u' SExtractor configuration for\n                                background determination [None] '))

coldPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=coldPixelMap, documentation=u' Information about the\n                                observational filter [None] '))

coldPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=coldPixelMap, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

coldPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), coldPixelMapParameters, scope=coldPixelMap, documentation=u' Processing and verification\n                                parameters [None] '))

coldPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=coldPixelMap, documentation=u' Information about the acquisition\n                                instrument [None] '))

coldPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=coldPixelMap, documentation=u' Information about the\n                                observational template [None] '))

coldPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=coldPixelMap, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

coldPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=coldPixelMap, documentation=u' Information about the detector\n                                chip [None] '))

coldPixelMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=coldPixelMap, documentation=u' Information about the\n                                observational block [None] '))
coldPixelMap._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
coldPixelMap._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
coldPixelMap._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coldPixelMap._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._GroupModel_4, min_occurs=1, max_occurs=1)
    )
coldPixelMap._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Count')), min_occurs=1, max_occurs=1)
    )
coldPixelMap._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coldPixelMap._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._GroupModel_5, min_occurs=1, max_occurs=1)
    )
coldPixelMap._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexConfig')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
coldPixelMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coldPixelMap._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMap._GroupModel_6, min_occurs=1, max_occurs=1)
    )
coldPixelMap._ContentModel = pyxb.binding.content.ParticleModel(coldPixelMap._GroupModel, min_occurs=1, max_occurs=1)



baseFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=baseFlatFrame, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

baseFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=baseFlatFrame, documentation=u' Information about the\n                                observational filter [None] '))

baseFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=baseFlatFrame, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

baseFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=baseFlatFrame, documentation=u' Information about the detector\n                                chip [None] '))
baseFlatFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
baseFlatFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
baseFlatFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFlatFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
baseFlatFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
baseFlatFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFlatFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
baseFlatFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
baseFlatFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseFlatFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseFlatFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
baseFlatFrame._ContentModel = pyxb.binding.content.ParticleModel(baseFlatFrame._GroupModel, min_occurs=1, max_occurs=1)



masterFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hot'), hotPixelMap, scope=masterFlatFrame, documentation=u' Information about the detector\n                                hot pixels [None] '))

masterFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TwilightFlat'), twilightFlatFrame, scope=masterFlatFrame, documentation=u' Information about the input\n                                twilight flat frame [None] '))

masterFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cold'), coldPixelMap, scope=masterFlatFrame, documentation=u' Information about the detector\n                                cold pixels [None] '))

masterFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DomeFlat'), domeFlatFrame, scope=masterFlatFrame, documentation=u' Information about the input dome\n                                flat frame [None] '))

masterFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NightSkyFlat'), nightSkyFlatFrame, scope=masterFlatFrame, documentation=u' Information about the input\n                                night-sky flat frame [None] '))

masterFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), masterFlatFrameParameters, scope=masterFlatFrame, documentation=u' Processing and verification\n                                parameters [None] '))
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
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DomeFlat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TwilightFlat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NightSkyFlat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hot')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
masterFlatFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
masterFlatFrame._ContentModel = pyxb.binding.content.ParticleModel(masterFlatFrame._GroupModel, min_occurs=1, max_occurs=1)



illuminationCorrectionFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IlluminationCorrection'), illuminationCorrection, scope=illuminationCorrectionFrame, documentation=u' Information about the\n                                illumination correction [None] '))

illuminationCorrectionFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=illuminationCorrectionFrame, documentation=u' Information about the\n                                observational filter [None] '))

illuminationCorrectionFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=illuminationCorrectionFrame, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

illuminationCorrectionFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=illuminationCorrectionFrame, documentation=u' Information about the detector\n                                chip [None] '))

illuminationCorrectionFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=illuminationCorrectionFrame, documentation=u' UTC date of the ending of the\n                                valid period [None] '))
illuminationCorrectionFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IlluminationCorrection')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
illuminationCorrectionFrame._ContentModel = pyxb.binding.content.ParticleModel(illuminationCorrectionFrame._GroupModel, min_occurs=1, max_occurs=1)



baseAtmosphericExtinction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=baseAtmosphericExtinction, documentation=u' Information about the acquisition\n                                instrument [None] '))

baseAtmosphericExtinction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtinctionCurve'), photExtinctionCurve, scope=baseAtmosphericExtinction, documentation=u' Information about the atmospheric\n                                extinction curve [None] '))

baseAtmosphericExtinction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.float, scope=baseAtmosphericExtinction, documentation=u' Value of the atmospheric\n                                extinction [mag / airmass]'))

baseAtmosphericExtinction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=baseAtmosphericExtinction, documentation=u' Information about the\n                                observational filter [None] '))

baseAtmosphericExtinction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Error'), pyxb.binding.datatypes.float, scope=baseAtmosphericExtinction, documentation=u' Error on atmospheric extinction\n                                [mag / airmass]'))

baseAtmosphericExtinction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagId'), CommonDM.dm.bas.dtd_stub.nameRestriction, scope=baseAtmosphericExtinction, documentation=u' Identifier for the photometric\n                                band [None]'))
baseAtmosphericExtinction._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
baseAtmosphericExtinction._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Error')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtinctionCurve')), min_occurs=1, max_occurs=1)
    )
baseAtmosphericExtinction._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._GroupModel_2, min_occurs=1, max_occurs=1)
    )
baseAtmosphericExtinction._ContentModel = pyxb.binding.content.ParticleModel(baseAtmosphericExtinction._GroupModel, min_occurs=1, max_occurs=1)



atmosphericExtinction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), atmosphericExtinctionParameters, scope=atmosphericExtinction, documentation=u' Processing and verification\n                                parameters [None] '))

atmosphericExtinction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Polar'), photSrcCatalog, scope=atmosphericExtinction, documentation=u' List of input photometric source\n                                catalogs [none] '))
atmosphericExtinction._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
atmosphericExtinction._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Error')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtinctionCurve')), min_occurs=1, max_occurs=1)
    )
atmosphericExtinction._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinction._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._GroupModel_3, min_occurs=1, max_occurs=1)
    )
atmosphericExtinction._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Polar')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
atmosphericExtinction._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinction._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinction._GroupModel_4, min_occurs=1, max_occurs=1)
    )
atmosphericExtinction._ContentModel = pyxb.binding.content.ParticleModel(atmosphericExtinction._GroupModel, min_occurs=1, max_occurs=1)



reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=reducedScienceFrameParameters, documentation=u' Unique EXT object identifier [None] '))

reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdHigh'), pyxb.binding.datatypes.float, scope=reducedScienceFrameParameters, documentation=u' Upper bound of fringed pixels to include\n                        in scaling [ADU] '))

reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), pyxb.binding.datatypes.int, scope=reducedScienceFrameParameters, documentation=u' Overscan correction method index [None] '))

reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImageThreshold'), pyxb.binding.datatypes.float, scope=reducedScienceFrameParameters, documentation=u' Pixel value Sigma-clipping threshold to\n                        estimate source-free background for scaling of fringe\n                        frames [None] '))

reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdLow'), pyxb.binding.datatypes.float, scope=reducedScienceFrameParameters, documentation=u' Lower bound of fringed pixels to include\n                        in scaling [ADU] '))

reducedScienceFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=reducedScienceFrameParameters, documentation=u' Version of the source code [None] '))
reducedScienceFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdLow')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FringeThresholdHigh')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImageThreshold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
reducedScienceFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(reducedScienceFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



zeroPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.float, scope=zeroPoint, documentation=u' Value of the photometric zeropoint [mag] '))

zeroPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Error'), pyxb.binding.datatypes.float, scope=zeroPoint, documentation=u' Error on the value of the photometric\n                        zeropoint [mag] '))

zeroPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=zeroPoint, documentation=u' Unique EXT object identifier [None] '))
zeroPoint._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(zeroPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(zeroPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(zeroPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Error')), min_occurs=1, max_occurs=1)
    )
zeroPoint._ContentModel = pyxb.binding.content.ParticleModel(zeroPoint._GroupModel, min_occurs=1, max_occurs=1)



rawTwilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=rawTwilightFlatFrameParameters, documentation=u' Unique EXT object identifier [None] '))

rawTwilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxFlatMean'), pyxb.binding.datatypes.int, scope=rawTwilightFlatFrameParameters, documentation=u' QC: Maximum level of the flat (mean of\n                        the flat pixel values) [ADU] '))

rawTwilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinFlatMean'), pyxb.binding.datatypes.int, scope=rawTwilightFlatFrameParameters, documentation=u' QC: Minimum level of the flat (mean of\n                        the flat pixel values) [ADU] '))

rawTwilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=rawTwilightFlatFrameParameters, documentation=u' Version of the source code [None] '))
rawTwilightFlatFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinFlatMean')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxFlatMean')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
rawTwilightFlatFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(rawTwilightFlatFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



illuminationCorrectionRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ChipName'), pyxb.binding.datatypes.string, scope=illuminationCorrectionRecord, documentation=u' Name of the detector chip [None] '))

illuminationCorrectionRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitParameters'), pyxb.binding.datatypes.float, scope=illuminationCorrectionRecord, documentation=u' List of fit parameters [None] '))

illuminationCorrectionRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=illuminationCorrectionRecord, documentation=u' Unique EXT object identifier [None] '))
illuminationCorrectionRecord._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ChipName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FitParameters')), min_occurs=1L, max_occurs=None)
    )
illuminationCorrectionRecord._ContentModel = pyxb.binding.content.ParticleModel(illuminationCorrectionRecord._GroupModel, min_occurs=1, max_occurs=1)



photRefCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Storage'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=photRefCatalog, documentation=u' Customized storage container for the data\n                        [None] '))

photRefCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), pyxb.binding.datatypes.dateTime, scope=photRefCatalog, documentation=u' UTC date this object was created [None] '))

photRefCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=photRefCatalog, documentation=u' Unique EXT object identifier [None] '))
photRefCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photRefCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photRefCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photRefCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1)
    )
photRefCatalog._ContentModel = pyxb.binding.content.ParticleModel(photRefCatalog._GroupModel, min_occurs=1, max_occurs=1)



astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_4'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,4 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AstromConfig'), astromConfig, scope=astrometricParameters, documentation=u' LDAC.astrom configuration [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRVAL2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Physical value of the reference\n                                pixel Y [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaDdecOverlap'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Sample standard deviation of\n                                overlap residuals in declination [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_0'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value c0 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_7'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,7 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Gastrom'), gAstrometric, scope=astrometricParameters, documentation=u' Information about the global\n                                astrometric solution [None]'))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Error in polynomial X coefficient\n                                [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CTYPE1'), pyxb.binding.datatypes.string, scope=astrometricParameters, documentation=u' Pixel coordinate system and\n                                projection of first axis (X) [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=astrometricParameters, documentation=u' Information about the\n                                observational template [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_5'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,5 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NRef'), pyxb.binding.datatypes.int, scope=astrometricParameters, documentation=u' Number of reference pairings used\n                                in the astrometric solution [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=astrometricParameters, documentation=u' Information about the\n                                observational filter [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_6'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,6 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_3'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,3 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociateConfig'), associateConfig, scope=astrometricParameters, documentation=u' LDAC.associate configuration\n                                [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,2 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NFitParm'), pyxb.binding.datatypes.int, scope=astrometricParameters, documentation=u' Number of fitted parameters\n                                [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD1_2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Linear transformation matrix\n                                parameter at i,j=1,2 (a2) [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_6'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,6 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=astrometricParameters, documentation=u' Information about the\n                                observational block [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitParams'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Degrees of freedom of fitted\n                                parameters [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_4'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,4 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD2_1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Linear transformation matrix\n                                parameter at i,j=2,1 (b1) [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_9'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,9 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CTYPE2'), pyxb.binding.datatypes.string, scope=astrometricParameters, documentation=u' Pixel coordinate system and\n                                projection of second axis (Y) [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_9'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,9 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=astrometricParameters, documentation=u' Information about the acquisition\n                                instrument [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitErrors'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Errors on fitted parameters [rad] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD2_2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Linear transformation matrix\n                                parameter at i,j=2,2 (b2) [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD1_1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Linear transformation matrix\n                                parameter at i,j=1,1 (a1) [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FieldError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Global position error [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), sextractorConfig, scope=astrometricParameters, documentation=u' SExtractor configuration for\n                                source extraction [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_10'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,10 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MeanDraOverlap'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Average overlap residual in right\n                                ascension [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_10'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,10 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,1 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_8'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,8 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_8'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,8 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NOverlap'), pyxb.binding.datatypes.int, scope=astrometricParameters, documentation=u' Number of overlap pairings used\n                                in the astrometric solution [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MeanDdecOverlap'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Average overlap residual in\n                                declination [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaDra'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Sample standard deviation of\n                                reference residuals in right ascension [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), astrometricParametersParameters, scope=astrometricParameters, documentation=u' Processing and verification\n                                parameters [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MeanDra'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Average reference residual in\n                                right ascension [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRVAL1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Physical value of the reference\n                                pixel X [deg] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRPIX2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Reference pixel in Y [pixel] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YyError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Error in polynomial YY\n                                coefficient [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaDdec'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Sample standard deviation of\n                                reference residuals in declination [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Error in polynomial Y coefficient\n                                [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaDraOverlap'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Sample standard deviation of\n                                overlap residuals in right ascension [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Rms'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Two-dimensional root-mean-square\n                                of reference residuals [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,1 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_2'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,2 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_0'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value a0 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XxError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Error in polynomial XX\n                                coefficient [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV1_7'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value b1,7 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Estimate of seeing using the\n                                median FWHM (filtered to isolate most\n                                stellar-like sources) [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_3'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,3 [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRPIX1'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Reference pixel in X [pixel] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MeanDdec'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Average reference residual in\n                                declination [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=astrometricParameters, documentation=u' Information about the detector\n                                chip [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RefcatSlid'), pyxb.binding.datatypes.int, scope=astrometricParameters, documentation=u' The ID of the source list used\n                                for the reference catalog [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PreastromConfig'), preastromConfig, scope=astrometricParameters, documentation=u' LDAC.preastrom configuration\n                                [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XyError'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Error in polynomial XY\n                                coefficient [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reduced'), CommonDM.dm.bas.img_stub.baseFrame, scope=astrometricParameters, documentation=u' Information about the input\n                                reduced science frame [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RmsOverlap'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Two-dimensional root-mean-square\n                                of overlap residuals [arcsec] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Residuals'), pyxb.binding.datatypes.string, scope=astrometricParameters, documentation=u' Filename of residuals FITS table\n                                [None] '))

astrometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PV2_5'), pyxb.binding.datatypes.float, scope=astrometricParameters, documentation=u' Non-linear transformation matrix\n                                parameter value d1,5 [None] '))
astrometricParameters._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
astrometricParameters._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RefcatSlid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reduced')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Gastrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexConfig')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PreastromConfig')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AssociateConfig')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AstromConfig')), min_occurs=1, max_occurs=1),
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
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Residuals')), min_occurs=1, max_occurs=1)
    )
astrometricParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astrometricParameters._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParameters._GroupModel_2, min_occurs=1, max_occurs=1)
    )
astrometricParameters._ContentModel = pyxb.binding.content.ParticleModel(astrometricParameters._GroupModel, min_occurs=1, max_occurs=1)



cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hot'), hotPixelMap, scope=cosmicMap, documentation=u' Information about the detector\n                                hot pixels [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), cosmicMapSexParameters, scope=cosmicMap, documentation=u' Processing and verification\n                                parameters [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Frame'), CommonDM.dm.bas.img_stub.baseFrame, scope=cosmicMap, documentation=u' Information about the input\n                                reduced science frame [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Gain'), gainLinearity, scope=cosmicMap, documentation=u' Information about the detector\n                                gain [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cold'), coldPixelMap, scope=cosmicMap, documentation=u' Information about the detector\n                                cold pixels [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=cosmicMap, documentation=u' Information about the acquisition\n                                instrument [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Saturated'), saturatedPixelMap, scope=cosmicMap, documentation=u' Information about saturated\n                                pixels [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=cosmicMap, documentation=u' Information about the detector\n                                chip [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flat'), masterFlatFrame, scope=cosmicMap, documentation=u' Information about the detector\n                                sensitivity variations [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CosmicCount'), pyxb.binding.datatypes.int, scope=cosmicMap, documentation=u' Number of cosmic ray events (not\n                                affected pixels) [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=cosmicMap, documentation=u' Information about the\n                                observational filter [None] '))

cosmicMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), illuminationCorrectionFrame, scope=cosmicMap, documentation=u' Information about the\n                                illumination correction [None] '))
cosmicMap._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_4, min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Count')), min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_5, min_occurs=1, max_occurs=1)
    )
cosmicMap._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Saturated')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hot')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cold')), min_occurs=1, max_occurs=1),
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
    pyxb.binding.content.ParticleModel(cosmicMap._GroupModel_6, min_occurs=1, max_occurs=1)
    )
cosmicMap._ContentModel = pyxb.binding.content.ParticleModel(cosmicMap._GroupModel, min_occurs=1, max_occurs=1)



gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Gain'), pyxb.binding.datatypes.float, scope=gainLinearity, documentation=u' Value of the gain measurement\n                                (ADU conversion factor) [electron / ADU] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=gainLinearity, documentation=u' Information about the\n                                observational template [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=gainLinearity, documentation=u' Information about the detector\n                                chip [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=gainLinearity, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bias'), biasFrame, scope=gainLinearity, documentation=u' Information about the detector\n                                bias offset levels [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureTimes'), pyxb.binding.datatypes.float, scope=gainLinearity, documentation=u' List of exposure times of the\n                                dome flat frames [second] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=gainLinearity, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawDomeFlatFrames'), rawDomeFlatFrame, scope=gainLinearity, documentation=u' List of input raw dome flat\n                                frames [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RmsDiff'), pyxb.binding.datatypes.float, scope=gainLinearity, documentation=u' List of raw measurements of\n                                sample standard deviation of pixel values of the\n                                subtracted dome flat frames [ADU] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=gainLinearity, documentation=u' Information about the\n                                observational block [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureLevels'), pyxb.binding.datatypes.float, scope=gainLinearity, documentation=u' List of exposure levels (median\n                                pixel value of each dome flat frame) [ADU] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=gainLinearity, documentation=u' Information about the acquisition\n                                instrument [None] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MedianSum'), pyxb.binding.datatypes.float, scope=gainLinearity, documentation=u' List of raw measurements of\n                                median pixel values of the added dome flat\n                                frames [ADU] '))

gainLinearity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), gainLinearityParameters, scope=gainLinearity, documentation=u' Processing and verification\n                                parameters [None] '))
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
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawDomeFlatFrames')), min_occurs=2L, max_occurs=None),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bias')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
gainLinearity._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(gainLinearity._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gainLinearity._GroupModel_4, min_occurs=1, max_occurs=1)
    )
gainLinearity._ContentModel = pyxb.binding.content.ParticleModel(gainLinearity._GroupModel, min_occurs=1, max_occurs=1)



fringeFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=fringeFrameParameters, documentation=u' Version of the source code [None] '))

fringeFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), pyxb.binding.datatypes.int, scope=fringeFrameParameters, documentation=u' Overscan correction method index [None] '))

fringeFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=fringeFrameParameters, documentation=u' Unique EXT object identifier [None] '))
fringeFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fringeFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
fringeFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(fringeFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



cosmicMapSexParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=cosmicMapSexParameters, documentation=u' Unique EXT object identifier [None] '))

cosmicMapSexParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectionThreshold'), pyxb.binding.datatypes.float, scope=cosmicMapSexParameters, documentation=u' Threshold for detecting pixels with\n                        cosmic ray events [None] '))
cosmicMapSexParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicMapSexParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cosmicMapSexParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectionThreshold')), min_occurs=1, max_occurs=1)
    )
cosmicMapSexParameters._ContentModel = pyxb.binding.content.ParticleModel(cosmicMapSexParameters._GroupModel, min_occurs=1, max_occurs=1)



sourceListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HtmDepth'), pyxb.binding.datatypes.int, scope=sourceListParameters, documentation=u' Highest level of HTM indexing [None] '))

sourceListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=sourceListParameters, documentation=u' Version of the source code [None] '))

sourceListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=sourceListParameters, documentation=u' Unique EXT object identifier [None] '))
sourceListParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sourceListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HtmDepth')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
sourceListParameters._ContentModel = pyxb.binding.content.ParticleModel(sourceListParameters._GroupModel, min_occurs=1, max_occurs=1)



sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'B'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Semi-minor axis of profile [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_AUTO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Kron-like elliptical aperture magnitude\n                        [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'THETAWCS'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Ellipse position angle [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'A_WCS'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Semi-major axis of profile [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FIELD_POS'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Observation index for multi-observation\n                        source lists [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XM2'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Variance along X [pixel**2] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_APER'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error vector for fixed aperture\n                        magnitude [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'B_WCS'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Semi-minor axis of profile [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_AUTO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error for AUTO flux [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUX_ISO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Isophotal flux [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BackGr'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Background level around a source [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_ISO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error for isophotal magnitude [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUX_RADIUS'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Fraction-of-light radius [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEC'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Declination [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CLASS_STAR'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Star/galaxy classifier index [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUX_APER'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Flux vector within fixed circular\n                        aperture(s) [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_APER'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error vector for aperture flux(es)\n                        [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SeqNr'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Index of extracted source [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Corr'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Covariance between X and Y [pixel**2] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'A'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Semi-major axis of profile [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SID'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Identifier of a source in the source list\n                        [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YM2'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Variance along Y [pixel**2] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MU_MAX'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Peak surface brightness above background\n                        [mag / arcsec**2] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_ISO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Isophotal magnitude [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUXERR_ISO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error for isophotal flux [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ERRB_IMAGE'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Error on measurement of semi-minor axis\n                        of profile [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLID'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Identifier of the source list [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FWHM_IMAGE'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Full width at half maximum assuming a\n                        gaussian core [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAGERR_AUTO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' RMS error for AUTO magnitude [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ERRTHETA_IMAGE'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Error on measurement of ellipse position\n                        angle [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ypos'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Source position along Y [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RA'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Right Ascension [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HTM'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Index of HTM (Hierarchical Triangular\n                        Mesh) [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ERRA_IMAGE'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Error on measurement of semi-major axis\n                        of profile [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'POSANG'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Ellipse position angle [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PosErr'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Positional error of extraction (measured\n                        semi-major axis) [deg] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxVal'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Peak flux above background [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_APER'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Fixed aperture magnitude vector [mag] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Level'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Level of detection threshold above\n                        background [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Source extraction flags [None] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLUX_AUTO'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Flux within a Kron-like elliptical\n                        aperture [count] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Xpos'), pyxb.binding.datatypes.float, scope=sourceListDict, documentation=u' Source position along X [pixel] '))

sourceListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NPIX'), pyxb.binding.datatypes.int, scope=sourceListDict, documentation=u' Isophotal area above analysis threshold\n                        [pixel**2] '))
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



config._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=config, documentation=u' Unique EXT object identifier [None] '))
config._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(config._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1)
    )
config._ContentModel = pyxb.binding.content.ParticleModel(config._GroupModel, min_occurs=1, max_occurs=1)



sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FILTER_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Name of file contianing the\n                                filter definition [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Filename for the check-image\n                                [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Verbosity level (QUIET, NORMAL,\n                                EXTRA_WARNINGS, FULL) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CLEAN_PARAM'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' Efficiency of cleaning [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOPARAMS'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' List of MAG_AUTO controls\n                                (scaling parameter k of the first order moment\n                                and minimum R_min in units of A and B) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ANALYSIS_THRESH'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' Threshold at which CLASS_STAR and\n                                FWHM_ operate [mag / arcsec^2] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Combination method for flags on\n                                the same object (OR, AND, MIN, MAX, MOST) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SEEING_FWHM'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' FWHM of stellar sources (for\n                                star/galaxy separation only) [arcsec] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CLEAN'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Clean the catalog before writing\n                                to disk (Y, N) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Type of information to put in the\n                                check-image (NONE, IDENTICAL, BACKGROUND,\n                                BACKGROUND_RMS, MINIBACKGROUND, MINIBACK_RMS,\n                                -BACKGROUND, FILTERED, OBJECTS, -OBJECTS,\n                                APERTURES, SEGMENTATION) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE'), pyxb.binding.datatypes.int, scope=sextractorConfig, documentation=u' Size of background filtering mask\n                                [background mesh] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_THICK'), pyxb.binding.datatypes.int, scope=sextractorConfig, documentation=u' Thickness of the background LOCAL\n                                annulus [pixel] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' Pixel size [arcsec / pixel] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'THRESH_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Meaning of DETECT_THRESH and\n                                ANALYSIS_THRESH parameters (RELATIVE, ABSOLUTE)\n                                [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_GAMMA'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' Gamma of the emulsion (when\n                                DETECT_TYPE is PHOTO) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE'), pyxb.binding.datatypes.int, scope=sextractorConfig, documentation=u' Size of a background mesh [pixel] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SATUR_LEVEL'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' Pixel value above which it is\n                                considered saturated [count] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Background used to compute\n                                magnitudes (GLOBAL, LOCAL) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Weighting scheme for weight-image\n                                (NONE, BACKGROUND, MAP_RMS, MAP_VAR, MAP_WEIGHT)\n                                [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_NTHRESH'), pyxb.binding.datatypes.int, scope=sextractorConfig, documentation=u' Number of deblending\n                                sub-thresholds [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOAPERS'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' List of MAG_AUTO minimum circular\n                                aperture diameters (estimation disk, measurement\n                                disk) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MASK_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Method of masking of neighbors\n                                for photometry (NONE, BLANK, CORRECT) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG_IMAGE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Filename of the flag-image [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DETECT_MINAREA'), pyxb.binding.datatypes.int, scope=sextractorConfig, documentation=u' Minimum number of pixels above\n                                threshold triggering detection [pixel] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_BUFSIZE'), pyxb.binding.datatypes.int, scope=sextractorConfig, documentation=u' Number of scan-lines in the image\n                                buffer [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_MINCONT'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' Minimum contrast parameter for\n                                deblending [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DETECT_THRESH'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' Detection threshold relative to\n                                background RMS (when THRESH_TYPE is RELATIVE)\n                                [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GAIN'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' Conversion factor used for error\n                                estimates of CCD magnitudes [electron / ADU] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_OBJSTACK'), pyxb.binding.datatypes.int, scope=sextractorConfig, documentation=u' Maximum number of objects that\n                                the object-stack can contain [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_VALUE'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' List of constant values to be\n                                subtracted from the images if BACK_TYPE is\n                                MANUAL [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'STARNNW_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Name of the file containing the\n                                neural-network weights for star/galaxy\n                                separation [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DETECT_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Type of device that produced the\n                                image (CCD, PHOTO) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHOT_APERTURES'), pyxb.binding.datatypes.int, scope=sextractorConfig, documentation=u' MAG_APER aperture diameter\n                                [pixel] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Name of the output catalog [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_ZEROPOINT'), pyxb.binding.datatypes.float, scope=sextractorConfig, documentation=u' Zero-point offset to be applied\n                                to magnitudes [mag] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FILTER'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Apply filtering to the data\n                                before extraction (Y, N) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Filename of the detection and\n                                measurement weight-image [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Format of the output catalog\n                                (ASCII, ASCII_HEAD, ASCII_SKYCAT, ASCII_VOTABLE,\n                                FITS_1.0, FITS_LDAC) [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_PIXSTACK'), pyxb.binding.datatypes.int, scope=sextractorConfig, documentation=u' Maximum number of pixels that the\n                                pixel-stack can contain [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PARAMETERS_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Name of the file containing the\n                                list of parameters that will be computed and put\n                                into the catalog for each object [None] '))

sextractorConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfig, documentation=u' Type of background subtracted\n                                from the images (AUTO, MANUAL) [None] '))
sextractorConfig._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1)
    )
sextractorConfig._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ANALYSIS_THRESH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_THICK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_VALUE')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CLEAN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CLEAN_PARAM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_MINCONT')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_NTHRESH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DETECT_MINAREA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DETECT_THRESH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DETECT_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FILTER')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FILTER_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLAG_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLAG_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GAIN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAG_GAMMA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAG_ZEROPOINT')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MASK_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_BUFSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_OBJSTACK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_PIXSTACK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PARAMETERS_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PHOT_APERTURES')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOPARAMS')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOAPERS')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SATUR_LEVEL')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SEEING_FWHM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'STARNNW_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'THRESH_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE')), min_occurs=1, max_occurs=1)
    )
sextractorConfig._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sextractorConfig._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfig._GroupModel_2, min_occurs=1, max_occurs=1)
    )
sextractorConfig._ContentModel = pyxb.binding.content.ParticleModel(sextractorConfig._GroupModel, min_occurs=1, max_occurs=1)



gridTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=gridTarget, documentation=u' Unique EXT object identifier [None] '))

gridTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PixelScale'), pyxb.binding.datatypes.float, scope=gridTarget, documentation=u' Pixel scale of the grid [arcsec / pixel] '))

gridTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Dec'), pyxb.binding.datatypes.float, scope=gridTarget, documentation=u' Declination of target reference pixel\n                        [deg] '))

gridTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ra'), pyxb.binding.datatypes.float, scope=gridTarget, documentation=u' Right Ascension of target reference pixel\n                        [deg] '))
gridTarget._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(gridTarget._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gridTarget._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ra')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gridTarget._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gridTarget._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PixelScale')), min_occurs=1, max_occurs=1)
    )
gridTarget._ContentModel = pyxb.binding.content.ParticleModel(gridTarget._GroupModel, min_occurs=1, max_occurs=1)



swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SUBTRACT_BACK'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Background-subtract images prior\n                                to resampling [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OVERSAMPLING'), pyxb.binding.datatypes.int, scope=swarpConfig, documentation=u' Amount of oversampling in each\n                                dimension [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Type of input weight map (NONE,\n                                MAP_WEIGHT, MAP_VARIANCE, MAP_RMS) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CELESTIAL_TYPE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Celestial coordinate system in\n                                output (NATIVE, PIXEL, EQUATORIAL, GALACTIC,\n                                ECLIPTIC) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PROJECTION_TYPE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Projection system used in output\n                                in standard WCS notation (AZP, TAN, STG, SIN,\n                                ARC, ZPN, ZEA, AIR, CYP, CEA, CAR, MER, COP,\n                                COE, COD, COO, BON, PCO, GLS, PAR, MOL, AIT,\n                                TCS, CSC, QSC) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLE_SUFFIX'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Extension of the resampled images\n                                [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IMAGEOUT_NAME'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Filename of output image [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CENTER_TYPE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' The way the output frame is\n                                centered (ALL, MOST, MANUAL) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VMEM_DIR'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Path of the directory where\n                                virtual-memory and other temporary files are\n                                written [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FSCALASTRO_TYPE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' How to compute the astrometric\n                                part of the flux scaling (NONE, FIXED) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CENTER'), pyxb.binding.datatypes.float, scope=swarpConfig, documentation=u' List of positions of center in\n                                CENTER_TYPE MANUAL mode [deg] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PIXELSCALE_TYPE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' How the output pixel size is set\n                                (MEDIAN, MIN, MAX, MANUAL, FIT) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HEADER_ONLY'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Only create the header in the\n                                combined image (Y, N) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WEIGHTOUT_NAME'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Filename of the output weight-map\n                                [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEM_MAX'), pyxb.binding.datatypes.int, scope=swarpConfig, documentation=u' Maximum amount of megabytes\n                                allowed for RAM storage [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FSCALE_DEFAULT'), pyxb.binding.datatypes.float, scope=swarpConfig, documentation=u' List of default flux scales to\n                                adopt if FSCALE_KEYWORD nonexistent [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IMAGE_SIZE'), pyxb.binding.datatypes.int, scope=swarpConfig, documentation=u' Dimensions of the output image\n                                [pixel] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLE_DIR'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Path of the directory where the\n                                resampled images are written [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE'), pyxb.binding.datatypes.float, scope=swarpConfig, documentation=u' Step between pixels in each\n                                dimension [arcsec / pixel] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HEADER_SUFFIX'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Extension of the replacement\n                                header files [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GAIN_KEYWORD'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' FITS keyword containing the gain\n                                in input images [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DELETE_TMPFILES'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Delete temporary image files\n                                [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GAIN_DEFAULT'), pyxb.binding.datatypes.float, scope=swarpConfig, documentation=u' Default gain to adopt if\n                                GAIN_KEYWORD nonexistent [electron / ADU] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE'), pyxb.binding.datatypes.int, scope=swarpConfig, documentation=u' Size of background filtering mask\n                                in factors of BACK_SIZE [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_DEFAULT'), pyxb.binding.datatypes.float, scope=swarpConfig, documentation=u' Default background to be\n                                subtracted in BACK_TYPE MANUAL mode [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Resample the input images (Y, N)\n                                [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NTHREADS'), pyxb.binding.datatypes.int, scope=swarpConfig, documentation=u' Number of threads to run\n                                simultaneously during resampling (0 is\n                                automatic) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' List of filenames of input weight\n                                maps [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VMEM_MAX'), pyxb.binding.datatypes.int, scope=swarpConfig, documentation=u' Maximum amount of megabytes\n                                allowed for virtual-memory storage [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WRITE_FILEINFO'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Write extended information from\n                                input images to output images [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'COMBINE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Combine resampled images (Y, N)\n                                [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'INTERPOLATE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Interpolate upon resampling (Y,\n                                N) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_SUFFIX'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Extension of the input weight\n                                maps [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Type of background to subtract\n                                (AUTO, MANUAL) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Verbosity level (QUIET, NORMAL,\n                                FULL) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'COMBINE_BUFSIZE'), pyxb.binding.datatypes.int, scope=swarpConfig, documentation=u' Amount of megabytes of buffer\n                                memory used for coaddition [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'COMBINE_TYPE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Image combination method (MEDIAN,\n                                AVERAGE, MIN, MAX, WEIGHTED, CHI2, SUM) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FSCALE_KEYWORD'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' FITS keyword containing flux\n                                scale in input images [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLING_TYPE'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' Resampling method (NEAREST,\n                                BILINEAR, LANCZOS2, LANCZOS3, LANCZOS4) [None] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE'), pyxb.binding.datatypes.int, scope=swarpConfig, documentation=u' Size of a background mesh [pixel] '))

swarpConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'COPY_KEYWORDS'), pyxb.binding.datatypes.string, scope=swarpConfig, documentation=u' String containing comma-separated\n                                FITS keywords to copy to output images [None] '))
swarpConfig._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1)
    )
swarpConfig._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IMAGEOUT_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WEIGHTOUT_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HEADER_ONLY')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HEADER_SUFFIX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_SUFFIX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'COMBINE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'COMBINE_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CELESTIAL_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PROJECTION_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CENTER_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CENTER')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PIXELSCALE_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IMAGE_SIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLE_DIR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLE_SUFFIX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RESAMPLING_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OVERSAMPLING')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'INTERPOLATE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FSCALASTRO_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FSCALE_KEYWORD')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FSCALE_DEFAULT')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GAIN_KEYWORD')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GAIN_DEFAULT')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SUBTRACT_BACK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_DEFAULT')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VMEM_DIR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VMEM_MAX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEM_MAX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'COMBINE_BUFSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DELETE_TMPFILES')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'COPY_KEYWORDS')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WRITE_FILEINFO')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NTHREADS')), min_occurs=1, max_occurs=1)
    )
swarpConfig._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(swarpConfig._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(swarpConfig._GroupModel_2, min_occurs=1, max_occurs=1)
    )
swarpConfig._ContentModel = pyxb.binding.content.ParticleModel(swarpConfig._GroupModel, min_occurs=1, max_occurs=1)



weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Naxis2'), pyxb.binding.datatypes.int, scope=weightFrame, documentation=u' Length of data in axis 2 [pixel] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hot'), hotPixelMap, scope=weightFrame, documentation=u' Information about the detector\n                                hot pixels [None] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImStat'), CommonDM.dm.bas.img_stub.imStats, scope=weightFrame, documentation=u' Information about the statistics\n                                of the image pixels [None] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Satellite'), satelliteMap, scope=weightFrame, documentation=u' Information about pixels affected\n                                by satellite tracks [None] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Saturated'), saturatedPixelMap, scope=weightFrame, documentation=u' Information about saturated\n                                pixels [None] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cold'), coldPixelMap, scope=weightFrame, documentation=u' Information about the detector\n                                cold pixels [None] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Naxis1'), pyxb.binding.datatypes.int, scope=weightFrame, documentation=u' Length of data in axis 1 [pixel] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flat'), masterFlatFrame, scope=weightFrame, documentation=u' Information about the detector\n                                sensitivity variations [None] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cosmic'), cosmicMap, scope=weightFrame, documentation=u' Information about pixels affected\n                                by cosmic ray events [None] '))

weightFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), illuminationCorrectionFrame, scope=weightFrame, documentation=u' Information about the\n                                illumination correction [None] '))
weightFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_3, min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Saturated')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hot')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cosmic')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Satellite')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Illumination')), min_occurs=1, max_occurs=1)
    )
weightFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(weightFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
weightFrame._ContentModel = pyxb.binding.content.ParticleModel(weightFrame._GroupModel, min_occurs=1, max_occurs=1)



rawBiasFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), rawBiasFrameParameters, scope=rawBiasFrame, documentation=u' Processing and verification\n                                parameters [None] '))
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
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawFits')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extension')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observer')), min_occurs=1, max_occurs=1),
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
rawBiasFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
rawBiasFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
rawBiasFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
rawBiasFrame._ContentModel = pyxb.binding.content.ParticleModel(rawBiasFrame._GroupModel, min_occurs=1, max_occurs=1)



readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MedianDiff'), pyxb.binding.datatypes.float, scope=readNoise, documentation=u' Median pixel value difference\n                                between biases [ADU] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MeanDiff'), pyxb.binding.datatypes.float, scope=readNoise, documentation=u' Mean pixel value difference\n                                between biases [ADU] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=readNoise, documentation=u' Information about the\n                                observational template [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise'), pyxb.binding.datatypes.float, scope=readNoise, documentation=u' Value of readout noise\n                                measurement [ADU] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames'), rawBiasFrame, scope=readNoise, documentation=u' List of input raw bias frames\n                                [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=readNoise, documentation=u' Information about the detector\n                                chip [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=readNoise, documentation=u' Information about the\n                                observational block [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), readNoiseParameters, scope=readNoise, documentation=u' Processing and verification\n                                parameters [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=readNoise, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=readNoise, documentation=u' Information about the acquisition\n                                instrument [None] '))

readNoise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=readNoise, documentation=u' UTC date of the ending of the\n                                valid period [None] '))
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



biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumStdevDifference'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' QC: Maximum sample standard deviation\n                        difference of the bias levels relative to the previous\n                        version [ADU] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=biasFrameParameters, documentation=u' Version of the source code [None] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumAbsMean'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' QC: Maximum absolute mean value of the\n                        bias levels [ADU] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' QC: Maximum difference between median\n                        values of any two sub-windows [ADU] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), pyxb.binding.datatypes.int, scope=biasFrameParameters, documentation=u' Overscan correction method index [None] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumStdev'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' QC: Maximum sample standard deviation\n                        value of the bias levels [ADU] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinStdev'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' QC: Maximum sample standard deviation\n                        value of any sub-window [ADU] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip'), pyxb.binding.datatypes.float, scope=biasFrameParameters, documentation=u' Threshold factor for rejecting raw bias\n                        pixel value outliers (sigma is taken as the readout\n                        noise measurement) [None] '))

biasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=biasFrameParameters, documentation=u' Unique EXT object identifier [None] '))
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



associateConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ISO_COLOR_TOL'), pyxb.binding.datatypes.float, scope=associateConfig, documentation=u' Factor with which the object\n                                dimensions (second order moments) are multiplied\n                                to search for overlap between objects within the\n                                same input catalog [None] '))

associateConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE'), pyxb.binding.datatypes.string, scope=associateConfig, documentation=u' Verbosity level (NONE, NORMAL,\n                                VERBOSE, DEBUG) [None] '))

associateConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MASK'), pyxb.binding.datatypes.float, scope=associateConfig, documentation=u' SExtractor mask to select objects\n                                for astrometric pairing: Flag and FLAG_MASK\n                                [None] '))

associateConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'INTER_COLOR_TOL'), pyxb.binding.datatypes.float, scope=associateConfig, documentation=u' Factor with which the object\n                                dimensions (second order moments) are multiplied\n                                to search for overlap between objects of\n                                different input catalogs [None] '))

associateConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PAIR_COLS'), pyxb.binding.datatypes.string, scope=associateConfig, documentation=u' Enable the output of the PAIRS\n                                association column [None] '))
associateConfig._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(associateConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1)
    )
associateConfig._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(associateConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'INTER_COLOR_TOL')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ISO_COLOR_TOL')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MASK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PAIR_COLS')), min_occurs=1, max_occurs=1)
    )
associateConfig._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(associateConfig._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateConfig._GroupModel_2, min_occurs=1, max_occurs=1)
    )
associateConfig._ContentModel = pyxb.binding.content.ParticleModel(associateConfig._GroupModel, min_occurs=1, max_occurs=1)



astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NITER'), pyxb.binding.datatypes.int, scope=astromConfig, documentation=u' Number of iterations during\n                                solving [None] '))

astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YMIN'), pyxb.binding.datatypes.float, scope=astromConfig, documentation=u' Minimum Y coordinate of useful\n                                pixel plane [pixel] '))

astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'THRESHFRAC'), pyxb.binding.datatypes.float, scope=astromConfig, documentation=u' Fraction of the maximum threshold\n                                below which the iteration is allowed to\n                                threshold [None] '))

astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XMIN'), pyxb.binding.datatypes.float, scope=astromConfig, documentation=u' Minimum X coordinate of useful\n                                pixel plane [pixel] '))

astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FDEG'), pyxb.binding.datatypes.int, scope=astromConfig, documentation=u' List of degrees of freedom of\n                                Chebychev polynomials [None] '))

astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YMAX'), pyxb.binding.datatypes.float, scope=astromConfig, documentation=u' Maximum Y coordinate of useful\n                                pixel plane [pixel] '))

astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE'), pyxb.binding.datatypes.string, scope=astromConfig, documentation=u' Verbosity level (QUIET, NORMAL,\n                                EXTRA_WARNINGS, FULL) [None] '))

astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XPIXSIZE'), pyxb.binding.datatypes.float, scope=astromConfig, documentation=u' Scaling of pixels with which\n                                CDELT1 is multiplied [None] '))

astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XMAX'), pyxb.binding.datatypes.float, scope=astromConfig, documentation=u' Maximum X coordinate of useful\n                                pixel plane [pixel] '))

astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PDEG'), pyxb.binding.datatypes.int, scope=astromConfig, documentation=u' Degrees of freedom for plate\n                                polynomials [None] '))

astromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YPIXSIZE'), pyxb.binding.datatypes.float, scope=astromConfig, documentation=u' Scaling of pixels with which\n                                CDELT2 is multiplied [None] '))
astromConfig._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1)
    )
astromConfig._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NITER')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XMIN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XMAX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YMIN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YMAX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PDEG')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FDEG')), min_occurs=3L, max_occurs=3L),
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XPIXSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YPIXSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'THRESHFRAC')), min_occurs=1, max_occurs=1)
    )
astromConfig._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astromConfig._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astromConfig._GroupModel_2, min_occurs=1, max_occurs=1)
    )
astromConfig._ContentModel = pyxb.binding.content.ParticleModel(astromConfig._GroupModel, min_occurs=1, max_occurs=1)



lamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=lamp, documentation=u' Name of the lamp [None] '))

lamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Position'), pyxb.binding.datatypes.int, scope=lamp, documentation=u' Position of the lamp [None] '))

lamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=lamp, documentation=u' ID of the lamp [None] '))

lamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=lamp, documentation=u' Unique EXT object identifier [None] '))

lamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateFit'), pyxb.binding.datatypes.dateTime, scope=lamp, documentation=u' Date the lamp was fitted [None] '))
lamp._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(lamp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(lamp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(lamp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(lamp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(lamp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateFit')), min_occurs=1, max_occurs=1)
    )
lamp._ContentModel = pyxb.binding.content.ParticleModel(lamp._GroupModel, min_occurs=1, max_occurs=1)



illuminationCorrectionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel'), pyxb.binding.datatypes.float, scope=illuminationCorrectionParameters, documentation=u' Sigma clipping threshold from the median\n                        zeropoint [None] '))

illuminationCorrectionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=illuminationCorrectionParameters, documentation=u' Unique EXT object identifier [None] '))
illuminationCorrectionParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(illuminationCorrectionParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(illuminationCorrectionParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel')), min_occurs=1, max_occurs=1)
    )
illuminationCorrectionParameters._ContentModel = pyxb.binding.content.ParticleModel(illuminationCorrectionParameters._GroupModel, min_occurs=1, max_occurs=1)



photSrcCatalogParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=photSrcCatalogParameters, documentation=u' Unique EXT object identifier [None] '))

photSrcCatalogParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxMagDiff'), pyxb.binding.datatypes.float, scope=photSrcCatalogParameters, documentation=u' Maximum difference of a standard star\n                        magnitude with respect to the median\n                        [mag]'))

photSrcCatalogParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FluxType'), pyxb.binding.datatypes.string, scope=photSrcCatalogParameters, documentation=u' Type of the measured flux (SExtractor\n                        parameter name) [None] '))

photSrcCatalogParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=photSrcCatalogParameters, documentation=u' Version of the source code [None] '))
photSrcCatalogParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photSrcCatalogParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalogParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FluxType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalogParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxMagDiff')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalogParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
photSrcCatalogParameters._ContentModel = pyxb.binding.content.ParticleModel(photSrcCatalogParameters._GroupModel, min_occurs=1, max_occurs=1)



readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumBiasDifference'), pyxb.binding.datatypes.float, scope=readNoiseParameters, documentation=u' QC: Maximum mean pixel value difference\n                        between biases [ADU] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations'), pyxb.binding.datatypes.int, scope=readNoiseParameters, documentation=u' Maximum number of iterations for\n                        estimating statistics [None] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumReadNoiseDifference'), pyxb.binding.datatypes.float, scope=readNoiseParameters, documentation=u' QC: Maximum difference between readout\n                        noise measurements relative to the previous version\n                        [ADU] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=readNoiseParameters, documentation=u' Unique EXT object identifier [None] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumReadNoise'), pyxb.binding.datatypes.float, scope=readNoiseParameters, documentation=u' QC: Maximum value for the readout noise\n                        [ADU] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=readNoiseParameters, documentation=u' Version of the source code [None] '))

readNoiseParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold'), pyxb.binding.datatypes.float, scope=readNoiseParameters, documentation=u' Threshold for rejecting pixels with\n                        outlying values [None] '))
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



photExtinctionCurve._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WavelengthIncrement'), pyxb.binding.datatypes.float, scope=photExtinctionCurve, documentation=u' Wavelength increment [angstrom] '))

photExtinctionCurve._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Storage'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=photExtinctionCurve, documentation=u' Customized storage container for the data\n                        [None] '))

photExtinctionCurve._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), pyxb.binding.datatypes.dateTime, scope=photExtinctionCurve, documentation=u' UTC date this object was created [None] '))

photExtinctionCurve._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=photExtinctionCurve, documentation=u' Unique EXT object identifier [None] '))

photExtinctionCurve._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtinctionPointList'), photExtinctionPoint, scope=photExtinctionCurve, documentation=u' List of input atmospheric extinction\n                        points [None] '))
photExtinctionCurve._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photExtinctionCurve._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photExtinctionCurve._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photExtinctionCurve._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtinctionPointList')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(photExtinctionCurve._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photExtinctionCurve._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WavelengthIncrement')), min_occurs=1, max_occurs=1)
    )
photExtinctionCurve._ContentModel = pyxb.binding.content.ParticleModel(photExtinctionCurve._GroupModel, min_occurs=1, max_occurs=1)



rawScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=rawScienceFrame, documentation=u' Information about the\n                                observational filter [None] '))

rawScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Astrom'), CommonDM.dm.bas.cot_stub.astrom, scope=rawScienceFrame, documentation=u' Basic information about the\n                                astrometry (linear terms only) [None] '))

rawScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), pyxb.binding.datatypes.float, scope=rawScienceFrame, documentation=u' Total time of an individual\n                                exposure [sec] '))

rawScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AirmassStart'), pyxb.binding.datatypes.float, scope=rawScienceFrame, documentation=u' Airmass at the beginning of the\n                                observation [None] '))

rawScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AirmassEnd'), pyxb.binding.datatypes.float, scope=rawScienceFrame, documentation=u' Airmass at the ending of the\n                                observation [None] '))
rawScienceFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
rawScienceFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
rawScienceFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawScienceFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
rawScienceFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
rawScienceFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawScienceFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
rawScienceFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawFits')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extension')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observer')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Date')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MjdObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Lst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Utc')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanYStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanYStat')), min_occurs=1, max_occurs=1)
    )
rawScienceFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawScienceFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
rawScienceFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Astrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AirmassStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AirmassEnd')), min_occurs=1, max_occurs=1)
    )
rawScienceFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawScienceFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawScienceFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
rawScienceFrame._ContentModel = pyxb.binding.content.ParticleModel(rawScienceFrame._GroupModel, min_occurs=1, max_occurs=1)



gAstrometric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Residuals'), pyxb.binding.datatypes.string, scope=gAstrometric, documentation=u' Filename of residuals FITS table [None] '))

gAstrometric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GasSList'), baseList, scope=gAstrometric, documentation=u' Information about the global astrometry\n                        associate list [None] '))

gAstrometric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=gAstrometric, documentation=u' Unique EXT object identifier [None] '))
gAstrometric._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(gAstrometric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gAstrometric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GasSList')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(gAstrometric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Residuals')), min_occurs=1, max_occurs=1)
    )
gAstrometric._ContentModel = pyxb.binding.content.ParticleModel(gAstrometric._GroupModel, min_occurs=1, max_occurs=1)



photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RA'), pyxb.binding.datatypes.float, scope=photSrcSource, documentation=u' Right ascension of the source [deg] '))

photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagErr'), pyxb.binding.datatypes.float, scope=photSrcSource, documentation=u' Measurement error of the magnitude error\n                        [mag] '))

photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Index'), pyxb.binding.datatypes.int, scope=photSrcSource, documentation=u' Index of the source [None] '))

photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEC'), pyxb.binding.datatypes.float, scope=photSrcSource, documentation=u' Declination of the source [deg] '))

photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=photSrcSource, documentation=u' Unique EXT object identifier [None] '))

photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InstrumentalMag'), pyxb.binding.datatypes.float, scope=photSrcSource, documentation=u' Instrumental magnitude of the source\n                        [mag] '))

photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YPosition'), pyxb.binding.datatypes.float, scope=photSrcSource, documentation=u' Detector Y position of the source [pixel] '))

photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XPosition'), pyxb.binding.datatypes.float, scope=photSrcSource, documentation=u' Detector X position of the source [pixel] '))

photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Mag'), pyxb.binding.datatypes.float, scope=photSrcSource, documentation=u' Magnitude of the source [mag] '))

photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InstrumentalMagErr'), pyxb.binding.datatypes.float, scope=photSrcSource, documentation=u' Measurement error of the instrumental\n                        magnitude [mag] '))

photSrcSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Origin'), pyxb.binding.datatypes.string, scope=photSrcSource, documentation=u' Origin of the source [None] '))
photSrcSource._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Index')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Origin')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEC')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Mag')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagErr')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InstrumentalMag')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InstrumentalMagErr')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XPosition')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YPosition')), min_occurs=1, max_occurs=1)
    )
photSrcSource._ContentModel = pyxb.binding.content.ParticleModel(photSrcSource._GroupModel, min_occurs=1, max_occurs=1)



atmosphericExtinctionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigclipLevel'), pyxb.binding.datatypes.float, scope=atmosphericExtinctionParameters, documentation=u' QC: Sigma clipping threshold factor\n                        [None] '))

atmosphericExtinctionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxError'), pyxb.binding.datatypes.float, scope=atmosphericExtinctionParameters, documentation=u' QC: Maximum relative (fractional) error\n                        [None] '))

atmosphericExtinctionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=atmosphericExtinctionParameters, documentation=u' Unique EXT object identifier [None] '))
atmosphericExtinctionParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinctionParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigclipLevel')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxError')), min_occurs=1, max_occurs=1)
    )
atmosphericExtinctionParameters._ContentModel = pyxb.binding.content.ParticleModel(atmosphericExtinctionParameters._GroupModel, min_occurs=1, max_occurs=1)



rawDomeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=rawDomeFlatFrame, documentation=u' Information about the\n                                observational filter [None] '))

rawDomeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Lamp'), lamp, scope=rawDomeFlatFrame, documentation=u' Information about the dome flat\n                                lamp [None] '))

rawDomeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), pyxb.binding.datatypes.float, scope=rawDomeFlatFrame, documentation=u' Total time of an individual\n                                exposure [sec] '))

rawDomeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), rawDomeFlatFrameParameters, scope=rawDomeFlatFrame, documentation=u' Processing and verification\n                                parameters [None] '))
rawDomeFlatFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
rawDomeFlatFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
rawDomeFlatFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
rawDomeFlatFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
rawDomeFlatFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
rawDomeFlatFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawFits')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extension')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observer')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Date')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MjdObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Lst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Utc')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanYStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanYStat')), min_occurs=1, max_occurs=1)
    )
rawDomeFlatFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
rawDomeFlatFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Lamp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
rawDomeFlatFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
rawDomeFlatFrame._ContentModel = pyxb.binding.content.ParticleModel(rawDomeFlatFrame._GroupModel, min_occurs=1, max_occurs=1)



biasFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames'), rawBiasFrame, scope=biasFrame, documentation=u' List of input raw bias frames\n                                [None] '))

biasFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise'), readNoise, scope=biasFrame, documentation=u' Information about the detector\n                                readout noise [None] '))

biasFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=biasFrame, documentation=u' Information about the\n                                observational template [None] '))

biasFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=biasFrame, documentation=u' Information about the\n                                observational block [None] '))

biasFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), biasFrameParameters, scope=biasFrame, documentation=u' Processing and verification\n                                parameters [None] '))
biasFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
biasFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
biasFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
biasFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
biasFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
biasFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
biasFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
biasFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawBiasFrames')), min_occurs=3L, max_occurs=None),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadNoise')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
biasFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(biasFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(biasFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
biasFrame._ContentModel = pyxb.binding.content.ParticleModel(biasFrame._GroupModel, min_occurs=1, max_occurs=1)



associateListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SearchDistance'), pyxb.binding.datatypes.float, scope=associateListParameters, documentation=u' Radius of search for associates [arcsec] '))

associateListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SextractorFlagMask'), pyxb.binding.datatypes.int, scope=associateListParameters, documentation=u' Value of SExtractor flag mask for source\n                        filtering [None]'))

associateListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleOutClosestPairs'), pyxb.binding.datatypes.int, scope=associateListParameters, documentation=u' Filter to retain only the closest\n                        associations [None] '))

associateListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=associateListParameters, documentation=u' Version of the source code [None] '))

associateListParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=associateListParameters, documentation=u' Unique EXT object identifier [None] '))
associateListParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(associateListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SearchDistance')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SingleOutClosestPairs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SextractorFlagMask')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
associateListParameters._ContentModel = pyxb.binding.content.ParticleModel(associateListParameters._GroupModel, min_occurs=1, max_occurs=1)



baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=baseList, documentation=u' Name of the list [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Object'), pyxb.binding.datatypes.string, scope=baseList, documentation=u' Name of target object [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URDec'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Declination of upper right corner [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=baseList, documentation=u' Unique EXT object identifier [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LLRa'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Right Ascension of lower left corner\n                        [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), pyxb.binding.datatypes.dateTime, scope=baseList, documentation=u' UTC date this object was created [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LRDec'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Declination of lower right corner [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IsValid'), pyxb.binding.datatypes.int, scope=baseList, documentation=u' Manual/external flag to disqualify bad\n                        data (SuperFlag) [None] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URRa'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Right Ascension of upper right corner\n                        [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ULDec'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Declination of upper left corner [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LRRa'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Right Ascension of lower right corner\n                        [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LLDec'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Declination of lower left corner [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ULRa'), pyxb.binding.datatypes.float, scope=baseList, documentation=u' Right Ascension of upper left corner\n                        [deg] '))

baseList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Storage'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=baseList, documentation=u' Customized storage container for the data\n                        [None] '))
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

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InputAssociateList'), associateList, scope=associateList, documentation=u' Information about the input\n                                associations [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Associates'), associateListDict, scope=associateList, documentation=u' Column definitions of\n                                associations [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), associateListParameters, scope=associateList, documentation=u' Processing and verification\n                                parameters [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociateListType'), pyxb.binding.datatypes.int, scope=associateList, documentation=u' Type of associate list [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Alid'), pyxb.binding.datatypes.int, scope=associateList, documentation=u' Identifier of the associate list\n                                [None] '))

associateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociateCount'), pyxb.binding.datatypes.int, scope=associateList, documentation=u' Number of associated source\n                                pairings [None] '))
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



nightSkyFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), pyxb.binding.datatypes.int, scope=nightSkyFlatFrameParameters, documentation=u' Overscan correction method index [None] '))

nightSkyFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=nightSkyFlatFrameParameters, documentation=u' Unique EXT object identifier [None] '))
nightSkyFlatFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nightSkyFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection')), min_occurs=1, max_occurs=1)
    )
nightSkyFlatFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(nightSkyFlatFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



domeFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip'), pyxb.binding.datatypes.float, scope=domeFlatFrameParameters, documentation=u' Threshold factor for rejecting raw dome\n                        flat pixel value outliers (sigma is taken as the scaled\n                        gain measurement) [None] '))

domeFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=domeFlatFrameParameters, documentation=u' Version of the source code [None] '))

domeFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=domeFlatFrameParameters, documentation=u' Unique EXT object identifier [None] '))

domeFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness'), pyxb.binding.datatypes.float, scope=domeFlatFrameParameters, documentation=u' QC: Maximum difference between median\n                        values of any two sub-windows [ADU] '))

domeFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), pyxb.binding.datatypes.int, scope=domeFlatFrameParameters, documentation=u' Overscan correction method index [None] '))

domeFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinDiff'), pyxb.binding.datatypes.float, scope=domeFlatFrameParameters, documentation=u' QC: Difference in MaximumSubwinFlatness\n                        relative to the previous version [ADU] '))
domeFlatFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domeFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinDiff')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
domeFlatFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(domeFlatFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



associateListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SID'), pyxb.binding.datatypes.int, scope=associateListDict, documentation=u' Identifier of a source in the source list\n                        [None] '))

associateListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLID'), pyxb.binding.datatypes.int, scope=associateListDict, documentation=u' Identifier of the source list [None] '))

associateListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ALID'), pyxb.binding.datatypes.int, scope=associateListDict, documentation=u' Identifier of the associate list [None] '))

associateListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AID'), pyxb.binding.datatypes.int, scope=associateListDict, documentation=u' Identifier of an association in the\n                        associate list [None] '))

associateListDict._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG'), pyxb.binding.datatypes.int, scope=associateListDict, documentation=u' Internal flag indicating the source\n                        list(s) participating in the association [None] '))
associateListDict._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(associateListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ALID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SLID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(associateListDict._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLAG')), min_occurs=1, max_occurs=1)
    )
associateListDict._ContentModel = pyxb.binding.content.ParticleModel(associateListDict._GroupModel, min_occurs=1, max_occurs=1)



photometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=photometricParametersParameters, documentation=u' Version of the source code [None] '))

photometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinSourceCount'), pyxb.binding.datatypes.int, scope=photometricParametersParameters, documentation=u' QC: Minimum number of sources used in\n                        zeropoint determination [None] '))

photometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=photometricParametersParameters, documentation=u' Unique EXT object identifier [None] '))

photometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel'), pyxb.binding.datatypes.float, scope=photometricParametersParameters, documentation=u' Sigma clipping threshold factor for raw\n                        zeropoints [None] '))

photometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxError'), pyxb.binding.datatypes.float, scope=photometricParametersParameters, documentation=u' QC: Maximum allowable error in the\n                        zeropoint [mag] '))
photometricParametersParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaClippingLevel')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinSourceCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
photometricParametersParameters._ContentModel = pyxb.binding.content.ParticleModel(photometricParametersParameters._GroupModel, min_occurs=1, max_occurs=1)



baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GridTarget'), gridTarget, scope=baseRegriddedFrame, documentation=u' Grid target for the regridding\n                                operation [None] '))

baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Object'), pyxb.binding.datatypes.string, scope=baseRegriddedFrame, documentation=u' Name of target object [None] '))

baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Astrom'), CommonDM.dm.bas.cot_stub.astrom, scope=baseRegriddedFrame, documentation=u' Basic information about the\n                                astrometry (linear terms only) [None] '))

baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), pyxb.binding.datatypes.float, scope=baseRegriddedFrame, documentation=u' Estimate of seeing using the\n                                median FWHM (filtered to isolate most\n                                stellar-like sources) [arcsec] '))

baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SwarpConf'), swarpConfig, scope=baseRegriddedFrame, documentation=u' SWarp configuration [None] '))

baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Weight'), weightFrame, scope=baseRegriddedFrame, documentation=u' Information about the detector\n                                pixel weights [None] '))

baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=baseRegriddedFrame, documentation=u' Information about the\n                                observational filter [None] '))

baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint'), pyxb.binding.datatypes.float, scope=baseRegriddedFrame, documentation=u' Value of the photometric\n                                zeropoint [mag] '))

baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=baseRegriddedFrame, documentation=u' Information about the\n                                observational block [None] '))

baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=baseRegriddedFrame, documentation=u' Information about the\n                                observational template [None] '))

baseRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ZeroPointError'), pyxb.binding.datatypes.float, scope=baseRegriddedFrame, documentation=u' Error on the value of the\n                                photometric zeropoint [mag] '))
baseRegriddedFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
baseRegriddedFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
baseRegriddedFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
baseRegriddedFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
baseRegriddedFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
baseRegriddedFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Astrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GridTarget')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SwarpConf')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Weight')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPointError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Seeing')), min_occurs=1, max_occurs=1)
    )
baseRegriddedFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRegriddedFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
baseRegriddedFrame._ContentModel = pyxb.binding.content.ParticleModel(baseRegriddedFrame._GroupModel, min_occurs=1, max_occurs=1)



regriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AstromParams'), astrometricParameters, scope=regriddedFrame, documentation=u' Advanced information about the\n                                derived astrometry (with higher-order terms)\n                                [None] '))

regriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=regriddedFrame, documentation=u' Information about the detector\n                                chip [None] '))

regriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), pyxb.binding.datatypes.dateTime, scope=regriddedFrame, documentation=u' UTC date at the start of the\n                                observation [None] '))

regriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FluxScale'), pyxb.binding.datatypes.float, scope=regriddedFrame, documentation=u' Derived flux scale\n                                [None]'))

regriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), regriddedFrameParameters, scope=regriddedFrame, documentation=u' Processing and verification\n                                parameters [None] '))

regriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reduced'), reducedScienceFrame, scope=regriddedFrame, documentation=u' Information about the input\n                                reduced science frame [None] '))

regriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Gain'), gainLinearity, scope=regriddedFrame, documentation=u' Information about the detector\n                                gain [None] '))

regriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PhotomParams'), photometricParameters, scope=regriddedFrame, documentation=u' Information about the photometry\n                                [None]'))
regriddedFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
regriddedFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
regriddedFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regriddedFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
regriddedFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
regriddedFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regriddedFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
regriddedFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Astrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GridTarget')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SwarpConf')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Weight')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPointError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Seeing')), min_occurs=1, max_occurs=1)
    )
regriddedFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regriddedFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
regriddedFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reduced')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Gain')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PhotomParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AstromParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FluxScale')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
regriddedFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regriddedFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
regriddedFrame._ContentModel = pyxb.binding.content.ParticleModel(regriddedFrame._GroupModel, min_occurs=1, max_occurs=1)



photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=photometricParameters, documentation=u' Information about the\n                                observational template [None] '))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=photometricParameters, documentation=u' Information about the acquisition\n                                instrument [None] '))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Extinction'), baseAtmosphericExtinction, scope=photometricParameters, documentation=u' Information about the atmospheric\n                                extinction [None] '))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=photometricParameters, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), pyxb.binding.datatypes.int, scope=photometricParameters, documentation=u' Number of sources used in\n                                zeropoint determination [None] '))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=photometricParameters, documentation=u' Information about the\n                                observational filter [None] '))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=photometricParameters, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PhotCat'), photSrcCatalog, scope=photometricParameters, documentation=u' Information about the input\n                                photometric sources [None]'))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=photometricParameters, documentation=u' Information about the detector\n                                chip [None] '))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=photometricParameters, documentation=u' Information about the\n                                observational block [None] '))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint'), zeroPoint, scope=photometricParameters, documentation=u' Information about the photometric\n                                zeropoint [None] '))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagId'), CommonDM.dm.bas.dtd_stub.nameRestriction, scope=photometricParameters, documentation=u' Identifier for the photometric\n                                band [None]'))

photometricParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), photometricParametersParameters, scope=photometricParameters, documentation=u' Processing and verification\n                                parameters [None] '))
photometricParameters._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
photometricParameters._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
photometricParameters._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photometricParameters._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._GroupModel_3, min_occurs=1, max_occurs=1)
    )
photometricParameters._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extinction')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PhotCat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
photometricParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photometricParameters._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricParameters._GroupModel_4, min_occurs=1, max_occurs=1)
    )
photometricParameters._ContentModel = pyxb.binding.content.ParticleModel(photometricParameters._GroupModel, min_occurs=1, max_occurs=1)



regriddedFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=regriddedFrameParameters, documentation=u' Unique EXT object identifier [None] '))

regriddedFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=regriddedFrameParameters, documentation=u' Version of the source code [None] '))

regriddedFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumPsfDifference'), pyxb.binding.datatypes.float, scope=regriddedFrameParameters, documentation=u' QC: Maximum fractional difference between\n                        average psf_radius of input reduced science frame and\n                        the regridded frame [None] '))

regriddedFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BackgroundSubstractionType'), pyxb.binding.datatypes.int, scope=regriddedFrameParameters, documentation=u' Index of the type of background\n                        subtraction [None] '))
regriddedFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regriddedFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BackgroundSubstractionType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumPsfDifference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regriddedFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
regriddedFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(regriddedFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumGainDifference'), pyxb.binding.datatypes.float, scope=gainLinearityParameters, documentation=u' QC: Maximum gain difference relative to\n                        the previous version [electron / ADU] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold'), pyxb.binding.datatypes.float, scope=gainLinearityParameters, documentation=u' Threshold for rejecting pixels with\n                        outlying values [None] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinimumGain'), pyxb.binding.datatypes.float, scope=gainLinearityParameters, documentation=u' QC: Minimum gain [electron / ADU] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=gainLinearityParameters, documentation=u' Unique EXT object identifier [None] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations'), pyxb.binding.datatypes.int, scope=gainLinearityParameters, documentation=u' Maximum number of iterations for\n                        estimating statistics [None] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximimGain'), pyxb.binding.datatypes.float, scope=gainLinearityParameters, documentation=u' QC: Maximum gain [electron / ADU] '))

gainLinearityParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), pyxb.binding.datatypes.int, scope=gainLinearityParameters, documentation=u' Overscan correction method index [None] '))
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



catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint'), pyxb.binding.datatypes.float, scope=catalog, documentation=u' Value of the photometric zeropoint [mag] '))

catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=catalog, documentation=u' Unique EXT object identifier [None] '))

catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), sextractorConfig, scope=catalog, documentation=u' SExtractor configuration for source\n                        extraction [None] '))

catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Weight'), CommonDM.dm.bas.img_stub.baseFrame, scope=catalog, documentation=u' Information about the detector pixel\n                        weights [None] '))

catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Threshold'), pyxb.binding.datatypes.float, scope=catalog, documentation=u' SExtractor detection threshold [None] '))

catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Frame'), CommonDM.dm.bas.img_stub.baseFrame, scope=catalog, documentation=u' Information about the input frame [None] '))

catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Storage'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=catalog, documentation=u' Customized storage container for the data\n                        [None] '))

catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), pyxb.binding.datatypes.float, scope=catalog, documentation=u' Estimate of seeing using the median FWHM\n                        (filtered to isolate most stellar-like sources) [arcsec] '))

catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), pyxb.binding.datatypes.int, scope=catalog, documentation=u' Number of extracted sources [None] '))

catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexParam'), pyxb.binding.datatypes.string, scope=catalog, documentation=u' List of parameters derived for each\n                        extracted source [None] '))

catalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WeightScale'), pyxb.binding.datatypes.float, scope=catalog, documentation=u' Weight scale [None] '))
catalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Weight')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Seeing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Threshold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WeightScale')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexConfig')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexParam')), min_occurs=0L, max_occurs=None)
    )
catalog._ContentModel = pyxb.binding.content.ParticleModel(catalog._GroupModel, min_occurs=1, max_occurs=1)



photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=photSrcCatalog, documentation=u' Information about the\n                                observational block [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=photSrcCatalog, documentation=u' Information about the\n                                observational template [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=photSrcCatalog, documentation=u' Information about the acquisition\n                                instrument [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=photSrcCatalog, documentation=u' Information about the\n                                observational filter [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IsValid'), pyxb.binding.datatypes.int, scope=photSrcCatalog, documentation=u' Manual/external flag to\n                                disqualify bad data (SuperFlag) [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PhotSourceList'), photSrcSource, scope=photSrcCatalog, documentation=u' List of input photometric sources\n                                [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=photSrcCatalog, documentation=u' Information about the detector\n                                chip [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagId'), CommonDM.dm.bas.dtd_stub.nameRestriction, scope=photSrcCatalog, documentation=u' Identifier for the photometric\n                                band [None]'))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), pyxb.binding.datatypes.dateTime, scope=photSrcCatalog, documentation=u' UTC date at the start of the\n                                observation [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Airmass'), pyxb.binding.datatypes.float, scope=photSrcCatalog, documentation=u' Average airmass of the\n                                observation [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Refcat'), photRefCatalog, scope=photSrcCatalog, documentation=u' Information about the photometric\n                                reference catalog [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), pyxb.binding.datatypes.dateTime, scope=photSrcCatalog, documentation=u' UTC date this object was created\n                                [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), photSrcCatalogParameters, scope=photSrcCatalog, documentation=u' Processing and verification\n                                parameters [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Transform'), photTransformation, scope=photSrcCatalog, documentation=u' Information about the photometric\n                                transformation between bands [None] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SkyBackground'), pyxb.binding.datatypes.float, scope=photSrcCatalog, documentation=u' Median flux value of the detector\n                                pixel values [count / sec / arcsec**2] '))

photSrcCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AstromParams'), astrometricParameters, scope=photSrcCatalog, documentation=u' Advanced information about the\n                                derived astrometry (with higher-order terms)\n                                [None] '))
photSrcCatalog._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Weight')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Seeing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Threshold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WeightScale')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexConfig')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexParam')), min_occurs=0L, max_occurs=None)
    )
photSrcCatalog._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PhotSourceList')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SkyBackground')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Airmass')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Refcat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Transform')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AstromParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
photSrcCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photSrcCatalog._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photSrcCatalog._GroupModel_2, min_occurs=1, max_occurs=1)
    )
photSrcCatalog._ContentModel = pyxb.binding.content.ParticleModel(photSrcCatalog._GroupModel, min_occurs=1, max_occurs=1)



rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Object'), CommonDM.dm.bas_stub.objectName, scope=rawFits, documentation=u' Name of target object [None] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Lst'), pyxb.binding.datatypes.float, scope=rawFits, documentation=u' Local sidereal time at the start of the\n                        observation expressed as the number of seconds (a float)\n                        since UTC midnight [sec] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Observer'), CommonDM.dm.sys.sgs_stub.curation, scope=rawFits, documentation=u' Information about the observer [None] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Utc'), pyxb.binding.datatypes.float, scope=rawFits, documentation=u' Universal coordinated time at the start\n                        of the observation expressed as the number of seconds (a\n                        float) since UTC midnight [sec] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=rawFits, documentation=u' Information about the observational block\n                        [None] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), pyxb.binding.datatypes.dateTime, scope=rawFits, documentation=u' UTC date at the start of the observation\n                        [None] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Date'), pyxb.binding.datatypes.dateTime, scope=rawFits, documentation=u' UTC date the original data file was saved\n                        [None] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=rawFits, documentation=u' Unique EXT object identifier [None] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=rawFits, documentation=u' Information about the acquisition\n                        instrument [None] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), pyxb.binding.datatypes.float, scope=rawFits, documentation=u' Total time of an individual exposure\n                        [sec] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OrigFilename'), pyxb.binding.datatypes.string, scope=rawFits, documentation=u' Archive file name [None] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Storage'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=rawFits, documentation=u' Customized storage container for the data\n                        [None] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MjdObs'), pyxb.binding.datatypes.float, scope=rawFits, documentation=u' Modified Julian date at the start of the\n                        observation (JD-2400000.5) [day] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=rawFits, documentation=u' Information about the observational\n                        filter [None] '))

rawFits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=rawFits, documentation=u' Information about the observational\n                        template [None] '))
rawFits._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observer')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Date')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MjdObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Lst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Utc')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawFits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OrigFilename')), min_occurs=1, max_occurs=1)
    )
rawFits._ContentModel = pyxb.binding.content.ParticleModel(rawFits._GroupModel, min_occurs=1, max_occurs=1)



rawTwilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), rawTwilightFlatFrameParameters, scope=rawTwilightFlatFrame, documentation=u' Processing and verification\n                                parameters [None] '))

rawTwilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), pyxb.binding.datatypes.float, scope=rawTwilightFlatFrame, documentation=u' Total time of an individual\n                                exposure [sec] '))

rawTwilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=rawTwilightFlatFrame, documentation=u' Information about the\n                                observational filter [None] '))
rawTwilightFlatFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
rawTwilightFlatFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
rawTwilightFlatFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
rawTwilightFlatFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
rawTwilightFlatFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
rawTwilightFlatFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawFits')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extension')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observer')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Date')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MjdObs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Lst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Utc')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscy')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Prscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscxpst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ovscypst')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrescanYStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanXStat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanYStat')), min_occurs=1, max_occurs=1)
    )
rawTwilightFlatFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
rawTwilightFlatFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
rawTwilightFlatFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
rawTwilightFlatFrame._ContentModel = pyxb.binding.content.ParticleModel(rawTwilightFlatFrame._GroupModel, min_occurs=1, max_occurs=1)



photExtinctionPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Extinction'), pyxb.binding.datatypes.float, scope=photExtinctionPoint, documentation=u' Atmospheric extinction [mag / airmass] '))

photExtinctionPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), pyxb.binding.datatypes.float, scope=photExtinctionPoint, documentation=u' Wavelength [angstrom] '))

photExtinctionPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=photExtinctionPoint, documentation=u' Unique EXT object identifier [None] '))
photExtinctionPoint._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photExtinctionPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photExtinctionPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Wavelength')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photExtinctionPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extinction')), min_occurs=1, max_occurs=1)
    )
photExtinctionPoint._ContentModel = pyxb.binding.content.ParticleModel(photExtinctionPoint._GroupModel, min_occurs=1, max_occurs=1)



twilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumNumberOfOutliers'), pyxb.binding.datatypes.int, scope=twilightFlatFrameParameters, documentation=u' QC: Maximum number of outliers [None] '))

twilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=twilightFlatFrameParameters, documentation=u' Unique EXT object identifier [None] '))

twilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness'), pyxb.binding.datatypes.float, scope=twilightFlatFrameParameters, documentation=u' QC: Maximum difference between median\n                        values of any two sub-windows [ADU] '))

twilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=twilightFlatFrameParameters, documentation=u' Version of the source code [None] '))

twilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection'), pyxb.binding.datatypes.int, scope=twilightFlatFrameParameters, documentation=u' Overscan correction method index [None] '))

twilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinDiff'), pyxb.binding.datatypes.float, scope=twilightFlatFrameParameters, documentation=u' QC: Difference in MaximumSubwinFlatness\n                        relative to the previous version [ADU] '))

twilightFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip'), pyxb.binding.datatypes.float, scope=twilightFlatFrameParameters, documentation=u' Threshold factor for rejecting raw\n                        twilight flat pixel value outliers (sigma is taken as\n                        the scaled gain measurement) [None] '))
twilightFlatFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(twilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OverscanCorrection')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaClip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinFlatness')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinDiff')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumNumberOfOutliers')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
twilightFlatFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(twilightFlatFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



coaddedRegriddedFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=coaddedRegriddedFrameParameters, documentation=u' Version of the source code [None] '))

coaddedRegriddedFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumPSFDifference'), pyxb.binding.datatypes.float, scope=coaddedRegriddedFrameParameters, documentation=u' QC: Maximum fractional difference between\n                        average psf_radius of input regridded frames and the\n                        coadded regridded frame [None] '))

coaddedRegriddedFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=coaddedRegriddedFrameParameters, documentation=u' Unique EXT object identifier [None] '))
coaddedRegriddedFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumPSFDifference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(coaddedRegriddedFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



astrometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxSigmaOverlap'), pyxb.binding.datatypes.float, scope=astrometricParametersParameters, documentation=u' QC: Maximum value of SigmaDraOverlap or\n                        SigmaDdecOverlap [arcsec] '))

astrometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxNref'), pyxb.binding.datatypes.int, scope=astrometricParametersParameters, documentation=u' QC: Maximum number of reference pairings\n                        [None] '))

astrometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinNOverlap'), pyxb.binding.datatypes.int, scope=astrometricParametersParameters, documentation=u' QC: Minimum number of overlap pairings\n                        [None] '))

astrometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxRmsOverlap'), pyxb.binding.datatypes.float, scope=astrometricParametersParameters, documentation=u' QC: Maximum (internal) RMS of overlap\n                        residuals [arcsec] '))

astrometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=astrometricParametersParameters, documentation=u' Unique EXT object identifier [None] '))

astrometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxSigma'), pyxb.binding.datatypes.float, scope=astrometricParametersParameters, documentation=u' QC: Maximum value of SigmaDra or\n                        SigmaDdec [arcsec] '))

astrometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxNOverlap'), pyxb.binding.datatypes.int, scope=astrometricParametersParameters, documentation=u' QC: Maximum number of overlap pairings\n                        [None] '))

astrometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=astrometricParametersParameters, documentation=u' Version of the source code [None] '))

astrometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinNref'), pyxb.binding.datatypes.int, scope=astrometricParametersParameters, documentation=u' QC: Minimum number of reference pairings\n                        [None] '))

astrometricParametersParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxRms'), pyxb.binding.datatypes.float, scope=astrometricParametersParameters, documentation=u' QC: Maximum (external) RMS of reference\n                        residuals [arcsec] '))
astrometricParametersParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astrometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinNref')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxNref')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxSigma')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxRms')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinNOverlap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxNOverlap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxSigmaOverlap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxRmsOverlap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrometricParametersParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
astrometricParametersParameters._ContentModel = pyxb.binding.content.ParticleModel(astrometricParametersParameters._GroupModel, min_occurs=1, max_occurs=1)



illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=illuminationCorrection, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxY'), pyxb.binding.datatypes.float, scope=illuminationCorrection, documentation=u' Y coordinate of the source with\n                                the highest Y position [pixel] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxX'), pyxb.binding.datatypes.float, scope=illuminationCorrection, documentation=u' X coordinate of the source with\n                                the highest X position [pixel] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=illuminationCorrection, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitCoeffs'), pyxb.binding.datatypes.float, scope=illuminationCorrection, documentation=u' List of fit coefficients [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), illuminationCorrectionParameters, scope=illuminationCorrection, documentation=u' Processing and verification\n                                parameters [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinY'), pyxb.binding.datatypes.float, scope=illuminationCorrection, documentation=u' Y coordinate of the source with\n                                the lowest Y position [pixel] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=illuminationCorrection, documentation=u' Information about the\n                                observational filter [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagId'), CommonDM.dm.bas.dtd_stub.nameRestriction, scope=illuminationCorrection, documentation=u' Identifier for the photometric\n                                band [None]'))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PhotCats'), photSrcCatalog, scope=illuminationCorrection, documentation=u' List of input photometric source\n                                catalogs [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=illuminationCorrection, documentation=u' Information about the acquisition\n                                instrument [None] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinX'), pyxb.binding.datatypes.float, scope=illuminationCorrection, documentation=u' X coordinate of the source with\n                                the lowest X position [pixel] '))

illuminationCorrection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Records'), illuminationCorrectionRecord, scope=illuminationCorrection, documentation=u' List of illumination correction\n                                records [None] '))
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
    pyxb.binding.content.ParticleModel(illuminationCorrection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PhotCats')), min_occurs=1L, max_occurs=None),
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



fringeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=fringeFrame, documentation=u' Information about the\n                                observational filter [None] '))

fringeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawScienceFrames'), rawScienceFrame, scope=fringeFrame, documentation=u' List of input raw science frames\n                                [None] '))

fringeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bias'), biasFrame, scope=fringeFrame, documentation=u' Information about the detector\n                                bias offset levels [None] '))

fringeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hot'), hotPixelMap, scope=fringeFrame, documentation=u' Information about the detector\n                                hot pixels [None] '))

fringeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cold'), coldPixelMap, scope=fringeFrame, documentation=u' Information about the detector\n                                cold pixels [None] '))

fringeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=fringeFrame, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

fringeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=fringeFrame, documentation=u' Information about the detector\n                                chip [None] '))

fringeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flat'), baseFlatFrame, scope=fringeFrame, documentation=u' Information about the detector\n                                sensitivity variations [None] '))

fringeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=fringeFrame, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

fringeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), fringeFrameParameters, scope=fringeFrame, documentation=u' Processing and verification\n                                parameters [None] '))
fringeFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
fringeFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
fringeFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fringeFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
fringeFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
fringeFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fringeFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
fringeFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawScienceFrames')), min_occurs=3L, max_occurs=None),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bias')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hot')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
fringeFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fringeFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fringeFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
fringeFrame._ContentModel = pyxb.binding.content.ParticleModel(fringeFrame._GroupModel, min_occurs=1, max_occurs=1)



reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AirmassEnd'), pyxb.binding.datatypes.float, scope=reducedScienceFrame, documentation=u' Airmass at the ending of the\n                                observation [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Weight'), weightFrame, scope=reducedScienceFrame, documentation=u' Information about the detector\n                                pixel weights [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), pyxb.binding.datatypes.float, scope=reducedScienceFrame, documentation=u' Estimate of seeing using the\n                                median FWHM (filtered to isolate most\n                                stellar-like sources) [arcsec] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=reducedScienceFrame, documentation=u' Information about the\n                                observational template [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ScaleFactor'), pyxb.binding.datatypes.float, scope=reducedScienceFrame, documentation=u' Detector fringe pattern scaling\n                                factor [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Raw'), rawScienceFrame, scope=reducedScienceFrame, documentation=u' Information about the input raw\n                                science frame [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=reducedScienceFrame, documentation=u' Information about the\n                                observational block [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=reducedScienceFrame, documentation=u' Information about the\n                                observational filter [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Astrom'), CommonDM.dm.bas.cot_stub.astrom, scope=reducedScienceFrame, documentation=u' Basic information about the\n                                astrometry (linear terms only) [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), reducedScienceFrameParameters, scope=reducedScienceFrame, documentation=u' Processing and verification\n                                parameters [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bias'), biasFrame, scope=reducedScienceFrame, documentation=u' Information about the detector\n                                bias offset levels [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), pyxb.binding.datatypes.float, scope=reducedScienceFrame, documentation=u' Total time of an individual\n                                exposure [sec] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flat'), masterFlatFrame, scope=reducedScienceFrame, documentation=u' Information about the detector\n                                sensitivity variations [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Object'), pyxb.binding.datatypes.string, scope=reducedScienceFrame, documentation=u' Name of target object [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hot'), hotPixelMap, scope=reducedScienceFrame, documentation=u' Information about the detector\n                                hot pixels [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Date'), pyxb.binding.datatypes.dateTime, scope=reducedScienceFrame, documentation=u' UTC date the original data file\n                                was saved [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cold'), coldPixelMap, scope=reducedScienceFrame, documentation=u' Information about the detector\n                                cold pixels [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateObs'), pyxb.binding.datatypes.dateTime, scope=reducedScienceFrame, documentation=u' UTC date at the start of the\n                                observation [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fringe'), fringeFrame, scope=reducedScienceFrame, documentation=u' Information about the detector\n                                fringe pattern [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AirmassStart'), pyxb.binding.datatypes.float, scope=reducedScienceFrame, documentation=u' Airmass at the beginning of the\n                                observation [None] '))

reducedScienceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), illuminationCorrectionFrame, scope=reducedScienceFrame, documentation=u' Information about the\n                                illumination correction\n                                [None]'))
reducedScienceFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Raw')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Astrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bias')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hot')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reducedScienceFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fringe')), min_occurs=1, max_occurs=1),
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
    pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
reducedScienceFrame._ContentModel = pyxb.binding.content.ParticleModel(reducedScienceFrame._GroupModel, min_occurs=1, max_occurs=1)



coldPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=coldPixelMapParameters, documentation=u' Unique EXT object identifier [None] '))

coldPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumColdPixelCount'), pyxb.binding.datatypes.int, scope=coldPixelMapParameters, documentation=u' QC: Maximum number of hot pixels [None] '))

coldPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ThresholdLow'), pyxb.binding.datatypes.float, scope=coldPixelMapParameters, documentation=u' Lower threshold for rejecting pixels with\n                        outlying values [None] '))

coldPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumColdPixelCountDifference'), pyxb.binding.datatypes.float, scope=coldPixelMapParameters, documentation=u' QC: Maximum number of new cold pixels\n                        relative to the previous version [None] '))

coldPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ThresholdHigh'), pyxb.binding.datatypes.float, scope=coldPixelMapParameters, documentation=u' Upper threshold for rejecting pixels with\n                        outlying values [None] '))

coldPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=coldPixelMapParameters, documentation=u' Version of the source code [None] '))
coldPixelMapParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coldPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ThresholdLow')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ThresholdHigh')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumColdPixelCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumColdPixelCountDifference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coldPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
coldPixelMapParameters._ContentModel = pyxb.binding.content.ParticleModel(coldPixelMapParameters._GroupModel, min_occurs=1, max_occurs=1)



satelliteMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectionThreshold'), pyxb.binding.datatypes.float, scope=satelliteMapParameters, documentation=u' Minimum SNR for pixels to enter line\n                        detection routine [None] '))

satelliteMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HoughThreshold'), pyxb.binding.datatypes.float, scope=satelliteMapParameters, documentation=u' Minimum number of pixels on a line, i.e.\n                        the minimum pixel value in the Hough image [None] '))

satelliteMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=satelliteMapParameters, documentation=u' Unique EXT object identifier [None] '))
satelliteMapParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(satelliteMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectionThreshold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HoughThreshold')), min_occurs=1, max_occurs=1)
    )
satelliteMapParameters._ContentModel = pyxb.binding.content.ParticleModel(satelliteMapParameters._GroupModel, min_occurs=1, max_occurs=1)



sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexParam'), pyxb.binding.datatypes.string, scope=sourceList, documentation=u' List of parameters derived for\n                                each extracted source [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=sourceList, documentation=u' Information about the acquisition\n                                instrument [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AstromParams'), astrometricParameters, scope=sourceList, documentation=u' Advanced information about the\n                                derived astrometry (with higher-order terms)\n                                [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), sourceListParameters, scope=sourceList, documentation=u' Processing and verification\n                                parameters [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=sourceList, documentation=u' Information about the detector\n                                chip [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Slid'), pyxb.binding.datatypes.int, scope=sourceList, documentation=u' Identifier of the source list\n                                [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), pyxb.binding.datatypes.int, scope=sourceList, documentation=u' Number of extracted sources\n                                [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sources'), sourceListDict, scope=sourceList, documentation=u' Column definitions of extracted\n                                sources [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectionFrame'), CommonDM.dm.bas.img_stub.baseFrame, scope=sourceList, documentation=u' Optional frame used to identify\n                                sources to be extracted (double image mode)\n                                [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=sourceList, documentation=u' Information about the\n                                observational filter [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Frame'), CommonDM.dm.bas.img_stub.baseFrame, scope=sourceList, documentation=u' Information about the input frame\n                                [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), sextractorConfig, scope=sourceList, documentation=u' SExtractor configuration for\n                                source extraction [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociateList'), pyxb.binding.datatypes.int, scope=sourceList, documentation=u' ALID (associate list identifier)\n                                that was used to create this (combined) source\n                                list [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filters'), pyxb.binding.datatypes.string, scope=sourceList, documentation=u' Observational filters for which\n                                columns are present in this (combined) source\n                                list [None] '))

sourceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CombineMethod'), pyxb.binding.datatypes.int, scope=sourceList, documentation=u' Method that was used to create\n                                this (combined) source list [None] '))
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
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AstromParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sourceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexConfig')), min_occurs=1, max_occurs=1),
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



atmosphericExtinctionCoefficient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=atmosphericExtinctionCoefficient, documentation=u' Information about the detector\n                                chip [None] [none] '))

atmosphericExtinctionCoefficient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=atmosphericExtinctionCoefficient, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

atmosphericExtinctionCoefficient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=atmosphericExtinctionCoefficient, documentation=u' UTC date of the ending of the\n                                valid period [None] '))
atmosphericExtinctionCoefficient._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
atmosphericExtinctionCoefficient._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Error')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtinctionCurve')), min_occurs=1, max_occurs=1)
    )
atmosphericExtinctionCoefficient._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._GroupModel_3, min_occurs=1, max_occurs=1)
    )
atmosphericExtinctionCoefficient._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
atmosphericExtinctionCoefficient._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._GroupModel_4, min_occurs=1, max_occurs=1)
    )
atmosphericExtinctionCoefficient._ContentModel = pyxb.binding.content.ParticleModel(atmosphericExtinctionCoefficient._GroupModel, min_occurs=1, max_occurs=1)



rawBiasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasLevel'), pyxb.binding.datatypes.float, scope=rawBiasFrameParameters, documentation=u' QC: Maximum average bias level (mean of\n                        the bias pixel values) [ADU] '))

rawBiasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasFlatness'), pyxb.binding.datatypes.float, scope=rawBiasFrameParameters, documentation=u' QC: Maximum difference in subwindow\n                        statistics (minimum minus maximum median values of 32\n                        sub-regions) [ADU] '))

rawBiasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=rawBiasFrameParameters, documentation=u' Unique EXT object identifier [None] '))

rawBiasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasStdev'), pyxb.binding.datatypes.float, scope=rawBiasFrameParameters, documentation=u' QC: Maximum sample standard deviation of\n                        the bias pixel values [ADU] '))

rawBiasFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=rawBiasFrameParameters, documentation=u' Version of the source code [None] '))
rawBiasFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawBiasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasStdev')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasLevel')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxBiasFlatness')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawBiasFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
rawBiasFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(rawBiasFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



hotPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations'), pyxb.binding.datatypes.int, scope=hotPixelMapParameters, documentation=u' Maximum number of iterations for\n                        estimating statistics [None] '))

hotPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=hotPixelMapParameters, documentation=u' Version of the source code [None] '))

hotPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=hotPixelMapParameters, documentation=u' Unique EXT object identifier [None] '))

hotPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumHotPixelCount'), pyxb.binding.datatypes.int, scope=hotPixelMapParameters, documentation=u' QC: Maximum number of hot pixels [None] '))

hotPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold'), pyxb.binding.datatypes.float, scope=hotPixelMapParameters, documentation=u' Threshold for rejecting pixels with\n                        outlying values [None] '))

hotPixelMapParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumHotPixelCountDifference'), pyxb.binding.datatypes.int, scope=hotPixelMapParameters, documentation=u' QC: Maximum number of new hot pixels\n                        relative to the previous version [None] '))
hotPixelMapParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hotPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RejectionThreshold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumIterations')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumHotPixelCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumHotPixelCountDifference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hotPixelMapParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
hotPixelMapParameters._ContentModel = pyxb.binding.content.ParticleModel(hotPixelMapParameters._GroupModel, min_occurs=1, max_occurs=1)



rawDarkFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpTime'), pyxb.binding.datatypes.float, scope=rawDarkFrame, documentation=u' Total time of an individual\n                                exposure [sec] '))
rawDarkFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawFits')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Extension')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observer')), min_occurs=1, max_occurs=1),
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
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpTime')), min_occurs=1, max_occurs=1)
    )
rawDarkFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
rawDarkFrame._ContentModel = pyxb.binding.content.ParticleModel(rawDarkFrame._GroupModel, min_occurs=1, max_occurs=1)



domeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Lamp'), lamp, scope=domeFlatFrame, documentation=u' Information about the dome flat\n                                lamp [None] '))

domeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawDomeFlatFrames'), rawDomeFlatFrame, scope=domeFlatFrame, documentation=u' List of input raw dome flat\n                                frames [None] '))

domeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bias'), biasFrame, scope=domeFlatFrame, documentation=u' Information about the detector\n                                bias offset levels [None] '))

domeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Gain'), gainLinearity, scope=domeFlatFrame, documentation=u' Information about the detector\n                                gain [None] '))

domeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hot'), hotPixelMap, scope=domeFlatFrame, documentation=u' Information about the detector\n                                hot pixels [None] '))

domeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cold'), coldPixelMap, scope=domeFlatFrame, documentation=u' Information about the detector\n                                cold pixels [None] '))

domeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), domeFlatFrameParameters, scope=domeFlatFrame, documentation=u' Processing and verification\n                                parameters [None] '))

domeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=domeFlatFrame, documentation=u' Information about the\n                                observational block [None] '))

domeFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=domeFlatFrame, documentation=u' Information about the\n                                observational template [None] '))
domeFlatFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
domeFlatFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
domeFlatFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domeFlatFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
domeFlatFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
domeFlatFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domeFlatFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
domeFlatFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
domeFlatFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domeFlatFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
domeFlatFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawDomeFlatFrames')), min_occurs=3L, max_occurs=None),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bias')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Gain')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hot')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Lamp')), min_occurs=1, max_occurs=1)
    )
domeFlatFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domeFlatFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(domeFlatFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
domeFlatFrame._ContentModel = pyxb.binding.content.ParticleModel(domeFlatFrame._GroupModel, min_occurs=1, max_occurs=1)



twilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Gain'), gainLinearity, scope=twilightFlatFrame, documentation=u' Information about the detector\n                                gain [None] '))

twilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hot'), hotPixelMap, scope=twilightFlatFrame, documentation=u' Information about the detector\n                                hot pixels [None] '))

twilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock'), CommonDM.dm.bas.img_stub.obsBlock, scope=twilightFlatFrame, documentation=u' Information about the\n                                observational block [None] '))

twilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawTwilightFlatFrames'), rawTwilightFlatFrame, scope=twilightFlatFrame, documentation=u' List of input raw twilight flat\n                                frames [None] '))

twilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), CommonDM.dm.bas.img_stub.template, scope=twilightFlatFrame, documentation=u' Information about the\n                                observational template [None] '))

twilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cold'), coldPixelMap, scope=twilightFlatFrame, documentation=u' Information about the detector\n                                cold pixels [None] '))

twilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bias'), biasFrame, scope=twilightFlatFrame, documentation=u' Information about the detector\n                                bias offset levels [None] '))

twilightFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), twilightFlatFrameParameters, scope=twilightFlatFrame, documentation=u' Processing and verification\n                                parameters [None] '))
twilightFlatFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
twilightFlatFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
twilightFlatFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(twilightFlatFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
twilightFlatFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
twilightFlatFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(twilightFlatFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
twilightFlatFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
twilightFlatFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(twilightFlatFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
twilightFlatFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawTwilightFlatFrames')), min_occurs=3L, max_occurs=None),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bias')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Gain')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hot')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
twilightFlatFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(twilightFlatFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(twilightFlatFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
twilightFlatFrame._ContentModel = pyxb.binding.content.ParticleModel(twilightFlatFrame._GroupModel, min_occurs=1, max_occurs=1)



nightSkyFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=nightSkyFlatFrame, documentation=u' Information about the\n                                observational filter [None] '))

nightSkyFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hot'), hotPixelMap, scope=nightSkyFlatFrame, documentation=u' Information about the detector\n                                hot pixels [None] '))

nightSkyFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bias'), biasFrame, scope=nightSkyFlatFrame, documentation=u' Information about the detector\n                                bias offset levels [None] '))

nightSkyFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=nightSkyFlatFrame, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

nightSkyFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flat'), baseFlatFrame, scope=nightSkyFlatFrame, documentation=u' Information about the detector\n                                sensitivity variations [None] '))

nightSkyFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cold'), coldPixelMap, scope=nightSkyFlatFrame, documentation=u' Information about the detector\n                                cold pixels [None] '))

nightSkyFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), nightSkyFlatFrameParameters, scope=nightSkyFlatFrame, documentation=u' Processing and verification\n                                parameters [None] '))

nightSkyFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawScienceFrames'), rawScienceFrame, scope=nightSkyFlatFrame, documentation=u' List of input raw science frames\n                                [None] '))

nightSkyFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=nightSkyFlatFrame, documentation=u' Information about the detector\n                                chip [None] '))

nightSkyFlatFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=nightSkyFlatFrame, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))
nightSkyFlatFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
nightSkyFlatFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
nightSkyFlatFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._GroupModel_4, min_occurs=1, max_occurs=1)
    )
nightSkyFlatFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
nightSkyFlatFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
nightSkyFlatFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawScienceFrames')), min_occurs=3L, max_occurs=None),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bias')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hot')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
nightSkyFlatFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nightSkyFlatFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
nightSkyFlatFrame._ContentModel = pyxb.binding.content.ParticleModel(nightSkyFlatFrame._GroupModel, min_occurs=1, max_occurs=1)



masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=masterFlatFrameParameters, documentation=u' Version of the source code [None] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CombineType'), pyxb.binding.datatypes.int, scope=masterFlatFrameParameters, documentation=u' Index for the type of input (some\n                        combination of dome and/or twilight flat frame) [None] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=masterFlatFrameParameters, documentation=u' Unique EXT object identifier [None] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MirrorYpix'), pyxb.binding.datatypes.int, scope=masterFlatFrameParameters, documentation=u' Number of pixels to mirror beyond the Y\n                        edges of the detector to provide Fourier transform\n                        continuity [pixel] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinDiff'), pyxb.binding.datatypes.float, scope=masterFlatFrameParameters, documentation=u' QC: Difference in MaximumSubwinFlatness\n                        relative to the previous version [ADU] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DigFilterSize'), pyxb.binding.datatypes.float, scope=masterFlatFrameParameters, documentation=u' Gaussian Fourier filter size [None] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MedianFilterSize'), pyxb.binding.datatypes.int, scope=masterFlatFrameParameters, documentation=u' Size of the median cleaning filter\n                        [pixel] '))

masterFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MirrorXpix'), pyxb.binding.datatypes.int, scope=masterFlatFrameParameters, documentation=u' Number of pixels to mirror beyond the X\n                        edges of the detector to provide Fourier transform\n                        continuity [pixel] '))
masterFlatFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DigFilterSize')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MirrorXpix')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MirrorYpix')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MedianFilterSize')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CombineType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumSubwinDiff')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(masterFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
masterFlatFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(masterFlatFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



satelliteMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Chip'), CommonDM.dm.bas.img_stub.chip, scope=satelliteMap, documentation=u' Information about the detector\n                                chip [None] '))

satelliteMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cold'), coldPixelMap, scope=satelliteMap, documentation=u' Information about the detector\n                                cold pixels [None] '))

satelliteMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Frame'), CommonDM.dm.bas.img_stub.baseFrame, scope=satelliteMap, documentation=u' Information about the input\n                                reduced science frame [None] '))

satelliteMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=satelliteMap, documentation=u' Information about the acquisition\n                                instrument [None] '))

satelliteMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), satelliteMapParameters, scope=satelliteMap, documentation=u' Processing and verification\n                                parameters [None] '))

satelliteMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Saturated'), saturatedPixelMap, scope=satelliteMap, documentation=u' Information about saturated\n                                pixels [None] '))

satelliteMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flat'), masterFlatFrame, scope=satelliteMap, documentation=u' Information about the detector\n                                sensitivity variations [None] '))

satelliteMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=satelliteMap, documentation=u' Information about the\n                                observational filter [None] '))

satelliteMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hot'), hotPixelMap, scope=satelliteMap, documentation=u' Information about the detector\n                                hot pixels [None] '))

satelliteMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Illumination'), illuminationCorrectionFrame, scope=satelliteMap, documentation=u' Information about the\n                                illumination correction [None] '))
satelliteMap._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
satelliteMap._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
satelliteMap._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(satelliteMap._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._GroupModel_4, min_occurs=1, max_occurs=1)
    )
satelliteMap._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Count')), min_occurs=1, max_occurs=1)
    )
satelliteMap._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(satelliteMap._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._GroupModel_5, min_occurs=1, max_occurs=1)
    )
satelliteMap._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Saturated')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hot')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Illumination')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Chip')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
satelliteMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(satelliteMap._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(satelliteMap._GroupModel_6, min_occurs=1, max_occurs=1)
    )
satelliteMap._ContentModel = pyxb.binding.content.ParticleModel(satelliteMap._GroupModel, min_occurs=1, max_occurs=1)



photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd'), pyxb.binding.datatypes.dateTime, scope=photTransformation, documentation=u' UTC date of the ending of the\n                                valid period [None] '))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ColorTermError'), pyxb.binding.datatypes.float, scope=photTransformation, documentation=u' Error on color term [mag] '))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagId'), CommonDM.dm.bas.dtd_stub.nameRestriction, scope=photTransformation, documentation=u' Identifier for the photometric\n                                band [None]'))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CoefficientError'), pyxb.binding.datatypes.float, scope=photTransformation, documentation=u' Error on additional offset [mag] '))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Coefficient'), pyxb.binding.datatypes.float, scope=photTransformation, documentation=u' Additional offset [mag] '))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Instrument'), CommonDM.dm.bas.img_stub.instrument, scope=photTransformation, documentation=u' Information about the acquisition\n                                instrument [None] '))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SecondaryBand'), pyxb.binding.datatypes.string, scope=photTransformation, documentation=u' Magnitude ID of secondary filter\n                                [None] '))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart'), pyxb.binding.datatypes.dateTime, scope=photTransformation, documentation=u' UTC date of the beginning of the\n                                valid period [None] '))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrimaryBand'), pyxb.binding.datatypes.string, scope=photTransformation, documentation=u' Magnitude ID of primary filter\n                                [None] '))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TertiaryBand'), pyxb.binding.datatypes.string, scope=photTransformation, documentation=u' Magnitude ID of tertiary filter\n                                [None] '))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), CommonDM.dm.bas.img_stub.filter, scope=photTransformation, documentation=u' Information about the\n                                observational filter [None] '))

photTransformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ColorTerm'), pyxb.binding.datatypes.float, scope=photTransformation, documentation=u' Color term [mag] '))
photTransformation._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
photTransformation._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrimaryBand')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SecondaryBand')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TertiaryBand')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coefficient')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CoefficientError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ColorTerm')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ColorTermError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampStart')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimestampEnd')), min_occurs=1, max_occurs=1)
    )
photTransformation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photTransformation._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photTransformation._GroupModel_2, min_occurs=1, max_occurs=1)
    )
photTransformation._ContentModel = pyxb.binding.content.ParticleModel(photTransformation._GroupModel, min_occurs=1, max_occurs=1)



rawDomeFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), CommonDM.dm.bas_stub.extObjectId, scope=rawDomeFlatFrameParameters, documentation=u' Unique EXT object identifier [None] '))

rawDomeFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion'), pyxb.binding.datatypes.int, scope=rawDomeFlatFrameParameters, documentation=u' Version of the source code [None] '))

rawDomeFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxFlatMean'), pyxb.binding.datatypes.int, scope=rawDomeFlatFrameParameters, documentation=u' QC: Maximum level of the flat (mean of\n                        the flat pixel values) [ADU] '))

rawDomeFlatFrameParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinFlatMean'), pyxb.binding.datatypes.int, scope=rawDomeFlatFrameParameters, documentation=u' QC: Minimum level of the flat (mean of\n                        the flat pixel values) [ADU] '))
rawDomeFlatFrameParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rawDomeFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinFlatMean')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxFlatMean')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(rawDomeFlatFrameParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCodeVersion')), min_occurs=1, max_occurs=1)
    )
rawDomeFlatFrameParameters._ContentModel = pyxb.binding.content.ParticleModel(rawDomeFlatFrameParameters._GroupModel, min_occurs=1, max_occurs=1)



coaddedRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegriddedFrames'), baseRegriddedFrame, scope=coaddedRegriddedFrame, documentation=u' List of regridded frames to be\n                                coadded [None] '))

coaddedRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams'), coaddedRegriddedFrameParameters, scope=coaddedRegriddedFrame, documentation=u' Processing and verification\n                                parameters [None] '))

coaddedRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PsfRadiiPerDetector'), pyxb.binding.datatypes.float, scope=coaddedRegriddedFrame, documentation=u' List of stellar FWHM in\n                                subsections of the coadd [arcsec] '))

coaddedRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Detectors'), CommonDM.dm.bas.img_stub.chip, scope=coaddedRegriddedFrame, documentation=u' List of detector names of which\n                                input is present in the output frame [None] '))
coaddedRegriddedFrame._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_5, min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_6, min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Astrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GridTarget')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Object')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SwarpConf')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Weight')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPointError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Seeing')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_7, min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel_8 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RegriddedFrames')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Detectors')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PsfRadiiPerDetector')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessParams')), min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel_8, min_occurs=1, max_occurs=1)
    )
coaddedRegriddedFrame._ContentModel = pyxb.binding.content.ParticleModel(coaddedRegriddedFrame._GroupModel, min_occurs=1, max_occurs=1)



preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE'), pyxb.binding.datatypes.string, scope=preastromConfig, documentation=u' Verbosity level (QUIET, NORMAL,\n                                EXTRA_WARNINGS, FULL) [None] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MIN_OBJ'), pyxb.binding.datatypes.int, scope=preastromConfig, documentation=u' Minimum number of reference\n                                objects required to determine affine\n                                transformation [None] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MIN_PHOTS'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' List of photometric parameter\n                                limits for pairing with reference objects [None] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YPIXSIZE'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' Scaling of pixels with which\n                                CDELT2 is multiplied [None] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG_MASK'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' SExtractor mask to select objects\n                                for astrometric pairing: Flag and FLAG_MASK\n                                [None] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RMS_TOL'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' RMS tolerenace for triangulation\n                                matching [pixel] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XMIN'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' Minimum X coordinate allowed in\n                                pairing [pixel] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SEL_MIN'), pyxb.binding.datatypes.int, scope=preastromConfig, documentation=u' Minumim number of objects used in\n                                triangulation method [None] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAX_OFFSET'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' Maximum allowed offset between\n                                extracted and reference objects [pixel] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AFFINE_PARS'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' List of Parameters for the affine\n                                transformation (a0, a1, a2, b0, b1, b2) [None] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHOT'), pyxb.binding.datatypes.string, scope=preastromConfig, documentation=u' Name of the table column\n                                containing object flux measures [None] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YMAX'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' Maximum Y coordinate allowed in\n                                pairing [pixel] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YMIN'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' Minimum Y coordinate allowed in\n                                pairing [pixel] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'POS_ERROR'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' Positional error between\n                                extracted and reference objects [pixel] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XMAX'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' Maximum X coordinate allowed in\n                                pairing [pixel] '))

preastromConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XPIXSIZE'), pyxb.binding.datatypes.float, scope=preastromConfig, documentation=u' Scaling of pixels with which\n                                CDELT1 is multiplied [None] '))
preastromConfig._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1)
    )
preastromConfig._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MIN_OBJ')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAX_OFFSET')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'POS_ERROR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MIN_PHOTS')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AFFINE_PARS')), min_occurs=6L, max_occurs=6L),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PHOT')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RMS_TOL')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XPIXSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YPIXSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XMIN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XMAX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YMIN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YMAX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLAG_MASK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SEL_MIN')), min_occurs=1, max_occurs=1)
    )
preastromConfig._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(preastromConfig._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(preastromConfig._GroupModel_2, min_occurs=1, max_occurs=1)
    )
preastromConfig._ContentModel = pyxb.binding.content.ParticleModel(preastromConfig._GroupModel, min_occurs=1, max_occurs=1)
