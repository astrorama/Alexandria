# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/pro/sim_stub.py
# PyXB bindings for NamespaceModule
# NSM:e0267dec5fc6efe1abf4ebb30dbf85ca520d7023
# Generated 2014-03-17 18:50:36.639997 by PyXB version 1.1.2
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
import CommonDM.dm.ins.nis_stub
import CommonDM.dm.bas.utd_stub
import CommonDM.dm.bas.dtd_stub
import CommonDM.dm.sys.sgs_stub
import CommonDM.dm.bas.fit_stub
import CommonDM.dm.ins_stub
import CommonDM.dm.bas_stub
import CommonDM.dm.sys_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/sim', create_if_missing=True)
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
class objectType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'objectType')
    _Documentation = None
objectType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=objectType, enum_prefix=None)
objectType.Star = objectType._CF_enumeration.addEnumeration(unicode_value=u'Star')
objectType.CalibStar = objectType._CF_enumeration.addEnumeration(unicode_value=u'CalibStar')
objectType.Galaxy = objectType._CF_enumeration.addEnumeration(unicode_value=u'Galaxy')
objectType._InitializeFacetMap(objectType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'objectType', objectType)

# Atomic SimpleTypeDefinition
class averageReadoutNoiseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The behavior of the average readout noise in relation with the readout noise maps of the detectors."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'averageReadoutNoiseType')
    _Documentation = u'The behavior of the average readout noise in relation with the readout noise maps of the detectors.'
averageReadoutNoiseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=averageReadoutNoiseType, enum_prefix=None)
averageReadoutNoiseType.Normalize = averageReadoutNoiseType._CF_enumeration.addEnumeration(unicode_value=u'Normalize')
averageReadoutNoiseType.Override = averageReadoutNoiseType._CF_enumeration.addEnumeration(unicode_value=u'Override')
averageReadoutNoiseType._InitializeFacetMap(averageReadoutNoiseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'averageReadoutNoiseType', averageReadoutNoiseType)

# Atomic SimpleTypeDefinition
class tipsInputConfigurationId (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'tipsInputConfigurationId')
    _Documentation = None
tipsInputConfigurationId._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'tipsInputConfigurationId', tipsInputConfigurationId)

# Atomic SimpleTypeDefinition
class filterTransmissionId (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'filterTransmissionId')
    _Documentation = None
filterTransmissionId._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'filterTransmissionId', filterTransmissionId)

# Atomic SimpleTypeDefinition
class fpaPointingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Determines the point of the FPA for which the RA, DEC are given. It can be either "Center" or "BottomLeft"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fpaPointingType')
    _Documentation = u'Determines the point of the FPA for which the RA, DEC are given. It can be either "Center" or "BottomLeft".'
fpaPointingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fpaPointingType, enum_prefix=None)
fpaPointingType.Center = fpaPointingType._CF_enumeration.addEnumeration(unicode_value=u'Center')
fpaPointingType.BottomLeft = fpaPointingType._CF_enumeration.addEnumeration(unicode_value=u'BottomLeft')
fpaPointingType._InitializeFacetMap(fpaPointingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'fpaPointingType', fpaPointingType)

# Atomic SimpleTypeDefinition
class averageQuantumEfficiencyType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The behavior of the average QE in relation with the QE maps of the detectors."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'averageQuantumEfficiencyType')
    _Documentation = u'The behavior of the average QE in relation with the QE maps of the detectors.'
averageQuantumEfficiencyType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=averageQuantumEfficiencyType, enum_prefix=None)
averageQuantumEfficiencyType.Normalize = averageQuantumEfficiencyType._CF_enumeration.addEnumeration(unicode_value=u'Normalize')
averageQuantumEfficiencyType.Override = averageQuantumEfficiencyType._CF_enumeration.addEnumeration(unicode_value=u'Override')
averageQuantumEfficiencyType._InitializeFacetMap(averageQuantumEfficiencyType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'averageQuantumEfficiencyType', averageQuantumEfficiencyType)

# Atomic SimpleTypeDefinition
class averageDarkCurrentType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The behavior of the average dark current in relation with the dark current maps of the detectors."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'averageDarkCurrentType')
    _Documentation = u'The behavior of the average dark current in relation with the dark current maps of the detectors.'
averageDarkCurrentType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=averageDarkCurrentType, enum_prefix=None)
averageDarkCurrentType.Normalize = averageDarkCurrentType._CF_enumeration.addEnumeration(unicode_value=u'Normalize')
averageDarkCurrentType.Override = averageDarkCurrentType._CF_enumeration.addEnumeration(unicode_value=u'Override')
averageDarkCurrentType._InitializeFacetMap(averageDarkCurrentType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'averageDarkCurrentType', averageDarkCurrentType)

# Atomic SimpleTypeDefinition
class shapeletType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shapeletType')
    _Documentation = None
shapeletType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=shapeletType, enum_prefix=None)
shapeletType.CARTESIAN = shapeletType._CF_enumeration.addEnumeration(unicode_value=u'CARTESIAN')
shapeletType.RADIAL = shapeletType._CF_enumeration.addEnumeration(unicode_value=u'RADIAL')
shapeletType._InitializeFacetMap(shapeletType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'shapeletType', shapeletType)

# List SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON (pyxb.binding.basis.STD_list):

    """Simple type that is a list of CommonDM.dm.ins.nis_stub.grismOrderName."""

    _ExpandedName = None
    _Documentation = None

    _ItemType = CommonDM.dm.ins.nis_stub.grismOrderName
STD_ANON._InitializeFacetMap()

# Complex type spectrumProperties with content type ELEMENT_ONLY
class spectrumProperties (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrumProperties')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}ExpectedPhotometricRedshift uses Python identifier ExpectedPhotometricRedshift
    __ExpectedPhotometricRedshift = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpectedPhotometricRedshift'), 'ExpectedPhotometricRedshift', '__httpeuclid_esa_orgschemaprosim_spectrumProperties_httpeuclid_esa_orgschemaprosimExpectedPhotometricRedshift', False)

    
    ExpectedPhotometricRedshift = property(__ExpectedPhotometricRedshift.value, __ExpectedPhotometricRedshift.set, None, u'The expected photometric redshift of the object.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}EmissionLineList uses Python identifier EmissionLineList
    __EmissionLineList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EmissionLineList'), 'EmissionLineList', '__httpeuclid_esa_orgschemaprosim_spectrumProperties_httpeuclid_esa_orgschemaprosimEmissionLineList', False)

    
    EmissionLineList = property(__EmissionLineList.value, __EmissionLineList.set, None, u'A list with all the available emission lines of the object.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}Redshift uses Python identifier Redshift
    __Redshift = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Redshift'), 'Redshift', '__httpeuclid_esa_orgschemaprosim_spectrumProperties_httpeuclid_esa_orgschemaprosimRedshift', False)

    
    Redshift = property(__Redshift.value, __Redshift.set, None, u'The redshift of the object.')


    _ElementMap = {
        __ExpectedPhotometricRedshift.name() : __ExpectedPhotometricRedshift,
        __EmissionLineList.name() : __EmissionLineList,
        __Redshift.name() : __Redshift
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spectrumProperties', spectrumProperties)


# Complex type SED with content type ELEMENT_ONLY
class SED (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SED')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}WavelengthUnit uses Python identifier WavelengthUnit
    __WavelengthUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WavelengthUnit'), 'WavelengthUnit', '__httpeuclid_esa_orgschemaprosim_SED_httpeuclid_esa_orgschemaprosimWavelengthUnit', False)

    
    WavelengthUnit = property(__WavelengthUnit.value, __WavelengthUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}FluxUnit uses Python identifier FluxUnit
    __FluxUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FluxUnit'), 'FluxUnit', '__httpeuclid_esa_orgschemaprosim_SED_httpeuclid_esa_orgschemaprosimFluxUnit', False)

    
    FluxUnit = property(__FluxUnit.value, __FluxUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}CatalogName uses Python identifier CatalogName
    __CatalogName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CatalogName'), 'CatalogName', '__httpeuclid_esa_orgschemaprosim_SED_httpeuclid_esa_orgschemaprosimCatalogName', False)

    
    CatalogName = property(__CatalogName.value, __CatalogName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}SED uses Python identifier SED
    __SED = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SED'), 'SED', '__httpeuclid_esa_orgschemaprosim_SED_httpeuclid_esa_orgschemaprosimSED', True)

    
    SED = property(__SED.value, __SED.set, None, None)


    _ElementMap = {
        __WavelengthUnit.name() : __WavelengthUnit,
        __FluxUnit.name() : __FluxUnit,
        __CatalogName.name() : __CatalogName,
        __SED.name() : __SED
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'SED', SED)


# Complex type emissionLineList with content type ELEMENT_ONLY
class emissionLineList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'emissionLineList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}EmissionLine uses Python identifier EmissionLine
    __EmissionLine = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EmissionLine'), 'EmissionLine', '__httpeuclid_esa_orgschemaprosim_emissionLineList_httpeuclid_esa_orgschemaprosimEmissionLine', True)

    
    EmissionLine = property(__EmissionLine.value, __EmissionLine.set, None, None)


    _ElementMap = {
        __EmissionLine.name() : __EmissionLine
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'emissionLineList', emissionLineList)


# Complex type simFocalPlaneArangement with content type ELEMENT_ONLY
class simFocalPlaneArangement (CommonDM.dm.ins.nis_stub.focalPlaneArrangement):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'simFocalPlaneArangement')
    # Base type is CommonDM.dm.ins.nis_stub.focalPlaneArrangement
    
    # Element {http://euclid.esa.org/schema/pro/sim}Pixelsize_um uses Python identifier Pixelsize_um
    __Pixelsize_um = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Pixelsize_um'), 'Pixelsize_um', '__httpeuclid_esa_orgschemaprosim_simFocalPlaneArangement_httpeuclid_esa_orgschemaprosimPixelsize_um', False)

    
    Pixelsize_um = property(__Pixelsize_um.value, __Pixelsize_um.set, None, u'Mean pixel size for simulation purposes in microns.')

    
    # Element Identifier ({http://euclid.esa.org/schema/ins/nis}Identifier) inherited from {http://euclid.esa.org/schema/ins/nis}focalPlaneArrangement
    
    # Element DetectorPositionList ({http://euclid.esa.org/schema/ins/nis}DetectorPositionList) inherited from {http://euclid.esa.org/schema/ins/nis}focalPlaneArrangement
    
    # Element {http://euclid.esa.org/schema/pro/sim}AverageDarkCurrent uses Python identifier AverageDarkCurrent
    __AverageDarkCurrent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AverageDarkCurrent'), 'AverageDarkCurrent', '__httpeuclid_esa_orgschemaprosim_simFocalPlaneArangement_httpeuclid_esa_orgschemaprosimAverageDarkCurrent', False)

    
    AverageDarkCurrent = property(__AverageDarkCurrent.value, __AverageDarkCurrent.set, None, u'The average dark current (expressed in electrons/s/pix), to be used for all the pixels of all the detectors. This value is ment for simulation reasons only and, when present, will either override or normalize the more detailed readout noise models of the detectors (depending on its type attribute).')

    
    # Element NumberOfRows ({http://euclid.esa.org/schema/ins/nis}NumberOfRows) inherited from {http://euclid.esa.org/schema/ins/nis}focalPlaneArrangement
    
    # Element {http://euclid.esa.org/schema/pro/sim}AverageQuantumEfficiency uses Python identifier AverageQuantumEfficiency
    __AverageQuantumEfficiency = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AverageQuantumEfficiency'), 'AverageQuantumEfficiency', '__httpeuclid_esa_orgschemaprosim_simFocalPlaneArangement_httpeuclid_esa_orgschemaprosimAverageQuantumEfficiency', False)

    
    AverageQuantumEfficiency = property(__AverageQuantumEfficiency.value, __AverageQuantumEfficiency.set, None, u'The average quantum efficiency (expressed in electrons/photons), to be used for all the pixels of all the detectors. This value is ment for simulation reasons only and, when present, will either override or normalize the more detailed QE models of the detectors (depending on its type attribute).')

    
    # Element {http://euclid.esa.org/schema/pro/sim}Pixelsize uses Python identifier Pixelsize
    __Pixelsize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Pixelsize'), 'Pixelsize', '__httpeuclid_esa_orgschemaprosim_simFocalPlaneArangement_httpeuclid_esa_orgschemaprosimPixelsize', False)

    
    Pixelsize = property(__Pixelsize.value, __Pixelsize.set, None, u'Mean pixel size for simulation purposes in arcsec.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}DetectorGapInX uses Python identifier DetectorGapInX
    __DetectorGapInX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorGapInX'), 'DetectorGapInX', '__httpeuclid_esa_orgschemaprosim_simFocalPlaneArangement_httpeuclid_esa_orgschemaprosimDetectorGapInX', False)

    
    DetectorGapInX = property(__DetectorGapInX.value, __DetectorGapInX.set, None, u'The gap between adjacent detectors in the horizontal (X) direction, expressed in um. Inacive pixel margins are included. This value is ment for simulation reasons only and, when present, will override the per detector gap information from the FPA DetectorPositionList (only row/column information will be used).')

    
    # Element NumberOfColumns ({http://euclid.esa.org/schema/ins/nis}NumberOfColumns) inherited from {http://euclid.esa.org/schema/ins/nis}focalPlaneArrangement
    
    # Element {http://euclid.esa.org/schema/pro/sim}AverageReadoutNoise uses Python identifier AverageReadoutNoise
    __AverageReadoutNoise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AverageReadoutNoise'), 'AverageReadoutNoise', '__httpeuclid_esa_orgschemaprosim_simFocalPlaneArangement_httpeuclid_esa_orgschemaprosimAverageReadoutNoise', False)

    
    AverageReadoutNoise = property(__AverageReadoutNoise.value, __AverageReadoutNoise.set, None, u'The average readout noise (expressed in electrons/pix), to be used for all the pixels of all the detectors. This value is ment for simulation reasons only and, when present, will either override or normalize the more detailed readout noise models of the detectors (depending on its type attribute).')

    
    # Element {http://euclid.esa.org/schema/pro/sim}DetectorGapInY uses Python identifier DetectorGapInY
    __DetectorGapInY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorGapInY'), 'DetectorGapInY', '__httpeuclid_esa_orgschemaprosim_simFocalPlaneArangement_httpeuclid_esa_orgschemaprosimDetectorGapInY', False)

    
    DetectorGapInY = property(__DetectorGapInY.value, __DetectorGapInY.set, None, u'The gap between adjacent detectors in the vertical (Y) direction, expressed in um. Inacive pixel margins are included. This value is ment for simulation reasons only and, when present, will override the per detector gap information from the FPA DetectorPositionList (only row/column information will be used).')


    _ElementMap = CommonDM.dm.ins.nis_stub.focalPlaneArrangement._ElementMap.copy()
    _ElementMap.update({
        __Pixelsize_um.name() : __Pixelsize_um,
        __AverageDarkCurrent.name() : __AverageDarkCurrent,
        __AverageQuantumEfficiency.name() : __AverageQuantumEfficiency,
        __Pixelsize.name() : __Pixelsize,
        __DetectorGapInX.name() : __DetectorGapInX,
        __AverageReadoutNoise.name() : __AverageReadoutNoise,
        __DetectorGapInY.name() : __DetectorGapInY
    })
    _AttributeMap = CommonDM.dm.ins.nis_stub.focalPlaneArrangement._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'simFocalPlaneArangement', simFocalPlaneArangement)


# Complex type setOfSimulatedImages with content type ELEMENT_ONLY
class setOfSimulatedImages (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'setOfSimulatedImages')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}SimulatedDetectorImage uses Python identifier SimulatedDetectorImage
    __SimulatedDetectorImage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SimulatedDetectorImage'), 'SimulatedDetectorImage', '__httpeuclid_esa_orgschemaprosim_setOfSimulatedImages_httpeuclid_esa_orgschemaprosimSimulatedDetectorImage', True)

    
    SimulatedDetectorImage = property(__SimulatedDetectorImage.value, __SimulatedDetectorImage.set, None, None)


    _ElementMap = {
        __SimulatedDetectorImage.name() : __SimulatedDetectorImage
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'setOfSimulatedImages', setOfSimulatedImages)


# Complex type detectorList with content type ELEMENT_ONLY
class detectorList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'detectorList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}Detector uses Python identifier Detector
    __Detector = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Detector'), 'Detector', '__httpeuclid_esa_orgschemaprosim_detectorList_httpeuclid_esa_orgschemaprosimDetector', True)

    
    Detector = property(__Detector.value, __Detector.set, None, None)


    _ElementMap = {
        __Detector.name() : __Detector
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'detectorList', detectorList)


# Complex type visInputConfiguration with content type ELEMENT_ONLY
class visInputConfiguration (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visInputConfiguration')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}DetectorList uses Python identifier DetectorList
    __DetectorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), 'DetectorList', '__httpeuclid_esa_orgschemaprosim_visInputConfiguration_httpeuclid_esa_orgschemaprosimDetectorList', False)

    
    DetectorList = property(__DetectorList.value, __DetectorList.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemaprosim_visInputConfiguration_httpeuclid_esa_orgschemaprosimIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}FPA uses Python identifier FPA
    __FPA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FPA'), 'FPA', '__httpeuclid_esa_orgschemaprosim_visInputConfiguration_httpeuclid_esa_orgschemaprosimFPA', False)

    
    FPA = property(__FPA.value, __FPA.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}SimulationSettings uses Python identifier SimulationSettings
    __SimulationSettings = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SimulationSettings'), 'SimulationSettings', '__httpeuclid_esa_orgschemaprosim_visInputConfiguration_httpeuclid_esa_orgschemaprosimSimulationSettings', False)

    
    SimulationSettings = property(__SimulationSettings.value, __SimulationSettings.set, None, None)


    _ElementMap = {
        __DetectorList.name() : __DetectorList,
        __Identifier.name() : __Identifier,
        __FPA.name() : __FPA,
        __SimulationSettings.name() : __SimulationSettings
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'visInputConfiguration', visInputConfiguration)


# Complex type mirroring with content type ELEMENT_ONLY
class mirroring (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'mirroring')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}Y uses Python identifier Y
    __Y = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Y'), 'Y', '__httpeuclid_esa_orgschemaprosim_mirroring_httpeuclid_esa_orgschemaprosimY', False)

    
    Y = property(__Y.value, __Y.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}X uses Python identifier X
    __X = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'X'), 'X', '__httpeuclid_esa_orgschemaprosim_mirroring_httpeuclid_esa_orgschemaprosimX', False)

    
    X = property(__X.value, __X.set, None, None)


    _ElementMap = {
        __Y.name() : __Y,
        __X.name() : __X
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'mirroring', mirroring)


