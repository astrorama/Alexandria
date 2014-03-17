# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/pro/spe_stub.py
# PyXB bindings for NamespaceModule
# NSM:26edd20c3857449d49a66aa8c083722722bbbacd
# Generated 2014-03-17 11:53:47.251204 by PyXB version 1.1.2
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
import CommonDM.dm.bas.spm_stub
import CommonDM.dm.sys_stub
import CommonDM.dm.bas.imp.stc_stub
import CommonDM.dm.bas_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/spe', create_if_missing=True)
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


# Complex type redshift with content type ELEMENT_ONLY
class redshift (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'redshift')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/spe}RedshiftError uses Python identifier RedshiftError
    __RedshiftError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RedshiftError'), 'RedshiftError', '__httpeuclid_esa_orgschemaprospe_redshift_httpeuclid_esa_orgschemaprospeRedshiftError', False)

    
    RedshiftError = property(__RedshiftError.value, __RedshiftError.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/spe}Redshift uses Python identifier Redshift
    __Redshift = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Redshift'), 'Redshift', '__httpeuclid_esa_orgschemaprospe_redshift_httpeuclid_esa_orgschemaprospeRedshift', False)

    
    Redshift = property(__Redshift.value, __Redshift.set, None, None)


    _ElementMap = {
        __RedshiftError.name() : __RedshiftError,
        __Redshift.name() : __Redshift
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'redshift', redshift)


