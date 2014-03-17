# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/ins/sky_stub.py
# PyXB bindings for NamespaceModule
# NSM:c511641e3e4c1554081270b88567f44db67597db
# Generated 2014-03-17 11:53:47.256876 by PyXB version 1.1.2
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
import CommonDM.dm.bas.utd_stub
import CommonDM.dm.bas.img_stub
import CommonDM.dm.ins_stub
import CommonDM.dm.bas.dtd_stub
import CommonDM.dm.bas.fit_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/ins/sky', create_if_missing=True)
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
class model (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'model')
    _Documentation = None
model._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=model, enum_prefix=None)
model.Aldering = model._CF_enumeration.addEnumeration(unicode_value=u'Aldering')
model._InitializeFacetMap(model._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'model', model)

# Complex type galacticAbsorption with content type ELEMENT_ONLY
class galacticAbsorption (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'galacticAbsorption')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/sky}Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Model'), 'Model', '__httpeuclid_esa_orgschemainssky_galacticAbsorption_httpeuclid_esa_orgschemainsskyModel', False)

    
    Model = property(__Model.value, __Model.set, None, u'The name of the model used to compute the Galactic absorption.')

    
    # Element {http://euclid.esa.org/schema/ins/sky}AbsorptionFactors uses Python identifier AbsorptionFactors
    __AbsorptionFactors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AbsorptionFactors'), 'AbsorptionFactors', '__httpeuclid_esa_orgschemainssky_galacticAbsorption_httpeuclid_esa_orgschemainsskyAbsorptionFactors', False)

    
    AbsorptionFactors = property(__AbsorptionFactors.value, __AbsorptionFactors.set, None, u'A Binary FITS table containing the calculated absoption factors for different wavelengths. The factors get values from 0 to 1 (inclusive).')

    
    # Element {http://euclid.esa.org/schema/ins/sky}GalaxyLongitude uses Python identifier GalaxyLongitude
    __GalaxyLongitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GalaxyLongitude'), 'GalaxyLongitude', '__httpeuclid_esa_orgschemainssky_galacticAbsorption_httpeuclid_esa_orgschemainsskyGalaxyLongitude', False)

    
    GalaxyLongitude = property(__GalaxyLongitude.value, __GalaxyLongitude.set, None, u'The galaxy longitude parameter of the galactic model.')

    
    # Element {http://euclid.esa.org/schema/ins/sky}GalaxyLatitude uses Python identifier GalaxyLatitude
    __GalaxyLatitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GalaxyLatitude'), 'GalaxyLatitude', '__httpeuclid_esa_orgschemainssky_galacticAbsorption_httpeuclid_esa_orgschemainsskyGalaxyLatitude', False)

    
    GalaxyLatitude = property(__GalaxyLatitude.value, __GalaxyLatitude.set, None, u'The galaxy latitude parameter of the galactic model.')


    _ElementMap = {
        __Model.name() : __Model,
        __AbsorptionFactors.name() : __AbsorptionFactors,
        __GalaxyLongitude.name() : __GalaxyLongitude,
        __GalaxyLatitude.name() : __GalaxyLatitude
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'galacticAbsorption', galacticAbsorption)


# Complex type backgroundMap with content type ELEMENT_ONLY
class backgroundMap (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'backgroundMap')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/sky}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemainssky_backgroundMap_httpeuclid_esa_orgschemainsskyUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/sky}Image uses Python identifier Image
    __Image = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Image'), 'Image', '__httpeuclid_esa_orgschemainssky_backgroundMap_httpeuclid_esa_orgschemainsskyImage', False)

    
    Image = property(__Image.value, __Image.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Image.name() : __Image
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'backgroundMap', backgroundMap)


