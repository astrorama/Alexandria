# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/dpd/ext_stub.py
# PyXB bindings for NamespaceModule
# NSM:c41bdd9aa0398bba4f9b269d9446297ad51ac9cc
# Generated 2014-03-17 11:53:47.252185 by PyXB version 1.1.2
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
import CommonDM.dm.pro.ext_stub
import CommonDM.dm.sys_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/dpd/ext', create_if_missing=True)
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


# Complex type dpCoaddedRegriddedFrame with content type ELEMENT_ONLY
class dpCoaddedRegriddedFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dpCoaddedRegriddedFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/dpd/ext}Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Data'), 'Data', '__httpeuclid_esa_orgschemadpdext_dpCoaddedRegriddedFrame_httpeuclid_esa_orgschemadpdextData', False)

    
    Data = property(__Data.value, __Data.set, None, None)

    
    # Element {http://euclid.esa.org/schema/dpd/ext}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Header'), 'Header', '__httpeuclid_esa_orgschemadpdext_dpCoaddedRegriddedFrame_httpeuclid_esa_orgschemadpdextHeader', False)

    
    Header = property(__Header.value, __Header.set, None, u'Generic Header as specified in /sys')


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'dpCoaddedRegriddedFrame', dpCoaddedRegriddedFrame)




dpCoaddedRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Data'), CommonDM.dm.pro.ext_stub.coaddedRegriddedFrame, scope=dpCoaddedRegriddedFrame))

dpCoaddedRegriddedFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Header'), CommonDM.dm.sys_stub.genericHeader, scope=dpCoaddedRegriddedFrame, documentation=u'Generic Header as specified in /sys'))
dpCoaddedRegriddedFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(dpCoaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dpCoaddedRegriddedFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Data')), min_occurs=1, max_occurs=1)
    )
dpCoaddedRegriddedFrame._ContentModel = pyxb.binding.content.ParticleModel(dpCoaddedRegriddedFrame._GroupModel, min_occurs=1, max_occurs=1)
