# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/sys/ial_stub.py
# PyXB bindings for NamespaceModule
# NSM:14b174fbf2463221ba40c6210b8bbc1f0cac46a0
# Generated 2014-03-14 15:21:54.443495 by PyXB version 1.1.2
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
import pyxb.binding.datatypes
import CommonDM.sys.sgs_stub
import CommonDM.sys_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/sys/ial', create_if_missing=True)
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
class processingOrderState (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                Enumeration that indicates the state the processing order. 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'processingOrderState')
    _Documentation = u'\n                Enumeration that indicates the state the processing order. \n            '
processingOrderState._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=processingOrderState, enum_prefix=None)
processingOrderState.NEW = processingOrderState._CF_enumeration.addEnumeration(unicode_value=u'NEW')
processingOrderState.RUNNING = processingOrderState._CF_enumeration.addEnumeration(unicode_value=u'RUNNING')
processingOrderState.TERMINATED = processingOrderState._CF_enumeration.addEnumeration(unicode_value=u'TERMINATED')
processingOrderState.ERROR = processingOrderState._CF_enumeration.addEnumeration(unicode_value=u'ERROR')
processingOrderState._InitializeFacetMap(processingOrderState._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'processingOrderState', processingOrderState)

# Atomic SimpleTypeDefinition
class pipelineTaskRunState (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pipelineTaskRunState')
    _Documentation = None
pipelineTaskRunState._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=pipelineTaskRunState, enum_prefix=None)
pipelineTaskRunState.PENDING = pipelineTaskRunState._CF_enumeration.addEnumeration(unicode_value=u'PENDING')
pipelineTaskRunState.QUEUED = pipelineTaskRunState._CF_enumeration.addEnumeration(unicode_value=u'QUEUED')
pipelineTaskRunState.EXECUTING = pipelineTaskRunState._CF_enumeration.addEnumeration(unicode_value=u'EXECUTING')
pipelineTaskRunState.COMPLETED = pipelineTaskRunState._CF_enumeration.addEnumeration(unicode_value=u'COMPLETED')
pipelineTaskRunState.ERROR = pipelineTaskRunState._CF_enumeration.addEnumeration(unicode_value=u'ERROR')
pipelineTaskRunState.UNKNOWN = pipelineTaskRunState._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWN')
pipelineTaskRunState.HELD = pipelineTaskRunState._CF_enumeration.addEnumeration(unicode_value=u'HELD')
pipelineTaskRunState.SUSPENDED = pipelineTaskRunState._CF_enumeration.addEnumeration(unicode_value=u'SUSPENDED')
pipelineTaskRunState.ABORTED = pipelineTaskRunState._CF_enumeration.addEnumeration(unicode_value=u'ABORTED')
pipelineTaskRunState._InitializeFacetMap(pipelineTaskRunState._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'pipelineTaskRunState', pipelineTaskRunState)

# Atomic SimpleTypeDefinition
class queryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                Enumeration for the supported query types.
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'queryType')
    _Documentation = u'\n                Enumeration for the supported query types.\n            '
queryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=queryType, enum_prefix=None)
queryType.PARAM_QUERY = queryType._CF_enumeration.addEnumeration(unicode_value=u'PARAM_QUERY')
queryType.POLLING_PARAM_QUERY = queryType._CF_enumeration.addEnumeration(unicode_value=u'POLLING_PARAM_QUERY')
queryType.VELOCITY_PARAM_QUERY = queryType._CF_enumeration.addEnumeration(unicode_value=u'VELOCITY_PARAM_QUERY')
queryType.XQUERY = queryType._CF_enumeration.addEnumeration(unicode_value=u'XQUERY')
queryType.LOCAL_SQL_QUERY = queryType._CF_enumeration.addEnumeration(unicode_value=u'LOCAL_SQL_QUERY')
queryType.LOCAL_SELECTION = queryType._CF_enumeration.addEnumeration(unicode_value=u'LOCAL_SELECTION')
queryType._InitializeFacetMap(queryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'queryType', queryType)

# Atomic SimpleTypeDefinition
class pipelineRunState (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                Enumeration that indicates the state the pipeline job. 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pipelineRunState')
    _Documentation = u'\n                Enumeration that indicates the state the pipeline job. \n            '
pipelineRunState._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=pipelineRunState, enum_prefix=None)
pipelineRunState.NEW = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'NEW')
pipelineRunState.TRANSFERRING = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'TRANSFERRING')
pipelineRunState.INPUTS_LOCAL = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'INPUTS_LOCAL')
pipelineRunState.UPLOADING = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'UPLOADING')
pipelineRunState.CLUSTER_READY = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'CLUSTER_READY')
pipelineRunState.PIPELINE_RUNNING = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'PIPELINE_RUNNING')
pipelineRunState.PIPELINE_FINISHED = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'PIPELINE_FINISHED')
pipelineRunState.ARCHIVING = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'ARCHIVING')
pipelineRunState.ARCHIVED = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'ARCHIVED')
pipelineRunState.PUBLISHING = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'PUBLISHING')
pipelineRunState.DONE = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'DONE')
pipelineRunState.FAILED = pipelineRunState._CF_enumeration.addEnumeration(unicode_value=u'FAILED')
pipelineRunState._InitializeFacetMap(pipelineRunState._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'pipelineRunState', pipelineRunState)

