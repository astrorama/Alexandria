# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/pro/le3_stub.py
# PyXB bindings for NamespaceModule
# NSM:6e92490d80fbb6dc02a66078ea11ba566a411393
# Generated 2014-03-17 18:50:36.642843 by PyXB version 1.1.2
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
import CommonDM.dm.bas.fit_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/le3', create_if_missing=True)
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

    """ Coordinate units of input catalogues."""

    _ExpandedName = None
    _Documentation = u' Coordinate units of input catalogues.'
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.arcsec = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'arcsec')
STD_ANON.arcmin = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'arcmin')
STD_ANON.deg = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'deg')
STD_ANON.rad = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'rad')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic SimpleTypeDefinition
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ Coordinate units of output files."""

    _ExpandedName = None
    _Documentation = u' Coordinate units of output files.'
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.arcsec = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'arcsec')
STD_ANON_.arcmin = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'arcmin')
STD_ANON_.deg = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'deg')
STD_ANON_.rad = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'rad')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic SimpleTypeDefinition
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ "Lin" or "Log" for linear or logarithmic bins. """

    _ExpandedName = None
    _Documentation = u' "Lin" or "Log" for linear or logarithmic bins. '
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.Lin = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'Lin')
STD_ANON_2.Log = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'Log')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic SimpleTypeDefinition
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ Choose "Cartesian" or "Spherical" system of coordinates. """

    _ExpandedName = None
    _Documentation = u' Choose "Cartesian" or "Spherical" system of coordinates. '
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.Cartesian = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Cartesian')
STD_ANON_3.Spherical = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Spherical')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic SimpleTypeDefinition
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ Controls error type, either "None","Bootstrap" or "Jackknife". """

    _ExpandedName = None
    _Documentation = u' Controls error type, either "None","Bootstrap" or "Jackknife". '
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.None_ = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'None')
STD_ANON_4.BootStrap = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'BootStrap')
STD_ANON_4.Jackknife = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'Jackknife')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Complex type catalogLe3FitFile with content type ELEMENT_ONLY
class catalogLe3FitFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogLe3FitFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'le3.catalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'catalogLe3FitFile', catalogLe3FitFile)


# Complex type athenaInputCatalogs with content type ELEMENT_ONLY
class athenaInputCatalogs (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'athenaInputCatalogs')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Catalog2 uses Python identifier Catalog2
    __Catalog2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Catalog2'), 'Catalog2', '__httpeuclid_esa_orgschemaprole3_athenaInputCatalogs_Catalog2', False)

    
    Catalog2 = property(__Catalog2.value, __Catalog2.set, None, None)

    
    # Element Catalog1 uses Python identifier Catalog1
    __Catalog1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Catalog1'), 'Catalog1', '__httpeuclid_esa_orgschemaprole3_athenaInputCatalogs_Catalog1', False)

    
    Catalog1 = property(__Catalog1.value, __Catalog1.set, None, None)


    _ElementMap = {
        __Catalog2.name() : __Catalog2,
        __Catalog1.name() : __Catalog1
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'athenaInputCatalogs', athenaInputCatalogs)


# Complex type athenaOutputShearShear2D with content type ELEMENT_ONLY
class athenaOutputShearShear2D (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'athenaOutputShearShear2D')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'le3.athena.output.shearshear2d', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'athenaOutputShearShear2D', athenaOutputShearShear2D)