# Complex type spectralTemplate with content type ELEMENT_ONLY
class spectralTemplate (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectralTemplate')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/spe}spectrum uses Python identifier spectrum
    __spectrum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spectrum'), 'spectrum', '__httpeuclid_esa_orgschemaprospe_spectralTemplate_httpeuclid_esa_orgschemaprospespectrum', False)

    
    spectrum = property(__spectrum.value, __spectrum.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/spe}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemaprospe_spectralTemplate_httpeuclid_esa_orgschemaprospeName', False)

    
    Name = property(__Name.value, __Name.set, None, None)


    _ElementMap = {
        __spectrum.name() : __spectrum,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spectralTemplate', spectralTemplate)


# Complex type SPEResults with content type ELEMENT_ONLY
class SPEResults (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SPEResults')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprospe_SPEResults_Data', True)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprospe_SPEResults_Header', True)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'SPEResults', SPEResults)


# Complex type SPECalibratedSpectra with content type ELEMENT_ONLY
class SPECalibratedSpectra (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SPECalibratedSpectra')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprospe_SPECalibratedSpectra_Data', True)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprospe_SPECalibratedSpectra_Header', True)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'SPECalibratedSpectra', SPECalibratedSpectra)


# Complex type SPESpectralTemplates with content type ELEMENT_ONLY
class SPESpectralTemplates (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SPESpectralTemplates')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprospe_SPESpectralTemplates_Header', True)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprospe_SPESpectralTemplates_Data', True)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'SPESpectralTemplates', SPESpectralTemplates)


# Complex type SPESpectralFeatures with content type ELEMENT_ONLY
class SPESpectralFeatures (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SPESpectralFeatures')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__httpeuclid_esa_orgschemaprospe_SPESpectralFeatures_Header', True)

    
    Header = property(__Header.value, __Header.set, None, u'The generic header of the product.')

    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__httpeuclid_esa_orgschemaprospe_SPESpectralFeatures_Data', True)

    
    Data = property(__Data.value, __Data.set, None, u'The data of the product.')


    _ElementMap = {
        __Header.name() : __Header,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'SPESpectralFeatures', SPESpectralFeatures)


# Complex type spectralFeature with content type ELEMENT_ONLY
class spectralFeature (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectralFeature')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/spe}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Type'), 'Type', '__httpeuclid_esa_orgschemaprospe_spectralFeature_httpeuclid_esa_orgschemaprospeType', False)

    
    Type = property(__Type.value, __Type.set, None, u"Feature's type :\nA(bsorption) ,\nE(mission) ,\t\t\nB(road)\t,\t\nD(iscontinuity")

    
    # Element {http://euclid.esa.org/schema/pro/spe}Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), 'Wavelength', '__httpeuclid_esa_orgschemaprospe_spectralFeature_httpeuclid_esa_orgschemaprospeWavelength', False)

    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, u'Vacuum Wavelength')

    
    # Element {http://euclid.esa.org/schema/pro/spe}Flag uses Python identifier Flag
    __Flag = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flag'), 'Flag', '__httpeuclid_esa_orgschemaprospe_spectralFeature_httpeuclid_esa_orgschemaprospeFlag', False)

    
    Flag = property(__Flag.value, __Flag.set, None, u'2 for the strong emission lines from which the redshift will be measured if they are present ; \n1 for weaker emission lines used for check ;\n-1 for strong absorption lines that can be used to measure a z if a continuum is there ; \n0 for those only used to superimpose on a spectrum once a z has been measured ;\n3 for the continuum features (Breaks) ')

    
    # Element {http://euclid.esa.org/schema/pro/spe}Element uses Python identifier Element
    __Element = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Element'), 'Element', '__httpeuclid_esa_orgschemaprospe_spectralFeature_httpeuclid_esa_orgschemaprospeElement', False)

    
    Element = property(__Element.value, __Element.set, None, u'Element name')

    
    # Element {http://euclid.esa.org/schema/pro/spe}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'comment'), 'comment', '__httpeuclid_esa_orgschemaprospe_spectralFeature_httpeuclid_esa_orgschemaprospecomment', False)

    
    comment = property(__comment.value, __comment.set, None, None)


    _ElementMap = {
        __Type.name() : __Type,
        __Wavelength.name() : __Wavelength,
        __Flag.name() : __Flag,
        __Element.name() : __Element,
        __comment.name() : __comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spectralFeature', spectralFeature)


# Complex type calibratedSpectrum with content type ELEMENT_ONLY
class calibratedSpectrum (CommonDM.dm.bas.spm_stub.spectrumMetadata):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'calibratedSpectrum')
    # Base type is CommonDM.dm.bas.spm_stub.spectrumMetadata
    
    # Element Observation ({http://euclid.esa.org/schema/bas/spm}Observation) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Filename ({http://euclid.esa.org/schema/bas/spm}Filename) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Array ({http://euclid.esa.org/schema/bas/spm}Array) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element OrigFile ({http://euclid.esa.org/schema/bas/spm}OrigFile) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element {http://euclid.esa.org/schema/pro/spe}SpectrumData uses Python identifier SpectrumData
    __SpectrumData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpectrumData'), 'SpectrumData', '__httpeuclid_esa_orgschemaprospe_calibratedSpectrum_httpeuclid_esa_orgschemaprospeSpectrumData', False)

    
    SpectrumData = property(__SpectrumData.value, __SpectrumData.set, None, None)

    
    # Element ObjectName ({http://euclid.esa.org/schema/bas/spm}ObjectName) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Class ({http://euclid.esa.org/schema/bas/spm}Class) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Frame ({http://euclid.esa.org/schema/bas/spm}Frame) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Id ({http://euclid.esa.org/schema/bas/spm}Id) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Patch ({http://euclid.esa.org/schema/bas/spm}Patch) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Coordinates ({http://euclid.esa.org/schema/bas/spm}Coordinates) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Exposure ({http://euclid.esa.org/schema/bas/spm}Exposure) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element Survey ({http://euclid.esa.org/schema/bas/spm}Survey) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element TrasmissionCurve ({http://euclid.esa.org/schema/bas/spm}TrasmissionCurve) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata
    
    # Element RangeID ({http://euclid.esa.org/schema/bas/spm}RangeID) inherited from {http://euclid.esa.org/schema/bas/spm}spectrumMetadata

    _ElementMap = CommonDM.dm.bas.spm_stub.spectrumMetadata._ElementMap.copy()
    _ElementMap.update({
        __SpectrumData.name() : __SpectrumData
    })
    _AttributeMap = CommonDM.dm.bas.spm_stub.spectrumMetadata._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'calibratedSpectrum', calibratedSpectrum)


# Complex type result with content type ELEMENT_ONLY
class result (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'result')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/spe}SpectroscopicRedshift uses Python identifier SpectroscopicRedshift
    __SpectroscopicRedshift = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SpectroscopicRedshift'), 'SpectroscopicRedshift', '__httpeuclid_esa_orgschemaprospe_result_httpeuclid_esa_orgschemaprospeSpectroscopicRedshift', False)

    
    SpectroscopicRedshift = property(__SpectroscopicRedshift.value, __SpectroscopicRedshift.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/spe}Coordinates uses Python identifier Coordinates
    __Coordinates = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Coordinates'), 'Coordinates', '__httpeuclid_esa_orgschemaprospe_result_httpeuclid_esa_orgschemaprospeCoordinates', False)

    
    Coordinates = property(__Coordinates.value, __Coordinates.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/spe}ObjectName uses Python identifier ObjectName
    __ObjectName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObjectName'), 'ObjectName', '__httpeuclid_esa_orgschemaprospe_result_httpeuclid_esa_orgschemaprospeObjectName', False)

    
    ObjectName = property(__ObjectName.value, __ObjectName.set, None, None)


    _ElementMap = {
        __SpectroscopicRedshift.name() : __SpectroscopicRedshift,
        __Coordinates.name() : __Coordinates,
        __ObjectName.name() : __ObjectName
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'result', result)


