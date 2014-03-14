# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/pro/mer_stub.py
# PyXB bindings for NamespaceModule
# NSM:db4a3ca9e083d26546786acafbe4eee2e4de7bb1
# Generated 2014-03-14 09:43:27.466759 by PyXB version 1.1.2
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
import euclid.dm.bas.fit_stub
import euclid.dm.bas.img_stub
import pyxb.binding.datatypes
import euclid.dm.bas.dtd_stub
import euclid.dm.bas_stub
import euclid.dm.sys.sgs_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/mer', create_if_missing=True)
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


# Complex type extCatalog with content type ELEMENT_ONLY
class extCatalog (euclid.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'extCatalog')
    # Base type is euclid.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', euclid.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', euclid.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.photometryCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = euclid.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = euclid.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'extCatalog', extCatalog)


# Complex type calStackExt with content type ELEMENT_ONLY
class calStackExt (euclid.dm.bas.img_stub.baseSciFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'calStackExt')
    # Base type is euclid.dm.bas.img_stub.baseSciFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Template ({http://euclid.esa.org/schema/bas/img}Template) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ObsBlock ({http://euclid.esa.org/schema/bas/img}ObsBlock) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Filter ({http://euclid.esa.org/schema/bas/img}Filter) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Astrom ({http://euclid.esa.org/schema/bas/img}Astrom) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame

    _ElementMap = euclid.dm.bas.img_stub.baseSciFrame._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = euclid.dm.bas.img_stub.baseSciFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'calStackExt', calStackExt)


# Complex type visCatalog with content type ELEMENT_ONLY
class visCatalog (euclid.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visCatalog')
    # Base type is euclid.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', euclid.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', euclid.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.photometryCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = euclid.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = euclid.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'visCatalog', visCatalog)


# Complex type nirCatalog with content type ELEMENT_ONLY
class nirCatalog (euclid.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nirCatalog')
    # Base type is euclid.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', euclid.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', euclid.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.photometryCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = euclid.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = euclid.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'nirCatalog', nirCatalog)


# Complex type visPsfModel with content type ELEMENT_ONLY
class visPsfModel (euclid.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visPsfModel')
    # Base type is euclid.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', euclid.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', euclid.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.photometryCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = euclid.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = euclid.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'visPsfModel', visPsfModel)


# Complex type VIScalibratedImages with content type ELEMENT_ONLY
class VIScalibratedImages (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VIScalibratedImages')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element VIScalibratedImage uses Python identifier VIScalibratedImage
    __VIScalibratedImage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'VIScalibratedImage'), 'VIScalibratedImage', '__httpeuclid_esa_orgschemapromer_VIScalibratedImages_VIScalibratedImage', False)

    
    VIScalibratedImage = property(__VIScalibratedImage.value, __VIScalibratedImage.set, None, None)

    
    # Element depth uses Python identifier depth
    __depth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'depth'), 'depth', '__httpeuclid_esa_orgschemapromer_VIScalibratedImages_depth', False)

    
    depth = property(__depth.value, __depth.set, None, None)


    _ElementMap = {
        __VIScalibratedImage.name() : __VIScalibratedImage,
        __depth.name() : __depth
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'VIScalibratedImages', VIScalibratedImages)


