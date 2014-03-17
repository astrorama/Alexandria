# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/pro/she_stub.py
# PyXB bindings for NamespaceModule
# NSM:7ac221f0a61cca2444b05519f207d18957d4a1cb
# Generated 2014-03-17 18:50:36.639432 by PyXB version 1.1.2
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
import CommonDM.dm.bas.fit_stub
import CommonDM.dm.sys.sgs_stub
import CommonDM.dm.bas.dtd_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/she', create_if_missing=True)
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


# Complex type slPhotoZCatalog with content type ELEMENT_ONLY
class slPhotoZCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slPhotoZCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slPhotoZCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slPhotoZCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slPhotoZCatalog', slPhotoZCatalog)


# Complex type merCatalog with content type ELEMENT_ONLY
class merCatalog (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'merCatalog')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sl.merCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'merCatalog', merCatalog)


# Complex type slShearCatalog with content type ELEMENT_ONLY
class slShearCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slShearCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slShearCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slShearCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slShearCatalog', slShearCatalog)


# Complex type slExtFrame with content type ELEMENT_ONLY
class slExtFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slExtFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slExtFrame_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slExtFrame_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slExtFrame', slExtFrame)


# Complex type slPreSelectionParameters with content type ELEMENT_ONLY
class slPreSelectionParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slPreSelectionParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slPreSelectionParameters_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slPreSelectionParameters_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slPreSelectionParameters', slPreSelectionParameters)


# Complex type slNirFitsStamp with content type ELEMENT_ONLY
class slNirFitsStamp (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slNirFitsStamp')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slNirFitsStamp_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slNirFitsStamp_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slNirFitsStamp', slNirFitsStamp)


# Complex type lensQuasarSubtractedStamp with content type ELEMENT_ONLY
class lensQuasarSubtractedStamp (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lensQuasarSubtractedStamp')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sl.subtractedImage', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'lensQuasarSubtractedStamp', lensQuasarSubtractedStamp)


# Complex type preSelectedCatalog with content type ELEMENT_ONLY
class preSelectedCatalog (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'preSelectedCatalog')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sl.preSelectedCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'preSelectedCatalog', preSelectedCatalog)


# Complex type shearMeasurementData with content type ELEMENT_ONLY
class shearMeasurementData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shearMeasurementData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ShearRMS uses Python identifier ShearRMS
    __ShearRMS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ShearRMS'), 'ShearRMS', '__httpeuclid_esa_orgschemaproshe_shearMeasurementData_ShearRMS', False)

    
    ShearRMS = property(__ShearRMS.value, __ShearRMS.set, None, None)

    
    # Element ShearMean uses Python identifier ShearMean
    __ShearMean = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ShearMean'), 'ShearMean', '__httpeuclid_esa_orgschemaproshe_shearMeasurementData_ShearMean', False)

    
    ShearMean = property(__ShearMean.value, __ShearMean.set, None, None)


    _ElementMap = {
        __ShearRMS.name() : __ShearRMS,
        __ShearMean.name() : __ShearMean
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'shearMeasurementData', shearMeasurementData)


# Complex type visCalibratedImageAndMaskData with content type ELEMENT_ONLY
class visCalibratedImageAndMaskData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visCalibratedImageAndMaskData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RaDecCommanding uses Python identifier RaDecCommanding
    __RaDecCommanding = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'RaDecCommanding'), 'RaDecCommanding', '__httpeuclid_esa_orgschemaproshe_visCalibratedImageAndMaskData_RaDecCommanding', False)

    
    RaDecCommanding = property(__RaDecCommanding.value, __RaDecCommanding.set, None, None)

    
    # Element VisCalibratedImage uses Python identifier VisCalibratedImage
    __VisCalibratedImage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'VisCalibratedImage'), 'VisCalibratedImage', '__httpeuclid_esa_orgschemaproshe_visCalibratedImageAndMaskData_VisCalibratedImage', False)

    
    VisCalibratedImage = property(__VisCalibratedImage.value, __VisCalibratedImage.set, None, None)

    
    # Element ObservationId uses Python identifier ObservationId
    __ObservationId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ObservationId'), 'ObservationId', '__httpeuclid_esa_orgschemaproshe_visCalibratedImageAndMaskData_ObservationId', False)

    
    ObservationId = property(__ObservationId.value, __ObservationId.set, None, None)

    
    # Element VisCalibratedImageMask uses Python identifier VisCalibratedImageMask
    __VisCalibratedImageMask = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'VisCalibratedImageMask'), 'VisCalibratedImageMask', '__httpeuclid_esa_orgschemaproshe_visCalibratedImageAndMaskData_VisCalibratedImageMask', False)

    
    VisCalibratedImageMask = property(__VisCalibratedImageMask.value, __VisCalibratedImageMask.set, None, None)


    _ElementMap = {
        __RaDecCommanding.name() : __RaDecCommanding,
        __VisCalibratedImage.name() : __VisCalibratedImage,
        __ObservationId.name() : __ObservationId,
        __VisCalibratedImageMask.name() : __VisCalibratedImageMask
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'visCalibratedImageAndMaskData', visCalibratedImageAndMaskData)