# Complex type skyBackground with content type ELEMENT_ONLY
class skyBackground (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'skyBackground')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/sky}EclipticLatitude uses Python identifier EclipticLatitude
    __EclipticLatitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EclipticLatitude'), 'EclipticLatitude', '__httpeuclid_esa_orgschemainssky_skyBackground_httpeuclid_esa_orgschemainsskyEclipticLatitude', False)

    
    EclipticLatitude = property(__EclipticLatitude.value, __EclipticLatitude.set, None, u'The ecliptic latitude parameter of the sky background model.')

    
    # Element {http://euclid.esa.org/schema/ins/sky}BackgroundList uses Python identifier BackgroundList
    __BackgroundList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BackgroundList'), 'BackgroundList', '__httpeuclid_esa_orgschemainssky_skyBackground_httpeuclid_esa_orgschemainsskyBackgroundList', True)

    
    BackgroundList = property(__BackgroundList.value, __BackgroundList.set, None, u'A list with the sky backgrounds for the different detectors.')

    
    # Element {http://euclid.esa.org/schema/ins/sky}Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Model'), 'Model', '__httpeuclid_esa_orgschemainssky_skyBackground_httpeuclid_esa_orgschemainsskyModel', False)

    
    Model = property(__Model.value, __Model.set, None, u'The name of the model used to compute the sky background.')

    
    # Element {http://euclid.esa.org/schema/ins/sky}EclipticLongitude uses Python identifier EclipticLongitude
    __EclipticLongitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EclipticLongitude'), 'EclipticLongitude', '__httpeuclid_esa_orgschemainssky_skyBackground_httpeuclid_esa_orgschemainsskyEclipticLongitude', False)

    
    EclipticLongitude = property(__EclipticLongitude.value, __EclipticLongitude.set, None, u'The ecliptic longitude parameter of the sky background model.')

    
    # Element {http://euclid.esa.org/schema/ins/sky}WavelengthBand uses Python identifier WavelengthBand
    __WavelengthBand = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WavelengthBand'), 'WavelengthBand', '__httpeuclid_esa_orgschemainssky_skyBackground_httpeuclid_esa_orgschemainsskyWavelengthBand', False)

    
    WavelengthBand = property(__WavelengthBand.value, __WavelengthBand.set, None, None)


    _ElementMap = {
        __EclipticLatitude.name() : __EclipticLatitude,
        __BackgroundList.name() : __BackgroundList,
        __Model.name() : __Model,
        __EclipticLongitude.name() : __EclipticLongitude,
        __WavelengthBand.name() : __WavelengthBand
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'skyBackground', skyBackground)


# Complex type skyCoordinate with content type ELEMENT_ONLY
class skyCoordinate (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'skyCoordinate')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/sky}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemainssky_skyCoordinate_httpeuclid_esa_orgschemainsskyUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/sky}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemainssky_skyCoordinate_httpeuclid_esa_orgschemainsskyValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'skyCoordinate', skyCoordinate)


# Complex type background with content type ELEMENT_ONLY
class background (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'background')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/sky}Nx uses Python identifier Nx
    __Nx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Nx'), 'Nx', '__httpeuclid_esa_orgschemainssky_background_httpeuclid_esa_orgschemainsskyNx', False)

    
    Nx = property(__Nx.value, __Nx.set, None, u'The number of pixels of the detector in X direction.')

    
    # Element {http://euclid.esa.org/schema/ins/sky}Ny uses Python identifier Ny
    __Ny = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ny'), 'Ny', '__httpeuclid_esa_orgschemainssky_background_httpeuclid_esa_orgschemainsskyNy', False)

    
    Ny = property(__Ny.value, __Ny.set, None, u'The number of pixels of the detector in Y direction.')

    
    # Element {http://euclid.esa.org/schema/ins/sky}BackgroundMap uses Python identifier BackgroundMap
    __BackgroundMap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BackgroundMap'), 'BackgroundMap', '__httpeuclid_esa_orgschemainssky_background_httpeuclid_esa_orgschemainsskyBackgroundMap', False)

    
    BackgroundMap = property(__BackgroundMap.value, __BackgroundMap.set, None, u'The detectors simulated sky background, expressed in photon/s/cm2.')

    
    # Element {http://euclid.esa.org/schema/ins/sky}detectorIdentifier uses Python identifier detectorIdentifier
    __detectorIdentifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'detectorIdentifier'), 'detectorIdentifier', '__httpeuclid_esa_orgschemainssky_background_httpeuclid_esa_orgschemainsskydetectorIdentifier', False)

    
    detectorIdentifier = property(__detectorIdentifier.value, __detectorIdentifier.set, None, u'The identifier of the detector')


    _ElementMap = {
        __Nx.name() : __Nx,
        __Ny.name() : __Ny,
        __BackgroundMap.name() : __BackgroundMap,
        __detectorIdentifier.name() : __detectorIdentifier
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'background', background)


