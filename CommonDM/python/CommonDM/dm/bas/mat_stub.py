# /home/nikoapos/ISDC/Projects/Alexandria/2.0/CommonDM/python/CommonDM/dm/bas/mat_stub.py
# PyXB bindings for NamespaceModule
# NSM:53a93ef17c0962f27bddfa3d42e62d3223c59234
# Generated 2014-06-12 14:36:51.814510 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:399d4060-f22e-11e3-acaf-c4d98710dc86')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import CommonDM.dm.bas.dtd_stub
import CommonDM.dm.bas.utd_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/mat', create_if_missing=True)
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


# Complex type xPolynome with content type ELEMENT_ONLY
class xPolynome (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'xPolynome')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}Coefficients uses Python identifier Coefficients
    __Coefficients = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), 'Coefficients', '__httpeuclid_esa_orgschemabasmat_xPolynome_httpeuclid_esa_orgschemabasmatCoefficients', True)

    
    Coefficients = property(__Coefficients.value, __Coefficients.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}Degree uses Python identifier Degree
    __Degree = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Degree'), 'Degree', '__httpeuclid_esa_orgschemabasmat_xPolynome_httpeuclid_esa_orgschemabasmatDegree', False)

    
    Degree = property(__Degree.value, __Degree.set, None, None)


    _ElementMap = {
        __Coefficients.name() : __Coefficients,
        __Degree.name() : __Degree
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'xPolynome', xPolynome)


# Complex type varXYpolynomialModel with content type ELEMENT_ONLY
class varXYpolynomialModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'varXYpolynomialModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}coefficients uses Python identifier coefficients
    __coefficients = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'coefficients'), 'coefficients', '__httpeuclid_esa_orgschemabasmat_varXYpolynomialModel_httpeuclid_esa_orgschemabasmatcoefficients', False)

    
    coefficients = property(__coefficients.value, __coefficients.set, None, u'First coefficient is constant coefficient')

    
    # Element {http://euclid.esa.org/schema/bas/mat}degree uses Python identifier degree
    __degree = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'degree'), 'degree', '__httpeuclid_esa_orgschemabasmat_varXYpolynomialModel_httpeuclid_esa_orgschemabasmatdegree', False)

    
    degree = property(__degree.value, __degree.set, None, None)


    _ElementMap = {
        __coefficients.name() : __coefficients,
        __degree.name() : __degree
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'varXYpolynomialModel', varXYpolynomialModel)


# Complex type xyPolynome with content type ELEMENT_ONLY
class xyPolynome (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'xyPolynome')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}Coefficients uses Python identifier Coefficients
    __Coefficients = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), 'Coefficients', '__httpeuclid_esa_orgschemabasmat_xyPolynome_httpeuclid_esa_orgschemabasmatCoefficients', True)

    
    Coefficients = property(__Coefficients.value, __Coefficients.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}Degree uses Python identifier Degree
    __Degree = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Degree'), 'Degree', '__httpeuclid_esa_orgschemabasmat_xyPolynome_httpeuclid_esa_orgschemabasmatDegree', False)

    
    Degree = property(__Degree.value, __Degree.set, None, None)


    _ElementMap = {
        __Coefficients.name() : __Coefficients,
        __Degree.name() : __Degree
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'xyPolynome', xyPolynome)


