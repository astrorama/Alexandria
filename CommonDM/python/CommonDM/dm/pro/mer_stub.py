# /home/nikoapos/ISDC/Projects/Alexandria/2.0/CommonDM/python/CommonDM/dm/pro/mer_stub.py
# PyXB bindings for NamespaceModule
# NSM:db4a3ca9e083d26546786acafbe4eee2e4de7bb1
# Generated 2014-06-12 14:36:51.813941 by PyXB version 1.1.2
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
import CommonDM.dm.bas.fit_stub
import CommonDM.dm.bas.dtd_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/mer', create_if_missing=True)
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


# Complex type VIScalibratedImages with content type ELEMENT_ONLY
class VIScalibratedImages (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VIScalibratedImages')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element VIScalibratedImage uses Python identifier VIScalibratedImage
    __VIScalibratedImage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'VIScalibratedImage'), 'VIScalibratedImage', '__httpeuclid_esa_orgschemapromer_VIScalibratedImages_VIScalibratedImage', False)

    
    VIScalibratedImage = property(__VIScalibratedImage.value, __VIScalibratedImage.set, None, None)

    
    # Element depth uses Python identifier depth
    __depth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'depth'), 'depth', '__httpeuclid_esa_orgschemapromer_VIScalibratedImages_depth', False)

    
    depth = property(__depth.value, __depth.set, None, None)


    _ElementMap = {
        __VIScalibratedImage.name() : __VIScalibratedImage,
        __depth.name() : __depth
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'VIScalibratedImages', VIScalibratedImages)




VIScalibratedImages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'VIScalibratedImage'), CommonDM.dm.bas.fit_stub.fitsFile, scope=VIScalibratedImages))

VIScalibratedImages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'depth'), CommonDM.dm.bas.dtd_stub.double1Type, scope=VIScalibratedImages))
VIScalibratedImages._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(VIScalibratedImages._UseForTag(pyxb.namespace.ExpandedName(None, u'depth')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(VIScalibratedImages._UseForTag(pyxb.namespace.ExpandedName(None, u'VIScalibratedImage')), min_occurs=1, max_occurs=1)
    )
VIScalibratedImages._ContentModel = pyxb.binding.content.ParticleModel(VIScalibratedImages._GroupModel, min_occurs=1, max_occurs=1)
