# /home/nikoapos/ISDC/Projects/Alexandria/2.0/CommonDM/python/CommonDM/dm/pro/le1_stub.py
# PyXB bindings for NamespaceModule
# NSM:23b1c64dcf05022ed49ac75f3cb8280755f2bfaf
# Generated 2014-06-12 14:36:51.820039 by PyXB version 1.1.2
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
import CommonDM.dm.ins.nis_stub
import CommonDM.dm.bas.dtd_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/pro/le1', create_if_missing=True)
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
class productType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Data product type: sky, bias, object, std, dark, flat, wave-lamp"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'productType')
    _Documentation = u'Data product type: sky, bias, object, std, dark, flat, wave-lamp'
productType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=productType, enum_prefix=None)
productType.Bias = productType._CF_enumeration.addEnumeration(unicode_value=u'Bias')
productType.Object = productType._CF_enumeration.addEnumeration(unicode_value=u'Object')
productType.Std = productType._CF_enumeration.addEnumeration(unicode_value=u'Std')
productType.Dark = productType._CF_enumeration.addEnumeration(unicode_value=u'Dark')
productType.Flat = productType._CF_enumeration.addEnumeration(unicode_value=u'Flat')
productType.WaveLamp = productType._CF_enumeration.addEnumeration(unicode_value=u'WaveLamp')
productType._InitializeFacetMap(productType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'productType', productType)

# Atomic SimpleTypeDefinition
class productCategory (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Data product category: science frame or calibration frame"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'productCategory')
    _Documentation = u'Data product category: science frame or calibration frame'
productCategory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=productCategory, enum_prefix=None)
productCategory.Science = productCategory._CF_enumeration.addEnumeration(unicode_value=u'Science')
productCategory.Calib = productCategory._CF_enumeration.addEnumeration(unicode_value=u'Calib')
productCategory._InitializeFacetMap(productCategory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'productCategory', productCategory)

# Atomic SimpleTypeDefinition
class readoutModeMethod (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """NISP readout modes available"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'readoutModeMethod')
    _Documentation = u'NISP readout modes available'
readoutModeMethod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=readoutModeMethod, enum_prefix=None)
readoutModeMethod.MULTIACCUM = readoutModeMethod._CF_enumeration.addEnumeration(unicode_value=u'MULTIACCUM')
readoutModeMethod.UP_THE_RAMP = readoutModeMethod._CF_enumeration.addEnumeration(unicode_value=u'UP_THE_RAMP')
readoutModeMethod.FOWLER_SAMPLES = readoutModeMethod._CF_enumeration.addEnumeration(unicode_value=u'FOWLER_SAMPLES')
readoutModeMethod._InitializeFacetMap(readoutModeMethod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'readoutModeMethod', readoutModeMethod)

# Atomic SimpleTypeDefinition
class instrumentMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """NISP instrument modes"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'instrumentMode')
    _Documentation = u'NISP instrument modes'
instrumentMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=instrumentMode, enum_prefix=None)
instrumentMode.Idle = instrumentMode._CF_enumeration.addEnumeration(unicode_value=u'Idle')
instrumentMode.NormalScience = instrumentMode._CF_enumeration.addEnumeration(unicode_value=u'NormalScience')
instrumentMode.Calibration = instrumentMode._CF_enumeration.addEnumeration(unicode_value=u'Calibration')
instrumentMode.ExtendedScience = instrumentMode._CF_enumeration.addEnumeration(unicode_value=u'ExtendedScience')
instrumentMode.Engineering = instrumentMode._CF_enumeration.addEnumeration(unicode_value=u'Engineering')
instrumentMode.Degraded = instrumentMode._CF_enumeration.addEnumeration(unicode_value=u'Degraded')
instrumentMode._InitializeFacetMap(instrumentMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'instrumentMode', instrumentMode)

# Atomic SimpleTypeDefinition
class observationMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Euclid (NISP) observation modes"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'observationMode')
    _Documentation = u'Euclid (NISP) observation modes'
observationMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=observationMode, enum_prefix=None)
observationMode.WideSurvey = observationMode._CF_enumeration.addEnumeration(unicode_value=u'WideSurvey')
observationMode.DeepSurvey = observationMode._CF_enumeration.addEnumeration(unicode_value=u'DeepSurvey')
observationMode.None_ = observationMode._CF_enumeration.addEnumeration(unicode_value=u'None')
observationMode._InitializeFacetMap(observationMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'observationMode', observationMode)

# Atomic SimpleTypeDefinition
class fpaPointingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Determines the point of the FPA for which the RA, DEC are given. It can be either "Center" or "BottomLeft"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fpaPointingType')
    _Documentation = u'Determines the point of the FPA for which the RA, DEC are given. It can be either "Center" or "BottomLeft".'
fpaPointingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fpaPointingType, enum_prefix=None)
fpaPointingType.Center = fpaPointingType._CF_enumeration.addEnumeration(unicode_value=u'Center')
fpaPointingType.BottomLeft = fpaPointingType._CF_enumeration.addEnumeration(unicode_value=u'BottomLeft')
fpaPointingType._InitializeFacetMap(fpaPointingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'fpaPointingType', fpaPointingType)

# Atomic SimpleTypeDefinition
class productTech (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Data product technique: image or spectrum"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'productTech')
    _Documentation = u'Data product technique: image or spectrum'
productTech._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=productTech, enum_prefix=None)
productTech.Image = productTech._CF_enumeration.addEnumeration(unicode_value=u'Image')
productTech.Spectrum = productTech._CF_enumeration.addEnumeration(unicode_value=u'Spectrum')
productTech._InitializeFacetMap(productTech._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'productTech', productTech)

# Atomic SimpleTypeDefinition
class filterWheelPosition (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """NISP Filter Wheel positions"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'filterWheelPosition')
    _Documentation = u'NISP Filter Wheel positions'
filterWheelPosition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=filterWheelPosition, enum_prefix=None)
filterWheelPosition.Y = filterWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'Y')
filterWheelPosition.J = filterWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'J')
filterWheelPosition.H = filterWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'H')
filterWheelPosition.OPEN = filterWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'OPEN')
filterWheelPosition.CLOSE = filterWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'CLOSE')
filterWheelPosition._InitializeFacetMap(filterWheelPosition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'filterWheelPosition', filterWheelPosition)

# Atomic SimpleTypeDefinition
class grismWheelPosition (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """NISP Grism Wheel positions"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'grismWheelPosition')
    _Documentation = u'NISP Grism Wheel positions'
grismWheelPosition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=grismWheelPosition, enum_prefix=None)
grismWheelPosition.RH = grismWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'RH')
grismWheelPosition.RV = grismWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'RV')
grismWheelPosition.BH = grismWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'BH')
grismWheelPosition.BV = grismWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'BV')
grismWheelPosition.OPEN = grismWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'OPEN')
grismWheelPosition.CLOSE = grismWheelPosition._CF_enumeration.addEnumeration(unicode_value=u'CLOSE')
grismWheelPosition._InitializeFacetMap(grismWheelPosition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'grismWheelPosition', grismWheelPosition)

