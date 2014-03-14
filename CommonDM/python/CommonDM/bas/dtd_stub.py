# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/bas/dtd_stub.py
# PyXB bindings for NamespaceModule
# NSM:b271ffc25c73f887dbff4e054cfd41e733c35b7f
# Generated 2014-03-14 15:21:54.438873 by PyXB version 1.1.2
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
import CommonDM.bas.utd_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/dtd', create_if_missing=True)
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


# List SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfInteger1 (pyxb.binding.basis.STD_list):

    """An unbounded list of one Byte Integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfInteger1')
    _Documentation = u'An unbounded list of one Byte Integer.'

    _ItemType = pyxb.binding.datatypes.byte
listOfInteger1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfInteger1', listOfInteger1)

# List SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfDouble (pyxb.binding.basis.STD_list):

    """An unbounded list of doubles (space separated). Used for tabulated data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfDouble')
    _Documentation = u'An unbounded list of doubles (space separated). Used for tabulated data.'

    _ItemType = pyxb.binding.datatypes.double
listOfDouble._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfDouble', listOfDouble)

# List SimpleTypeDefinition
# superclasses listOfDouble
class listOf2Double (pyxb.binding.basis.STD_list):

    """Space separated list of 2 double values, used for array2D."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOf2Double')
    _Documentation = u'Space separated list of 2 double values, used for array2D.'

    _ItemType = pyxb.binding.datatypes.double
listOf2Double._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
listOf2Double._InitializeFacetMap(listOf2Double._CF_length)
Namespace.addCategoryObject('typeBinding', u'listOf2Double', listOf2Double)

# Atomic SimpleTypeDefinition
class positiveDouble (pyxb.binding.datatypes.double):

    """Double between 0 (inclusive) and infinity"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positiveDouble')
    _Documentation = u'Double between 0 (inclusive) and infinity'
positiveDouble._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveDouble, value=pyxb.binding.datatypes.double(0.0))
positiveDouble._InitializeFacetMap(positiveDouble._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'positiveDouble', positiveDouble)

# Atomic SimpleTypeDefinition
class var64String (pyxb.binding.datatypes.string):

    """Character string : exact length 64"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'var64String')
    _Documentation = u'Character string : exact length 64'
var64String._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
var64String._InitializeFacetMap(var64String._CF_length)
Namespace.addCategoryObject('typeBinding', u'var64String', var64String)

# List SimpleTypeDefinition
# superclasses listOfDouble
class listOf3Double (pyxb.binding.basis.STD_list):

    """Space separated list of 3 double values, used for matrix or Array3D."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOf3Double')
    _Documentation = u'Space separated list of 3 double values, used for matrix or Array3D.'

    _ItemType = pyxb.binding.datatypes.double
listOf3Double._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
listOf3Double._InitializeFacetMap(listOf3Double._CF_length)
Namespace.addCategoryObject('typeBinding', u'listOf3Double', listOf3Double)

# List SimpleTypeDefinition
# superclasses listOfDouble
class listOf6Double (pyxb.binding.basis.STD_list):

    """Space separated list of 6 double values, used for matrix."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOf6Double')
    _Documentation = u'Space separated list of 6 double values, used for matrix.'

    _ItemType = pyxb.binding.datatypes.double
listOf6Double._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(6L))
listOf6Double._InitializeFacetMap(listOf6Double._CF_length)
Namespace.addCategoryObject('typeBinding', u'listOf6Double', listOf6Double)

# Atomic SimpleTypeDefinition
class degAngle (pyxb.binding.datatypes.double):

    """Angle in degrees between -180 and 360		"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'degAngle')
    _Documentation = u'Angle in degrees between -180 and 360\t\t'
degAngle._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes.anySimpleType(u'360.0'))
degAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=degAngle, value=pyxb.binding.datatypes.double(-180.0))
degAngle._InitializeFacetMap(degAngle._CF_maxExclusive,
   degAngle._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'degAngle', degAngle)

# Atomic SimpleTypeDefinition
class curveShape (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The position of the points connecting the vertices (or end points) of a polygon in space (so on a sphere) may be a large circle (or geodesic) or a line (iso coordinate on an axis)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'curveShape')
    _Documentation = u'The position of the points connecting the vertices (or end points) of a polygon in space (so on a sphere) may be a large circle (or geodesic) or a line (iso coordinate on an axis).'