# Complex type analyticExpression with content type ELEMENT_ONLY
class analyticExpression (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'analyticExpression')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}Expression uses Python identifier Expression
    __Expression = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Expression'), 'Expression', '__httpeuclid_esa_orgschemabasmat_analyticExpression_httpeuclid_esa_orgschemabasmatExpression', False)

    
    Expression = property(__Expression.value, __Expression.set, None, u'This is the actual string containing the analytical function f(R, Theta), where R is the radial distance from pixel (X,Y)\n                        and Theta is the angle in degrees. The general methematical syntax is based on Python language. The variable\n                        arguments are passed labelled with a $ char as specified in PEP 292 (http://www.python.org/dev/peps/pep-0292/). Example:\n                        \n                    ')

    
    # Element {http://euclid.esa.org/schema/bas/mat}Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Parameter'), 'Parameter', '__httpeuclid_esa_orgschemabasmat_analyticExpression_httpeuclid_esa_orgschemabasmatParameter', False)

    
    Parameter = property(__Parameter.value, __Parameter.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasmat_analyticExpression_httpeuclid_esa_orgschemabasmatName', False)

    
    Name = property(__Name.value, __Name.set, None, u'This is an nick name of the analytic function, useful as reference for a customized numerical implementation of its algorithm.')

    
    # Element {http://euclid.esa.org/schema/bas/mat}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpeuclid_esa_orgschemabasmat_analyticExpression_httpeuclid_esa_orgschemabasmatVersion', False)

    
    Version = property(__Version.value, __Version.set, None, u'The analytical function version (referred to the Name)')


    _ElementMap = {
        __Expression.name() : __Expression,
        __Parameter.name() : __Parameter,
        __Name.name() : __Name,
        __Version.name() : __Version
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'analyticExpression', analyticExpression)


# Complex type doubleGaussian with content type ELEMENT_ONLY
class doubleGaussian (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'doubleGaussian')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}C uses Python identifier C
    __C = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'C'), 'C', '__httpeuclid_esa_orgschemabasmat_doubleGaussian_httpeuclid_esa_orgschemabasmatC', False)

    
    C = property(__C.value, __C.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}Sigma2 uses Python identifier Sigma2
    __Sigma2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sigma2'), 'Sigma2', '__httpeuclid_esa_orgschemabasmat_doubleGaussian_httpeuclid_esa_orgschemabasmatSigma2', False)

    
    Sigma2 = property(__Sigma2.value, __Sigma2.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}LambdaCoefs uses Python identifier LambdaCoefs
    __LambdaCoefs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LambdaCoefs'), 'LambdaCoefs', '__httpeuclid_esa_orgschemabasmat_doubleGaussian_httpeuclid_esa_orgschemabasmatLambdaCoefs', False)

    
    LambdaCoefs = property(__LambdaCoefs.value, __LambdaCoefs.set, None, u'Coefficients of the model describing the variations of the PSF as a function of wavelength.')

    
    # Element {http://euclid.esa.org/schema/bas/mat}Sigma1 uses Python identifier Sigma1
    __Sigma1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sigma1'), 'Sigma1', '__httpeuclid_esa_orgschemabasmat_doubleGaussian_httpeuclid_esa_orgschemabasmatSigma1', False)

    
    Sigma1 = property(__Sigma1.value, __Sigma1.set, None, None)


    _ElementMap = {
        __C.name() : __C,
        __Sigma2.name() : __Sigma2,
        __LambdaCoefs.name() : __LambdaCoefs,
        __Sigma1.name() : __Sigma1
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'doubleGaussian', doubleGaussian)


# Complex type coefficientX with content type ELEMENT_ONLY
class coefficientX (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coefficientX')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasmat_coefficientX_httpeuclid_esa_orgschemabasmatValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}X uses Python identifier X
    __X = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'X'), 'X', '__httpeuclid_esa_orgschemabasmat_coefficientX_httpeuclid_esa_orgschemabasmatX', False)

    
    X = property(__X.value, __X.set, None, None)


    _ElementMap = {
        __Value.name() : __Value,
        __X.name() : __X
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'coefficientX', coefficientX)


# Complex type extendedXPolynomialModel with content type ELEMENT_ONLY
class extendedXPolynomialModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'extendedXPolynomialModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}XPolynome uses Python identifier XPolynome
    __XPolynome = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XPolynome'), 'XPolynome', '__httpeuclid_esa_orgschemabasmat_extendedXPolynomialModel_httpeuclid_esa_orgschemabasmatXPolynome', True)

    
    XPolynome = property(__XPolynome.value, __XPolynome.set, None, None)


    _ElementMap = {
        __XPolynome.name() : __XPolynome
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'extendedXPolynomialModel', extendedXPolynomialModel)


# Complex type xyzPolynomialModelElement with content type ELEMENT_ONLY
class xyzPolynomialModelElement (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'xyzPolynomialModelElement')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}Coefficients uses Python identifier Coefficients
    __Coefficients = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), 'Coefficients', '__httpeuclid_esa_orgschemabasmat_xyzPolynomialModelElement_httpeuclid_esa_orgschemabasmatCoefficients', False)

    
    Coefficients = property(__Coefficients.value, __Coefficients.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}Degrees uses Python identifier Degrees
    __Degrees = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Degrees'), 'Degrees', '__httpeuclid_esa_orgschemabasmat_xyzPolynomialModelElement_httpeuclid_esa_orgschemabasmatDegrees', False)

    
    Degrees = property(__Degrees.value, __Degrees.set, None, None)


    _ElementMap = {
        __Coefficients.name() : __Coefficients,
        __Degrees.name() : __Degrees
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'xyzPolynomialModelElement', xyzPolynomialModelElement)