# Complex type calibratedSpectrumData with content type ELEMENT_ONLY
class calibratedSpectrumData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'calibratedSpectrumData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/spe}Noise uses Python identifier Noise
    __Noise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Noise'), 'Noise', '__httpeuclid_esa_orgschemaprospe_calibratedSpectrumData_httpeuclid_esa_orgschemaprospeNoise', False)

    
    Noise = property(__Noise.value, __Noise.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/spe}Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), 'Wavelength', '__httpeuclid_esa_orgschemaprospe_calibratedSpectrumData_httpeuclid_esa_orgschemaprospeWavelength', False)

    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/spe}Contamination uses Python identifier Contamination
    __Contamination = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Contamination'), 'Contamination', '__httpeuclid_esa_orgschemaprospe_calibratedSpectrumData_httpeuclid_esa_orgschemaprospeContamination', False)

    
    Contamination = property(__Contamination.value, __Contamination.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/spe}Flux uses Python identifier Flux
    __Flux = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flux'), 'Flux', '__httpeuclid_esa_orgschemaprospe_calibratedSpectrumData_httpeuclid_esa_orgschemaprospeFlux', False)

    
    Flux = property(__Flux.value, __Flux.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/spe}PixelQuality uses Python identifier PixelQuality
    __PixelQuality = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PixelQuality'), 'PixelQuality', '__httpeuclid_esa_orgschemaprospe_calibratedSpectrumData_httpeuclid_esa_orgschemaprospePixelQuality', False)

    
    PixelQuality = property(__PixelQuality.value, __PixelQuality.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/spe}WavelengthError uses Python identifier WavelengthError
    __WavelengthError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WavelengthError'), 'WavelengthError', '__httpeuclid_esa_orgschemaprospe_calibratedSpectrumData_httpeuclid_esa_orgschemaprospeWavelengthError', False)

    
    WavelengthError = property(__WavelengthError.value, __WavelengthError.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/spe}FluxError uses Python identifier FluxError
    __FluxError = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FluxError'), 'FluxError', '__httpeuclid_esa_orgschemaprospe_calibratedSpectrumData_httpeuclid_esa_orgschemaprospeFluxError', False)

    
    FluxError = property(__FluxError.value, __FluxError.set, None, None)


    _ElementMap = {
        __Noise.name() : __Noise,
        __Wavelength.name() : __Wavelength,
        __Contamination.name() : __Contamination,
        __Flux.name() : __Flux,
        __PixelQuality.name() : __PixelQuality,
        __WavelengthError.name() : __WavelengthError,
        __FluxError.name() : __FluxError
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'calibratedSpectrumData', calibratedSpectrumData)




redshift._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RedshiftError'), pyxb.binding.datatypes.float, scope=redshift))

redshift._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Redshift'), pyxb.binding.datatypes.float, scope=redshift))
redshift._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(redshift._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Redshift')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(redshift._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RedshiftError')), min_occurs=1, max_occurs=1)
    )
redshift._ContentModel = pyxb.binding.content.ParticleModel(redshift._GroupModel, min_occurs=1, max_occurs=1)



spectralTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spectrum'), CommonDM.dm.bas.spm_stub.spectrum1DData, scope=spectralTemplate))

spectralTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=spectralTemplate))
spectralTemplate._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectralTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectralTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spectrum')), min_occurs=1, max_occurs=1)
    )
spectralTemplate._ContentModel = pyxb.binding.content.ParticleModel(spectralTemplate._GroupModel, min_occurs=1, max_occurs=1)



SPEResults._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), result, scope=SPEResults, documentation=u'The data of the product.'))

SPEResults._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=SPEResults, documentation=u'The generic header of the product.'))
SPEResults._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SPEResults._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SPEResults._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
SPEResults._ContentModel = pyxb.binding.content.ParticleModel(SPEResults._GroupModel, min_occurs=1, max_occurs=None)



SPECalibratedSpectra._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), calibratedSpectrum, scope=SPECalibratedSpectra, documentation=u'The data of the product.'))

SPECalibratedSpectra._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=SPECalibratedSpectra, documentation=u'The generic header of the product.'))
SPECalibratedSpectra._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SPECalibratedSpectra._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SPECalibratedSpectra._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
SPECalibratedSpectra._ContentModel = pyxb.binding.content.ParticleModel(SPECalibratedSpectra._GroupModel, min_occurs=1, max_occurs=None)



SPESpectralTemplates._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=SPESpectralTemplates, documentation=u'The generic header of the product.'))

SPESpectralTemplates._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), spectralTemplate, scope=SPESpectralTemplates, documentation=u'The data of the product.'))
SPESpectralTemplates._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SPESpectralTemplates._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SPESpectralTemplates._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
SPESpectralTemplates._ContentModel = pyxb.binding.content.ParticleModel(SPESpectralTemplates._GroupModel, min_occurs=1, max_occurs=None)