# Complex type wavelengthRange with content type ELEMENT_ONLY
class wavelengthRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wavelengthRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}WavelengthMax uses Python identifier WavelengthMax
    __WavelengthMax = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WavelengthMax'), 'WavelengthMax', '__httpeuclid_esa_orgschemaprosim_wavelengthRange_httpeuclid_esa_orgschemaprosimWavelengthMax', False)

    
    WavelengthMax = property(__WavelengthMax.value, __WavelengthMax.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}WavelenthUnit uses Python identifier WavelenthUnit
    __WavelenthUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WavelenthUnit'), 'WavelenthUnit', '__httpeuclid_esa_orgschemaprosim_wavelengthRange_httpeuclid_esa_orgschemaprosimWavelenthUnit', False)

    
    WavelenthUnit = property(__WavelenthUnit.value, __WavelenthUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}WavelengthMin uses Python identifier WavelengthMin
    __WavelengthMin = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WavelengthMin'), 'WavelengthMin', '__httpeuclid_esa_orgschemaprosim_wavelengthRange_httpeuclid_esa_orgschemaprosimWavelengthMin', False)

    
    WavelengthMin = property(__WavelengthMin.value, __WavelengthMin.set, None, None)


    _ElementMap = {
        __WavelengthMax.name() : __WavelengthMax,
        __WavelenthUnit.name() : __WavelenthUnit,
        __WavelengthMin.name() : __WavelengthMin
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'wavelengthRange', wavelengthRange)


# Complex type morphologyImage with content type ELEMENT_ONLY
class morphologyImage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'morphologyImage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}SurveyName uses Python identifier SurveyName
    __SurveyName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SurveyName'), 'SurveyName', '__httpeuclid_esa_orgschemaprosim_morphologyImage_httpeuclid_esa_orgschemaprosimSurveyName', False)

    
    SurveyName = property(__SurveyName.value, __SurveyName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Mirroring uses Python identifier Mirroring
    __Mirroring = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Mirroring'), 'Mirroring', '__httpeuclid_esa_orgschemaprosim_morphologyImage_httpeuclid_esa_orgschemaprosimMirroring', False)

    
    Mirroring = property(__Mirroring.value, __Mirroring.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}WavelengthRange uses Python identifier WavelengthRange
    __WavelengthRange = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WavelengthRange'), 'WavelengthRange', '__httpeuclid_esa_orgschemaprosim_morphologyImage_httpeuclid_esa_orgschemaprosimWavelengthRange', False)

    
    WavelengthRange = property(__WavelengthRange.value, __WavelengthRange.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}PositionAngle uses Python identifier PositionAngle
    __PositionAngle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PositionAngle'), 'PositionAngle', '__httpeuclid_esa_orgschemaprosim_morphologyImage_httpeuclid_esa_orgschemaprosimPositionAngle', False)

    
    PositionAngle = property(__PositionAngle.value, __PositionAngle.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Scaling uses Python identifier Scaling
    __Scaling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Scaling'), 'Scaling', '__httpeuclid_esa_orgschemaprosim_morphologyImage_httpeuclid_esa_orgschemaprosimScaling', False)

    
    Scaling = property(__Scaling.value, __Scaling.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}PositionAngleUnit uses Python identifier PositionAngleUnit
    __PositionAngleUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PositionAngleUnit'), 'PositionAngleUnit', '__httpeuclid_esa_orgschemaprosim_morphologyImage_httpeuclid_esa_orgschemaprosimPositionAngleUnit', False)

    
    PositionAngleUnit = property(__PositionAngleUnit.value, __PositionAngleUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}DataContainer uses Python identifier DataContainer
    __DataContainer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataContainer'), 'DataContainer', '__httpeuclid_esa_orgschemaprosim_morphologyImage_httpeuclid_esa_orgschemaprosimDataContainer', False)

    
    DataContainer = property(__DataContainer.value, __DataContainer.set, None, None)


    _ElementMap = {
        __SurveyName.name() : __SurveyName,
        __Mirroring.name() : __Mirroring,
        __WavelengthRange.name() : __WavelengthRange,
        __PositionAngle.name() : __PositionAngle,
        __Scaling.name() : __Scaling,
        __PositionAngleUnit.name() : __PositionAngleUnit,
        __DataContainer.name() : __DataContainer
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'morphologyImage', morphologyImage)


# Complex type spectraFitsFile with content type ELEMENT_ONLY
class spectraFitsFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectraFitsFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sim.spectra', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'spectraFitsFile', spectraFitsFile)


# Complex type magnitude with content type ELEMENT_ONLY
class magnitude (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'magnitude')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filter'), 'Filter', '__httpeuclid_esa_orgschemaprosim_magnitude_httpeuclid_esa_orgschemaprosimFilter', False)

    
    Filter = property(__Filter.value, __Filter.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Error uses Python identifier Error
    __Error = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Error'), 'Error', '__httpeuclid_esa_orgschemaprosim_magnitude_httpeuclid_esa_orgschemaprosimError', False)

    
    Error = property(__Error.value, __Error.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}MagType uses Python identifier MagType
    __MagType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagType'), 'MagType', '__httpeuclid_esa_orgschemaprosim_magnitude_httpeuclid_esa_orgschemaprosimMagType', False)

    
    MagType = property(__MagType.value, __MagType.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemaprosim_magnitude_httpeuclid_esa_orgschemaprosimValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Filter.name() : __Filter,
        __Error.name() : __Error,
        __MagType.name() : __MagType,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'magnitude', magnitude)


# Complex type averageReadoutNoise with content type SIMPLE
class averageReadoutNoise (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = CommonDM.dm.bas.dtd_stub.positiveDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'averageReadoutNoise')
    # Base type is CommonDM.dm.bas.dtd_stub.positiveDouble
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpeuclid_esa_orgschemaprosim_averageReadoutNoise_type', averageReadoutNoiseType, unicode_default=u'Override')
    
    type = property(__type.value, __type.set, None, u'Defines if the average RON will override or normalize the RON maps of the detectors. Defaults to override.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'averageReadoutNoise', averageReadoutNoise)


# Complex type simulatedImageFitsFile with content type ELEMENT_ONLY
class simulatedImageFitsFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'simulatedImageFitsFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sim.simulatedImage', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'simulatedImageFitsFile', simulatedImageFitsFile)


# Complex type simulatedExposureSequence with content type ELEMENT_ONLY
class simulatedExposureSequence (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'simulatedExposureSequence')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}ExposureDate uses Python identifier ExposureDate
    __ExposureDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureDate'), 'ExposureDate', '__httpeuclid_esa_orgschemaprosim_simulatedExposureSequence_httpeuclid_esa_orgschemaprosimExposureDate', False)

    
    ExposureDate = property(__ExposureDate.value, __ExposureDate.set, None, u'Refers to the Exposure Date expressed with the resolution of ms.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}FPAPointingRA uses Python identifier FPAPointingRA
    __FPAPointingRA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FPAPointingRA'), 'FPAPointingRA', '__httpeuclid_esa_orgschemaprosim_simulatedExposureSequence_httpeuclid_esa_orgschemaprosimFPAPointingRA', False)

    
    FPAPointingRA = property(__FPAPointingRA.value, __FPAPointingRA.set, None, u'Right Ascension of the pointing angles of the FPA via the telescope in the Bottom Left of the detector.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}FPAPointingDec uses Python identifier FPAPointingDec
    __FPAPointingDec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FPAPointingDec'), 'FPAPointingDec', '__httpeuclid_esa_orgschemaprosim_simulatedExposureSequence_httpeuclid_esa_orgschemaprosimFPAPointingDec', False)

    
    FPAPointingDec = property(__FPAPointingDec.value, __FPAPointingDec.set, None, u'Declinaison of the pointing angles of the FPA via the telescope in the Bottom Left of the detector.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}ExposureTime uses Python identifier ExposureTime
    __ExposureTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime'), 'ExposureTime', '__httpeuclid_esa_orgschemaprosim_simulatedExposureSequence_httpeuclid_esa_orgschemaprosimExposureTime', False)

    
    ExposureTime = property(__ExposureTime.value, __ExposureTime.set, None, u'Refers to the duration of Exposure expressed in seconds with the resolution of the us')

    
    # Element {http://euclid.esa.org/schema/pro/sim}SelectedGrism uses Python identifier SelectedGrism
    __SelectedGrism = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SelectedGrism'), 'SelectedGrism', '__httpeuclid_esa_orgschemaprosim_simulatedExposureSequence_httpeuclid_esa_orgschemaprosimSelectedGrism', False)

    
    SelectedGrism = property(__SelectedGrism.value, __SelectedGrism.set, None, u'Refers to the Grism mode selected : GBlue or Gred and polar angle 0 or 90')


    _ElementMap = {
        __ExposureDate.name() : __ExposureDate,
        __FPAPointingRA.name() : __FPAPointingRA,
        __FPAPointingDec.name() : __FPAPointingDec,
        __ExposureTime.name() : __ExposureTime,
        __SelectedGrism.name() : __SelectedGrism
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'simulatedExposureSequence', simulatedExposureSequence)


# Complex type shapeletModel with content type ELEMENT_ONLY
class shapeletModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shapeletModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Type'), 'Type', '__httpeuclid_esa_orgschemaprosim_shapeletModel_httpeuclid_esa_orgschemaprosimType', False)

    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}M uses Python identifier M
    __M = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'M'), 'M', '__httpeuclid_esa_orgschemaprosim_shapeletModel_httpeuclid_esa_orgschemaprosimM', False)

    
    M = property(__M.value, __M.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}N uses Python identifier N
    __N = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'N'), 'N', '__httpeuclid_esa_orgschemaprosim_shapeletModel_httpeuclid_esa_orgschemaprosimN', False)

    
    N = property(__N.value, __N.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Scale uses Python identifier Scale
    __Scale = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Scale'), 'Scale', '__httpeuclid_esa_orgschemaprosim_shapeletModel_httpeuclid_esa_orgschemaprosimScale', False)

    
    Scale = property(__Scale.value, __Scale.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Coefficients uses Python identifier Coefficients
    __Coefficients = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), 'Coefficients', '__httpeuclid_esa_orgschemaprosim_shapeletModel_httpeuclid_esa_orgschemaprosimCoefficients', True)

    
    Coefficients = property(__Coefficients.value, __Coefficients.set, None, u'Coefficients of shapelets as NxM matrix')


    _ElementMap = {
        __Type.name() : __Type,
        __M.name() : __M,
        __N.name() : __N,
        __Scale.name() : __Scale,
        __Coefficients.name() : __Coefficients
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'shapeletModel', shapeletModel)