# Complex type varXpolynomialModel with content type ELEMENT_ONLY
class varXpolynomialModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'varXpolynomialModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}coefficients uses Python identifier coefficients
    __coefficients = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'coefficients'), 'coefficients', '__httpeuclid_esa_orgschemabasmat_varXpolynomialModel_httpeuclid_esa_orgschemabasmatcoefficients', False)

    
    coefficients = property(__coefficients.value, __coefficients.set, None, u'The length of the list must be degree+1, first is constant coefficient')

    
    # Element {http://euclid.esa.org/schema/bas/mat}degree uses Python identifier degree
    __degree = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'degree'), 'degree', '__httpeuclid_esa_orgschemabasmat_varXpolynomialModel_httpeuclid_esa_orgschemabasmatdegree', False)

    
    degree = property(__degree.value, __degree.set, None, None)


    _ElementMap = {
        __coefficients.name() : __coefficients,
        __degree.name() : __degree
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'varXpolynomialModel', varXpolynomialModel)


# Complex type varXpolynomialModelUnit with content type ELEMENT_ONLY
class varXpolynomialModelUnit (varXpolynomialModel):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'varXpolynomialModelUnit')
    # Base type is varXpolynomialModel
    
    # Element {http://euclid.esa.org/schema/bas/mat}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemabasmat_varXpolynomialModelUnit_httpeuclid_esa_orgschemabasmatUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element coefficients ({http://euclid.esa.org/schema/bas/mat}coefficients) inherited from {http://euclid.esa.org/schema/bas/mat}varXpolynomialModel
    
    # Element degree ({http://euclid.esa.org/schema/bas/mat}degree) inherited from {http://euclid.esa.org/schema/bas/mat}varXpolynomialModel

    _ElementMap = varXpolynomialModel._ElementMap.copy()
    _ElementMap.update({
        __Unit.name() : __Unit
    })
    _AttributeMap = varXpolynomialModel._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'varXpolynomialModelUnit', varXpolynomialModelUnit)


# Complex type varXYpolynomialModelUnit with content type ELEMENT_ONLY
class varXYpolynomialModelUnit (varXYpolynomialModel):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'varXYpolynomialModelUnit')
    # Base type is varXYpolynomialModel
    
    # Element {http://euclid.esa.org/schema/bas/mat}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Unit'), 'Unit', '__httpeuclid_esa_orgschemabasmat_varXYpolynomialModelUnit_httpeuclid_esa_orgschemabasmatUnit', False)

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element degree ({http://euclid.esa.org/schema/bas/mat}degree) inherited from {http://euclid.esa.org/schema/bas/mat}varXYpolynomialModel
    
    # Element coefficients ({http://euclid.esa.org/schema/bas/mat}coefficients) inherited from {http://euclid.esa.org/schema/bas/mat}varXYpolynomialModel

    _ElementMap = varXYpolynomialModel._ElementMap.copy()
    _ElementMap.update({
        __Unit.name() : __Unit
    })
    _AttributeMap = varXYpolynomialModel._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'varXYpolynomialModelUnit', varXYpolynomialModelUnit)


# Complex type coefficientXY with content type ELEMENT_ONLY
class coefficientXY (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coefficientXY')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasmat_coefficientXY_httpeuclid_esa_orgschemabasmatValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}X uses Python identifier X
    __X = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'X'), 'X', '__httpeuclid_esa_orgschemabasmat_coefficientXY_httpeuclid_esa_orgschemabasmatX', False)

    
    X = property(__X.value, __X.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}Y uses Python identifier Y
    __Y = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Y'), 'Y', '__httpeuclid_esa_orgschemabasmat_coefficientXY_httpeuclid_esa_orgschemabasmatY', False)

    
    Y = property(__Y.value, __Y.set, None, None)


    _ElementMap = {
        __Value.name() : __Value,
        __X.name() : __X,
        __Y.name() : __Y
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'coefficientXY', coefficientXY)


