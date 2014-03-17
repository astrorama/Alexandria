# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/sys/sgs_stub.py
# PyXB bindings for NamespaceModule
# NSM:77d3da8c9c0b8eec64b9957d9ec227ca99caec32
# Generated 2014-03-17 11:53:47.248850 by PyXB version 1.1.2
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
import CommonDM.dm.sys_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/sys/sgs', create_if_missing=True)
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
class emailAddress (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'emailAddress')
    _Documentation = None
emailAddress._CF_pattern = pyxb.binding.facets.CF_pattern()
emailAddress._CF_pattern.addPattern(pattern=u'[^@]+@[^\\.]+\\..+')
emailAddress._InitializeFacetMap(emailAddress._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'emailAddress', emailAddress)

# Atomic SimpleTypeDefinition
class checksumAlgorithm (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'checksumAlgorithm')
    _Documentation = None
checksumAlgorithm._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=checksumAlgorithm, enum_prefix=None)
checksumAlgorithm.MD5 = checksumAlgorithm._CF_enumeration.addEnumeration(unicode_value=u'MD5')
checksumAlgorithm.Adler32 = checksumAlgorithm._CF_enumeration.addEnumeration(unicode_value=u'Adler32')
checksumAlgorithm._InitializeFacetMap(checksumAlgorithm._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'checksumAlgorithm', checksumAlgorithm)

# Atomic SimpleTypeDefinition
class protocol (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'protocol')
    _Documentation = None
protocol._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=protocol, enum_prefix=None)
protocol.http = protocol._CF_enumeration.addEnumeration(unicode_value=u'http')
protocol.https = protocol._CF_enumeration.addEnumeration(unicode_value=u'https')
protocol.ftp = protocol._CF_enumeration.addEnumeration(unicode_value=u'ftp')
protocol.sftp = protocol._CF_enumeration.addEnumeration(unicode_value=u'sftp')
protocol.file = protocol._CF_enumeration.addEnumeration(unicode_value=u'file')
protocol.gridftp = protocol._CF_enumeration.addEnumeration(unicode_value=u'gridftp')
protocol.srm = protocol._CF_enumeration.addEnumeration(unicode_value=u'srm')
protocol._InitializeFacetMap(protocol._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'protocol', protocol)