# Complex type sgsProcessingOrder with content type ELEMENT_ONLY
class sgsProcessingOrder (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sgsProcessingOrder')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}Author uses Python identifier Author
    __Author = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Author'), 'Author', '__httpeuclid_esa_orgschemasysial_sgsProcessingOrder_httpeuclid_esa_orgschemasysialAuthor', False)

    
    Author = property(__Author.value, __Author.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ProcessingCampaign uses Python identifier ProcessingCampaign
    __ProcessingCampaign = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessingCampaign'), 'ProcessingCampaign', '__httpeuclid_esa_orgschemasysial_sgsProcessingOrder_httpeuclid_esa_orgschemasysialProcessingCampaign', False)

    
    ProcessingCampaign = property(__ProcessingCampaign.value, __ProcessingCampaign.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}PipelineDescription uses Python identifier PipelineDescription
    __PipelineDescription = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PipelineDescription'), 'PipelineDescription', '__httpeuclid_esa_orgschemasysial_sgsProcessingOrder_httpeuclid_esa_orgschemasysialPipelineDescription', False)

    
    PipelineDescription = property(__PipelineDescription.value, __PipelineDescription.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}TriggeringData uses Python identifier TriggeringData
    __TriggeringData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TriggeringData'), 'TriggeringData', '__httpeuclid_esa_orgschemasysial_sgsProcessingOrder_httpeuclid_esa_orgschemasysialTriggeringData', False)

    
    TriggeringData = property(__TriggeringData.value, __TriggeringData.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_sgsProcessingOrder_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)


    _ElementMap = {
        __Author.name() : __Author,
        __ProcessingCampaign.name() : __ProcessingCampaign,
        __PipelineDescription.name() : __PipelineDescription,
        __TriggeringData.name() : __TriggeringData,
        __Id.name() : __Id
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sgsProcessingOrder', sgsProcessingOrder)


# Complex type sdcProcessingOrder with content type ELEMENT_ONLY
class sdcProcessingOrder (sgsProcessingOrder):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sdcProcessingOrder')
    # Base type is sgsProcessingOrder
    
    # Element ProcessingCampaign ({http://euclid.esa.org/schema/sys/ial}ProcessingCampaign) inherited from {http://euclid.esa.org/schema/sys/ial}sgsProcessingOrder
    
    # Element {http://euclid.esa.org/schema/sys/ial}ClusterConfiguration uses Python identifier ClusterConfiguration
    __ClusterConfiguration = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ClusterConfiguration'), 'ClusterConfiguration', '__httpeuclid_esa_orgschemasysial_sdcProcessingOrder_httpeuclid_esa_orgschemasysialClusterConfiguration', False)

    
    ClusterConfiguration = property(__ClusterConfiguration.value, __ClusterConfiguration.set, None, None)

    
    # Element Id ({http://euclid.esa.org/schema/sys/ial}Id) inherited from {http://euclid.esa.org/schema/sys/ial}sgsProcessingOrder
    
    # Element Author ({http://euclid.esa.org/schema/sys/ial}Author) inherited from {http://euclid.esa.org/schema/sys/ial}sgsProcessingOrder
    
    # Element {http://euclid.esa.org/schema/sys/ial}IalConfiguration uses Python identifier IalConfiguration
    __IalConfiguration = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IalConfiguration'), 'IalConfiguration', '__httpeuclid_esa_orgschemasysial_sdcProcessingOrder_httpeuclid_esa_orgschemasysialIalConfiguration', False)

    
    IalConfiguration = property(__IalConfiguration.value, __IalConfiguration.set, None, None)

    
    # Element TriggeringData ({http://euclid.esa.org/schema/sys/ial}TriggeringData) inherited from {http://euclid.esa.org/schema/sys/ial}sgsProcessingOrder
    
    # Element {http://euclid.esa.org/schema/sys/ial}ProcessingState uses Python identifier ProcessingState
    __ProcessingState = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessingState'), 'ProcessingState', '__httpeuclid_esa_orgschemasysial_sdcProcessingOrder_httpeuclid_esa_orgschemasysialProcessingState', False)

    
    ProcessingState = property(__ProcessingState.value, __ProcessingState.set, None, None)

    
    # Element PipelineDescription ({http://euclid.esa.org/schema/sys/ial}PipelineDescription) inherited from {http://euclid.esa.org/schema/sys/ial}sgsProcessingOrder

    _ElementMap = sgsProcessingOrder._ElementMap.copy()
    _ElementMap.update({
        __ClusterConfiguration.name() : __ClusterConfiguration,
        __IalConfiguration.name() : __IalConfiguration,
        __ProcessingState.name() : __ProcessingState
    })
    _AttributeMap = sgsProcessingOrder._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sdcProcessingOrder', sdcProcessingOrder)


# Complex type clusterConfiguration with content type ELEMENT_ONLY
class clusterConfiguration (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'clusterConfiguration')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}TaskScheduler uses Python identifier TaskScheduler
    __TaskScheduler = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TaskScheduler'), 'TaskScheduler', '__httpeuclid_esa_orgschemasysial_clusterConfiguration_httpeuclid_esa_orgschemasysialTaskScheduler', False)

    
    TaskScheduler = property(__TaskScheduler.value, __TaskScheduler.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Workspace uses Python identifier Workspace
    __Workspace = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Workspace'), 'Workspace', '__httpeuclid_esa_orgschemasysial_clusterConfiguration_httpeuclid_esa_orgschemasysialWorkspace', False)

    
    Workspace = property(__Workspace.value, __Workspace.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_clusterConfiguration_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Sdc uses Python identifier Sdc
    __Sdc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sdc'), 'Sdc', '__httpeuclid_esa_orgschemasysial_clusterConfiguration_httpeuclid_esa_orgschemasysialSdc', False)

    
    Sdc = property(__Sdc.value, __Sdc.set, None, None)


    _ElementMap = {
        __TaskScheduler.name() : __TaskScheduler,
        __Workspace.name() : __Workspace,
        __Id.name() : __Id,
        __Sdc.name() : __Sdc
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'clusterConfiguration', clusterConfiguration)


# Complex type taskProduct with content type ELEMENT_ONLY
class taskProduct (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'taskProduct')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_taskProduct_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ProductId uses Python identifier ProductId
    __ProductId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProductId'), 'ProductId', '__httpeuclid_esa_orgschemasysial_taskProduct_httpeuclid_esa_orgschemasysialProductId', False)

    
    ProductId = property(__ProductId.value, __ProductId.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ProductRef uses Python identifier ProductRef
    __ProductRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProductRef'), 'ProductRef', '__httpeuclid_esa_orgschemasysial_taskProduct_httpeuclid_esa_orgschemasysialProductRef', False)

    
    ProductRef = property(__ProductRef.value, __ProductRef.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}PortName uses Python identifier PortName
    __PortName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PortName'), 'PortName', '__httpeuclid_esa_orgschemasysial_taskProduct_httpeuclid_esa_orgschemasysialPortName', False)

    
    PortName = property(__PortName.value, __PortName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ProductType uses Python identifier ProductType
    __ProductType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProductType'), 'ProductType', '__httpeuclid_esa_orgschemasysial_taskProduct_httpeuclid_esa_orgschemasysialProductType', False)

    
    ProductType = property(__ProductType.value, __ProductType.set, None, None)


    _ElementMap = {
        __Id.name() : __Id,
        __ProductId.name() : __ProductId,
        __ProductRef.name() : __ProductRef,
        __PortName.name() : __PortName,
        __ProductType.name() : __ProductType
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'taskProduct', taskProduct)


# Complex type ialConfiguration with content type ELEMENT_ONLY
class ialConfiguration (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ialConfiguration')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_ialConfiguration_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemasysial_ialConfiguration_httpeuclid_esa_orgschemasysialVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ConfigName uses Python identifier ConfigName
    __ConfigName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConfigName'), 'ConfigName', '__httpeuclid_esa_orgschemasysial_ialConfiguration_httpeuclid_esa_orgschemasysialConfigName', False)

    
    ConfigName = property(__ConfigName.value, __ConfigName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Sdc uses Python identifier Sdc
    __Sdc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sdc'), 'Sdc', '__httpeuclid_esa_orgschemasysial_ialConfiguration_httpeuclid_esa_orgschemasysialSdc', False)

    
    Sdc = property(__Sdc.value, __Sdc.set, None, None)


    _ElementMap = {
        __Id.name() : __Id,
        __Version.name() : __Version,
        __ConfigName.name() : __ConfigName,
        __Sdc.name() : __Sdc
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ialConfiguration', ialConfiguration)


# Complex type logFiles with content type ELEMENT_ONLY
class logFiles (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'logFiles')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}LogFile uses Python identifier LogFile
    __LogFile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LogFile'), 'LogFile', '__httpeuclid_esa_orgschemasysial_logFiles_httpeuclid_esa_orgschemasysialLogFile', True)

    
    LogFile = property(__LogFile.value, __LogFile.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}PipelineRunId uses Python identifier PipelineRunId
    __PipelineRunId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PipelineRunId'), 'PipelineRunId', '__httpeuclid_esa_orgschemasysial_logFiles_httpeuclid_esa_orgschemasysialPipelineRunId', False)

    
    PipelineRunId = property(__PipelineRunId.value, __PipelineRunId.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_logFiles_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)


    _ElementMap = {
        __LogFile.name() : __LogFile,
        __PipelineRunId.name() : __PipelineRunId,
        __Id.name() : __Id
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'logFiles', logFiles)


# Complex type triggeringData with content type ELEMENT_ONLY
class triggeringData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'triggeringData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}ExecTime uses Python identifier ExecTime
    __ExecTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExecTime'), 'ExecTime', '__httpeuclid_esa_orgschemasysial_triggeringData_httpeuclid_esa_orgschemasysialExecTime', False)

    
    ExecTime = property(__ExecTime.value, __ExecTime.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_triggeringData_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Query uses Python identifier Query
    __Query = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Query'), 'Query', '__httpeuclid_esa_orgschemasysial_triggeringData_httpeuclid_esa_orgschemasysialQuery', False)

    
    Query = property(__Query.value, __Query.set, None, None)


    _ElementMap = {
        __ExecTime.name() : __ExecTime,
        __Id.name() : __Id,
        __Query.name() : __Query
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'triggeringData', triggeringData)


# Complex type pipelineRun with content type ELEMENT_ONLY
class pipelineRun (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pipelineRun')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}StartDate uses Python identifier StartDate
    __StartDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StartDate'), 'StartDate', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialStartDate', False)

    
    StartDate = property(__StartDate.value, __StartDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Output'), 'Output', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialOutput', True)

    
    Output = property(__Output.value, __Output.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}IalConfiguration uses Python identifier IalConfiguration
    __IalConfiguration = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IalConfiguration'), 'IalConfiguration', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialIalConfiguration', False)

    
    IalConfiguration = property(__IalConfiguration.value, __IalConfiguration.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}EndDate uses Python identifier EndDate
    __EndDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EndDate'), 'EndDate', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialEndDate', False)

    
    EndDate = property(__EndDate.value, __EndDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ClusterConfiguration uses Python identifier ClusterConfiguration
    __ClusterConfiguration = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ClusterConfiguration'), 'ClusterConfiguration', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialClusterConfiguration', False)

    
    ClusterConfiguration = property(__ClusterConfiguration.value, __ClusterConfiguration.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ProcessingOrder uses Python identifier ProcessingOrder
    __ProcessingOrder = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessingOrder'), 'ProcessingOrder', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialProcessingOrder', False)

    
    ProcessingOrder = property(__ProcessingOrder.value, __ProcessingOrder.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}CompletedPipelineTasks uses Python identifier CompletedPipelineTasks
    __CompletedPipelineTasks = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CompletedPipelineTasks'), 'CompletedPipelineTasks', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialCompletedPipelineTasks', True)

    
    CompletedPipelineTasks = property(__CompletedPipelineTasks.value, __CompletedPipelineTasks.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}LogFiles uses Python identifier LogFiles
    __LogFiles = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LogFiles'), 'LogFiles', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialLogFiles', False)

    
    LogFiles = property(__LogFiles.value, __LogFiles.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Input uses Python identifier Input
    __Input = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Input'), 'Input', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialInput', True)

    
    Input = property(__Input.value, __Input.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ProcessingState uses Python identifier ProcessingState
    __ProcessingState = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessingState'), 'ProcessingState', '__httpeuclid_esa_orgschemasysial_pipelineRun_httpeuclid_esa_orgschemasysialProcessingState', False)

    
    ProcessingState = property(__ProcessingState.value, __ProcessingState.set, None, None)


    _ElementMap = {
        __StartDate.name() : __StartDate,
        __Output.name() : __Output,
        __IalConfiguration.name() : __IalConfiguration,
        __EndDate.name() : __EndDate,
        __ClusterConfiguration.name() : __ClusterConfiguration,
        __Id.name() : __Id,
        __ProcessingOrder.name() : __ProcessingOrder,
        __CompletedPipelineTasks.name() : __CompletedPipelineTasks,
        __LogFiles.name() : __LogFiles,
        __Input.name() : __Input,
        __ProcessingState.name() : __ProcessingState
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'pipelineRun', pipelineRun)


# Complex type taskProductList with content type ELEMENT_ONLY
class taskProductList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'taskProductList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}TaskProduct uses Python identifier TaskProduct
    __TaskProduct = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TaskProduct'), 'TaskProduct', '__httpeuclid_esa_orgschemasysial_taskProductList_httpeuclid_esa_orgschemasysialTaskProduct', True)

    
    TaskProduct = property(__TaskProduct.value, __TaskProduct.set, None, None)


    _ElementMap = {
        __TaskProduct.name() : __TaskProduct
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'taskProductList', taskProductList)


# Complex type query with content type ELEMENT_ONLY
class query (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'query')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}Params uses Python identifier Params
    __Params = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Params'), 'Params', '__httpeuclid_esa_orgschemasysial_query_httpeuclid_esa_orgschemasysialParams', False)

    
    Params = property(__Params.value, __Params.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Type'), 'Type', '__httpeuclid_esa_orgschemasysial_query_httpeuclid_esa_orgschemasysialType', False)

    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_query_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Template uses Python identifier Template
    __Template = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Template'), 'Template', '__httpeuclid_esa_orgschemasysial_query_httpeuclid_esa_orgschemasysialTemplate', False)

    
    Template = property(__Template.value, __Template.set, None, None)


    _ElementMap = {
        __Params.name() : __Params,
        __Type.name() : __Type,
        __Id.name() : __Id,
        __Template.name() : __Template
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'query', query)


# Complex type queryParameters with content type ELEMENT_ONLY
class queryParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'queryParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}Param uses Python identifier Param
    __Param = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Param'), 'Param', '__httpeuclid_esa_orgschemasysial_queryParameters_httpeuclid_esa_orgschemasysialParam', True)

    
    Param = property(__Param.value, __Param.set, None, None)


    _ElementMap = {
        __Param.name() : __Param
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'queryParameters', queryParameters)


# Complex type CTD_ANON with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpeuclid_esa_orgschemasysial_CTD_ANON_value', pyxb.binding.datatypes.string)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'key'), 'key', '__httpeuclid_esa_orgschemasysial_CTD_ANON_key', pyxb.binding.datatypes.string)
    
    key = property(__key.value, __key.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __value.name() : __value,
        __key.name() : __key
    }



# Complex type pipelineTaskRun with content type ELEMENT_ONLY
class pipelineTaskRun (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pipelineTaskRun')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Input uses Python identifier Input
    __Input = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Input'), 'Input', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialInput', True)

    
    Input = property(__Input.value, __Input.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ProcessStdout uses Python identifier ProcessStdout
    __ProcessStdout = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessStdout'), 'ProcessStdout', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialProcessStdout', False)

    
    ProcessStdout = property(__ProcessStdout.value, __ProcessStdout.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}PackageVersion uses Python identifier PackageVersion
    __PackageVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PackageVersion'), 'PackageVersion', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialPackageVersion', False)

    
    PackageVersion = property(__PackageVersion.value, __PackageVersion.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}LogFile uses Python identifier LogFile
    __LogFile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LogFile'), 'LogFile', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialLogFile', False)

    
    LogFile = property(__LogFile.value, __LogFile.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}PipelineRun uses Python identifier PipelineRun
    __PipelineRun = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PipelineRun'), 'PipelineRun', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialPipelineRun', False)

    
    PipelineRun = property(__PipelineRun.value, __PipelineRun.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ExecutableName uses Python identifier ExecutableName
    __ExecutableName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExecutableName'), 'ExecutableName', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialExecutableName', False)

    
    ExecutableName = property(__ExecutableName.value, __ExecutableName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ProcessingState uses Python identifier ProcessingState
    __ProcessingState = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessingState'), 'ProcessingState', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialProcessingState', False)

    
    ProcessingState = property(__ProcessingState.value, __ProcessingState.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Output'), 'Output', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialOutput', True)

    
    Output = property(__Output.value, __Output.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ProcessId uses Python identifier ProcessId
    __ProcessId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessId'), 'ProcessId', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialProcessId', False)

    
    ProcessId = property(__ProcessId.value, __ProcessId.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}PipelineTaskName uses Python identifier PipelineTaskName
    __PipelineTaskName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PipelineTaskName'), 'PipelineTaskName', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialPipelineTaskName', False)

    
    PipelineTaskName = property(__PipelineTaskName.value, __PipelineTaskName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ProcessStderr uses Python identifier ProcessStderr
    __ProcessStderr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessStderr'), 'ProcessStderr', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialProcessStderr', False)

    
    ProcessStderr = property(__ProcessStderr.value, __ProcessStderr.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}PackageName uses Python identifier PackageName
    __PackageName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PackageName'), 'PackageName', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialPackageName', False)

    
    PackageName = property(__PackageName.value, __PackageName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}ClusterConfiguration uses Python identifier ClusterConfiguration
    __ClusterConfiguration = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ClusterConfiguration'), 'ClusterConfiguration', '__httpeuclid_esa_orgschemasysial_pipelineTaskRun_httpeuclid_esa_orgschemasysialClusterConfiguration', False)

    
    ClusterConfiguration = property(__ClusterConfiguration.value, __ClusterConfiguration.set, None, None)


    _ElementMap = {
        __Id.name() : __Id,
        __Input.name() : __Input,
        __ProcessStdout.name() : __ProcessStdout,
        __PackageVersion.name() : __PackageVersion,
        __LogFile.name() : __LogFile,
        __PipelineRun.name() : __PipelineRun,
        __ExecutableName.name() : __ExecutableName,
        __ProcessingState.name() : __ProcessingState,
        __Output.name() : __Output,
        __ProcessId.name() : __ProcessId,
        __PipelineTaskName.name() : __PipelineTaskName,
        __ProcessStderr.name() : __ProcessStderr,
        __PackageName.name() : __PackageName,
        __ClusterConfiguration.name() : __ClusterConfiguration
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'pipelineTaskRun', pipelineTaskRun)


# Complex type taskScheduler with content type ELEMENT_ONLY
class taskScheduler (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'taskScheduler')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}JobStatusCheckCmd uses Python identifier JobStatusCheckCmd
    __JobStatusCheckCmd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'JobStatusCheckCmd'), 'JobStatusCheckCmd', '__httpeuclid_esa_orgschemasysial_taskScheduler_httpeuclid_esa_orgschemasysialJobStatusCheckCmd', False)

    
    JobStatusCheckCmd = property(__JobStatusCheckCmd.value, __JobStatusCheckCmd.set, None, u"\n\t\t\t\t\t\tName of the command fired in a process on the login node in the HPC environment. \n\t\t\t\t\t\tThis command is used to check the status of jobs submitted for execution on the HPC.\n\t\t\t\t\t\tThe result of the command is send to stdout in the format key=value separated by new lines.\n\t\t\t\t\t\tThe main key is the 'status'. The associated value is a string compliant with the \n\t\t\t\t\t\tIVOA Universal Worker Service v1.0 specification \n\t\t\t\t\t\t(see http://www.ivoa.net/Documents/UWS/20101010/REC-UWS-1.0-20101010.html#ExecutionPhase).   \n\t\t\t\t\t\tThe command should accept the following arguments:\n\t\t\t\t\t\t--jobid=job_id\n\t\t\t\t\t")

    
    # Element {http://euclid.esa.org/schema/sys/ial}ConfigData uses Python identifier ConfigData
    __ConfigData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConfigData'), 'ConfigData', '__httpeuclid_esa_orgschemasysial_taskScheduler_httpeuclid_esa_orgschemasysialConfigData', False)

    
    ConfigData = property(__ConfigData.value, __ConfigData.set, None, u'\n\t\t\t\t\t\tData (typically specified as CDATA) used for the HPC setup.  \n\t\t\t\t\t')

    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_taskScheduler_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}JobSubmitCmd uses Python identifier JobSubmitCmd
    __JobSubmitCmd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'JobSubmitCmd'), 'JobSubmitCmd', '__httpeuclid_esa_orgschemasysial_taskScheduler_httpeuclid_esa_orgschemasysialJobSubmitCmd', False)

    
    JobSubmitCmd = property(__JobSubmitCmd.value, __JobSubmitCmd.set, None, u"\n\t\t\t\t\t\tName of the command fired in a process on the login node in the HPC environment. \n\t\t\t\t\t\tThis command is used to submit ClusterJob's as defined in the IAL to the HPC.\n\t\t\t\t\t\tThe submission typically sends the jobs to the HPC queuing system and the task will be invoked asynchronously.\n\t\t\t\t\t\tThe result of the submitting the task is a process id (a string) which is used as an id to check the status with \n\t\t\t\t\t\tthe help of the ClusterJobStatusCmd (see below).   \n\t\t\t\t\t\tThe command should accept the following arguments:\n\t\t\t\t\t\t--task=task_name\n\t\t\t\t\t\t--package=pckg_name\n\t\t\t\t\t\t--input=path : path to the xml file (as seen on the login node) describing the task input data.\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t--params=path : path to the xml file (as seen on the login node) describing the task parameters (static pipeline task configuration parameters).\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t--outdir=path : path to the output directory the task should write the output to. \n\t\t\t\t\t\tNote that all these paths should point to a location on the login node also referred to as local storage. \n\t\t\t\t\t\tThe HPCTaskExecutor might then pick up these files and transport them to the computing nodes for the task execution\n\t\t\t\t\t\tand write its results back from the computing node to the login node. In a typical cluster environment with a shared file system mounted by the \n\t\t\t\t\t\tcompute nodes this is however not necessary.\n\t\t\t\t\t")

    
    # Element {http://euclid.esa.org/schema/sys/ial}SetupCmd uses Python identifier SetupCmd
    __SetupCmd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SetupCmd'), 'SetupCmd', '__httpeuclid_esa_orgschemasysial_taskScheduler_httpeuclid_esa_orgschemasysialSetupCmd', False)

    
    SetupCmd = property(__SetupCmd.value, __SetupCmd.set, None, u'\n\t\t\t\t\t\tName of the command fired in a process on the login node in the HPC environment.\n\t\t\t\t\t\tThis command can be used to setup / prepare the environment for running jobs.\n\t\t\t\t\t\tThe command will be called from within the IAL when preparing a pipeline processing order.\n\t\t\t\t\t\tNote that, typically, it does not include installation of the pipeline software on the HPC. \n\t\t\t\t\t\tRather, it will include e.g. configuring a queue (if there are many available) or to set PYTHONPATH.\n\t\t\t\t\t\tThis command should accept the following arguments \n\t\t\t\t\t\t(1) --config=data: Configuration data found in the HpcConfigData element; could be a shell script.\n\t\t\t\t\t\t(2) --log-level=LOG_LEVEL: Set the default log-level to be used.\n\t\t\t\t\t')

    
    # Element {http://euclid.esa.org/schema/sys/ial}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemasysial_taskScheduler_httpeuclid_esa_orgschemasysialName', False)

    
    Name = property(__Name.value, __Name.set, None, None)


    _ElementMap = {
        __JobStatusCheckCmd.name() : __JobStatusCheckCmd,
        __ConfigData.name() : __ConfigData,
        __Id.name() : __Id,
        __JobSubmitCmd.name() : __JobSubmitCmd,
        __SetupCmd.name() : __SetupCmd,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'taskScheduler', taskScheduler)