# Complex type pallasParams with content type ELEMENT_ONLY
class pallasParams (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pallasParams')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element MinEll uses Python identifier MinEll
    __MinEll = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'MinEll'), 'MinEll', '__httpeuclid_esa_orgschemaprole3_pallasParams_MinEll', False)

    
    MinEll = property(__MinEll.value, __MinEll.set, None, u' Minimal band limit. ')

    
    # Element MaxEll uses Python identifier MaxEll
    __MaxEll = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'MaxEll'), 'MaxEll', '__httpeuclid_esa_orgschemaprole3_pallasParams_MaxEll', False)

    
    MaxEll = property(__MaxEll.value, __MaxEll.set, None, u' Maximal band limit. ')

    
    # Element Nbins uses Python identifier Nbins
    __Nbins = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Nbins'), 'Nbins', '__httpeuclid_esa_orgschemaprole3_pallasParams_Nbins', False)

    
    Nbins = property(__Nbins.value, __Nbins.set, None, u' Number of power spectrum bins. ')


    _ElementMap = {
        __MinEll.name() : __MinEll,
        __MaxEll.name() : __MaxEll,
        __Nbins.name() : __Nbins
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'pallasParams', pallasParams)


# Complex type pallasParamsShearShear2d with content type ELEMENT_ONLY
class pallasParamsShearShear2d (pallasParams):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pallasParamsShearShear2d')
    # Base type is pallasParams
    
    # Element AthenaShearshear2D uses Python identifier AthenaShearshear2D
    __AthenaShearshear2D = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AthenaShearshear2D'), 'AthenaShearshear2D', '__httpeuclid_esa_orgschemaprole3_pallasParamsShearShear2d_AthenaShearshear2D', False)

    
    AthenaShearshear2D = property(__AthenaShearshear2D.value, __AthenaShearshear2D.set, None, None)

    
    # Element MaxEll (MaxEll) inherited from {http://euclid.esa.org/schema/pro/le3}pallasParams
    
    # Element Nbins (Nbins) inherited from {http://euclid.esa.org/schema/pro/le3}pallasParams
    
    # Element MinEll (MinEll) inherited from {http://euclid.esa.org/schema/pro/le3}pallasParams

    _ElementMap = pallasParams._ElementMap.copy()
    _ElementMap.update({
        __AthenaShearshear2D.name() : __AthenaShearshear2D
    })
    _AttributeMap = pallasParams._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'pallasParamsShearShear2d', pallasParamsShearShear2d)