curveShape._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=curveShape, enum_prefix=None)
curveShape.line = curveShape._CF_enumeration.addEnumeration(unicode_value=u'line')
curveShape.great_circle = curveShape._CF_enumeration.addEnumeration(unicode_value=u'great circle')
curveShape._InitializeFacetMap(curveShape._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'curveShape', curveShape)

# Atomic SimpleTypeDefinition
class nameRestriction (pyxb.binding.datatypes.string):

    """Basic naming convention: length between 4 and 100 characters, white spaces collapsed"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameRestriction')
    _Documentation = u'Basic naming convention: length between 4 and 100 characters, white spaces collapsed'
nameRestriction._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
nameRestriction._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
nameRestriction._InitializeFacetMap(nameRestriction._CF_minLength,
   nameRestriction._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'nameRestriction', nameRestriction)

# List SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfInteger2 (pyxb.binding.basis.STD_list):

    """An unbounded list of two Bytes (short) Integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfInteger2')
    _Documentation = u'An unbounded list of two Bytes (short) Integer.'

    _ItemType = pyxb.binding.datatypes.short
listOfInteger2._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfInteger2', listOfInteger2)

# List SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfInteger8 (pyxb.binding.basis.STD_list):

    """An unbounded list of 8  Bytes (int) Integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfInteger8')
    _Documentation = u'An unbounded list of 8  Bytes (int) Integer.'

    _ItemType = pyxb.binding.datatypes.long
listOfInteger8._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfInteger8', listOfInteger8)

# List SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfFloat (pyxb.binding.basis.STD_list):

    """An unbounded list of float. Used for tabulated data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfFloat')
    _Documentation = u'An unbounded list of float. Used for tabulated data.'

    _ItemType = pyxb.binding.datatypes.float
listOfFloat._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfFloat', listOfFloat)

# Atomic SimpleTypeDefinition
class hexaString (pyxb.binding.datatypes.string):

    """An hexadecimal number."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hexaString')
    _Documentation = u'An hexadecimal number.'
hexaString._CF_pattern = pyxb.binding.facets.CF_pattern()
hexaString._CF_pattern.addPattern(pattern=u'[0-9,A-F,a-f]*')
hexaString._InitializeFacetMap(hexaString._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'hexaString', hexaString)

# Atomic SimpleTypeDefinition
class negativeDouble (pyxb.binding.datatypes.double):

    """Double between  infinity and O (inclusive)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'negativeDouble')
    _Documentation = u'Double between  infinity and O (inclusive)'
negativeDouble._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=negativeDouble, value=pyxb.binding.datatypes.double(0.0))
negativeDouble._InitializeFacetMap(negativeDouble._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', u'negativeDouble', negativeDouble)

# Atomic SimpleTypeDefinition
class percentValue (pyxb.binding.datatypes.double):

    """Double between  0 and 100 inclusive"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'percentValue')
    _Documentation = u'Double between  0 and 100 inclusive'
percentValue._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=percentValue, value=pyxb.binding.datatypes.double(100.0))
percentValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=percentValue, value=pyxb.binding.datatypes.double(0.0))
percentValue._InitializeFacetMap(percentValue._CF_maxInclusive,
   percentValue._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'percentValue', percentValue)

# List SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfInteger4 (pyxb.binding.basis.STD_list):

    """An unbounded list of 4  Bytes (int) Integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfInteger4')
    _Documentation = u'An unbounded list of 4  Bytes (int) Integer.'

    _ItemType = pyxb.binding.datatypes.int
listOfInteger4._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfInteger4', listOfInteger4)

# Complex type double1Type with content type SIMPLE
class double1Type (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'double1Type')
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpeuclid_esa_orgschemabasdtd_double1Type_unit', CommonDM.bas.utd_stub.unit)
    
    unit = property(__unit.value, __unit.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __unit.name() : __unit
    }
Namespace.addCategoryObject('typeBinding', u'double1Type', double1Type)


# Complex type double4Type with content type ELEMENT_ONLY
class double4Type (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'double4Type')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element M12 uses Python identifier M12
    __M12 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M12'), 'M12', '__httpeuclid_esa_orgschemabasdtd_double4Type_M12', False)

    
    M12 = property(__M12.value, __M12.set, None, None)

    
    # Element M21 uses Python identifier M21
    __M21 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M21'), 'M21', '__httpeuclid_esa_orgschemabasdtd_double4Type_M21', False)

    
    M21 = property(__M21.value, __M21.set, None, None)

    
    # Element M11 uses Python identifier M11
    __M11 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M11'), 'M11', '__httpeuclid_esa_orgschemabasdtd_double4Type_M11', False)

    
    M11 = property(__M11.value, __M11.set, None, None)

    
    # Element M22 uses Python identifier M22
    __M22 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M22'), 'M22', '__httpeuclid_esa_orgschemabasdtd_double4Type_M22', False)

    
    M22 = property(__M22.value, __M22.set, None, None)

    
    # Attribute MijUnit uses Python identifier MijUnit
    __MijUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'MijUnit'), 'MijUnit', '__httpeuclid_esa_orgschemabasdtd_double4Type_MijUnit', CommonDM.bas.utd_stub.unit)
    
    MijUnit = property(__MijUnit.value, __MijUnit.set, None, None)


    _ElementMap = {
        __M12.name() : __M12,
        __M21.name() : __M21,
        __M11.name() : __M11,
        __M22.name() : __M22
    }
    _AttributeMap = {
        __MijUnit.name() : __MijUnit
    }
