# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/bas/cot_stub.py
# PyXB bindings for NamespaceModule
# NSM:1f4fe8b16d279182add9c54818352556887a4f2e
# Generated 2014-03-17 11:53:47.250874 by PyXB version 1.1.2
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
import CommonDM.dm.bas.imp_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/cot', create_if_missing=True)
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


# Complex type astrom with content type ELEMENT_ONLY
class astrom (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'astrom')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/cot}CRVAL2 uses Python identifier CRVAL2
    __CRVAL2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRVAL2'), 'CRVAL2', '__httpeuclid_esa_orgschemabascot_astrom_httpeuclid_esa_orgschemabascotCRVAL2', False)

    
    CRVAL2 = property(__CRVAL2.value, __CRVAL2.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cot}CTYPE2 uses Python identifier CTYPE2
    __CTYPE2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CTYPE2'), 'CTYPE2', '__httpeuclid_esa_orgschemabascot_astrom_httpeuclid_esa_orgschemabascotCTYPE2', False)

    
    CTYPE2 = property(__CTYPE2.value, __CTYPE2.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cot}CRPIX1 uses Python identifier CRPIX1
    __CRPIX1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRPIX1'), 'CRPIX1', '__httpeuclid_esa_orgschemabascot_astrom_httpeuclid_esa_orgschemabascotCRPIX1', False)

    
    CRPIX1 = property(__CRPIX1.value, __CRPIX1.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cot}CD1_1 uses Python identifier CD1_1
    __CD1_1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD1_1'), 'CD1_1', '__httpeuclid_esa_orgschemabascot_astrom_httpeuclid_esa_orgschemabascotCD1_1', False)

    
    CD1_1 = property(__CD1_1.value, __CD1_1.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cot}CD2_1 uses Python identifier CD2_1
    __CD2_1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD2_1'), 'CD2_1', '__httpeuclid_esa_orgschemabascot_astrom_httpeuclid_esa_orgschemabascotCD2_1', False)

    
    CD2_1 = property(__CD2_1.value, __CD2_1.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cot}CD2_2 uses Python identifier CD2_2
    __CD2_2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD2_2'), 'CD2_2', '__httpeuclid_esa_orgschemabascot_astrom_httpeuclid_esa_orgschemabascotCD2_2', False)

    
    CD2_2 = property(__CD2_2.value, __CD2_2.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cot}CTYPE1 uses Python identifier CTYPE1
    __CTYPE1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CTYPE1'), 'CTYPE1', '__httpeuclid_esa_orgschemabascot_astrom_httpeuclid_esa_orgschemabascotCTYPE1', False)

    
    CTYPE1 = property(__CTYPE1.value, __CTYPE1.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cot}CRVAL1 uses Python identifier CRVAL1
    __CRVAL1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRVAL1'), 'CRVAL1', '__httpeuclid_esa_orgschemabascot_astrom_httpeuclid_esa_orgschemabascotCRVAL1', False)

    
    CRVAL1 = property(__CRVAL1.value, __CRVAL1.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cot}CRPIX2 uses Python identifier CRPIX2
    __CRPIX2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRPIX2'), 'CRPIX2', '__httpeuclid_esa_orgschemabascot_astrom_httpeuclid_esa_orgschemabascotCRPIX2', False)

    
    CRPIX2 = property(__CRPIX2.value, __CRPIX2.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/cot}CD1_2 uses Python identifier CD1_2
    __CD1_2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CD1_2'), 'CD1_2', '__httpeuclid_esa_orgschemabascot_astrom_httpeuclid_esa_orgschemabascotCD1_2', False)

    
    CD1_2 = property(__CD1_2.value, __CD1_2.set, None, None)


    _ElementMap = {
        __CRVAL2.name() : __CRVAL2,
        __CTYPE2.name() : __CTYPE2,
        __CRPIX1.name() : __CRPIX1,
        __CD1_1.name() : __CD1_1,
        __CD2_1.name() : __CD2_1,
        __CD2_2.name() : __CD2_2,
        __CTYPE1.name() : __CTYPE1,
        __CRVAL1.name() : __CRVAL1,
        __CRPIX2.name() : __CRPIX2,
        __CD1_2.name() : __CD1_2
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'astrom', astrom)




astrom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRVAL2'), pyxb.binding.datatypes.float, scope=astrom))

astrom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CTYPE2'), CommonDM.dm.bas.imp_stub.projectionType, scope=astrom))

astrom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRPIX1'), pyxb.binding.datatypes.float, scope=astrom))

astrom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD1_1'), pyxb.binding.datatypes.double, scope=astrom))

astrom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD2_1'), pyxb.binding.datatypes.double, scope=astrom))

astrom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD2_2'), pyxb.binding.datatypes.double, scope=astrom))

astrom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CTYPE1'), CommonDM.dm.bas.imp_stub.projectionType, scope=astrom))

astrom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRVAL1'), pyxb.binding.datatypes.float, scope=astrom))

astrom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRPIX2'), pyxb.binding.datatypes.float, scope=astrom))

astrom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CD1_2'), pyxb.binding.datatypes.double, scope=astrom))
astrom._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astrom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CTYPE1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CTYPE2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CRVAL1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CRVAL2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CRPIX1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CRPIX2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CD1_1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CD1_2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CD2_1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(astrom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CD2_2')), min_occurs=1, max_occurs=1)
    )
astrom._ContentModel = pyxb.binding.content.ParticleModel(astrom._GroupModel, min_occurs=1, max_occurs=1)
