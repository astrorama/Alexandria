# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/Interfaces/pro/vis_stub.py
# PyXB bindings for NamespaceModule
# NSM:539c73c8f73a663b381cbefc2c790f5c063cac08
# Generated 2014-03-17 11:53:47.256588 by PyXB version 1.1.2
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
import CommonDM.dm.pro.vis_stub
import CommonDM.dm.pro.sim_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/Interfaces/pro/vis', create_if_missing=True)
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


# Complex type BiasInput with content type ELEMENT_ONLY
class BiasInput (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BiasInput')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/Interfaces/pro/vis}Master uses Python identifier Master
    __Master = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Master'), 'Master', '__httpeuclid_esa_orgschemaInterfacesprovis_BiasInput_httpeuclid_esa_orgschemaInterfacesprovisMaster', False)

    
    Master = property(__Master.value, __Master.set, None, None)

    
    # Element {http://euclid.esa.org/schema/Interfaces/pro/vis}Bias uses Python identifier Bias
    __Bias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Bias'), 'Bias', '__httpeuclid_esa_orgschemaInterfacesprovis_BiasInput_httpeuclid_esa_orgschemaInterfacesprovisBias', False)

    
    Bias = property(__Bias.value, __Bias.set, None, None)


    _ElementMap = {
        __Master.name() : __Master,
        __Bias.name() : __Bias
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'BiasInput', BiasInput)


SimInputConfiguration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimInputConfiguration'), CommonDM.dm.pro.sim_stub.visInputConfiguration)
Namespace.addCategoryObject('elementBinding', SimInputConfiguration.name().localName(), SimInputConfiguration)

VisInputConfiguration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VisInputConfiguration'), CommonDM.dm.pro.vis_stub.visBaseFrame)
Namespace.addCategoryObject('elementBinding', VisInputConfiguration.name().localName(), VisInputConfiguration)

GainLinearityInputConfiguration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GainLinearityInputConfiguration'), CommonDM.dm.pro.vis_stub.gainLinearity)
Namespace.addCategoryObject('elementBinding', GainLinearityInputConfiguration.name().localName(), GainLinearityInputConfiguration)

BiasInputConfiguration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BiasInputConfiguration'), BiasInput)
Namespace.addCategoryObject('elementBinding', BiasInputConfiguration.name().localName(), BiasInputConfiguration)



BiasInput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Master'), CommonDM.dm.pro.vis_stub.masterFlatFrame, scope=BiasInput))

BiasInput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bias'), CommonDM.dm.pro.vis_stub.biasFrame, scope=BiasInput))
BiasInput._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(BiasInput._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bias')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(BiasInput._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Master')), min_occurs=1, max_occurs=1)
    )
BiasInput._ContentModel = pyxb.binding.content.ParticleModel(BiasInput._GroupModel, min_occurs=1, max_occurs=1)