# Complex type dataContainer with content type ELEMENT_ONLY
class dataContainer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataContainer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/sgs}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpeuclid_esa_orgschemasyssgs_dataContainer_httpeuclid_esa_orgschemasyssgsDescription', False)

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Location'), 'Location', '__httpeuclid_esa_orgschemasyssgs_dataContainer_httpeuclid_esa_orgschemasyssgsLocation', True)

    
    Location = property(__Location.value, __Location.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Type'), 'Type', '__httpeuclid_esa_orgschemasyssgs_dataContainer_httpeuclid_esa_orgschemasyssgsType', False)

    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}CheckSum uses Python identifier CheckSum
    __CheckSum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CheckSum'), 'CheckSum', '__httpeuclid_esa_orgschemasyssgs_dataContainer_httpeuclid_esa_orgschemasyssgsCheckSum', False)

    
    CheckSum = property(__CheckSum.value, __CheckSum.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), 'CreationDate', '__httpeuclid_esa_orgschemasyssgs_dataContainer_httpeuclid_esa_orgschemasyssgsCreationDate', False)

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Filename uses Python identifier Filename
    __Filename = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filename'), 'Filename', '__httpeuclid_esa_orgschemasyssgs_dataContainer_httpeuclid_esa_orgschemasyssgsFilename', False)

    
    Filename = property(__Filename.value, __Filename.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasyssgs_dataContainer_httpeuclid_esa_orgschemasyssgsId', False)

    
    Id = property(__Id.value, __Id.set, None, None)


    _ElementMap = {
        __Description.name() : __Description,
        __Location.name() : __Location,
        __Type.name() : __Type,
        __CheckSum.name() : __CheckSum,
        __CreationDate.name() : __CreationDate,
        __Filename.name() : __Filename,
        __Id.name() : __Id
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'dataContainer', dataContainer)


# Complex type contact with content type ELEMENT_ONLY
class contact (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'contact')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/sgs}Email uses Python identifier Email
    __Email = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Email'), 'Email', '__httpeuclid_esa_orgschemasyssgs_contact_httpeuclid_esa_orgschemasyssgsEmail', False)

    
    Email = property(__Email.value, __Email.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemasyssgs_contact_httpeuclid_esa_orgschemasyssgsName', False)

    
    Name = property(__Name.value, __Name.set, None, None)


    _ElementMap = {
        __Email.name() : __Email,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'contact', contact)


# Complex type ivoaUCDParam with content type ELEMENT_ONLY
class ivoaUCDParam (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ivoaUCDParam')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/sgs}UCD uses Python identifier UCD
    __UCD = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'UCD'), 'UCD', '__httpeuclid_esa_orgschemasyssgs_ivoaUCDParam_httpeuclid_esa_orgschemasyssgsUCD', False)

    
    UCD = property(__UCD.value, __UCD.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemasyssgs_ivoaUCDParam_httpeuclid_esa_orgschemasyssgsName', False)

    
    Name = property(__Name.value, __Name.set, None, None)


    _ElementMap = {
        __UCD.name() : __UCD,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ivoaUCDParam', ivoaUCDParam)


# Complex type fileDescriptor with content type ELEMENT_ONLY
class fileDescriptor (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fileDescriptor')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/sgs}Filename uses Python identifier Filename
    __Filename = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Filename'), 'Filename', '__httpeuclid_esa_orgschemasyssgs_fileDescriptor_httpeuclid_esa_orgschemasyssgsFilename', False)

    
    Filename = property(__Filename.value, __Filename.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasyssgs_fileDescriptor_httpeuclid_esa_orgschemasyssgsId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}StorageId uses Python identifier StorageId
    __StorageId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StorageId'), 'StorageId', '__httpeuclid_esa_orgschemasyssgs_fileDescriptor_httpeuclid_esa_orgschemasyssgsStorageId', False)

    
    StorageId = property(__StorageId.value, __StorageId.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Path uses Python identifier Path
    __Path = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Path'), 'Path', '__httpeuclid_esa_orgschemasyssgs_fileDescriptor_httpeuclid_esa_orgschemasyssgsPath', False)

    
    Path = property(__Path.value, __Path.set, None, None)


    _ElementMap = {
        __Filename.name() : __Filename,
        __Id.name() : __Id,
        __StorageId.name() : __StorageId,
        __Path.name() : __Path
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'fileDescriptor', fileDescriptor)


# Complex type product with content type ELEMENT_ONLY
class product (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'product')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/sgs}ProductionDate uses Python identifier ProductionDate
    __ProductionDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProductionDate'), 'ProductionDate', '__httpeuclid_esa_orgschemasyssgs_product_httpeuclid_esa_orgschemasyssgsProductionDate', False)

    
    ProductionDate = property(__ProductionDate.value, __ProductionDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemasyssgs_product_httpeuclid_esa_orgschemasyssgsName', False)

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpeuclid_esa_orgschemasyssgs_product_httpeuclid_esa_orgschemasyssgsDescription', False)

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Producer uses Python identifier Producer
    __Producer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Producer'), 'Producer', '__httpeuclid_esa_orgschemasyssgs_product_httpeuclid_esa_orgschemasyssgsProducer', False)

    
    Producer = property(__Producer.value, __Producer.set, None, u'Creator of the data.')

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Type'), 'Type', '__httpeuclid_esa_orgschemasyssgs_product_httpeuclid_esa_orgschemasyssgsType', False)

    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Source'), 'Source', '__httpeuclid_esa_orgschemasyssgs_product_httpeuclid_esa_orgschemasyssgsSource', False)

    
    Source = property(__Source.value, __Source.set, None, None)


    _ElementMap = {
        __ProductionDate.name() : __ProductionDate,
        __Name.name() : __Name,
        __Description.name() : __Description,
        __Producer.name() : __Producer,
        __Type.name() : __Type,
        __Source.name() : __Source
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'product', product)


# Complex type curation with content type ELEMENT_ONLY
class curation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'curation')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/sgs}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Reference'), 'Reference', '__httpeuclid_esa_orgschemasyssgs_curation_httpeuclid_esa_orgschemasyssgsReference', False)

    
    Reference = property(__Reference.value, __Reference.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemasyssgs_curation_httpeuclid_esa_orgschemasyssgsVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}PublisherDID uses Python identifier PublisherDID
    __PublisherDID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PublisherDID'), 'PublisherDID', '__httpeuclid_esa_orgschemasyssgs_curation_httpeuclid_esa_orgschemasyssgsPublisherDID', False)

    
    PublisherDID = property(__PublisherDID.value, __PublisherDID.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Publisher uses Python identifier Publisher
    __Publisher = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Publisher'), 'Publisher', '__httpeuclid_esa_orgschemasyssgs_curation_httpeuclid_esa_orgschemasyssgsPublisher', False)

    
    Publisher = property(__Publisher.value, __Publisher.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__httpeuclid_esa_orgschemasyssgs_curation_httpeuclid_esa_orgschemasyssgsContact', False)

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}PublisherID uses Python identifier PublisherID
    __PublisherID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PublisherID'), 'PublisherID', '__httpeuclid_esa_orgschemasyssgs_curation_httpeuclid_esa_orgschemasyssgsPublisherID', False)

    
    PublisherID = property(__PublisherID.value, __PublisherID.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Rights uses Python identifier Rights
    __Rights = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Rights'), 'Rights', '__httpeuclid_esa_orgschemasyssgs_curation_httpeuclid_esa_orgschemasyssgsRights', False)

    
    Rights = property(__Rights.value, __Rights.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Date uses Python identifier Date
    __Date = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Date'), 'Date', '__httpeuclid_esa_orgschemasyssgs_curation_httpeuclid_esa_orgschemasyssgsDate', False)

    
    Date = property(__Date.value, __Date.set, None, None)


    _ElementMap = {
        __Reference.name() : __Reference,
        __Version.name() : __Version,
        __PublisherDID.name() : __PublisherDID,
        __Publisher.name() : __Publisher,
        __Contact.name() : __Contact,
        __PublisherID.name() : __PublisherID,
        __Rights.name() : __Rights,
        __Date.name() : __Date
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'curation', curation)


# Complex type storageNode with content type ELEMENT_ONLY
class storageNode (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'storageNode')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/sgs}BasePath uses Python identifier BasePath
    __BasePath = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BasePath'), 'BasePath', '__httpeuclid_esa_orgschemasyssgs_storageNode_httpeuclid_esa_orgschemasyssgsBasePath', False)

    
    BasePath = property(__BasePath.value, __BasePath.set, None, u'Root path for the where to refer file locations to.')

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Domain uses Python identifier Domain
    __Domain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Domain'), 'Domain', '__httpeuclid_esa_orgschemasyssgs_storageNode_httpeuclid_esa_orgschemasyssgsDomain', False)

    
    Domain = property(__Domain.value, __Domain.set, None, u'Name of the domain for this storage node.')

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Sdc uses Python identifier Sdc
    __Sdc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sdc'), 'Sdc', '__httpeuclid_esa_orgschemasyssgs_storageNode_httpeuclid_esa_orgschemasyssgsSdc', False)

    
    Sdc = property(__Sdc.value, __Sdc.set, None, u'Name of the SDC this storage node is associated with.')

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasyssgs_storageNode_httpeuclid_esa_orgschemasyssgsId', False)

    
    Id = property(__Id.value, __Id.set, None, u'Should be of the form: sdc_protocol_domain_port_basePath')

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Port uses Python identifier Port
    __Port = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Port'), 'Port', '__httpeuclid_esa_orgschemasyssgs_storageNode_httpeuclid_esa_orgschemasyssgsPort', False)

    
    Port = property(__Port.value, __Port.set, None, u'Port number this storage node can be accessed.')

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Protocol uses Python identifier Protocol
    __Protocol = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Protocol'), 'Protocol', '__httpeuclid_esa_orgschemasyssgs_storageNode_httpeuclid_esa_orgschemasyssgsProtocol', False)

    
    Protocol = property(__Protocol.value, __Protocol.set, None, u'Protocol used to retrieve the file from this storage node.')


    _ElementMap = {
        __BasePath.name() : __BasePath,
        __Domain.name() : __Domain,
        __Sdc.name() : __Sdc,
        __Id.name() : __Id,
        __Port.name() : __Port,
        __Protocol.name() : __Protocol
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'storageNode', storageNode)


# Complex type checksumType with content type ELEMENT_ONLY
class checksumType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'checksumType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/sgs}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemasyssgs_checksumType_httpeuclid_esa_orgschemasyssgsValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Algorithm uses Python identifier Algorithm
    __Algorithm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Algorithm'), 'Algorithm', '__httpeuclid_esa_orgschemasyssgs_checksumType_httpeuclid_esa_orgschemasyssgsAlgorithm', False)

    
    Algorithm = property(__Algorithm.value, __Algorithm.set, None, None)


    _ElementMap = {
        __Value.name() : __Value,
        __Algorithm.name() : __Algorithm
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'checksumType', checksumType)


# Complex type fileContainer with content type ELEMENT_ONLY
class fileContainer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fileContainer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/sys/sgs}StorageNode uses Python identifier StorageNode
    __StorageNode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StorageNode'), 'StorageNode', '__httpeuclid_esa_orgschemasyssgs_fileContainer_httpeuclid_esa_orgschemasyssgsStorageNode', False)

    
    StorageNode = property(__StorageNode.value, __StorageNode.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Path uses Python identifier Path
    __Path = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Path'), 'Path', '__httpeuclid_esa_orgschemasyssgs_fileContainer_httpeuclid_esa_orgschemasyssgsPath', False)

    
    Path = property(__Path.value, __Path.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Id'), 'Id', '__httpeuclid_esa_orgschemasyssgs_fileContainer_httpeuclid_esa_orgschemasyssgsId', False)

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {http://euclid.esa.org/schema/sys/sgs}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__httpeuclid_esa_orgschemasyssgs_fileContainer_httpeuclid_esa_orgschemasyssgsURL', False)

    
    URL = property(__URL.value, __URL.set, None, None)


    _ElementMap = {
        __StorageNode.name() : __StorageNode,
        __Path.name() : __Path,
        __Id.name() : __Id,
        __URL.name() : __URL
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'fileContainer', fileContainer)




dataContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), pyxb.binding.datatypes.string, scope=dataContainer))

dataContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Location'), fileContainer, scope=dataContainer))

dataContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Type'), pyxb.binding.datatypes.string, scope=dataContainer))

dataContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CheckSum'), checksumType, scope=dataContainer))

dataContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CreationDate'), CommonDM.dm.sys_stub.systemDateTime, scope=dataContainer))

dataContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filename'), CommonDM.dm.sys_stub.dataFileName, scope=dataContainer))

dataContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=dataContainer))
dataContainer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(dataContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filename')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Type')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CreationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CheckSum')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Location')), min_occurs=0L, max_occurs=None)
    )