SPESpectralFeatures._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=SPESpectralFeatures, documentation=u'The generic header of the product.'))

SPESpectralFeatures._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), spectralFeature, scope=SPESpectralFeatures, documentation=u'The data of the product.'))
SPESpectralFeatures._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SPESpectralFeatures._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SPESpectralFeatures._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
SPESpectralFeatures._ContentModel = pyxb.binding.content.ParticleModel(SPESpectralFeatures._GroupModel, min_occurs=1, max_occurs=None)



spectralFeature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Type'), pyxb.binding.datatypes.string, scope=spectralFeature, documentation=u"Feature's type :\nA(bsorption) ,\nE(mission) ,\t\t\nB(road)\t,\t\nD(iscontinuity"))

spectralFeature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), pyxb.binding.datatypes.double, scope=spectralFeature, documentation=u'Vacuum Wavelength'))

spectralFeature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flag'), pyxb.binding.datatypes.short, scope=spectralFeature, documentation=u'2 for the strong emission lines from which the redshift will be measured if they are present ; \n1 for weaker emission lines used for check ;\n-1 for strong absorption lines that can be used to measure a z if a continuum is there ; \n0 for those only used to superimpose on a spectrum once a z has been measured ;\n3 for the continuum features (Breaks) '))

spectralFeature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Element'), pyxb.binding.datatypes.string, scope=spectralFeature, documentation=u'Element name'))

spectralFeature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), pyxb.binding.datatypes.string, scope=spectralFeature))
spectralFeature._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectralFeature._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Wavelength')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectralFeature._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Element')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectralFeature._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Type')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectralFeature._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flag')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectralFeature._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), min_occurs=1, max_occurs=1)
    )
spectralFeature._ContentModel = pyxb.binding.content.ParticleModel(spectralFeature._GroupModel, min_occurs=1, max_occurs=1)



calibratedSpectrum._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpectrumData'), calibratedSpectrumData, scope=calibratedSpectrum))
calibratedSpectrum._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'ObjectName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'Coordinates')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'Filename')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'OrigFile')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'Class')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'RangeID')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'TrasmissionCurve')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'Survey')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'Patch')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'Observation')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'Frame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'Exposure')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/spm'), u'Array')), min_occurs=1, max_occurs=1)
    )
calibratedSpectrum._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calibratedSpectrum._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpectrumData')), min_occurs=1, max_occurs=1)
    )
calibratedSpectrum._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calibratedSpectrum._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrum._GroupModel_2, min_occurs=1, max_occurs=1)
    )
calibratedSpectrum._ContentModel = pyxb.binding.content.ParticleModel(calibratedSpectrum._GroupModel, min_occurs=1, max_occurs=1)



result._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpectroscopicRedshift'), redshift, scope=result))

result._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Coordinates'), CommonDM.dm.bas.imp.stc_stub.astroCoordSystem, scope=result))

result._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObjectName'), CommonDM.dm.bas_stub.objectName, scope=result))
result._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(result._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObjectName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(result._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coordinates')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(result._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpectroscopicRedshift')), min_occurs=1, max_occurs=1)
    )
result._ContentModel = pyxb.binding.content.ParticleModel(result._GroupModel, min_occurs=1, max_occurs=1)



calibratedSpectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Noise'), CommonDM.dm.bas.spm_stub.spectrum1DError, scope=calibratedSpectrumData))

calibratedSpectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), CommonDM.dm.bas.spm_stub.spectrum1DData, scope=calibratedSpectrumData))

calibratedSpectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contamination'), CommonDM.dm.bas.spm_stub.spectrum1DData, scope=calibratedSpectrumData))

calibratedSpectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flux'), CommonDM.dm.bas.spm_stub.spectrum1DData, scope=calibratedSpectrumData))

calibratedSpectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PixelQuality'), CommonDM.dm.bas.spm_stub.spectrum1DFlag, scope=calibratedSpectrumData))

calibratedSpectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WavelengthError'), CommonDM.dm.bas.spm_stub.spectrum1DError, scope=calibratedSpectrumData))

calibratedSpectrumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FluxError'), CommonDM.dm.bas.spm_stub.spectrum1DError, scope=calibratedSpectrumData))
calibratedSpectrumData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(calibratedSpectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Wavelength')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WavelengthError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flux')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FluxError')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Noise')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contamination')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(calibratedSpectrumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PixelQuality')), min_occurs=1, max_occurs=1)
    )
calibratedSpectrumData._ContentModel = pyxb.binding.content.ParticleModel(calibratedSpectrumData._GroupModel, min_occurs=1, max_occurs=1)