Namespace.addCategoryObject('typeBinding', u'double4Type', double4Type)


# Complex type double2Type with content type ELEMENT_ONLY
class double2Type (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'double2Type')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element C2 uses Python identifier C2
    __C2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'C2'), 'C2', '__httpeuclid_esa_orgschemabasdtd_double2Type_C2', False)

    
    C2 = property(__C2.value, __C2.set, None, None)

    
    # Element C1 uses Python identifier C1
    __C1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'C1'), 'C1', '__httpeuclid_esa_orgschemabasdtd_double2Type_C1', False)

    
    C1 = property(__C1.value, __C1.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasdtd_double2Type_CoordUnit', CommonDM.bas.utd_stub.unit)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)


    _ElementMap = {
        __C2.name() : __C2,
        __C1.name() : __C1
    }
    _AttributeMap = {
        __CoordUnit.name() : __CoordUnit
    }
Namespace.addCategoryObject('typeBinding', u'double2Type', double2Type)


# Complex type double3Type with content type ELEMENT_ONLY
class double3Type (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'double3Type')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element C3 uses Python identifier C3
    __C3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'C3'), 'C3', '__httpeuclid_esa_orgschemabasdtd_double3Type_C3', False)

    
    C3 = property(__C3.value, __C3.set, None, None)

    
    # Element C1 uses Python identifier C1
    __C1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'C1'), 'C1', '__httpeuclid_esa_orgschemabasdtd_double3Type_C1', False)

    
    C1 = property(__C1.value, __C1.set, None, None)

    
    # Element C2 uses Python identifier C2
    __C2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'C2'), 'C2', '__httpeuclid_esa_orgschemabasdtd_double3Type_C2', False)

    
    C2 = property(__C2.value, __C2.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasdtd_double3Type_CoordUnit', CommonDM.bas.utd_stub.unit)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)


    _ElementMap = {
        __C3.name() : __C3,
        __C1.name() : __C1,
        __C2.name() : __C2
    }
    _AttributeMap = {
        __CoordUnit.name() : __CoordUnit
    }
Namespace.addCategoryObject('typeBinding', u'double3Type', double3Type)


# Complex type doubleUnit with content type ELEMENT_ONLY
class doubleUnit (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'doubleUnit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemabasdtd_doubleUnit_Unit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasdtd_doubleUnit_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Unit.name() : __Unit,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'doubleUnit', doubleUnit)


# Complex type curve2Type with content type ELEMENT_ONLY
class curve2Type (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'curve2Type')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element P2 uses Python identifier P2
    __P2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'P2'), 'P2', '__httpeuclid_esa_orgschemabasdtd_curve2Type_P2', False)

    
    P2 = property(__P2.value, __P2.set, None, None)

    
    # Element P1 uses Python identifier P1
    __P1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'P1'), 'P1', '__httpeuclid_esa_orgschemabasdtd_curve2Type_P1', False)

    
    P1 = property(__P1.value, __P1.set, None, None)

    
    # Attribute CurveShape uses Python identifier CurveShape
    __CurveShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CurveShape'), 'CurveShape', '__httpeuclid_esa_orgschemabasdtd_curve2Type_CurveShape', curveShape)
    
    CurveShape = property(__CurveShape.value, __CurveShape.set, None, None)


    _ElementMap = {
        __P2.name() : __P2,
        __P1.name() : __P1
    }
    _AttributeMap = {
        __CurveShape.name() : __CurveShape
    }
