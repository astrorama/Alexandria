# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/sys_stub.py
# PyXB bindings for NamespaceModule
# NSM:ef11d8db76a7f46c6c12cc44757c7de95f0af727
# Generated 2014-03-17 11:53:47.248661 by PyXB version 1.1.2
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
import CommonDM.dm.bas_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/sys', create_if_missing=True)
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
class configFileName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'configFileName')
    _Documentation = None
configFileName._CF_pattern = pyxb.binding.facets.CF_pattern()
configFileName._CF_pattern.addPattern(pattern=u'EUC-[GSOV|IOTE|OPER|4SVT?|TD??|TEST].[A-Za-z0-9]{3,4}')
configFileName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
configFileName._InitializeFacetMap(configFileName._CF_pattern,
   configFileName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'configFileName', configFileName)

# Atomic SimpleTypeDefinition
class version (pyxb.binding.datatypes.string):

    """Generic use for a release of data,software, model,...No specific constraint between 3 and 6 characters from 0.1to 2.2.3 for example."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'version')
    _Documentation = u'Generic use for a release of data,software, model,...No specific constraint between 3 and 6 characters from 0.1to 2.2.3 for example.'
version._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
version._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(6L))
version._InitializeFacetMap(version._CF_minLength,
   version._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'version', version)

# Atomic SimpleTypeDefinition
class scientificGroupName (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of scientific groups used in EUCLID SGSreferring to OUs andSWG	"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'scientificGroupName')
    _Documentation = u'List of scientific groups used in EUCLID SGSreferring to OUs andSWG\t'
scientificGroupName._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=scientificGroupName, enum_prefix=None)
scientificGroupName.VIS = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'VIS')
scientificGroupName.NIR = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'NIR')
scientificGroupName.SIR = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'SIR')
scientificGroupName.SPE = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'SPE')
scientificGroupName.SIMWL = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'SIMWL')
scientificGroupName.SIM = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'SIM')
scientificGroupName.PHZ = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'PHZ')
scientificGroupName.LE3 = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'LE3')
scientificGroupName.EXTDES = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'EXTDES')
scientificGroupName.EXTPAN = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'EXTPAN')
scientificGroupName.EXTLSST = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'EXTLSST')
scientificGroupName.EXTKIDS = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'EXTKIDS')
scientificGroupName.SHE = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'SHE')
scientificGroupName.MER = scientificGroupName._CF_enumeration.addEnumeration(unicode_value=u'MER')
scientificGroupName._InitializeFacetMap(scientificGroupName._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'scientificGroupName', scientificGroupName)

# Atomic SimpleTypeDefinition
class systemDateTime (pyxb.binding.datatypes.dateTime):

    """
                An UTC date-time value with a precision of one millisecond
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'systemDateTime')
    _Documentation = u'\n                An UTC date-time value with a precision of one millisecond\n            '
systemDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
systemDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\dZ')
systemDateTime._InitializeFacetMap(systemDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'systemDateTime', systemDateTime)

# Atomic SimpleTypeDefinition
class infraName (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of SDC/infrastructures components used in EUCLID SGS.	"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'infraName')
    _Documentation = u'List of SDC/infrastructures components used in EUCLID SGS.\t'
infraName._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=infraName, enum_prefix=None)
infraName.EAS = infraName._CF_enumeration.addEnumeration(unicode_value=u'EAS')
infraName.SDC_FR = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-FR')
infraName.SDC_IT = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-IT')
infraName.SDC_UK = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-UK')
infraName.SDC_NL = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-NL')
infraName.SDC_ES = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-ES')
infraName.SDC_FI = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-FI')
infraName.SDC_CH = infraName._CF_enumeration.addEnumeration(unicode_value=u'SDC-CH')
infraName.SOC = infraName._CF_enumeration.addEnumeration(unicode_value=u'SOC')
infraName.MOC = infraName._CF_enumeration.addEnumeration(unicode_value=u'MOC')
infraName.CLOUDServices = infraName._CF_enumeration.addEnumeration(unicode_value=u'CLOUDServices')
infraName.LOCAL = infraName._CF_enumeration.addEnumeration(unicode_value=u'LOCAL')
infraName._InitializeFacetMap(infraName._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'infraName', infraName)

# Atomic SimpleTypeDefinition
class dataFileName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataFileName')
    _Documentation = None
dataFileName._CF_pattern = pyxb.binding.facets.CF_pattern()
dataFileName._CF_pattern.addPattern(pattern=u'EUC-[GSOV|IOTE|OPER|4SVT?|TD??|TEST]{4}-[A-Za-z0-9]{1,10}-[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]{1,6})?Z?\\.[A-Za-z0-9]{3,4}')
dataFileName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
dataFileName._InitializeFacetMap(dataFileName._CF_pattern,
   dataFileName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'dataFileName', dataFileName)