# Complex type nPix with content type ELEMENT_ONLY
class nPix (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nPix')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/sky}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemainssky_nPix_httpeuclid_esa_orgschemainsskyUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/sky}NPix uses Python identifier NPix
    __NPix = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NPix'), 'NPix', '__httpeuclid_esa_orgschemainssky_nPix_httpeuclid_esa_orgschemainsskyNPix', False)

    
    NPix = property(__NPix.value, __NPix.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __NPix.name() : __NPix
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nPix', nPix)


# Complex type absorptionFactors with content type ELEMENT_ONLY
class absorptionFactors (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'absorptionFactors')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'sky.absorptionFactors', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'absorptionFactors', absorptionFactors)




galacticAbsorption._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Model'), model, scope=galacticAbsorption, documentation=u'The name of the model used to compute the Galactic absorption.'))

galacticAbsorption._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AbsorptionFactors'), absorptionFactors, scope=galacticAbsorption, documentation=u'A Binary FITS table containing the calculated absoption factors for different wavelengths. The factors get values from 0 to 1 (inclusive).'))

galacticAbsorption._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GalaxyLongitude'), skyCoordinate, scope=galacticAbsorption, documentation=u'The galaxy longitude parameter of the galactic model.'))

galacticAbsorption._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GalaxyLatitude'), skyCoordinate, scope=galacticAbsorption, documentation=u'The galaxy latitude parameter of the galactic model.'))
galacticAbsorption._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(galacticAbsorption._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Model')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galacticAbsorption._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GalaxyLatitude')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galacticAbsorption._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GalaxyLongitude')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(galacticAbsorption._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AbsorptionFactors')), min_occurs=1, max_occurs=1)
    )
galacticAbsorption._ContentModel = pyxb.binding.content.ParticleModel(galacticAbsorption._GroupModel, min_occurs=1, max_occurs=1)



backgroundMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=backgroundMap))

backgroundMap._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Image'), CommonDM.dm.bas.img_stub.baseFrame, scope=backgroundMap))
backgroundMap._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(backgroundMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Image')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(backgroundMap._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
backgroundMap._ContentModel = pyxb.binding.content.ParticleModel(backgroundMap._GroupModel, min_occurs=1, max_occurs=1)



skyBackground._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EclipticLatitude'), skyCoordinate, scope=skyBackground, documentation=u'The ecliptic latitude parameter of the sky background model.'))

skyBackground._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BackgroundList'), background, scope=skyBackground, documentation=u'A list with the sky backgrounds for the different detectors.'))

skyBackground._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Model'), model, scope=skyBackground, documentation=u'The name of the model used to compute the sky background.'))

skyBackground._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EclipticLongitude'), skyCoordinate, scope=skyBackground, documentation=u'The ecliptic longitude parameter of the sky background model.'))

skyBackground._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WavelengthBand'), CommonDM.dm.ins_stub.wavelengthBand, scope=skyBackground))
skyBackground._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(skyBackground._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Model')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(skyBackground._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EclipticLatitude')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(skyBackground._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EclipticLongitude')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(skyBackground._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WavelengthBand')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(skyBackground._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BackgroundList')), min_occurs=1L, max_occurs=None)
    )
skyBackground._ContentModel = pyxb.binding.content.ParticleModel(skyBackground._GroupModel, min_occurs=1, max_occurs=1)



skyCoordinate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=skyCoordinate))

skyCoordinate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), CommonDM.dm.bas.dtd_stub.degAngle, scope=skyCoordinate))
skyCoordinate._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(skyCoordinate._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(skyCoordinate._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
skyCoordinate._ContentModel = pyxb.binding.content.ParticleModel(skyCoordinate._GroupModel, min_occurs=1, max_occurs=1)



background._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Nx'), nPix, scope=background, documentation=u'The number of pixels of the detector in X direction.'))

background._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ny'), nPix, scope=background, documentation=u'The number of pixels of the detector in Y direction.'))

background._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BackgroundMap'), backgroundMap, scope=background, documentation=u'The detectors simulated sky background, expressed in photon/s/cm2.'))

background._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'detectorIdentifier'), CommonDM.dm.ins_stub.detectorId, scope=background, documentation=u'The identifier of the detector'))
background._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(background._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Nx')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(background._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ny')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(background._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BackgroundMap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(background._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'detectorIdentifier')), min_occurs=1, max_occurs=1)
    )
background._ContentModel = pyxb.binding.content.ParticleModel(background._GroupModel, min_occurs=1, max_occurs=1)



nPix._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=nPix))

nPix._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NPix'), pyxb.binding.datatypes.short, scope=nPix))
nPix._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nPix._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NPix')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nPix._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
nPix._ContentModel = pyxb.binding.content.ParticleModel(nPix._GroupModel, min_occurs=1, max_occurs=1)


absorptionFactors._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(absorptionFactors._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
absorptionFactors._ContentModel = pyxb.binding.content.ParticleModel(absorptionFactors._GroupModel, min_occurs=1, max_occurs=1)