# Complex type logFile with content type ELEMENT_ONLY
class logFile (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'logFile')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/ial}PipelineTaskName uses Python identifier PipelineTaskName
    __PipelineTaskName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PipelineTaskName'), 'PipelineTaskName', '__httpeuclid_esa_orgschemasysial_logFile_httpeuclid_esa_orgschemasysialPipelineTaskName', False)

    
    PipelineTaskName = property(__PipelineTaskName.value, __PipelineTaskName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}PipelineTaskRunId uses Python identifier PipelineTaskRunId
    __PipelineTaskRunId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PipelineTaskRunId'), 'PipelineTaskRunId', '__httpeuclid_esa_orgschemasysial_logFile_httpeuclid_esa_orgschemasysialPipelineTaskRunId', False)

    
    PipelineTaskRunId = property(__PipelineTaskRunId.value, __PipelineTaskRunId.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}File uses Python identifier File
    __File = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'File'), 'File', '__httpeuclid_esa_orgschemasysial_logFile_httpeuclid_esa_orgschemasysialFile', False)

    
    File = property(__File.value, __File.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/ial}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasysial_logFile_httpeuclid_esa_orgschemasysialId', False)

    
    Id = property(__Id.value, __Id.set, None, None)


    _ElementMap = {
        __PipelineTaskName.name() : __PipelineTaskName,
        __PipelineTaskRunId.name() : __PipelineTaskRunId,
        __File.name() : __File,
        __Id.name() : __Id
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'logFile', logFile)