# Complex type morphologyGeneric with content type ELEMENT_ONLY
class morphologyGeneric (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'morphologyGeneric')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}MinorAxisUnit uses Python identifier MinorAxisUnit
    __MinorAxisUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinorAxisUnit'), 'MinorAxisUnit', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimMinorAxisUnit', False)

    
    MinorAxisUnit = property(__MinorAxisUnit.value, __MinorAxisUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}MinorAxis uses Python identifier MinorAxis
    __MinorAxis = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinorAxis'), 'MinorAxis', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimMinorAxis', False)

    
    MinorAxis = property(__MinorAxis.value, __MinorAxis.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}BuldgeToTotal uses Python identifier BuldgeToTotal
    __BuldgeToTotal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BuldgeToTotal'), 'BuldgeToTotal', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimBuldgeToTotal', False)

    
    BuldgeToTotal = property(__BuldgeToTotal.value, __BuldgeToTotal.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}PositionAngle uses Python identifier PositionAngle
    __PositionAngle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PositionAngle'), 'PositionAngle', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimPositionAngle', False)

    
    PositionAngle = property(__PositionAngle.value, __PositionAngle.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}DiskHalfRadius uses Python identifier DiskHalfRadius
    __DiskHalfRadius = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DiskHalfRadius'), 'DiskHalfRadius', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimDiskHalfRadius', False)

    
    DiskHalfRadius = property(__DiskHalfRadius.value, __DiskHalfRadius.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}PositionAngleUnit uses Python identifier PositionAngleUnit
    __PositionAngleUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PositionAngleUnit'), 'PositionAngleUnit', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimPositionAngleUnit', False)

    
    PositionAngleUnit = property(__PositionAngleUnit.value, __PositionAngleUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}AxisRatio uses Python identifier AxisRatio
    __AxisRatio = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AxisRatio'), 'AxisRatio', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimAxisRatio', False)

    
    AxisRatio = property(__AxisRatio.value, __AxisRatio.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}DiskHalfRadiusUnit uses Python identifier DiskHalfRadiusUnit
    __DiskHalfRadiusUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DiskHalfRadiusUnit'), 'DiskHalfRadiusUnit', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimDiskHalfRadiusUnit', False)

    
    DiskHalfRadiusUnit = property(__DiskHalfRadiusUnit.value, __DiskHalfRadiusUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}MajorAxisUnit uses Python identifier MajorAxisUnit
    __MajorAxisUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MajorAxisUnit'), 'MajorAxisUnit', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimMajorAxisUnit', False)

    
    MajorAxisUnit = property(__MajorAxisUnit.value, __MajorAxisUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}BuldgeHalfRadius uses Python identifier BuldgeHalfRadius
    __BuldgeHalfRadius = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BuldgeHalfRadius'), 'BuldgeHalfRadius', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimBuldgeHalfRadius', False)

    
    BuldgeHalfRadius = property(__BuldgeHalfRadius.value, __BuldgeHalfRadius.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}MorphologicalType uses Python identifier MorphologicalType
    __MorphologicalType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MorphologicalType'), 'MorphologicalType', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimMorphologicalType', False)

    
    MorphologicalType = property(__MorphologicalType.value, __MorphologicalType.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}MajorAxis uses Python identifier MajorAxis
    __MajorAxis = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MajorAxis'), 'MajorAxis', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimMajorAxis', False)

    
    MajorAxis = property(__MajorAxis.value, __MajorAxis.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}BuldgeHalfRadiusUnit uses Python identifier BuldgeHalfRadiusUnit
    __BuldgeHalfRadiusUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BuldgeHalfRadiusUnit'), 'BuldgeHalfRadiusUnit', '__httpeuclid_esa_orgschemaprosim_morphologyGeneric_httpeuclid_esa_orgschemaprosimBuldgeHalfRadiusUnit', False)

    
    BuldgeHalfRadiusUnit = property(__BuldgeHalfRadiusUnit.value, __BuldgeHalfRadiusUnit.set, None, None)


    _ElementMap = {
        __MinorAxisUnit.name() : __MinorAxisUnit,
        __MinorAxis.name() : __MinorAxis,
        __BuldgeToTotal.name() : __BuldgeToTotal,
        __PositionAngle.name() : __PositionAngle,
        __DiskHalfRadius.name() : __DiskHalfRadius,
        __PositionAngleUnit.name() : __PositionAngleUnit,
        __AxisRatio.name() : __AxisRatio,
        __DiskHalfRadiusUnit.name() : __DiskHalfRadiusUnit,
        __MajorAxisUnit.name() : __MajorAxisUnit,
        __BuldgeHalfRadius.name() : __BuldgeHalfRadius,
        __MorphologicalType.name() : __MorphologicalType,
        __MajorAxis.name() : __MajorAxis,
        __BuldgeHalfRadiusUnit.name() : __BuldgeHalfRadiusUnit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'morphologyGeneric', morphologyGeneric)


# Complex type filterTransmission with content type ELEMENT_ONLY
class filterTransmission (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'filterTransmission')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), 'Wavelength', '__httpeuclid_esa_orgschemaprosim_filterTransmission_httpeuclid_esa_orgschemaprosimWavelength', False)

    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}TransmissionFactor uses Python identifier TransmissionFactor
    __TransmissionFactor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TransmissionFactor'), 'TransmissionFactor', '__httpeuclid_esa_orgschemaprosim_filterTransmission_httpeuclid_esa_orgschemaprosimTransmissionFactor', False)

    
    TransmissionFactor = property(__TransmissionFactor.value, __TransmissionFactor.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemaprosim_filterTransmission_httpeuclid_esa_orgschemaprosimVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}ErrorOnTransmission uses Python identifier ErrorOnTransmission
    __ErrorOnTransmission = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ErrorOnTransmission'), 'ErrorOnTransmission', '__httpeuclid_esa_orgschemaprosim_filterTransmission_httpeuclid_esa_orgschemaprosimErrorOnTransmission', False)

    
    ErrorOnTransmission = property(__ErrorOnTransmission.value, __ErrorOnTransmission.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}CalibrationDataPath uses Python identifier CalibrationDataPath
    __CalibrationDataPath = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath'), 'CalibrationDataPath', '__httpeuclid_esa_orgschemaprosim_filterTransmission_httpeuclid_esa_orgschemaprosimCalibrationDataPath', False)

    
    CalibrationDataPath = property(__CalibrationDataPath.value, __CalibrationDataPath.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}ComputationDate uses Python identifier ComputationDate
    __ComputationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), 'ComputationDate', '__httpeuclid_esa_orgschemaprosim_filterTransmission_httpeuclid_esa_orgschemaprosimComputationDate', False)

    
    ComputationDate = property(__ComputationDate.value, __ComputationDate.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpeuclid_esa_orgschemaprosim_filterTransmission_id', filterTransmissionId, required=True)
    
    id = property(__id.value, __id.set, None, None)


    _ElementMap = {
        __Wavelength.name() : __Wavelength,
        __TransmissionFactor.name() : __TransmissionFactor,
        __Version.name() : __Version,
        __ErrorOnTransmission.name() : __ErrorOnTransmission,
        __CalibrationDataPath.name() : __CalibrationDataPath,
        __ComputationDate.name() : __ComputationDate
    }
    _AttributeMap = {
        __id.name() : __id
    }
Namespace.addCategoryObject('typeBinding', u'filterTransmission', filterTransmission)


# Complex type SEDPoint with content type ELEMENT_ONLY
class SEDPoint (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SEDPoint')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}Flux uses Python identifier Flux
    __Flux = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flux'), 'Flux', '__httpeuclid_esa_orgschemaprosim_SEDPoint_httpeuclid_esa_orgschemaprosimFlux', False)

    
    Flux = property(__Flux.value, __Flux.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), 'Wavelength', '__httpeuclid_esa_orgschemaprosim_SEDPoint_httpeuclid_esa_orgschemaprosimWavelength', False)

    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, None)


    _ElementMap = {
        __Flux.name() : __Flux,
        __Wavelength.name() : __Wavelength
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'SEDPoint', SEDPoint)


# Complex type simulatedDetectorImage with content type ELEMENT_ONLY
class simulatedDetectorImage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'simulatedDetectorImage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}ExposureSequence uses Python identifier ExposureSequence
    __ExposureSequence = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureSequence'), 'ExposureSequence', '__httpeuclid_esa_orgschemaprosim_simulatedDetectorImage_httpeuclid_esa_orgschemaprosimExposureSequence', False)

    
    ExposureSequence = property(__ExposureSequence.value, __ExposureSequence.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}DetectorImagePath uses Python identifier DetectorImagePath
    __DetectorImagePath = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorImagePath'), 'DetectorImagePath', '__httpeuclid_esa_orgschemaprosim_simulatedDetectorImage_httpeuclid_esa_orgschemaprosimDetectorImagePath', False)

    
    DetectorImagePath = property(__DetectorImagePath.value, __DetectorImagePath.set, None, u'Path corresponding to the Simulated Images File.')


    _ElementMap = {
        __ExposureSequence.name() : __ExposureSequence,
        __DetectorImagePath.name() : __DetectorImagePath
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'simulatedDetectorImage', simulatedDetectorImage)


# Complex type emissionLine with content type ELEMENT_ONLY
class emissionLine (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'emissionLine')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemaprosim_emissionLine_httpeuclid_esa_orgschemaprosimName', False)

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}WidthUnit uses Python identifier WidthUnit
    __WidthUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WidthUnit'), 'WidthUnit', '__httpeuclid_esa_orgschemaprosim_emissionLine_httpeuclid_esa_orgschemaprosimWidthUnit', False)

    
    WidthUnit = property(__WidthUnit.value, __WidthUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}FWHM uses Python identifier FWHM
    __FWHM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FWHM'), 'FWHM', '__httpeuclid_esa_orgschemaprosim_emissionLine_httpeuclid_esa_orgschemaprosimFWHM', False)

    
    FWHM = property(__FWHM.value, __FWHM.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}LineFlux uses Python identifier LineFlux
    __LineFlux = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LineFlux'), 'LineFlux', '__httpeuclid_esa_orgschemaprosim_emissionLine_httpeuclid_esa_orgschemaprosimLineFlux', False)

    
    LineFlux = property(__LineFlux.value, __LineFlux.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}FluxUnit uses Python identifier FluxUnit
    __FluxUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FluxUnit'), 'FluxUnit', '__httpeuclid_esa_orgschemaprosim_emissionLine_httpeuclid_esa_orgschemaprosimFluxUnit', False)

    
    FluxUnit = property(__FluxUnit.value, __FluxUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}ObservedWidth uses Python identifier ObservedWidth
    __ObservedWidth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObservedWidth'), 'ObservedWidth', '__httpeuclid_esa_orgschemaprosim_emissionLine_httpeuclid_esa_orgschemaprosimObservedWidth', False)

    
    ObservedWidth = property(__ObservedWidth.value, __ObservedWidth.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}FWHMUnit uses Python identifier FWHMUnit
    __FWHMUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FWHMUnit'), 'FWHMUnit', '__httpeuclid_esa_orgschemaprosim_emissionLine_httpeuclid_esa_orgschemaprosimFWHMUnit', False)

    
    FWHMUnit = property(__FWHMUnit.value, __FWHMUnit.set, None, None)


    _ElementMap = {
        __Name.name() : __Name,
        __WidthUnit.name() : __WidthUnit,
        __FWHM.name() : __FWHM,
        __LineFlux.name() : __LineFlux,
        __FluxUnit.name() : __FluxUnit,
        __ObservedWidth.name() : __ObservedWidth,
        __FWHMUnit.name() : __FWHMUnit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'emissionLine', emissionLine)