dataContainer._ContentModel = pyxb.binding.content.ParticleModel(dataContainer._GroupModel, min_occurs=1, max_occurs=1)



contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Email'), emailAddress, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=contact))
contact._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Email')), min_occurs=0L, max_occurs=1)
    )
contact._ContentModel = pyxb.binding.content.ParticleModel(contact._GroupModel, min_occurs=1, max_occurs=1)



ivoaUCDParam._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UCD'), pyxb.binding.datatypes.string, scope=ivoaUCDParam))

ivoaUCDParam._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=ivoaUCDParam))
ivoaUCDParam._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ivoaUCDParam._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ivoaUCDParam._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UCD')), min_occurs=1, max_occurs=1)
    )
ivoaUCDParam._ContentModel = pyxb.binding.content.ParticleModel(ivoaUCDParam._GroupModel, min_occurs=1, max_occurs=1)



fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Filename'), pyxb.binding.datatypes.string, scope=fileDescriptor))

fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=fileDescriptor))

fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StorageId'), pyxb.binding.datatypes.string, scope=fileDescriptor))

fileDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Path'), pyxb.binding.datatypes.string, scope=fileDescriptor))
fileDescriptor._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Filename')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Path')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fileDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StorageId')), min_occurs=1, max_occurs=1)
    )