# Complex type slExtFitsStamp with content type ELEMENT_ONLY
class slExtFitsStamp (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slExtFitsStamp')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slExtFitsStamp_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slExtFitsStamp_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slExtFitsStamp', slExtFitsStamp)


# Complex type slSpecZCatalog with content type ELEMENT_ONLY
class slSpecZCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slSpecZCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slSpecZCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slSpecZCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slSpecZCatalog', slSpecZCatalog)


# Complex type slInspectionParameters with content type ELEMENT_ONLY
class slInspectionParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slInspectionParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slInspectionParameters_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slInspectionParameters_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slInspectionParameters', slInspectionParameters)


# Complex type slVisFitsStamp with content type ELEMENT_ONLY
class slVisFitsStamp (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slVisFitsStamp')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slVisFitsStamp_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slVisFitsStamp_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slVisFitsStamp', slVisFitsStamp)


# Complex type slPreSelectedCatalog with content type ELEMENT_ONLY
class slPreSelectedCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slPreSelectedCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slPreSelectedCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slPreSelectedCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slPreSelectedCatalog', slPreSelectedCatalog)


# Complex type lensCandidatesCatalog with content type ELEMENT_ONLY
class lensCandidatesCatalog (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lensCandidatesCatalog')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sl.lensCandidatesCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'lensCandidatesCatalog', lensCandidatesCatalog)


# Complex type specZCatalog with content type ELEMENT_ONLY
class specZCatalog (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'specZCatalog')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sl.specZCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'specZCatalog', specZCatalog)


# Complex type sl2DSpectrum with content type ELEMENT_ONLY
class sl2DSpectrum (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sl2DSpectrum')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_sl2DSpectrum_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_sl2DSpectrum_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sl2DSpectrum', sl2DSpectrum)


# Complex type slVisPsfModel with content type ELEMENT_ONLY
class slVisPsfModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slVisPsfModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slVisPsfModel_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slVisPsfModel_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slVisPsfModel', slVisPsfModel)


# Complex type slMerCatalog with content type ELEMENT_ONLY
class slMerCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slMerCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slMerCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slMerCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slMerCatalog', slMerCatalog)


# Complex type slLensQuasarSubtractedStamps with content type ELEMENT_ONLY
class slLensQuasarSubtractedStamps (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slLensQuasarSubtractedStamps')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slLensQuasarSubtractedStamps_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slLensQuasarSubtractedStamps_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slLensQuasarSubtractedStamps', slLensQuasarSubtractedStamps)


# Complex type slExtPsfModel with content type ELEMENT_ONLY
class slExtPsfModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slExtPsfModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slExtPsfModel_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slExtPsfModel_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slExtPsfModel', slExtPsfModel)


# Complex type slPhysicalParametersCatalog with content type ELEMENT_ONLY
class slPhysicalParametersCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slPhysicalParametersCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slPhysicalParametersCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slPhysicalParametersCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slPhysicalParametersCatalog', slPhysicalParametersCatalog)


# Complex type slLensCandidatesCatalog with content type ELEMENT_ONLY
class slLensCandidatesCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slLensCandidatesCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slLensCandidatesCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slLensCandidatesCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slLensCandidatesCatalog', slLensCandidatesCatalog)


# Complex type slVisCoAddedFrame with content type ELEMENT_ONLY
class slVisCoAddedFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slVisCoAddedFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slVisCoAddedFrame_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slVisCoAddedFrame_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slVisCoAddedFrame', slVisCoAddedFrame)


