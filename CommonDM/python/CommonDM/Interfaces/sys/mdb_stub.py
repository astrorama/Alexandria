# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/Interfaces/sys/mdb_stub.py
# PyXB bindings for NamespaceModule
# NSM:fc10a69a6a2395443e180d74c59da8c7fc1ebf16
# Generated 2014-03-14 15:21:54.445053 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:fcce2776-ab83-11e3-b899-c4d98710dc86')

# Import bindings for namespaces imported into schema
import CommonDM.sys.mdb_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/Interfaces/sys/mdb', create_if_missing=True)
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


MissionDataBaseSetOfParameters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MissionDataBaseSetOfParameters'), CommonDM.sys.mdb_stub.missionDataBaseSetOfParameters)
Namespace.addCategoryObject('elementBinding', MissionDataBaseSetOfParameters.name().localName(), MissionDataBaseSetOfParameters)
