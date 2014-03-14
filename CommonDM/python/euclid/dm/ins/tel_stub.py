# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/ins/tel_stub.py
# PyXB bindings for NamespaceModule
# NSM:a659c9609d911b0b0de7dec344c20026ccc5f00c
# Generated 2014-03-14 09:43:27.464087 by PyXB version 1.1.2
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
import euclid.dm.bas.utd_stub
import euclid.dm.ins_stub
import euclid.dm.sys.sgs_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/ins/tel', create_if_missing=True)
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


# Complex type telescopeOptics with content type ELEMENT_ONLY
class telescopeOptics (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'telescopeOptics')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/tel}Obscuration uses Python identifier Obscuration
    __Obscuration = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Obscuration'), 'Obscuration', '__httpeuclid_esa_orgschemainstel_telescopeOptics_httpeuclid_esa_orgschemainstelObscuration', False)

    
    Obscuration = property(__Obscuration.value, __Obscuration.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}ComputationDate uses Python identifier ComputationDate
    __ComputationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), 'ComputationDate', '__httpeuclid_esa_orgschemainstel_telescopeOptics_httpeuclid_esa_orgschemainstelComputationDate', False)

    
    ComputationDate = property(__ComputationDate.value, __ComputationDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemainstel_telescopeOptics_httpeuclid_esa_orgschemainstelVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}Diameter uses Python identifier Diameter
    __Diameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Diameter'), 'Diameter', '__httpeuclid_esa_orgschemainstel_telescopeOptics_httpeuclid_esa_orgschemainstelDiameter', False)

    
    Diameter = property(__Diameter.value, __Diameter.set, None, None)


    _ElementMap = {
        __Obscuration.name() : __Obscuration,
        __ComputationDate.name() : __ComputationDate,
        __Version.name() : __Version,
        __Diameter.name() : __Diameter
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'telescopeOptics', telescopeOptics)


# Complex type diameter with content type ELEMENT_ONLY
class diameter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'diameter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/tel}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemainstel_diameter_httpeuclid_esa_orgschemainstelUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemainstel_diameter_httpeuclid_esa_orgschemainstelValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'diameter', diameter)


# Complex type scatteredNoiseModel with content type ELEMENT_ONLY
class scatteredNoiseModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'scatteredNoiseModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/tel}Flux uses Python identifier Flux
    __Flux = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flux'), 'Flux', '__httpeuclid_esa_orgschemainstel_scatteredNoiseModel_httpeuclid_esa_orgschemainstelFlux', False)

    
    Flux = property(__Flux.value, __Flux.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}ComputationDate uses Python identifier ComputationDate
    __ComputationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), 'ComputationDate', '__httpeuclid_esa_orgschemainstel_scatteredNoiseModel_httpeuclid_esa_orgschemainstelComputationDate', False)

    
    ComputationDate = property(__ComputationDate.value, __ComputationDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), 'Wavelength', '__httpeuclid_esa_orgschemainstel_scatteredNoiseModel_httpeuclid_esa_orgschemainstelWavelength', False)

    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}CalibrationDataPath uses Python identifier CalibrationDataPath
    __CalibrationDataPath = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath'), 'CalibrationDataPath', '__httpeuclid_esa_orgschemainstel_scatteredNoiseModel_httpeuclid_esa_orgschemainstelCalibrationDataPath', False)

    
    CalibrationDataPath = property(__CalibrationDataPath.value, __CalibrationDataPath.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemainstel_scatteredNoiseModel_httpeuclid_esa_orgschemainstelVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)


    _ElementMap = {
        __Flux.name() : __Flux,
        __ComputationDate.name() : __ComputationDate,
        __Wavelength.name() : __Wavelength,
        __CalibrationDataPath.name() : __CalibrationDataPath,
        __Version.name() : __Version
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'scatteredNoiseModel', scatteredNoiseModel)


# Complex type obscuration with content type ELEMENT_ONLY
class obscuration (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'obscuration')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/tel}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemainstel_obscuration_httpeuclid_esa_orgschemainstelUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemainstel_obscuration_httpeuclid_esa_orgschemainstelValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'obscuration', obscuration)