# Complex type objectCandidateList with content type ELEMENT_ONLY
class objectCandidateList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'objectCandidateList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/mer}SexParam uses Python identifier SexParam
    __SexParam = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexParam'), 'SexParam', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerSexParam', True)

    
    SexParam = property(__SexParam.value, __SexParam.set, None, u' List of parameters derived for each\n                        extracted source [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}Storage uses Python identifier Storage
    __Storage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Storage'), 'Storage', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerStorage', False)

    
    Storage = property(__Storage.value, __Storage.set, None, u' Customized storage container for the data\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}WeightScale uses Python identifier WeightScale
    __WeightScale = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WeightScale'), 'WeightScale', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerWeightScale', False)

    
    WeightScale = property(__WeightScale.value, __WeightScale.set, None, u' Weight scale [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}Weight uses Python identifier Weight
    __Weight = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Weight'), 'Weight', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerWeight', False)

    
    Weight = property(__Weight.value, __Weight.set, None, u' Information about the detector pixel\n                        weights [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}SourceCount uses Python identifier SourceCount
    __SourceCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), 'SourceCount', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerSourceCount', False)

    
    SourceCount = property(__SourceCount.value, __SourceCount.set, None, u' Number of extracted sources [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}Threshold uses Python identifier Threshold
    __Threshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Threshold'), 'Threshold', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerThreshold', False)

    
    Threshold = property(__Threshold.value, __Threshold.set, None, u' SExtractor detection threshold [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}SexConfig uses Python identifier SexConfig
    __SexConfig = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), 'SexConfig', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerSexConfig', False)

    
    SexConfig = property(__SexConfig.value, __SexConfig.set, None, u' SExtractor configuration for source\n                        extraction [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}Seeing uses Python identifier Seeing
    __Seeing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), 'Seeing', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerSeeing', False)

    
    Seeing = property(__Seeing.value, __Seeing.set, None, u' Estimate of seeing using the median FWHM\n                        (filtered to isolate most stellar-like sources) [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}Frame uses Python identifier Frame
    __Frame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Frame'), 'Frame', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerFrame', False)

    
    Frame = property(__Frame.value, __Frame.set, None, u' Information about the input frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}ZeroPoint uses Python identifier ZeroPoint
    __ZeroPoint = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint'), 'ZeroPoint', '__httpeuclid_esa_orgschemapromer_objectCandidateList_httpeuclid_esa_orgschemapromerZeroPoint', False)

    
    ZeroPoint = property(__ZeroPoint.value, __ZeroPoint.set, None, u' Value of the photometric zeropoint [mag] ')


    _ElementMap = {
        __SexParam.name() : __SexParam,
        __ExtObjectId.name() : __ExtObjectId,
        __Storage.name() : __Storage,
        __WeightScale.name() : __WeightScale,
        __Weight.name() : __Weight,
        __SourceCount.name() : __SourceCount,
        __Threshold.name() : __Threshold,
        __SexConfig.name() : __SexConfig,
        __Seeing.name() : __Seeing,
        __Frame.name() : __Frame,
        __ZeroPoint.name() : __ZeroPoint
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'objectCandidateList', objectCandidateList)


# Complex type sextractorConfigDetection with content type ELEMENT_ONLY
class sextractorConfigDetection (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sextractorConfigDetection')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/mer}CLEAN_PARAM uses Python identifier CLEAN_PARAM
    __CLEAN_PARAM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CLEAN_PARAM'), 'CLEAN_PARAM', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerCLEAN_PARAM', False)

    
    CLEAN_PARAM = property(__CLEAN_PARAM.value, __CLEAN_PARAM.set, None, u' Efficiency of cleaning [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}GAIN uses Python identifier GAIN
    __GAIN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GAIN'), 'GAIN', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerGAIN', False)

    
    GAIN = property(__GAIN.value, __GAIN.set, None, u' Conversion factor used for error\n                                estimates of CCD magnitudes [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}PIXEL_SCALE uses Python identifier PIXEL_SCALE
    __PIXEL_SCALE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE'), 'PIXEL_SCALE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerPIXEL_SCALE', False)

    
    PIXEL_SCALE = property(__PIXEL_SCALE.value, __PIXEL_SCALE.set, None, u' Pixel size [arcsec / pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACKPHOTO_THICK uses Python identifier BACKPHOTO_THICK
    __BACKPHOTO_THICK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_THICK'), 'BACKPHOTO_THICK', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerBACKPHOTO_THICK', False)

    
    BACKPHOTO_THICK = property(__BACKPHOTO_THICK.value, __BACKPHOTO_THICK.set, None, u' Thickness of the background LOCAL\n                                annulus [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}DEBLEND_MINCONT uses Python identifier DEBLEND_MINCONT
    __DEBLEND_MINCONT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_MINCONT'), 'DEBLEND_MINCONT', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerDEBLEND_MINCONT', False)

    
    DEBLEND_MINCONT = property(__DEBLEND_MINCONT.value, __DEBLEND_MINCONT.set, None, u' Minimum contrast parameter for\n                                deblending [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MEMORY_BUFSIZE uses Python identifier MEMORY_BUFSIZE
    __MEMORY_BUFSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_BUFSIZE'), 'MEMORY_BUFSIZE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerMEMORY_BUFSIZE', False)

    
    MEMORY_BUFSIZE = property(__MEMORY_BUFSIZE.value, __MEMORY_BUFSIZE.set, None, u' Number of scan-lines in the image\n                                buffer [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}FLAG_TYPE uses Python identifier FLAG_TYPE
    __FLAG_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG_TYPE'), 'FLAG_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerFLAG_TYPE', False)

    
    FLAG_TYPE = property(__FLAG_TYPE.value, __FLAG_TYPE.set, None, u' Combination method for flags on\n                                the same object (OR, AND, MIN, MAX, MOST) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MAG_ZEROPOINT uses Python identifier MAG_ZEROPOINT
    __MAG_ZEROPOINT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_ZEROPOINT'), 'MAG_ZEROPOINT', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerMAG_ZEROPOINT', False)

    
    MAG_ZEROPOINT = property(__MAG_ZEROPOINT.value, __MAG_ZEROPOINT.set, None, u' Zero-point offset to be applied\n                                to magnitudes [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}SEEING_FWHM uses Python identifier SEEING_FWHM
    __SEEING_FWHM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SEEING_FWHM'), 'SEEING_FWHM', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerSEEING_FWHM', False)

    
    SEEING_FWHM = property(__SEEING_FWHM.value, __SEEING_FWHM.set, None, u' FWHM of stellar sources (for\n                                star/galaxy separation only) [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}DEBLEND_NTHRESH uses Python identifier DEBLEND_NTHRESH
    __DEBLEND_NTHRESH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_NTHRESH'), 'DEBLEND_NTHRESH', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerDEBLEND_NTHRESH', False)

    
    DEBLEND_NTHRESH = property(__DEBLEND_NTHRESH.value, __DEBLEND_NTHRESH.set, None, u' Number of deblending\n                                sub-thresholds [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MEMORY_PIXSTACK uses Python identifier MEMORY_PIXSTACK
    __MEMORY_PIXSTACK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_PIXSTACK'), 'MEMORY_PIXSTACK', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerMEMORY_PIXSTACK', False)

    
    MEMORY_PIXSTACK = property(__MEMORY_PIXSTACK.value, __MEMORY_PIXSTACK.set, None, u' Maximum number of pixels that the\n                                pixel-stack can contain [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MASK_TYPE uses Python identifier MASK_TYPE
    __MASK_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MASK_TYPE'), 'MASK_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerMASK_TYPE', False)

    
    MASK_TYPE = property(__MASK_TYPE.value, __MASK_TYPE.set, None, u' Method of masking of neighbors\n                                for photometry (NONE, BLANK, CORRECT) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}DETECT_MINAREA uses Python identifier DETECT_MINAREA
    __DETECT_MINAREA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DETECT_MINAREA'), 'DETECT_MINAREA', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerDETECT_MINAREA', False)

    
    DETECT_MINAREA = property(__DETECT_MINAREA.value, __DETECT_MINAREA.set, None, u' Minimum number of pixels above\n                                threshold triggering detection [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}THRESH_TYPE uses Python identifier THRESH_TYPE
    __THRESH_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'THRESH_TYPE'), 'THRESH_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerTHRESH_TYPE', False)

    
    THRESH_TYPE = property(__THRESH_TYPE.value, __THRESH_TYPE.set, None, u' Meaning of DETECT_THRESH and\n                                ANALYSIS_THRESH parameters (RELATIVE, ABSOLUTE)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACK_TYPE uses Python identifier BACK_TYPE
    __BACK_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE'), 'BACK_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerBACK_TYPE', False)

    
    BACK_TYPE = property(__BACK_TYPE.value, __BACK_TYPE.set, None, u' Type of background subtracted\n                                from the images (AUTO, MANUAL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}PHOT_APERTURES uses Python identifier PHOT_APERTURES
    __PHOT_APERTURES = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PHOT_APERTURES'), 'PHOT_APERTURES', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerPHOT_APERTURES', False)

    
    PHOT_APERTURES = property(__PHOT_APERTURES.value, __PHOT_APERTURES.set, None, u' MAG_APER aperture diameter\n                                [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}DETECT_THRESH uses Python identifier DETECT_THRESH
    __DETECT_THRESH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DETECT_THRESH'), 'DETECT_THRESH', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerDETECT_THRESH', False)

    
    DETECT_THRESH = property(__DETECT_THRESH.value, __DETECT_THRESH.set, None, u' Detection threshold relative to\n                                background RMS (when THRESH_TYPE is RELATIVE)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}FILTER uses Python identifier FILTER
    __FILTER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FILTER'), 'FILTER', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerFILTER', False)

    
    FILTER = property(__FILTER.value, __FILTER.set, None, u' Apply filtering to the data\n                                before extraction (Y, N) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACK_VALUE uses Python identifier BACK_VALUE
    __BACK_VALUE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_VALUE'), 'BACK_VALUE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerBACK_VALUE', True)

    
    BACK_VALUE = property(__BACK_VALUE.value, __BACK_VALUE.set, None, u' List of constant values to be\n                                subtracted from the images if BACK_TYPE is\n                                MANUAL [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}DETECT_TYPE uses Python identifier DETECT_TYPE
    __DETECT_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DETECT_TYPE'), 'DETECT_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerDETECT_TYPE', False)

    
    DETECT_TYPE = property(__DETECT_TYPE.value, __DETECT_TYPE.set, None, u' Type of device that produced the\n                                image (CCD, PHOTO) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}PHOT_AUTOAPERS uses Python identifier PHOT_AUTOAPERS
    __PHOT_AUTOAPERS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOAPERS'), 'PHOT_AUTOAPERS', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerPHOT_AUTOAPERS', True)

    
    PHOT_AUTOAPERS = property(__PHOT_AUTOAPERS.value, __PHOT_AUTOAPERS.set, None, u' List of MAG_AUTO minimum circular\n                                aperture diameters (estimation disk, measurement\n                                disk) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CATALOG_NAME uses Python identifier CATALOG_NAME
    __CATALOG_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_NAME'), 'CATALOG_NAME', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerCATALOG_NAME', False)

    
    CATALOG_NAME = property(__CATALOG_NAME.value, __CATALOG_NAME.set, None, u' Name of the output catalog [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACK_SIZE uses Python identifier BACK_SIZE
    __BACK_SIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE'), 'BACK_SIZE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerBACK_SIZE', False)

    
    BACK_SIZE = property(__BACK_SIZE.value, __BACK_SIZE.set, None, u' Size of a background mesh [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}WEIGHT_TYPE uses Python identifier WEIGHT_TYPE
    __WEIGHT_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE'), 'WEIGHT_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerWEIGHT_TYPE', False)

    
    WEIGHT_TYPE = property(__WEIGHT_TYPE.value, __WEIGHT_TYPE.set, None, u' Weighting scheme for weight-image\n                                (NONE, BACKGROUND, MAP_RMS, MAP_VAR, MAP_WEIGHT)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}SATUR_LEVEL uses Python identifier SATUR_LEVEL
    __SATUR_LEVEL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SATUR_LEVEL'), 'SATUR_LEVEL', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerSATUR_LEVEL', False)

    
    SATUR_LEVEL = property(__SATUR_LEVEL.value, __SATUR_LEVEL.set, None, u' Pixel value above which it is\n                                considered saturated [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}PARAMETERS_NAME uses Python identifier PARAMETERS_NAME
    __PARAMETERS_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PARAMETERS_NAME'), 'PARAMETERS_NAME', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerPARAMETERS_NAME', False)

    
    PARAMETERS_NAME = property(__PARAMETERS_NAME.value, __PARAMETERS_NAME.set, None, u' Name of the file containing the\n                                list of parameters that will be computed and put\n                                into the catalog for each object [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}FILTER_NAME uses Python identifier FILTER_NAME
    __FILTER_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FILTER_NAME'), 'FILTER_NAME', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerFILTER_NAME', False)

    
    FILTER_NAME = property(__FILTER_NAME.value, __FILTER_NAME.set, None, u' Name of file contianing the\n                                filter definition [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MEMORY_OBJSTACK uses Python identifier MEMORY_OBJSTACK
    __MEMORY_OBJSTACK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_OBJSTACK'), 'MEMORY_OBJSTACK', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerMEMORY_OBJSTACK', False)

    
    MEMORY_OBJSTACK = property(__MEMORY_OBJSTACK.value, __MEMORY_OBJSTACK.set, None, u' Maximum number of objects that\n                                the object-stack can contain [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CHECKIMAGE_NAME uses Python identifier CHECKIMAGE_NAME
    __CHECKIMAGE_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_NAME'), 'CHECKIMAGE_NAME', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerCHECKIMAGE_NAME', False)

    
    CHECKIMAGE_NAME = property(__CHECKIMAGE_NAME.value, __CHECKIMAGE_NAME.set, None, u' Filename for the check-image\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}STARNNW_NAME uses Python identifier STARNNW_NAME
    __STARNNW_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'STARNNW_NAME'), 'STARNNW_NAME', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerSTARNNW_NAME', False)

    
    STARNNW_NAME = property(__STARNNW_NAME.value, __STARNNW_NAME.set, None, u' Name of the file containing the\n                                neural-network weights for star/galaxy\n                                separation [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}FLAG_IMAGE uses Python identifier FLAG_IMAGE
    __FLAG_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG_IMAGE'), 'FLAG_IMAGE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerFLAG_IMAGE', False)

    
    FLAG_IMAGE = property(__FLAG_IMAGE.value, __FLAG_IMAGE.set, None, u' Filename of the flag-image [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CATALOG_TYPE uses Python identifier CATALOG_TYPE
    __CATALOG_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_TYPE'), 'CATALOG_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerCATALOG_TYPE', False)

    
    CATALOG_TYPE = property(__CATALOG_TYPE.value, __CATALOG_TYPE.set, None, u' Format of the output catalog\n                                (ASCII, ASCII_HEAD, ASCII_SKYCAT, ASCII_VOTABLE,\n                                FITS_1.0, FITS_LDAC) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CHECKIMAGE_TYPE uses Python identifier CHECKIMAGE_TYPE
    __CHECKIMAGE_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_TYPE'), 'CHECKIMAGE_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerCHECKIMAGE_TYPE', False)

    
    CHECKIMAGE_TYPE = property(__CHECKIMAGE_TYPE.value, __CHECKIMAGE_TYPE.set, None, u' Type of information to put in the\n                                check-image (NONE, IDENTICAL, BACKGROUND,\n                                BACKGROUND_RMS, MINIBACKGROUND, MINIBACK_RMS,\n                                -BACKGROUND, FILTERED, OBJECTS, -OBJECTS,\n                                APERTURES, SEGMENTATION) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}ANALYSIS_THRESH uses Python identifier ANALYSIS_THRESH
    __ANALYSIS_THRESH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ANALYSIS_THRESH'), 'ANALYSIS_THRESH', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerANALYSIS_THRESH', False)

    
    ANALYSIS_THRESH = property(__ANALYSIS_THRESH.value, __ANALYSIS_THRESH.set, None, u' Threshold at which CLASS_STAR and\n                                FWHM_ operate [mag / arcsec^2] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}WEIGHT_IMAGE uses Python identifier WEIGHT_IMAGE
    __WEIGHT_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE'), 'WEIGHT_IMAGE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerWEIGHT_IMAGE', False)

    
    WEIGHT_IMAGE = property(__WEIGHT_IMAGE.value, __WEIGHT_IMAGE.set, None, u' Filename of the detection and\n                                measurement weight-image [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CLEAN uses Python identifier CLEAN
    __CLEAN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CLEAN'), 'CLEAN', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerCLEAN', False)

    
    CLEAN = property(__CLEAN.value, __CLEAN.set, None, u' Clean the catalog before writing\n                                to disk (Y, N) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}PHOT_AUTOPARAMS uses Python identifier PHOT_AUTOPARAMS
    __PHOT_AUTOPARAMS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOPARAMS'), 'PHOT_AUTOPARAMS', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerPHOT_AUTOPARAMS', True)

    
    PHOT_AUTOPARAMS = property(__PHOT_AUTOPARAMS.value, __PHOT_AUTOPARAMS.set, None, u' List of MAG_AUTO controls\n                                (scaling parameter k of the first order moment\n                                and minimum R_min in units of A and B) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACK_FILTERSIZE uses Python identifier BACK_FILTERSIZE
    __BACK_FILTERSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE'), 'BACK_FILTERSIZE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerBACK_FILTERSIZE', False)

    
    BACK_FILTERSIZE = property(__BACK_FILTERSIZE.value, __BACK_FILTERSIZE.set, None, u' Size of background filtering mask\n                                [background mesh] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}VERBOSE_TYPE uses Python identifier VERBOSE_TYPE
    __VERBOSE_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE'), 'VERBOSE_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerVERBOSE_TYPE', False)

    
    VERBOSE_TYPE = property(__VERBOSE_TYPE.value, __VERBOSE_TYPE.set, None, u' Verbosity level (QUIET, NORMAL,\n                                EXTRA_WARNINGS, FULL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MAG_GAMMA uses Python identifier MAG_GAMMA
    __MAG_GAMMA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_GAMMA'), 'MAG_GAMMA', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerMAG_GAMMA', False)

    
    MAG_GAMMA = property(__MAG_GAMMA.value, __MAG_GAMMA.set, None, u' Gamma of the emulsion (when\n                                DETECT_TYPE is PHOTO) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACKPHOTO_TYPE uses Python identifier BACKPHOTO_TYPE
    __BACKPHOTO_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_TYPE'), 'BACKPHOTO_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigDetection_httpeuclid_esa_orgschemapromerBACKPHOTO_TYPE', False)

    
    BACKPHOTO_TYPE = property(__BACKPHOTO_TYPE.value, __BACKPHOTO_TYPE.set, None, u' Background used to compute\n                                magnitudes (GLOBAL, LOCAL) [None] ')


    _ElementMap = {
        __CLEAN_PARAM.name() : __CLEAN_PARAM,
        __GAIN.name() : __GAIN,
        __PIXEL_SCALE.name() : __PIXEL_SCALE,
        __BACKPHOTO_THICK.name() : __BACKPHOTO_THICK,
        __DEBLEND_MINCONT.name() : __DEBLEND_MINCONT,
        __MEMORY_BUFSIZE.name() : __MEMORY_BUFSIZE,
        __FLAG_TYPE.name() : __FLAG_TYPE,
        __MAG_ZEROPOINT.name() : __MAG_ZEROPOINT,
        __SEEING_FWHM.name() : __SEEING_FWHM,
        __DEBLEND_NTHRESH.name() : __DEBLEND_NTHRESH,
        __MEMORY_PIXSTACK.name() : __MEMORY_PIXSTACK,
        __MASK_TYPE.name() : __MASK_TYPE,
        __DETECT_MINAREA.name() : __DETECT_MINAREA,
        __THRESH_TYPE.name() : __THRESH_TYPE,
        __BACK_TYPE.name() : __BACK_TYPE,
        __PHOT_APERTURES.name() : __PHOT_APERTURES,
        __DETECT_THRESH.name() : __DETECT_THRESH,
        __FILTER.name() : __FILTER,
        __BACK_VALUE.name() : __BACK_VALUE,
        __DETECT_TYPE.name() : __DETECT_TYPE,
        __PHOT_AUTOAPERS.name() : __PHOT_AUTOAPERS,
        __CATALOG_NAME.name() : __CATALOG_NAME,
        __BACK_SIZE.name() : __BACK_SIZE,
        __WEIGHT_TYPE.name() : __WEIGHT_TYPE,
        __SATUR_LEVEL.name() : __SATUR_LEVEL,
        __PARAMETERS_NAME.name() : __PARAMETERS_NAME,
        __FILTER_NAME.name() : __FILTER_NAME,
        __MEMORY_OBJSTACK.name() : __MEMORY_OBJSTACK,
        __CHECKIMAGE_NAME.name() : __CHECKIMAGE_NAME,
        __STARNNW_NAME.name() : __STARNNW_NAME,
        __FLAG_IMAGE.name() : __FLAG_IMAGE,
        __CATALOG_TYPE.name() : __CATALOG_TYPE,
        __CHECKIMAGE_TYPE.name() : __CHECKIMAGE_TYPE,
        __ANALYSIS_THRESH.name() : __ANALYSIS_THRESH,
        __WEIGHT_IMAGE.name() : __WEIGHT_IMAGE,
        __CLEAN.name() : __CLEAN,
        __PHOT_AUTOPARAMS.name() : __PHOT_AUTOPARAMS,
        __BACK_FILTERSIZE.name() : __BACK_FILTERSIZE,
        __VERBOSE_TYPE.name() : __VERBOSE_TYPE,
        __MAG_GAMMA.name() : __MAG_GAMMA,
        __BACKPHOTO_TYPE.name() : __BACKPHOTO_TYPE
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sextractorConfigDetection', sextractorConfigDetection)


# Complex type objectCatalog with content type ELEMENT_ONLY
class objectCatalog (euclid.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'objectCatalog')
    # Base type is euclid.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', euclid.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', euclid.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.photometryCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = euclid.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = euclid.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'objectCatalog', objectCatalog)


# Complex type calStackVIS with content type ELEMENT_ONLY
class calStackVIS (euclid.dm.bas.img_stub.baseSciFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'calStackVIS')
    # Base type is euclid.dm.bas.img_stub.baseSciFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Template ({http://euclid.esa.org/schema/bas/img}Template) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ObsBlock ({http://euclid.esa.org/schema/bas/img}ObsBlock) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Filter ({http://euclid.esa.org/schema/bas/img}Filter) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Astrom ({http://euclid.esa.org/schema/bas/img}Astrom) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame

    _ElementMap = euclid.dm.bas.img_stub.baseSciFrame._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = euclid.dm.bas.img_stub.baseSciFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'calStackVIS', calStackVIS)


# Complex type calStackNir with content type ELEMENT_ONLY
class calStackNir (euclid.dm.bas.img_stub.baseSciFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'calStackNir')
    # Base type is euclid.dm.bas.img_stub.baseSciFrame
    
    # Element QualityFlags ({http://euclid.esa.org/schema/bas/img}QualityFlags) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Template ({http://euclid.esa.org/schema/bas/img}Template) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame
    
    # Element Naxis2 ({http://euclid.esa.org/schema/bas/img}Naxis2) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Storage ({http://euclid.esa.org/schema/bas/img}Storage) inherited from {http://euclid.esa.org/schema/bas/img}processTargetDataObject
    
    # Element CreationDate ({http://euclid.esa.org/schema/bas/img}CreationDate) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element ImStat ({http://euclid.esa.org/schema/bas/img}ImStat) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element ObsBlock ({http://euclid.esa.org/schema/bas/img}ObsBlock) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame
    
    # Element Instrument ({http://euclid.esa.org/schema/bas/img}Instrument) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element IsValid ({http://euclid.esa.org/schema/bas/img}IsValid) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Filter ({http://euclid.esa.org/schema/bas/img}Filter) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame
    
    # Element ExtObjectId ({http://euclid.esa.org/schema/bas/img}ExtObjectId) inherited from {http://euclid.esa.org/schema/bas/img}processTarget
    
    # Element Naxis1 ({http://euclid.esa.org/schema/bas/img}Naxis1) inherited from {http://euclid.esa.org/schema/bas/img}baseFrame
    
    # Element Astrom ({http://euclid.esa.org/schema/bas/img}Astrom) inherited from {http://euclid.esa.org/schema/bas/img}baseSciFrame

    _ElementMap = euclid.dm.bas.img_stub.baseSciFrame._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = euclid.dm.bas.img_stub.baseSciFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'calStackNir', calStackNir)


# Complex type photometricCatalog with content type ELEMENT_ONLY
class photometricCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photometricCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/mer}SexParam uses Python identifier SexParam
    __SexParam = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexParam'), 'SexParam', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerSexParam', True)

    
    SexParam = property(__SexParam.value, __SexParam.set, None, u' List of parameters derived for each\n                        extracted source [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}ExtObjectId uses Python identifier ExtObjectId
    __ExtObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), 'ExtObjectId', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerExtObjectId', False)

    
    ExtObjectId = property(__ExtObjectId.value, __ExtObjectId.set, None, u' Unique EXT object identifier [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}ZeroPoint uses Python identifier ZeroPoint
    __ZeroPoint = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint'), 'ZeroPoint', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerZeroPoint', False)

    
    ZeroPoint = property(__ZeroPoint.value, __ZeroPoint.set, None, u' Value of the photometric zeropoint [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}Weight uses Python identifier Weight
    __Weight = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Weight'), 'Weight', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerWeight', False)

    
    Weight = property(__Weight.value, __Weight.set, None, u' Information about the detector pixel\n                        weights [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}Threshold uses Python identifier Threshold
    __Threshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Threshold'), 'Threshold', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerThreshold', False)

    
    Threshold = property(__Threshold.value, __Threshold.set, None, u' SExtractor detection threshold [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}Storage uses Python identifier Storage
    __Storage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Storage'), 'Storage', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerStorage', False)

    
    Storage = property(__Storage.value, __Storage.set, None, u' Customized storage container for the data\n                        [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}Seeing uses Python identifier Seeing
    __Seeing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), 'Seeing', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerSeeing', False)

    
    Seeing = property(__Seeing.value, __Seeing.set, None, u' Estimate of seeing using the median FWHM\n                        (filtered to isolate most stellar-like sources) [arcsec] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}WeightScale uses Python identifier WeightScale
    __WeightScale = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WeightScale'), 'WeightScale', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerWeightScale', False)

    
    WeightScale = property(__WeightScale.value, __WeightScale.set, None, u' Weight scale [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}SourceCount uses Python identifier SourceCount
    __SourceCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), 'SourceCount', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerSourceCount', False)

    
    SourceCount = property(__SourceCount.value, __SourceCount.set, None, u' Number of extracted sources [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}Frame uses Python identifier Frame
    __Frame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Frame'), 'Frame', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerFrame', False)

    
    Frame = property(__Frame.value, __Frame.set, None, u' Information about the input frame [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}SexConfig uses Python identifier SexConfig
    __SexConfig = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), 'SexConfig', '__httpeuclid_esa_orgschemapromer_photometricCatalog_httpeuclid_esa_orgschemapromerSexConfig', False)

    
    SexConfig = property(__SexConfig.value, __SexConfig.set, None, u' SExtractor configuration for source\n                        extraction [None] ')


    _ElementMap = {
        __SexParam.name() : __SexParam,
        __ExtObjectId.name() : __ExtObjectId,
        __ZeroPoint.name() : __ZeroPoint,
        __Weight.name() : __Weight,
        __Threshold.name() : __Threshold,
        __Storage.name() : __Storage,
        __Seeing.name() : __Seeing,
        __WeightScale.name() : __WeightScale,
        __SourceCount.name() : __SourceCount,
        __Frame.name() : __Frame,
        __SexConfig.name() : __SexConfig
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'photometricCatalog', photometricCatalog)


# Complex type nirPsfModel with content type ELEMENT_ONLY
class nirPsfModel (euclid.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nirPsfModel')
    # Base type is euclid.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', euclid.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', euclid.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.photometryCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = euclid.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = euclid.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'nirPsfModel', nirPsfModel)


# Complex type sextractorConfigPhotometry with content type ELEMENT_ONLY
class sextractorConfigPhotometry (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sextractorConfigPhotometry')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/mer}MAG_GAMMA uses Python identifier MAG_GAMMA
    __MAG_GAMMA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_GAMMA'), 'MAG_GAMMA', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerMAG_GAMMA', False)

    
    MAG_GAMMA = property(__MAG_GAMMA.value, __MAG_GAMMA.set, None, u' Gamma of the emulsion (when\n                                DETECT_TYPE is PHOTO) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MEMORY_PIXSTACK uses Python identifier MEMORY_PIXSTACK
    __MEMORY_PIXSTACK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_PIXSTACK'), 'MEMORY_PIXSTACK', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerMEMORY_PIXSTACK', False)

    
    MEMORY_PIXSTACK = property(__MEMORY_PIXSTACK.value, __MEMORY_PIXSTACK.set, None, u' Maximum number of pixels that the\n                                pixel-stack can contain [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}SATUR_LEVEL uses Python identifier SATUR_LEVEL
    __SATUR_LEVEL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SATUR_LEVEL'), 'SATUR_LEVEL', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerSATUR_LEVEL', False)

    
    SATUR_LEVEL = property(__SATUR_LEVEL.value, __SATUR_LEVEL.set, None, u' Pixel value above which it is\n                                considered saturated [count] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}DETECT_THRESH uses Python identifier DETECT_THRESH
    __DETECT_THRESH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DETECT_THRESH'), 'DETECT_THRESH', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerDETECT_THRESH', False)

    
    DETECT_THRESH = property(__DETECT_THRESH.value, __DETECT_THRESH.set, None, u' Detection threshold relative to\n                                background RMS (when THRESH_TYPE is RELATIVE)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACKPHOTO_TYPE uses Python identifier BACKPHOTO_TYPE
    __BACKPHOTO_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_TYPE'), 'BACKPHOTO_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerBACKPHOTO_TYPE', False)

    
    BACKPHOTO_TYPE = property(__BACKPHOTO_TYPE.value, __BACKPHOTO_TYPE.set, None, u' Background used to compute\n                                magnitudes (GLOBAL, LOCAL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}DEBLEND_NTHRESH uses Python identifier DEBLEND_NTHRESH
    __DEBLEND_NTHRESH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_NTHRESH'), 'DEBLEND_NTHRESH', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerDEBLEND_NTHRESH', False)

    
    DEBLEND_NTHRESH = property(__DEBLEND_NTHRESH.value, __DEBLEND_NTHRESH.set, None, u' Number of deblending\n                                sub-thresholds [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CHECKIMAGE_NAME uses Python identifier CHECKIMAGE_NAME
    __CHECKIMAGE_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_NAME'), 'CHECKIMAGE_NAME', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerCHECKIMAGE_NAME', False)

    
    CHECKIMAGE_NAME = property(__CHECKIMAGE_NAME.value, __CHECKIMAGE_NAME.set, None, u' Filename for the check-image\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MASK_TYPE uses Python identifier MASK_TYPE
    __MASK_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MASK_TYPE'), 'MASK_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerMASK_TYPE', False)

    
    MASK_TYPE = property(__MASK_TYPE.value, __MASK_TYPE.set, None, u' Method of masking of neighbors\n                                for photometry (NONE, BLANK, CORRECT) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}WEIGHT_TYPE uses Python identifier WEIGHT_TYPE
    __WEIGHT_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE'), 'WEIGHT_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerWEIGHT_TYPE', False)

    
    WEIGHT_TYPE = property(__WEIGHT_TYPE.value, __WEIGHT_TYPE.set, None, u' Weighting scheme for weight-image\n                                (NONE, BACKGROUND, MAP_RMS, MAP_VAR, MAP_WEIGHT)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}DETECT_MINAREA uses Python identifier DETECT_MINAREA
    __DETECT_MINAREA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DETECT_MINAREA'), 'DETECT_MINAREA', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerDETECT_MINAREA', False)

    
    DETECT_MINAREA = property(__DETECT_MINAREA.value, __DETECT_MINAREA.set, None, u' Minimum number of pixels above\n                                threshold triggering detection [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}VERBOSE_TYPE uses Python identifier VERBOSE_TYPE
    __VERBOSE_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE'), 'VERBOSE_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerVERBOSE_TYPE', False)

    
    VERBOSE_TYPE = property(__VERBOSE_TYPE.value, __VERBOSE_TYPE.set, None, u' Verbosity level (QUIET, NORMAL,\n                                EXTRA_WARNINGS, FULL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}GAIN uses Python identifier GAIN
    __GAIN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GAIN'), 'GAIN', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerGAIN', False)

    
    GAIN = property(__GAIN.value, __GAIN.set, None, u' Conversion factor used for error\n                                estimates of CCD magnitudes [electron / ADU] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}PHOT_AUTOAPERS uses Python identifier PHOT_AUTOAPERS
    __PHOT_AUTOAPERS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOAPERS'), 'PHOT_AUTOAPERS', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerPHOT_AUTOAPERS', True)

    
    PHOT_AUTOAPERS = property(__PHOT_AUTOAPERS.value, __PHOT_AUTOAPERS.set, None, u' List of MAG_AUTO minimum circular\n                                aperture diameters (estimation disk, measurement\n                                disk) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MEMORY_BUFSIZE uses Python identifier MEMORY_BUFSIZE
    __MEMORY_BUFSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_BUFSIZE'), 'MEMORY_BUFSIZE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerMEMORY_BUFSIZE', False)

    
    MEMORY_BUFSIZE = property(__MEMORY_BUFSIZE.value, __MEMORY_BUFSIZE.set, None, u' Number of scan-lines in the image\n                                buffer [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}THRESH_TYPE uses Python identifier THRESH_TYPE
    __THRESH_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'THRESH_TYPE'), 'THRESH_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerTHRESH_TYPE', False)

    
    THRESH_TYPE = property(__THRESH_TYPE.value, __THRESH_TYPE.set, None, u' Meaning of DETECT_THRESH and\n                                ANALYSIS_THRESH parameters (RELATIVE, ABSOLUTE)\n                                [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACK_SIZE uses Python identifier BACK_SIZE
    __BACK_SIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE'), 'BACK_SIZE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerBACK_SIZE', False)

    
    BACK_SIZE = property(__BACK_SIZE.value, __BACK_SIZE.set, None, u' Size of a background mesh [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACK_VALUE uses Python identifier BACK_VALUE
    __BACK_VALUE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_VALUE'), 'BACK_VALUE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerBACK_VALUE', True)

    
    BACK_VALUE = property(__BACK_VALUE.value, __BACK_VALUE.set, None, u' List of constant values to be\n                                subtracted from the images if BACK_TYPE is\n                                MANUAL [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}DEBLEND_MINCONT uses Python identifier DEBLEND_MINCONT
    __DEBLEND_MINCONT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_MINCONT'), 'DEBLEND_MINCONT', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerDEBLEND_MINCONT', False)

    
    DEBLEND_MINCONT = property(__DEBLEND_MINCONT.value, __DEBLEND_MINCONT.set, None, u' Minimum contrast parameter for\n                                deblending [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}DETECT_TYPE uses Python identifier DETECT_TYPE
    __DETECT_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DETECT_TYPE'), 'DETECT_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerDETECT_TYPE', False)

    
    DETECT_TYPE = property(__DETECT_TYPE.value, __DETECT_TYPE.set, None, u' Type of device that produced the\n                                image (CCD, PHOTO) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}FLAG_TYPE uses Python identifier FLAG_TYPE
    __FLAG_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG_TYPE'), 'FLAG_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerFLAG_TYPE', False)

    
    FLAG_TYPE = property(__FLAG_TYPE.value, __FLAG_TYPE.set, None, u' Combination method for flags on\n                                the same object (OR, AND, MIN, MAX, MOST) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MEMORY_OBJSTACK uses Python identifier MEMORY_OBJSTACK
    __MEMORY_OBJSTACK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_OBJSTACK'), 'MEMORY_OBJSTACK', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerMEMORY_OBJSTACK', False)

    
    MEMORY_OBJSTACK = property(__MEMORY_OBJSTACK.value, __MEMORY_OBJSTACK.set, None, u' Maximum number of objects that\n                                the object-stack can contain [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CATALOG_NAME uses Python identifier CATALOG_NAME
    __CATALOG_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_NAME'), 'CATALOG_NAME', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerCATALOG_NAME', False)

    
    CATALOG_NAME = property(__CATALOG_NAME.value, __CATALOG_NAME.set, None, u' Name of the output catalog [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}FILTER uses Python identifier FILTER
    __FILTER = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FILTER'), 'FILTER', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerFILTER', False)

    
    FILTER = property(__FILTER.value, __FILTER.set, None, u' Apply filtering to the data\n                                before extraction (Y, N) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}STARNNW_NAME uses Python identifier STARNNW_NAME
    __STARNNW_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'STARNNW_NAME'), 'STARNNW_NAME', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerSTARNNW_NAME', False)

    
    STARNNW_NAME = property(__STARNNW_NAME.value, __STARNNW_NAME.set, None, u' Name of the file containing the\n                                neural-network weights for star/galaxy\n                                separation [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CATALOG_TYPE uses Python identifier CATALOG_TYPE
    __CATALOG_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_TYPE'), 'CATALOG_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerCATALOG_TYPE', False)

    
    CATALOG_TYPE = property(__CATALOG_TYPE.value, __CATALOG_TYPE.set, None, u' Format of the output catalog\n                                (ASCII, ASCII_HEAD, ASCII_SKYCAT, ASCII_VOTABLE,\n                                FITS_1.0, FITS_LDAC) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}PARAMETERS_NAME uses Python identifier PARAMETERS_NAME
    __PARAMETERS_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PARAMETERS_NAME'), 'PARAMETERS_NAME', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerPARAMETERS_NAME', False)

    
    PARAMETERS_NAME = property(__PARAMETERS_NAME.value, __PARAMETERS_NAME.set, None, u' Name of the file containing the\n                                list of parameters that will be computed and put\n                                into the catalog for each object [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}FILTER_NAME uses Python identifier FILTER_NAME
    __FILTER_NAME = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FILTER_NAME'), 'FILTER_NAME', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerFILTER_NAME', False)

    
    FILTER_NAME = property(__FILTER_NAME.value, __FILTER_NAME.set, None, u' Name of file contianing the\n                                filter definition [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}WEIGHT_IMAGE uses Python identifier WEIGHT_IMAGE
    __WEIGHT_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE'), 'WEIGHT_IMAGE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerWEIGHT_IMAGE', False)

    
    WEIGHT_IMAGE = property(__WEIGHT_IMAGE.value, __WEIGHT_IMAGE.set, None, u' Filename of the detection and\n                                measurement weight-image [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}PHOT_APERTURES uses Python identifier PHOT_APERTURES
    __PHOT_APERTURES = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PHOT_APERTURES'), 'PHOT_APERTURES', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerPHOT_APERTURES', False)

    
    PHOT_APERTURES = property(__PHOT_APERTURES.value, __PHOT_APERTURES.set, None, u' MAG_APER aperture diameter\n                                [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}FLAG_IMAGE uses Python identifier FLAG_IMAGE
    __FLAG_IMAGE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FLAG_IMAGE'), 'FLAG_IMAGE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerFLAG_IMAGE', False)

    
    FLAG_IMAGE = property(__FLAG_IMAGE.value, __FLAG_IMAGE.set, None, u' Filename of the flag-image [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CHECKIMAGE_TYPE uses Python identifier CHECKIMAGE_TYPE
    __CHECKIMAGE_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_TYPE'), 'CHECKIMAGE_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerCHECKIMAGE_TYPE', False)

    
    CHECKIMAGE_TYPE = property(__CHECKIMAGE_TYPE.value, __CHECKIMAGE_TYPE.set, None, u' Type of information to put in the\n                                check-image (NONE, IDENTICAL, BACKGROUND,\n                                BACKGROUND_RMS, MINIBACKGROUND, MINIBACK_RMS,\n                                -BACKGROUND, FILTERED, OBJECTS, -OBJECTS,\n                                APERTURES, SEGMENTATION) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}PHOT_AUTOPARAMS uses Python identifier PHOT_AUTOPARAMS
    __PHOT_AUTOPARAMS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOPARAMS'), 'PHOT_AUTOPARAMS', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerPHOT_AUTOPARAMS', True)

    
    PHOT_AUTOPARAMS = property(__PHOT_AUTOPARAMS.value, __PHOT_AUTOPARAMS.set, None, u' List of MAG_AUTO controls\n                                (scaling parameter k of the first order moment\n                                and minimum R_min in units of A and B) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}MAG_ZEROPOINT uses Python identifier MAG_ZEROPOINT
    __MAG_ZEROPOINT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MAG_ZEROPOINT'), 'MAG_ZEROPOINT', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerMAG_ZEROPOINT', False)

    
    MAG_ZEROPOINT = property(__MAG_ZEROPOINT.value, __MAG_ZEROPOINT.set, None, u' Zero-point offset to be applied\n                                to magnitudes [mag] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}ANALYSIS_THRESH uses Python identifier ANALYSIS_THRESH
    __ANALYSIS_THRESH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ANALYSIS_THRESH'), 'ANALYSIS_THRESH', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerANALYSIS_THRESH', False)

    
    ANALYSIS_THRESH = property(__ANALYSIS_THRESH.value, __ANALYSIS_THRESH.set, None, u' Threshold at which CLASS_STAR and\n                                FWHM_ operate [mag / arcsec^2] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CLEAN_PARAM uses Python identifier CLEAN_PARAM
    __CLEAN_PARAM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CLEAN_PARAM'), 'CLEAN_PARAM', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerCLEAN_PARAM', False)

    
    CLEAN_PARAM = property(__CLEAN_PARAM.value, __CLEAN_PARAM.set, None, u' Efficiency of cleaning [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}CLEAN uses Python identifier CLEAN
    __CLEAN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CLEAN'), 'CLEAN', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerCLEAN', False)

    
    CLEAN = property(__CLEAN.value, __CLEAN.set, None, u' Clean the catalog before writing\n                                to disk (Y, N) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACK_FILTERSIZE uses Python identifier BACK_FILTERSIZE
    __BACK_FILTERSIZE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE'), 'BACK_FILTERSIZE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerBACK_FILTERSIZE', False)

    
    BACK_FILTERSIZE = property(__BACK_FILTERSIZE.value, __BACK_FILTERSIZE.set, None, u' Size of background filtering mask\n                                [background mesh] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACK_TYPE uses Python identifier BACK_TYPE
    __BACK_TYPE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE'), 'BACK_TYPE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerBACK_TYPE', False)

    
    BACK_TYPE = property(__BACK_TYPE.value, __BACK_TYPE.set, None, u' Type of background subtracted\n                                from the images (AUTO, MANUAL) [None] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}BACKPHOTO_THICK uses Python identifier BACKPHOTO_THICK
    __BACKPHOTO_THICK = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_THICK'), 'BACKPHOTO_THICK', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerBACKPHOTO_THICK', False)

    
    BACKPHOTO_THICK = property(__BACKPHOTO_THICK.value, __BACKPHOTO_THICK.set, None, u' Thickness of the background LOCAL\n                                annulus [pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}PIXEL_SCALE uses Python identifier PIXEL_SCALE
    __PIXEL_SCALE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE'), 'PIXEL_SCALE', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerPIXEL_SCALE', False)

    
    PIXEL_SCALE = property(__PIXEL_SCALE.value, __PIXEL_SCALE.set, None, u' Pixel size [arcsec / pixel] ')

    
    # Element {http://euclid.esa.org/schema/pro/mer}SEEING_FWHM uses Python identifier SEEING_FWHM
    __SEEING_FWHM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SEEING_FWHM'), 'SEEING_FWHM', '__httpeuclid_esa_orgschemapromer_sextractorConfigPhotometry_httpeuclid_esa_orgschemapromerSEEING_FWHM', False)

    
    SEEING_FWHM = property(__SEEING_FWHM.value, __SEEING_FWHM.set, None, u' FWHM of stellar sources (for\n                                star/galaxy separation only) [arcsec] ')


    _ElementMap = {
        __MAG_GAMMA.name() : __MAG_GAMMA,
        __MEMORY_PIXSTACK.name() : __MEMORY_PIXSTACK,
        __SATUR_LEVEL.name() : __SATUR_LEVEL,
        __DETECT_THRESH.name() : __DETECT_THRESH,
        __BACKPHOTO_TYPE.name() : __BACKPHOTO_TYPE,
        __DEBLEND_NTHRESH.name() : __DEBLEND_NTHRESH,
        __CHECKIMAGE_NAME.name() : __CHECKIMAGE_NAME,
        __MASK_TYPE.name() : __MASK_TYPE,
        __WEIGHT_TYPE.name() : __WEIGHT_TYPE,
        __DETECT_MINAREA.name() : __DETECT_MINAREA,
        __VERBOSE_TYPE.name() : __VERBOSE_TYPE,
        __GAIN.name() : __GAIN,
        __PHOT_AUTOAPERS.name() : __PHOT_AUTOAPERS,
        __MEMORY_BUFSIZE.name() : __MEMORY_BUFSIZE,
        __THRESH_TYPE.name() : __THRESH_TYPE,
        __BACK_SIZE.name() : __BACK_SIZE,
        __BACK_VALUE.name() : __BACK_VALUE,
        __DEBLEND_MINCONT.name() : __DEBLEND_MINCONT,
        __DETECT_TYPE.name() : __DETECT_TYPE,
        __FLAG_TYPE.name() : __FLAG_TYPE,
        __MEMORY_OBJSTACK.name() : __MEMORY_OBJSTACK,
        __CATALOG_NAME.name() : __CATALOG_NAME,
        __FILTER.name() : __FILTER,
        __STARNNW_NAME.name() : __STARNNW_NAME,
        __CATALOG_TYPE.name() : __CATALOG_TYPE,
        __PARAMETERS_NAME.name() : __PARAMETERS_NAME,
        __FILTER_NAME.name() : __FILTER_NAME,
        __WEIGHT_IMAGE.name() : __WEIGHT_IMAGE,
        __PHOT_APERTURES.name() : __PHOT_APERTURES,
        __FLAG_IMAGE.name() : __FLAG_IMAGE,
        __CHECKIMAGE_TYPE.name() : __CHECKIMAGE_TYPE,
        __PHOT_AUTOPARAMS.name() : __PHOT_AUTOPARAMS,
        __MAG_ZEROPOINT.name() : __MAG_ZEROPOINT,
        __ANALYSIS_THRESH.name() : __ANALYSIS_THRESH,
        __CLEAN_PARAM.name() : __CLEAN_PARAM,
        __CLEAN.name() : __CLEAN,
        __BACK_FILTERSIZE.name() : __BACK_FILTERSIZE,
        __BACK_TYPE.name() : __BACK_TYPE,
        __BACKPHOTO_THICK.name() : __BACKPHOTO_THICK,
        __PIXEL_SCALE.name() : __PIXEL_SCALE,
        __SEEING_FWHM.name() : __SEEING_FWHM
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sextractorConfigPhotometry', sextractorConfigPhotometry)


# Complex type extPsfModel with content type ELEMENT_ONLY
class extPsfModel (euclid.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'extPsfModel')
    # Base type is euclid.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', euclid.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', euclid.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.photometryCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = euclid.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = euclid.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'extPsfModel', extPsfModel)



extCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(extCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
extCatalog._ContentModel = pyxb.binding.content.ParticleModel(extCatalog._GroupModel, min_occurs=1, max_occurs=1)


calStackExt._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
calStackExt._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
calStackExt._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackExt._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._GroupModel_4, min_occurs=1, max_occurs=1)
    )
calStackExt._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
calStackExt._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackExt._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._GroupModel_5, min_occurs=1, max_occurs=1)
    )
calStackExt._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Astrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Template')), min_occurs=1, max_occurs=1)
    )
calStackExt._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackExt._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackExt._GroupModel_6, min_occurs=1, max_occurs=1)
    )
calStackExt._ContentModel = pyxb.binding.content.ParticleModel(calStackExt._GroupModel, min_occurs=1, max_occurs=1)


visCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
visCatalog._ContentModel = pyxb.binding.content.ParticleModel(visCatalog._GroupModel, min_occurs=1, max_occurs=1)


nirCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nirCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
nirCatalog._ContentModel = pyxb.binding.content.ParticleModel(nirCatalog._GroupModel, min_occurs=1, max_occurs=1)


visPsfModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visPsfModel._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
visPsfModel._ContentModel = pyxb.binding.content.ParticleModel(visPsfModel._GroupModel, min_occurs=1, max_occurs=1)



VIScalibratedImages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'VIScalibratedImage'), euclid.dm.bas.fit_stub.fitsFile, scope=VIScalibratedImages))

VIScalibratedImages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'depth'), euclid.dm.bas.dtd_stub.double1Type, scope=VIScalibratedImages))
VIScalibratedImages._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(VIScalibratedImages._UseForTag(pyxb.namespace.ExpandedName(None, u'depth')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(VIScalibratedImages._UseForTag(pyxb.namespace.ExpandedName(None, u'VIScalibratedImage')), min_occurs=1, max_occurs=1)
    )
VIScalibratedImages._ContentModel = pyxb.binding.content.ParticleModel(VIScalibratedImages._GroupModel, min_occurs=1, max_occurs=1)



objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexParam'), pyxb.binding.datatypes.string, scope=objectCandidateList, documentation=u' List of parameters derived for each\n                        extracted source [None] '))

objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=objectCandidateList, documentation=u' Unique EXT object identifier [None] '))

objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Storage'), euclid.dm.sys.sgs_stub.dataContainer, scope=objectCandidateList, documentation=u' Customized storage container for the data\n                        [None] '))

objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WeightScale'), pyxb.binding.datatypes.float, scope=objectCandidateList, documentation=u' Weight scale [None] '))

objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Weight'), euclid.dm.bas.img_stub.baseFrame, scope=objectCandidateList, documentation=u' Information about the detector pixel\n                        weights [None] '))

objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), pyxb.binding.datatypes.int, scope=objectCandidateList, documentation=u' Number of extracted sources [None] '))

objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Threshold'), pyxb.binding.datatypes.float, scope=objectCandidateList, documentation=u' SExtractor detection threshold [None] '))

objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), sextractorConfigDetection, scope=objectCandidateList, documentation=u' SExtractor configuration for source\n                        extraction [None] '))

objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), pyxb.binding.datatypes.float, scope=objectCandidateList, documentation=u' Estimate of seeing using the median FWHM\n                        (filtered to isolate most stellar-like sources) [arcsec] '))

objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Frame'), euclid.dm.bas.img_stub.baseFrame, scope=objectCandidateList, documentation=u' Information about the input frame [None] '))

objectCandidateList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint'), pyxb.binding.datatypes.float, scope=objectCandidateList, documentation=u' Value of the photometric zeropoint [mag] '))
objectCandidateList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Weight')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Seeing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Threshold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WeightScale')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexConfig')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(objectCandidateList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexParam')), min_occurs=0L, max_occurs=None)
    )
objectCandidateList._ContentModel = pyxb.binding.content.ParticleModel(objectCandidateList._GroupModel, min_occurs=1, max_occurs=1)



sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CLEAN_PARAM'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' Efficiency of cleaning [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GAIN'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' Conversion factor used for error\n                                estimates of CCD magnitudes [electron / ADU] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' Pixel size [arcsec / pixel] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_THICK'), pyxb.binding.datatypes.int, scope=sextractorConfigDetection, documentation=u' Thickness of the background LOCAL\n                                annulus [pixel] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_MINCONT'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' Minimum contrast parameter for\n                                deblending [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_BUFSIZE'), pyxb.binding.datatypes.int, scope=sextractorConfigDetection, documentation=u' Number of scan-lines in the image\n                                buffer [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Combination method for flags on\n                                the same object (OR, AND, MIN, MAX, MOST) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_ZEROPOINT'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' Zero-point offset to be applied\n                                to magnitudes [mag] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SEEING_FWHM'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' FWHM of stellar sources (for\n                                star/galaxy separation only) [arcsec] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_NTHRESH'), pyxb.binding.datatypes.int, scope=sextractorConfigDetection, documentation=u' Number of deblending\n                                sub-thresholds [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_PIXSTACK'), pyxb.binding.datatypes.int, scope=sextractorConfigDetection, documentation=u' Maximum number of pixels that the\n                                pixel-stack can contain [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MASK_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Method of masking of neighbors\n                                for photometry (NONE, BLANK, CORRECT) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DETECT_MINAREA'), pyxb.binding.datatypes.int, scope=sextractorConfigDetection, documentation=u' Minimum number of pixels above\n                                threshold triggering detection [pixel] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'THRESH_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Meaning of DETECT_THRESH and\n                                ANALYSIS_THRESH parameters (RELATIVE, ABSOLUTE)\n                                [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Type of background subtracted\n                                from the images (AUTO, MANUAL) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHOT_APERTURES'), pyxb.binding.datatypes.int, scope=sextractorConfigDetection, documentation=u' MAG_APER aperture diameter\n                                [pixel] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DETECT_THRESH'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' Detection threshold relative to\n                                background RMS (when THRESH_TYPE is RELATIVE)\n                                [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FILTER'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Apply filtering to the data\n                                before extraction (Y, N) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_VALUE'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' List of constant values to be\n                                subtracted from the images if BACK_TYPE is\n                                MANUAL [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DETECT_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Type of device that produced the\n                                image (CCD, PHOTO) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOAPERS'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' List of MAG_AUTO minimum circular\n                                aperture diameters (estimation disk, measurement\n                                disk) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Name of the output catalog [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE'), pyxb.binding.datatypes.int, scope=sextractorConfigDetection, documentation=u' Size of a background mesh [pixel] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Weighting scheme for weight-image\n                                (NONE, BACKGROUND, MAP_RMS, MAP_VAR, MAP_WEIGHT)\n                                [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SATUR_LEVEL'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' Pixel value above which it is\n                                considered saturated [count] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PARAMETERS_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Name of the file containing the\n                                list of parameters that will be computed and put\n                                into the catalog for each object [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FILTER_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Name of file contianing the\n                                filter definition [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_OBJSTACK'), pyxb.binding.datatypes.int, scope=sextractorConfigDetection, documentation=u' Maximum number of objects that\n                                the object-stack can contain [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Filename for the check-image\n                                [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'STARNNW_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Name of the file containing the\n                                neural-network weights for star/galaxy\n                                separation [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG_IMAGE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Filename of the flag-image [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Format of the output catalog\n                                (ASCII, ASCII_HEAD, ASCII_SKYCAT, ASCII_VOTABLE,\n                                FITS_1.0, FITS_LDAC) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Type of information to put in the\n                                check-image (NONE, IDENTICAL, BACKGROUND,\n                                BACKGROUND_RMS, MINIBACKGROUND, MINIBACK_RMS,\n                                -BACKGROUND, FILTERED, OBJECTS, -OBJECTS,\n                                APERTURES, SEGMENTATION) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ANALYSIS_THRESH'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' Threshold at which CLASS_STAR and\n                                FWHM_ operate [mag / arcsec^2] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Filename of the detection and\n                                measurement weight-image [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CLEAN'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Clean the catalog before writing\n                                to disk (Y, N) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOPARAMS'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' List of MAG_AUTO controls\n                                (scaling parameter k of the first order moment\n                                and minimum R_min in units of A and B) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE'), pyxb.binding.datatypes.int, scope=sextractorConfigDetection, documentation=u' Size of background filtering mask\n                                [background mesh] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Verbosity level (QUIET, NORMAL,\n                                EXTRA_WARNINGS, FULL) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_GAMMA'), pyxb.binding.datatypes.float, scope=sextractorConfigDetection, documentation=u' Gamma of the emulsion (when\n                                DETECT_TYPE is PHOTO) [None] '))