# Complex type genericHeader with content type ELEMENT_ONLY
class genericHeader (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'genericHeader')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys}ProductType uses Python identifier ProductType
    __ProductType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProductType'), 'ProductType', '__httpeuclid_esa_orgschemasys_genericHeader_httpeuclid_esa_orgschemasysProductType', False)

    
    ProductType = property(__ProductType.value, __ProductType.set, None, u'Identifies the type of product. The list of product types is defined within the Data Model.')

    
    # Element {http://euclid.esa.org/schema/sys}ScientificCustodian uses Python identifier ScientificCustodian
    __ScientificCustodian = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ScientificCustodian'), 'ScientificCustodian', '__httpeuclid_esa_orgschemasys_genericHeader_httpeuclid_esa_orgschemasysScientificCustodian', False)

    
    ScientificCustodian = property(__ScientificCustodian.value, __ScientificCustodian.set, None, u'Scientific Group responsible of the quality of  the data referring to the OU or SWG or else. The custodian of this group and coordinates complete ')

    
    # Element {http://euclid.esa.org/schema/sys}ProductName uses Python identifier ProductName
    __ProductName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProductName'), 'ProductName', '__httpeuclid_esa_orgschemasys_genericHeader_httpeuclid_esa_orgschemasysProductName', False)

    
    ProductName = property(__ProductName.value, __ProductName.set, None, u'Product Name, the interface embeds one and only one Product. This information is derived from the task schema input/output name. ')

    
    # Element {http://euclid.esa.org/schema/sys}SoftwareName uses Python identifier SoftwareName
    __SoftwareName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SoftwareName'), 'SoftwareName', '__httpeuclid_esa_orgschemasys_genericHeader_httpeuclid_esa_orgschemasysSoftwareName', False)

    
    SoftwareName = property(__SoftwareName.value, __SoftwareName.set, None, u'This SoftwareName is extracted from the task definition : /tsk/component tsk/executable')

    
    # Element {http://euclid.esa.org/schema/sys}AccessRights uses Python identifier AccessRights
    __AccessRights = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AccessRights'), 'AccessRights', '__httpeuclid_esa_orgschemasys_genericHeader_httpeuclid_esa_orgschemasysAccessRights', False)

    
    AccessRights = property(__AccessRights.value, __AccessRights.set, None, u'Interface access rights.')

    
    # Element {http://euclid.esa.org/schema/sys}ProductId uses Python identifier ProductId
    __ProductId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProductId'), 'ProductId', '__httpeuclid_esa_orgschemasys_genericHeader_httpeuclid_esa_orgschemasysProductId', False)

    
    ProductId = property(__ProductId.value, __ProductId.set, None, u'This Id is the unique reference of the object defined in thi interface, this Id is processed by IAL to ensure the uniqueness.')

    
    # Element {http://euclid.esa.org/schema/sys}SoftwareRelease uses Python identifier SoftwareRelease
    __SoftwareRelease = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SoftwareRelease'), 'SoftwareRelease', '__httpeuclid_esa_orgschemasys_genericHeader_httpeuclid_esa_orgschemasysSoftwareRelease', False)

    
    SoftwareRelease = property(__SoftwareRelease.value, __SoftwareRelease.set, None, u'This SoftwareRelease is extracted from the task definition : /tsk/component tsk/version')


    _ElementMap = {
        __ProductType.name() : __ProductType,
        __ScientificCustodian.name() : __ScientificCustodian,
        __ProductName.name() : __ProductName,
        __SoftwareName.name() : __SoftwareName,
        __AccessRights.name() : __AccessRights,
        __ProductId.name() : __ProductId,
        __SoftwareRelease.name() : __SoftwareRelease
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'genericHeader', genericHeader)


