# /home/nikoapos/ISDC/Projects/Alexandria/2.0/CommonDM/python/CommonDM/dm/bas/imp_stub.py
# PyXB bindings for NamespaceModule
# NSM:2ed9285e6403c6edceede22f2008b03af2f91840
# Generated 2014-06-12 14:36:51.814178 by PyXB version 1.1.2
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
import CommonDM.dm.bas.imp.stc_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/imp', create_if_missing=True)
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
class coordinateType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The list of designations for coordinates"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coordinateType')
    _Documentation = u'The list of designations for coordinates'
coordinateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=coordinateType, enum_prefix=None)
coordinateType.RA = coordinateType._CF_enumeration.addEnumeration(unicode_value=u'RA')
coordinateType.DEC = coordinateType._CF_enumeration.addEnumeration(unicode_value=u'DEC')
coordinateType._InitializeFacetMap(coordinateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'coordinateType', coordinateType)

# Complex type projectionType with content type ELEMENT_ONLY
class projectionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'projectionType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/imp}ProjectionType uses Python identifier ProjectionType
    __ProjectionType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProjectionType'), 'ProjectionType', '__httpeuclid_esa_orgschemabasimp_projectionType_httpeuclid_esa_orgschemabasimpProjectionType', False)

    
    ProjectionType = property(__ProjectionType.value, __ProjectionType.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/imp}CoordinateType uses Python identifier CoordinateType
    __CoordinateType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CoordinateType'), 'CoordinateType', '__httpeuclid_esa_orgschemabasimp_projectionType_httpeuclid_esa_orgschemabasimpCoordinateType', False)

    
    CoordinateType = property(__CoordinateType.value, __CoordinateType.set, None, None)


    _ElementMap = {
        __ProjectionType.name() : __ProjectionType,
        __CoordinateType.name() : __CoordinateType
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'projectionType', projectionType)




projectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProjectionType'), CommonDM.dm.bas.imp.stc_stub.projection, scope=projectionType))

projectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CoordinateType'), coordinateType, scope=projectionType))
projectionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(projectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CoordinateType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(projectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProjectionType')), min_occurs=1, max_occurs=1)
    )
projectionType._ContentModel = pyxb.binding.content.ParticleModel(projectionType._GroupModel, min_occurs=1, max_occurs=1)
