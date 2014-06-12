# /home/nikoapos/ISDC/Projects/Alexandria/2.0/CommonDM/python/CommonDM/dm/sys/tsk_schema_stub.py
# PyXB bindings for NamespaceModule
# NSM:8ed31b84105a7061a176a4a58392bf2784b9a287
# Generated 2014-06-12 14:36:51.815973 by PyXB version 1.1.2
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
import CommonDM.dm.sys.tsk_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/sys/tsk-schema', create_if_missing=True)
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


PackageDef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PackageDef'), CommonDM.dm.sys.tsk_stub.packageDefinition)
Namespace.addCategoryObject('elementBinding', PackageDef.name().localName(), PackageDef)

PipelineDef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PipelineDef'), CommonDM.dm.sys.tsk_stub.pipelineDefinition)
Namespace.addCategoryObject('elementBinding', PipelineDef.name().localName(), PipelineDef)