Namespace.addCategoryObject('typeBinding', u'curve2Type', curve2Type)


# Complex type curve3Type with content type ELEMENT_ONLY
class curve3Type (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'curve3Type')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element P2 uses Python identifier P2
    __P2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'P2'), 'P2', '__httpeuclid_esa_orgschemabasdtd_curve3Type_P2', False)

    
    P2 = property(__P2.value, __P2.set, None, None)

    
    # Element P1 uses Python identifier P1
    __P1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'P1'), 'P1', '__httpeuclid_esa_orgschemabasdtd_curve3Type_P1', False)

    
    P1 = property(__P1.value, __P1.set, None, None)

    
    # Attribute CurveShape uses Python identifier CurveShape
    __CurveShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CurveShape'), 'CurveShape', '__httpeuclid_esa_orgschemabasdtd_curve3Type_CurveShape', curveShape)
    
    CurveShape = property(__CurveShape.value, __CurveShape.set, None, None)


    _ElementMap = {
        __P2.name() : __P2,
        __P1.name() : __P1
    }
    _AttributeMap = {
        __CurveShape.name() : __CurveShape
    }
Namespace.addCategoryObject('typeBinding', u'curve3Type', curve3Type)


# Complex type matrixDouble3x3 with content type ELEMENT_ONLY
class matrixDouble3x3 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'matrixDouble3x3')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element row3 uses Python identifier row3
    __row3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'row3'), 'row3', '__httpeuclid_esa_orgschemabasdtd_matrixDouble3x3_row3', True)

    
    row3 = property(__row3.value, __row3.set, None, None)

    
    # Element row1 uses Python identifier row1
    __row1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'row1'), 'row1', '__httpeuclid_esa_orgschemabasdtd_matrixDouble3x3_row1', True)

    
    row1 = property(__row1.value, __row1.set, None, None)

    
    # Element row2 uses Python identifier row2
    __row2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'row2'), 'row2', '__httpeuclid_esa_orgschemabasdtd_matrixDouble3x3_row2', True)

    
    row2 = property(__row2.value, __row2.set, None, None)


    _ElementMap = {
        __row3.name() : __row3,
        __row1.name() : __row1,
        __row2.name() : __row2
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'matrixDouble3x3', matrixDouble3x3)


# Complex type matrixDouble6x6 with content type ELEMENT_ONLY
class matrixDouble6x6 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'matrixDouble6x6')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element row5 uses Python identifier row5
    __row5 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'row5'), 'row5', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row5', False)

    
    row5 = property(__row5.value, __row5.set, None, None)

    
    # Element row1 uses Python identifier row1
    __row1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'row1'), 'row1', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row1', False)

    
    row1 = property(__row1.value, __row1.set, None, None)

    
    # Element row6 uses Python identifier row6
    __row6 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'row6'), 'row6', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row6', False)

    
    row6 = property(__row6.value, __row6.set, None, None)

    
    # Element row3 uses Python identifier row3
    __row3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'row3'), 'row3', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row3', False)

    
    row3 = property(__row3.value, __row3.set, None, None)

    
    # Element row2 uses Python identifier row2
    __row2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'row2'), 'row2', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row2', False)

    
    row2 = property(__row2.value, __row2.set, None, None)

    
    # Element row4 uses Python identifier row4
    __row4 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'row4'), 'row4', '__httpeuclid_esa_orgschemabasdtd_matrixDouble6x6_row4', False)

    
    row4 = property(__row4.value, __row4.set, None, None)


    _ElementMap = {
        __row5.name() : __row5,
        __row1.name() : __row1,
        __row6.name() : __row6,
        __row3.name() : __row3,
        __row2.name() : __row2,
        __row4.name() : __row4
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'matrixDouble6x6', matrixDouble6x6)