# Complex type readoutMode with content type ELEMENT_ONLY
class readoutMode (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'readoutMode')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}ExpSampleTime uses Python identifier ExpSampleTime
    __ExpSampleTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpSampleTime'), 'ExpSampleTime', '__httpeuclid_esa_orgschemaprole1_readoutMode_httpeuclid_esa_orgschemaprole1ExpSampleTime', False)

    
    ExpSampleTime = property(__ExpSampleTime.value, __ExpSampleTime.set, None, u'NISP exposure time in seconds for single samples of the readout')

    
    # Element {http://euclid.esa.org/schema/pro/le1}NumSamples uses Python identifier NumSamples
    __NumSamples = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumSamples'), 'NumSamples', '__httpeuclid_esa_orgschemaprole1_readoutMode_httpeuclid_esa_orgschemaprole1NumSamples', False)

    
    NumSamples = property(__NumSamples.value, __NumSamples.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/le1}ReadoutMode uses Python identifier ReadoutMode
    __ReadoutMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode'), 'ReadoutMode', '__httpeuclid_esa_orgschemaprole1_readoutMode_httpeuclid_esa_orgschemaprole1ReadoutMode', False)

    
    ReadoutMode = property(__ReadoutMode.value, __ReadoutMode.set, None, None)


    _ElementMap = {
        __ExpSampleTime.name() : __ExpSampleTime,
        __NumSamples.name() : __NumSamples,
        __ReadoutMode.name() : __ReadoutMode
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'readoutMode', readoutMode)