sgsProcessingOrder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Author'), pyxb.binding.datatypes.string, scope=sgsProcessingOrder))

sgsProcessingOrder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessingCampaign'), pyxb.binding.datatypes.string, scope=sgsProcessingOrder))

sgsProcessingOrder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PipelineDescription'), CommonDM.sys.sgs_stub.dataContainer, scope=sgsProcessingOrder))

sgsProcessingOrder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TriggeringData'), triggeringData, scope=sgsProcessingOrder))

sgsProcessingOrder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.ID, scope=sgsProcessingOrder))
sgsProcessingOrder._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sgsProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(sgsProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TriggeringData')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sgsProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PipelineDescription')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sgsProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessingCampaign')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sgsProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Author')), min_occurs=1, max_occurs=1)
    )
sgsProcessingOrder._ContentModel = pyxb.binding.content.ParticleModel(sgsProcessingOrder._GroupModel, min_occurs=1, max_occurs=1)



sdcProcessingOrder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClusterConfiguration'), clusterConfiguration, scope=sdcProcessingOrder))

sdcProcessingOrder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IalConfiguration'), ialConfiguration, scope=sdcProcessingOrder))

sdcProcessingOrder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessingState'), processingOrderState, scope=sdcProcessingOrder))
sdcProcessingOrder._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sdcProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(sdcProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TriggeringData')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sdcProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PipelineDescription')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sdcProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessingCampaign')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sdcProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Author')), min_occurs=1, max_occurs=1)
    )
