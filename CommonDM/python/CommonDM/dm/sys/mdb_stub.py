# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/sys/mdb_stub.py
# PyXB bindings for NamespaceModule
# NSM:8f18aa402fa0000678654b104d8a6cbeca1b5fe1
# Generated 2014-03-17 11:53:47.256244 by PyXB version 1.1.2
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
import CommonDM.dm.bas.imp.stc_stub
import CommonDM.dm.sys_stub
import CommonDM.dm.bas.utd_stub
import CommonDM.dm.bas.dtd_stub
import CommonDM.dm.bas.fit_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/sys/mdb', create_if_missing=True)
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


# Complex type missionDataBaseSetOfParameters with content type ELEMENT_ONLY
class missionDataBaseSetOfParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'missionDataBaseSetOfParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element EndValidity uses Python identifier EndValidity
    __EndValidity = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'EndValidity'), 'EndValidity', '__httpeuclid_esa_orgschemasysmdb_missionDataBaseSetOfParameters_EndValidity', False)

    
    EndValidity = property(__EndValidity.value, __EndValidity.set, None, None)

    
    # Element EuclidMissionParameterSet uses Python identifier EuclidMissionParameterSet
    __EuclidMissionParameterSet = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'EuclidMissionParameterSet'), 'EuclidMissionParameterSet', '__httpeuclid_esa_orgschemasysmdb_missionDataBaseSetOfParameters_EuclidMissionParameterSet', False)

    
    EuclidMissionParameterSet = property(__EuclidMissionParameterSet.value, __EuclidMissionParameterSet.set, None, None)

    
    # Element Release uses Python identifier Release
    __Release = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Release'), 'Release', '__httpeuclid_esa_orgschemasysmdb_missionDataBaseSetOfParameters_Release', False)

    
    Release = property(__Release.value, __Release.set, None, None)

    
    # Element GenericHeader uses Python identifier GenericHeader
    __GenericHeader = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'GenericHeader'), 'GenericHeader', '__httpeuclid_esa_orgschemasysmdb_missionDataBaseSetOfParameters_GenericHeader', False)

    
    GenericHeader = property(__GenericHeader.value, __GenericHeader.set, None, None)

    
    # Element ReleaseDate uses Python identifier ReleaseDate
    __ReleaseDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ReleaseDate'), 'ReleaseDate', '__httpeuclid_esa_orgschemasysmdb_missionDataBaseSetOfParameters_ReleaseDate', False)

    
    ReleaseDate = property(__ReleaseDate.value, __ReleaseDate.set, None, None)

    
    # Element StartValidity uses Python identifier StartValidity
    __StartValidity = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'StartValidity'), 'StartValidity', '__httpeuclid_esa_orgschemasysmdb_missionDataBaseSetOfParameters_StartValidity', False)

    
    StartValidity = property(__StartValidity.value, __StartValidity.set, None, None)


    _ElementMap = {
        __EndValidity.name() : __EndValidity,
        __EuclidMissionParameterSet.name() : __EuclidMissionParameterSet,
        __Release.name() : __Release,
        __GenericHeader.name() : __GenericHeader,
        __ReleaseDate.name() : __ReleaseDate,
        __StartValidity.name() : __StartValidity
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'missionDataBaseSetOfParameters', missionDataBaseSetOfParameters)


# Complex type listOfThematicParameters with content type ELEMENT_ONLY
class listOfThematicParameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfThematicParameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Parameter'), 'Parameter', '__httpeuclid_esa_orgschemasysmdb_listOfThematicParameters_Parameter', True)

    
    Parameter = property(__Parameter.value, __Parameter.set, None, None)


    _ElementMap = {
        __Parameter.name() : __Parameter
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'listOfThematicParameters', listOfThematicParameters)


# Complex type thematicParameter with content type ELEMENT_ONLY
class thematicParameter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'thematicParameter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Description'), 'Description', '__httpeuclid_esa_orgschemasysmdb_thematicParameter_Description', False)

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__httpeuclid_esa_orgschemasysmdb_thematicParameter_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element Derived uses Python identifier Derived
    __Derived = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Derived'), 'Derived', '__httpeuclid_esa_orgschemasysmdb_thematicParameter_Derived', False)

    
    Derived = property(__Derived.value, __Derived.set, None, None)

    
    # Element Expression uses Python identifier Expression
    __Expression = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Expression'), 'Expression', '__httpeuclid_esa_orgschemasysmdb_thematicParameter_Expression', False)

    
    Expression = property(__Expression.value, __Expression.set, None, None)

    
    # Element Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Source'), 'Source', '__httpeuclid_esa_orgschemasysmdb_thematicParameter_Source', False)

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Element Release uses Python identifier Release
    __Release = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Release'), 'Release', '__httpeuclid_esa_orgschemasysmdb_thematicParameter_Release', False)

    
    Release = property(__Release.value, __Release.set, None, None)

    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpeuclid_esa_orgschemasysmdb_thematicParameter_unit', CommonDM.dm.bas.utd_stub.unit, required=True)
    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__httpeuclid_esa_orgschemasysmdb_thematicParameter_title', pyxb.binding.datatypes.string, required=True)
    
    title = property(__title.value, __title.set, None, None)


    _ElementMap = {
        __Description.name() : __Description,
        __Value.name() : __Value,
        __Derived.name() : __Derived,
        __Expression.name() : __Expression,
        __Source.name() : __Source,
        __Release.name() : __Release
    }
    _AttributeMap = {
        __unit.name() : __unit,
        __title.name() : __title
    }