# Complex type athenaParams with content type ELEMENT_ONLY
class athenaParams (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'athenaParams')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element BinType uses Python identifier BinType
    __BinType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'BinType'), 'BinType', '__httpeuclid_esa_orgschemaprole3_athenaParams_BinType', False)

    
    BinType = property(__BinType.value, __BinType.set, None, None)

    
    # Element NRCat1 uses Python identifier NRCat1
    __NRCat1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'NRCat1'), 'NRCat1', '__httpeuclid_esa_orgschemaprole3_athenaParams_NRCat1', False)

    
    NRCat1 = property(__NRCat1.value, __NRCat1.set, None, u' Give number of samples for error calculations for catalog 1. ')

    
    # Element Coordinates uses Python identifier Coordinates
    __Coordinates = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Coordinates'), 'Coordinates', '__httpeuclid_esa_orgschemaprole3_athenaParams_Coordinates', False)

    
    Coordinates = property(__Coordinates.value, __Coordinates.set, None, None)

    
    # Element ThMax uses Python identifier ThMax
    __ThMax = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ThMax'), 'ThMax', '__httpeuclid_esa_orgschemaprole3_athenaParams_ThMax', False)

    
    ThMax = property(__ThMax.value, __ThMax.set, None, u' Maximum angular separation, in units specified by ScoordOutput. ')

    
    # Element NRCat2 uses Python identifier NRCat2
    __NRCat2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'NRCat2'), 'NRCat2', '__httpeuclid_esa_orgschemaprole3_athenaParams_NRCat2', False)

    
    NRCat2 = property(__NRCat2.value, __NRCat2.set, None, u' Give number of samples for error calculations for catalog 2. ')

    
    # Element EstError uses Python identifier EstError
    __EstError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'EstError'), 'EstError', '__httpeuclid_esa_orgschemaprole3_athenaParams_EstError', False)

    
    EstError = property(__EstError.value, __EstError.set, None, None)

    
    # Element CatalogFormat uses Python identifier CatalogFormat
    __CatalogFormat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CatalogFormat'), 'CatalogFormat', '__httpeuclid_esa_orgschemaprole3_athenaParams_CatalogFormat', False)

    
    CatalogFormat = property(__CatalogFormat.value, __CatalogFormat.set, None, u' Fixed to standard catalog (defined by a fits file ).')

    
    # Element Nbins uses Python identifier Nbins
    __Nbins = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Nbins'), 'Nbins', '__httpeuclid_esa_orgschemaprole3_athenaParams_Nbins', False)

    
    Nbins = property(__Nbins.value, __Nbins.set, None, u' Number of angular bins. ')

    
    # Element MergMultiples uses Python identifier MergMultiples
    __MergMultiples = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'MergMultiples'), 'MergMultiples', '__httpeuclid_esa_orgschemaprole3_athenaParams_MergMultiples', False)

    
    MergMultiples = property(__MergMultiples.value, __MergMultiples.set, None, u' Control the merging of multiple objects (i.e. objects at same position).')

    
    # Element WeightScales uses Python identifier WeightScales
    __WeightScales = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'WeightScales'), 'WeightScales', '__httpeuclid_esa_orgschemaprole3_athenaParams_WeightScales', False)

    
    WeightScales = property(__WeightScales.value, __WeightScales.set, None, u' Control the use of weighting for the bin center . ')

    
    # Element InputCatalog uses Python identifier InputCatalog
    __InputCatalog = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'InputCatalog'), 'InputCatalog', '__httpeuclid_esa_orgschemaprole3_athenaParams_InputCatalog', False)

    
    InputCatalog = property(__InputCatalog.value, __InputCatalog.set, None, None)

    
    # Element OpenAngle uses Python identifier OpenAngle
    __OpenAngle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'OpenAngle'), 'OpenAngle', '__httpeuclid_esa_orgschemaprole3_athenaParams_OpenAngle', False)

    
    OpenAngle = property(__OpenAngle.value, __OpenAngle.set, None, u' Give open angle in rad, the smaller the slower but result is more precise". ')

    
    # Element ThMin uses Python identifier ThMin
    __ThMin = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ThMin'), 'ThMin', '__httpeuclid_esa_orgschemaprole3_athenaParams_ThMin', False)

    
    ThMin = property(__ThMin.value, __ThMin.set, None, u' Minimum angular separation, in units specified by ScoordOutput. ')

    
    # Element ScoordInput uses Python identifier ScoordInput
    __ScoordInput = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ScoordInput'), 'ScoordInput', '__httpeuclid_esa_orgschemaprole3_athenaParams_ScoordInput', False)

    
    ScoordInput = property(__ScoordInput.value, __ScoordInput.set, None, None)

    
    # Element ScoordOutput uses Python identifier ScoordOutput
    __ScoordOutput = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ScoordOutput'), 'ScoordOutput', '__httpeuclid_esa_orgschemaprole3_athenaParams_ScoordOutput', False)

    
    ScoordOutput = property(__ScoordOutput.value, __ScoordOutput.set, None, None)


    _ElementMap = {
        __BinType.name() : __BinType,
        __NRCat1.name() : __NRCat1,
        __Coordinates.name() : __Coordinates,
        __ThMax.name() : __ThMax,
        __NRCat2.name() : __NRCat2,
        __EstError.name() : __EstError,
        __CatalogFormat.name() : __CatalogFormat,
        __Nbins.name() : __Nbins,
        __MergMultiples.name() : __MergMultiples,
        __WeightScales.name() : __WeightScales,
        __InputCatalog.name() : __InputCatalog,
        __OpenAngle.name() : __OpenAngle,
        __ThMin.name() : __ThMin,
        __ScoordInput.name() : __ScoordInput,
        __ScoordOutput.name() : __ScoordOutput
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'athenaParams', athenaParams)