sdcProcessingOrder._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sdcProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClusterConfiguration')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sdcProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IalConfiguration')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sdcProcessingOrder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessingState')), min_occurs=1, max_occurs=1)
    )
sdcProcessingOrder._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sdcProcessingOrder._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sdcProcessingOrder._GroupModel_2, min_occurs=1, max_occurs=1)
    )
sdcProcessingOrder._ContentModel = pyxb.binding.content.ParticleModel(sdcProcessingOrder._GroupModel, min_occurs=1, max_occurs=1)



clusterConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TaskScheduler'), taskScheduler, scope=clusterConfiguration))

clusterConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Workspace'), CommonDM.sys.sgs_stub.storageNode, scope=clusterConfiguration))

clusterConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=clusterConfiguration))

clusterConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sdc'), CommonDM.sys_stub.infraName, scope=clusterConfiguration))
clusterConfiguration._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(clusterConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(clusterConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sdc')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(clusterConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Workspace')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(clusterConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TaskScheduler')), min_occurs=0L, max_occurs=1)
    )
clusterConfiguration._ContentModel = pyxb.binding.content.ParticleModel(clusterConfiguration._GroupModel, min_occurs=1, max_occurs=1)



taskProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=taskProduct))

taskProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProductId'), pyxb.binding.datatypes.string, scope=taskProduct))

taskProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProductRef'), CommonDM.sys.sgs_stub.fileDescriptor, scope=taskProduct))

taskProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PortName'), pyxb.binding.datatypes.string, scope=taskProduct))

taskProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProductType'), pyxb.binding.datatypes.string, scope=taskProduct))
taskProduct._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(taskProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(taskProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PortName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(taskProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProductId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(taskProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProductType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(taskProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProductRef')), min_occurs=0L, max_occurs=1)
    )
taskProduct._ContentModel = pyxb.binding.content.ParticleModel(taskProduct._GroupModel, min_occurs=1, max_occurs=1)



ialConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=ialConfiguration))

ialConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), pyxb.binding.datatypes.string, scope=ialConfiguration))

ialConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConfigName'), pyxb.binding.datatypes.string, scope=ialConfiguration))

ialConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sdc'), CommonDM.sys_stub.infraName, scope=ialConfiguration))
ialConfiguration._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ialConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ialConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sdc')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ialConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ialConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConfigName')), min_occurs=1, max_occurs=1)
    )
ialConfiguration._ContentModel = pyxb.binding.content.ParticleModel(ialConfiguration._GroupModel, min_occurs=1, max_occurs=1)



logFiles._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogFile'), logFile, scope=logFiles))