# Complex type array2D with content type ELEMENT_ONLY
class array2D (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'array2D')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PairedValues uses Python identifier PairedValues
    __PairedValues = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'PairedValues'), 'PairedValues', '__httpeuclid_esa_orgschemabasdtd_array2D_PairedValues', True)

    
    PairedValues = property(__PairedValues.value, __PairedValues.set, None, None)

    
    # Element SizeOfArray uses Python identifier SizeOfArray
    __SizeOfArray = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SizeOfArray'), 'SizeOfArray', '__httpeuclid_esa_orgschemabasdtd_array2D_SizeOfArray', False)

    
    SizeOfArray = property(__SizeOfArray.value, __SizeOfArray.set, None, None)

    
    # Attribute Yunit uses Python identifier Yunit
    __Yunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Yunit'), 'Yunit', '__httpeuclid_esa_orgschemabasdtd_array2D_Yunit', CommonDM.bas.utd_stub.unit, required=True)
    
    Yunit = property(__Yunit.value, __Yunit.set, None, None)

    
    # Attribute Xunit uses Python identifier Xunit
    __Xunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Xunit'), 'Xunit', '__httpeuclid_esa_orgschemabasdtd_array2D_Xunit', CommonDM.bas.utd_stub.unit, required=True)
    
    Xunit = property(__Xunit.value, __Xunit.set, None, None)


    _ElementMap = {
        __PairedValues.name() : __PairedValues,
        __SizeOfArray.name() : __SizeOfArray
    }
    _AttributeMap = {
        __Yunit.name() : __Yunit,
        __Xunit.name() : __Xunit
    }
Namespace.addCategoryObject('typeBinding', u'array2D', array2D)


# Complex type array3D with content type ELEMENT_ONLY
class array3D (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'array3D')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element TripletValues uses Python identifier TripletValues
    __TripletValues = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'TripletValues'), 'TripletValues', '__httpeuclid_esa_orgschemabasdtd_array3D_TripletValues', True)

    
    TripletValues = property(__TripletValues.value, __TripletValues.set, None, None)

    
    # Element SizeOfArray uses Python identifier SizeOfArray
    __SizeOfArray = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SizeOfArray'), 'SizeOfArray', '__httpeuclid_esa_orgschemabasdtd_array3D_SizeOfArray', False)

    
    SizeOfArray = property(__SizeOfArray.value, __SizeOfArray.set, None, None)

    
    # Attribute Xunit uses Python identifier Xunit
    __Xunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Xunit'), 'Xunit', '__httpeuclid_esa_orgschemabasdtd_array3D_Xunit', CommonDM.bas.utd_stub.unit, required=True)
    
    Xunit = property(__Xunit.value, __Xunit.set, None, None)

    
    # Attribute Zunit uses Python identifier Zunit
    __Zunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Zunit'), 'Zunit', '__httpeuclid_esa_orgschemabasdtd_array3D_Zunit', CommonDM.bas.utd_stub.unit, required=True)
    
    Zunit = property(__Zunit.value, __Zunit.set, None, None)

    
    # Attribute Yunit uses Python identifier Yunit
    __Yunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Yunit'), 'Yunit', '__httpeuclid_esa_orgschemabasdtd_array3D_Yunit', CommonDM.bas.utd_stub.unit, required=True)
    
    Yunit = property(__Yunit.value, __Yunit.set, None, None)


    _ElementMap = {
        __TripletValues.name() : __TripletValues,
        __SizeOfArray.name() : __SizeOfArray
    }
    _AttributeMap = {
        __Xunit.name() : __Xunit,
        __Zunit.name() : __Zunit,
        __Yunit.name() : __Yunit
    }
Namespace.addCategoryObject('typeBinding', u'array3D', array3D)