# Complex type nipCatalogProduct with content type ELEMENT_ONLY
class nipCatalogProduct (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nipCatalogProduct')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}DataContainer uses Python identifier DataContainer
    __DataContainer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataContainer'), 'DataContainer', '__httpeuclid_esa_orgschemaprosim_nipCatalogProduct_httpeuclid_esa_orgschemaprosimDataContainer', False)

    
    DataContainer = property(__DataContainer.value, __DataContainer.set, None, None)


    _ElementMap = {
        __DataContainer.name() : __DataContainer
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nipCatalogProduct', nipCatalogProduct)


# Complex type nipSimulatedImage with content type ELEMENT_ONLY
class nipSimulatedImage (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nipSimulatedImage')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sim.nipSimulatedImage', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'nipSimulatedImage', nipSimulatedImage)


# Complex type simulationSettings with content type ELEMENT_ONLY
class simulationSettings (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'simulationSettings')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}FPAPointing uses Python identifier FPAPointing
    __FPAPointing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FPAPointing'), 'FPAPointing', '__httpeuclid_esa_orgschemaprosim_simulationSettings_httpeuclid_esa_orgschemaprosimFPAPointing', False)

    
    FPAPointing = property(__FPAPointing.value, __FPAPointing.set, None, u'The Focal Plane Assembly pointing on the sky.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemaprosim_simulationSettings_httpeuclid_esa_orgschemaprosimIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}ExposureTime uses Python identifier ExposureTime
    __ExposureTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime'), 'ExposureTime', '__httpeuclid_esa_orgschemaprosim_simulationSettings_httpeuclid_esa_orgschemaprosimExposureTime', False)

    
    ExposureTime = property(__ExposureTime.value, __ExposureTime.set, None, u'The duration of the exposure of the CCD in seconds.')


    _ElementMap = {
        __FPAPointing.name() : __FPAPointing,
        __Identifier.name() : __Identifier,
        __ExposureTime.name() : __ExposureTime
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'simulationSettings', simulationSettings)


# Complex type visSimulationSettings with content type ELEMENT_ONLY
class visSimulationSettings (simulationSettings):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visSimulationSettings')
    # Base type is simulationSettings
    
    # Element {http://euclid.esa.org/schema/pro/sim}ProcessingSteps uses Python identifier ProcessingSteps
    __ProcessingSteps = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessingSteps'), 'ProcessingSteps', '__httpeuclid_esa_orgschemaprosim_visSimulationSettings_httpeuclid_esa_orgschemaprosimProcessingSteps', False)

    
    ProcessingSteps = property(__ProcessingSteps.value, __ProcessingSteps.set, None, u'Allows to enable/disable the different processing steps which will be applied during the simulation.')

    
    # Element Identifier ({http://euclid.esa.org/schema/pro/sim}Identifier) inherited from {http://euclid.esa.org/schema/pro/sim}simulationSettings
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/sim}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/sim}simulationSettings
    
    # Element FPAPointing ({http://euclid.esa.org/schema/pro/sim}FPAPointing) inherited from {http://euclid.esa.org/schema/pro/sim}simulationSettings

    _ElementMap = simulationSettings._ElementMap.copy()
    _ElementMap.update({
        __ProcessingSteps.name() : __ProcessingSteps
    })
    _AttributeMap = simulationSettings._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'visSimulationSettings', visSimulationSettings)


# Complex type morphologyModel with content type ELEMENT_ONLY
class morphologyModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'morphologyModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}PositionAngleUnit uses Python identifier PositionAngleUnit
    __PositionAngleUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PositionAngleUnit'), 'PositionAngleUnit', '__httpeuclid_esa_orgschemaprosim_morphologyModel_httpeuclid_esa_orgschemaprosimPositionAngleUnit', False)

    
    PositionAngleUnit = property(__PositionAngleUnit.value, __PositionAngleUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}MorphologySED uses Python identifier MorphologySED
    __MorphologySED = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MorphologySED'), 'MorphologySED', '__httpeuclid_esa_orgschemaprosim_morphologyModel_httpeuclid_esa_orgschemaprosimMorphologySED', False)

    
    MorphologySED = property(__MorphologySED.value, __MorphologySED.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Eccentricity uses Python identifier Eccentricity
    __Eccentricity = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Eccentricity'), 'Eccentricity', '__httpeuclid_esa_orgschemaprosim_morphologyModel_httpeuclid_esa_orgschemaprosimEccentricity', False)

    
    Eccentricity = property(__Eccentricity.value, __Eccentricity.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}SersicIndexes uses Python identifier SersicIndexes
    __SersicIndexes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SersicIndexes'), 'SersicIndexes', '__httpeuclid_esa_orgschemaprosim_morphologyModel_httpeuclid_esa_orgschemaprosimSersicIndexes', False)

    
    SersicIndexes = property(__SersicIndexes.value, __SersicIndexes.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}SersicRadiusUnit uses Python identifier SersicRadiusUnit
    __SersicRadiusUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SersicRadiusUnit'), 'SersicRadiusUnit', '__httpeuclid_esa_orgschemaprosim_morphologyModel_httpeuclid_esa_orgschemaprosimSersicRadiusUnit', False)

    
    SersicRadiusUnit = property(__SersicRadiusUnit.value, __SersicRadiusUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}PositionAngle uses Python identifier PositionAngle
    __PositionAngle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PositionAngle'), 'PositionAngle', '__httpeuclid_esa_orgschemaprosim_morphologyModel_httpeuclid_esa_orgschemaprosimPositionAngle', False)

    
    PositionAngle = property(__PositionAngle.value, __PositionAngle.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}SersicRadiuses uses Python identifier SersicRadiuses
    __SersicRadiuses = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SersicRadiuses'), 'SersicRadiuses', '__httpeuclid_esa_orgschemaprosim_morphologyModel_httpeuclid_esa_orgschemaprosimSersicRadiuses', False)

    
    SersicRadiuses = property(__SersicRadiuses.value, __SersicRadiuses.set, None, None)


    _ElementMap = {
        __PositionAngleUnit.name() : __PositionAngleUnit,
        __MorphologySED.name() : __MorphologySED,
        __Eccentricity.name() : __Eccentricity,
        __SersicIndexes.name() : __SersicIndexes,
        __SersicRadiusUnit.name() : __SersicRadiusUnit,
        __PositionAngle.name() : __PositionAngle,
        __SersicRadiuses.name() : __SersicRadiuses
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'morphologyModel', morphologyModel)


# Complex type galaxySourceCatalog with content type ELEMENT_ONLY
class galaxySourceCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'galaxySourceCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), 'CreationDate', '__httpeuclid_esa_orgschemaprosim_galaxySourceCatalog_httpeuclid_esa_orgschemaprosimCreationDate', False)

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}GalaxySources uses Python identifier GalaxySources
    __GalaxySources = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GalaxySources'), 'GalaxySources', '__httpeuclid_esa_orgschemaprosim_galaxySourceCatalog_httpeuclid_esa_orgschemaprosimGalaxySources', True)

    
    GalaxySources = property(__GalaxySources.value, __GalaxySources.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}FilterTransmission uses Python identifier FilterTransmission
    __FilterTransmission = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FilterTransmission'), 'FilterTransmission', '__httpeuclid_esa_orgschemaprosim_galaxySourceCatalog_httpeuclid_esa_orgschemaprosimFilterTransmission', True)

    
    FilterTransmission = property(__FilterTransmission.value, __FilterTransmission.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemaprosim_galaxySourceCatalog_httpeuclid_esa_orgschemaprosimVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpeuclid_esa_orgschemaprosim_galaxySourceCatalog_httpeuclid_esa_orgschemaprosimDescription', False)

    
    Description = property(__Description.value, __Description.set, None, None)


    _ElementMap = {
        __CreationDate.name() : __CreationDate,
        __GalaxySources.name() : __GalaxySources,
        __FilterTransmission.name() : __FilterTransmission,
        __Version.name() : __Version,
        __Description.name() : __Description
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'galaxySourceCatalog', galaxySourceCatalog)


# Complex type simulationInputModels with content type ELEMENT_ONLY
class simulationInputModels (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'simulationInputModels')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}GalaxyAbsorptionInputDataMoodel uses Python identifier GalaxyAbsorptionInputDataMoodel
    __GalaxyAbsorptionInputDataMoodel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GalaxyAbsorptionInputDataMoodel'), 'GalaxyAbsorptionInputDataMoodel', '__httpeuclid_esa_orgschemaprosim_simulationInputModels_httpeuclid_esa_orgschemaprosimGalaxyAbsorptionInputDataMoodel', False)

    
    GalaxyAbsorptionInputDataMoodel = property(__GalaxyAbsorptionInputDataMoodel.value, __GalaxyAbsorptionInputDataMoodel.set, None, u'Reference to Galaxy absorption input data model (refFormat).')

    
    # Element {http://euclid.esa.org/schema/pro/sim}NISPInputDataModel uses Python identifier NISPInputDataModel
    __NISPInputDataModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NISPInputDataModel'), 'NISPInputDataModel', '__httpeuclid_esa_orgschemaprosim_simulationInputModels_httpeuclid_esa_orgschemaprosimNISPInputDataModel', False)

    
    NISPInputDataModel = property(__NISPInputDataModel.value, __NISPInputDataModel.set, None, u'Reference to NISP input data model (refFormat).')

    
    # Element {http://euclid.esa.org/schema/pro/sim}PixelSimulatorConfigurationId uses Python identifier PixelSimulatorConfigurationId
    __PixelSimulatorConfigurationId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PixelSimulatorConfigurationId'), 'PixelSimulatorConfigurationId', '__httpeuclid_esa_orgschemaprosim_simulationInputModels_httpeuclid_esa_orgschemaprosimPixelSimulatorConfigurationId', False)

    
    PixelSimulatorConfigurationId = property(__PixelSimulatorConfigurationId.value, __PixelSimulatorConfigurationId.set, None, u'Reference to Simulator configuration input data model (refFormat)')

    
    # Element {http://euclid.esa.org/schema/pro/sim}TelescopeInputDataModel uses Python identifier TelescopeInputDataModel
    __TelescopeInputDataModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TelescopeInputDataModel'), 'TelescopeInputDataModel', '__httpeuclid_esa_orgschemaprosim_simulationInputModels_httpeuclid_esa_orgschemaprosimTelescopeInputDataModel', False)

    
    TelescopeInputDataModel = property(__TelescopeInputDataModel.value, __TelescopeInputDataModel.set, None, u'Reference to Telescope input data model.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}NISPOpticsInputDataModel uses Python identifier NISPOpticsInputDataModel
    __NISPOpticsInputDataModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NISPOpticsInputDataModel'), 'NISPOpticsInputDataModel', '__httpeuclid_esa_orgschemaprosim_simulationInputModels_httpeuclid_esa_orgschemaprosimNISPOpticsInputDataModel', False)

    
    NISPOpticsInputDataModel = property(__NISPOpticsInputDataModel.value, __NISPOpticsInputDataModel.set, None, u'Reference to NISP optics input data model (refFormat).')

    
    # Element {http://euclid.esa.org/schema/pro/sim}SkyBackgroundInputDataModel uses Python identifier SkyBackgroundInputDataModel
    __SkyBackgroundInputDataModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SkyBackgroundInputDataModel'), 'SkyBackgroundInputDataModel', '__httpeuclid_esa_orgschemaprosim_simulationInputModels_httpeuclid_esa_orgschemaprosimSkyBackgroundInputDataModel', False)

    
    SkyBackgroundInputDataModel = property(__SkyBackgroundInputDataModel.value, __SkyBackgroundInputDataModel.set, None, u'Reference to Sky background input data model (refFormat).')

    
    # Element {http://euclid.esa.org/schema/pro/sim}TelescopeOpticsInputDataModel uses Python identifier TelescopeOpticsInputDataModel
    __TelescopeOpticsInputDataModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TelescopeOpticsInputDataModel'), 'TelescopeOpticsInputDataModel', '__httpeuclid_esa_orgschemaprosim_simulationInputModels_httpeuclid_esa_orgschemaprosimTelescopeOpticsInputDataModel', False)

    
    TelescopeOpticsInputDataModel = property(__TelescopeOpticsInputDataModel.value, __TelescopeOpticsInputDataModel.set, None, u'Reference to Telescope optics input data model (refFormat)')


    _ElementMap = {
        __GalaxyAbsorptionInputDataMoodel.name() : __GalaxyAbsorptionInputDataMoodel,
        __NISPInputDataModel.name() : __NISPInputDataModel,
        __PixelSimulatorConfigurationId.name() : __PixelSimulatorConfigurationId,
        __TelescopeInputDataModel.name() : __TelescopeInputDataModel,
        __NISPOpticsInputDataModel.name() : __NISPOpticsInputDataModel,
        __SkyBackgroundInputDataModel.name() : __SkyBackgroundInputDataModel,
        __TelescopeOpticsInputDataModel.name() : __TelescopeOpticsInputDataModel
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'simulationInputModels', simulationInputModels)


# Complex type nipInputConfiguration with content type ELEMENT_ONLY
class nipInputConfiguration (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nipInputConfiguration')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemaprosim_nipInputConfiguration_httpeuclid_esa_orgschemaprosimIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}SimulationSettings uses Python identifier SimulationSettings
    __SimulationSettings = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SimulationSettings'), 'SimulationSettings', '__httpeuclid_esa_orgschemaprosim_nipInputConfiguration_httpeuclid_esa_orgschemaprosimSimulationSettings', False)

    
    SimulationSettings = property(__SimulationSettings.value, __SimulationSettings.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}FPA uses Python identifier FPA
    __FPA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FPA'), 'FPA', '__httpeuclid_esa_orgschemaprosim_nipInputConfiguration_httpeuclid_esa_orgschemaprosimFPA', False)

    
    FPA = property(__FPA.value, __FPA.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}DetectorList uses Python identifier DetectorList
    __DetectorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), 'DetectorList', '__httpeuclid_esa_orgschemaprosim_nipInputConfiguration_httpeuclid_esa_orgschemaprosimDetectorList', False)

    
    DetectorList = property(__DetectorList.value, __DetectorList.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Catalog uses Python identifier Catalog
    __Catalog = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Catalog'), 'Catalog', '__httpeuclid_esa_orgschemaprosim_nipInputConfiguration_httpeuclid_esa_orgschemaprosimCatalog', False)

    
    Catalog = property(__Catalog.value, __Catalog.set, None, None)


    _ElementMap = {
        __Identifier.name() : __Identifier,
        __SimulationSettings.name() : __SimulationSettings,
        __FPA.name() : __FPA,
        __DetectorList.name() : __DetectorList,
        __Catalog.name() : __Catalog
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nipInputConfiguration', nipInputConfiguration)


# Complex type galaxySource with content type ELEMENT_ONLY
class galaxySource (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'galaxySource')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}EmissionLines uses Python identifier EmissionLines
    __EmissionLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EmissionLines'), 'EmissionLines', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimEmissionLines', True)

    
    EmissionLines = property(__EmissionLines.value, __EmissionLines.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}ObjectType uses Python identifier ObjectType
    __ObjectType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObjectType'), 'ObjectType', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimObjectType', False)

    
    ObjectType = property(__ObjectType.value, __ObjectType.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}MorphologyGeneric uses Python identifier MorphologyGeneric
    __MorphologyGeneric = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MorphologyGeneric'), 'MorphologyGeneric', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimMorphologyGeneric', False)

    
    MorphologyGeneric = property(__MorphologyGeneric.value, __MorphologyGeneric.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}SpectrumStorage uses Python identifier SpectrumStorage
    __SpectrumStorage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpectrumStorage'), 'SpectrumStorage', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimSpectrumStorage', False)

    
    SpectrumStorage = property(__SpectrumStorage.value, __SpectrumStorage.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}RA uses Python identifier RA
    __RA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RA'), 'RA', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimRA', False)

    
    RA = property(__RA.value, __RA.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Magnitude uses Python identifier Magnitude
    __Magnitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Magnitude'), 'Magnitude', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimMagnitude', True)

    
    Magnitude = property(__Magnitude.value, __Magnitude.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Redshift uses Python identifier Redshift
    __Redshift = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Redshift'), 'Redshift', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimRedshift', False)

    
    Redshift = property(__Redshift.value, __Redshift.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}ShapeletModel uses Python identifier ShapeletModel
    __ShapeletModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ShapeletModel'), 'ShapeletModel', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimShapeletModel', False)

    
    ShapeletModel = property(__ShapeletModel.value, __ShapeletModel.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}DEC uses Python identifier DEC
    __DEC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEC'), 'DEC', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimDEC', False)

    
    DEC = property(__DEC.value, __DEC.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}MorphologySersic uses Python identifier MorphologySersic
    __MorphologySersic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MorphologySersic'), 'MorphologySersic', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimMorphologySersic', False)

    
    MorphologySersic = property(__MorphologySersic.value, __MorphologySersic.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}ExpectedRedshift uses Python identifier ExpectedRedshift
    __ExpectedRedshift = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpectedRedshift'), 'ExpectedRedshift', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimExpectedRedshift', False)

    
    ExpectedRedshift = property(__ExpectedRedshift.value, __ExpectedRedshift.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}MorphologyImage uses Python identifier MorphologyImage
    __MorphologyImage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MorphologyImage'), 'MorphologyImage', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimMorphologyImage', False)

    
    MorphologyImage = property(__MorphologyImage.value, __MorphologyImage.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}SED uses Python identifier SED
    __SED = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SED'), 'SED', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimSED', False)

    
    SED = property(__SED.value, __SED.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemaprosim_galaxySource_httpeuclid_esa_orgschemaprosimIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)


    _ElementMap = {
        __EmissionLines.name() : __EmissionLines,
        __ObjectType.name() : __ObjectType,
        __MorphologyGeneric.name() : __MorphologyGeneric,
        __SpectrumStorage.name() : __SpectrumStorage,
        __RA.name() : __RA,
        __Magnitude.name() : __Magnitude,
        __Redshift.name() : __Redshift,
        __ShapeletModel.name() : __ShapeletModel,
        __DEC.name() : __DEC,
        __MorphologySersic.name() : __MorphologySersic,
        __ExpectedRedshift.name() : __ExpectedRedshift,
        __MorphologyImage.name() : __MorphologyImage,
        __SED.name() : __SED,
        __Identifier.name() : __Identifier
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'galaxySource', galaxySource)