# Complex type nispRawFrame with content type ELEMENT_ONLY
class nispRawFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nispRawFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}ReadoutMode uses Python identifier ReadoutMode
    __ReadoutMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode'), 'ReadoutMode', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ReadoutMode', False)

    
    ReadoutMode = property(__ReadoutMode.value, __ReadoutMode.set, None, u'Readout mode used in this exposure')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ExposureTime uses Python identifier ExposureTime
    __ExposureTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime'), 'ExposureTime', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ExposureTime', False)

    
    ExposureTime = property(__ExposureTime.value, __ExposureTime.set, None, u'Exposure of the CCD in seconds')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ObservationMode uses Python identifier ObservationMode
    __ObservationMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode'), 'ObservationMode', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ObservationMode', False)

    
    ObservationMode = property(__ObservationMode.value, __ObservationMode.set, None, u'Observation mode: Wide Survey or Deep Survey')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ObservationSequence uses Python identifier ObservationSequence
    __ObservationSequence = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObservationSequence'), 'ObservationSequence', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ObservationSequence', False)

    
    ObservationSequence = property(__ObservationSequence.value, __ObservationSequence.set, None, u'Information on the observation sequence in which the exposure is acquired')

    
    # Element {http://euclid.esa.org/schema/pro/le1}DataProduct uses Python identifier DataProduct
    __DataProduct = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataProduct'), 'DataProduct', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1DataProduct', False)

    
    DataProduct = property(__DataProduct.value, __DataProduct.set, None, u'Data product type and category (e.g. Image or Spectrum, Science or Calibration, Dark or Flat, etc.)')

    
    # Element {http://euclid.esa.org/schema/pro/le1}CommandedFPAPointing uses Python identifier CommandedFPAPointing
    __CommandedFPAPointing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CommandedFPAPointing'), 'CommandedFPAPointing', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1CommandedFPAPointing', False)

    
    CommandedFPAPointing = property(__CommandedFPAPointing.value, __CommandedFPAPointing.set, None, u'Commanded FPA pointing (RA, DEC, Pointing Angle)')

    
    # Element {http://euclid.esa.org/schema/pro/le1}InstrumentMode uses Python identifier InstrumentMode
    __InstrumentMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InstrumentMode'), 'InstrumentMode', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1InstrumentMode', False)

    
    InstrumentMode = property(__InstrumentMode.value, __InstrumentMode.set, None, u'Instrument mode during the exposure acquisition')

    
    # Element {http://euclid.esa.org/schema/pro/le1}GrismWheelPos uses Python identifier GrismWheelPos
    __GrismWheelPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GrismWheelPos'), 'GrismWheelPos', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1GrismWheelPos', False)

    
    GrismWheelPos = property(__GrismWheelPos.value, __GrismWheelPos.set, None, u'Grism wheel position')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ObservationDate uses Python identifier ObservationDate
    __ObservationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate'), 'ObservationDate', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ObservationDate', False)

    
    ObservationDate = property(__ObservationDate.value, __ObservationDate.set, None, u'Observation date of the exposure')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ReconsFPAPointing uses Python identifier ReconsFPAPointing
    __ReconsFPAPointing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReconsFPAPointing'), 'ReconsFPAPointing', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ReconsFPAPointing', False)

    
    ReconsFPAPointing = property(__ReconsFPAPointing.value, __ReconsFPAPointing.set, None, u'Reconstructed FPA pointing (RA, DEC, Pointing Angle)')

    
    # Element {http://euclid.esa.org/schema/pro/le1}FilterWheelPos uses Python identifier FilterWheelPos
    __FilterWheelPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FilterWheelPos'), 'FilterWheelPos', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1FilterWheelPos', False)

    
    FilterWheelPos = property(__FilterWheelPos.value, __FilterWheelPos.set, None, u'Filter wheel position')


    _ElementMap = {
        __ReadoutMode.name() : __ReadoutMode,
        __ExposureTime.name() : __ExposureTime,
        __ObservationMode.name() : __ObservationMode,
        __ObservationSequence.name() : __ObservationSequence,
        __DataProduct.name() : __DataProduct,
        __CommandedFPAPointing.name() : __CommandedFPAPointing,
        __InstrumentMode.name() : __InstrumentMode,
        __GrismWheelPos.name() : __GrismWheelPos,
        __ObservationDate.name() : __ObservationDate,
        __ReconsFPAPointing.name() : __ReconsFPAPointing,
        __FilterWheelPos.name() : __FilterWheelPos
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nispRawFrame', nispRawFrame)


# Complex type dataProduct with content type ELEMENT_ONLY
class dataProduct (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataProduct')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}Tech uses Python identifier Tech
    __Tech = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Tech'), 'Tech', '__httpeuclid_esa_orgschemaprole1_dataProduct_httpeuclid_esa_orgschemaprole1Tech', False)

    
    Tech = property(__Tech.value, __Tech.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/le1}Category uses Python identifier Category
    __Category = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Category'), 'Category', '__httpeuclid_esa_orgschemaprole1_dataProduct_httpeuclid_esa_orgschemaprole1Category', False)

    
    Category = property(__Category.value, __Category.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/le1}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Type'), 'Type', '__httpeuclid_esa_orgschemaprole1_dataProduct_httpeuclid_esa_orgschemaprole1Type', False)

    
    Type = property(__Type.value, __Type.set, None, None)


    _ElementMap = {
        __Tech.name() : __Tech,
        __Category.name() : __Category,
        __Type.name() : __Type
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'dataProduct', dataProduct)


# Complex type fpaPointing with content type ELEMENT_ONLY
class fpaPointing (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fpaPointing')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}Orientation uses Python identifier Orientation
    __Orientation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Orientation'), 'Orientation', '__httpeuclid_esa_orgschemaprole1_fpaPointing_httpeuclid_esa_orgschemaprole1Orientation', False)

    
    Orientation = property(__Orientation.value, __Orientation.set, None, u'Counterclockwise angle from the positive RA axis, in degrees.')

    
    # Element {http://euclid.esa.org/schema/pro/le1}Dec uses Python identifier Dec
    __Dec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Dec'), 'Dec', '__httpeuclid_esa_orgschemaprole1_fpaPointing_httpeuclid_esa_orgschemaprole1Dec', False)

    
    Dec = property(__Dec.value, __Dec.set, None, u'Declination of the FPA, in degrees.')

    
    # Element {http://euclid.esa.org/schema/pro/le1}RA uses Python identifier RA
    __RA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RA'), 'RA', '__httpeuclid_esa_orgschemaprole1_fpaPointing_httpeuclid_esa_orgschemaprole1RA', False)

    
    RA = property(__RA.value, __RA.set, None, u'Right ascension of the FPA, in degrees.')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpeuclid_esa_orgschemaprole1_fpaPointing_type', fpaPointingType, required=True)
    
    type = property(__type.value, __type.set, None, u'Specifies the point of the FPA for which the RA, DEC are given for.')


    _ElementMap = {
        __Orientation.name() : __Orientation,
        __Dec.name() : __Dec,
        __RA.name() : __RA
    }
    _AttributeMap = {
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'fpaPointing', fpaPointing)


# Complex type observationSequence with content type ELEMENT_ONLY
class observationSequence (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'observationSequence')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}TotSequence uses Python identifier TotSequence
    __TotSequence = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TotSequence'), 'TotSequence', '__httpeuclid_esa_orgschemaprole1_observationSequence_httpeuclid_esa_orgschemaprole1TotSequence', False)

    
    TotSequence = property(__TotSequence.value, __TotSequence.set, None, u'Total number of frames in the observation sequence')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ObjectName uses Python identifier ObjectName
    __ObjectName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObjectName'), 'ObjectName', '__httpeuclid_esa_orgschemaprole1_observationSequence_httpeuclid_esa_orgschemaprole1ObjectName', False)

    
    ObjectName = property(__ObjectName.value, __ObjectName.set, None, u'Name of the target')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ObjectId uses Python identifier ObjectId
    __ObjectId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObjectId'), 'ObjectId', '__httpeuclid_esa_orgschemaprole1_observationSequence_httpeuclid_esa_orgschemaprole1ObjectId', False)

    
    ObjectId = property(__ObjectId.value, __ObjectId.set, None, u'Unique object identifier (standard source)')

    
    # Element {http://euclid.esa.org/schema/pro/le1}DitherId uses Python identifier DitherId
    __DitherId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DitherId'), 'DitherId', '__httpeuclid_esa_orgschemaprole1_observationSequence_httpeuclid_esa_orgschemaprole1DitherId', False)

    
    DitherId = property(__DitherId.value, __DitherId.set, None, u'Unique ID identifying the dither performed')

    
    # Element {http://euclid.esa.org/schema/pro/le1}SequenceNum uses Python identifier SequenceNum
    __SequenceNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SequenceNum'), 'SequenceNum', '__httpeuclid_esa_orgschemaprole1_observationSequence_httpeuclid_esa_orgschemaprole1SequenceNum', False)

    
    SequenceNum = property(__SequenceNum.value, __SequenceNum.set, None, u'Frame number in the observation sequence')

    
    # Element {http://euclid.esa.org/schema/pro/le1}FieldId uses Python identifier FieldId
    __FieldId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FieldId'), 'FieldId', '__httpeuclid_esa_orgschemaprole1_observationSequence_httpeuclid_esa_orgschemaprole1FieldId', False)

    
    FieldId = property(__FieldId.value, __FieldId.set, None, u'Unique ID identifying the Field observed')


    _ElementMap = {
        __TotSequence.name() : __TotSequence,
        __ObjectName.name() : __ObjectName,
        __ObjectId.name() : __ObjectId,
        __DitherId.name() : __DitherId,
        __SequenceNum.name() : __SequenceNum,
        __FieldId.name() : __FieldId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'observationSequence', observationSequence)




readoutMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpSampleTime'), CommonDM.dm.ins.nis_stub.exposureTime, scope=readoutMode, documentation=u'NISP exposure time in seconds for single samples of the readout'))

readoutMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumSamples'), pyxb.binding.datatypes.int, scope=readoutMode))

readoutMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode'), readoutModeMethod, scope=readoutMode))
readoutMode._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(readoutMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readoutMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumSamples')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readoutMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpSampleTime')), min_occurs=1, max_occurs=1)
    )