sextractorConfigDetection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigDetection, documentation=u' Background used to compute\n                                magnitudes (GLOBAL, LOCAL) [None] '))
sextractorConfigDetection._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ANALYSIS_THRESH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_THICK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_VALUE')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CLEAN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CLEAN_PARAM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_MINCONT')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_NTHRESH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DETECT_MINAREA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DETECT_THRESH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DETECT_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FILTER')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FILTER_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLAG_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLAG_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GAIN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAG_GAMMA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAG_ZEROPOINT')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MASK_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_BUFSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_OBJSTACK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_PIXSTACK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PARAMETERS_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PHOT_APERTURES')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOPARAMS')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOAPERS')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SATUR_LEVEL')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SEEING_FWHM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'STARNNW_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'THRESH_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigDetection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE')), min_occurs=1, max_occurs=1)
    )
sextractorConfigDetection._ContentModel = pyxb.binding.content.ParticleModel(sextractorConfigDetection._GroupModel, min_occurs=1, max_occurs=1)


objectCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(objectCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
objectCatalog._ContentModel = pyxb.binding.content.ParticleModel(objectCatalog._GroupModel, min_occurs=1, max_occurs=1)


calStackVIS._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
calStackVIS._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
calStackVIS._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackVIS._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._GroupModel_4, min_occurs=1, max_occurs=1)
    )
