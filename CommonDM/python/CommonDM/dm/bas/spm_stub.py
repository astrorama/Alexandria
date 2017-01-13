# /home/nikoapos/ISDC/Projects/Alexandria/2.0/CommonDM/python/CommonDM/dm/bas/spm_stub.py
# PyXB bindings for NamespaceModule
# NSM:8f3807dbd7e5a83390236640f018e76f2abc9bfa
# Generated 2014-06-12 14:36:51.814762 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:399d4060-f22e-11e3-acaf-c4d98710dc86')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import CommonDM.dm.bas.utd_stub
import CommonDM.dm.bas.dtd_stub
import CommonDM.dm.bas_stub
import CommonDM.dm.bas.imp.stc_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm', create_if_missing=True)
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
class spectralRangeName (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of acronyms for spectral ranges"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectralRangeName')
    _Documentation = u'List of acronyms for spectral ranges'
spectralRangeName._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=spectralRangeName, enum_prefix=None)
spectralRangeName.BLUE = spectralRangeName._CF_enumeration.addEnumeration(unicode_value=u'BLUE')
spectralRangeName.RED = spectralRangeName._CF_enumeration.addEnumeration(unicode_value=u'RED')
spectralRangeName.COADD = spectralRangeName._CF_enumeration.addEnumeration(unicode_value=u'COADD')
spectralRangeName._InitializeFacetMap(spectralRangeName._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'spectralRangeName', spectralRangeName)