# Complex type metadataVISNISPSimulationInterfaces with content type ELEMENT_ONLY
class metadataVISNISPSimulationInterfaces (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'metadataVISNISPSimulationInterfaces')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprosim_metadataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimData', False)

    
    Data = property(__Data.value, __Data.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprosim_metadataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimHeader', False)

    
    Header = property(__Header.value, __Header.set, None, None)


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'metadataVISNISPSimulationInterfaces', metadataVISNISPSimulationInterfaces)


# Complex type fpaPointing with content type ELEMENT_ONLY
class fpaPointing (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fpaPointing')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}Dec uses Python identifier Dec
    __Dec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Dec'), 'Dec', '__httpeuclid_esa_orgschemaprosim_fpaPointing_httpeuclid_esa_orgschemaprosimDec', False)

    
    Dec = property(__Dec.value, __Dec.set, None, u'Declination of the FPA, in degrees.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}Orientation uses Python identifier Orientation
    __Orientation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Orientation'), 'Orientation', '__httpeuclid_esa_orgschemaprosim_fpaPointing_httpeuclid_esa_orgschemaprosimOrientation', False)

    
    Orientation = property(__Orientation.value, __Orientation.set, None, u'Counterclockwise angle from the positive RA axis, in degrees.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}RA uses Python identifier RA
    __RA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RA'), 'RA', '__httpeuclid_esa_orgschemaprosim_fpaPointing_httpeuclid_esa_orgschemaprosimRA', False)

    
    RA = property(__RA.value, __RA.set, None, u'Right ascension of the FPA, in degrees.')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpeuclid_esa_orgschemaprosim_fpaPointing_type', fpaPointingType, required=True)
    
    type = property(__type.value, __type.set, None, u'Specifies the point of the FPA for which the RA, DEC are given for.')


    _ElementMap = {
        __Dec.name() : __Dec,
        __Orientation.name() : __Orientation,
        __RA.name() : __RA
    }
    _AttributeMap = {
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'fpaPointing', fpaPointing)


# Complex type averageQuantumEfficiency with content type SIMPLE
class averageQuantumEfficiency (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = CommonDM.dm.bas.dtd_stub.positiveDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'averageQuantumEfficiency')
    # Base type is CommonDM.dm.bas.dtd_stub.positiveDouble
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpeuclid_esa_orgschemaprosim_averageQuantumEfficiency_type', averageQuantumEfficiencyType, unicode_default=u'Override')
    
    type = property(__type.value, __type.set, None, u'Defines if the average QE will override or normalize the QE maps of the detectors. Defaults to override.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'averageQuantumEfficiency', averageQuantumEfficiency)


# Complex type averageDarkCurrent with content type SIMPLE
class averageDarkCurrent (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = CommonDM.dm.bas.dtd_stub.positiveDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'averageDarkCurrent')
    # Base type is CommonDM.dm.bas.dtd_stub.positiveDouble
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpeuclid_esa_orgschemaprosim_averageDarkCurrent_type', averageDarkCurrentType, unicode_default=u'Override')
    
    type = property(__type.value, __type.set, None, u'Defines if the average dark current will override or normalize the dark current maps of the detectors. Defaults to override.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'averageDarkCurrent', averageDarkCurrent)


# Complex type WeakLensingMap with content type ELEMENT_ONLY
class WeakLensingMap (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WeakLensingMap')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}ShearParameters uses Python identifier ShearParameters
    __ShearParameters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ShearParameters'), 'ShearParameters', '__httpeuclid_esa_orgschemaprosim_WeakLensingMap_httpeuclid_esa_orgschemaprosimShearParameters', True)

    
    ShearParameters = property(__ShearParameters.value, __ShearParameters.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpeuclid_esa_orgschemaprosim_WeakLensingMap_httpeuclid_esa_orgschemaprosimDescription', False)

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemaprosim_WeakLensingMap_httpeuclid_esa_orgschemaprosimVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)


    _ElementMap = {
        __ShearParameters.name() : __ShearParameters,
        __Description.name() : __Description,
        __Version.name() : __Version
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'WeakLensingMap', WeakLensingMap)


# Complex type shearParameter with content type ELEMENT_ONLY
class shearParameter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shearParameter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}g2 uses Python identifier g2
    __g2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'g2'), 'g2', '__httpeuclid_esa_orgschemaprosim_shearParameter_httpeuclid_esa_orgschemaprosimg2', False)

    
    g2 = property(__g2.value, __g2.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}RAUnit uses Python identifier RAUnit
    __RAUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RAUnit'), 'RAUnit', '__httpeuclid_esa_orgschemaprosim_shearParameter_httpeuclid_esa_orgschemaprosimRAUnit', False)

    
    RAUnit = property(__RAUnit.value, __RAUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}g1 uses Python identifier g1
    __g1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'g1'), 'g1', '__httpeuclid_esa_orgschemaprosim_shearParameter_httpeuclid_esa_orgschemaprosimg1', False)

    
    g1 = property(__g1.value, __g1.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}DECUnit uses Python identifier DECUnit
    __DECUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DECUnit'), 'DECUnit', '__httpeuclid_esa_orgschemaprosim_shearParameter_httpeuclid_esa_orgschemaprosimDECUnit', False)

    
    DECUnit = property(__DECUnit.value, __DECUnit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}RA uses Python identifier RA
    __RA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RA'), 'RA', '__httpeuclid_esa_orgschemaprosim_shearParameter_httpeuclid_esa_orgschemaprosimRA', False)

    
    RA = property(__RA.value, __RA.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}DEC uses Python identifier DEC
    __DEC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DEC'), 'DEC', '__httpeuclid_esa_orgschemaprosim_shearParameter_httpeuclid_esa_orgschemaprosimDEC', False)

    
    DEC = property(__DEC.value, __DEC.set, None, None)


    _ElementMap = {
        __g2.name() : __g2,
        __RAUnit.name() : __RAUnit,
        __g1.name() : __g1,
        __DECUnit.name() : __DECUnit,
        __RA.name() : __RA,
        __DEC.name() : __DEC
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'shearParameter', shearParameter)


# Complex type nipSimulationSettings with content type ELEMENT_ONLY
class nipSimulationSettings (simulationSettings):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nipSimulationSettings')
    # Base type is simulationSettings
    
    # Element {http://euclid.esa.org/schema/pro/sim}FilterName uses Python identifier FilterName
    __FilterName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FilterName'), 'FilterName', '__httpeuclid_esa_orgschemaprosim_nipSimulationSettings_httpeuclid_esa_orgschemaprosimFilterName', False)

    
    FilterName = property(__FilterName.value, __FilterName.set, None, u'The name of the filter to simulate.')

    
    # Element Identifier ({http://euclid.esa.org/schema/pro/sim}Identifier) inherited from {http://euclid.esa.org/schema/pro/sim}simulationSettings
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/sim}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/sim}simulationSettings
    
    # Element FPAPointing ({http://euclid.esa.org/schema/pro/sim}FPAPointing) inherited from {http://euclid.esa.org/schema/pro/sim}simulationSettings

    _ElementMap = simulationSettings._ElementMap.copy()
    _ElementMap.update({
        __FilterName.name() : __FilterName
    })
    _AttributeMap = simulationSettings._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'nipSimulationSettings', nipSimulationSettings)


# Complex type tipsInputConfiguration with content type ELEMENT_ONLY
class tipsInputConfiguration (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'tipsInputConfiguration')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}SimulationSettings uses Python identifier SimulationSettings
    __SimulationSettings = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SimulationSettings'), 'SimulationSettings', '__httpeuclid_esa_orgschemaprosim_tipsInputConfiguration_httpeuclid_esa_orgschemaprosimSimulationSettings', False)

    
    SimulationSettings = property(__SimulationSettings.value, __SimulationSettings.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}OpticsModel uses Python identifier OpticsModel
    __OpticsModel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OpticsModel'), 'OpticsModel', '__httpeuclid_esa_orgschemaprosim_tipsInputConfiguration_httpeuclid_esa_orgschemaprosimOpticsModel', False)

    
    OpticsModel = property(__OpticsModel.value, __OpticsModel.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Catalog uses Python identifier Catalog
    __Catalog = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Catalog'), 'Catalog', '__httpeuclid_esa_orgschemaprosim_tipsInputConfiguration_httpeuclid_esa_orgschemaprosimCatalog', False)

    
    Catalog = property(__Catalog.value, __Catalog.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}DetectorList uses Python identifier DetectorList
    __DetectorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), 'DetectorList', '__httpeuclid_esa_orgschemaprosim_tipsInputConfiguration_httpeuclid_esa_orgschemaprosimDetectorList', False)

    
    DetectorList = property(__DetectorList.value, __DetectorList.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}FPA uses Python identifier FPA
    __FPA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FPA'), 'FPA', '__httpeuclid_esa_orgschemaprosim_tipsInputConfiguration_httpeuclid_esa_orgschemaprosimFPA', False)

    
    FPA = property(__FPA.value, __FPA.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemaprosim_tipsInputConfiguration_httpeuclid_esa_orgschemaprosimIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)


    _ElementMap = {
        __SimulationSettings.name() : __SimulationSettings,
        __OpticsModel.name() : __OpticsModel,
        __Catalog.name() : __Catalog,
        __DetectorList.name() : __DetectorList,
        __FPA.name() : __FPA,
        __Identifier.name() : __Identifier
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'tipsInputConfiguration', tipsInputConfiguration)


