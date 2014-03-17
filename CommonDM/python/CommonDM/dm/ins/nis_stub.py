# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/ins/nis_stub.py
# PyXB bindings for NamespaceModule
# NSM:6e6d3cdee0146c7b53063e709e7bcb83a74176c6
# Generated 2014-03-17 11:53:47.250325 by PyXB version 1.1.2
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
import CommonDM.dm.bas.spm_stub
import CommonDM.dm.bas.utd_stub
import CommonDM.dm.bas.dtd_stub
import CommonDM.dm.sys_stub
import CommonDM.dm.sys.sgs_stub
import CommonDM.dm.bas.mat_stub
import CommonDM.dm.ins_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/ins/nis', create_if_missing=True)
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
class grismOrderName (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Defines the available grism order names, A, B, C and D."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'grismOrderName')
    _Documentation = u'Defines the available grism order names, A, B, C and D.'
grismOrderName._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=grismOrderName, enum_prefix=None)
grismOrderName.A = grismOrderName._CF_enumeration.addEnumeration(unicode_value=u'A')
grismOrderName.B = grismOrderName._CF_enumeration.addEnumeration(unicode_value=u'B')
grismOrderName.C = grismOrderName._CF_enumeration.addEnumeration(unicode_value=u'C')
grismOrderName.D = grismOrderName._CF_enumeration.addEnumeration(unicode_value=u'D')
grismOrderName._InitializeFacetMap(grismOrderName._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'grismOrderName', grismOrderName)

# Atomic SimpleTypeDefinition
class filterName (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of the filter selected."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'filterName')
    _Documentation = u'List of the filter selected.'
filterName._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=filterName, enum_prefix=None)
filterName.Y = filterName._CF_enumeration.addEnumeration(unicode_value=u'Y')
filterName.J = filterName._CF_enumeration.addEnumeration(unicode_value=u'J')
filterName.H = filterName._CF_enumeration.addEnumeration(unicode_value=u'H')
filterName._InitializeFacetMap(filterName._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'filterName', filterName)

# Atomic SimpleTypeDefinition
class grismName (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of the Grism selected."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'grismName')
    _Documentation = u'List of the Grism selected.'
grismName._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=grismName, enum_prefix=None)
grismName.GBLUE0 = grismName._CF_enumeration.addEnumeration(unicode_value=u'GBLUE0')
grismName.GBLUE90 = grismName._CF_enumeration.addEnumeration(unicode_value=u'GBLUE90')
grismName.GRED0 = grismName._CF_enumeration.addEnumeration(unicode_value=u'GRED0')
grismName.GRED90 = grismName._CF_enumeration.addEnumeration(unicode_value=u'GRED90')
grismName._InitializeFacetMap(grismName._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'grismName', grismName)