# Atomic SimpleTypeDefinition
class spectrumId (pyxb.binding.datatypes.string):

    """A string containing a unique ID for the spectrum."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrumId')
    _Documentation = u'A string containing a unique ID for the spectrum.'
spectrumId._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'spectrumId', spectrumId)

# Atomic SimpleTypeDefinition
class spectrumClass (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The spectrum class, which specifies whether the spectrum is a sub-spectrum or a co-added, and which one."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrumClass')
    _Documentation = u'The spectrum class, which specifies whether the spectrum is a sub-spectrum or a co-added, and which one.'
spectrumClass._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=spectrumClass, enum_prefix=None)
spectrumClass.SUB_B0 = spectrumClass._CF_enumeration.addEnumeration(unicode_value=u'SUB_B0')
spectrumClass.SUB_B90 = spectrumClass._CF_enumeration.addEnumeration(unicode_value=u'SUB_B90')
spectrumClass.SUB_R0 = spectrumClass._CF_enumeration.addEnumeration(unicode_value=u'SUB_R0')
spectrumClass.SUB_R90 = spectrumClass._CF_enumeration.addEnumeration(unicode_value=u'SUB_R90')
spectrumClass.COADD_RB0 = spectrumClass._CF_enumeration.addEnumeration(unicode_value=u'COADD_RB0')
spectrumClass.COADD_RB90 = spectrumClass._CF_enumeration.addEnumeration(unicode_value=u'COADD_RB90')
spectrumClass.COADD_FULL = spectrumClass._CF_enumeration.addEnumeration(unicode_value=u'COADD_FULL')
spectrumClass._InitializeFacetMap(spectrumClass._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'spectrumClass', spectrumClass)

# Complex type spectralRangeId with content type ELEMENT_ONLY
class spectralRangeId (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectralRangeId')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/spm}SpectrumLength uses Python identifier SpectrumLength
    __SpectrumLength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpectrumLength'), 'SpectrumLength', '__httpeuclid_esa_orgschemabasspm_spectralRangeId_httpeuclid_esa_orgschemabasspmSpectrumLength', False)

    
    SpectrumLength = property(__SpectrumLength.value, __SpectrumLength.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}SpectralRangeName uses Python identifier SpectralRangeName
    __SpectralRangeName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpectralRangeName'), 'SpectralRangeName', '__httpeuclid_esa_orgschemabasspm_spectralRangeId_httpeuclid_esa_orgschemabasspmSpectralRangeName', False)

    
    SpectralRangeName = property(__SpectralRangeName.value, __SpectralRangeName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}SpectralOrder uses Python identifier SpectralOrder
    __SpectralOrder = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpectralOrder'), 'SpectralOrder', '__httpeuclid_esa_orgschemabasspm_spectralRangeId_httpeuclid_esa_orgschemabasspmSpectralOrder', False)

    
    SpectralOrder = property(__SpectralOrder.value, __SpectralOrder.set, None, None)


    _ElementMap = {
        __SpectrumLength.name() : __SpectrumLength,
        __SpectralRangeName.name() : __SpectralRangeName,
        __SpectralOrder.name() : __SpectralOrder
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spectralRangeId', spectralRangeId)


# Complex type spectrum1DError with content type ELEMENT_ONLY
class spectrum1DError (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrum1DError')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/spm}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemabasspm_spectrum1DError_httpeuclid_esa_orgschemabasspmUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}Values uses Python identifier Values
    __Values = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Values'), 'Values', '__httpeuclid_esa_orgschemabasspm_spectrum1DError_httpeuclid_esa_orgschemabasspmValues', False)

    
    Values = property(__Values.value, __Values.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Values.name() : __Values
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spectrum1DError', spectrum1DError)


# Complex type spectrum1DData with content type ELEMENT_ONLY
class spectrum1DData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrum1DData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/spm}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemabasspm_spectrum1DData_httpeuclid_esa_orgschemabasspmUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}Values uses Python identifier Values
    __Values = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Values'), 'Values', '__httpeuclid_esa_orgschemabasspm_spectrum1DData_httpeuclid_esa_orgschemabasspmValues', False)

    
    Values = property(__Values.value, __Values.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Values.name() : __Values
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spectrum1DData', spectrum1DData)


# Complex type spectrum1DFlag with content type ELEMENT_ONLY
class spectrum1DFlag (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrum1DFlag')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/spm}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemabasspm_spectrum1DFlag_httpeuclid_esa_orgschemabasspmUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}Values uses Python identifier Values
    __Values = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Values'), 'Values', '__httpeuclid_esa_orgschemabasspm_spectrum1DFlag_httpeuclid_esa_orgschemabasspmValues', False)

    
    Values = property(__Values.value, __Values.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Values.name() : __Values
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spectrum1DFlag', spectrum1DFlag)


# Complex type spectrumMetadata with content type ELEMENT_ONLY
class spectrumMetadata (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrumMetadata')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/spm}ObjectName uses Python identifier ObjectName
    __ObjectName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObjectName'), 'ObjectName', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmObjectName', False)

    
    ObjectName = property(__ObjectName.value, __ObjectName.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/bas/spm}RangeID uses Python identifier RangeID
    __RangeID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RangeID'), 'RangeID', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmRangeID', False)

    
    RangeID = property(__RangeID.value, __RangeID.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}TrasmissionCurve uses Python identifier TrasmissionCurve
    __TrasmissionCurve = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TrasmissionCurve'), 'TrasmissionCurve', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmTrasmissionCurve', False)

    
    TrasmissionCurve = property(__TrasmissionCurve.value, __TrasmissionCurve.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Class'), 'Class', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmClass', False)

    
    Class = property(__Class.value, __Class.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}Array uses Python identifier Array
    __Array = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Array'), 'Array', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmArray', False)

    
    Array = property(__Array.value, __Array.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/bas/spm}Coordinates uses Python identifier Coordinates
    __Coordinates = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Coordinates'), 'Coordinates', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmCoordinates', False)

    
    Coordinates = property(__Coordinates.value, __Coordinates.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/bas/spm}Survey uses Python identifier Survey
    __Survey = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Survey'), 'Survey', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmSurvey', False)

    
    Survey = property(__Survey.value, __Survey.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/bas/spm}Frame uses Python identifier Frame
    __Frame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Frame'), 'Frame', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmFrame', False)

    
    Frame = property(__Frame.value, __Frame.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/bas/spm}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmId', False)

    
    Id = property(__Id.value, __Id.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/bas/spm}Observation uses Python identifier Observation
    __Observation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Observation'), 'Observation', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmObservation', False)

    
    Observation = property(__Observation.value, __Observation.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/bas/spm}Filename uses Python identifier Filename
    __Filename = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filename'), 'Filename', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmFilename', False)

    
    Filename = property(__Filename.value, __Filename.set, None, u'Source file name')

    
    # Element {http://euclid.esa.org/schema/bas/spm}Patch uses Python identifier Patch
    __Patch = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Patch'), 'Patch', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmPatch', False)

    
    Patch = property(__Patch.value, __Patch.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/bas/spm}Exposure uses Python identifier Exposure
    __Exposure = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Exposure'), 'Exposure', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmExposure', False)

    
    Exposure = property(__Exposure.value, __Exposure.set, None, u'')

    
    # Element {http://euclid.esa.org/schema/bas/spm}OrigFile uses Python identifier OrigFile
    __OrigFile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OrigFile'), 'OrigFile', '__httpeuclid_esa_orgschemabasspm_spectrumMetadata_httpeuclid_esa_orgschemabasspmOrigFile', False)

    
    OrigFile = property(__OrigFile.value, __OrigFile.set, None, u'Original file name')


    _ElementMap = {
        __ObjectName.name() : __ObjectName,
        __RangeID.name() : __RangeID,
        __TrasmissionCurve.name() : __TrasmissionCurve,
        __Class.name() : __Class,
        __Array.name() : __Array,
        __Coordinates.name() : __Coordinates,
        __Survey.name() : __Survey,
        __Frame.name() : __Frame,
        __Id.name() : __Id,
        __Observation.name() : __Observation,
        __Filename.name() : __Filename,
        __Patch.name() : __Patch,
        __Exposure.name() : __Exposure,
        __OrigFile.name() : __OrigFile
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spectrumMetadata', spectrumMetadata)


# Complex type spectrum with content type ELEMENT_ONLY
class spectrum (spectrumMetadata):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrum')
    # Base type is spectrumMetadata
    
    # Element ObjectName ({http://euclid.esa.org/schema/bas/spm}ObjectName) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element RangeID ({http://euclid.esa.org/schema/bas/spm}RangeID) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element OrigFile ({http://euclid.esa.org/schema/bas/spm}OrigFile) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Exposure ({http://euclid.esa.org/schema/bas/spm}Exposure) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Class ({http://euclid.esa.org/schema/bas/spm}Class) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Array ({http://euclid.esa.org/schema/bas/spm}Array) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Coordinates ({http://euclid.esa.org/schema/bas/spm}Coordinates) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Survey ({http://euclid.esa.org/schema/bas/spm}Survey) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Frame ({http://euclid.esa.org/schema/bas/spm}Frame) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Id ({http://euclid.esa.org/schema/bas/spm}Id) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Observation ({http://euclid.esa.org/schema/bas/spm}Observation) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Filename ({http://euclid.esa.org/schema/bas/spm}Filename) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Patch ({http://euclid.esa.org/schema/bas/spm}Patch) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element {http://euclid.esa.org/schema/bas/spm}SpectrumData uses Python identifier SpectrumData
    __SpectrumData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpectrumData'), 'SpectrumData', '__httpeuclid_esa_orgschemabasspm_spectrum_httpeuclid_esa_orgschemabasspmSpectrumData', False)

    
    SpectrumData = property(__SpectrumData.value, __SpectrumData.set, None, None)

    
    # Element TrasmissionCurve ({http://euclid.esa.org/schema/bas/spm}TrasmissionCurve) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata

    _ElementMap = spectrumMetadata._ElementMap.copy()
    _ElementMap.update({
        __SpectrumData.name() : __SpectrumData
    })
    _AttributeMap = spectrumMetadata._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'spectrum', spectrum)


# Complex type spectrumData with content type ELEMENT_ONLY
class spectrumData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectrumData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/spm}Noise uses Python identifier Noise
    __Noise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Noise'), 'Noise', '__httpeuclid_esa_orgschemabasspm_spectrumData_httpeuclid_esa_orgschemabasspmNoise', False)

    
    Noise = property(__Noise.value, __Noise.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}Contamination uses Python identifier Contamination
    __Contamination = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Contamination'), 'Contamination', '__httpeuclid_esa_orgschemabasspm_spectrumData_httpeuclid_esa_orgschemabasspmContamination', False)

    
    Contamination = property(__Contamination.value, __Contamination.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}Wavelegth uses Python identifier Wavelegth
    __Wavelegth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Wavelegth'), 'Wavelegth', '__httpeuclid_esa_orgschemabasspm_spectrumData_httpeuclid_esa_orgschemabasspmWavelegth', False)

    
    Wavelegth = property(__Wavelegth.value, __Wavelegth.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}Flux uses Python identifier Flux
    __Flux = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flux'), 'Flux', '__httpeuclid_esa_orgschemabasspm_spectrumData_httpeuclid_esa_orgschemabasspmFlux', False)

    
    Flux = property(__Flux.value, __Flux.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/spm}PixelQuality uses Python identifier PixelQuality
    __PixelQuality = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PixelQuality'), 'PixelQuality', '__httpeuclid_esa_orgschemabasspm_spectrumData_httpeuclid_esa_orgschemabasspmPixelQuality', False)

    
    PixelQuality = property(__PixelQuality.value, __PixelQuality.set, None, None)


    _ElementMap = {
        __Noise.name() : __Noise,
        __Contamination.name() : __Contamination,
        __Wavelegth.name() : __Wavelegth,
        __Flux.name() : __Flux,
        __PixelQuality.name() : __PixelQuality
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spectrumData', spectrumData)




spectralRangeId._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpectrumLength'), pyxb.binding.datatypes.short, scope=spectralRangeId))

spectralRangeId._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpectralRangeName'), spectralRangeName, scope=spectralRangeId))

spectralRangeId._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpectralOrder'), pyxb.binding.datatypes.short, scope=spectralRangeId))
spectralRangeId._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectralRangeId._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpectralRangeName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectralRangeId._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpectralOrder')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectralRangeId._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpectrumLength')), min_occurs=1, max_occurs=1)
    )
spectralRangeId._ContentModel = pyxb.binding.content.ParticleModel(spectralRangeId._GroupModel, min_occurs=1, max_occurs=1)



spectrum1DError._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=spectrum1DError))

spectrum1DError._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Values'), CommonDM.dm.bas.dtd_stub.listOfDouble, scope=spectrum1DError))
spectrum1DError._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrum1DError._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Values')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum1DError._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=0L, max_occurs=1)
    )
spectrum1DError._ContentModel = pyxb.binding.content.ParticleModel(spectrum1DError._GroupModel, min_occurs=1, max_occurs=1)



spectrum1DData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=spectrum1DData))

spectrum1DData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Values'), CommonDM.dm.bas.dtd_stub.listOfDouble, scope=spectrum1DData))
spectrum1DData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrum1DData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Values')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum1DData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=0L, max_occurs=1)
    )
spectrum1DData._ContentModel = pyxb.binding.content.ParticleModel(spectrum1DData._GroupModel, min_occurs=1, max_occurs=1)



spectrum1DFlag._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=spectrum1DFlag))

spectrum1DFlag._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Values'), CommonDM.dm.bas.dtd_stub.listOfInteger8, scope=spectrum1DFlag))
spectrum1DFlag._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrum1DFlag._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Values')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum1DFlag._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=0L, max_occurs=1)
    )
spectrum1DFlag._ContentModel = pyxb.binding.content.ParticleModel(spectrum1DFlag._GroupModel, min_occurs=1, max_occurs=1)



spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObjectName'), CommonDM.dm.bas_stub.objectName, scope=spectrumMetadata, documentation=u''))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RangeID'), spectralRangeId, scope=spectrumMetadata))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TrasmissionCurve'), pyxb.binding.datatypes.string, scope=spectrumMetadata))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Class'), spectrumClass, scope=spectrumMetadata))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Array'), pyxb.binding.datatypes.string, scope=spectrumMetadata, documentation=u''))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Coordinates'), CommonDM.dm.bas.imp.stc_stub.astroCoordSystem, scope=spectrumMetadata, documentation=u''))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Survey'), pyxb.binding.datatypes.string, scope=spectrumMetadata, documentation=u''))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Frame'), pyxb.binding.datatypes.string, scope=spectrumMetadata, documentation=u''))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), spectrumId, scope=spectrumMetadata, documentation=u''))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Observation'), pyxb.binding.datatypes.string, scope=spectrumMetadata, documentation=u''))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filename'), pyxb.binding.datatypes.string, scope=spectrumMetadata, documentation=u'Source file name'))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Patch'), pyxb.binding.datatypes.string, scope=spectrumMetadata, documentation=u''))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Exposure'), pyxb.binding.datatypes.string, scope=spectrumMetadata, documentation=u''))

spectrumMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OrigFile'), pyxb.binding.datatypes.string, scope=spectrumMetadata, documentation=u'Original file name'))
spectrumMetadata._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObjectName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coordinates')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filename')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OrigFile')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Class')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RangeID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TrasmissionCurve')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Survey')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Patch')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observation')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Exposure')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Array')), min_occurs=1, max_occurs=1)
    )
spectrumMetadata._ContentModel = pyxb.binding.content.ParticleModel(spectrumMetadata._GroupModel, min_occurs=1, max_occurs=1)



spectrum._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpectrumData'), spectrumData, scope=spectrum))
spectrum._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObjectName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coordinates')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filename')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OrigFile')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Class')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RangeID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TrasmissionCurve')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Survey')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Patch')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observation')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Exposure')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Array')), min_occurs=1, max_occurs=1)
    )
spectrum._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpectrumData')), min_occurs=1, max_occurs=1)
    )
spectrum._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrum._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrum._GroupModel_2, min_occurs=1, max_occurs=1)
    )
spectrum._ContentModel = pyxb.binding.content.ParticleModel(spectrum._GroupModel, min_occurs=1, max_occurs=1)



spectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Noise'), spectrum1DError, scope=spectrumData))

spectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contamination'), spectrum1DData, scope=spectrumData))

spectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wavelegth'), spectrum1DData, scope=spectrumData))

spectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flux'), spectrum1DData, scope=spectrumData))

spectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PixelQuality'), spectrum1DFlag, scope=spectrumData))
spectrumData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Wavelegth')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flux')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Noise')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contamination')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PixelQuality')), min_occurs=1, max_occurs=1)
    )
spectrumData._ContentModel = pyxb.binding.content.ParticleModel(spectrumData._GroupModel, min_occurs=1, max_occurs=1)
