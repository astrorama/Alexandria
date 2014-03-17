# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/pro/sir-mockup_stub.py
# PyXB bindings for NamespaceModule
# NSM:7377929d2e4063e13e3254db56c66c4116c61fe3
# Generated 2014-03-17 11:53:47.253995 by PyXB version 1.1.2
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
import CommonDM.dm.sys.sgs_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/sir-mockup', create_if_missing=True)
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
class stellarSpectralType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'stellarSpectralType')
    _Documentation = None
stellarSpectralType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stellarSpectralType, enum_prefix=None)
stellarSpectralType.O = stellarSpectralType._CF_enumeration.addEnumeration(unicode_value=u'O')
stellarSpectralType.B = stellarSpectralType._CF_enumeration.addEnumeration(unicode_value=u'B')
stellarSpectralType.A = stellarSpectralType._CF_enumeration.addEnumeration(unicode_value=u'A')
stellarSpectralType.F = stellarSpectralType._CF_enumeration.addEnumeration(unicode_value=u'F')
stellarSpectralType.G = stellarSpectralType._CF_enumeration.addEnumeration(unicode_value=u'G')
stellarSpectralType.K = stellarSpectralType._CF_enumeration.addEnumeration(unicode_value=u'K')
stellarSpectralType.M = stellarSpectralType._CF_enumeration.addEnumeration(unicode_value=u'M')
stellarSpectralType._InitializeFacetMap(stellarSpectralType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'stellarSpectralType', stellarSpectralType)

# Atomic SimpleTypeDefinition
class offset (pyxb.binding.datatypes.float):

    """The zero-order expected offset"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'offset')
    _Documentation = u'The zero-order expected offset'
offset._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'offset', offset)

# Atomic SimpleTypeDefinition
class border (pyxb.binding.datatypes.integer):

    """The extra pixels added to the search window"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'border')
    _Documentation = u'The extra pixels added to the search window'
border._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'border', border)

# Complex type outputCatalog with content type ELEMENT_ONLY
class outputCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'outputCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sir-mockup}Magnitude uses Python identifier Magnitude
    __Magnitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Magnitude'), 'Magnitude', '__httpeuclid_esa_orgschemaprosir_mockup_outputCatalog_httpeuclid_esa_orgschemaprosir_mockupMagnitude', False)

    
    Magnitude = property(__Magnitude.value, __Magnitude.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sir-mockup}DataContainer uses Python identifier DataContainer
    __DataContainer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataContainer'), 'DataContainer', '__httpeuclid_esa_orgschemaprosir_mockup_outputCatalog_httpeuclid_esa_orgschemaprosir_mockupDataContainer', False)

    
    DataContainer = property(__DataContainer.value, __DataContainer.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sir-mockup}StellarSpectralType uses Python identifier StellarSpectralType
    __StellarSpectralType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StellarSpectralType'), 'StellarSpectralType', '__httpeuclid_esa_orgschemaprosir_mockup_outputCatalog_httpeuclid_esa_orgschemaprosir_mockupStellarSpectralType', False)

    
    StellarSpectralType = property(__StellarSpectralType.value, __StellarSpectralType.set, None, None)


    _ElementMap = {
        __Magnitude.name() : __Magnitude,
        __DataContainer.name() : __DataContainer,
        __StellarSpectralType.name() : __StellarSpectralType
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'outputCatalog', outputCatalog)


# Complex type nispImage with content type ELEMENT_ONLY
class nispImage (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nispImage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DataContainer uses Python identifier DataContainer
    __DataContainer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'DataContainer'), 'DataContainer', '__httpeuclid_esa_orgschemaprosir_mockup_nispImage_DataContainer', False)

    
    DataContainer = property(__DataContainer.value, __DataContainer.set, None, None)


    _ElementMap = {
        __DataContainer.name() : __DataContainer
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nispImage', nispImage)


# Complex type parentCatalog with content type ELEMENT_ONLY
class parentCatalog (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'parentCatalog')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DataContainer uses Python identifier DataContainer
    __DataContainer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'DataContainer'), 'DataContainer', '__httpeuclid_esa_orgschemaprosir_mockup_parentCatalog_DataContainer', False)

    
    DataContainer = property(__DataContainer.value, __DataContainer.set, None, None)


    _ElementMap = {
        __DataContainer.name() : __DataContainer
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'parentCatalog', parentCatalog)


# Complex type inputParameters with content type ELEMENT_ONLY
class inputParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'inputParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/sir-mockup}Offset uses Python identifier Offset
    __Offset = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Offset'), 'Offset', '__httpeuclid_esa_orgschemaprosir_mockup_inputParameters_httpeuclid_esa_orgschemaprosir_mockupOffset', False)

    
    Offset = property(__Offset.value, __Offset.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/sir-mockup}Border uses Python identifier Border
    __Border = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Border'), 'Border', '__httpeuclid_esa_orgschemaprosir_mockup_inputParameters_httpeuclid_esa_orgschemaprosir_mockupBorder', False)

    
    Border = property(__Border.value, __Border.set, None, None)


    _ElementMap = {
        __Offset.name() : __Offset,
        __Border.name() : __Border
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'inputParameters', inputParameters)




outputCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Magnitude'), pyxb.binding.datatypes.float, scope=outputCatalog))

outputCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataContainer'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=outputCatalog))

outputCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StellarSpectralType'), stellarSpectralType, scope=outputCatalog))
outputCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(outputCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataContainer')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(outputCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StellarSpectralType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(outputCatalog._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Magnitude')), min_occurs=1, max_occurs=1)
    )
outputCatalog._ContentModel = pyxb.binding.content.ParticleModel(outputCatalog._GroupModel, min_occurs=1, max_occurs=1)



nispImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'DataContainer'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=nispImage))
nispImage._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nispImage._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
nispImage._ContentModel = pyxb.binding.content.ParticleModel(nispImage._GroupModel, min_occurs=1, max_occurs=1)



parentCatalog._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'DataContainer'), CommonDM.dm.sys.sgs_stub.dataContainer, scope=parentCatalog))
parentCatalog._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(parentCatalog._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
parentCatalog._ContentModel = pyxb.binding.content.ParticleModel(parentCatalog._GroupModel, min_occurs=1, max_occurs=1)



inputParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Offset'), offset, scope=inputParameters))

inputParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Border'), border, scope=inputParameters))
inputParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(inputParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Border')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(inputParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Offset')), min_occurs=1, max_occurs=1)
    )
inputParameters._ContentModel = pyxb.binding.content.ParticleModel(inputParameters._GroupModel, min_occurs=1, max_occurs=1)
