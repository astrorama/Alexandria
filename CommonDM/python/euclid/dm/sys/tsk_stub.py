# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/sys/tsk_stub.py
# PyXB bindings for NamespaceModule
# NSM:4d4c1cd48d5bfb7604fcb66c8a481339a235819e
# Generated 2014-03-14 09:43:27.465777 by PyXB version 1.1.2
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
import pyxb.binding.datatypes
import euclid.dm.sys_stub
import euclid.dm.sys.sgs_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/sys/tsk', create_if_missing=True)
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


# Complex type taskDefinition with content type ELEMENT_ONLY
class taskDefinition (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'taskDefinition')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/tsk}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Output'), 'Output', '__httpeuclid_esa_orgschemasystsk_taskDefinition_httpeuclid_esa_orgschemasystskOutput', True)

    
    Output = property(__Output.value, __Output.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/tsk}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpeuclid_esa_orgschemasystsk_taskDefinition_httpeuclid_esa_orgschemasystskDescription', False)

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/tsk}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemasystsk_taskDefinition_httpeuclid_esa_orgschemasystskName', False)

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/tsk}Input uses Python identifier Input
    __Input = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Input'), 'Input', '__httpeuclid_esa_orgschemasystsk_taskDefinition_httpeuclid_esa_orgschemasystskInput', True)

    
    Input = property(__Input.value, __Input.set, None, None)


    _ElementMap = {
        __Output.name() : __Output,
        __Description.name() : __Description,
        __Name.name() : __Name,
        __Input.name() : __Input
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'taskDefinition', taskDefinition)


# Complex type workflowDefinition with content type ELEMENT_ONLY
class workflowDefinition (taskDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'workflowDefinition')
    # Base type is taskDefinition
    
    # Element {http://euclid.esa.org/schema/sys/tsk}Task uses Python identifier Task
    __Task = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Task'), 'Task', '__httpeuclid_esa_orgschemasystsk_workflowDefinition_httpeuclid_esa_orgschemasystskTask', True)

    
    Task = property(__Task.value, __Task.set, None, None)

    
    # Element Input ({http://euclid.esa.org/schema/sys/tsk}Input) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition
    
    # Element Name ({http://euclid.esa.org/schema/sys/tsk}Name) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition
    
    # Element {http://euclid.esa.org/schema/sys/tsk}Workflow uses Python identifier Workflow
    __Workflow = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Workflow'), 'Workflow', '__httpeuclid_esa_orgschemasystsk_workflowDefinition_httpeuclid_esa_orgschemasystskWorkflow', True)

    
    Workflow = property(__Workflow.value, __Workflow.set, None, None)

    
    # Element Output ({http://euclid.esa.org/schema/sys/tsk}Output) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition
    
    # Element {http://euclid.esa.org/schema/sys/tsk}Edge uses Python identifier Edge
    __Edge = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Edge'), 'Edge', '__httpeuclid_esa_orgschemasystsk_workflowDefinition_httpeuclid_esa_orgschemasystskEdge', True)

    
    Edge = property(__Edge.value, __Edge.set, None, None)

    
    # Element Description ({http://euclid.esa.org/schema/sys/tsk}Description) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition

    _ElementMap = taskDefinition._ElementMap.copy()
    _ElementMap.update({
        __Task.name() : __Task,
        __Workflow.name() : __Workflow,
        __Edge.name() : __Edge
    })
    _AttributeMap = taskDefinition._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'workflowDefinition', workflowDefinition)