fileDescriptor._ContentModel = pyxb.binding.content.ParticleModel(fileDescriptor._GroupModel, min_occurs=1, max_occurs=1)



product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProductionDate'), CommonDM.dm.sys_stub.systemDateTime, scope=product))

product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=product))

product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), pyxb.binding.datatypes.string, scope=product))

product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Producer'), CommonDM.dm.sys_stub.infraName, scope=product, documentation=u'Creator of the data.'))

product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Type'), pyxb.binding.datatypes.string, scope=product))

product._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Source'), dataContainer, scope=product))
product._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(product._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Source')), min_occurs=1, max_occurs=1)
    )
product._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(product._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(product._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(product._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Type')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(product._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProductionDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(product._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Producer')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(product._GroupModel_, min_occurs=1, max_occurs=1)
    )
product._ContentModel = pyxb.binding.content.ParticleModel(product._GroupModel, min_occurs=1, max_occurs=1)



curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), ivoaUCDParam, scope=curation))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), ivoaUCDParam, scope=curation))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PublisherDID'), ivoaUCDParam, scope=curation))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Publisher'), ivoaUCDParam, scope=curation))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), contact, scope=curation))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PublisherID'), ivoaUCDParam, scope=curation))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Rights'), ivoaUCDParam, scope=curation))