# Complex type extendedXYPolynomialModel with content type ELEMENT_ONLY
class extendedXYPolynomialModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'extendedXYPolynomialModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}XYPolynome uses Python identifier XYPolynome
    __XYPolynome = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'XYPolynome'), 'XYPolynome', '__httpeuclid_esa_orgschemabasmat_extendedXYPolynomialModel_httpeuclid_esa_orgschemabasmatXYPolynome', True)

    
    XYPolynome = property(__XYPolynome.value, __XYPolynome.set, None, None)


    _ElementMap = {
        __XYPolynome.name() : __XYPolynome
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'extendedXYPolynomialModel', extendedXYPolynomialModel)


# Complex type degreesXYZ with content type ELEMENT_ONLY
class degreesXYZ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'degreesXYZ')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}Z uses Python identifier Z
    __Z = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Z'), 'Z', '__httpeuclid_esa_orgschemabasmat_degreesXYZ_httpeuclid_esa_orgschemabasmatZ', False)

    
    Z = property(__Z.value, __Z.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}X uses Python identifier X
    __X = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'X'), 'X', '__httpeuclid_esa_orgschemabasmat_degreesXYZ_httpeuclid_esa_orgschemabasmatX', False)

    
    X = property(__X.value, __X.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}Y uses Python identifier Y
    __Y = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Y'), 'Y', '__httpeuclid_esa_orgschemabasmat_degreesXYZ_httpeuclid_esa_orgschemabasmatY', False)

    
    Y = property(__Y.value, __Y.set, None, None)


    _ElementMap = {
        __Z.name() : __Z,
        __X.name() : __X,
        __Y.name() : __Y
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'degreesXYZ', degreesXYZ)


# Complex type xyzPolynomialModel with content type ELEMENT_ONLY
class xyzPolynomialModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'xyzPolynomialModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}ModelElement uses Python identifier ModelElement
    __ModelElement = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ModelElement'), 'ModelElement', '__httpeuclid_esa_orgschemabasmat_xyzPolynomialModel_httpeuclid_esa_orgschemabasmatModelElement', True)

    
    ModelElement = property(__ModelElement.value, __ModelElement.set, None, None)


    _ElementMap = {
        __ModelElement.name() : __ModelElement
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'xyzPolynomialModel', xyzPolynomialModel)


# Complex type coefficientXYZ with content type ELEMENT_ONLY
class coefficientXYZ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coefficientXYZ')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/mat}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasmat_coefficientXYZ_httpeuclid_esa_orgschemabasmatValue', False)

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}X uses Python identifier X
    __X = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'X'), 'X', '__httpeuclid_esa_orgschemabasmat_coefficientXYZ_httpeuclid_esa_orgschemabasmatX', False)

    
    X = property(__X.value, __X.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}Z uses Python identifier Z
    __Z = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Z'), 'Z', '__httpeuclid_esa_orgschemabasmat_coefficientXYZ_httpeuclid_esa_orgschemabasmatZ', False)

    
    Z = property(__Z.value, __Z.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/mat}Y uses Python identifier Y
    __Y = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Y'), 'Y', '__httpeuclid_esa_orgschemabasmat_coefficientXYZ_httpeuclid_esa_orgschemabasmatY', False)

    
    Y = property(__Y.value, __Y.set, None, None)


    _ElementMap = {
        __Value.name() : __Value,
        __X.name() : __X,
        __Z.name() : __Z,
        __Y.name() : __Y
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'coefficientXYZ', coefficientXYZ)




xPolynome._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), coefficientX, scope=xPolynome))

xPolynome._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Degree'), pyxb.binding.datatypes.nonNegativeInteger, scope=xPolynome))
xPolynome._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(xPolynome._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Degree')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(xPolynome._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coefficients')), min_occurs=1, max_occurs=None)
    )
xPolynome._ContentModel = pyxb.binding.content.ParticleModel(xPolynome._GroupModel, min_occurs=1, max_occurs=1)



varXYpolynomialModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'coefficients'), CommonDM.dm.bas.dtd_stub.listOfDouble, scope=varXYpolynomialModel, documentation=u'First coefficient is constant coefficient'))

varXYpolynomialModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'degree'), pyxb.binding.datatypes.nonNegativeInteger, scope=varXYpolynomialModel))
varXYpolynomialModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(varXYpolynomialModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'degree')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(varXYpolynomialModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'coefficients')), min_occurs=1, max_occurs=1)
    )
varXYpolynomialModel._ContentModel = pyxb.binding.content.ParticleModel(varXYpolynomialModel._GroupModel, min_occurs=1, max_occurs=1)



xyPolynome._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), coefficientXY, scope=xyPolynome))