# Complex type nipOutput with content type ELEMENT_ONLY
class nipOutput (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nipOutput')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}SimulatedDetectorImage uses Python identifier SimulatedDetectorImage
    __SimulatedDetectorImage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SimulatedDetectorImage'), 'SimulatedDetectorImage', '__httpeuclid_esa_orgschemaprosim_nipOutput_httpeuclid_esa_orgschemaprosimSimulatedDetectorImage', True)

    
    SimulatedDetectorImage = property(__SimulatedDetectorImage.value, __SimulatedDetectorImage.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}InputConfigurationId uses Python identifier InputConfigurationId
    __InputConfigurationId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InputConfigurationId'), 'InputConfigurationId', '__httpeuclid_esa_orgschemaprosim_nipOutput_httpeuclid_esa_orgschemaprosimInputConfigurationId', False)

    
    InputConfigurationId = property(__InputConfigurationId.value, __InputConfigurationId.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpeuclid_esa_orgschemaprosim_nipOutput_httpeuclid_esa_orgschemaprosimIdentifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)


    _ElementMap = {
        __SimulatedDetectorImage.name() : __SimulatedDetectorImage,
        __InputConfigurationId.name() : __InputConfigurationId,
        __Identifier.name() : __Identifier
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nipOutput', nipOutput)


# Complex type dataVISNISPSimulationInterfaces with content type ELEMENT_ONLY
class dataVISNISPSimulationInterfaces (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataVISNISPSimulationInterfaces')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}SimulationInputModels uses Python identifier SimulationInputModels
    __SimulationInputModels = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SimulationInputModels'), 'SimulationInputModels', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimSimulationInputModels', False)

    
    SimulationInputModels = property(__SimulationInputModels.value, __SimulationInputModels.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}ListOfImageSequenceSimulated uses Python identifier ListOfImageSequenceSimulated
    __ListOfImageSequenceSimulated = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ListOfImageSequenceSimulated'), 'ListOfImageSequenceSimulated', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimListOfImageSequenceSimulated', False)

    
    ListOfImageSequenceSimulated = property(__ListOfImageSequenceSimulated.value, __ListOfImageSequenceSimulated.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}FPADetectorList uses Python identifier FPADetectorList
    __FPADetectorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FPADetectorList'), 'FPADetectorList', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimFPADetectorList', False)

    
    FPADetectorList = property(__FPADetectorList.value, __FPADetectorList.set, None, u'List of detector identifiers simulated.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}PixelSimulatorName uses Python identifier PixelSimulatorName
    __PixelSimulatorName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PixelSimulatorName'), 'PixelSimulatorName', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimPixelSimulatorName', False)

    
    PixelSimulatorName = property(__PixelSimulatorName.value, __PixelSimulatorName.set, None, u'Different codes of simulation could be used for different objects. Please refere here the name of the Simulator SW code.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}ObservationMode uses Python identifier ObservationMode
    __ObservationMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode'), 'ObservationMode', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimObservationMode', False)

    
    ObservationMode = property(__ObservationMode.value, __ObservationMode.set, None, u'refer to observation Mode used for the simulation runtime : calibration, wide or deep.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}TelescopePointingDec uses Python identifier TelescopePointingDec
    __TelescopePointingDec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TelescopePointingDec'), 'TelescopePointingDec', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimTelescopePointingDec', False)

    
    TelescopePointingDec = property(__TelescopePointingDec.value, __TelescopePointingDec.set, None, u'Declinaison of the pointing angles of the telescope in the center of the field.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}NumberOfSimulatedDetectors uses Python identifier NumberOfSimulatedDetectors
    __NumberOfSimulatedDetectors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumberOfSimulatedDetectors'), 'NumberOfSimulatedDetectors', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimNumberOfSimulatedDetectors', False)

    
    NumberOfSimulatedDetectors = property(__NumberOfSimulatedDetectors.value, __NumberOfSimulatedDetectors.set, None, u'Number of simulated detectors corresponding to the cardinality of FPADetectorList.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}PixelSimulatorVersion uses Python identifier PixelSimulatorVersion
    __PixelSimulatorVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PixelSimulatorVersion'), 'PixelSimulatorVersion', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimPixelSimulatorVersion', False)

    
    PixelSimulatorVersion = property(__PixelSimulatorVersion.value, __PixelSimulatorVersion.set, None, u'Refer here to the version of the SW simulator code.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}ObservationDate uses Python identifier ObservationDate
    __ObservationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate'), 'ObservationDate', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimObservationDate', False)

    
    ObservationDate = property(__ObservationDate.value, __ObservationDate.set, None, u'refer to observation date of the image.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}GrismOrderSimulation uses Python identifier GrismOrderSimulation
    __GrismOrderSimulation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GrismOrderSimulation'), 'GrismOrderSimulation', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimGrismOrderSimulation', False)

    
    GrismOrderSimulation = property(__GrismOrderSimulation.value, __GrismOrderSimulation.set, None, u'Order of the grism simulation image inside the fits file.')

    
    # Element {http://euclid.esa.org/schema/pro/sim}TelescopePointingRA uses Python identifier TelescopePointingRA
    __TelescopePointingRA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TelescopePointingRA'), 'TelescopePointingRA', '__httpeuclid_esa_orgschemaprosim_dataVISNISPSimulationInterfaces_httpeuclid_esa_orgschemaprosimTelescopePointingRA', False)

    
    TelescopePointingRA = property(__TelescopePointingRA.value, __TelescopePointingRA.set, None, u'Right Ascension of the pointing angles of the telescope in the center of the field.')


    _ElementMap = {
        __SimulationInputModels.name() : __SimulationInputModels,
        __ListOfImageSequenceSimulated.name() : __ListOfImageSequenceSimulated,
        __FPADetectorList.name() : __FPADetectorList,
        __PixelSimulatorName.name() : __PixelSimulatorName,
        __ObservationMode.name() : __ObservationMode,
        __TelescopePointingDec.name() : __TelescopePointingDec,
        __NumberOfSimulatedDetectors.name() : __NumberOfSimulatedDetectors,
        __PixelSimulatorVersion.name() : __PixelSimulatorVersion,
        __ObservationDate.name() : __ObservationDate,
        __GrismOrderSimulation.name() : __GrismOrderSimulation,
        __TelescopePointingRA.name() : __TelescopePointingRA
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'dataVISNISPSimulationInterfaces', dataVISNISPSimulationInterfaces)


# Complex type catalogFitsFile with content type ELEMENT_ONLY
class catalogFitsFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogFitsFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sim.catalog', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'catalogFitsFile', catalogFitsFile)


# Complex type tipsSimulationSettings with content type ELEMENT_ONLY
class tipsSimulationSettings (simulationSettings):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'tipsSimulationSettings')
    # Base type is simulationSettings
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/sim}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/sim}simulationSettings
    
    # Element FPAPointing ({http://euclid.esa.org/schema/pro/sim}FPAPointing) inherited from {http://euclid.esa.org/schema/pro/sim}simulationSettings
    
    # Element {http://euclid.esa.org/schema/pro/sim}SimulatedGrismOrderList uses Python identifier SimulatedGrismOrderList
    __SimulatedGrismOrderList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SimulatedGrismOrderList'), 'SimulatedGrismOrderList', '__httpeuclid_esa_orgschemaprosim_tipsSimulationSettings_httpeuclid_esa_orgschemaprosimSimulatedGrismOrderList', False)

    
    SimulatedGrismOrderList = property(__SimulatedGrismOrderList.value, __SimulatedGrismOrderList.set, None, None)

    
    # Element Identifier ({http://euclid.esa.org/schema/pro/sim}Identifier) inherited from {http://euclid.esa.org/schema/pro/sim}simulationSettings

    _ElementMap = simulationSettings._ElementMap.copy()
    _ElementMap.update({
        __SimulatedGrismOrderList.name() : __SimulatedGrismOrderList
    })
    _AttributeMap = simulationSettings._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'tipsSimulationSettings', tipsSimulationSettings)


# Complex type catalogProduct with content type ELEMENT_ONLY
class catalogProduct (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'catalogProduct')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sim}SpectraFitsFile uses Python identifier SpectraFitsFile
    __SpectraFitsFile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpectraFitsFile'), 'SpectraFitsFile', '__httpeuclid_esa_orgschemaprosim_catalogProduct_httpeuclid_esa_orgschemaprosimSpectraFitsFile', False)

    
    SpectraFitsFile = property(__SpectraFitsFile.value, __SpectraFitsFile.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sim}CatalogFitsFile uses Python identifier CatalogFitsFile
    __CatalogFitsFile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CatalogFitsFile'), 'CatalogFitsFile', '__httpeuclid_esa_orgschemaprosim_catalogProduct_httpeuclid_esa_orgschemaprosimCatalogFitsFile', False)

    
    CatalogFitsFile = property(__CatalogFitsFile.value, __CatalogFitsFile.set, None, None)


    _ElementMap = {
        __SpectraFitsFile.name() : __SpectraFitsFile,
        __CatalogFitsFile.name() : __CatalogFitsFile
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'catalogProduct', catalogProduct)


# Complex type visProcessingSteps with content type EMPTY
class visProcessingSteps (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visProcessingSteps')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute darkCurrent uses Python identifier darkCurrent
    __darkCurrent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'darkCurrent'), 'darkCurrent', '__httpeuclid_esa_orgschemaprosim_visProcessingSteps_darkCurrent', pyxb.binding.datatypes.boolean)
    
    darkCurrent = property(__darkCurrent.value, __darkCurrent.set, None, u'Apply or not the dark current.')

    
    # Attribute readoutNoise uses Python identifier readoutNoise
    __readoutNoise = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'readoutNoise'), 'readoutNoise', '__httpeuclid_esa_orgschemaprosim_visProcessingSteps_readoutNoise', pyxb.binding.datatypes.boolean)
    
    readoutNoise = property(__readoutNoise.value, __readoutNoise.set, None, u'Apply or not the readout noise.')

    
    # Attribute flatField uses Python identifier flatField
    __flatField = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'flatField'), 'flatField', '__httpeuclid_esa_orgschemaprosim_visProcessingSteps_flatField', pyxb.binding.datatypes.boolean)
    
    flatField = property(__flatField.value, __flatField.set, None, u'Apply or not the flat field.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __darkCurrent.name() : __darkCurrent,
        __readoutNoise.name() : __readoutNoise,
        __flatField.name() : __flatField
    }
Namespace.addCategoryObject('typeBinding', u'visProcessingSteps', visProcessingSteps)


# Complex type spectrumFile with content type ELEMENT_ONLY
class spectrumFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrumFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sim.spectrum', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'spectrumFile', spectrumFile)




spectrumProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpectedPhotometricRedshift'), pyxb.binding.datatypes.double, scope=spectrumProperties, documentation=u'The expected photometric redshift of the object.'))

spectrumProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmissionLineList'), emissionLineList, scope=spectrumProperties, documentation=u'A list with all the available emission lines of the object.'))

spectrumProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Redshift'), pyxb.binding.datatypes.double, scope=spectrumProperties, documentation=u'The redshift of the object.'))
spectrumProperties._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrumProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Redshift')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpectedPhotometricRedshift')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EmissionLineList')), min_occurs=1, max_occurs=1)
    )
spectrumProperties._ContentModel = pyxb.binding.content.ParticleModel(spectrumProperties._GroupModel, min_occurs=1, max_occurs=1)



SED._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WavelengthUnit'), CommonDM.dm.bas.utd_stub.unit, scope=SED))

SED._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FluxUnit'), CommonDM.dm.bas.utd_stub.unit, scope=SED))

SED._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogName'), pyxb.binding.datatypes.string, scope=SED))

SED._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SED'), SEDPoint, scope=SED))
SED._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SED._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SED._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WavelengthUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SED._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FluxUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SED._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SED')), min_occurs=0L, max_occurs=None)
    )
SED._ContentModel = pyxb.binding.content.ParticleModel(SED._GroupModel, min_occurs=1, max_occurs=1)



emissionLineList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmissionLine'), emissionLine, scope=emissionLineList))
emissionLineList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(emissionLineList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EmissionLine')), min_occurs=0L, max_occurs=None)
    )
emissionLineList._ContentModel = pyxb.binding.content.ParticleModel(emissionLineList._GroupModel, min_occurs=1, max_occurs=1)



simFocalPlaneArangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Pixelsize_um'), pyxb.binding.datatypes.double, scope=simFocalPlaneArangement, documentation=u'Mean pixel size for simulation purposes in microns.'))

simFocalPlaneArangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AverageDarkCurrent'), averageDarkCurrent, scope=simFocalPlaneArangement, documentation=u'The average dark current (expressed in electrons/s/pix), to be used for all the pixels of all the detectors. This value is ment for simulation reasons only and, when present, will either override or normalize the more detailed readout noise models of the detectors (depending on its type attribute).'))

simFocalPlaneArangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AverageQuantumEfficiency'), averageQuantumEfficiency, scope=simFocalPlaneArangement, documentation=u'The average quantum efficiency (expressed in electrons/photons), to be used for all the pixels of all the detectors. This value is ment for simulation reasons only and, when present, will either override or normalize the more detailed QE models of the detectors (depending on its type attribute).'))

simFocalPlaneArangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Pixelsize'), pyxb.binding.datatypes.double, scope=simFocalPlaneArangement, documentation=u'Mean pixel size for simulation purposes in arcsec.'))

simFocalPlaneArangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorGapInX'), CommonDM.dm.bas.dtd_stub.positiveDouble, scope=simFocalPlaneArangement, documentation=u'The gap between adjacent detectors in the horizontal (X) direction, expressed in um. Inacive pixel margins are included. This value is ment for simulation reasons only and, when present, will override the per detector gap information from the FPA DetectorPositionList (only row/column information will be used).'))

simFocalPlaneArangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AverageReadoutNoise'), averageReadoutNoise, scope=simFocalPlaneArangement, documentation=u'The average readout noise (expressed in electrons/pix), to be used for all the pixels of all the detectors. This value is ment for simulation reasons only and, when present, will either override or normalize the more detailed readout noise models of the detectors (depending on its type attribute).'))

simFocalPlaneArangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorGapInY'), CommonDM.dm.bas.dtd_stub.positiveDouble, scope=simFocalPlaneArangement, documentation=u'The gap between adjacent detectors in the vertical (Y) direction, expressed in um. Inacive pixel margins are included. This value is ment for simulation reasons only and, when present, will override the per detector gap information from the FPA DetectorPositionList (only row/column information will be used).'))
simFocalPlaneArangement._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/ins/nis'), u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/ins/nis'), u'NumberOfRows')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/ins/nis'), u'NumberOfColumns')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/ins/nis'), u'DetectorPositionList')), min_occurs=1, max_occurs=1)
    )
simFocalPlaneArangement._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorGapInX')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorGapInY')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AverageQuantumEfficiency')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AverageReadoutNoise')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AverageDarkCurrent')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Pixelsize')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Pixelsize_um')), min_occurs=1, max_occurs=1)
    )
simFocalPlaneArangement._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simFocalPlaneArangement._GroupModel_2, min_occurs=1, max_occurs=1)
    )
simFocalPlaneArangement._ContentModel = pyxb.binding.content.ParticleModel(simFocalPlaneArangement._GroupModel, min_occurs=1, max_occurs=1)