logFiles._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PipelineRunId'), pyxb.binding.datatypes.string, scope=logFiles))

logFiles._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=logFiles))
logFiles._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(logFiles._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(logFiles._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PipelineRunId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(logFiles._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogFile')), min_occurs=0L, max_occurs=None)
    )
logFiles._ContentModel = pyxb.binding.content.ParticleModel(logFiles._GroupModel, min_occurs=1, max_occurs=1)



triggeringData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExecTime'), pyxb.binding.datatypes.dateTime, scope=triggeringData))

triggeringData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=triggeringData))

triggeringData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Query'), query, scope=triggeringData))
triggeringData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(triggeringData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(triggeringData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Query')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(triggeringData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExecTime')), min_occurs=0L, max_occurs=1)
    )
triggeringData._ContentModel = pyxb.binding.content.ParticleModel(triggeringData._GroupModel, min_occurs=1, max_occurs=1)



pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartDate'), CommonDM.sys_stub.systemDateTime, scope=pipelineRun))

pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Output'), taskProduct, scope=pipelineRun))

pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IalConfiguration'), ialConfiguration, scope=pipelineRun))

pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndDate'), CommonDM.sys_stub.systemDateTime, scope=pipelineRun))

pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClusterConfiguration'), clusterConfiguration, scope=pipelineRun))

pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.ID, scope=pipelineRun))

pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessingOrder'), pyxb.binding.datatypes.IDREF, scope=pipelineRun))

pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CompletedPipelineTasks'), pyxb.binding.datatypes.string, scope=pipelineRun))

pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogFiles'), logFiles, scope=pipelineRun))

pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Input'), taskProduct, scope=pipelineRun))

pipelineRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessingState'), pipelineRunState, scope=pipelineRun))
pipelineRun._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessingOrder')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Input')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Output')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClusterConfiguration')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IalConfiguration')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CompletedPipelineTasks')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogFiles')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pipelineRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessingState')), min_occurs=0L, max_occurs=1)
    )
pipelineRun._ContentModel = pyxb.binding.content.ParticleModel(pipelineRun._GroupModel, min_occurs=1, max_occurs=1)



taskProductList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TaskProduct'), taskProduct, scope=taskProductList))
taskProductList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(taskProductList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TaskProduct')), min_occurs=0L, max_occurs=None)
    )
taskProductList._ContentModel = pyxb.binding.content.ParticleModel(taskProductList._GroupModel, min_occurs=1, max_occurs=1)



query._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Params'), queryParameters, scope=query))

query._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Type'), queryType, scope=query))

query._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=query))

query._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Template'), pyxb.binding.datatypes.string, scope=query))
query._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(query._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(query._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Type')), min_occurs=1L, max_occurs=1),
    pyxb.binding.content.ParticleModel(query._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Template')), min_occurs=1L, max_occurs=1),
    pyxb.binding.content.ParticleModel(query._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Params')), min_occurs=0L, max_occurs=1)
    )
query._ContentModel = pyxb.binding.content.ParticleModel(query._GroupModel, min_occurs=1, max_occurs=1)



queryParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Param'), CTD_ANON, scope=queryParameters))
queryParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(queryParameters._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Param')), min_occurs=1, max_occurs=1)
    )
queryParameters._ContentModel = pyxb.binding.content.ParticleModel(queryParameters._GroupModel, min_occurs=0L, max_occurs=None)



pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.ID, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Input'), taskProduct, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessStdout'), pyxb.binding.datatypes.string, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PackageVersion'), pyxb.binding.datatypes.string, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogFile'), logFile, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PipelineRun'), pyxb.binding.datatypes.IDREF, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExecutableName'), pyxb.binding.datatypes.string, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessingState'), pipelineTaskRunState, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Output'), taskProduct, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessId'), pyxb.binding.datatypes.string, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PipelineTaskName'), pyxb.binding.datatypes.string, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessStderr'), pyxb.binding.datatypes.string, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PackageName'), pyxb.binding.datatypes.string, scope=pipelineTaskRun))

pipelineTaskRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClusterConfiguration'), clusterConfiguration, scope=pipelineTaskRun))
pipelineTaskRun._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PipelineRun')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PipelineTaskName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PackageName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PackageVersion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExecutableName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Input')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Output')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClusterConfiguration')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessStdout')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessStderr')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogFile')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessingState')), min_occurs=1, max_occurs=1)
    )
pipelineTaskRun._ContentModel = pyxb.binding.content.ParticleModel(pipelineTaskRun._GroupModel, min_occurs=1, max_occurs=1)



taskScheduler._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'JobStatusCheckCmd'), pyxb.binding.datatypes.string, scope=taskScheduler, documentation=u"\n\t\t\t\t\t\tName of the command fired in a process on the login node in the HPC environment. \n\t\t\t\t\t\tThis command is used to check the status of jobs submitted for execution on the HPC.\n\t\t\t\t\t\tThe result of the command is send to stdout in the format key=value separated by new lines.\n\t\t\t\t\t\tThe main key is the 'status'. The associated value is a string compliant with the \n\t\t\t\t\t\tIVOA Universal Worker Service v1.0 specification \n\t\t\t\t\t\t(see http://www.ivoa.net/Documents/UWS/20101010/REC-UWS-1.0-20101010.html#ExecutionPhase).   \n\t\t\t\t\t\tThe command should accept the following arguments:\n\t\t\t\t\t\t--jobid=job_id\n\t\t\t\t\t"))

taskScheduler._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConfigData'), pyxb.binding.datatypes.string, scope=taskScheduler, documentation=u'\n\t\t\t\t\t\tData (typically specified as CDATA) used for the HPC setup.  \n\t\t\t\t\t'))

taskScheduler._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=taskScheduler))

taskScheduler._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'JobSubmitCmd'), pyxb.binding.datatypes.string, scope=taskScheduler, documentation=u"\n\t\t\t\t\t\tName of the command fired in a process on the login node in the HPC environment. \n\t\t\t\t\t\tThis command is used to submit ClusterJob's as defined in the IAL to the HPC.\n\t\t\t\t\t\tThe submission typically sends the jobs to the HPC queuing system and the task will be invoked asynchronously.\n\t\t\t\t\t\tThe result of the submitting the task is a process id (a string) which is used as an id to check the status with \n\t\t\t\t\t\tthe help of the ClusterJobStatusCmd (see below).   \n\t\t\t\t\t\tThe command should accept the following arguments:\n\t\t\t\t\t\t--task=task_name\n\t\t\t\t\t\t--package=pckg_name\n\t\t\t\t\t\t--input=path : path to the xml file (as seen on the login node) describing the task input data.\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t--params=path : path to the xml file (as seen on the login node) describing the task parameters (static pipeline task configuration parameters).\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t--outdir=path : path to the output directory the task should write the output to. \n\t\t\t\t\t\tNote that all these paths should point to a location on the login node also referred to as local storage. \n\t\t\t\t\t\tThe HPCTaskExecutor might then pick up these files and transport them to the computing nodes for the task execution\n\t\t\t\t\t\tand write its results back from the computing node to the login node. In a typical cluster environment with a shared file system mounted by the \n\t\t\t\t\t\tcompute nodes this is however not necessary.\n\t\t\t\t\t"))

taskScheduler._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SetupCmd'), pyxb.binding.datatypes.string, scope=taskScheduler, documentation=u'\n\t\t\t\t\t\tName of the command fired in a process on the login node in the HPC environment.\n\t\t\t\t\t\tThis command can be used to setup / prepare the environment for running jobs.\n\t\t\t\t\t\tThe command will be called from within the IAL when preparing a pipeline processing order.\n\t\t\t\t\t\tNote that, typically, it does not include installation of the pipeline software on the HPC. \n\t\t\t\t\t\tRather, it will include e.g. configuring a queue (if there are many available) or to set PYTHONPATH.\n\t\t\t\t\t\tThis command should accept the following arguments \n\t\t\t\t\t\t(1) --config=data: Configuration data found in the HpcConfigData element; could be a shell script.\n\t\t\t\t\t\t(2) --log-level=LOG_LEVEL: Set the default log-level to be used.\n\t\t\t\t\t'))

taskScheduler._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=taskScheduler))
taskScheduler._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(taskScheduler._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(taskScheduler._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(taskScheduler._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SetupCmd')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(taskScheduler._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConfigData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(taskScheduler._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'JobSubmitCmd')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(taskScheduler._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'JobStatusCheckCmd')), min_occurs=1, max_occurs=1)
    )
taskScheduler._ContentModel = pyxb.binding.content.ParticleModel(taskScheduler._GroupModel, min_occurs=1, max_occurs=1)



logFile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PipelineTaskName'), pyxb.binding.datatypes.string, scope=logFile))

logFile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PipelineTaskRunId'), pyxb.binding.datatypes.string, scope=logFile))

logFile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'File'), CommonDM.sys.sgs_stub.dataContainer, scope=logFile))

logFile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=logFile))
logFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(logFile._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(logFile._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PipelineTaskName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(logFile._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PipelineTaskRunId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(logFile._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'File')), min_occurs=1, max_occurs=1)
    )
logFile._ContentModel = pyxb.binding.content.ParticleModel(logFile._GroupModel, min_occurs=1, max_occurs=1)