# Complex type accessRights with content type ELEMENT_ONLY
class accessRights (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accessRights')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys}ScientificGroupWrite uses Python identifier ScientificGroupWrite
    __ScientificGroupWrite = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ScientificGroupWrite'), 'ScientificGroupWrite', '__httpeuclid_esa_orgschemasys_accessRights_httpeuclid_esa_orgschemasysScientificGroupWrite', False)

    
    ScientificGroupWrite = property(__ScientificGroupWrite.value, __ScientificGroupWrite.set, None, u'True if the interface is the writable from scientific group')

    
    # Element {http://euclid.esa.org/schema/sys}EuclidConsortiumRead uses Python identifier EuclidConsortiumRead
    __EuclidConsortiumRead = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EuclidConsortiumRead'), 'EuclidConsortiumRead', '__httpeuclid_esa_orgschemasys_accessRights_httpeuclid_esa_orgschemasysEuclidConsortiumRead', False)

    
    EuclidConsortiumRead = property(__EuclidConsortiumRead.value, __EuclidConsortiumRead.set, None, u'True if the interface is readable from Euclid consortia ')

    
    # Element {http://euclid.esa.org/schema/sys}ScientificGroupRead uses Python identifier ScientificGroupRead
    __ScientificGroupRead = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ScientificGroupRead'), 'ScientificGroupRead', '__httpeuclid_esa_orgschemasys_accessRights_httpeuclid_esa_orgschemasysScientificGroupRead', False)

    
    ScientificGroupRead = property(__ScientificGroupRead.value, __ScientificGroupRead.set, None, u'True if the interface is readable from scientific group')

    
    # Element {http://euclid.esa.org/schema/sys}EuclidConsortiumWrite uses Python identifier EuclidConsortiumWrite
    __EuclidConsortiumWrite = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EuclidConsortiumWrite'), 'EuclidConsortiumWrite', '__httpeuclid_esa_orgschemasys_accessRights_httpeuclid_esa_orgschemasysEuclidConsortiumWrite', False)

    
    EuclidConsortiumWrite = property(__EuclidConsortiumWrite.value, __EuclidConsortiumWrite.set, None, u'True if the interface is the writable from Euclid consortia')


    _ElementMap = {
        __ScientificGroupWrite.name() : __ScientificGroupWrite,
        __EuclidConsortiumRead.name() : __EuclidConsortiumRead,
        __ScientificGroupRead.name() : __ScientificGroupRead,
        __EuclidConsortiumWrite.name() : __EuclidConsortiumWrite
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'accessRights', accessRights)




genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProductType'), pyxb.binding.datatypes.QName, scope=genericHeader, documentation=u'Identifies the type of product. The list of product types is defined within the Data Model.'))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ScientificCustodian'), scientificGroupName, scope=genericHeader, documentation=u'Scientific Group responsible of the quality of  the data referring to the OU or SWG or else. The custodian of this group and coordinates complete '))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProductName'), CommonDM.dm.bas_stub.objectName, scope=genericHeader, documentation=u'Product Name, the interface embeds one and only one Product. This information is derived from the task schema input/output name. '))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SoftwareName'), pyxb.binding.datatypes.string, scope=genericHeader, documentation=u'This SoftwareName is extracted from the task definition : /tsk/component tsk/executable'))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AccessRights'), accessRights, scope=genericHeader, documentation=u'Interface access rights.'))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProductId'), CommonDM.dm.bas_stub.objectId, scope=genericHeader, documentation=u'This Id is the unique reference of the object defined in thi interface, this Id is processed by IAL to ensure the uniqueness.'))

genericHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SoftwareRelease'), version, scope=genericHeader, documentation=u'This SoftwareRelease is extracted from the task definition : /tsk/component tsk/version'))
genericHeader._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(genericHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProductName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(genericHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProductId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(genericHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProductType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(genericHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SoftwareName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(genericHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SoftwareRelease')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(genericHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ScientificCustodian')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(genericHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AccessRights')), min_occurs=1, max_occurs=1)
    )
genericHeader._ContentModel = pyxb.binding.content.ParticleModel(genericHeader._GroupModel, min_occurs=1, max_occurs=1)



accessRights._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ScientificGroupWrite'), pyxb.binding.datatypes.boolean, scope=accessRights, documentation=u'True if the interface is the writable from scientific group'))

accessRights._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EuclidConsortiumRead'), pyxb.binding.datatypes.boolean, scope=accessRights, documentation=u'True if the interface is readable from Euclid consortia '))

accessRights._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ScientificGroupRead'), pyxb.binding.datatypes.boolean, scope=accessRights, documentation=u'True if the interface is readable from scientific group'))

accessRights._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EuclidConsortiumWrite'), pyxb.binding.datatypes.boolean, scope=accessRights, documentation=u'True if the interface is the writable from Euclid consortia'))
accessRights._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accessRights._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EuclidConsortiumRead')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(accessRights._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EuclidConsortiumWrite')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(accessRights._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ScientificGroupRead')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(accessRights._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ScientificGroupWrite')), min_occurs=1, max_occurs=1)
    )
accessRights._ContentModel = pyxb.binding.content.ParticleModel(accessRights._GroupModel, min_occurs=1, max_occurs=1)