# Complex type athenaParamsPosPos2D with content type ELEMENT_ONLY
class athenaParamsPosPos2D (athenaParams):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'athenaParamsPosPos2D')
    # Base type is athenaParams
    
    # Element BinType (BinType) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element InputCatalog (InputCatalog) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element Coordinates (Coordinates) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element ThMax (ThMax) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element CatalogFormat (CatalogFormat) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element EstError (EstError) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element NRCat1 (NRCat1) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element Nbins (Nbins) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element MergMultiples (MergMultiples) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element ThMin (ThMin) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element WeightScales (WeightScales) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element TypeCorr uses Python identifier TypeCorr
    __TypeCorr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'TypeCorr'), 'TypeCorr', '__httpeuclid_esa_orgschemaprole3_athenaParamsPosPos2D_TypeCorr', False)

    
    TypeCorr = property(__TypeCorr.value, __TypeCorr.set, None, None)

    
    # Element NRCat2 (NRCat2) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element OpenAngle (OpenAngle) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element SubTypeCorr uses Python identifier SubTypeCorr
    __SubTypeCorr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SubTypeCorr'), 'SubTypeCorr', '__httpeuclid_esa_orgschemaprole3_athenaParamsPosPos2D_SubTypeCorr', False)

    
    SubTypeCorr = property(__SubTypeCorr.value, __SubTypeCorr.set, None, None)

    
    # Element ScoordInput (ScoordInput) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element ScoordOutput (ScoordOutput) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams

    _ElementMap = athenaParams._ElementMap.copy()
    _ElementMap.update({
        __TypeCorr.name() : __TypeCorr,
        __SubTypeCorr.name() : __SubTypeCorr
    })
    _AttributeMap = athenaParams._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'athenaParamsPosPos2D', athenaParamsPosPos2D)


# Complex type athenaParamsShearShear2D with content type ELEMENT_ONLY
class athenaParamsShearShear2D (athenaParams):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'athenaParamsShearShear2D')
    # Base type is athenaParams
    
    # Element BinType (BinType) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element InputCatalog (InputCatalog) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element Coordinates (Coordinates) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element ThMax (ThMax) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element CatalogFormat (CatalogFormat) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element EstError (EstError) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element NRCat1 (NRCat1) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element Nbins (Nbins) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element MergMultiples (MergMultiples) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element ThMin (ThMin) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element TypeCorr uses Python identifier TypeCorr
    __TypeCorr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'TypeCorr'), 'TypeCorr', '__httpeuclid_esa_orgschemaprole3_athenaParamsShearShear2D_TypeCorr', False)

    
    TypeCorr = property(__TypeCorr.value, __TypeCorr.set, None, None)

    
    # Element WeightScales (WeightScales) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element NRCat2 (NRCat2) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element OpenAngle (OpenAngle) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element SubTypeCorr uses Python identifier SubTypeCorr
    __SubTypeCorr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SubTypeCorr'), 'SubTypeCorr', '__httpeuclid_esa_orgschemaprole3_athenaParamsShearShear2D_SubTypeCorr', False)

    
    SubTypeCorr = property(__SubTypeCorr.value, __SubTypeCorr.set, None, None)

    
    # Element ScoordInput (ScoordInput) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element ScoordOutput (ScoordOutput) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams

    _ElementMap = athenaParams._ElementMap.copy()
    _ElementMap.update({
        __TypeCorr.name() : __TypeCorr,
        __SubTypeCorr.name() : __SubTypeCorr
    })
    _AttributeMap = athenaParams._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'athenaParamsShearShear2D', athenaParamsShearShear2D)


# Complex type pallasOutputShearShearPspec2D with content type ELEMENT_ONLY
class pallasOutputShearShearPspec2D (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pallasOutputShearShearPspec2D')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ShearPspec2D uses Python identifier ShearPspec2D
    __ShearPspec2D = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ShearPspec2D'), 'ShearPspec2D', '__httpeuclid_esa_orgschemaprole3_pallasOutputShearShearPspec2D_ShearPspec2D', False)

    
    ShearPspec2D = property(__ShearPspec2D.value, __ShearPspec2D.set, None, None)


    _ElementMap = {
        __ShearPspec2D.name() : __ShearPspec2D
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'pallasOutputShearShearPspec2D', pallasOutputShearShearPspec2D)


# Complex type shearPspec2DLe3FitFile with content type ELEMENT_ONLY
class shearPspec2DLe3FitFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shearPspec2DLe3FitFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'le3.pallas.output.shearshearpspec2d', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'shearPspec2DLe3FitFile', shearPspec2DLe3FitFile)