# Complex type double9Type with content type ELEMENT_ONLY
class double9Type (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'double9Type')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element M21 uses Python identifier M21
    __M21 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M21'), 'M21', '__httpeuclid_esa_orgschemabasdtd_double9Type_M21', False)

    
    M21 = property(__M21.value, __M21.set, None, None)

    
    # Element M12 uses Python identifier M12
    __M12 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M12'), 'M12', '__httpeuclid_esa_orgschemabasdtd_double9Type_M12', False)

    
    M12 = property(__M12.value, __M12.set, None, None)

    
    # Element M11 uses Python identifier M11
    __M11 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M11'), 'M11', '__httpeuclid_esa_orgschemabasdtd_double9Type_M11', False)

    
    M11 = property(__M11.value, __M11.set, None, None)

    
    # Element M13 uses Python identifier M13
    __M13 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M13'), 'M13', '__httpeuclid_esa_orgschemabasdtd_double9Type_M13', False)

    
    M13 = property(__M13.value, __M13.set, None, None)

    
    # Element M33 uses Python identifier M33
    __M33 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M33'), 'M33', '__httpeuclid_esa_orgschemabasdtd_double9Type_M33', False)

    
    M33 = property(__M33.value, __M33.set, None, None)

    
    # Element M23 uses Python identifier M23
    __M23 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M23'), 'M23', '__httpeuclid_esa_orgschemabasdtd_double9Type_M23', False)

    
    M23 = property(__M23.value, __M23.set, None, None)

    
    # Element M22 uses Python identifier M22
    __M22 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M22'), 'M22', '__httpeuclid_esa_orgschemabasdtd_double9Type_M22', False)

    
    M22 = property(__M22.value, __M22.set, None, None)

    
    # Element M31 uses Python identifier M31
    __M31 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M31'), 'M31', '__httpeuclid_esa_orgschemabasdtd_double9Type_M31', False)

    
    M31 = property(__M31.value, __M31.set, None, None)

    
    # Element M32 uses Python identifier M32
    __M32 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'M32'), 'M32', '__httpeuclid_esa_orgschemabasdtd_double9Type_M32', False)

    
    M32 = property(__M32.value, __M32.set, None, None)

    
    # Attribute MijUnit uses Python identifier MijUnit
    __MijUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'MijUnit'), 'MijUnit', '__httpeuclid_esa_orgschemabasdtd_double9Type_MijUnit', CommonDM.bas.utd_stub.unit)
    
    MijUnit = property(__MijUnit.value, __MijUnit.set, None, None)


    _ElementMap = {
        __M21.name() : __M21,
        __M12.name() : __M12,
        __M11.name() : __M11,
        __M13.name() : __M13,
        __M33.name() : __M33,
        __M23.name() : __M23,
        __M22.name() : __M22,
        __M31.name() : __M31,
        __M32.name() : __M32
    }
    _AttributeMap = {
        __MijUnit.name() : __MijUnit
    }
Namespace.addCategoryObject('typeBinding', u'double9Type', double9Type)




double4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M12'), pyxb.binding.datatypes.double, scope=double4Type))

double4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M21'), pyxb.binding.datatypes.double, scope=double4Type))

double4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M11'), pyxb.binding.datatypes.double, scope=double4Type))

double4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M22'), pyxb.binding.datatypes.double, scope=double4Type))
double4Type._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(double4Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M11')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double4Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M12')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double4Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M21')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double4Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M22')), min_occurs=1, max_occurs=1)
    )
double4Type._ContentModel = pyxb.binding.content.ParticleModel(double4Type._GroupModel, min_occurs=1, max_occurs=1)



double2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'C2'), double1Type, scope=double2Type))

double2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'C1'), double1Type, scope=double2Type))
double2Type._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(double2Type._UseForTag(pyxb.namespace.ExpandedName(None, u'C1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double2Type._UseForTag(pyxb.namespace.ExpandedName(None, u'C2')), min_occurs=1, max_occurs=1)
    )
double2Type._ContentModel = pyxb.binding.content.ParticleModel(double2Type._GroupModel, min_occurs=1, max_occurs=1)



double3Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'C3'), double1Type, scope=double3Type))

double3Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'C1'), double1Type, scope=double3Type))

double3Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'C2'), double1Type, scope=double3Type))
double3Type._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(double3Type._UseForTag(pyxb.namespace.ExpandedName(None, u'C1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double3Type._UseForTag(pyxb.namespace.ExpandedName(None, u'C2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double3Type._UseForTag(pyxb.namespace.ExpandedName(None, u'C3')), min_occurs=1, max_occurs=1)
    )
double3Type._ContentModel = pyxb.binding.content.ParticleModel(double3Type._GroupModel, min_occurs=1, max_occurs=1)



doubleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Unit'), CommonDM.bas.utd_stub.unit, scope=doubleUnit))

doubleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), pyxb.binding.datatypes.double, scope=doubleUnit))
doubleUnit._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(doubleUnit._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(doubleUnit._UseForTag(pyxb.namespace.ExpandedName(None, u'Unit')), min_occurs=1, max_occurs=1)
    )
doubleUnit._ContentModel = pyxb.binding.content.ParticleModel(doubleUnit._GroupModel, min_occurs=1, max_occurs=1)



curve2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'P2'), double2Type, scope=curve2Type))

curve2Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'P1'), double2Type, scope=curve2Type))
curve2Type._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(curve2Type._UseForTag(pyxb.namespace.ExpandedName(None, u'P1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(curve2Type._UseForTag(pyxb.namespace.ExpandedName(None, u'P2')), min_occurs=1, max_occurs=1)
    )
curve2Type._ContentModel = pyxb.binding.content.ParticleModel(curve2Type._GroupModel, min_occurs=1, max_occurs=1)



curve3Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'P2'), double3Type, scope=curve3Type))