readoutMode._ContentModel = pyxb.binding.content.ParticleModel(readoutMode._GroupModel, min_occurs=1, max_occurs=1)



nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode'), readoutMode, scope=nispRawFrame, documentation=u'Readout mode used in this exposure'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime'), CommonDM.dm.ins.nis_stub.exposureTime, scope=nispRawFrame, documentation=u'Exposure of the CCD in seconds'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode'), observationMode, scope=nispRawFrame, documentation=u'Observation mode: Wide Survey or Deep Survey'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservationSequence'), observationSequence, scope=nispRawFrame, documentation=u'Information on the observation sequence in which the exposure is acquired'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataProduct'), dataProduct, scope=nispRawFrame, documentation=u'Data product type and category (e.g. Image or Spectrum, Science or Calibration, Dark or Flat, etc.)'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CommandedFPAPointing'), fpaPointing, scope=nispRawFrame, documentation=u'Commanded FPA pointing (RA, DEC, Pointing Angle)'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InstrumentMode'), instrumentMode, scope=nispRawFrame, documentation=u'Instrument mode during the exposure acquisition'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GrismWheelPos'), grismWheelPosition, scope=nispRawFrame, documentation=u'Grism wheel position'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate'), pyxb.binding.datatypes.dateTime, scope=nispRawFrame, documentation=u'Observation date of the exposure'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReconsFPAPointing'), fpaPointing, scope=nispRawFrame, documentation=u'Reconstructed FPA pointing (RA, DEC, Pointing Angle)'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FilterWheelPos'), filterWheelPosition, scope=nispRawFrame, documentation=u'Filter wheel position'))
nispRawFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationSequence')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InstrumentMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataProduct')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CommandedFPAPointing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReconsFPAPointing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GrismWheelPos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FilterWheelPos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode')), min_occurs=1, max_occurs=1)
    )