# Complex type athenaParamsShearPos2D with content type ELEMENT_ONLY
class athenaParamsShearPos2D (athenaParams):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'athenaParamsShearPos2D')
    # Base type is athenaParams
    
    # Element BinType (BinType) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element InputCatalog (InputCatalog) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element Coordinates (Coordinates) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element ThMax (ThMax) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element CatalogFormat (CatalogFormat) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element EstError (EstError) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element NRCat1 (NRCat1) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element Nbins (Nbins) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element MergMultiples (MergMultiples) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element ThMin (ThMin) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element WeightScales (WeightScales) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element TypeCorr uses Python identifier TypeCorr
    __TypeCorr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'TypeCorr'), 'TypeCorr', '__httpeuclid_esa_orgschemaprole3_athenaParamsShearPos2D_TypeCorr', False)

    
    TypeCorr = property(__TypeCorr.value, __TypeCorr.set, None, None)

    
    # Element NRCat2 (NRCat2) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element OpenAngle (OpenAngle) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element SubTypeCorr uses Python identifier SubTypeCorr
    __SubTypeCorr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SubTypeCorr'), 'SubTypeCorr', '__httpeuclid_esa_orgschemaprole3_athenaParamsShearPos2D_SubTypeCorr', False)

    
    SubTypeCorr = property(__SubTypeCorr.value, __SubTypeCorr.set, None, None)

    
    # Element ScoordInput (ScoordInput) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams
    
    # Element ScoordOutput (ScoordOutput) inherited from {http://euclid.esa.org/schema/pro/le3}athenaParams

    _ElementMap = athenaParams._ElementMap.copy()
    _ElementMap.update({
        __TypeCorr.name() : __TypeCorr,
        __SubTypeCorr.name() : __SubTypeCorr
    })
    _AttributeMap = athenaParams._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'athenaParamsShearPos2D', athenaParamsShearPos2D)



catalogLe3FitFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogLe3FitFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
catalogLe3FitFile._ContentModel = pyxb.binding.content.ParticleModel(catalogLe3FitFile._GroupModel, min_occurs=1, max_occurs=1)



athenaInputCatalogs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Catalog2'), catalogLe3FitFile, scope=athenaInputCatalogs))

athenaInputCatalogs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Catalog1'), catalogLe3FitFile, scope=athenaInputCatalogs))
athenaInputCatalogs._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaInputCatalogs._UseForTag(pyxb.namespace.ExpandedName(None, u'Catalog1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaInputCatalogs._UseForTag(pyxb.namespace.ExpandedName(None, u'Catalog2')), min_occurs=0L, max_occurs=1)
    )
athenaInputCatalogs._ContentModel = pyxb.binding.content.ParticleModel(athenaInputCatalogs._GroupModel, min_occurs=1, max_occurs=1)


athenaOutputShearShear2D._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaOutputShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
athenaOutputShearShear2D._ContentModel = pyxb.binding.content.ParticleModel(athenaOutputShearShear2D._GroupModel, min_occurs=1, max_occurs=1)



pallasParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MinEll'), pyxb.binding.datatypes.long, scope=pallasParams, documentation=u' Minimal band limit. '))

pallasParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MaxEll'), pyxb.binding.datatypes.long, scope=pallasParams, documentation=u' Maximal band limit. '))

pallasParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Nbins'), pyxb.binding.datatypes.long, scope=pallasParams, documentation=u' Number of power spectrum bins. '))
pallasParams._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pallasParams._UseForTag(pyxb.namespace.ExpandedName(None, u'Nbins')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pallasParams._UseForTag(pyxb.namespace.ExpandedName(None, u'MinEll')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pallasParams._UseForTag(pyxb.namespace.ExpandedName(None, u'MaxEll')), min_occurs=1, max_occurs=1)
    )
pallasParams._ContentModel = pyxb.binding.content.ParticleModel(pallasParams._GroupModel, min_occurs=1, max_occurs=1)



pallasParamsShearShear2d._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AthenaShearshear2D'), athenaOutputShearShear2D, scope=pallasParamsShearShear2d))
pallasParamsShearShear2d._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pallasParamsShearShear2d._UseForTag(pyxb.namespace.ExpandedName(None, u'Nbins')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pallasParamsShearShear2d._UseForTag(pyxb.namespace.ExpandedName(None, u'MinEll')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pallasParamsShearShear2d._UseForTag(pyxb.namespace.ExpandedName(None, u'MaxEll')), min_occurs=1, max_occurs=1)
    )
pallasParamsShearShear2d._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pallasParamsShearShear2d._UseForTag(pyxb.namespace.ExpandedName(None, u'AthenaShearshear2D')), min_occurs=1, max_occurs=1)
    )
