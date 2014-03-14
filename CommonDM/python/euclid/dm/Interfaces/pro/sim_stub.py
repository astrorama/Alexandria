# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/Interfaces/pro/sim_stub.py
# PyXB bindings for NamespaceModule
# NSM:597a9d3938750139e92466200f1278b1a9dd9acd
# Generated 2014-03-14 09:43:27.465449 by PyXB version 1.1.2
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
import euclid.dm.pro.sim_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/Interfaces/pro/sim', create_if_missing=True)
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


TipsInputConfiguration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipsInputConfiguration'), euclid.dm.pro.sim_stub.tipsInputConfiguration)
Namespace.addCategoryObject('elementBinding', TipsInputConfiguration.name().localName(), TipsInputConfiguration)

NipInputConfiguration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NipInputConfiguration'), euclid.dm.pro.sim_stub.nipInputConfiguration)
Namespace.addCategoryObject('elementBinding', NipInputConfiguration.name().localName(), NipInputConfiguration)

TipsOutput = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipsOutput'), euclid.dm.pro.sim_stub.metadataVISNISPSimulationInterfaces)
Namespace.addCategoryObject('elementBinding', TipsOutput.name().localName(), TipsOutput)

VisInputConfiguration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VisInputConfiguration'), euclid.dm.pro.sim_stub.visInputConfiguration)
Namespace.addCategoryObject('elementBinding', VisInputConfiguration.name().localName(), VisInputConfiguration)

NipOutput = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NipOutput'), euclid.dm.pro.sim_stub.nipOutput)
Namespace.addCategoryObject('elementBinding', NipOutput.name().localName(), NipOutput)