# Complex type telescopeNoiseModel with content type ELEMENT_ONLY
class telescopeNoiseModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'telescopeNoiseModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/ins/tel}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemainstel_telescopeNoiseModel_httpeuclid_esa_orgschemainstelVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), 'Wavelength', '__httpeuclid_esa_orgschemainstel_telescopeNoiseModel_httpeuclid_esa_orgschemainstelWavelength', False)

    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}ComputationDate uses Python identifier ComputationDate
    __ComputationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), 'ComputationDate', '__httpeuclid_esa_orgschemainstel_telescopeNoiseModel_httpeuclid_esa_orgschemainstelComputationDate', False)

    
    ComputationDate = property(__ComputationDate.value, __ComputationDate.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}CalibrationDataPath uses Python identifier CalibrationDataPath
    __CalibrationDataPath = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath'), 'CalibrationDataPath', '__httpeuclid_esa_orgschemainstel_telescopeNoiseModel_httpeuclid_esa_orgschemainstelCalibrationDataPath', False)

    
    CalibrationDataPath = property(__CalibrationDataPath.value, __CalibrationDataPath.set, None, None)

    
    # Element {http://euclid.esa.org/schema/ins/tel}Flux uses Python identifier Flux
    __Flux = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Flux'), 'Flux', '__httpeuclid_esa_orgschemainstel_telescopeNoiseModel_httpeuclid_esa_orgschemainstelFlux', False)

    
    Flux = property(__Flux.value, __Flux.set, None, None)


    _ElementMap = {
        __Version.name() : __Version,
        __Wavelength.name() : __Wavelength,
        __ComputationDate.name() : __ComputationDate,
        __CalibrationDataPath.name() : __CalibrationDataPath,
        __Flux.name() : __Flux
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'telescopeNoiseModel', telescopeNoiseModel)




telescopeOptics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Obscuration'), obscuration, scope=telescopeOptics))

telescopeOptics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), pyxb.binding.datatypes.dateTime, scope=telescopeOptics))

telescopeOptics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), euclid.dm.sys_stub.version, scope=telescopeOptics))

telescopeOptics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Diameter'), diameter, scope=telescopeOptics))
telescopeOptics._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(telescopeOptics._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(telescopeOptics._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(telescopeOptics._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Diameter')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(telescopeOptics._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Obscuration')), min_occurs=1, max_occurs=1)
    )
telescopeOptics._ContentModel = pyxb.binding.content.ParticleModel(telescopeOptics._GroupModel, min_occurs=1, max_occurs=1)



diameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), euclid.dm.bas.utd_stub.unit, scope=diameter))

diameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.double, scope=diameter))
diameter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(diameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(diameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
diameter._ContentModel = pyxb.binding.content.ParticleModel(diameter._GroupModel, min_occurs=1, max_occurs=1)



scatteredNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flux'), euclid.dm.ins_stub.flux, scope=scatteredNoiseModel))

scatteredNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), pyxb.binding.datatypes.dateTime, scope=scatteredNoiseModel))

scatteredNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), euclid.dm.ins_stub.wavelength, scope=scatteredNoiseModel))

scatteredNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath'), euclid.dm.sys.sgs_stub.dataContainer, scope=scatteredNoiseModel))

scatteredNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), euclid.dm.sys_stub.version, scope=scatteredNoiseModel))
scatteredNoiseModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(scatteredNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(scatteredNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(scatteredNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(scatteredNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Wavelength')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(scatteredNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flux')), min_occurs=1, max_occurs=1)
    )
scatteredNoiseModel._ContentModel = pyxb.binding.content.ParticleModel(scatteredNoiseModel._GroupModel, min_occurs=1, max_occurs=1)



obscuration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), euclid.dm.bas.utd_stub.unit, scope=obscuration))

obscuration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.double, scope=obscuration))
obscuration._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(obscuration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(obscuration._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
obscuration._ContentModel = pyxb.binding.content.ParticleModel(obscuration._GroupModel, min_occurs=1, max_occurs=1)



telescopeNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), euclid.dm.sys_stub.version, scope=telescopeNoiseModel))

telescopeNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wavelength'), euclid.dm.ins_stub.wavelength, scope=telescopeNoiseModel))

telescopeNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate'), pyxb.binding.datatypes.dateTime, scope=telescopeNoiseModel))

telescopeNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath'), euclid.dm.sys.sgs_stub.dataContainer, scope=telescopeNoiseModel))

telescopeNoiseModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flux'), euclid.dm.ins_stub.flux, scope=telescopeNoiseModel))
telescopeNoiseModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(telescopeNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(telescopeNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComputationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(telescopeNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CalibrationDataPath')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(telescopeNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Wavelength')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(telescopeNoiseModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flux')), min_occurs=1, max_occurs=1)
    )
telescopeNoiseModel._ContentModel = pyxb.binding.content.ParticleModel(telescopeNoiseModel._GroupModel, min_occurs=1, max_occurs=1)