pallasParamsShearShear2d._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pallasParamsShearShear2d._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pallasParamsShearShear2d._GroupModel_2, min_occurs=1, max_occurs=1)
    )
pallasParamsShearShear2d._ContentModel = pyxb.binding.content.ParticleModel(pallasParamsShearShear2d._GroupModel, min_occurs=1, max_occurs=1)



athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'BinType'), STD_ANON_2, scope=athenaParams))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'NRCat1'), pyxb.binding.datatypes.double, scope=athenaParams, documentation=u' Give number of samples for error calculations for catalog 1. '))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Coordinates'), STD_ANON_3, scope=athenaParams))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ThMax'), pyxb.binding.datatypes.double, scope=athenaParams, documentation=u' Maximum angular separation, in units specified by ScoordOutput. '))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'NRCat2'), pyxb.binding.datatypes.double, scope=athenaParams, documentation=u' Give number of samples for error calculations for catalog 2. '))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'EstError'), STD_ANON_4, scope=athenaParams))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CatalogFormat'), pyxb.binding.datatypes.string, scope=athenaParams, documentation=u' Fixed to standard catalog (defined by a fits file ).'))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Nbins'), pyxb.binding.datatypes.double, scope=athenaParams, documentation=u' Number of angular bins. '))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MergMultiples'), pyxb.binding.datatypes.boolean, scope=athenaParams, documentation=u' Control the merging of multiple objects (i.e. objects at same position).'))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'WeightScales'), pyxb.binding.datatypes.boolean, scope=athenaParams, documentation=u' Control the use of weighting for the bin center . '))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'InputCatalog'), athenaInputCatalogs, scope=athenaParams))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'OpenAngle'), pyxb.binding.datatypes.double, scope=athenaParams, documentation=u' Give open angle in rad, the smaller the slower but result is more precise". '))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ThMin'), pyxb.binding.datatypes.double, scope=athenaParams, documentation=u' Minimum angular separation, in units specified by ScoordOutput. '))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ScoordInput'), STD_ANON, scope=athenaParams))

athenaParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ScoordOutput'), STD_ANON_, scope=athenaParams))
athenaParams._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'CatalogFormat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'InputCatalog')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'MergMultiples')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'ScoordInput')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'ScoordOutput')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'ThMin')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'ThMax')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'Nbins')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'BinType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'Coordinates')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'OpenAngle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'EstError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'NRCat1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'NRCat2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParams._UseForTag(pyxb.namespace.ExpandedName(None, u'WeightScales')), min_occurs=1, max_occurs=1)
    )
athenaParams._ContentModel = pyxb.binding.content.ParticleModel(athenaParams._GroupModel, min_occurs=1, max_occurs=1)



athenaParamsPosPos2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TypeCorr'), pyxb.binding.datatypes.int, scope=athenaParamsPosPos2D))

