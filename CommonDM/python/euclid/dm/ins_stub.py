# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/ins_stub.py
# PyXB bindings for NamespaceModule
# NSM:b0796ff167f6d7eb4af7e5fe181d133e7dd0aa4e
# Generated 2014-03-14 09:43:27.463734 by PyXB version 1.1.2
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
import pyxb.binding.datatypes
import euclid.dm.bas.utd_stub
import euclid.dm.bas.dtd_stub
import euclid.dm.bas.mat_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/ins', create_if_missing=True)
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
class detectorId (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Detector Id"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'detectorId')
    _Documentation = u'Detector Id'
detectorId._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=detectorId, enum_prefix=None)
detectorId.n0 = detectorId._CF_enumeration.addEnumeration(unicode_value=u'0')
detectorId._InitializeFacetMap(detectorId._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'detectorId', detectorId)

# Atomic SimpleTypeDefinition
class observationMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """observation modes"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'observationMode')
    _Documentation = u'observation modes'
observationMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=observationMode, enum_prefix=None)
observationMode.ScienceWide = observationMode._CF_enumeration.addEnumeration(unicode_value=u'ScienceWide')
observationMode.ScienceDeep = observationMode._CF_enumeration.addEnumeration(unicode_value=u'ScienceDeep')
observationMode.Calibration = observationMode._CF_enumeration.addEnumeration(unicode_value=u'Calibration')
observationMode.WIDE_SURVEY = observationMode._CF_enumeration.addEnumeration(unicode_value=u'WIDE_SURVEY')
observationMode._InitializeFacetMap(observationMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'observationMode', observationMode)

# Atomic SimpleTypeDefinition
class wavelengthBand (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The wavelength band for which the sky background is calculated. It can take the values "BLUE" and "RED"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wavelengthBand')
    _Documentation = u'The wavelength band for which the sky background is calculated. It can take the values "BLUE" and "RED".'
wavelengthBand._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=wavelengthBand, enum_prefix=None)
wavelengthBand.BLUE = wavelengthBand._CF_enumeration.addEnumeration(unicode_value=u'BLUE')
wavelengthBand.RED = wavelengthBand._CF_enumeration.addEnumeration(unicode_value=u'RED')
wavelengthBand._InitializeFacetMap(wavelengthBand._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'wavelengthBand', wavelengthBand)

# Complex type wavelength with content type ELEMENT_ONLY
class wavelength (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wavelength')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemains_wavelength_httpeuclid_esa_orgschemainsUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemains_wavelength_httpeuclid_esa_orgschemainsValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'wavelength', wavelength)


# Complex type transmissionFactor with content type ELEMENT_ONLY
class transmissionFactor (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'transmissionFactor')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemains_transmissionFactor_httpeuclid_esa_orgschemainsUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemains_transmissionFactor_httpeuclid_esa_orgschemainsValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'transmissionFactor', transmissionFactor)


# Complex type errorOnTransmission with content type ELEMENT_ONLY
class errorOnTransmission (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'errorOnTransmission')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemains_errorOnTransmission_httpeuclid_esa_orgschemainsUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemains_errorOnTransmission_httpeuclid_esa_orgschemainsValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'errorOnTransmission', errorOnTransmission)


# Complex type flux with content type ELEMENT_ONLY
class flux (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'flux')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemains_flux_httpeuclid_esa_orgschemainsUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemains_flux_httpeuclid_esa_orgschemainsValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'flux', flux)


# Complex type insParameter with content type ELEMENT_ONLY
class insParameter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'insParameter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemains_insParameter_httpeuclid_esa_orgschemainsUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins}source uses Python identifier source
    __source = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'source'), 'source', '__httpeuclid_esa_orgschemains_insParameter_httpeuclid_esa_orgschemainssource', False)

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemains_insParameter_httpeuclid_esa_orgschemainsValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __source.name() : __source,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'insParameter', insParameter)


# Complex type insParameterValue with content type ELEMENT_ONLY
class insParameterValue (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'insParameterValue')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins}text uses Python identifier text
    __text = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'text'), 'text', '__httpeuclid_esa_orgschemains_insParameterValue_httpeuclid_esa_orgschemainstext', False)

    
    text = property(__text.value, __text.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins}polynomial uses Python identifier polynomial
    __polynomial = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'polynomial'), 'polynomial', '__httpeuclid_esa_orgschemains_insParameterValue_httpeuclid_esa_orgschemainspolynomial', False)

    
    polynomial = property(__polynomial.value, __polynomial.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins}list uses Python identifier list
    __list = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'list'), 'list', '__httpeuclid_esa_orgschemains_insParameterValue_httpeuclid_esa_orgschemainslist', False)

    
    list = property(__list.value, __list.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins}double uses Python identifier double
    __double = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'double'), 'double', '__httpeuclid_esa_orgschemains_insParameterValue_httpeuclid_esa_orgschemainsdouble', False)

    
    double = property(__double.value, __double.set, None, None)


    _ElementMap = {
        __text.name() : __text,
        __polynomial.name() : __polynomial,
        __list.name() : __list,
        __double.name() : __double
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'insParameterValue', insParameterValue)


# Complex type noise with content type ELEMENT_ONLY
class noise (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'noise')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemains_noise_httpeuclid_esa_orgschemainsUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemains_noise_httpeuclid_esa_orgschemainsValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'noise', noise)




wavelength._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), euclid.dm.bas.utd_stub.unit, scope=wavelength))

wavelength._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), euclid.dm.bas.dtd_stub.listOfDouble, scope=wavelength))
wavelength._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(wavelength._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(wavelength._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
wavelength._ContentModel = pyxb.binding.content.ParticleModel(wavelength._GroupModel, min_occurs=1, max_occurs=1)



transmissionFactor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), euclid.dm.bas.utd_stub.unit, scope=transmissionFactor))

transmissionFactor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), euclid.dm.bas.dtd_stub.listOfDouble, scope=transmissionFactor))
transmissionFactor._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(transmissionFactor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(transmissionFactor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
transmissionFactor._ContentModel = pyxb.binding.content.ParticleModel(transmissionFactor._GroupModel, min_occurs=1, max_occurs=1)



errorOnTransmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), euclid.dm.bas.utd_stub.unit, scope=errorOnTransmission))

errorOnTransmission._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), euclid.dm.bas.dtd_stub.listOfDouble, scope=errorOnTransmission))
errorOnTransmission._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(errorOnTransmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(errorOnTransmission._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
errorOnTransmission._ContentModel = pyxb.binding.content.ParticleModel(errorOnTransmission._GroupModel, min_occurs=1, max_occurs=1)



flux._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), euclid.dm.bas.utd_stub.unit, scope=flux))

flux._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), euclid.dm.bas.dtd_stub.listOfDouble, scope=flux))
flux._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(flux._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(flux._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
flux._ContentModel = pyxb.binding.content.ParticleModel(flux._GroupModel, min_occurs=1, max_occurs=1)



insParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), euclid.dm.bas.utd_stub.unit, scope=insParameter))

insParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source'), pyxb.binding.datatypes.string, scope=insParameter))

insParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), insParameterValue, scope=insParameter))
insParameter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(insParameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(insParameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(insParameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
insParameter._ContentModel = pyxb.binding.content.ParticleModel(insParameter._GroupModel, min_occurs=1, max_occurs=1)



insParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'text'), pyxb.binding.datatypes.string, scope=insParameterValue))

insParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'polynomial'), euclid.dm.bas.mat_stub.varXpolynomialModel, scope=insParameterValue))

insParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'list'), euclid.dm.bas.dtd_stub.listOfDouble, scope=insParameterValue))

insParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'double'), pyxb.binding.datatypes.double, scope=insParameterValue))
insParameterValue._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(insParameterValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'text')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(insParameterValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'double')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(insParameterValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'list')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(insParameterValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'polynomial')), min_occurs=1, max_occurs=1)
    )
insParameterValue._ContentModel = pyxb.binding.content.ParticleModel(insParameterValue._GroupModel, min_occurs=1, max_occurs=1)



noise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), euclid.dm.bas.utd_stub.unit, scope=noise))

noise._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), euclid.dm.bas.dtd_stub.listOfDouble, scope=noise))
noise._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(noise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(noise._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
noise._ContentModel = pyxb.binding.content.ParticleModel(noise._GroupModel, min_occurs=1, max_occurs=1)