calStackVIS._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
calStackVIS._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackVIS._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._GroupModel_5, min_occurs=1, max_occurs=1)
    )
calStackVIS._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Astrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Template')), min_occurs=1, max_occurs=1)
    )
calStackVIS._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackVIS._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackVIS._GroupModel_6, min_occurs=1, max_occurs=1)
    )
calStackVIS._ContentModel = pyxb.binding.content.ParticleModel(calStackVIS._GroupModel, min_occurs=1, max_occurs=1)


calStackNir._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'IsValid')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'QualityFlags')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'CreationDate')), min_occurs=1, max_occurs=1)
    )
calStackNir._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Storage')), min_occurs=1, max_occurs=1)
    )
calStackNir._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackNir._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._GroupModel_4, min_occurs=1, max_occurs=1)
    )
calStackNir._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Instrument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Naxis2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ImStat')), min_occurs=1, max_occurs=1)
    )
calStackNir._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackNir._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._GroupModel_5, min_occurs=1, max_occurs=1)
    )
calStackNir._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Filter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Astrom')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'ObsBlock')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/img'), u'Template')), min_occurs=1, max_occurs=1)
    )
calStackNir._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calStackNir._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calStackNir._GroupModel_6, min_occurs=1, max_occurs=1)
    )