# Complex type pipelineDefinition with content type ELEMENT_ONLY
class pipelineDefinition (workflowDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pipelineDefinition')
    # Base type is workflowDefinition
    
    # Element Description ({http://euclid.esa.org/schema/sys/tsk}Description) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition
    
    # Element Input ({http://euclid.esa.org/schema/sys/tsk}Input) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition
    
    # Element Name ({http://euclid.esa.org/schema/sys/tsk}Name) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition
    
    # Element Workflow ({http://euclid.esa.org/schema/sys/tsk}Workflow) inherited from {http://euclid.esa.org/schema/sys/tsk}workflowDefinition
    
    # Element Task ({http://euclid.esa.org/schema/sys/tsk}Task) inherited from {http://euclid.esa.org/schema/sys/tsk}workflowDefinition
    
    # Element {http://euclid.esa.org/schema/sys/tsk}Owner uses Python identifier Owner
    __Owner = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Owner'), 'Owner', '__httpeuclid_esa_orgschemasystsk_pipelineDefinition_httpeuclid_esa_orgschemasystskOwner', False)

    
    Owner = property(__Owner.value, __Owner.set, None, None)

    
    # Element Edge ({http://euclid.esa.org/schema/sys/tsk}Edge) inherited from {http://euclid.esa.org/schema/sys/tsk}workflowDefinition
    
    # Element Output ({http://euclid.esa.org/schema/sys/tsk}Output) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition

    _ElementMap = workflowDefinition._ElementMap.copy()
    _ElementMap.update({
        __Owner.name() : __Owner
    })
    _AttributeMap = workflowDefinition._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'pipelineDefinition', pipelineDefinition)


# Complex type port with content type ELEMENT_ONLY
class port (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'port')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/tsk}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Reference'), 'Reference', '__httpeuclid_esa_orgschemasystsk_port_httpeuclid_esa_orgschemasystskReference', True)

    
    Reference = property(__Reference.value, __Reference.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/tsk}ProductType uses Python identifier ProductType
    __ProductType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProductType'), 'ProductType', '__httpeuclid_esa_orgschemasystsk_port_httpeuclid_esa_orgschemasystskProductType', False)

    
    ProductType = property(__ProductType.value, __ProductType.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/tsk}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpeuclid_esa_orgschemasystsk_port_httpeuclid_esa_orgschemasystskDescription', False)

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/tsk}Mandatory uses Python identifier Mandatory
    __Mandatory = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Mandatory'), 'Mandatory', '__httpeuclid_esa_orgschemasystsk_port_httpeuclid_esa_orgschemasystskMandatory', False)

    
    Mandatory = property(__Mandatory.value, __Mandatory.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemasystsk_port_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __Reference.name() : __Reference,
        __ProductType.name() : __ProductType,
        __Description.name() : __Description,
        __Mandatory.name() : __Mandatory
    }
    _AttributeMap = {
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'port', port)


# Complex type edge with content type EMPTY
class edge (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'edge')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'to'), 'to', '__httpeuclid_esa_orgschemasystsk_edge_to', pyxb.binding.datatypes.string)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemasystsk_edge_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'from'), 'from_', '__httpeuclid_esa_orgschemasystsk_edge_from', pyxb.binding.datatypes.string)
    
    from_ = property(__from.value, __from.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __to.name() : __to,
        __name.name() : __name,
        __from.name() : __from
    }
Namespace.addCategoryObject('typeBinding', u'edge', edge)