# Union SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class nispMode (pyxb.binding.basis.STD_union):

    """The different available modes for the NISP instrument."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nispMode')
    _Documentation = u'The different available modes for the NISP instrument.'

    _MemberTypes = ( grismName, filterName, )
nispMode._CF_pattern = pyxb.binding.facets.CF_pattern()
nispMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nispMode)
nispMode.GBLUE0 = u'GBLUE0'                       # originally grismName.GBLUE0
nispMode.GBLUE90 = u'GBLUE90'                     # originally grismName.GBLUE90
nispMode.GRED0 = u'GRED0'                         # originally grismName.GRED0
nispMode.GRED90 = u'GRED90'                       # originally grismName.GRED90
nispMode.Y = u'Y'                                 # originally filterName.Y
nispMode.J = u'J'                                 # originally filterName.J
nispMode.H = u'H'                                 # originally filterName.H
nispMode._InitializeFacetMap(nispMode._CF_pattern,
   nispMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'nispMode', nispMode)

# Atomic SimpleTypeDefinition
class FPAName (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FPAName')
    _Documentation = None
FPAName._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FPAName, enum_prefix=None)
FPAName.VIS_FPA = FPAName._CF_enumeration.addEnumeration(unicode_value=u'VIS_FPA')
FPAName.NISP_FPA = FPAName._CF_enumeration.addEnumeration(unicode_value=u'NISP_FPA')
FPAName._InitializeFacetMap(FPAName._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'FPAName', FPAName)

# Complex type cosmicRayMap with content type ELEMENT_ONLY
class cosmicRayMap (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cosmicRayMap')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'nis.cosmicRayMap', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'cosmicRayMap', cosmicRayMap)


# Complex type nipOpticsModel with content type ELEMENT_ONLY
class nipOpticsModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nipOpticsModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}FilterMode uses Python identifier FilterMode
    __FilterMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FilterMode'), 'FilterMode', '__httpeuclid_esa_orgschemainsnis_nipOpticsModel_httpeuclid_esa_orgschemainsnisFilterMode', True)

    
    FilterMode = property(__FilterMode.value, __FilterMode.set, None, None)


    _ElementMap = {
        __FilterMode.name() : __FilterMode
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nipOpticsModel', nipOpticsModel)


# Complex type darkCurrentMap with content type ELEMENT_ONLY
class darkCurrentMap (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'darkCurrentMap')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'nis.detectorDarkCurrentMap', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'darkCurrentMap', darkCurrentMap)


# Complex type spectrumRange with content type ELEMENT_ONLY
class spectrumRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrumRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}MinWavelengthValue uses Python identifier MinWavelengthValue
    __MinWavelengthValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinWavelengthValue'), 'MinWavelengthValue', '__httpeuclid_esa_orgschemainsnis_spectrumRange_httpeuclid_esa_orgschemainsnisMinWavelengthValue', False)

    
    MinWavelengthValue = property(__MinWavelengthValue.value, __MinWavelengthValue.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/ins/nis}MaxWavelengthValue uses Python identifier MaxWavelengthValue
    __MaxWavelengthValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxWavelengthValue'), 'MaxWavelengthValue', '__httpeuclid_esa_orgschemainsnis_spectrumRange_httpeuclid_esa_orgschemainsnisMaxWavelengthValue', False)

    
    MaxWavelengthValue = property(__MaxWavelengthValue.value, __MaxWavelengthValue.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/ins/nis}RangeID uses Python identifier RangeID
    __RangeID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RangeID'), 'RangeID', '__httpeuclid_esa_orgschemainsnis_spectrumRange_httpeuclid_esa_orgschemainsnisRangeID', False)

    
    RangeID = property(__RangeID.value, __RangeID.set, None, u'Name or ID commonly used for this spectral band')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemainsnis_spectrumRange_httpeuclid_esa_orgschemainsnisUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Resolution uses Python identifier Resolution
    __Resolution = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Resolution'), 'Resolution', '__httpeuclid_esa_orgschemainsnis_spectrumRange_httpeuclid_esa_orgschemainsnisResolution', False)

    
    Resolution = property(__Resolution.value, __Resolution.set, None, u'The number of samples is equal to : max - min divided by resolution + 2 ')


    _ElementMap = {
        __MinWavelengthValue.name() : __MinWavelengthValue,
        __MaxWavelengthValue.name() : __MaxWavelengthValue,
        __RangeID.name() : __RangeID,
        __Unit.name() : __Unit,
        __Resolution.name() : __Resolution
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spectrumRange', spectrumRange)


# Complex type grismModeModel with content type ELEMENT_ONLY
class grismModeModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'grismModeModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}GrismOrderList uses Python identifier GrismOrderList
    __GrismOrderList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GrismOrderList'), 'GrismOrderList', '__httpeuclid_esa_orgschemainsnis_grismModeModel_httpeuclid_esa_orgschemainsnisGrismOrderList', False)

    
    GrismOrderList = property(__GrismOrderList.value, __GrismOrderList.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}GrismName uses Python identifier GrismName
    __GrismName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GrismName'), 'GrismName', '__httpeuclid_esa_orgschemainsnis_grismModeModel_httpeuclid_esa_orgschemainsnisGrismName', False)

    
    GrismName = property(__GrismName.value, __GrismName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemainsnis_grismModeModel_httpeuclid_esa_orgschemainsnisIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)


    _ElementMap = {
        __GrismOrderList.name() : __GrismOrderList,
        __GrismName.name() : __GrismName,
        __Identifier.name() : __Identifier
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'grismModeModel', grismModeModel)


# Complex type grismOrderModel with content type ELEMENT_ONLY
class grismOrderModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'grismOrderModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}OrderName uses Python identifier OrderName
    __OrderName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OrderName'), 'OrderName', '__httpeuclid_esa_orgschemainsnis_grismOrderModel_httpeuclid_esa_orgschemainsnisOrderName', False)

    
    OrderName = property(__OrderName.value, __OrderName.set, None, u'Order name (A, B, etc)')

    
    # Element {http://euclid.esa.org/schema/ins/nis}PSF uses Python identifier PSF
    __PSF = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PSF'), 'PSF', '__httpeuclid_esa_orgschemainsnis_grismOrderModel_httpeuclid_esa_orgschemainsnisPSF', False)

    
    PSF = property(__PSF.value, __PSF.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Curvature uses Python identifier Curvature
    __Curvature = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Curvature'), 'Curvature', '__httpeuclid_esa_orgschemainsnis_grismOrderModel_httpeuclid_esa_orgschemainsnisCurvature', False)

    
    Curvature = property(__Curvature.value, __Curvature.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Transmission uses Python identifier Transmission
    __Transmission = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Transmission'), 'Transmission', '__httpeuclid_esa_orgschemainsnis_grismOrderModel_httpeuclid_esa_orgschemainsnisTransmission', False)

    
    Transmission = property(__Transmission.value, __Transmission.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Dispersion uses Python identifier Dispersion
    __Dispersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Dispersion'), 'Dispersion', '__httpeuclid_esa_orgschemainsnis_grismOrderModel_httpeuclid_esa_orgschemainsnisDispersion', False)

    
    Dispersion = property(__Dispersion.value, __Dispersion.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemainsnis_grismOrderModel_httpeuclid_esa_orgschemainsnisIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Distortion uses Python identifier Distortion
    __Distortion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Distortion'), 'Distortion', '__httpeuclid_esa_orgschemainsnis_grismOrderModel_httpeuclid_esa_orgschemainsnisDistortion', False)

    
    Distortion = property(__Distortion.value, __Distortion.set, None, None)


    _ElementMap = {
        __OrderName.name() : __OrderName,
        __PSF.name() : __PSF,
        __Curvature.name() : __Curvature,
        __Transmission.name() : __Transmission,
        __Dispersion.name() : __Dispersion,
        __Identifier.name() : __Identifier,
        __Distortion.name() : __Distortion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'grismOrderModel', grismOrderModel)


# Complex type curvatureModel with content type ELEMENT_ONLY
class curvatureModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'curvatureModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemainsnis_curvatureModel_httpeuclid_esa_orgschemainsnisUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, u'The unit used to describe the Start, End and polynomial coefficients of the trace. Default: um')

    
    # Element {http://euclid.esa.org/schema/ins/nis}DispAngle uses Python identifier DispAngle
    __DispAngle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DispAngle'), 'DispAngle', '__httpeuclid_esa_orgschemainsnis_curvatureModel_httpeuclid_esa_orgschemainsnisDispAngle', False)

    
    DispAngle = property(__DispAngle.value, __DispAngle.set, None, u'The dispersion direction (0 or 90). Counter-clockwise in the FPA frame.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}PolyOrder uses Python identifier PolyOrder
    __PolyOrder = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PolyOrder'), 'PolyOrder', '__httpeuclid_esa_orgschemainsnis_curvatureModel_httpeuclid_esa_orgschemainsnisPolyOrder', False)

    
    PolyOrder = property(__PolyOrder.value, __PolyOrder.set, None, u'The order of the polynomial DY = a0 + a1 DX + a2 DX^2 + ...')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemainsnis_curvatureModel_httpeuclid_esa_orgschemainsnisVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}End uses Python identifier End
    __End = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'End'), 'End', '__httpeuclid_esa_orgschemainsnis_curvatureModel_httpeuclid_esa_orgschemainsnisEnd', False)

    
    End = property(__End.value, __End.set, None, u'The position of the end of the spectrum in the dispersion direction, blueward of the reference wavelength.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Start uses Python identifier Start
    __Start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Start'), 'Start', '__httpeuclid_esa_orgschemainsnis_curvatureModel_httpeuclid_esa_orgschemainsnisStart', False)

    
    Start = property(__Start.value, __Start.set, None, u'The position of the beginning of the spectrum in the dispersion direction, redward of the reference wavelength.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}ComputationDate uses Python identifier ComputationDate
    __ComputationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), 'ComputationDate', '__httpeuclid_esa_orgschemainsnis_curvatureModel_httpeuclid_esa_orgschemainsnisComputationDate', False)

    
    ComputationDate = property(__ComputationDate.value, __ComputationDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}CalibrationDataPath uses Python identifier CalibrationDataPath
    __CalibrationDataPath = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath'), 'CalibrationDataPath', '__httpeuclid_esa_orgschemainsnis_curvatureModel_httpeuclid_esa_orgschemainsnisCalibrationDataPath', False)

    
    CalibrationDataPath = property(__CalibrationDataPath.value, __CalibrationDataPath.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Coefficients uses Python identifier Coefficients
    __Coefficients = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), 'Coefficients', '__httpeuclid_esa_orgschemainsnis_curvatureModel_httpeuclid_esa_orgschemainsnisCoefficients', True)

    
    Coefficients = property(__Coefficients.value, __Coefficients.set, None, u'The coefficients of the polynomial DY = a0 + a1 DX + a2 DX^2 + ... Each coefficient (a0, a1, a2, etc) can be a constant or a 2D xy field dependent polynomial. ')


    _ElementMap = {
        __Unit.name() : __Unit,
        __DispAngle.name() : __DispAngle,
        __PolyOrder.name() : __PolyOrder,
        __Version.name() : __Version,
        __End.name() : __End,
        __Start.name() : __Start,
        __ComputationDate.name() : __ComputationDate,
        __CalibrationDataPath.name() : __CalibrationDataPath,
        __Coefficients.name() : __Coefficients
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'curvatureModel', curvatureModel)


# Complex type dispersionFunction with content type ELEMENT_ONLY
class dispersionFunction (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dispersionFunction')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}Coefficients uses Python identifier Coefficients
    __Coefficients = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), 'Coefficients', '__httpeuclid_esa_orgschemainsnis_dispersionFunction_httpeuclid_esa_orgschemainsnisCoefficients', True)

    
    Coefficients = property(__Coefficients.value, __Coefficients.set, None, u'The coefficients of the polynomial DL = a0 + a1 DX + a2 DX^2 + ..., where DX is the distance along the trace. Each coefficient (a0, a1, a2, etc) can be a constant or a 2D xy field dependent polynomial. ')

    
    # Element {http://euclid.esa.org/schema/ins/nis}ComputationDate uses Python identifier ComputationDate
    __ComputationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), 'ComputationDate', '__httpeuclid_esa_orgschemainsnis_dispersionFunction_httpeuclid_esa_orgschemainsnisComputationDate', False)

    
    ComputationDate = property(__ComputationDate.value, __ComputationDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}CalibrationDataPath uses Python identifier CalibrationDataPath
    __CalibrationDataPath = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath'), 'CalibrationDataPath', '__httpeuclid_esa_orgschemainsnis_dispersionFunction_httpeuclid_esa_orgschemainsnisCalibrationDataPath', False)

    
    CalibrationDataPath = property(__CalibrationDataPath.value, __CalibrationDataPath.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}DXUnit uses Python identifier DXUnit
    __DXUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DXUnit'), 'DXUnit', '__httpeuclid_esa_orgschemainsnis_dispersionFunction_httpeuclid_esa_orgschemainsnisDXUnit', False)

    
    DXUnit = property(__DXUnit.value, __DXUnit.set, None, u'The unit used for the displacement DX in the dispersion function. Default: um')

    
    # Element {http://euclid.esa.org/schema/ins/nis}PolyOrder uses Python identifier PolyOrder
    __PolyOrder = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PolyOrder'), 'PolyOrder', '__httpeuclid_esa_orgschemainsnis_dispersionFunction_httpeuclid_esa_orgschemainsnisPolyOrder', False)

    
    PolyOrder = property(__PolyOrder.value, __PolyOrder.set, None, u'The order of the polynomial DL = a0 + a1 DX + a2 DX^2 + ..., where DX is the distance along the trace.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}DLUnit uses Python identifier DLUnit
    __DLUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DLUnit'), 'DLUnit', '__httpeuclid_esa_orgschemainsnis_dispersionFunction_httpeuclid_esa_orgschemainsnisDLUnit', False)

    
    DLUnit = property(__DLUnit.value, __DLUnit.set, None, u'The unit used for the dispersion DL in the dispersion function. Default: Angstrom')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemainsnis_dispersionFunction_httpeuclid_esa_orgschemainsnisVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)


    _ElementMap = {
        __Coefficients.name() : __Coefficients,
        __ComputationDate.name() : __ComputationDate,
        __CalibrationDataPath.name() : __CalibrationDataPath,
        __DXUnit.name() : __DXUnit,
        __PolyOrder.name() : __PolyOrder,
        __DLUnit.name() : __DLUnit,
        __Version.name() : __Version
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'dispersionFunction', dispersionFunction)


# Complex type distortionModel with content type ELEMENT_ONLY
class distortionModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'distortionModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemainsnis_distortionModel_httpeuclid_esa_orgschemainsnisUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, u'The unit used to describe the polynomial coefficients of the X and Y offsets. Default: um')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Yoff uses Python identifier Yoff
    __Yoff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Yoff'), 'Yoff', '__httpeuclid_esa_orgschemainsnis_distortionModel_httpeuclid_esa_orgschemainsnisYoff', False)

    
    Yoff = property(__Yoff.value, __Yoff.set, None, u'A column offset between the reference position of this grism order and the position of the object on the FPA. This can be a 2D field dependent representation.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Xoff uses Python identifier Xoff
    __Xoff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Xoff'), 'Xoff', '__httpeuclid_esa_orgschemainsnis_distortionModel_httpeuclid_esa_orgschemainsnisXoff', False)

    
    Xoff = property(__Xoff.value, __Xoff.set, None, u'A row offset between the reference position of this grism order and the position of the object on the FPA. This can be a 2D field dependent representation.')


    _ElementMap = {
        __Unit.name() : __Unit,
        __Yoff.name() : __Yoff,
        __Xoff.name() : __Xoff
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'distortionModel', distortionModel)


# Complex type filterModeModel with content type ELEMENT_ONLY
class filterModeModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'filterModeModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}PSF uses Python identifier PSF
    __PSF = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PSF'), 'PSF', '__httpeuclid_esa_orgschemainsnis_filterModeModel_httpeuclid_esa_orgschemainsnisPSF', False)

    
    PSF = property(__PSF.value, __PSF.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Distortion uses Python identifier Distortion
    __Distortion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Distortion'), 'Distortion', '__httpeuclid_esa_orgschemainsnis_filterModeModel_httpeuclid_esa_orgschemainsnisDistortion', False)

    
    Distortion = property(__Distortion.value, __Distortion.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}FilterName uses Python identifier FilterName
    __FilterName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FilterName'), 'FilterName', '__httpeuclid_esa_orgschemainsnis_filterModeModel_httpeuclid_esa_orgschemainsnisFilterName', False)

    
    FilterName = property(__FilterName.value, __FilterName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Transmission uses Python identifier Transmission
    __Transmission = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Transmission'), 'Transmission', '__httpeuclid_esa_orgschemainsnis_filterModeModel_httpeuclid_esa_orgschemainsnisTransmission', False)

    
    Transmission = property(__Transmission.value, __Transmission.set, None, None)


    _ElementMap = {
        __PSF.name() : __PSF,
        __Distortion.name() : __Distortion,
        __FilterName.name() : __FilterName,
        __Transmission.name() : __Transmission
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'filterModeModel', filterModeModel)


# Complex type pixelPSF with content type ELEMENT_ONLY
class pixelPSF (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pixelPSF')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}FitsCubeImage uses Python identifier FitsCubeImage
    __FitsCubeImage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FitsCubeImage'), 'FitsCubeImage', '__httpeuclid_esa_orgschemainsnis_pixelPSF_httpeuclid_esa_orgschemainsnisFitsCubeImage', True)

    
    FitsCubeImage = property(__FitsCubeImage.value, __FitsCubeImage.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}ReferenceChip uses Python identifier ReferenceChip
    __ReferenceChip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReferenceChip'), 'ReferenceChip', '__httpeuclid_esa_orgschemainsnis_pixelPSF_httpeuclid_esa_orgschemainsnisReferenceChip', True)

    
    ReferenceChip = property(__ReferenceChip.value, __ReferenceChip.set, None, None)


    _ElementMap = {
        __FitsCubeImage.name() : __FitsCubeImage,
        __ReferenceChip.name() : __ReferenceChip
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'pixelPSF', pixelPSF)


# Complex type nispNoiseModel with content type ELEMENT_ONLY
class nispNoiseModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nispNoiseModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}StraylightNoiseModel uses Python identifier StraylightNoiseModel
    __StraylightNoiseModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StraylightNoiseModel'), 'StraylightNoiseModel', '__httpeuclid_esa_orgschemainsnis_nispNoiseModel_httpeuclid_esa_orgschemainsnisStraylightNoiseModel', False)

    
    StraylightNoiseModel = property(__StraylightNoiseModel.value, __StraylightNoiseModel.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}ThermalNoiseModel uses Python identifier ThermalNoiseModel
    __ThermalNoiseModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ThermalNoiseModel'), 'ThermalNoiseModel', '__httpeuclid_esa_orgschemainsnis_nispNoiseModel_httpeuclid_esa_orgschemainsnisThermalNoiseModel', False)

    
    ThermalNoiseModel = property(__ThermalNoiseModel.value, __ThermalNoiseModel.set, None, None)


    _ElementMap = {
        __StraylightNoiseModel.name() : __StraylightNoiseModel,
        __ThermalNoiseModel.name() : __ThermalNoiseModel
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nispNoiseModel', nispNoiseModel)


# Complex type straylightNoiseModel with content type ELEMENT_ONLY
class straylightNoiseModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'straylightNoiseModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}Noise uses Python identifier Noise
    __Noise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Noise'), 'Noise', '__httpeuclid_esa_orgschemainsnis_straylightNoiseModel_httpeuclid_esa_orgschemainsnisNoise', False)

    
    Noise = property(__Noise.value, __Noise.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}InstrumentReference uses Python identifier InstrumentReference
    __InstrumentReference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InstrumentReference'), 'InstrumentReference', '__httpeuclid_esa_orgschemainsnis_straylightNoiseModel_httpeuclid_esa_orgschemainsnisInstrumentReference', False)

    
    InstrumentReference = property(__InstrumentReference.value, __InstrumentReference.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), 'Wavelength', '__httpeuclid_esa_orgschemainsnis_straylightNoiseModel_httpeuclid_esa_orgschemainsnisWavelength', False)

    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}ComputationDate uses Python identifier ComputationDate
    __ComputationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), 'ComputationDate', '__httpeuclid_esa_orgschemainsnis_straylightNoiseModel_httpeuclid_esa_orgschemainsnisComputationDate', False)

    
    ComputationDate = property(__ComputationDate.value, __ComputationDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemainsnis_straylightNoiseModel_httpeuclid_esa_orgschemainsnisVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)


    _ElementMap = {
        __Noise.name() : __Noise,
        __InstrumentReference.name() : __InstrumentReference,
        __Wavelength.name() : __Wavelength,
        __ComputationDate.name() : __ComputationDate,
        __Version.name() : __Version
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'straylightNoiseModel', straylightNoiseModel)


# Complex type transmissionFitsFile with content type ELEMENT_ONLY
class transmissionFitsFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'transmissionFitsFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'nis.transmission', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'transmissionFitsFile', transmissionFitsFile)


# Complex type thermalNoiseModel with content type ELEMENT_ONLY
class thermalNoiseModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'thermalNoiseModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemainsnis_thermalNoiseModel_httpeuclid_esa_orgschemainsnisVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}InstrumentReference uses Python identifier InstrumentReference
    __InstrumentReference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InstrumentReference'), 'InstrumentReference', '__httpeuclid_esa_orgschemainsnis_thermalNoiseModel_httpeuclid_esa_orgschemainsnisInstrumentReference', False)

    
    InstrumentReference = property(__InstrumentReference.value, __InstrumentReference.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Noise uses Python identifier Noise
    __Noise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Noise'), 'Noise', '__httpeuclid_esa_orgschemainsnis_thermalNoiseModel_httpeuclid_esa_orgschemainsnisNoise', False)

    
    Noise = property(__Noise.value, __Noise.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}ComputationDate uses Python identifier ComputationDate
    __ComputationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), 'ComputationDate', '__httpeuclid_esa_orgschemainsnis_thermalNoiseModel_httpeuclid_esa_orgschemainsnisComputationDate', False)

    
    ComputationDate = property(__ComputationDate.value, __ComputationDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), 'Wavelength', '__httpeuclid_esa_orgschemainsnis_thermalNoiseModel_httpeuclid_esa_orgschemainsnisWavelength', False)

    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, None)


    _ElementMap = {
        __Version.name() : __Version,
        __InstrumentReference.name() : __InstrumentReference,
        __Noise.name() : __Noise,
        __ComputationDate.name() : __ComputationDate,
        __Wavelength.name() : __Wavelength
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'thermalNoiseModel', thermalNoiseModel)


# Complex type detectorSize with content type ELEMENT_ONLY
class detectorSize (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'detectorSize')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}NumberOfPixelsInX uses Python identifier NumberOfPixelsInX
    __NumberOfPixelsInX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumberOfPixelsInX'), 'NumberOfPixelsInX', '__httpeuclid_esa_orgschemainsnis_detectorSize_httpeuclid_esa_orgschemainsnisNumberOfPixelsInX', False)

    
    NumberOfPixelsInX = property(__NumberOfPixelsInX.value, __NumberOfPixelsInX.set, None, u'Number of pixels in X direction.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}NumberOfPixelsInY uses Python identifier NumberOfPixelsInY
    __NumberOfPixelsInY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumberOfPixelsInY'), 'NumberOfPixelsInY', '__httpeuclid_esa_orgschemainsnis_detectorSize_httpeuclid_esa_orgschemainsnisNumberOfPixelsInY', False)

    
    NumberOfPixelsInY = property(__NumberOfPixelsInY.value, __NumberOfPixelsInY.set, None, u'Number of pixels in Y direction.')


    _ElementMap = {
        __NumberOfPixelsInX.name() : __NumberOfPixelsInX,
        __NumberOfPixelsInY.name() : __NumberOfPixelsInY
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'detectorSize', detectorSize)


# Complex type readoutNoiseMap with content type ELEMENT_ONLY
class readoutNoiseMap (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'readoutNoiseMap')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'nis.detectorReadoutNoiseMap', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'readoutNoiseMap', readoutNoiseMap)


# Complex type darkCurrentModel with content type ELEMENT_ONLY
class darkCurrentModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'darkCurrentModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}DarkCurrentMap uses Python identifier DarkCurrentMap
    __DarkCurrentMap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DarkCurrentMap'), 'DarkCurrentMap', '__httpeuclid_esa_orgschemainsnis_darkCurrentModel_httpeuclid_esa_orgschemainsnisDarkCurrentMap', False)

    
    DarkCurrentMap = property(__DarkCurrentMap.value, __DarkCurrentMap.set, None, None)


    _ElementMap = {
        __DarkCurrentMap.name() : __DarkCurrentMap
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'darkCurrentModel', darkCurrentModel)


# Complex type quantumEfficiencyModel with content type ELEMENT_ONLY
class quantumEfficiencyModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'quantumEfficiencyModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}QuantumEfficiencyMap uses Python identifier QuantumEfficiencyMap
    __QuantumEfficiencyMap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'QuantumEfficiencyMap'), 'QuantumEfficiencyMap', '__httpeuclid_esa_orgschemainsnis_quantumEfficiencyModel_httpeuclid_esa_orgschemainsnisQuantumEfficiencyMap', False)

    
    QuantumEfficiencyMap = property(__QuantumEfficiencyMap.value, __QuantumEfficiencyMap.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}QuantumEfficiencyCube uses Python identifier QuantumEfficiencyCube
    __QuantumEfficiencyCube = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'QuantumEfficiencyCube'), 'QuantumEfficiencyCube', '__httpeuclid_esa_orgschemainsnis_quantumEfficiencyModel_httpeuclid_esa_orgschemainsnisQuantumEfficiencyCube', False)

    
    QuantumEfficiencyCube = property(__QuantumEfficiencyCube.value, __QuantumEfficiencyCube.set, None, None)


    _ElementMap = {
        __QuantumEfficiencyMap.name() : __QuantumEfficiencyMap,
        __QuantumEfficiencyCube.name() : __QuantumEfficiencyCube
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'quantumEfficiencyModel', quantumEfficiencyModel)


# Complex type readoutNoiseModel with content type ELEMENT_ONLY
class readoutNoiseModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'readoutNoiseModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}ReadoutNoiseMap uses Python identifier ReadoutNoiseMap
    __ReadoutNoiseMap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoiseMap'), 'ReadoutNoiseMap', '__httpeuclid_esa_orgschemainsnis_readoutNoiseModel_httpeuclid_esa_orgschemainsnisReadoutNoiseMap', False)

    
    ReadoutNoiseMap = property(__ReadoutNoiseMap.value, __ReadoutNoiseMap.set, None, None)


    _ElementMap = {
        __ReadoutNoiseMap.name() : __ReadoutNoiseMap
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'readoutNoiseModel', readoutNoiseModel)


# Complex type exposureTime with content type ELEMENT_ONLY
class exposureTime (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'exposureTime')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemainsnis_exposureTime_httpeuclid_esa_orgschemainsnisUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemainsnis_exposureTime_httpeuclid_esa_orgschemainsnisValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'exposureTime', exposureTime)


# Complex type cosmicRayModel with content type ELEMENT_ONLY
class cosmicRayModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cosmicRayModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}CosmicRayMap uses Python identifier CosmicRayMap
    __CosmicRayMap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CosmicRayMap'), 'CosmicRayMap', '__httpeuclid_esa_orgschemainsnis_cosmicRayModel_httpeuclid_esa_orgschemainsnisCosmicRayMap', False)

    
    CosmicRayMap = property(__CosmicRayMap.value, __CosmicRayMap.set, None, None)


    _ElementMap = {
        __CosmicRayMap.name() : __CosmicRayMap
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cosmicRayModel', cosmicRayModel)


# Complex type detector with content type ELEMENT_ONLY
class detector (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'detector')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}Size uses Python identifier Size
    __Size = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Size'), 'Size', '__httpeuclid_esa_orgschemainsnis_detector_httpeuclid_esa_orgschemainsnisSize', False)

    
    Size = property(__Size.value, __Size.set, None, u'The size of the detector in pixels.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}DarkCurrentModel uses Python identifier DarkCurrentModel
    __DarkCurrentModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DarkCurrentModel'), 'DarkCurrentModel', '__httpeuclid_esa_orgschemainsnis_detector_httpeuclid_esa_orgschemainsnisDarkCurrentModel', False)

    
    DarkCurrentModel = property(__DarkCurrentModel.value, __DarkCurrentModel.set, None, u'The dark current of the detector.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}QuantumEfficiencyModel uses Python identifier QuantumEfficiencyModel
    __QuantumEfficiencyModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'QuantumEfficiencyModel'), 'QuantumEfficiencyModel', '__httpeuclid_esa_orgschemainsnis_detector_httpeuclid_esa_orgschemainsnisQuantumEfficiencyModel', False)

    
    QuantumEfficiencyModel = property(__QuantumEfficiencyModel.value, __QuantumEfficiencyModel.set, None, u'The QE model of the detector.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}CosmicRayModel uses Python identifier CosmicRayModel
    __CosmicRayModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CosmicRayModel'), 'CosmicRayModel', '__httpeuclid_esa_orgschemainsnis_detector_httpeuclid_esa_orgschemainsnisCosmicRayModel', False)

    
    CosmicRayModel = property(__CosmicRayModel.value, __CosmicRayModel.set, None, u'The simulated cosmic ray map of the detector.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}ReadoutNoiseModel uses Python identifier ReadoutNoiseModel
    __ReadoutNoiseModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoiseModel'), 'ReadoutNoiseModel', '__httpeuclid_esa_orgschemainsnis_detector_httpeuclid_esa_orgschemainsnisReadoutNoiseModel', False)

    
    ReadoutNoiseModel = property(__ReadoutNoiseModel.value, __ReadoutNoiseModel.set, None, u'The readout noise model of the detector.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemainsnis_detector_httpeuclid_esa_orgschemainsnisIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)


    _ElementMap = {
        __Size.name() : __Size,
        __DarkCurrentModel.name() : __DarkCurrentModel,
        __QuantumEfficiencyModel.name() : __QuantumEfficiencyModel,
        __CosmicRayModel.name() : __CosmicRayModel,
        __ReadoutNoiseModel.name() : __ReadoutNoiseModel,
        __Identifier.name() : __Identifier
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'detector', detector)


# Complex type CTD_ANON with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}DetectorPosition uses Python identifier DetectorPosition
    __DetectorPosition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorPosition'), 'DetectorPosition', '__httpeuclid_esa_orgschemainsnis_CTD_ANON_httpeuclid_esa_orgschemainsnisDetectorPosition', True)

    
    DetectorPosition = property(__DetectorPosition.value, __DetectorPosition.set, None, None)


    _ElementMap = {
        __DetectorPosition.name() : __DetectorPosition
    }
    _AttributeMap = {
        
    }



# Complex type FPA with content type ELEMENT_ONLY
class FPA (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FPA')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}Ndetectors uses Python identifier Ndetectors
    __Ndetectors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ndetectors'), 'Ndetectors', '__httpeuclid_esa_orgschemainsnis_FPA_httpeuclid_esa_orgschemainsnisNdetectors', False)

    
    Ndetectors = property(__Ndetectors.value, __Ndetectors.set, None, u'Number of detectors in the FPA.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}DetectorList uses Python identifier DetectorList
    __DetectorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), 'DetectorList', '__httpeuclid_esa_orgschemainsnis_FPA_httpeuclid_esa_orgschemainsnisDetectorList', True)

    
    DetectorList = property(__DetectorList.value, __DetectorList.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemainsnis_FPA_httpeuclid_esa_orgschemainsnisName', False)

    
    Name = property(__Name.value, __Name.set, None, u'Name of the FPA VIS_FPA or NISP_FPA.')


    _ElementMap = {
        __Ndetectors.name() : __Ndetectors,
        __DetectorList.name() : __DetectorList,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'FPA', FPA)


# Complex type detectorInFPA with content type ELEMENT_ONLY
class detectorInFPA (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'detectorInFPA')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}YFPA uses Python identifier YFPA
    __YFPA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'YFPA'), 'YFPA', '__httpeuclid_esa_orgschemainsnis_detectorInFPA_httpeuclid_esa_orgschemainsnisYFPA', False)

    
    YFPA = property(__YFPA.value, __YFPA.set, None, u'Relative Y position of the detector in the FPA with respect to the FPA center, and in the North/East coordinate system.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}RotAngle uses Python identifier RotAngle
    __RotAngle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RotAngle'), 'RotAngle', '__httpeuclid_esa_orgschemainsnis_detectorInFPA_httpeuclid_esa_orgschemainsnisRotAngle', False)

    
    RotAngle = property(__RotAngle.value, __RotAngle.set, None, u'Rotation angle around the axis described by the vector normal to the FPA passing through the detector center. Angles are increasing CCW. Zero value means the detector is aligned with the North/East coordinate system. ')

    
    # Element {http://euclid.esa.org/schema/ins/nis}XFPA uses Python identifier XFPA
    __XFPA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XFPA'), 'XFPA', '__httpeuclid_esa_orgschemainsnis_detectorInFPA_httpeuclid_esa_orgschemainsnisXFPA', False)

    
    XFPA = property(__XFPA.value, __XFPA.set, None, u'Relative X position of the detector in the FPA with respect to the FPA center, and in the North/East coordinate system.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Elevation uses Python identifier Elevation
    __Elevation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Elevation'), 'Elevation', '__httpeuclid_esa_orgschemainsnis_detectorInFPA_httpeuclid_esa_orgschemainsnisElevation', False)

    
    Elevation = property(__Elevation.value, __Elevation.set, None, u'Elevation of the detector above or below the reference plane of the FPA.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemainsnis_detectorInFPA_httpeuclid_esa_orgschemainsnisIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)


    _ElementMap = {
        __YFPA.name() : __YFPA,
        __RotAngle.name() : __RotAngle,
        __XFPA.name() : __XFPA,
        __Elevation.name() : __Elevation,
        __Identifier.name() : __Identifier
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'detectorInFPA', detectorInFPA)


# Complex type focalPlaneArrangement with content type ELEMENT_ONLY
class focalPlaneArrangement (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'focalPlaneArrangement')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}NumberOfColumns uses Python identifier NumberOfColumns
    __NumberOfColumns = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumberOfColumns'), 'NumberOfColumns', '__httpeuclid_esa_orgschemainsnis_focalPlaneArrangement_httpeuclid_esa_orgschemainsnisNumberOfColumns', False)

    
    NumberOfColumns = property(__NumberOfColumns.value, __NumberOfColumns.set, None, u'Number of columns of detectors.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}DetectorPositionList uses Python identifier DetectorPositionList
    __DetectorPositionList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorPositionList'), 'DetectorPositionList', '__httpeuclid_esa_orgschemainsnis_focalPlaneArrangement_httpeuclid_esa_orgschemainsnisDetectorPositionList', False)

    
    DetectorPositionList = property(__DetectorPositionList.value, __DetectorPositionList.set, None, u'The detectors in the FPA.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemainsnis_focalPlaneArrangement_httpeuclid_esa_orgschemainsnisIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}NumberOfRows uses Python identifier NumberOfRows
    __NumberOfRows = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumberOfRows'), 'NumberOfRows', '__httpeuclid_esa_orgschemainsnis_focalPlaneArrangement_httpeuclid_esa_orgschemainsnisNumberOfRows', False)

    
    NumberOfRows = property(__NumberOfRows.value, __NumberOfRows.set, None, u'Number of rows of detectors.')


    _ElementMap = {
        __NumberOfColumns.name() : __NumberOfColumns,
        __DetectorPositionList.name() : __DetectorPositionList,
        __Identifier.name() : __Identifier,
        __NumberOfRows.name() : __NumberOfRows
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'focalPlaneArrangement', focalPlaneArrangement)


# Complex type grismOrderList with content type ELEMENT_ONLY
class grismOrderList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'grismOrderList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}GrismOrder uses Python identifier GrismOrder
    __GrismOrder = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GrismOrder'), 'GrismOrder', '__httpeuclid_esa_orgschemainsnis_grismOrderList_httpeuclid_esa_orgschemainsnisGrismOrder', True)

    
    GrismOrder = property(__GrismOrder.value, __GrismOrder.set, None, None)


    _ElementMap = {
        __GrismOrder.name() : __GrismOrder
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'grismOrderList', grismOrderList)


# Complex type detectorPosition with content type ELEMENT_ONLY
class detectorPosition (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'detectorPosition')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}Column uses Python identifier Column
    __Column = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Column'), 'Column', '__httpeuclid_esa_orgschemainsnis_detectorPosition_httpeuclid_esa_orgschemainsnisColumn', False)

    
    Column = property(__Column.value, __Column.set, None, u'The column in which the detector is in. The numbering starts from the left and from 0.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemainsnis_detectorPosition_httpeuclid_esa_orgschemainsnisIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'The identifier of the detector. Can be used to retrieve the detectors model.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Row uses Python identifier Row
    __Row = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Row'), 'Row', '__httpeuclid_esa_orgschemainsnis_detectorPosition_httpeuclid_esa_orgschemainsnisRow', False)

    
    Row = property(__Row.value, __Row.set, None, u'The row in which the detector is in. The numbering starts from the bottom and from 0.')


    _ElementMap = {
        __Column.name() : __Column,
        __Identifier.name() : __Identifier,
        __Row.name() : __Row
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'detectorPosition', detectorPosition)


# Complex type pixelPsfFitsFile with content type ELEMENT_ONLY
class pixelPsfFitsFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pixelPsfFitsFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'nis.pixelPsf', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'pixelPsfFitsFile', pixelPsfFitsFile)


# Complex type quantumEfficiencyMap with content type ELEMENT_ONLY
class quantumEfficiencyMap (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'quantumEfficiencyMap')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'nis.detectorQuantumEfficiencyMap', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'quantumEfficiencyMap', quantumEfficiencyMap)


# Complex type nisOpticsModel with content type ELEMENT_ONLY
class nisOpticsModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nisOpticsModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}GrismMode uses Python identifier GrismMode
    __GrismMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GrismMode'), 'GrismMode', '__httpeuclid_esa_orgschemainsnis_nisOpticsModel_httpeuclid_esa_orgschemainsnisGrismMode', True)

    
    GrismMode = property(__GrismMode.value, __GrismMode.set, None, None)


    _ElementMap = {
        __GrismMode.name() : __GrismMode
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nisOpticsModel', nisOpticsModel)


# Complex type pointSpreadFunction with content type ELEMENT_ONLY
class pointSpreadFunction (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pointSpreadFunction')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}PixelPSF uses Python identifier PixelPSF
    __PixelPSF = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PixelPSF'), 'PixelPSF', '__httpeuclid_esa_orgschemainsnis_pointSpreadFunction_httpeuclid_esa_orgschemainsnisPixelPSF', False)

    
    PixelPSF = property(__PixelPSF.value, __PixelPSF.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}ModelPSF uses Python identifier ModelPSF
    __ModelPSF = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ModelPSF'), 'ModelPSF', '__httpeuclid_esa_orgschemainsnis_pointSpreadFunction_httpeuclid_esa_orgschemainsnisModelPSF', False)

    
    ModelPSF = property(__ModelPSF.value, __ModelPSF.set, None, None)


    _ElementMap = {
        __PixelPSF.name() : __PixelPSF,
        __ModelPSF.name() : __ModelPSF
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'pointSpreadFunction', pointSpreadFunction)


# Complex type quantumEfficiencyCube with content type ELEMENT_ONLY
class quantumEfficiencyCube (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'quantumEfficiencyCube')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'nis.detectorQuantumEfficiencyCube', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'quantumEfficiencyCube', quantumEfficiencyCube)


# Complex type dataCubeElement with content type ELEMENT_ONLY
class dataCubeElement (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataCubeElement')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}FPAY uses Python identifier FPAY
    __FPAY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FPAY'), 'FPAY', '__httpeuclid_esa_orgschemainsnis_dataCubeElement_httpeuclid_esa_orgschemainsnisFPAY', False)

    
    FPAY = property(__FPAY.value, __FPAY.set, None, u'Y Position of the PSF centroid in the FPA.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Path uses Python identifier Path
    __Path = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Path'), 'Path', '__httpeuclid_esa_orgschemainsnis_dataCubeElement_httpeuclid_esa_orgschemainsnisPath', False)

    
    Path = property(__Path.value, __Path.set, None, u'Path to the dataCube in FITS format that contains for different locations in the FPA (X,Y), the normalized PSF in (X,Y,Lambda).')

    
    # Element {http://euclid.esa.org/schema/ins/nis}FPAX uses Python identifier FPAX
    __FPAX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FPAX'), 'FPAX', '__httpeuclid_esa_orgschemainsnis_dataCubeElement_httpeuclid_esa_orgschemainsnisFPAX', False)

    
    FPAX = property(__FPAX.value, __FPAX.set, None, u'X Position of the PSF centroid in the FPA.')


    _ElementMap = {
        __FPAY.name() : __FPAY,
        __Path.name() : __Path,
        __FPAX.name() : __FPAX
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'dataCubeElement', dataCubeElement)


# Complex type dataCube with content type ELEMENT_ONLY
class dataCube (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataCube')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}DataCubeElement uses Python identifier DataCubeElement
    __DataCubeElement = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataCubeElement'), 'DataCubeElement', '__httpeuclid_esa_orgschemainsnis_dataCube_httpeuclid_esa_orgschemainsnisDataCubeElement', True)

    
    DataCubeElement = property(__DataCubeElement.value, __DataCubeElement.set, None, None)


    _ElementMap = {
        __DataCubeElement.name() : __DataCubeElement
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'dataCube', dataCube)


# Complex type doubleGaussianPSF with content type ELEMENT_ONLY
class doubleGaussianPSF (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'doubleGaussianPSF')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}SigmaUnit uses Python identifier SigmaUnit
    __SigmaUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SigmaUnit'), 'SigmaUnit', '__httpeuclid_esa_orgschemainsnis_doubleGaussianPSF_httpeuclid_esa_orgschemainsnisSigmaUnit', False)

    
    SigmaUnit = property(__SigmaUnit.value, __SigmaUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}C uses Python identifier C
    __C = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'C'), 'C', '__httpeuclid_esa_orgschemainsnis_doubleGaussianPSF_httpeuclid_esa_orgschemainsnisC', False)

    
    C = property(__C.value, __C.set, None, u'Multiplicative factor of the small Gaussian. The big Gaussian is multiplied by (1-C). The coefficients of the polynomial describe the field dependence of this parameter.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}LambdaCoef uses Python identifier LambdaCoef
    __LambdaCoef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LambdaCoef'), 'LambdaCoef', '__httpeuclid_esa_orgschemainsnis_doubleGaussianPSF_httpeuclid_esa_orgschemainsnisLambdaCoef', False)

    
    LambdaCoef = property(__LambdaCoef.value, __LambdaCoef.set, None, u'Coefficient c1 of the model Sigma(\u03bb)=Sigma(\u03bbref) * (\u03bbref/\u03bb)^c1 describing the variations of the PSF as a function of wavelength in Angstroms.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Sigma2 uses Python identifier Sigma2
    __Sigma2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sigma2'), 'Sigma2', '__httpeuclid_esa_orgschemainsnis_doubleGaussianPSF_httpeuclid_esa_orgschemainsnisSigma2', False)

    
    Sigma2 = property(__Sigma2.value, __Sigma2.set, None, u'Width of the big Gaussian. The coefficients of the polynomial describe the field dependence of this parameter.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}Sigma1 uses Python identifier Sigma1
    __Sigma1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sigma1'), 'Sigma1', '__httpeuclid_esa_orgschemainsnis_doubleGaussianPSF_httpeuclid_esa_orgschemainsnisSigma1', False)

    
    Sigma1 = property(__Sigma1.value, __Sigma1.set, None, u'Width of the small Gaussian. The coefficients of the polynomial describe the field dependence of this parameter.')

    
    # Element {http://euclid.esa.org/schema/ins/nis}LambdaRef uses Python identifier LambdaRef
    __LambdaRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LambdaRef'), 'LambdaRef', '__httpeuclid_esa_orgschemainsnis_doubleGaussianPSF_httpeuclid_esa_orgschemainsnisLambdaRef', False)

    
    LambdaRef = property(__LambdaRef.value, __LambdaRef.set, None, u'Wavelength at which the PSF parameters have been measured.')


    _ElementMap = {
        __SigmaUnit.name() : __SigmaUnit,
        __C.name() : __C,
        __LambdaCoef.name() : __LambdaCoef,
        __Sigma2.name() : __Sigma2,
        __Sigma1.name() : __Sigma1,
        __LambdaRef.name() : __LambdaRef
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'doubleGaussianPSF', doubleGaussianPSF)


# Complex type psf with content type ELEMENT_ONLY
class psf (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'psf')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/nis}DoubleGaussian uses Python identifier DoubleGaussian
    __DoubleGaussian = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DoubleGaussian'), 'DoubleGaussian', '__httpeuclid_esa_orgschemainsnis_psf_httpeuclid_esa_orgschemainsnisDoubleGaussian', False)

    
    DoubleGaussian = property(__DoubleGaussian.value, __DoubleGaussian.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}AnalyticExpression uses Python identifier AnalyticExpression
    __AnalyticExpression = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AnalyticExpression'), 'AnalyticExpression', '__httpeuclid_esa_orgschemainsnis_psf_httpeuclid_esa_orgschemainsnisAnalyticExpression', False)

    
    AnalyticExpression = property(__AnalyticExpression.value, __AnalyticExpression.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/nis}DataCube uses Python identifier DataCube
    __DataCube = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataCube'), 'DataCube', '__httpeuclid_esa_orgschemainsnis_psf_httpeuclid_esa_orgschemainsnisDataCube', False)

    
    DataCube = property(__DataCube.value, __DataCube.set, None, None)


    _ElementMap = {
        __DoubleGaussian.name() : __DoubleGaussian,
        __AnalyticExpression.name() : __AnalyticExpression,
        __DataCube.name() : __DataCube
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'psf', psf)



cosmicRayMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cosmicRayMap._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
cosmicRayMap._ContentModel = pyxb.binding.content.ParticleModel(cosmicRayMap._GroupModel, min_occurs=1, max_occurs=1)



nipOpticsModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FilterMode'), filterModeModel, scope=nipOpticsModel))
nipOpticsModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nipOpticsModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FilterMode')), min_occurs=1, max_occurs=None)
    )
nipOpticsModel._ContentModel = pyxb.binding.content.ParticleModel(nipOpticsModel._GroupModel, min_occurs=1, max_occurs=1)


darkCurrentMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(darkCurrentMap._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
darkCurrentMap._ContentModel = pyxb.binding.content.ParticleModel(darkCurrentMap._GroupModel, min_occurs=1, max_occurs=1)



spectrumRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinWavelengthValue'), pyxb.binding.datatypes.double, scope=spectrumRange, documentation=u''))

spectrumRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxWavelengthValue'), pyxb.binding.datatypes.double, scope=spectrumRange, documentation=u''))

spectrumRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RangeID'), CommonDM.dm.bas.spm_stub.spectralRangeId, scope=spectrumRange, documentation=u'Name or ID commonly used for this spectral band'))

spectrumRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=spectrumRange))

spectrumRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Resolution'), pyxb.binding.datatypes.double, scope=spectrumRange, documentation=u'The number of samples is equal to : max - min divided by resolution + 2 '))
spectrumRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrumRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RangeID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinWavelengthValue')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxWavelengthValue')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Resolution')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
spectrumRange._ContentModel = pyxb.binding.content.ParticleModel(spectrumRange._GroupModel, min_occurs=1, max_occurs=1)



grismModeModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GrismOrderList'), grismOrderList, scope=grismModeModel))

grismModeModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GrismName'), grismName, scope=grismModeModel))

grismModeModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=grismModeModel))
grismModeModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(grismModeModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(grismModeModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GrismName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(grismModeModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GrismOrderList')), min_occurs=1, max_occurs=1L)
    )
grismModeModel._ContentModel = pyxb.binding.content.ParticleModel(grismModeModel._GroupModel, min_occurs=1, max_occurs=1)



grismOrderModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OrderName'), grismOrderName, scope=grismOrderModel, documentation=u'Order name (A, B, etc)'))

grismOrderModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PSF'), psf, scope=grismOrderModel))

grismOrderModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Curvature'), curvatureModel, scope=grismOrderModel))

grismOrderModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Transmission'), transmissionFitsFile, scope=grismOrderModel))

grismOrderModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Dispersion'), dispersionFunction, scope=grismOrderModel))

grismOrderModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=grismOrderModel))

grismOrderModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Distortion'), distortionModel, scope=grismOrderModel))
grismOrderModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(grismOrderModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(grismOrderModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OrderName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(grismOrderModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Curvature')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(grismOrderModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dispersion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(grismOrderModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Distortion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(grismOrderModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PSF')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(grismOrderModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Transmission')), min_occurs=1, max_occurs=1)
    )
grismOrderModel._ContentModel = pyxb.binding.content.ParticleModel(grismOrderModel._GroupModel, min_occurs=1, max_occurs=1)



curvatureModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=curvatureModel, documentation=u'The unit used to describe the Start, End and polynomial coefficients of the trace. Default: um'))

curvatureModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DispAngle'), CommonDM.dm.bas.dtd_stub.degAngle, scope=curvatureModel, documentation=u'The dispersion direction (0 or 90). Counter-clockwise in the FPA frame.'))

curvatureModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PolyOrder'), pyxb.binding.datatypes.int, scope=curvatureModel, documentation=u'The order of the polynomial DY = a0 + a1 DX + a2 DX^2 + ...'))

curvatureModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), CommonDM.dm.sys_stub.version, scope=curvatureModel))

curvatureModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'End'), pyxb.binding.datatypes.double, scope=curvatureModel, documentation=u'The position of the end of the spectrum in the dispersion direction, blueward of the reference wavelength.'))

curvatureModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Start'), pyxb.binding.datatypes.double, scope=curvatureModel, documentation=u'The position of the beginning of the spectrum in the dispersion direction, redward of the reference wavelength.'))

curvatureModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), pyxb.binding.datatypes.dateTime, scope=curvatureModel))

curvatureModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=curvatureModel))

curvatureModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), CommonDM.dm.bas.mat_stub.xyPolynome, scope=curvatureModel, documentation=u'The coefficients of the polynomial DY = a0 + a1 DX + a2 DX^2 + ... Each coefficient (a0, a1, a2, etc) can be a constant or a 2D xy field dependent polynomial. '))
curvatureModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(curvatureModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(curvatureModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(curvatureModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(curvatureModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DispAngle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(curvatureModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Start')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(curvatureModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'End')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(curvatureModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PolyOrder')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(curvatureModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coefficients')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(curvatureModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
curvatureModel._ContentModel = pyxb.binding.content.ParticleModel(curvatureModel._GroupModel, min_occurs=1, max_occurs=1)



dispersionFunction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), CommonDM.dm.bas.mat_stub.xyPolynome, scope=dispersionFunction, documentation=u'The coefficients of the polynomial DL = a0 + a1 DX + a2 DX^2 + ..., where DX is the distance along the trace. Each coefficient (a0, a1, a2, etc) can be a constant or a 2D xy field dependent polynomial. '))

dispersionFunction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), pyxb.binding.datatypes.dateTime, scope=dispersionFunction))

dispersionFunction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=dispersionFunction))

dispersionFunction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DXUnit'), CommonDM.dm.bas.utd_stub.unit, scope=dispersionFunction, documentation=u'The unit used for the displacement DX in the dispersion function. Default: um'))

dispersionFunction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PolyOrder'), pyxb.binding.datatypes.int, scope=dispersionFunction, documentation=u'The order of the polynomial DL = a0 + a1 DX + a2 DX^2 + ..., where DX is the distance along the trace.'))

dispersionFunction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DLUnit'), CommonDM.dm.bas.utd_stub.unit, scope=dispersionFunction, documentation=u'The unit used for the dispersion DL in the dispersion function. Default: Angstrom'))

dispersionFunction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), CommonDM.dm.sys_stub.version, scope=dispersionFunction))
dispersionFunction._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(dispersionFunction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dispersionFunction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dispersionFunction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(dispersionFunction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PolyOrder')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dispersionFunction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coefficients')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(dispersionFunction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DXUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dispersionFunction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DLUnit')), min_occurs=1, max_occurs=1)
    )
dispersionFunction._ContentModel = pyxb.binding.content.ParticleModel(dispersionFunction._GroupModel, min_occurs=1, max_occurs=1)



distortionModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=distortionModel, documentation=u'The unit used to describe the polynomial coefficients of the X and Y offsets. Default: um'))

distortionModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Yoff'), CommonDM.dm.bas.mat_stub.xyPolynome, scope=distortionModel, documentation=u'A column offset between the reference position of this grism order and the position of the object on the FPA. This can be a 2D field dependent representation.'))

distortionModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Xoff'), CommonDM.dm.bas.mat_stub.xyPolynome, scope=distortionModel, documentation=u'A row offset between the reference position of this grism order and the position of the object on the FPA. This can be a 2D field dependent representation.'))
distortionModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(distortionModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Xoff')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(distortionModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Yoff')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(distortionModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
distortionModel._ContentModel = pyxb.binding.content.ParticleModel(distortionModel._GroupModel, min_occurs=1, max_occurs=1)



filterModeModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PSF'), psf, scope=filterModeModel))

filterModeModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Distortion'), distortionModel, scope=filterModeModel))

filterModeModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FilterName'), filterName, scope=filterModeModel))

filterModeModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Transmission'), transmissionFitsFile, scope=filterModeModel))
filterModeModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(filterModeModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FilterName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filterModeModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Transmission')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filterModeModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Distortion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filterModeModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PSF')), min_occurs=1, max_occurs=1)
    )
filterModeModel._ContentModel = pyxb.binding.content.ParticleModel(filterModeModel._GroupModel, min_occurs=1, max_occurs=1)



pixelPSF._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitsCubeImage'), pixelPsfFitsFile, scope=pixelPSF))

pixelPSF._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceChip'), pyxb.binding.datatypes.int, scope=pixelPSF))
pixelPSF._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelPSF._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceChip')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(pixelPSF._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FitsCubeImage')), min_occurs=1, max_occurs=None)
    )
pixelPSF._ContentModel = pyxb.binding.content.ParticleModel(pixelPSF._GroupModel, min_occurs=1, max_occurs=1)



nispNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StraylightNoiseModel'), straylightNoiseModel, scope=nispNoiseModel))

nispNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ThermalNoiseModel'), thermalNoiseModel, scope=nispNoiseModel))
nispNoiseModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nispNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ThermalNoiseModel')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StraylightNoiseModel')), min_occurs=1, max_occurs=1)
    )
nispNoiseModel._ContentModel = pyxb.binding.content.ParticleModel(nispNoiseModel._GroupModel, min_occurs=1, max_occurs=1)



straylightNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Noise'), CommonDM.dm.ins_stub.noise, scope=straylightNoiseModel))

straylightNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InstrumentReference'), pyxb.binding.datatypes.string, scope=straylightNoiseModel))

straylightNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), CommonDM.dm.ins_stub.wavelength, scope=straylightNoiseModel))

straylightNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), pyxb.binding.datatypes.dateTime, scope=straylightNoiseModel))

straylightNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), CommonDM.dm.sys_stub.version, scope=straylightNoiseModel))
straylightNoiseModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(straylightNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(straylightNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(straylightNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InstrumentReference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(straylightNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Wavelength')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(straylightNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Noise')), min_occurs=1, max_occurs=1)
    )
straylightNoiseModel._ContentModel = pyxb.binding.content.ParticleModel(straylightNoiseModel._GroupModel, min_occurs=1, max_occurs=1)


transmissionFitsFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(transmissionFitsFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
transmissionFitsFile._ContentModel = pyxb.binding.content.ParticleModel(transmissionFitsFile._GroupModel, min_occurs=1, max_occurs=1)



thermalNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), CommonDM.dm.sys_stub.version, scope=thermalNoiseModel))

thermalNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InstrumentReference'), pyxb.binding.datatypes.string, scope=thermalNoiseModel))

thermalNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Noise'), CommonDM.dm.ins_stub.noise, scope=thermalNoiseModel))

thermalNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), pyxb.binding.datatypes.dateTime, scope=thermalNoiseModel))

thermalNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), CommonDM.dm.ins_stub.wavelength, scope=thermalNoiseModel))
thermalNoiseModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(thermalNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thermalNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thermalNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InstrumentReference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thermalNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Wavelength')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thermalNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Noise')), min_occurs=1, max_occurs=1)
    )
thermalNoiseModel._ContentModel = pyxb.binding.content.ParticleModel(thermalNoiseModel._GroupModel, min_occurs=1, max_occurs=1)



detectorSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumberOfPixelsInX'), pyxb.binding.datatypes.int, scope=detectorSize, documentation=u'Number of pixels in X direction.'))

detectorSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumberOfPixelsInY'), pyxb.binding.datatypes.int, scope=detectorSize, documentation=u'Number of pixels in Y direction.'))
detectorSize._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(detectorSize._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumberOfPixelsInX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detectorSize._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumberOfPixelsInY')), min_occurs=1, max_occurs=1)
    )
detectorSize._ContentModel = pyxb.binding.content.ParticleModel(detectorSize._GroupModel, min_occurs=1, max_occurs=1)


readoutNoiseMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(readoutNoiseMap._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
readoutNoiseMap._ContentModel = pyxb.binding.content.ParticleModel(readoutNoiseMap._GroupModel, min_occurs=1, max_occurs=1)



darkCurrentModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DarkCurrentMap'), darkCurrentMap, scope=darkCurrentModel))
darkCurrentModel._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(darkCurrentModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DarkCurrentMap')), min_occurs=1, max_occurs=1)
    )
darkCurrentModel._ContentModel = pyxb.binding.content.ParticleModel(darkCurrentModel._GroupModel, min_occurs=1, max_occurs=1)



quantumEfficiencyModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuantumEfficiencyMap'), quantumEfficiencyMap, scope=quantumEfficiencyModel))

quantumEfficiencyModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuantumEfficiencyCube'), quantumEfficiencyCube, scope=quantumEfficiencyModel))
quantumEfficiencyModel._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(quantumEfficiencyModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QuantumEfficiencyMap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(quantumEfficiencyModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QuantumEfficiencyCube')), min_occurs=1, max_occurs=1)
    )
quantumEfficiencyModel._ContentModel = pyxb.binding.content.ParticleModel(quantumEfficiencyModel._GroupModel, min_occurs=1, max_occurs=1)



readoutNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoiseMap'), readoutNoiseMap, scope=readoutNoiseModel))
readoutNoiseModel._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(readoutNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoiseMap')), min_occurs=1, max_occurs=1)
    )
readoutNoiseModel._ContentModel = pyxb.binding.content.ParticleModel(readoutNoiseModel._GroupModel, min_occurs=1, max_occurs=1)



exposureTime._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=exposureTime))

exposureTime._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.double, scope=exposureTime))
exposureTime._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(exposureTime._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(exposureTime._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
exposureTime._ContentModel = pyxb.binding.content.ParticleModel(exposureTime._GroupModel, min_occurs=1, max_occurs=1)



cosmicRayModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CosmicRayMap'), cosmicRayMap, scope=cosmicRayModel))
cosmicRayModel._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(cosmicRayModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CosmicRayMap')), min_occurs=1, max_occurs=1)
    )
cosmicRayModel._ContentModel = pyxb.binding.content.ParticleModel(cosmicRayModel._GroupModel, min_occurs=1, max_occurs=1)



detector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Size'), detectorSize, scope=detector, documentation=u'The size of the detector in pixels.'))

detector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DarkCurrentModel'), darkCurrentModel, scope=detector, documentation=u'The dark current of the detector.'))

detector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuantumEfficiencyModel'), quantumEfficiencyModel, scope=detector, documentation=u'The QE model of the detector.'))

detector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CosmicRayModel'), cosmicRayModel, scope=detector, documentation=u'The simulated cosmic ray map of the detector.'))

detector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoiseModel'), readoutNoiseModel, scope=detector, documentation=u'The readout noise model of the detector.'))

detector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=detector))
detector._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(detector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Size')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QuantumEfficiencyModel')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoiseModel')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DarkCurrentModel')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CosmicRayModel')), min_occurs=0L, max_occurs=1)
    )
detector._ContentModel = pyxb.binding.content.ParticleModel(detector._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorPosition'), detectorPosition, scope=CTD_ANON))
CTD_ANON._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorPosition')), min_occurs=1L, max_occurs=None)
    )
CTD_ANON._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON._GroupModel, min_occurs=1, max_occurs=1)



FPA._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ndetectors'), pyxb.binding.datatypes.int, scope=FPA, documentation=u'Number of detectors in the FPA.'))

FPA._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), detectorInFPA, scope=FPA))

FPA._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), FPAName, scope=FPA, documentation=u'Name of the FPA VIS_FPA or NISP_FPA.'))
FPA._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(FPA._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(FPA._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ndetectors')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(FPA._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorList')), min_occurs=1L, max_occurs=None)
    )
FPA._ContentModel = pyxb.binding.content.ParticleModel(FPA._GroupModel, min_occurs=1, max_occurs=1)



detectorInFPA._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'YFPA'), CommonDM.dm.bas.dtd_stub.doubleUnit, scope=detectorInFPA, documentation=u'Relative Y position of the detector in the FPA with respect to the FPA center, and in the North/East coordinate system.'))

detectorInFPA._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RotAngle'), CommonDM.dm.bas.dtd_stub.doubleUnit, scope=detectorInFPA, documentation=u'Rotation angle around the axis described by the vector normal to the FPA passing through the detector center. Angles are increasing CCW. Zero value means the detector is aligned with the North/East coordinate system. '))

detectorInFPA._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XFPA'), CommonDM.dm.bas.dtd_stub.doubleUnit, scope=detectorInFPA, documentation=u'Relative X position of the detector in the FPA with respect to the FPA center, and in the North/East coordinate system.'))

detectorInFPA._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Elevation'), CommonDM.dm.bas.dtd_stub.doubleUnit, scope=detectorInFPA, documentation=u'Elevation of the detector above or below the reference plane of the FPA.'))

detectorInFPA._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), CommonDM.dm.ins_stub.detectorId, scope=detectorInFPA))
detectorInFPA._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(detectorInFPA._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XFPA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detectorInFPA._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'YFPA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detectorInFPA._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RotAngle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detectorInFPA._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Elevation')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detectorInFPA._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1)
    )
detectorInFPA._ContentModel = pyxb.binding.content.ParticleModel(detectorInFPA._GroupModel, min_occurs=1, max_occurs=1)



focalPlaneArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumberOfColumns'), pyxb.binding.datatypes.int, scope=focalPlaneArrangement, documentation=u'Number of columns of detectors.'))

focalPlaneArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorPositionList'), CTD_ANON, scope=focalPlaneArrangement, documentation=u'The detectors in the FPA.'))

focalPlaneArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=focalPlaneArrangement))

focalPlaneArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumberOfRows'), pyxb.binding.datatypes.int, scope=focalPlaneArrangement, documentation=u'Number of rows of detectors.'))
focalPlaneArrangement._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(focalPlaneArrangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(focalPlaneArrangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumberOfRows')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(focalPlaneArrangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumberOfColumns')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(focalPlaneArrangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorPositionList')), min_occurs=1, max_occurs=1)
    )
focalPlaneArrangement._ContentModel = pyxb.binding.content.ParticleModel(focalPlaneArrangement._GroupModel, min_occurs=1, max_occurs=1)



grismOrderList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GrismOrder'), grismOrderModel, scope=grismOrderList))
grismOrderList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(grismOrderList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GrismOrder')), min_occurs=1, max_occurs=None)
    )
grismOrderList._ContentModel = pyxb.binding.content.ParticleModel(grismOrderList._GroupModel, min_occurs=1, max_occurs=1)



detectorPosition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Column'), pyxb.binding.datatypes.int, scope=detectorPosition, documentation=u'The column in which the detector is in. The numbering starts from the left and from 0.'))

detectorPosition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=detectorPosition, documentation=u'The identifier of the detector. Can be used to retrieve the detectors model.'))

detectorPosition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Row'), pyxb.binding.datatypes.int, scope=detectorPosition, documentation=u'The row in which the detector is in. The numbering starts from the bottom and from 0.'))
detectorPosition._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(detectorPosition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detectorPosition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Row')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detectorPosition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Column')), min_occurs=1, max_occurs=1)
    )
detectorPosition._ContentModel = pyxb.binding.content.ParticleModel(detectorPosition._GroupModel, min_occurs=1, max_occurs=1)


pixelPsfFitsFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelPsfFitsFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
pixelPsfFitsFile._ContentModel = pyxb.binding.content.ParticleModel(pixelPsfFitsFile._GroupModel, min_occurs=1, max_occurs=1)


quantumEfficiencyMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(quantumEfficiencyMap._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
quantumEfficiencyMap._ContentModel = pyxb.binding.content.ParticleModel(quantumEfficiencyMap._GroupModel, min_occurs=1, max_occurs=1)



nisOpticsModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GrismMode'), grismModeModel, scope=nisOpticsModel))
nisOpticsModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nisOpticsModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GrismMode')), min_occurs=1, max_occurs=None)
    )
nisOpticsModel._ContentModel = pyxb.binding.content.ParticleModel(nisOpticsModel._GroupModel, min_occurs=1, max_occurs=1)



pointSpreadFunction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PixelPSF'), pixelPSF, scope=pointSpreadFunction))

pointSpreadFunction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModelPSF'), CommonDM.dm.bas.mat_stub.varXYpolynomialModel, scope=pointSpreadFunction))
pointSpreadFunction._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(pointSpreadFunction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PixelPSF')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pointSpreadFunction._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ModelPSF')), min_occurs=1, max_occurs=1)
    )
pointSpreadFunction._ContentModel = pyxb.binding.content.ParticleModel(pointSpreadFunction._GroupModel, min_occurs=1, max_occurs=1)


quantumEfficiencyCube._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(quantumEfficiencyCube._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
quantumEfficiencyCube._ContentModel = pyxb.binding.content.ParticleModel(quantumEfficiencyCube._GroupModel, min_occurs=1, max_occurs=1)



dataCubeElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FPAY'), CommonDM.dm.bas.dtd_stub.doubleUnit, scope=dataCubeElement, documentation=u'Y Position of the PSF centroid in the FPA.'))

dataCubeElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Path'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=dataCubeElement, documentation=u'Path to the dataCube in FITS format that contains for different locations in the FPA (X,Y), the normalized PSF in (X,Y,Lambda).'))

dataCubeElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FPAX'), CommonDM.dm.bas.dtd_stub.doubleUnit, scope=dataCubeElement, documentation=u'X Position of the PSF centroid in the FPA.'))
dataCubeElement._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(dataCubeElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPAX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataCubeElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPAY')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataCubeElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Path')), min_occurs=1, max_occurs=1)
    )
dataCubeElement._ContentModel = pyxb.binding.content.ParticleModel(dataCubeElement._GroupModel, min_occurs=1, max_occurs=1)



dataCube._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataCubeElement'), dataCubeElement, scope=dataCube))
dataCube._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(dataCube._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataCubeElement')), min_occurs=1L, max_occurs=None)
    )
dataCube._ContentModel = pyxb.binding.content.ParticleModel(dataCube._GroupModel, min_occurs=1, max_occurs=1)



doubleGaussianPSF._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SigmaUnit'), CommonDM.dm.bas.utd_stub.unit, scope=doubleGaussianPSF))

doubleGaussianPSF._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'C'), CommonDM.dm.bas.mat_stub.xyPolynome, scope=doubleGaussianPSF, documentation=u'Multiplicative factor of the small Gaussian. The big Gaussian is multiplied by (1-C). The coefficients of the polynomial describe the field dependence of this parameter.'))

doubleGaussianPSF._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LambdaCoef'), pyxb.binding.datatypes.double, scope=doubleGaussianPSF, documentation=u'Coefficient c1 of the model Sigma(\u03bb)=Sigma(\u03bbref) * (\u03bbref/\u03bb)^c1 describing the variations of the PSF as a function of wavelength in Angstroms.'))

doubleGaussianPSF._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sigma2'), CommonDM.dm.bas.mat_stub.xyPolynome, scope=doubleGaussianPSF, documentation=u'Width of the big Gaussian. The coefficients of the polynomial describe the field dependence of this parameter.'))

doubleGaussianPSF._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sigma1'), CommonDM.dm.bas.mat_stub.xyPolynome, scope=doubleGaussianPSF, documentation=u'Width of the small Gaussian. The coefficients of the polynomial describe the field dependence of this parameter.'))

doubleGaussianPSF._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LambdaRef'), CommonDM.dm.bas.dtd_stub.doubleUnit, scope=doubleGaussianPSF, documentation=u'Wavelength at which the PSF parameters have been measured.'))
doubleGaussianPSF._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(doubleGaussianPSF._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LambdaCoef')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(doubleGaussianPSF._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LambdaRef')), min_occurs=1L, max_occurs=1),
    pyxb.binding.content.ParticleModel(doubleGaussianPSF._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sigma1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(doubleGaussianPSF._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sigma2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(doubleGaussianPSF._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SigmaUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(doubleGaussianPSF._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'C')), min_occurs=1, max_occurs=1)
    )
doubleGaussianPSF._ContentModel = pyxb.binding.content.ParticleModel(doubleGaussianPSF._GroupModel, min_occurs=1, max_occurs=1)



psf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DoubleGaussian'), doubleGaussianPSF, scope=psf))

psf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AnalyticExpression'), CommonDM.dm.bas.mat_stub.analyticExpression, scope=psf))

psf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataCube'), dataCube, scope=psf))
psf._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(psf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AnalyticExpression')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(psf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataCube')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(psf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DoubleGaussian')), min_occurs=1, max_occurs=1)
    )
psf._ContentModel = pyxb.binding.content.ParticleModel(psf._GroupModel, min_occurs=1, max_occurs=1)