nispRawFrame._ContentModel = pyxb.binding.content.ParticleModel(nispRawFrame._GroupModel, min_occurs=1, max_occurs=1)



dataProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Tech'), productTech, scope=dataProduct))

dataProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Category'), productCategory, scope=dataProduct))

dataProduct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Type'), productType, scope=dataProduct))
dataProduct._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(dataProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Category')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Type')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(dataProduct._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Tech')), min_occurs=1, max_occurs=1)
    )
dataProduct._ContentModel = pyxb.binding.content.ParticleModel(dataProduct._GroupModel, min_occurs=1, max_occurs=1)



fpaPointing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Orientation'), CommonDM.dm.bas.dtd_stub.degAngle, scope=fpaPointing, documentation=u'Counterclockwise angle from the positive RA axis, in degrees.'))

fpaPointing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Dec'), CommonDM.dm.bas.dtd_stub.degAngle, scope=fpaPointing, documentation=u'Declination of the FPA, in degrees.'))

fpaPointing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RA'), CommonDM.dm.bas.dtd_stub.degAngle, scope=fpaPointing, documentation=u'Right ascension of the FPA, in degrees.'))
fpaPointing._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fpaPointing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fpaPointing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dec')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fpaPointing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Orientation')), min_occurs=1, max_occurs=1)
    )
fpaPointing._ContentModel = pyxb.binding.content.ParticleModel(fpaPointing._GroupModel, min_occurs=1, max_occurs=1)



observationSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TotSequence'), pyxb.binding.datatypes.short, scope=observationSequence, documentation=u'Total number of frames in the observation sequence'))

observationSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObjectName'), pyxb.binding.datatypes.string, scope=observationSequence, documentation=u'Name of the target'))

observationSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObjectId'), pyxb.binding.datatypes.string, scope=observationSequence, documentation=u'Unique object identifier (standard source)'))

observationSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DitherId'), pyxb.binding.datatypes.string, scope=observationSequence, documentation=u'Unique ID identifying the dither performed'))

observationSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SequenceNum'), pyxb.binding.datatypes.short, scope=observationSequence, documentation=u'Frame number in the observation sequence'))

observationSequence._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FieldId'), pyxb.binding.datatypes.string, scope=observationSequence, documentation=u'Unique ID identifying the Field observed'))
observationSequence._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(observationSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FieldId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(observationSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DitherId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(observationSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObjectId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(observationSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObjectName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(observationSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SequenceNum')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(observationSequence._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TotSequence')), min_occurs=1, max_occurs=1)
    )
observationSequence._ContentModel = pyxb.binding.content.ParticleModel(observationSequence._GroupModel, min_occurs=1, max_occurs=1)