# Complex type slNirCoAddedFrame with content type ELEMENT_ONLY
class slNirCoAddedFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slNirCoAddedFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slNirCoAddedFrame_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slNirCoAddedFrame_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slNirCoAddedFrame', slNirCoAddedFrame)


# Complex type slNirPsfModel with content type ELEMENT_ONLY
class slNirPsfModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'slNirPsfModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaproshe_slNirPsfModel_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaproshe_slNirPsfModel_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'slNirPsfModel', slNirPsfModel)


# Complex type photoZCatalog with content type ELEMENT_ONLY
class photoZCatalog (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photoZCatalog')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sl.photoZCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'photoZCatalog', photoZCatalog)


# Complex type shearCatalog with content type ELEMENT_ONLY
class shearCatalog (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shearCatalog')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sl.shearCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'shearCatalog', shearCatalog)




slPhotoZCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), photoZCatalog, scope=slPhotoZCatalog, documentation=u'The data of the product.'))

slPhotoZCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slPhotoZCatalog, documentation=u'The generic header of the product.'))
slPhotoZCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slPhotoZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slPhotoZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slPhotoZCatalog._ContentModel = pyxb.binding.content.ParticleModel(slPhotoZCatalog._GroupModel, min_occurs=1, max_occurs=1)


merCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(merCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
merCatalog._ContentModel = pyxb.binding.content.ParticleModel(merCatalog._GroupModel, min_occurs=1, max_occurs=1)



slShearCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slShearCatalog, documentation=u'The generic header of the product.'))

slShearCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), shearCatalog, scope=slShearCatalog, documentation=u'The data of the product.'))
slShearCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slShearCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slShearCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slShearCatalog._ContentModel = pyxb.binding.content.ParticleModel(slShearCatalog._GroupModel, min_occurs=1, max_occurs=1)



slExtFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slExtFrame, documentation=u'The data of the product.'))

slExtFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slExtFrame, documentation=u'The generic header of the product.'))
slExtFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slExtFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slExtFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slExtFrame._ContentModel = pyxb.binding.content.ParticleModel(slExtFrame._GroupModel, min_occurs=1, max_occurs=1)



slPreSelectionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slPreSelectionParameters, documentation=u'The generic header of the product.'))

slPreSelectionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slPreSelectionParameters, documentation=u'The data of the product.'))
slPreSelectionParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slPreSelectionParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slPreSelectionParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slPreSelectionParameters._ContentModel = pyxb.binding.content.ParticleModel(slPreSelectionParameters._GroupModel, min_occurs=1, max_occurs=1)



slNirFitsStamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slNirFitsStamp, documentation=u'The generic header of the product.'))

slNirFitsStamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slNirFitsStamp, documentation=u'The data of the product.'))
slNirFitsStamp._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slNirFitsStamp._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slNirFitsStamp._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slNirFitsStamp._ContentModel = pyxb.binding.content.ParticleModel(slNirFitsStamp._GroupModel, min_occurs=1, max_occurs=1)


lensQuasarSubtractedStamp._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(lensQuasarSubtractedStamp._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
lensQuasarSubtractedStamp._ContentModel = pyxb.binding.content.ParticleModel(lensQuasarSubtractedStamp._GroupModel, min_occurs=1, max_occurs=1)


preSelectedCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(preSelectedCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
preSelectedCatalog._ContentModel = pyxb.binding.content.ParticleModel(preSelectedCatalog._GroupModel, min_occurs=1, max_occurs=1)



shearMeasurementData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ShearRMS'), pyxb.binding.datatypes.double, scope=shearMeasurementData))

shearMeasurementData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ShearMean'), pyxb.binding.datatypes.double, scope=shearMeasurementData))
shearMeasurementData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(shearMeasurementData._UseForTag(pyxb.namespace.ExpandedName(None, u'ShearMean')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shearMeasurementData._UseForTag(pyxb.namespace.ExpandedName(None, u'ShearRMS')), min_occurs=1, max_occurs=1)
    )
shearMeasurementData._ContentModel = pyxb.binding.content.ParticleModel(shearMeasurementData._GroupModel, min_occurs=1, max_occurs=1)



visCalibratedImageAndMaskData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'RaDecCommanding'), CommonDM.dm.bas.dtd_stub.listOf2Double, scope=visCalibratedImageAndMaskData))

