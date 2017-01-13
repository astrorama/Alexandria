# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/sys/ial-schema_stub.py
# PyXB bindings for NamespaceModule
# NSM:7b32b549ba1ef428108ac1d1711bd9c5e64f1a53
# Generated 2014-03-17 11:53:47.253885 by PyXB version 1.1.2
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
import CommonDM.dm.sys.ial_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/sys/ial-schema', create_if_missing=True)
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


TaskRun = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TaskRun'), CommonDM.dm.sys.ial_stub.pipelineTaskRun)
Namespace.addCategoryObject('elementBinding', TaskRun.name().localName(), TaskRun)

TaskProducts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TaskProducts'), CommonDM.dm.sys.ial_stub.taskProductList)
Namespace.addCategoryObject('elementBinding', TaskProducts.name().localName(), TaskProducts)

PPO = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PPO'), CommonDM.dm.sys.ial_stub.sgsProcessingOrder)
Namespace.addCategoryObject('elementBinding', PPO.name().localName(), PPO)

IalConfig = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IalConfig'), CommonDM.dm.sys.ial_stub.ialConfiguration)
Namespace.addCategoryObject('elementBinding', IalConfig.name().localName(), IalConfig)

TriggerData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TriggerData'), CommonDM.dm.sys.ial_stub.triggeringData)
Namespace.addCategoryObject('elementBinding', TriggerData.name().localName(), TriggerData)

Run = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Run'), CommonDM.dm.sys.ial_stub.pipelineRun)
Namespace.addCategoryObject('elementBinding', Run.name().localName(), Run)

ClusterConfig = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClusterConfig'), CommonDM.dm.sys.ial_stub.clusterConfiguration)
Namespace.addCategoryObject('elementBinding', ClusterConfig.name().localName(), ClusterConfig)