athenaParamsPosPos2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SubTypeCorr'), pyxb.binding.datatypes.int, scope=athenaParamsPosPos2D))
athenaParamsPosPos2D._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'CatalogFormat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'InputCatalog')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'MergMultiples')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ScoordInput')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ScoordOutput')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ThMin')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ThMax')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'Nbins')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'BinType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'Coordinates')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'OpenAngle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'EstError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'NRCat1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'NRCat2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'WeightScales')), min_occurs=1, max_occurs=1)
    )
athenaParamsPosPos2D._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'TypeCorr')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'SubTypeCorr')), min_occurs=1, max_occurs=1)
    )
athenaParamsPosPos2D._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._GroupModel_2, min_occurs=1, max_occurs=1)
    )
athenaParamsPosPos2D._ContentModel = pyxb.binding.content.ParticleModel(athenaParamsPosPos2D._GroupModel, min_occurs=1, max_occurs=1)



athenaParamsShearShear2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TypeCorr'), pyxb.binding.datatypes.int, scope=athenaParamsShearShear2D))

athenaParamsShearShear2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SubTypeCorr'), pyxb.binding.datatypes.int, scope=athenaParamsShearShear2D))
athenaParamsShearShear2D._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'CatalogFormat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'InputCatalog')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'MergMultiples')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ScoordInput')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ScoordOutput')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ThMin')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ThMax')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'Nbins')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'BinType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'Coordinates')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'OpenAngle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'EstError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'NRCat1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'NRCat2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'WeightScales')), min_occurs=1, max_occurs=1)
    )
athenaParamsShearShear2D._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'TypeCorr')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._UseForTag(pyxb.namespace.ExpandedName(None, u'SubTypeCorr')), min_occurs=1, max_occurs=1)
    )
athenaParamsShearShear2D._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._GroupModel_2, min_occurs=1, max_occurs=1)
    )
athenaParamsShearShear2D._ContentModel = pyxb.binding.content.ParticleModel(athenaParamsShearShear2D._GroupModel, min_occurs=1, max_occurs=1)



pallasOutputShearShearPspec2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ShearPspec2D'), shearPspec2DLe3FitFile, scope=pallasOutputShearShearPspec2D))
pallasOutputShearShearPspec2D._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pallasOutputShearShearPspec2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ShearPspec2D')), min_occurs=1, max_occurs=1)
    )
pallasOutputShearShearPspec2D._ContentModel = pyxb.binding.content.ParticleModel(pallasOutputShearShearPspec2D._GroupModel, min_occurs=1, max_occurs=1)


shearPspec2DLe3FitFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(shearPspec2DLe3FitFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
shearPspec2DLe3FitFile._ContentModel = pyxb.binding.content.ParticleModel(shearPspec2DLe3FitFile._GroupModel, min_occurs=1, max_occurs=1)



athenaParamsShearPos2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TypeCorr'), pyxb.binding.datatypes.int, scope=athenaParamsShearPos2D))

athenaParamsShearPos2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SubTypeCorr'), pyxb.binding.datatypes.int, scope=athenaParamsShearPos2D))
athenaParamsShearPos2D._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'CatalogFormat')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'InputCatalog')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'MergMultiples')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ScoordInput')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ScoordOutput')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ThMin')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'ThMax')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'Nbins')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'BinType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'Coordinates')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'OpenAngle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'EstError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'NRCat1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'NRCat2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'WeightScales')), min_occurs=1, max_occurs=1)
    )
athenaParamsShearPos2D._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'TypeCorr')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._UseForTag(pyxb.namespace.ExpandedName(None, u'SubTypeCorr')), min_occurs=1, max_occurs=1)
    )
athenaParamsShearPos2D._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._GroupModel_2, min_occurs=1, max_occurs=1)
    )
athenaParamsShearPos2D._ContentModel = pyxb.binding.content.ParticleModel(athenaParamsShearPos2D._GroupModel, min_occurs=1, max_occurs=1)