visCalibratedImageAndMaskData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'VisCalibratedImage'), CommonDM.dm.bas.fit_stub.fitsFile, scope=visCalibratedImageAndMaskData))

visCalibratedImageAndMaskData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ObservationId'), pyxb.binding.datatypes.long, scope=visCalibratedImageAndMaskData))

visCalibratedImageAndMaskData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'VisCalibratedImageMask'), CommonDM.dm.bas.fit_stub.fitsFile, scope=visCalibratedImageAndMaskData))
visCalibratedImageAndMaskData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visCalibratedImageAndMaskData._UseForTag(pyxb.namespace.ExpandedName(None, u'ObservationId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visCalibratedImageAndMaskData._UseForTag(pyxb.namespace.ExpandedName(None, u'RaDecCommanding')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visCalibratedImageAndMaskData._UseForTag(pyxb.namespace.ExpandedName(None, u'VisCalibratedImage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visCalibratedImageAndMaskData._UseForTag(pyxb.namespace.ExpandedName(None, u'VisCalibratedImageMask')), min_occurs=1, max_occurs=1)
    )
visCalibratedImageAndMaskData._ContentModel = pyxb.binding.content.ParticleModel(visCalibratedImageAndMaskData._GroupModel, min_occurs=1, max_occurs=1)



slExtFitsStamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slExtFitsStamp, documentation=u'The generic header of the product.'))

slExtFitsStamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slExtFitsStamp, documentation=u'The data of the product.'))
slExtFitsStamp._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slExtFitsStamp._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slExtFitsStamp._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slExtFitsStamp._ContentModel = pyxb.binding.content.ParticleModel(slExtFitsStamp._GroupModel, min_occurs=1, max_occurs=1)



slSpecZCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slSpecZCatalog, documentation=u'The generic header of the product.'))

slSpecZCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), specZCatalog, scope=slSpecZCatalog, documentation=u'The data of the product.'))
slSpecZCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slSpecZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slSpecZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slSpecZCatalog._ContentModel = pyxb.binding.content.ParticleModel(slSpecZCatalog._GroupModel, min_occurs=1, max_occurs=1)



slInspectionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slInspectionParameters, documentation=u'The generic header of the product.'))

slInspectionParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slInspectionParameters, documentation=u'The data of the product.'))
slInspectionParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slInspectionParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slInspectionParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slInspectionParameters._ContentModel = pyxb.binding.content.ParticleModel(slInspectionParameters._GroupModel, min_occurs=1, max_occurs=1)



slVisFitsStamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slVisFitsStamp, documentation=u'The data of the product.'))

slVisFitsStamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slVisFitsStamp, documentation=u'The generic header of the product.'))
slVisFitsStamp._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slVisFitsStamp._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slVisFitsStamp._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slVisFitsStamp._ContentModel = pyxb.binding.content.ParticleModel(slVisFitsStamp._GroupModel, min_occurs=1, max_occurs=1)



slPreSelectedCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slPreSelectedCatalog, documentation=u'The generic header of the product.'))

slPreSelectedCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), preSelectedCatalog, scope=slPreSelectedCatalog, documentation=u'The data of the product.'))
slPreSelectedCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slPreSelectedCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slPreSelectedCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slPreSelectedCatalog._ContentModel = pyxb.binding.content.ParticleModel(slPreSelectedCatalog._GroupModel, min_occurs=1, max_occurs=1)


lensCandidatesCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(lensCandidatesCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
lensCandidatesCatalog._ContentModel = pyxb.binding.content.ParticleModel(lensCandidatesCatalog._GroupModel, min_occurs=1, max_occurs=1)


specZCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(specZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
specZCatalog._ContentModel = pyxb.binding.content.ParticleModel(specZCatalog._GroupModel, min_occurs=1, max_occurs=1)



sl2DSpectrum._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=sl2DSpectrum, documentation=u'The data of the product.'))

sl2DSpectrum._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=sl2DSpectrum, documentation=u'The generic header of the product.'))
sl2DSpectrum._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sl2DSpectrum._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sl2DSpectrum._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
sl2DSpectrum._ContentModel = pyxb.binding.content.ParticleModel(sl2DSpectrum._GroupModel, min_occurs=1, max_occurs=1)



slVisPsfModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slVisPsfModel, documentation=u'The data of the product.'))

slVisPsfModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slVisPsfModel, documentation=u'The generic header of the product.'))
slVisPsfModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slVisPsfModel._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slVisPsfModel._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slVisPsfModel._ContentModel = pyxb.binding.content.ParticleModel(slVisPsfModel._GroupModel, min_occurs=1, max_occurs=1)



slMerCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), merCatalog, scope=slMerCatalog, documentation=u'The data of the product.'))

slMerCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slMerCatalog, documentation=u'The generic header of the product.'))
slMerCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slMerCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slMerCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slMerCatalog._ContentModel = pyxb.binding.content.ParticleModel(slMerCatalog._GroupModel, min_occurs=1, max_occurs=1)



slLensQuasarSubtractedStamps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slLensQuasarSubtractedStamps, documentation=u'The generic header of the product.'))

slLensQuasarSubtractedStamps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), lensQuasarSubtractedStamp, scope=slLensQuasarSubtractedStamps, documentation=u'The data of the product.'))
slLensQuasarSubtractedStamps._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slLensQuasarSubtractedStamps._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slLensQuasarSubtractedStamps._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slLensQuasarSubtractedStamps._ContentModel = pyxb.binding.content.ParticleModel(slLensQuasarSubtractedStamps._GroupModel, min_occurs=1, max_occurs=1)



slExtPsfModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slExtPsfModel, documentation=u'The data of the product.'))

slExtPsfModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slExtPsfModel, documentation=u'The generic header of the product.'))
slExtPsfModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slExtPsfModel._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slExtPsfModel._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slExtPsfModel._ContentModel = pyxb.binding.content.ParticleModel(slExtPsfModel._GroupModel, min_occurs=1, max_occurs=1)



slPhysicalParametersCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slPhysicalParametersCatalog, documentation=u'The data of the product.'))

slPhysicalParametersCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slPhysicalParametersCatalog, documentation=u'The generic header of the product.'))
slPhysicalParametersCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slPhysicalParametersCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slPhysicalParametersCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slPhysicalParametersCatalog._ContentModel = pyxb.binding.content.ParticleModel(slPhysicalParametersCatalog._GroupModel, min_occurs=1, max_occurs=1)



slLensCandidatesCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), lensQuasarSubtractedStamp, scope=slLensCandidatesCatalog, documentation=u'The data of the product.'))

slLensCandidatesCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slLensCandidatesCatalog, documentation=u'The generic header of the product.'))
slLensCandidatesCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slLensCandidatesCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slLensCandidatesCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slLensCandidatesCatalog._ContentModel = pyxb.binding.content.ParticleModel(slLensCandidatesCatalog._GroupModel, min_occurs=1, max_occurs=1)



slVisCoAddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slVisCoAddedFrame, documentation=u'The data of the product.'))

slVisCoAddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slVisCoAddedFrame, documentation=u'The generic header of the product.'))
slVisCoAddedFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slVisCoAddedFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slVisCoAddedFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slVisCoAddedFrame._ContentModel = pyxb.binding.content.ParticleModel(slVisCoAddedFrame._GroupModel, min_occurs=1, max_occurs=1)



slNirCoAddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slNirCoAddedFrame, documentation=u'The generic header of the product.'))

slNirCoAddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slNirCoAddedFrame, documentation=u'The data of the product.'))
slNirCoAddedFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slNirCoAddedFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slNirCoAddedFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slNirCoAddedFrame._ContentModel = pyxb.binding.content.ParticleModel(slNirCoAddedFrame._GroupModel, min_occurs=1, max_occurs=1)



slNirPsfModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=slNirPsfModel, documentation=u'The data of the product.'))

slNirPsfModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=slNirPsfModel, documentation=u'The generic header of the product.'))
slNirPsfModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(slNirPsfModel._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(slNirPsfModel._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
slNirPsfModel._ContentModel = pyxb.binding.content.ParticleModel(slNirPsfModel._GroupModel, min_occurs=1, max_occurs=1)


photoZCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photoZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
photoZCatalog._ContentModel = pyxb.binding.content.ParticleModel(photoZCatalog._GroupModel, min_occurs=1, max_occurs=1)


shearCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(shearCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
shearCatalog._ContentModel = pyxb.binding.content.ParticleModel(shearCatalog._GroupModel, min_occurs=1, max_occurs=1)