Namespace.addCategoryObject('typeBinding', u'thematicParameter', thematicParameter)


# Complex type thematicParameterValue with content type ELEMENT_ONLY
class thematicParameterValue (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'thematicParameterValue')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ListOfInteger uses Python identifier ListOfInteger
    __ListOfInteger = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ListOfInteger'), 'ListOfInteger', '__httpeuclid_esa_orgschemasysmdb_thematicParameterValue_ListOfInteger', False)

    
    ListOfInteger = property(__ListOfInteger.value, __ListOfInteger.set, None, None)

    
    # Element Array3D uses Python identifier Array3D
    __Array3D = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Array3D'), 'Array3D', '__httpeuclid_esa_orgschemasysmdb_thematicParameterValue_Array3D', False)

    
    Array3D = property(__Array3D.value, __Array3D.set, None, None)

    
    # Element Array2D uses Python identifier Array2D
    __Array2D = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Array2D'), 'Array2D', '__httpeuclid_esa_orgschemasysmdb_thematicParameterValue_Array2D', False)

    
    Array2D = property(__Array2D.value, __Array2D.set, None, None)

    
    # Element Double uses Python identifier Double
    __Double = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Double'), 'Double', '__httpeuclid_esa_orgschemasysmdb_thematicParameterValue_Double', False)

    
    Double = property(__Double.value, __Double.set, None, None)

    
    # Element ListOfDouble uses Python identifier ListOfDouble
    __ListOfDouble = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ListOfDouble'), 'ListOfDouble', '__httpeuclid_esa_orgschemasysmdb_thematicParameterValue_ListOfDouble', False)

    
    ListOfDouble = property(__ListOfDouble.value, __ListOfDouble.set, None, None)

    
    # Element FitsFile uses Python identifier FitsFile
    __FitsFile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'FitsFile'), 'FitsFile', '__httpeuclid_esa_orgschemasysmdb_thematicParameterValue_FitsFile', False)

    
    FitsFile = property(__FitsFile.value, __FitsFile.set, None, None)

    
    # Element Boolean uses Python identifier Boolean
    __Boolean = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Boolean'), 'Boolean', '__httpeuclid_esa_orgschemasysmdb_thematicParameterValue_Boolean', False)

    
    Boolean = property(__Boolean.value, __Boolean.set, None, None)

    
    # Element Integer uses Python identifier Integer
    __Integer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Integer'), 'Integer', '__httpeuclid_esa_orgschemasysmdb_thematicParameterValue_Integer', False)

    
    Integer = property(__Integer.value, __Integer.set, None, None)

    
    # Element Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Text'), 'Text', '__httpeuclid_esa_orgschemasysmdb_thematicParameterValue_Text', False)

    
    Text = property(__Text.value, __Text.set, None, None)


    _ElementMap = {
        __ListOfInteger.name() : __ListOfInteger,
        __Array3D.name() : __Array3D,
        __Array2D.name() : __Array2D,
        __Double.name() : __Double,
        __ListOfDouble.name() : __ListOfDouble,
        __FitsFile.name() : __FitsFile,
        __Boolean.name() : __Boolean,
        __Integer.name() : __Integer,
        __Text.name() : __Text
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'thematicParameterValue', thematicParameterValue)




missionDataBaseSetOfParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'EndValidity'), CommonDM.dm.bas.imp.stc_stub.dateTime, scope=missionDataBaseSetOfParameters))

missionDataBaseSetOfParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'EuclidMissionParameterSet'), listOfThematicParameters, scope=missionDataBaseSetOfParameters))

missionDataBaseSetOfParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Release'), pyxb.binding.datatypes.string, scope=missionDataBaseSetOfParameters))

missionDataBaseSetOfParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'GenericHeader'), CommonDM.dm.sys_stub.genericHeader, scope=missionDataBaseSetOfParameters))

missionDataBaseSetOfParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReleaseDate'), CommonDM.dm.bas.imp.stc_stub.dateTime, scope=missionDataBaseSetOfParameters))

missionDataBaseSetOfParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'StartValidity'), CommonDM.dm.bas.imp.stc_stub.dateTime, scope=missionDataBaseSetOfParameters))
missionDataBaseSetOfParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(missionDataBaseSetOfParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'GenericHeader')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(missionDataBaseSetOfParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'EuclidMissionParameterSet')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(missionDataBaseSetOfParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'Release')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(missionDataBaseSetOfParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'ReleaseDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(missionDataBaseSetOfParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'StartValidity')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(missionDataBaseSetOfParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'EndValidity')), min_occurs=1, max_occurs=1)
    )
missionDataBaseSetOfParameters._ContentModel = pyxb.binding.content.ParticleModel(missionDataBaseSetOfParameters._GroupModel, min_occurs=1, max_occurs=1)



listOfThematicParameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Parameter'), thematicParameter, scope=listOfThematicParameters))
listOfThematicParameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(listOfThematicParameters._UseForTag(pyxb.namespace.ExpandedName(None, u'Parameter')), min_occurs=1, max_occurs=None)
    )
listOfThematicParameters._ContentModel = pyxb.binding.content.ParticleModel(listOfThematicParameters._GroupModel, min_occurs=1, max_occurs=1)



thematicParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Description'), pyxb.binding.datatypes.string, scope=thematicParameter))

thematicParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), thematicParameterValue, scope=thematicParameter))

thematicParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Derived'), pyxb.binding.datatypes.string, scope=thematicParameter))

thematicParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Expression'), pyxb.binding.datatypes.string, scope=thematicParameter))

thematicParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Source'), pyxb.binding.datatypes.string, scope=thematicParameter))

thematicParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Release'), pyxb.binding.datatypes.string, scope=thematicParameter))
thematicParameter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(thematicParameter._UseForTag(pyxb.namespace.ExpandedName(None, u'Description')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameter._UseForTag(pyxb.namespace.ExpandedName(None, u'Source')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameter._UseForTag(pyxb.namespace.ExpandedName(None, u'Expression')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameter._UseForTag(pyxb.namespace.ExpandedName(None, u'Release')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameter._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameter._UseForTag(pyxb.namespace.ExpandedName(None, u'Derived')), min_occurs=0L, max_occurs=1)
    )
thematicParameter._ContentModel = pyxb.binding.content.ParticleModel(thematicParameter._GroupModel, min_occurs=1, max_occurs=1)



thematicParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ListOfInteger'), CommonDM.dm.bas.dtd_stub.listOfInteger4, scope=thematicParameterValue))

thematicParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Array3D'), CommonDM.dm.bas.dtd_stub.array3D, scope=thematicParameterValue))

thematicParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Array2D'), CommonDM.dm.bas.dtd_stub.array2D, scope=thematicParameterValue))

thematicParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Double'), pyxb.binding.datatypes.double, scope=thematicParameterValue))

thematicParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ListOfDouble'), CommonDM.dm.bas.dtd_stub.listOfDouble, scope=thematicParameterValue))

thematicParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'FitsFile'), CommonDM.dm.bas.fit_stub.fitsFile, scope=thematicParameterValue))

thematicParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Boolean'), pyxb.binding.datatypes.boolean, scope=thematicParameterValue))

thematicParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Integer'), pyxb.binding.datatypes.long, scope=thematicParameterValue))

thematicParameterValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Text'), pyxb.binding.datatypes.string, scope=thematicParameterValue))
thematicParameterValue._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(thematicParameterValue._UseForTag(pyxb.namespace.ExpandedName(None, u'Text')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameterValue._UseForTag(pyxb.namespace.ExpandedName(None, u'Double')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameterValue._UseForTag(pyxb.namespace.ExpandedName(None, u'ListOfDouble')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameterValue._UseForTag(pyxb.namespace.ExpandedName(None, u'Integer')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameterValue._UseForTag(pyxb.namespace.ExpandedName(None, u'ListOfInteger')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameterValue._UseForTag(pyxb.namespace.ExpandedName(None, u'Array2D')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameterValue._UseForTag(pyxb.namespace.ExpandedName(None, u'Array3D')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameterValue._UseForTag(pyxb.namespace.ExpandedName(None, u'Boolean')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(thematicParameterValue._UseForTag(pyxb.namespace.ExpandedName(None, u'FitsFile')), min_occurs=1, max_occurs=1)
    )
thematicParameterValue._ContentModel = pyxb.binding.content.ParticleModel(thematicParameterValue._GroupModel, min_occurs=1, max_occurs=1)