curation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Date'), pyxb.binding.datatypes.dateTime, scope=curation))
curation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(curation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Publisher')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(curation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PublisherID')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(curation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reference')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(curation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(curation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(curation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Rights')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(curation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Date')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(curation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PublisherDID')), min_occurs=0L, max_occurs=1)
    )
curation._ContentModel = pyxb.binding.content.ParticleModel(curation._GroupModel, min_occurs=1, max_occurs=1)



storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BasePath'), pyxb.binding.datatypes.string, scope=storageNode, documentation=u'Root path for the where to refer file locations to.'))

storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Domain'), pyxb.binding.datatypes.string, scope=storageNode, documentation=u'Name of the domain for this storage node.'))

storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sdc'), CommonDM.dm.sys_stub.infraName, scope=storageNode, documentation=u'Name of the SDC this storage node is associated with.'))

storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=storageNode, documentation=u'Should be of the form: sdc_protocol_domain_port_basePath'))

storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Port'), pyxb.binding.datatypes.int, scope=storageNode, documentation=u'Port number this storage node can be accessed.'))

storageNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Protocol'), protocol, scope=storageNode, documentation=u'Protocol used to retrieve the file from this storage node.'))
storageNode._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Protocol')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Domain')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Port')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BasePath')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(storageNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sdc')), min_occurs=1, max_occurs=1)
    )
storageNode._ContentModel = pyxb.binding.content.ParticleModel(storageNode._GroupModel, min_occurs=1, max_occurs=1)



checksumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.string, scope=checksumType))

checksumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Algorithm'), checksumAlgorithm, scope=checksumType))
checksumType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(checksumType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Algorithm')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(checksumType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1)
    )
checksumType._ContentModel = pyxb.binding.content.ParticleModel(checksumType._GroupModel, min_occurs=1, max_occurs=1)



fileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StorageNode'), storageNode, scope=fileContainer))

fileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Path'), pyxb.binding.datatypes.string, scope=fileContainer))

fileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Id'), pyxb.binding.datatypes.string, scope=fileContainer))

fileContainer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.string, scope=fileContainer))
fileContainer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Id')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Path')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(fileContainer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StorageNode')), min_occurs=1, max_occurs=1)
    )
fileContainer._ContentModel = pyxb.binding.content.ParticleModel(fileContainer._GroupModel, min_occurs=1, max_occurs=1)