xyPolynome._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Degree'), pyxb.binding.datatypes.nonNegativeInteger, scope=xyPolynome))
xyPolynome._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(xyPolynome._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Degree')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(xyPolynome._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coefficients')), min_occurs=1, max_occurs=None)
    )
xyPolynome._ContentModel = pyxb.binding.content.ParticleModel(xyPolynome._GroupModel, min_occurs=1, max_occurs=1)



analyticExpression._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Expression'), pyxb.binding.datatypes.string, scope=analyticExpression, documentation=u'This is the actual string containing the analytical function f(R, Theta), where R is the radial distance from pixel (X,Y)\n                        and Theta is the angle in degrees. The general methematical syntax is based on Python language. The variable\n                        arguments are passed labelled with a $ char as specified in PEP 292 (http://www.python.org/dev/peps/pep-0292/). Example:\n                        \n                    '))

analyticExpression._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Parameter'), xyzPolynomialModel, scope=analyticExpression))

analyticExpression._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=analyticExpression, documentation=u'This is an nick name of the analytic function, useful as reference for a customized numerical implementation of its algorithm.'))

analyticExpression._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), pyxb.binding.datatypes.string, scope=analyticExpression, documentation=u'The analytical function version (referred to the Name)'))
analyticExpression._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(analyticExpression._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(analyticExpression._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(analyticExpression._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Expression')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(analyticExpression._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Parameter')), min_occurs=1, max_occurs=1)
    )
analyticExpression._ContentModel = pyxb.binding.content.ParticleModel(analyticExpression._GroupModel, min_occurs=1, max_occurs=1)



doubleGaussian._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'C'), varXYpolynomialModel, scope=doubleGaussian))

doubleGaussian._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sigma2'), varXYpolynomialModelUnit, scope=doubleGaussian))

doubleGaussian._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LambdaCoefs'), varXpolynomialModelUnit, scope=doubleGaussian, documentation=u'Coefficients of the model describing the variations of the PSF as a function of wavelength.'))

doubleGaussian._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sigma1'), varXYpolynomialModelUnit, scope=doubleGaussian))
doubleGaussian._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(doubleGaussian._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LambdaCoefs')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(doubleGaussian._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sigma1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(doubleGaussian._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sigma2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(doubleGaussian._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'C')), min_occurs=1, max_occurs=1)
    )
doubleGaussian._ContentModel = pyxb.binding.content.ParticleModel(doubleGaussian._GroupModel, min_occurs=1, max_occurs=1)



coefficientX._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.double, scope=coefficientX))

coefficientX._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'X'), pyxb.binding.datatypes.nonNegativeInteger, scope=coefficientX))
coefficientX._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coefficientX._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'X')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coefficientX._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1)
    )
coefficientX._ContentModel = pyxb.binding.content.ParticleModel(coefficientX._GroupModel, min_occurs=1, max_occurs=1)



extendedXPolynomialModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XPolynome'), xPolynome, scope=extendedXPolynomialModel))
extendedXPolynomialModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(extendedXPolynomialModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XPolynome')), min_occurs=1, max_occurs=None)
    )
extendedXPolynomialModel._ContentModel = pyxb.binding.content.ParticleModel(extendedXPolynomialModel._GroupModel, min_occurs=1, max_occurs=1)



xyzPolynomialModelElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Coefficients'), coefficientXYZ, scope=xyzPolynomialModelElement))

xyzPolynomialModelElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Degrees'), degreesXYZ, scope=xyzPolynomialModelElement))
xyzPolynomialModelElement._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(xyzPolynomialModelElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Degrees')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(xyzPolynomialModelElement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coefficients')), min_occurs=1, max_occurs=1)
    )
xyzPolynomialModelElement._ContentModel = pyxb.binding.content.ParticleModel(xyzPolynomialModelElement._GroupModel, min_occurs=1, max_occurs=1)



varXpolynomialModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'coefficients'), CommonDM.dm.bas.dtd_stub.listOfDouble, scope=varXpolynomialModel, documentation=u'The length of the list must be degree+1, first is constant coefficient'))

varXpolynomialModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'degree'), pyxb.binding.datatypes.nonNegativeInteger, scope=varXpolynomialModel))
varXpolynomialModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(varXpolynomialModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'degree')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(varXpolynomialModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'coefficients')), min_occurs=1, max_occurs=1)
    )
varXpolynomialModel._ContentModel = pyxb.binding.content.ParticleModel(varXpolynomialModel._GroupModel, min_occurs=1, max_occurs=1)



varXpolynomialModelUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=varXpolynomialModelUnit))
varXpolynomialModelUnit._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(varXpolynomialModelUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'degree')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(varXpolynomialModelUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'coefficients')), min_occurs=1, max_occurs=1)
    )
varXpolynomialModelUnit._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(varXpolynomialModelUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
varXpolynomialModelUnit._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(varXpolynomialModelUnit._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(varXpolynomialModelUnit._GroupModel_2, min_occurs=1, max_occurs=1)
    )
varXpolynomialModelUnit._ContentModel = pyxb.binding.content.ParticleModel(varXpolynomialModelUnit._GroupModel, min_occurs=1, max_occurs=1)



varXYpolynomialModelUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Unit'), CommonDM.dm.bas.utd_stub.unit, scope=varXYpolynomialModelUnit))
varXYpolynomialModelUnit._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(varXYpolynomialModelUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'degree')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(varXYpolynomialModelUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'coefficients')), min_occurs=1, max_occurs=1)
    )
varXYpolynomialModelUnit._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(varXYpolynomialModelUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Unit')), min_occurs=1, max_occurs=1)
    )
varXYpolynomialModelUnit._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(varXYpolynomialModelUnit._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(varXYpolynomialModelUnit._GroupModel_2, min_occurs=1, max_occurs=1)
    )
varXYpolynomialModelUnit._ContentModel = pyxb.binding.content.ParticleModel(varXYpolynomialModelUnit._GroupModel, min_occurs=1, max_occurs=1)



coefficientXY._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.double, scope=coefficientXY))

coefficientXY._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'X'), pyxb.binding.datatypes.nonNegativeInteger, scope=coefficientXY))

coefficientXY._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Y'), pyxb.binding.datatypes.nonNegativeInteger, scope=coefficientXY))
coefficientXY._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coefficientXY._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'X')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coefficientXY._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Y')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coefficientXY._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1)
    )
coefficientXY._ContentModel = pyxb.binding.content.ParticleModel(coefficientXY._GroupModel, min_occurs=1, max_occurs=1)



extendedXYPolynomialModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XYPolynome'), xyPolynome, scope=extendedXYPolynomialModel))
extendedXYPolynomialModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(extendedXYPolynomialModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XYPolynome')), min_occurs=1, max_occurs=None)
    )
extendedXYPolynomialModel._ContentModel = pyxb.binding.content.ParticleModel(extendedXYPolynomialModel._GroupModel, min_occurs=1, max_occurs=1)



degreesXYZ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Z'), pyxb.binding.datatypes.unsignedByte, scope=degreesXYZ))

degreesXYZ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'X'), pyxb.binding.datatypes.unsignedByte, scope=degreesXYZ))

degreesXYZ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Y'), pyxb.binding.datatypes.unsignedByte, scope=degreesXYZ))
degreesXYZ._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(degreesXYZ._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'X')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(degreesXYZ._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Y')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(degreesXYZ._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Z')), min_occurs=1, max_occurs=1)
    )
degreesXYZ._ContentModel = pyxb.binding.content.ParticleModel(degreesXYZ._GroupModel, min_occurs=1, max_occurs=1)



xyzPolynomialModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModelElement'), xyzPolynomialModelElement, scope=xyzPolynomialModel))
xyzPolynomialModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(xyzPolynomialModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ModelElement')), min_occurs=1, max_occurs=None)
    )
xyzPolynomialModel._ContentModel = pyxb.binding.content.ParticleModel(xyzPolynomialModel._GroupModel, min_occurs=1, max_occurs=1)



coefficientXYZ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.double, scope=coefficientXYZ))

coefficientXYZ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'X'), pyxb.binding.datatypes.negativeInteger, scope=coefficientXYZ))

coefficientXYZ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Z'), pyxb.binding.datatypes.negativeInteger, scope=coefficientXYZ))

coefficientXYZ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Y'), pyxb.binding.datatypes.negativeInteger, scope=coefficientXYZ))
coefficientXYZ._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coefficientXYZ._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'X')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coefficientXYZ._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Y')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coefficientXYZ._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Z')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(coefficientXYZ._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), min_occurs=1, max_occurs=1)
    )
coefficientXYZ._ContentModel = pyxb.binding.content.ParticleModel(coefficientXYZ._GroupModel, min_occurs=1, max_occurs=1)
