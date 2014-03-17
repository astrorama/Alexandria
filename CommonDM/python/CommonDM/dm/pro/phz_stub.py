# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/pro/phz_stub.py
# PyXB bindings for NamespaceModule
# NSM:faf5d855b7f1f68d353c36d6320cae7b5b4f4df5
# Generated 2014-03-17 11:53:47.251660 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6923c468-adc2-11e3-8fb8-f01faf601f90')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import CommonDM.dm.bas.fit_stub
import CommonDM.dm.sys_stub
import CommonDM.dm.sys.sgs_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/phz', create_if_missing=True)
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
class configurationIdentifier (pyxb.binding.datatypes.string):

    """The identifier of a PHZ configuration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'configurationIdentifier')
    _Documentation = u'The identifier of a PHZ configuration.'
configurationIdentifier._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'configurationIdentifier', configurationIdentifier)

# Atomic SimpleTypeDefinition
class filterName (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The filter names for which the photometry is provided by OU-MER."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'filterName')
    _Documentation = u'The filter names for which the photometry is provided by OU-MER.'
filterName._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=filterName, enum_prefix=None)
filterName.VIS = filterName._CF_enumeration.addEnumeration(unicode_value=u'VIS')
filterName.NIR_Y = filterName._CF_enumeration.addEnumeration(unicode_value=u'NIR_Y')
filterName.NIR_J = filterName._CF_enumeration.addEnumeration(unicode_value=u'NIR_J')
filterName.NIR_H = filterName._CF_enumeration.addEnumeration(unicode_value=u'NIR_H')
filterName.EXT_g = filterName._CF_enumeration.addEnumeration(unicode_value=u'EXT_g')
filterName.EXT_r = filterName._CF_enumeration.addEnumeration(unicode_value=u'EXT_r')
filterName.EXT_i = filterName._CF_enumeration.addEnumeration(unicode_value=u'EXT_i')
filterName.EXT_z = filterName._CF_enumeration.addEnumeration(unicode_value=u'EXT_z')
filterName._InitializeFacetMap(filterName._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'filterName', filterName)

# Complex type sedFile with content type ELEMENT_ONLY
class sedFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sedFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.sed', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'sedFile', sedFile)


# Complex type reddeningCurveFile with content type ELEMENT_ONLY
class reddeningCurveFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reddeningCurveFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.reddeningCurve', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'reddeningCurveFile', reddeningCurveFile)


# Complex type sed with content type ELEMENT_ONLY
class sed (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sed')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_sed_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The SED data points.')

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemaprophz_sed_Name', False)

    
    Name = property(__Name.value, __Name.set, None, u'The name of the SED.')


    _ElementMap = {
        __Data.name() : __Data,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sed', sed)


# Complex type reddeningCurve with content type ELEMENT_ONLY
class reddeningCurve (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reddeningCurve')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemaprophz_reddeningCurve_Name', False)

    
    Name = property(__Name.value, __Name.set, None, u'The name of the extinction law represented by this reddening curve.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_reddeningCurve_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The reddening curve data.')


    _ElementMap = {
        __Name.name() : __Name,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'reddeningCurve', reddeningCurve)


# Complex type valueRange with content type ELEMENT_ONLY
class valueRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'valueRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Step uses Python identifier Step
    __Step = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Step'), 'Step', '__httpeuclid_esa_orgschemaprophz_valueRange_Step', False)

    
    Step = property(__Step.value, __Step.set, None, u'The step between the values of the list.')

    
    # Element End uses Python identifier End
    __End = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'End'), 'End', '__httpeuclid_esa_orgschemaprophz_valueRange_End', False)

    
    End = property(__End.value, __End.set, None, u'The ending value of the range.')

    
    # Element Start uses Python identifier Start
    __Start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Start'), 'Start', '__httpeuclid_esa_orgschemaprophz_valueRange_Start', False)

    
    Start = property(__Start.value, __Start.set, None, u'The starting value of the range.')


    _ElementMap = {
        __Step.name() : __Step,
        __End.name() : __End,
        __Start.name() : __Start
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'valueRange', valueRange)


# Complex type configuration with content type ELEMENT_ONLY
class configuration (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'configuration')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Redshift uses Python identifier Redshift
    __Redshift = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Redshift'), 'Redshift', '__httpeuclid_esa_orgschemaprophz_configuration_Redshift', False)

    
    Redshift = property(__Redshift.value, __Redshift.set, None, u'The list of the redshift values.')

    
    # Element Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemaprophz_configuration_Identifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'The identifier of the PHZ configuration.')

    
    # Element ReddeningCurve uses Python identifier ReddeningCurve
    __ReddeningCurve = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ReddeningCurve'), 'ReddeningCurve', '__httpeuclid_esa_orgschemaprophz_configuration_ReddeningCurve', True)

    
    ReddeningCurve = property(__ReddeningCurve.value, __ReddeningCurve.set, None, u'The list of the reddening curves.')

    
    # Element Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaprophz_configuration_Filter', True)

    
    Filter = property(__Filter.value, __Filter.set, None, u'The filter transmissions as provided by the instrument team.')

    
    # Element Ebv uses Python identifier Ebv
    __Ebv = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Ebv'), 'Ebv', '__httpeuclid_esa_orgschemaprophz_configuration_Ebv', False)

    
    Ebv = property(__Ebv.value, __Ebv.set, None, u'The list of the E(B-V) values.')

    
    # Element SED uses Python identifier SED
    __SED = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SED'), 'SED', '__httpeuclid_esa_orgschemaprophz_configuration_SED', True)

    
    SED = property(__SED.value, __SED.set, None, u'The list of the SED templates.')


    _ElementMap = {
        __Redshift.name() : __Redshift,
        __Identifier.name() : __Identifier,
        __ReddeningCurve.name() : __ReddeningCurve,
        __Filter.name() : __Filter,
        __Ebv.name() : __Ebv,
        __SED.name() : __SED
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'configuration', configuration)


# Complex type phzPhotoZCatalog with content type ELEMENT_ONLY
class phzPhotoZCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phzPhotoZCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprophz_phzPhotoZCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_phzPhotoZCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'phzPhotoZCatalog', phzPhotoZCatalog)


# Complex type phzPhysicalParametersCatalog with content type ELEMENT_ONLY
class phzPhysicalParametersCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phzPhysicalParametersCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprophz_phzPhysicalParametersCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_phzPhysicalParametersCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'phzPhysicalParametersCatalog', phzPhysicalParametersCatalog)


# Complex type calibrationModel with content type ELEMENT_ONLY
class calibrationModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'calibrationModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Model'), 'Model', '__httpeuclid_esa_orgschemaprophz_calibrationModel_Model', False)

    
    Model = property(__Model.value, __Model.set, None, u'A file containing the calibration model. This model is both produced and consumed by OU-PHZ, so its format is internal in the OU-PHZ. For this reason it is defined as just a file.')

    
    # Element Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemaprophz_calibrationModel_Identifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'The identifier of the configuration used.')


    _ElementMap = {
        __Model.name() : __Model,
        __Identifier.name() : __Identifier
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'calibrationModel', calibrationModel)


# Complex type filter with content type ELEMENT_ONLY
class filter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'filter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_filter_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The transmission of the filter.')

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemaprophz_filter_Name', False)

    
    Name = property(__Name.value, __Name.set, None, u'The name of the filter.')


    _ElementMap = {
        __Data.name() : __Data,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'filter', filter)


# Complex type phzPDFCatalog with content type ELEMENT_ONLY
class phzPDFCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phzPDFCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_phzPDFCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprophz_phzPDFCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'phzPDFCatalog', phzPDFCatalog)


# Complex type phzPhotometryCatalog with content type ELEMENT_ONLY
class phzPhotometryCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phzPhotometryCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_phzPhotometryCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprophz_phzPhotometryCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'phzPhotometryCatalog', phzPhotometryCatalog)


# Complex type phzCalibrationData with content type ELEMENT_ONLY
class phzCalibrationData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phzCalibrationData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_phzCalibrationData_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprophz_phzCalibrationData_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'phzCalibrationData', phzCalibrationData)


# Complex type pdfCatalog with content type ELEMENT_ONLY
class pdfCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pdfCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PDF uses Python identifier PDF
    __PDF = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'PDF'), 'PDF', '__httpeuclid_esa_orgschemaprophz_pdfCatalog_PDF', True)

    
    PDF = property(__PDF.value, __PDF.set, None, u'An entry of a photometric redshift PDF catalog.')


    _ElementMap = {
        __PDF.name() : __PDF
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'pdfCatalog', pdfCatalog)


# Complex type phzMorphologyCatalog with content type ELEMENT_ONLY
class phzMorphologyCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phzMorphologyCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprophz_phzMorphologyCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_phzMorphologyCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'phzMorphologyCatalog', phzMorphologyCatalog)


# Complex type phzConfigurationSet with content type ELEMENT_ONLY
class phzConfigurationSet (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phzConfigurationSet')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprophz_phzConfigurationSet_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_phzConfigurationSet_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'phzConfigurationSet', phzConfigurationSet)


# Complex type configurationSet with content type ELEMENT_ONLY
class configurationSet (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'configurationSet')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Configuration uses Python identifier Configuration
    __Configuration = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Configuration'), 'Configuration', '__httpeuclid_esa_orgschemaprophz_configurationSet_Configuration', True)

    
    Configuration = property(__Configuration.value, __Configuration.set, None, u'The list of the different PHZ configurations.')


    _ElementMap = {
        __Configuration.name() : __Configuration
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'configurationSet', configurationSet)


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
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.specZCatalog', required=True)
    
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


# Complex type pdfFile with content type ELEMENT_ONLY
class pdfFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pdfFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.pdf', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'pdfFile', pdfFile)


# Complex type pdf with content type ELEMENT_ONLY
class pdf (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pdf')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SourceID uses Python identifier SourceID
    __SourceID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SourceID'), 'SourceID', '__httpeuclid_esa_orgschemaprophz_pdf_SourceID', False)

    
    SourceID = property(__SourceID.value, __SourceID.set, None, u'The source identifier.')

    
    # Element PDFFile uses Python identifier PDFFile
    __PDFFile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'PDFFile'), 'PDFFile', '__httpeuclid_esa_orgschemaprophz_pdf_PDFFile', False)

    
    PDFFile = property(__PDFFile.value, __PDFFile.set, None, u'The file containing the PDF.')

    
    # Element ConfigurationIdentifier uses Python identifier ConfigurationIdentifier
    __ConfigurationIdentifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ConfigurationIdentifier'), 'ConfigurationIdentifier', '__httpeuclid_esa_orgschemaprophz_pdf_ConfigurationIdentifier', False)

    
    ConfigurationIdentifier = property(__ConfigurationIdentifier.value, __ConfigurationIdentifier.set, None, u'The identifier of the configuration used for producing the PDF.')


    _ElementMap = {
        __SourceID.name() : __SourceID,
        __PDFFile.name() : __PDFFile,
        __ConfigurationIdentifier.name() : __ConfigurationIdentifier
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'pdf', pdf)


# Complex type photometryCatalog with content type ELEMENT_ONLY
class photometryCatalog (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'photometryCatalog')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.photometryCatalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'photometryCatalog', photometryCatalog)


# Complex type calibrationData with content type ELEMENT_ONLY
class calibrationData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'calibrationData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CalibrationModel uses Python identifier CalibrationModel
    __CalibrationModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CalibrationModel'), 'CalibrationModel', '__httpeuclid_esa_orgschemaprophz_calibrationData_CalibrationModel', True)

    
    CalibrationModel = property(__CalibrationModel.value, __CalibrationModel.set, None, u'The list of the calibration models for all the different configurations.')

    
    # Element OptimizationParameters uses Python identifier OptimizationParameters
    __OptimizationParameters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'OptimizationParameters'), 'OptimizationParameters', '__httpeuclid_esa_orgschemaprophz_calibrationData_OptimizationParameters', False)

    
    OptimizationParameters = property(__OptimizationParameters.value, __OptimizationParameters.set, None, u'Optimization parameters (correction matrices, etc) as calculated by the PHZ calibration pipeline segment, based on the available spectroscopic redshifts. These parameters are both produced and consumed by OU-PHZ, so their format is internal in the OU-PHZ. For this reason they are defined as just a file.')


    _ElementMap = {
        __CalibrationModel.name() : __CalibrationModel,
        __OptimizationParameters.name() : __OptimizationParameters
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'calibrationData', calibrationData)


# Complex type filterFile with content type ELEMENT_ONLY
class filterFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'filterFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.filter', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'filterFile', filterFile)


# Complex type phzRadioCatalog with content type ELEMENT_ONLY
class phzRadioCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phzRadioCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_phzRadioCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprophz_phzRadioCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'phzRadioCatalog', phzRadioCatalog)


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
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'phz.photoZCatalog', required=True)
    
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


# Complex type phzSpecZCatalog with content type ELEMENT_ONLY
class phzSpecZCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phzSpecZCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprophz_phzSpecZCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_phzSpecZCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'phzSpecZCatalog', phzSpecZCatalog)


# Complex type phzXRayCatalog with content type ELEMENT_ONLY
class phzXRayCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phzXRayCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprophz_phzXRayCatalog_Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprophz_phzXRayCatalog_Header', False)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'phzXRayCatalog', phzXRayCatalog)



sedFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sedFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
sedFile._ContentModel = pyxb.binding.content.ParticleModel(sedFile._GroupModel, min_occurs=1, max_occurs=1)


reddeningCurveFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reddeningCurveFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
reddeningCurveFile._ContentModel = pyxb.binding.content.ParticleModel(reddeningCurveFile._GroupModel, min_occurs=1, max_occurs=1)



sed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), sedFile, scope=sed, documentation=u'The SED data points.'))

sed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=sed, documentation=u'The name of the SED.'))
sed._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sed._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sed._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
sed._ContentModel = pyxb.binding.content.ParticleModel(sed._GroupModel, min_occurs=1, max_occurs=1)



reddeningCurve._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=reddeningCurve, documentation=u'The name of the extinction law represented by this reddening curve.'))

reddeningCurve._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), reddeningCurveFile, scope=reddeningCurve, documentation=u'The reddening curve data.'))
reddeningCurve._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(reddeningCurve._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(reddeningCurve._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
reddeningCurve._ContentModel = pyxb.binding.content.ParticleModel(reddeningCurve._GroupModel, min_occurs=1, max_occurs=1)



valueRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Step'), pyxb.binding.datatypes.double, scope=valueRange, documentation=u'The step between the values of the list.'))

valueRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'End'), pyxb.binding.datatypes.double, scope=valueRange, documentation=u'The ending value of the range.'))

valueRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Start'), pyxb.binding.datatypes.double, scope=valueRange, documentation=u'The starting value of the range.'))
valueRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(valueRange._UseForTag(pyxb.namespace.ExpandedName(None, u'Start')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(valueRange._UseForTag(pyxb.namespace.ExpandedName(None, u'End')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(valueRange._UseForTag(pyxb.namespace.ExpandedName(None, u'Step')), min_occurs=1, max_occurs=1)
    )
valueRange._ContentModel = pyxb.binding.content.ParticleModel(valueRange._GroupModel, min_occurs=1, max_occurs=1)



configuration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Redshift'), valueRange, scope=configuration, documentation=u'The list of the redshift values.'))

configuration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Identifier'), configurationIdentifier, scope=configuration, documentation=u'The identifier of the PHZ configuration.'))

configuration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReddeningCurve'), reddeningCurve, scope=configuration, documentation=u'The list of the reddening curves.'))

configuration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Filter'), filter, scope=configuration, documentation=u'The filter transmissions as provided by the instrument team.'))

configuration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Ebv'), valueRange, scope=configuration, documentation=u'The list of the E(B-V) values.'))

configuration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SED'), sed, scope=configuration, documentation=u'The list of the SED templates.'))
configuration._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(configuration._UseForTag(pyxb.namespace.ExpandedName(None, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(configuration._UseForTag(pyxb.namespace.ExpandedName(None, u'Filter')), min_occurs=8L, max_occurs=8L),
    pyxb.binding.content.ParticleModel(configuration._UseForTag(pyxb.namespace.ExpandedName(None, u'SED')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(configuration._UseForTag(pyxb.namespace.ExpandedName(None, u'ReddeningCurve')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(configuration._UseForTag(pyxb.namespace.ExpandedName(None, u'Ebv')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(configuration._UseForTag(pyxb.namespace.ExpandedName(None, u'Redshift')), min_occurs=1, max_occurs=1)
    )
configuration._ContentModel = pyxb.binding.content.ParticleModel(configuration._GroupModel, min_occurs=1, max_occurs=1)



phzPhotoZCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=phzPhotoZCatalog, documentation=u'The generic header of the product.'))

phzPhotoZCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), photoZCatalog, scope=phzPhotoZCatalog, documentation=u'The data of the product.'))
phzPhotoZCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(phzPhotoZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(phzPhotoZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
phzPhotoZCatalog._ContentModel = pyxb.binding.content.ParticleModel(phzPhotoZCatalog._GroupModel, min_occurs=1, max_occurs=1)



phzPhysicalParametersCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=phzPhysicalParametersCatalog, documentation=u'The generic header of the product.'))

phzPhysicalParametersCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=phzPhysicalParametersCatalog, documentation=u'The data of the product.'))
phzPhysicalParametersCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(phzPhysicalParametersCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(phzPhysicalParametersCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
phzPhysicalParametersCatalog._ContentModel = pyxb.binding.content.ParticleModel(phzPhysicalParametersCatalog._GroupModel, min_occurs=1, max_occurs=1)



calibrationModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Model'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=calibrationModel, documentation=u'A file containing the calibration model. This model is both produced and consumed by OU-PHZ, so its format is internal in the OU-PHZ. For this reason it is defined as just a file.'))

calibrationModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Identifier'), configurationIdentifier, scope=calibrationModel, documentation=u'The identifier of the configuration used.'))
calibrationModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calibrationModel._UseForTag(pyxb.namespace.ExpandedName(None, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibrationModel._UseForTag(pyxb.namespace.ExpandedName(None, u'Model')), min_occurs=1, max_occurs=1)
    )
calibrationModel._ContentModel = pyxb.binding.content.ParticleModel(calibrationModel._GroupModel, min_occurs=1, max_occurs=1)



filter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), filterFile, scope=filter, documentation=u'The transmission of the filter.'))

filter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), filterName, scope=filter, documentation=u'The name of the filter.'))
filter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(filter._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filter._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
filter._ContentModel = pyxb.binding.content.ParticleModel(filter._GroupModel, min_occurs=1, max_occurs=1)



phzPDFCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), pdfCatalog, scope=phzPDFCatalog, documentation=u'The data of the product.'))

phzPDFCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=phzPDFCatalog, documentation=u'The generic header of the product.'))
phzPDFCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(phzPDFCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(phzPDFCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
phzPDFCatalog._ContentModel = pyxb.binding.content.ParticleModel(phzPDFCatalog._GroupModel, min_occurs=1, max_occurs=1)



phzPhotometryCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), photometryCatalog, scope=phzPhotometryCatalog, documentation=u'The data of the product.'))

phzPhotometryCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=phzPhotometryCatalog, documentation=u'The generic header of the product.'))
phzPhotometryCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(phzPhotometryCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(phzPhotometryCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
phzPhotometryCatalog._ContentModel = pyxb.binding.content.ParticleModel(phzPhotometryCatalog._GroupModel, min_occurs=1, max_occurs=1)



phzCalibrationData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), calibrationData, scope=phzCalibrationData, documentation=u'The data of the product.'))

phzCalibrationData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=phzCalibrationData, documentation=u'The generic header of the product.'))
phzCalibrationData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(phzCalibrationData._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(phzCalibrationData._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
phzCalibrationData._ContentModel = pyxb.binding.content.ParticleModel(phzCalibrationData._GroupModel, min_occurs=1, max_occurs=1)



pdfCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PDF'), pdf, scope=pdfCatalog, documentation=u'An entry of a photometric redshift PDF catalog.'))
pdfCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pdfCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'PDF')), min_occurs=0L, max_occurs=None)
    )
pdfCatalog._ContentModel = pyxb.binding.content.ParticleModel(pdfCatalog._GroupModel, min_occurs=1, max_occurs=1)



phzMorphologyCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=phzMorphologyCatalog, documentation=u'The generic header of the product.'))

phzMorphologyCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=phzMorphologyCatalog, documentation=u'The data of the product.'))
phzMorphologyCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(phzMorphologyCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(phzMorphologyCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
phzMorphologyCatalog._ContentModel = pyxb.binding.content.ParticleModel(phzMorphologyCatalog._GroupModel, min_occurs=1, max_occurs=1)



phzConfigurationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=phzConfigurationSet, documentation=u'The generic header of the product.'))

phzConfigurationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), configurationSet, scope=phzConfigurationSet, documentation=u'The data of the product.'))
phzConfigurationSet._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(phzConfigurationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(phzConfigurationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
phzConfigurationSet._ContentModel = pyxb.binding.content.ParticleModel(phzConfigurationSet._GroupModel, min_occurs=1, max_occurs=1)



configurationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Configuration'), configuration, scope=configurationSet, documentation=u'The list of the different PHZ configurations.'))
configurationSet._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(configurationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'Configuration')), min_occurs=1, max_occurs=None)
    )
configurationSet._ContentModel = pyxb.binding.content.ParticleModel(configurationSet._GroupModel, min_occurs=1, max_occurs=1)


specZCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(specZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
specZCatalog._ContentModel = pyxb.binding.content.ParticleModel(specZCatalog._GroupModel, min_occurs=1, max_occurs=1)


pdfFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pdfFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
pdfFile._ContentModel = pyxb.binding.content.ParticleModel(pdfFile._GroupModel, min_occurs=1, max_occurs=1)



pdf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SourceID'), pyxb.binding.datatypes.long, scope=pdf, documentation=u'The source identifier.'))

pdf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PDFFile'), pdfFile, scope=pdf, documentation=u'The file containing the PDF.'))

pdf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ConfigurationIdentifier'), configurationIdentifier, scope=pdf, documentation=u'The identifier of the configuration used for producing the PDF.'))
pdf._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pdf._UseForTag(pyxb.namespace.ExpandedName(None, u'SourceID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pdf._UseForTag(pyxb.namespace.ExpandedName(None, u'ConfigurationIdentifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pdf._UseForTag(pyxb.namespace.ExpandedName(None, u'PDFFile')), min_occurs=1, max_occurs=1)
    )
pdf._ContentModel = pyxb.binding.content.ParticleModel(pdf._GroupModel, min_occurs=1, max_occurs=1)


photometryCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photometryCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
photometryCatalog._ContentModel = pyxb.binding.content.ParticleModel(photometryCatalog._GroupModel, min_occurs=1, max_occurs=1)



calibrationData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CalibrationModel'), calibrationModel, scope=calibrationData, documentation=u'The list of the calibration models for all the different configurations.'))

calibrationData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'OptimizationParameters'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=calibrationData, documentation=u'Optimization parameters (correction matrices, etc) as calculated by the PHZ calibration pipeline segment, based on the available spectroscopic redshifts. These parameters are both produced and consumed by OU-PHZ, so their format is internal in the OU-PHZ. For this reason they are defined as just a file.'))
calibrationData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calibrationData._UseForTag(pyxb.namespace.ExpandedName(None, u'OptimizationParameters')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibrationData._UseForTag(pyxb.namespace.ExpandedName(None, u'CalibrationModel')), min_occurs=1, max_occurs=None)
    )
calibrationData._ContentModel = pyxb.binding.content.ParticleModel(calibrationData._GroupModel, min_occurs=1, max_occurs=1)


filterFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(filterFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
filterFile._ContentModel = pyxb.binding.content.ParticleModel(filterFile._GroupModel, min_occurs=1, max_occurs=1)



phzRadioCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=phzRadioCatalog, documentation=u'The data of the product.'))

phzRadioCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=phzRadioCatalog, documentation=u'The generic header of the product.'))
phzRadioCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(phzRadioCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(phzRadioCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
phzRadioCatalog._ContentModel = pyxb.binding.content.ParticleModel(phzRadioCatalog._GroupModel, min_occurs=1, max_occurs=1)


photoZCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(photoZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
photoZCatalog._ContentModel = pyxb.binding.content.ParticleModel(photoZCatalog._GroupModel, min_occurs=1, max_occurs=1)



phzSpecZCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=phzSpecZCatalog, documentation=u'The generic header of the product.'))

phzSpecZCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), specZCatalog, scope=phzSpecZCatalog, documentation=u'The data of the product.'))
phzSpecZCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(phzSpecZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(phzSpecZCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
phzSpecZCatalog._ContentModel = pyxb.binding.content.ParticleModel(phzSpecZCatalog._GroupModel, min_occurs=1, max_occurs=1)



phzXRayCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=phzXRayCatalog, documentation=u'The data of the product.'))

phzXRayCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=phzXRayCatalog, documentation=u'The generic header of the product.'))
phzXRayCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(phzXRayCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(phzXRayCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
phzXRayCatalog._ContentModel = pyxb.binding.content.ParticleModel(phzXRayCatalog._GroupModel, min_occurs=1, max_occurs=1)