curve3Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'P1'), double3Type, scope=curve3Type))
curve3Type._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(curve3Type._UseForTag(pyxb.namespace.ExpandedName(None, u'P1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(curve3Type._UseForTag(pyxb.namespace.ExpandedName(None, u'P2')), min_occurs=1, max_occurs=1)
    )
curve3Type._ContentModel = pyxb.binding.content.ParticleModel(curve3Type._GroupModel, min_occurs=1, max_occurs=1)



matrixDouble3x3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row3'), listOf3Double, scope=matrixDouble3x3))

matrixDouble3x3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row1'), listOf3Double, scope=matrixDouble3x3))

matrixDouble3x3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row2'), listOf3Double, scope=matrixDouble3x3))
matrixDouble3x3._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(matrixDouble3x3._UseForTag(pyxb.namespace.ExpandedName(None, u'row1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(matrixDouble3x3._UseForTag(pyxb.namespace.ExpandedName(None, u'row2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(matrixDouble3x3._UseForTag(pyxb.namespace.ExpandedName(None, u'row3')), min_occurs=1, max_occurs=1)
    )
matrixDouble3x3._ContentModel = pyxb.binding.content.ParticleModel(matrixDouble3x3._GroupModel, min_occurs=3L, max_occurs=3L)



matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row5'), listOf6Double, scope=matrixDouble6x6))

matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row1'), listOf6Double, scope=matrixDouble6x6))

matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row6'), listOf6Double, scope=matrixDouble6x6))

matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row3'), listOf6Double, scope=matrixDouble6x6))

matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row2'), listOf6Double, scope=matrixDouble6x6))

matrixDouble6x6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'row4'), listOf6Double, scope=matrixDouble6x6))
matrixDouble6x6._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row3')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row4')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row5')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(matrixDouble6x6._UseForTag(pyxb.namespace.ExpandedName(None, u'row6')), min_occurs=1, max_occurs=1)
    )
matrixDouble6x6._ContentModel = pyxb.binding.content.ParticleModel(matrixDouble6x6._GroupModel, min_occurs=1, max_occurs=1)



array2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PairedValues'), listOf2Double, scope=array2D))

array2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SizeOfArray'), pyxb.binding.datatypes.long, scope=array2D))
array2D._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(array2D._UseForTag(pyxb.namespace.ExpandedName(None, u'SizeOfArray')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(array2D._UseForTag(pyxb.namespace.ExpandedName(None, u'PairedValues')), min_occurs=1, max_occurs=None)
    )
array2D._ContentModel = pyxb.binding.content.ParticleModel(array2D._GroupModel, min_occurs=1, max_occurs=1)



array3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TripletValues'), listOf3Double, scope=array3D))

array3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SizeOfArray'), pyxb.binding.datatypes.long, scope=array3D))
array3D._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(array3D._UseForTag(pyxb.namespace.ExpandedName(None, u'SizeOfArray')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(array3D._UseForTag(pyxb.namespace.ExpandedName(None, u'TripletValues')), min_occurs=1, max_occurs=None)
    )
array3D._ContentModel = pyxb.binding.content.ParticleModel(array3D._GroupModel, min_occurs=1, max_occurs=1)



double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M21'), pyxb.binding.datatypes.double, scope=double9Type))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M12'), pyxb.binding.datatypes.double, scope=double9Type))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M11'), pyxb.binding.datatypes.double, scope=double9Type))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M13'), pyxb.binding.datatypes.double, scope=double9Type))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M33'), pyxb.binding.datatypes.double, scope=double9Type))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M23'), pyxb.binding.datatypes.double, scope=double9Type))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M22'), pyxb.binding.datatypes.double, scope=double9Type))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M31'), pyxb.binding.datatypes.double, scope=double9Type))

double9Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'M32'), pyxb.binding.datatypes.double, scope=double9Type))
double9Type._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M11')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M12')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M13')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M21')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M22')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M23')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M31')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M32')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(double9Type._UseForTag(pyxb.namespace.ExpandedName(None, u'M33')), min_occurs=1, max_occurs=1)
    )
double9Type._ContentModel = pyxb.binding.content.ParticleModel(double9Type._GroupModel, min_occurs=1, max_occurs=1)
