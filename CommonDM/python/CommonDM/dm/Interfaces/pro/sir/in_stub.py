# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/Interfaces/pro/sir/in_stub.py
# PyXB bindings for NamespaceModule
# NSM:e2b8695628fe894ba26bb65e75625907c4e1d81b
# Generated 2014-03-17 18:50:36.642024 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:a3e7637c-adfc-11e3-9f2e-c4d98710dc86')

# Import bindings for namespaces imported into schema
import CommonDM.dm.pro.sir_mockup_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/Interfaces/pro/sir/in', create_if_missing=True)
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


OutputCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OutputCatalog'), CommonDM.dm.pro.sir_mockup_stub.outputCatalog)
Namespace.addCategoryObject('elementBinding', OutputCatalog.name().localName(), OutputCatalog)

InputImage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InputImage'), CommonDM.dm.pro.sir_mockup_stub.nispImage)
Namespace.addCategoryObject('elementBinding', InputImage.name().localName(), InputImage)

InputCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InputCatalog'), CommonDM.dm.pro.sir_mockup_stub.parentCatalog)
Namespace.addCategoryObject('elementBinding', InputCatalog.name().localName(), InputCatalog)

InputParameters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InputParameters'), CommonDM.dm.pro.sir_mockup_stub.inputParameters)
Namespace.addCategoryObject('elementBinding', InputParameters.name().localName(), InputParameters)