setOfSimulatedImages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimulatedDetectorImage'), simulatedDetectorImage, scope=setOfSimulatedImages))
setOfSimulatedImages._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(setOfSimulatedImages._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SimulatedDetectorImage')), min_occurs=1, max_occurs=None)
    )
setOfSimulatedImages._ContentModel = pyxb.binding.content.ParticleModel(setOfSimulatedImages._GroupModel, min_occurs=1, max_occurs=1)



detectorList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Detector'), CommonDM.dm.ins.nis_stub.detector, scope=detectorList))
detectorList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(detectorList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Detector')), min_occurs=1, max_occurs=None)
    )
detectorList._ContentModel = pyxb.binding.content.ParticleModel(detectorList._GroupModel, min_occurs=1, max_occurs=1)



visInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), detectorList, scope=visInputConfiguration))

visInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=visInputConfiguration))

visInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FPA'), simFocalPlaneArangement, scope=visInputConfiguration))

visInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimulationSettings'), visSimulationSettings, scope=visInputConfiguration))
visInputConfiguration._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SimulationSettings')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorList')), min_occurs=1, max_occurs=1)
    )
visInputConfiguration._ContentModel = pyxb.binding.content.ParticleModel(visInputConfiguration._GroupModel, min_occurs=1, max_occurs=1)



mirroring._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Y'), pyxb.binding.datatypes.boolean, scope=mirroring))

mirroring._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'X'), pyxb.binding.datatypes.boolean, scope=mirroring))
mirroring._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(mirroring._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'X')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(mirroring._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Y')), min_occurs=1, max_occurs=1)
    )
mirroring._ContentModel = pyxb.binding.content.ParticleModel(mirroring._GroupModel, min_occurs=1, max_occurs=1)



wavelengthRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WavelengthMax'), pyxb.binding.datatypes.double, scope=wavelengthRange))

wavelengthRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WavelenthUnit'), CommonDM.dm.bas.utd_stub.unit, scope=wavelengthRange))

wavelengthRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WavelengthMin'), pyxb.binding.datatypes.double, scope=wavelengthRange))
wavelengthRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(wavelengthRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WavelenthUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(wavelengthRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WavelengthMin')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(wavelengthRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WavelengthMax')), min_occurs=1, max_occurs=1)
    )
wavelengthRange._ContentModel = pyxb.binding.content.ParticleModel(wavelengthRange._GroupModel, min_occurs=1, max_occurs=1)



morphologyImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SurveyName'), pyxb.binding.datatypes.string, scope=morphologyImage))

morphologyImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Mirroring'), mirroring, scope=morphologyImage))

morphologyImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WavelengthRange'), wavelengthRange, scope=morphologyImage))

morphologyImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PositionAngle'), pyxb.binding.datatypes.double, scope=morphologyImage))

morphologyImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Scaling'), pyxb.binding.datatypes.double, scope=morphologyImage))

morphologyImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PositionAngleUnit'), CommonDM.dm.bas.utd_stub.unit, scope=morphologyImage))

morphologyImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataContainer'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=morphologyImage))
morphologyImage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(morphologyImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SurveyName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Mirroring')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionAngle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionAngleUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Scaling')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WavelengthRange')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
morphologyImage._ContentModel = pyxb.binding.content.ParticleModel(morphologyImage._GroupModel, min_occurs=1, max_occurs=1)


spectraFitsFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectraFitsFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
spectraFitsFile._ContentModel = pyxb.binding.content.ParticleModel(spectraFitsFile._GroupModel, min_occurs=1, max_occurs=1)



magnitude._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filter'), filterTransmissionId, scope=magnitude))

magnitude._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Error'), pyxb.binding.datatypes.double, scope=magnitude))

magnitude._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagType'), pyxb.binding.datatypes.string, scope=magnitude))

magnitude._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.double, scope=magnitude))
magnitude._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(magnitude._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(magnitude._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(magnitude._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Error')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(magnitude._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filter')), min_occurs=1, max_occurs=1)
    )
magnitude._ContentModel = pyxb.binding.content.ParticleModel(magnitude._GroupModel, min_occurs=1, max_occurs=1)


simulatedImageFitsFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(simulatedImageFitsFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
simulatedImageFitsFile._ContentModel = pyxb.binding.content.ParticleModel(simulatedImageFitsFile._GroupModel, min_occurs=1, max_occurs=1)



simulatedExposureSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureDate'), pyxb.binding.datatypes.dateTime, scope=simulatedExposureSequence, documentation=u'Refers to the Exposure Date expressed with the resolution of ms.'))

simulatedExposureSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FPAPointingRA'), CommonDM.dm.bas.dtd_stub.degAngle, scope=simulatedExposureSequence, documentation=u'Right Ascension of the pointing angles of the FPA via the telescope in the Bottom Left of the detector.'))

simulatedExposureSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FPAPointingDec'), CommonDM.dm.bas.dtd_stub.degAngle, scope=simulatedExposureSequence, documentation=u'Declinaison of the pointing angles of the FPA via the telescope in the Bottom Left of the detector.'))

simulatedExposureSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime'), CommonDM.dm.ins.nis_stub.exposureTime, scope=simulatedExposureSequence, documentation=u'Refers to the duration of Exposure expressed in seconds with the resolution of the us'))

simulatedExposureSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SelectedGrism'), CommonDM.dm.ins.nis_stub.grismName, scope=simulatedExposureSequence, documentation=u'Refers to the Grism mode selected : GBlue or Gred and polar angle 0 or 90'))
simulatedExposureSequence._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(simulatedExposureSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulatedExposureSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulatedExposureSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SelectedGrism')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulatedExposureSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPAPointingRA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulatedExposureSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPAPointingDec')), min_occurs=1, max_occurs=1)
    )
simulatedExposureSequence._ContentModel = pyxb.binding.content.ParticleModel(simulatedExposureSequence._GroupModel, min_occurs=1, max_occurs=1)



shapeletModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Type'), shapeletType, scope=shapeletModel))

shapeletModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'M'), pyxb.binding.datatypes.integer, scope=shapeletModel))

shapeletModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'N'), pyxb.binding.datatypes.integer, scope=shapeletModel))

shapeletModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Scale'), pyxb.binding.datatypes.double, scope=shapeletModel))

shapeletModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), CommonDM.dm.bas.dtd_stub.listOfDouble, scope=shapeletModel, documentation=u'Coefficients of shapelets as NxM matrix'))
shapeletModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(shapeletModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Type')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shapeletModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Scale')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shapeletModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coefficients')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(shapeletModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'N')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shapeletModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'M')), min_occurs=1, max_occurs=1)
    )
shapeletModel._ContentModel = pyxb.binding.content.ParticleModel(shapeletModel._GroupModel, min_occurs=1, max_occurs=1)



morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinorAxisUnit'), CommonDM.dm.bas.utd_stub.unit, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinorAxis'), pyxb.binding.datatypes.double, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BuldgeToTotal'), pyxb.binding.datatypes.double, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PositionAngle'), pyxb.binding.datatypes.double, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DiskHalfRadius'), pyxb.binding.datatypes.double, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PositionAngleUnit'), CommonDM.dm.bas.utd_stub.unit, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AxisRatio'), pyxb.binding.datatypes.double, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DiskHalfRadiusUnit'), CommonDM.dm.bas.utd_stub.unit, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MajorAxisUnit'), CommonDM.dm.bas.utd_stub.unit, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BuldgeHalfRadius'), pyxb.binding.datatypes.double, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MorphologicalType'), pyxb.binding.datatypes.integer, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MajorAxis'), pyxb.binding.datatypes.double, scope=morphologyGeneric))

morphologyGeneric._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BuldgeHalfRadiusUnit'), CommonDM.dm.bas.utd_stub.unit, scope=morphologyGeneric))
morphologyGeneric._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MajorAxis')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinorAxis')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MajorAxisUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinorAxisUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionAngle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionAngleUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MorphologicalType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DiskHalfRadius')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BuldgeHalfRadius')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DiskHalfRadiusUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BuldgeHalfRadiusUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BuldgeToTotal')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyGeneric._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AxisRatio')), min_occurs=1, max_occurs=1)
    )
morphologyGeneric._ContentModel = pyxb.binding.content.ParticleModel(morphologyGeneric._GroupModel, min_occurs=1, max_occurs=1)



filterTransmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), CommonDM.dm.ins_stub.wavelength, scope=filterTransmission))

filterTransmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransmissionFactor'), CommonDM.dm.ins_stub.transmissionFactor, scope=filterTransmission))

filterTransmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), pyxb.binding.datatypes.double, scope=filterTransmission))

filterTransmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ErrorOnTransmission'), CommonDM.dm.ins_stub.errorOnTransmission, scope=filterTransmission))

filterTransmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=filterTransmission))

filterTransmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), pyxb.binding.datatypes.dateTime, scope=filterTransmission))
filterTransmission._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(filterTransmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filterTransmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filterTransmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filterTransmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Wavelength')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filterTransmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TransmissionFactor')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(filterTransmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ErrorOnTransmission')), min_occurs=1, max_occurs=1)
    )
filterTransmission._ContentModel = pyxb.binding.content.ParticleModel(filterTransmission._GroupModel, min_occurs=1, max_occurs=1)



SEDPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flux'), pyxb.binding.datatypes.double, scope=SEDPoint))

SEDPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), pyxb.binding.datatypes.double, scope=SEDPoint))
SEDPoint._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SEDPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Wavelength')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SEDPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flux')), min_occurs=1, max_occurs=1)
    )
SEDPoint._ContentModel = pyxb.binding.content.ParticleModel(SEDPoint._GroupModel, min_occurs=1, max_occurs=1)



simulatedDetectorImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureSequence'), simulatedExposureSequence, scope=simulatedDetectorImage))

simulatedDetectorImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorImagePath'), simulatedImageFitsFile, scope=simulatedDetectorImage, documentation=u'Path corresponding to the Simulated Images File.'))
simulatedDetectorImage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(simulatedDetectorImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorImagePath')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulatedDetectorImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureSequence')), min_occurs=1, max_occurs=1)
    )
simulatedDetectorImage._ContentModel = pyxb.binding.content.ParticleModel(simulatedDetectorImage._GroupModel, min_occurs=1, max_occurs=1)



emissionLine._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.double, scope=emissionLine))

emissionLine._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WidthUnit'), CommonDM.dm.bas.utd_stub.unit, scope=emissionLine))

emissionLine._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FWHM'), pyxb.binding.datatypes.double, scope=emissionLine))

emissionLine._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LineFlux'), pyxb.binding.datatypes.double, scope=emissionLine))

emissionLine._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FluxUnit'), CommonDM.dm.bas.utd_stub.unit, scope=emissionLine))

emissionLine._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservedWidth'), pyxb.binding.datatypes.double, scope=emissionLine))

emissionLine._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FWHMUnit'), CommonDM.dm.bas.utd_stub.unit, scope=emissionLine))
emissionLine._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(emissionLine._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(emissionLine._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LineFlux')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(emissionLine._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FluxUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(emissionLine._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservedWidth')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(emissionLine._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WidthUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(emissionLine._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FWHM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(emissionLine._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FWHMUnit')), min_occurs=1, max_occurs=1)
    )
emissionLine._ContentModel = pyxb.binding.content.ParticleModel(emissionLine._GroupModel, min_occurs=1, max_occurs=1)



nipCatalogProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataContainer'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=nipCatalogProduct))
nipCatalogProduct._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nipCatalogProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
nipCatalogProduct._ContentModel = pyxb.binding.content.ParticleModel(nipCatalogProduct._GroupModel, min_occurs=1, max_occurs=1)


nipSimulatedImage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nipSimulatedImage._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
nipSimulatedImage._ContentModel = pyxb.binding.content.ParticleModel(nipSimulatedImage._GroupModel, min_occurs=1, max_occurs=1)



simulationSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FPAPointing'), fpaPointing, scope=simulationSettings, documentation=u'The Focal Plane Assembly pointing on the sky.'))

simulationSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=simulationSettings))

simulationSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime'), CommonDM.dm.ins.nis_stub.exposureTime, scope=simulationSettings, documentation=u'The duration of the exposure of the CCD in seconds.'))
simulationSettings._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(simulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPAPointing')), min_occurs=1, max_occurs=1)
    )
simulationSettings._ContentModel = pyxb.binding.content.ParticleModel(simulationSettings._GroupModel, min_occurs=1, max_occurs=1)



visSimulationSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessingSteps'), visProcessingSteps, scope=visSimulationSettings, documentation=u'Allows to enable/disable the different processing steps which will be applied during the simulation.'))
visSimulationSettings._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPAPointing')), min_occurs=1, max_occurs=1)
    )
visSimulationSettings._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessingSteps')), min_occurs=1, max_occurs=1)
    )
visSimulationSettings._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visSimulationSettings._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visSimulationSettings._GroupModel_2, min_occurs=1, max_occurs=1)
    )
visSimulationSettings._ContentModel = pyxb.binding.content.ParticleModel(visSimulationSettings._GroupModel, min_occurs=1, max_occurs=1)



morphologyModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PositionAngleUnit'), CommonDM.dm.bas.utd_stub.unit, scope=morphologyModel))

morphologyModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MorphologySED'), SED, scope=morphologyModel))

morphologyModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Eccentricity'), pyxb.binding.datatypes.double, scope=morphologyModel))

morphologyModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SersicIndexes'), CommonDM.dm.bas.dtd_stub.listOfDouble, scope=morphologyModel))

morphologyModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SersicRadiusUnit'), CommonDM.dm.bas.utd_stub.unit, scope=morphologyModel))

morphologyModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PositionAngle'), pyxb.binding.datatypes.double, scope=morphologyModel))

morphologyModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SersicRadiuses'), CommonDM.dm.bas.dtd_stub.listOfDouble, scope=morphologyModel))
morphologyModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(morphologyModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SersicRadiuses')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SersicRadiusUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SersicIndexes')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionAngle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionAngleUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Eccentricity')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(morphologyModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MorphologySED')), min_occurs=1, max_occurs=1)
    )