calStackNir._ContentModel = pyxb.binding.content.ParticleModel(calStackNir._GroupModel, min_occurs=1, max_occurs=1)



photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexParam'), pyxb.binding.datatypes.string, scope=photometricCatalog, documentation=u' List of parameters derived for each\n                        extracted source [None] '))

photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId'), euclid.dm.bas_stub.extObjectId, scope=photometricCatalog, documentation=u' Unique EXT object identifier [None] '))

photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint'), pyxb.binding.datatypes.float, scope=photometricCatalog, documentation=u' Value of the photometric zeropoint [mag] '))

photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Weight'), euclid.dm.bas.img_stub.baseFrame, scope=photometricCatalog, documentation=u' Information about the detector pixel\n                        weights [None] '))

photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Threshold'), pyxb.binding.datatypes.float, scope=photometricCatalog, documentation=u' SExtractor detection threshold [None] '))

photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Storage'), euclid.dm.sys.sgs_stub.dataContainer, scope=photometricCatalog, documentation=u' Customized storage container for the data\n                        [None] '))

photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Seeing'), pyxb.binding.datatypes.float, scope=photometricCatalog, documentation=u' Estimate of seeing using the median FWHM\n                        (filtered to isolate most stellar-like sources) [arcsec] '))

photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WeightScale'), pyxb.binding.datatypes.float, scope=photometricCatalog, documentation=u' Weight scale [None] '))

photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SourceCount'), pyxb.binding.datatypes.int, scope=photometricCatalog, documentation=u' Number of extracted sources [None] '))

photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Frame'), euclid.dm.bas.img_stub.baseFrame, scope=photometricCatalog, documentation=u' Information about the input frame [None] '))

photometricCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SexConfig'), sextractorConfigDetection, scope=photometricCatalog, documentation=u' SExtractor configuration for source\n                        extraction [None] '))
photometricCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Storage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Weight')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Seeing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ZeroPoint')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Threshold')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SourceCount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WeightScale')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexConfig')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(photometricCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SexParam')), min_occurs=0L, max_occurs=None)
    )
photometricCatalog._ContentModel = pyxb.binding.content.ParticleModel(photometricCatalog._GroupModel, min_occurs=1, max_occurs=1)


nirPsfModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nirPsfModel._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
nirPsfModel._ContentModel = pyxb.binding.content.ParticleModel(nirPsfModel._GroupModel, min_occurs=1, max_occurs=1)



sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_GAMMA'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' Gamma of the emulsion (when\n                                DETECT_TYPE is PHOTO) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_PIXSTACK'), pyxb.binding.datatypes.int, scope=sextractorConfigPhotometry, documentation=u' Maximum number of pixels that the\n                                pixel-stack can contain [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SATUR_LEVEL'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' Pixel value above which it is\n                                considered saturated [count] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DETECT_THRESH'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' Detection threshold relative to\n                                background RMS (when THRESH_TYPE is RELATIVE)\n                                [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Background used to compute\n                                magnitudes (GLOBAL, LOCAL) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_NTHRESH'), pyxb.binding.datatypes.int, scope=sextractorConfigPhotometry, documentation=u' Number of deblending\n                                sub-thresholds [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Filename for the check-image\n                                [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MASK_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Method of masking of neighbors\n                                for photometry (NONE, BLANK, CORRECT) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Weighting scheme for weight-image\n                                (NONE, BACKGROUND, MAP_RMS, MAP_VAR, MAP_WEIGHT)\n                                [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DETECT_MINAREA'), pyxb.binding.datatypes.int, scope=sextractorConfigPhotometry, documentation=u' Minimum number of pixels above\n                                threshold triggering detection [pixel] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Verbosity level (QUIET, NORMAL,\n                                EXTRA_WARNINGS, FULL) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GAIN'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' Conversion factor used for error\n                                estimates of CCD magnitudes [electron / ADU] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOAPERS'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' List of MAG_AUTO minimum circular\n                                aperture diameters (estimation disk, measurement\n                                disk) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_BUFSIZE'), pyxb.binding.datatypes.int, scope=sextractorConfigPhotometry, documentation=u' Number of scan-lines in the image\n                                buffer [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'THRESH_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Meaning of DETECT_THRESH and\n                                ANALYSIS_THRESH parameters (RELATIVE, ABSOLUTE)\n                                [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE'), pyxb.binding.datatypes.int, scope=sextractorConfigPhotometry, documentation=u' Size of a background mesh [pixel] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_VALUE'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' List of constant values to be\n                                subtracted from the images if BACK_TYPE is\n                                MANUAL [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_MINCONT'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' Minimum contrast parameter for\n                                deblending [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DETECT_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Type of device that produced the\n                                image (CCD, PHOTO) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Combination method for flags on\n                                the same object (OR, AND, MIN, MAX, MOST) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_OBJSTACK'), pyxb.binding.datatypes.int, scope=sextractorConfigPhotometry, documentation=u' Maximum number of objects that\n                                the object-stack can contain [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Name of the output catalog [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FILTER'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Apply filtering to the data\n                                before extraction (Y, N) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'STARNNW_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Name of the file containing the\n                                neural-network weights for star/galaxy\n                                separation [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Format of the output catalog\n                                (ASCII, ASCII_HEAD, ASCII_SKYCAT, ASCII_VOTABLE,\n                                FITS_1.0, FITS_LDAC) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PARAMETERS_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Name of the file containing the\n                                list of parameters that will be computed and put\n                                into the catalog for each object [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FILTER_NAME'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Name of file contianing the\n                                filter definition [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Filename of the detection and\n                                measurement weight-image [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHOT_APERTURES'), pyxb.binding.datatypes.int, scope=sextractorConfigPhotometry, documentation=u' MAG_APER aperture diameter\n                                [pixel] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FLAG_IMAGE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Filename of the flag-image [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Type of information to put in the\n                                check-image (NONE, IDENTICAL, BACKGROUND,\n                                BACKGROUND_RMS, MINIBACKGROUND, MINIBACK_RMS,\n                                -BACKGROUND, FILTERED, OBJECTS, -OBJECTS,\n                                APERTURES, SEGMENTATION) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOPARAMS'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' List of MAG_AUTO controls\n                                (scaling parameter k of the first order moment\n                                and minimum R_min in units of A and B) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MAG_ZEROPOINT'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' Zero-point offset to be applied\n                                to magnitudes [mag] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ANALYSIS_THRESH'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' Threshold at which CLASS_STAR and\n                                FWHM_ operate [mag / arcsec^2] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CLEAN_PARAM'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' Efficiency of cleaning [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CLEAN'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Clean the catalog before writing\n                                to disk (Y, N) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE'), pyxb.binding.datatypes.int, scope=sextractorConfigPhotometry, documentation=u' Size of background filtering mask\n                                [background mesh] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE'), pyxb.binding.datatypes.string, scope=sextractorConfigPhotometry, documentation=u' Type of background subtracted\n                                from the images (AUTO, MANUAL) [None] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_THICK'), pyxb.binding.datatypes.int, scope=sextractorConfigPhotometry, documentation=u' Thickness of the background LOCAL\n                                annulus [pixel] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' Pixel size [arcsec / pixel] '))

sextractorConfigPhotometry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SEEING_FWHM'), pyxb.binding.datatypes.float, scope=sextractorConfigPhotometry, documentation=u' FWHM of stellar sources (for\n                                star/galaxy separation only) [arcsec] '))
sextractorConfigPhotometry._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VERBOSE_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ANALYSIS_THRESH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_FILTERSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_THICK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACKPHOTO_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_SIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BACK_VALUE')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CATALOG_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CHECKIMAGE_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CLEAN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CLEAN_PARAM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_MINCONT')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEBLEND_NTHRESH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DETECT_MINAREA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DETECT_THRESH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DETECT_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FILTER')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FILTER_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLAG_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FLAG_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GAIN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAG_GAMMA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MAG_ZEROPOINT')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MASK_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_BUFSIZE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_OBJSTACK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMORY_PIXSTACK')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PARAMETERS_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PHOT_APERTURES')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOPARAMS')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PHOT_AUTOAPERS')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PIXEL_SCALE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SATUR_LEVEL')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SEEING_FWHM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'STARNNW_NAME')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'THRESH_TYPE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_IMAGE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WEIGHT_TYPE')), min_occurs=1, max_occurs=1)
    )
sextractorConfigPhotometry._ContentModel = pyxb.binding.content.ParticleModel(sextractorConfigPhotometry._GroupModel, min_occurs=1, max_occurs=1)


extPsfModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(extPsfModel._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
extPsfModel._ContentModel = pyxb.binding.content.ParticleModel(extPsfModel._GroupModel, min_occurs=1, max_occurs=1)