# Complex type pipelineTaskDefinition with content type ELEMENT_ONLY
class pipelineTaskDefinition (taskDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pipelineTaskDefinition')
    # Base type is taskDefinition
    
    # Element Output ({http://euclid.esa.org/schema/sys/tsk}Output) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition
    
    # Element Description ({http://euclid.esa.org/schema/sys/tsk}Description) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition
    
    # Element {http://euclid.esa.org/schema/sys/tsk}ExecutableName uses Python identifier ExecutableName
    __ExecutableName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExecutableName'), 'ExecutableName', '__httpeuclid_esa_orgschemasystsk_pipelineTaskDefinition_httpeuclid_esa_orgschemasystskExecutableName', False)

    
    ExecutableName = property(__ExecutableName.value, __ExecutableName.set, None, None)

    
    # Element Input ({http://euclid.esa.org/schema/sys/tsk}Input) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition
    
    # Element {http://euclid.esa.org/schema/sys/tsk}Interpreter uses Python identifier Interpreter
    __Interpreter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Interpreter'), 'Interpreter', '__httpeuclid_esa_orgschemasystsk_pipelineTaskDefinition_httpeuclid_esa_orgschemasystskInterpreter', False)

    
    Interpreter = property(__Interpreter.value, __Interpreter.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/tsk}PackageName uses Python identifier PackageName
    __PackageName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PackageName'), 'PackageName', '__httpeuclid_esa_orgschemasystsk_pipelineTaskDefinition_httpeuclid_esa_orgschemasystskPackageName', False)

    
    PackageName = property(__PackageName.value, __PackageName.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/tsk}PackageVersion uses Python identifier PackageVersion
    __PackageVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PackageVersion'), 'PackageVersion', '__httpeuclid_esa_orgschemasystsk_pipelineTaskDefinition_httpeuclid_esa_orgschemasystskPackageVersion', False)

    
    PackageVersion = property(__PackageVersion.value, __PackageVersion.set, None, None)

    
    # Element Name ({http://euclid.esa.org/schema/sys/tsk}Name) inherited from {http://euclid.esa.org/schema/sys/tsk}taskDefinition

    _ElementMap = taskDefinition._ElementMap.copy()
    _ElementMap.update({
        __ExecutableName.name() : __ExecutableName,
        __Interpreter.name() : __Interpreter,
        __PackageName.name() : __PackageName,
        __PackageVersion.name() : __PackageVersion
    })
    _AttributeMap = taskDefinition._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'pipelineTaskDefinition', pipelineTaskDefinition)


# Complex type packageDefinition with content type ELEMENT_ONLY
class packageDefinition (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'packageDefinition')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/tsk}TaskDefinition uses Python identifier TaskDefinition
    __TaskDefinition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TaskDefinition'), 'TaskDefinition', '__httpeuclid_esa_orgschemasystsk_packageDefinition_httpeuclid_esa_orgschemasystskTaskDefinition', True)

    
    TaskDefinition = property(__TaskDefinition.value, __TaskDefinition.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/tsk}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemasystsk_packageDefinition_httpeuclid_esa_orgschemasystskName', False)

    
    Name = property(__Name.value, __Name.set, None, None)


    _ElementMap = {
        __TaskDefinition.name() : __TaskDefinition,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'packageDefinition', packageDefinition)


# Complex type pipelineTask with content type EMPTY
class pipelineTask (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pipelineTask')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute packageName uses Python identifier packageName
    __packageName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'packageName'), 'packageName', '__httpeuclid_esa_orgschemasystsk_pipelineTask_packageName', pyxb.binding.datatypes.string, required=True)
    
    packageName = property(__packageName.value, __packageName.set, None, None)

    
    # Attribute taskDefinition uses Python identifier taskDefinition
    __taskDefinition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'taskDefinition'), 'taskDefinition', '__httpeuclid_esa_orgschemasystsk_pipelineTask_taskDefinition', pyxb.binding.datatypes.string, required=True)
    
    taskDefinition = property(__taskDefinition.value, __taskDefinition.set, None, None)

    
    # Attribute packageVersion uses Python identifier packageVersion
    __packageVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'packageVersion'), 'packageVersion', '__httpeuclid_esa_orgschemasystsk_pipelineTask_packageVersion', pyxb.binding.datatypes.string, required=True)
    
    packageVersion = property(__packageVersion.value, __packageVersion.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemasystsk_pipelineTask_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __packageName.name() : __packageName,
        __taskDefinition.name() : __taskDefinition,
        __packageVersion.name() : __packageVersion,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'pipelineTask', pipelineTask)




taskDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Output'), port, scope=taskDefinition))

taskDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), pyxb.binding.datatypes.string, scope=taskDefinition))

taskDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=taskDefinition))

taskDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Input'), port, scope=taskDefinition))
taskDefinition._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(taskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(taskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(taskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Input')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(taskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Output')), min_occurs=0L, max_occurs=None)
    )
taskDefinition._ContentModel = pyxb.binding.content.ParticleModel(taskDefinition._GroupModel, min_occurs=1, max_occurs=1)



workflowDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Task'), pipelineTask, scope=workflowDefinition))

workflowDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Workflow'), workflowDefinition, scope=workflowDefinition))

workflowDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Edge'), edge, scope=workflowDefinition))
workflowDefinition._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(workflowDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(workflowDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(workflowDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Input')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(workflowDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Output')), min_occurs=0L, max_occurs=None)
    )
workflowDefinition._GroupModel_3 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(workflowDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Task')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(workflowDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Workflow')), min_occurs=1, max_occurs=1)
    )
workflowDefinition._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(workflowDefinition._GroupModel_3, min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(workflowDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Edge')), min_occurs=0L, max_occurs=None)
    )
workflowDefinition._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(workflowDefinition._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(workflowDefinition._GroupModel_2, min_occurs=1, max_occurs=1)
    )
workflowDefinition._ContentModel = pyxb.binding.content.ParticleModel(workflowDefinition._GroupModel, min_occurs=1, max_occurs=1)



pipelineDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Owner'), euclid.dm.sys_stub.scientificGroupName, scope=pipelineDefinition))
pipelineDefinition._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pipelineDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pipelineDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pipelineDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Input')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pipelineDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Output')), min_occurs=0L, max_occurs=None)
    )
pipelineDefinition._GroupModel_4 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(pipelineDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Task')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Workflow')), min_occurs=1, max_occurs=1)
    )
pipelineDefinition._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pipelineDefinition._GroupModel_4, min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pipelineDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Edge')), min_occurs=0L, max_occurs=None)
    )
pipelineDefinition._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pipelineDefinition._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineDefinition._GroupModel_3, min_occurs=1, max_occurs=1)
    )
pipelineDefinition._GroupModel_5 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pipelineDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Owner')), min_occurs=0L, max_occurs=1)
    )
pipelineDefinition._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pipelineDefinition._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineDefinition._GroupModel_5, min_occurs=1, max_occurs=1)
    )
pipelineDefinition._ContentModel = pyxb.binding.content.ParticleModel(pipelineDefinition._GroupModel, min_occurs=1, max_occurs=1)



port._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), euclid.dm.sys.sgs_stub.fileDescriptor, scope=port))

port._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProductType'), pyxb.binding.datatypes.string, scope=port))

port._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), pyxb.binding.datatypes.string, scope=port))

port._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Mandatory'), pyxb.binding.datatypes.boolean, scope=port))
port._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(port._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(port._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProductType')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(port._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Mandatory')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(port._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reference')), min_occurs=0L, max_occurs=None)
    )
port._ContentModel = pyxb.binding.content.ParticleModel(port._GroupModel, min_occurs=1, max_occurs=1)



pipelineTaskDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExecutableName'), pyxb.binding.datatypes.string, scope=pipelineTaskDefinition))

pipelineTaskDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Interpreter'), pyxb.binding.datatypes.string, scope=pipelineTaskDefinition))

pipelineTaskDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PackageName'), pyxb.binding.datatypes.string, scope=pipelineTaskDefinition))

pipelineTaskDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PackageVersion'), pyxb.binding.datatypes.string, scope=pipelineTaskDefinition))
pipelineTaskDefinition._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pipelineTaskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pipelineTaskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pipelineTaskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Input')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pipelineTaskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Output')), min_occurs=0L, max_occurs=None)
    )
pipelineTaskDefinition._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pipelineTaskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExecutableName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PackageName')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pipelineTaskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PackageVersion')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pipelineTaskDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Interpreter')), min_occurs=0L, max_occurs=1L)
    )
pipelineTaskDefinition._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pipelineTaskDefinition._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(pipelineTaskDefinition._GroupModel_2, min_occurs=1, max_occurs=1)
    )
pipelineTaskDefinition._ContentModel = pyxb.binding.content.ParticleModel(pipelineTaskDefinition._GroupModel, min_occurs=1, max_occurs=1)



packageDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TaskDefinition'), pipelineTaskDefinition, scope=packageDefinition))

packageDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=packageDefinition))
packageDefinition._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(packageDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(packageDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TaskDefinition')), min_occurs=0L, max_occurs=None)
    )
packageDefinition._ContentModel = pyxb.binding.content.ParticleModel(packageDefinition._GroupModel, min_occurs=1, max_occurs=1)