morphologyModel._ContentModel = pyxb.binding.content.ParticleModel(morphologyModel._GroupModel, min_occurs=1, max_occurs=1)



galaxySourceCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), pyxb.binding.datatypes.dateTime, scope=galaxySourceCatalog))

galaxySourceCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GalaxySources'), galaxySource, scope=galaxySourceCatalog))

galaxySourceCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FilterTransmission'), filterTransmission, scope=galaxySourceCatalog))

galaxySourceCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), pyxb.binding.datatypes.string, scope=galaxySourceCatalog))

galaxySourceCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), pyxb.binding.datatypes.string, scope=galaxySourceCatalog))
galaxySourceCatalog._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(galaxySourceCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FilterTransmission')), min_occurs=0L, max_occurs=None)
    )
galaxySourceCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(galaxySourceCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySourceCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySourceCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySourceCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GalaxySources')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(galaxySourceCatalog._GroupModel_, min_occurs=1, max_occurs=1)
    )
galaxySourceCatalog._ContentModel = pyxb.binding.content.ParticleModel(galaxySourceCatalog._GroupModel, min_occurs=1, max_occurs=1)



simulationInputModels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GalaxyAbsorptionInputDataMoodel'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=simulationInputModels, documentation=u'Reference to Galaxy absorption input data model (refFormat).'))

simulationInputModels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NISPInputDataModel'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=simulationInputModels, documentation=u'Reference to NISP input data model (refFormat).'))

simulationInputModels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PixelSimulatorConfigurationId'), tipsInputConfigurationId, scope=simulationInputModels, documentation=u'Reference to Simulator configuration input data model (refFormat)'))

simulationInputModels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TelescopeInputDataModel'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=simulationInputModels, documentation=u'Reference to Telescope input data model.'))

simulationInputModels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NISPOpticsInputDataModel'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=simulationInputModels, documentation=u'Reference to NISP optics input data model (refFormat).'))

simulationInputModels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SkyBackgroundInputDataModel'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=simulationInputModels, documentation=u'Reference to Sky background input data model (refFormat).'))

simulationInputModels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TelescopeOpticsInputDataModel'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=simulationInputModels, documentation=u'Reference to Telescope optics input data model (refFormat)'))
simulationInputModels._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(simulationInputModels._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PixelSimulatorConfigurationId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulationInputModels._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SkyBackgroundInputDataModel')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulationInputModels._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GalaxyAbsorptionInputDataMoodel')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulationInputModels._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TelescopeInputDataModel')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulationInputModels._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TelescopeOpticsInputDataModel')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulationInputModels._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NISPInputDataModel')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(simulationInputModels._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NISPOpticsInputDataModel')), min_occurs=0L, max_occurs=1)
    )
simulationInputModels._ContentModel = pyxb.binding.content.ParticleModel(simulationInputModels._GroupModel, min_occurs=1, max_occurs=1)



nipInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=nipInputConfiguration))

nipInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimulationSettings'), nipSimulationSettings, scope=nipInputConfiguration))

nipInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FPA'), simFocalPlaneArangement, scope=nipInputConfiguration))

nipInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), detectorList, scope=nipInputConfiguration))

nipInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Catalog'), nipCatalogProduct, scope=nipInputConfiguration))
nipInputConfiguration._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nipInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nipInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SimulationSettings')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nipInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Catalog')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nipInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nipInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorList')), min_occurs=1, max_occurs=1)
    )
nipInputConfiguration._ContentModel = pyxb.binding.content.ParticleModel(nipInputConfiguration._GroupModel, min_occurs=1, max_occurs=1)



galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmissionLines'), emissionLine, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObjectType'), objectType, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MorphologyGeneric'), morphologyGeneric, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpectrumStorage'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RA'), pyxb.binding.datatypes.double, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Magnitude'), magnitude, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Redshift'), pyxb.binding.datatypes.double, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ShapeletModel'), morphologyModel, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEC'), pyxb.binding.datatypes.double, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MorphologySersic'), morphologyModel, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpectedRedshift'), pyxb.binding.datatypes.double, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MorphologyImage'), morphologyImage, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SED'), SED, scope=galaxySource))

galaxySource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), CommonDM.dm.bas_stub.objectId, scope=galaxySource))
galaxySource._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObjectType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEC')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Magnitude')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SED')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Redshift')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpectedRedshift')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EmissionLines')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MorphologySersic')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ShapeletModel')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MorphologyImage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MorphologyGeneric')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galaxySource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpectrumStorage')), min_occurs=0L, max_occurs=1)
    )
galaxySource._ContentModel = pyxb.binding.content.ParticleModel(galaxySource._GroupModel, min_occurs=1, max_occurs=1)



metadataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Data'), dataVISNISPSimulationInterfaces, scope=metadataVISNISPSimulationInterfaces))

metadataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=metadataVISNISPSimulationInterfaces))
metadataVISNISPSimulationInterfaces._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(metadataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(metadataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Data')), min_occurs=1, max_occurs=1)
    )
metadataVISNISPSimulationInterfaces._ContentModel = pyxb.binding.content.ParticleModel(metadataVISNISPSimulationInterfaces._GroupModel, min_occurs=1, max_occurs=1)



fpaPointing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Dec'), CommonDM.dm.bas.dtd_stub.degAngle, scope=fpaPointing, documentation=u'Declination of the FPA, in degrees.'))

fpaPointing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Orientation'), CommonDM.dm.bas.dtd_stub.degAngle, scope=fpaPointing, documentation=u'Counterclockwise angle from the positive RA axis, in degrees.'))

fpaPointing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RA'), CommonDM.dm.bas.dtd_stub.degAngle, scope=fpaPointing, documentation=u'Right ascension of the FPA, in degrees.'))
fpaPointing._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fpaPointing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fpaPointing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fpaPointing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Orientation')), min_occurs=1, max_occurs=1)
    )
fpaPointing._ContentModel = pyxb.binding.content.ParticleModel(fpaPointing._GroupModel, min_occurs=1, max_occurs=1)



WeakLensingMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ShearParameters'), shearParameter, scope=WeakLensingMap))

WeakLensingMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), pyxb.binding.datatypes.string, scope=WeakLensingMap))

WeakLensingMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), pyxb.binding.datatypes.string, scope=WeakLensingMap))
WeakLensingMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(WeakLensingMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(WeakLensingMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(WeakLensingMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ShearParameters')), min_occurs=1L, max_occurs=None)
    )
WeakLensingMap._ContentModel = pyxb.binding.content.ParticleModel(WeakLensingMap._GroupModel, min_occurs=1, max_occurs=1)



shearParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'g2'), pyxb.binding.datatypes.double, scope=shearParameter))

shearParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RAUnit'), CommonDM.dm.bas.utd_stub.unit, scope=shearParameter))

shearParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'g1'), pyxb.binding.datatypes.double, scope=shearParameter))

shearParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DECUnit'), CommonDM.dm.bas.utd_stub.unit, scope=shearParameter))

shearParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RA'), pyxb.binding.datatypes.double, scope=shearParameter))

shearParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DEC'), pyxb.binding.datatypes.double, scope=shearParameter))
shearParameter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(shearParameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shearParameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DEC')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shearParameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RAUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shearParameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DECUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shearParameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'g1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shearParameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'g2')), min_occurs=1, max_occurs=1)
    )
shearParameter._ContentModel = pyxb.binding.content.ParticleModel(shearParameter._GroupModel, min_occurs=1, max_occurs=1)



nipSimulationSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FilterName'), CommonDM.dm.ins.nis_stub.filterName, scope=nipSimulationSettings, documentation=u'The name of the filter to simulate.'))
nipSimulationSettings._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nipSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nipSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nipSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPAPointing')), min_occurs=1, max_occurs=1)
    )
nipSimulationSettings._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nipSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FilterName')), min_occurs=1, max_occurs=1)
    )
nipSimulationSettings._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nipSimulationSettings._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nipSimulationSettings._GroupModel_2, min_occurs=1, max_occurs=1)
    )
nipSimulationSettings._ContentModel = pyxb.binding.content.ParticleModel(nipSimulationSettings._GroupModel, min_occurs=1, max_occurs=1)



tipsInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimulationSettings'), tipsSimulationSettings, scope=tipsInputConfiguration))

tipsInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OpticsModel'), CommonDM.dm.ins.nis_stub.grismModeModel, scope=tipsInputConfiguration))

tipsInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Catalog'), catalogProduct, scope=tipsInputConfiguration))

tipsInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), detectorList, scope=tipsInputConfiguration))

tipsInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FPA'), simFocalPlaneArangement, scope=tipsInputConfiguration))

tipsInputConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=tipsInputConfiguration))
tipsInputConfiguration._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(tipsInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(tipsInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SimulationSettings')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(tipsInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Catalog')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(tipsInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(tipsInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorList')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(tipsInputConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OpticsModel')), min_occurs=1, max_occurs=1)
    )
tipsInputConfiguration._ContentModel = pyxb.binding.content.ParticleModel(tipsInputConfiguration._GroupModel, min_occurs=1, max_occurs=1)



nipOutput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimulatedDetectorImage'), nipSimulatedImage, scope=nipOutput))

nipOutput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InputConfigurationId'), pyxb.binding.datatypes.string, scope=nipOutput))

nipOutput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), pyxb.binding.datatypes.string, scope=nipOutput))
nipOutput._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nipOutput._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nipOutput._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InputConfigurationId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nipOutput._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SimulatedDetectorImage')), min_occurs=0L, max_occurs=None)
    )
nipOutput._ContentModel = pyxb.binding.content.ParticleModel(nipOutput._GroupModel, min_occurs=1, max_occurs=1)



dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimulationInputModels'), simulationInputModels, scope=dataVISNISPSimulationInterfaces))

dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ListOfImageSequenceSimulated'), setOfSimulatedImages, scope=dataVISNISPSimulationInterfaces))

dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FPADetectorList'), CommonDM.dm.bas.dtd_stub.listOfInteger2, scope=dataVISNISPSimulationInterfaces, documentation=u'List of detector identifiers simulated.'))

dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PixelSimulatorName'), pyxb.binding.datatypes.string, scope=dataVISNISPSimulationInterfaces, documentation=u'Different codes of simulation could be used for different objects. Please refere here the name of the Simulator SW code.'))

dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode'), CommonDM.dm.ins_stub.observationMode, scope=dataVISNISPSimulationInterfaces, documentation=u'refer to observation Mode used for the simulation runtime : calibration, wide or deep.'))

dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TelescopePointingDec'), CommonDM.dm.bas.dtd_stub.degAngle, scope=dataVISNISPSimulationInterfaces, documentation=u'Declinaison of the pointing angles of the telescope in the center of the field.'))

dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumberOfSimulatedDetectors'), pyxb.binding.datatypes.short, scope=dataVISNISPSimulationInterfaces, documentation=u'Number of simulated detectors corresponding to the cardinality of FPADetectorList.'))

dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PixelSimulatorVersion'), CommonDM.dm.sys_stub.version, scope=dataVISNISPSimulationInterfaces, documentation=u'Refer here to the version of the SW simulator code.'))

dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate'), pyxb.binding.datatypes.dateTime, scope=dataVISNISPSimulationInterfaces, documentation=u'refer to observation date of the image.'))

dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GrismOrderSimulation'), CommonDM.dm.bas.dtd_stub.listOfInteger2, scope=dataVISNISPSimulationInterfaces, documentation=u'Order of the grism simulation image inside the fits file.'))

dataVISNISPSimulationInterfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TelescopePointingRA'), CommonDM.dm.bas.dtd_stub.degAngle, scope=dataVISNISPSimulationInterfaces, documentation=u'Right Ascension of the pointing angles of the telescope in the center of the field.'))
dataVISNISPSimulationInterfaces._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PixelSimulatorName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PixelSimulatorVersion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SimulationInputModels')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TelescopePointingRA')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TelescopePointingDec')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GrismOrderSimulation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPADetectorList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumberOfSimulatedDetectors')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ListOfImageSequenceSimulated')), min_occurs=1, max_occurs=1)
    )
dataVISNISPSimulationInterfaces._ContentModel = pyxb.binding.content.ParticleModel(dataVISNISPSimulationInterfaces._GroupModel, min_occurs=1, max_occurs=1)


catalogFitsFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogFitsFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
catalogFitsFile._ContentModel = pyxb.binding.content.ParticleModel(catalogFitsFile._GroupModel, min_occurs=1, max_occurs=1)



tipsSimulationSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimulatedGrismOrderList'), STD_ANON, scope=tipsSimulationSettings))
tipsSimulationSettings._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(tipsSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(tipsSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(tipsSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FPAPointing')), min_occurs=1, max_occurs=1)
    )
tipsSimulationSettings._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(tipsSimulationSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SimulatedGrismOrderList')), min_occurs=1, max_occurs=1)
    )
tipsSimulationSettings._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(tipsSimulationSettings._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(tipsSimulationSettings._GroupModel_2, min_occurs=1, max_occurs=1)
    )
tipsSimulationSettings._ContentModel = pyxb.binding.content.ParticleModel(tipsSimulationSettings._GroupModel, min_occurs=1, max_occurs=1)



catalogProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpectraFitsFile'), spectraFitsFile, scope=catalogProduct))

catalogProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogFitsFile'), catalogFitsFile, scope=catalogProduct))
catalogProduct._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(catalogProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogFitsFile')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(catalogProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpectraFitsFile')), min_occurs=1, max_occurs=1)
    )
catalogProduct._ContentModel = pyxb.binding.content.ParticleModel(catalogProduct._GroupModel, min_occurs=1, max_occurs=1)


spectrumFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrumFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
spectrumFile._ContentModel = pyxb.binding.content.ParticleModel(spectrumFile._GroupModel, min_occurs=1, max_occurs=1)
