# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/pro/le1_stub.py
# PyXB bindings for NamespaceModule
# NSM:23b1c64dcf05022ed49ac75f3cb8280755f2bfaf
# Generated 2014-03-17 11:53:47.252296 by PyXB version 1.1.2
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
import CommonDM.dm.ins.nis_stub
import CommonDM.dm.bas.fit_stub
import CommonDM.dm.bas.cot_stub
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

    """Data product type: sky, bias, dark, flat, wave-lamp, standard source"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'productType')
    _Documentation = u'Data product type: sky, bias, dark, flat, wave-lamp, standard source'
productType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=productType, enum_prefix=None)
productType.Object = productType._CF_enumeration.addEnumeration(unicode_value=u'Object')
productType.Bias = productType._CF_enumeration.addEnumeration(unicode_value=u'Bias')
productType.Dark = productType._CF_enumeration.addEnumeration(unicode_value=u'Dark')
productType.Flat = productType._CF_enumeration.addEnumeration(unicode_value=u'Flat')
productType.WaveLamp = productType._CF_enumeration.addEnumeration(unicode_value=u'WaveLamp')
productType.Std = productType._CF_enumeration.addEnumeration(unicode_value=u'Std')
productType._InitializeFacetMap(productType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'productType', productType)

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

# Complex type nispRawFrame with content type ELEMENT_ONLY
class nispRawFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nispRawFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}ObservationSequence uses Python identifier ObservationSequence
    __ObservationSequence = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObservationSequence'), 'ObservationSequence', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ObservationSequence', False)

    
    ObservationSequence = property(__ObservationSequence.value, __ObservationSequence.set, None, u'Information on the observation sequence in which the exposure is acquired')

    
    # Element {http://euclid.esa.org/schema/pro/le1}DataProduct uses Python identifier DataProduct
    __DataProduct = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataProduct'), 'DataProduct', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1DataProduct', False)

    
    DataProduct = property(__DataProduct.value, __DataProduct.set, None, u'Data product type and category (e.g. Image or Spectrum, Science or Calibration, Dark or Flat, etc.)')

    
    # Element {http://euclid.esa.org/schema/pro/le1}GrismWheelPos uses Python identifier GrismWheelPos
    __GrismWheelPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GrismWheelPos'), 'GrismWheelPos', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1GrismWheelPos', False)

    
    GrismWheelPos = property(__GrismWheelPos.value, __GrismWheelPos.set, None, u'Grism wheel position')

    
    # Element {http://euclid.esa.org/schema/pro/le1}CommandedFPAPointing uses Python identifier CommandedFPAPointing
    __CommandedFPAPointing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CommandedFPAPointing'), 'CommandedFPAPointing', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1CommandedFPAPointing', False)

    
    CommandedFPAPointing = property(__CommandedFPAPointing.value, __CommandedFPAPointing.set, None, u'Commanded FPA pointing (RA, DEC, Pointing Angle)')

    
    # Element {http://euclid.esa.org/schema/pro/le1}FilterWheelPos uses Python identifier FilterWheelPos
    __FilterWheelPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FilterWheelPos'), 'FilterWheelPos', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1FilterWheelPos', False)

    
    FilterWheelPos = property(__FilterWheelPos.value, __FilterWheelPos.set, None, u'Filter wheel position')

    
    # Element {http://euclid.esa.org/schema/pro/le1}InstrumentMode uses Python identifier InstrumentMode
    __InstrumentMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InstrumentMode'), 'InstrumentMode', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1InstrumentMode', False)

    
    InstrumentMode = property(__InstrumentMode.value, __InstrumentMode.set, None, u'Instrument mode during the exposure acquisition')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ObservationDate uses Python identifier ObservationDate
    __ObservationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate'), 'ObservationDate', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ObservationDate', False)

    
    ObservationDate = property(__ObservationDate.value, __ObservationDate.set, None, u'Observation date of the exposure')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ReconsFPAPointing uses Python identifier ReconsFPAPointing
    __ReconsFPAPointing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReconsFPAPointing'), 'ReconsFPAPointing', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ReconsFPAPointing', False)

    
    ReconsFPAPointing = property(__ReconsFPAPointing.value, __ReconsFPAPointing.set, None, u'Reconstructed FPA pointing (RA, DEC, Pointing Angle)')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ObservationMode uses Python identifier ObservationMode
    __ObservationMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode'), 'ObservationMode', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ObservationMode', False)

    
    ObservationMode = property(__ObservationMode.value, __ObservationMode.set, None, u'Observation mode: Wide Survey or Deep Survey')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ReadoutMode uses Python identifier ReadoutMode
    __ReadoutMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode'), 'ReadoutMode', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ReadoutMode', False)

    
    ReadoutMode = property(__ReadoutMode.value, __ReadoutMode.set, None, u'Readout mode used in this exposure')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ExposureTime uses Python identifier ExposureTime
    __ExposureTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime'), 'ExposureTime', '__httpeuclid_esa_orgschemaprole1_nispRawFrame_httpeuclid_esa_orgschemaprole1ExposureTime', False)

    
    ExposureTime = property(__ExposureTime.value, __ExposureTime.set, None, u'Exposure of the CCD in seconds')


    _ElementMap = {
        __ObservationSequence.name() : __ObservationSequence,
        __DataProduct.name() : __DataProduct,
        __GrismWheelPos.name() : __GrismWheelPos,
        __CommandedFPAPointing.name() : __CommandedFPAPointing,
        __FilterWheelPos.name() : __FilterWheelPos,
        __InstrumentMode.name() : __InstrumentMode,
        __ObservationDate.name() : __ObservationDate,
        __ReconsFPAPointing.name() : __ReconsFPAPointing,
        __ObservationMode.name() : __ObservationMode,
        __ReadoutMode.name() : __ReadoutMode,
        __ExposureTime.name() : __ExposureTime
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nispRawFrame', nispRawFrame)


# Complex type nispCalibrationFrame with content type ELEMENT_ONLY
class nispCalibrationFrame (nispRawFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nispCalibrationFrame')
    # Base type is nispRawFrame
    
    # Element GrismWheelPos ({http://euclid.esa.org/schema/pro/le1}GrismWheelPos) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element DataProduct ({http://euclid.esa.org/schema/pro/le1}DataProduct) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ObservationSequence ({http://euclid.esa.org/schema/pro/le1}ObservationSequence) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element {http://euclid.esa.org/schema/pro/le1}CalibUnit uses Python identifier CalibUnit
    __CalibUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CalibUnit'), 'CalibUnit', '__httpeuclid_esa_orgschemaprole1_nispCalibrationFrame_httpeuclid_esa_orgschemaprole1CalibUnit', False)

    
    CalibUnit = property(__CalibUnit.value, __CalibUnit.set, None, u' Calibration Unit (ON/OFF and intensity level)')

    
    # Element FilterWheelPos ({http://euclid.esa.org/schema/pro/le1}FilterWheelPos) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element InstrumentMode ({http://euclid.esa.org/schema/pro/le1}InstrumentMode) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ObservationDate ({http://euclid.esa.org/schema/pro/le1}ObservationDate) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element {http://euclid.esa.org/schema/pro/le1}DetectorList uses Python identifier DetectorList
    __DetectorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), 'DetectorList', '__httpeuclid_esa_orgschemaprole1_nispCalibrationFrame_httpeuclid_esa_orgschemaprole1DetectorList', False)

    
    DetectorList = property(__DetectorList.value, __DetectorList.set, None, None)

    
    # Element CommandedFPAPointing ({http://euclid.esa.org/schema/pro/le1}CommandedFPAPointing) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ReadoutMode ({http://euclid.esa.org/schema/pro/le1}ReadoutMode) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ObservationMode ({http://euclid.esa.org/schema/pro/le1}ObservationMode) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/le1}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ReconsFPAPointing ({http://euclid.esa.org/schema/pro/le1}ReconsFPAPointing) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame

    _ElementMap = nispRawFrame._ElementMap.copy()
    _ElementMap.update({
        __CalibUnit.name() : __CalibUnit,
        __DetectorList.name() : __DetectorList
    })
    _AttributeMap = nispRawFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'nispCalibrationFrame', nispCalibrationFrame)


# Complex type sirRawFrame with content type ELEMENT_ONLY
class sirRawFrame (nispRawFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sirRawFrame')
    # Base type is nispRawFrame
    
    # Element GrismWheelPos ({http://euclid.esa.org/schema/pro/le1}GrismWheelPos) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element DataProduct ({http://euclid.esa.org/schema/pro/le1}DataProduct) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ObservationSequence ({http://euclid.esa.org/schema/pro/le1}ObservationSequence) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element CommandedFPAPointing ({http://euclid.esa.org/schema/pro/le1}CommandedFPAPointing) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element FilterWheelPos ({http://euclid.esa.org/schema/pro/le1}FilterWheelPos) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element InstrumentMode ({http://euclid.esa.org/schema/pro/le1}InstrumentMode) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ObservationDate ({http://euclid.esa.org/schema/pro/le1}ObservationDate) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element {http://euclid.esa.org/schema/pro/le1}DetectorList uses Python identifier DetectorList
    __DetectorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), 'DetectorList', '__httpeuclid_esa_orgschemaprole1_sirRawFrame_httpeuclid_esa_orgschemaprole1DetectorList', False)

    
    DetectorList = property(__DetectorList.value, __DetectorList.set, None, None)

    
    # Element ReconsFPAPointing ({http://euclid.esa.org/schema/pro/le1}ReconsFPAPointing) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ObservationMode ({http://euclid.esa.org/schema/pro/le1}ObservationMode) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ReadoutMode ({http://euclid.esa.org/schema/pro/le1}ReadoutMode) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/le1}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame

    _ElementMap = nispRawFrame._ElementMap.copy()
    _ElementMap.update({
        __DetectorList.name() : __DetectorList
    })
    _AttributeMap = nispRawFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sirRawFrame', sirRawFrame)


# Complex type nisRawFrameFitsFile with content type ELEMENT_ONLY
class nisRawFrameFitsFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nisRawFrameFitsFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'le1.nisRawImage', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'nisRawFrameFitsFile', nisRawFrameFitsFile)


# Complex type sirRawFrameFitsFile with content type ELEMENT_ONLY
class sirRawFrameFitsFile (CommonDM.dm.bas.fit_stub.fitsFile):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sirRawFrameFitsFile')
    # Base type is CommonDM.dm.bas.fit_stub.fitsFile
    
    # Element DataContainer (DataContainer) inherited from {http://euclid.esa.org/schema/bas/fit}fitsFile
    
    # Attribute version is restricted from parent
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', CommonDM.dm.bas.fit_stub.fitsFormatVersion, fixed=True, unicode_default=u'0.1', required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format is restricted from parent
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', CommonDM.dm.bas.fit_stub.fitsFormatIdentifier, fixed=True, unicode_default=u'le1.sirRawImage', required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = CommonDM.dm.bas.fit_stub.fitsFile._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = CommonDM.dm.bas.fit_stub.fitsFile._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version,
        __format.name() : __format
    })
Namespace.addCategoryObject('typeBinding', u'sirRawFrameFitsFile', sirRawFrameFitsFile)


# Complex type detectorFrame with content type ELEMENT_ONLY
class detectorFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'detectorFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}ChipId uses Python identifier ChipId
    __ChipId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ChipId'), 'ChipId', '__httpeuclid_esa_orgschemaprole1_detectorFrame_httpeuclid_esa_orgschemaprole1ChipId', False)

    
    ChipId = property(__ChipId.value, __ChipId.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/le1}AstrometricSolution uses Python identifier AstrometricSolution
    __AstrometricSolution = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AstrometricSolution'), 'AstrometricSolution', '__httpeuclid_esa_orgschemaprole1_detectorFrame_httpeuclid_esa_orgschemaprole1AstrometricSolution', False)

    
    AstrometricSolution = property(__AstrometricSolution.value, __AstrometricSolution.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/le1}ReadoutNoise uses Python identifier ReadoutNoise
    __ReadoutNoise = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoise'), 'ReadoutNoise', '__httpeuclid_esa_orgschemaprole1_detectorFrame_httpeuclid_esa_orgschemaprole1ReadoutNoise', False)

    
    ReadoutNoise = property(__ReadoutNoise.value, __ReadoutNoise.set, None, None)

    
    # Element {http://euclid.esa.org/schema/pro/le1}Gain uses Python identifier Gain
    __Gain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Gain'), 'Gain', '__httpeuclid_esa_orgschemaprole1_detectorFrame_httpeuclid_esa_orgschemaprole1Gain', False)

    
    Gain = property(__Gain.value, __Gain.set, None, None)


    _ElementMap = {
        __ChipId.name() : __ChipId,
        __AstrometricSolution.name() : __AstrometricSolution,
        __ReadoutNoise.name() : __ReadoutNoise,
        __Gain.name() : __Gain
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'detectorFrame', detectorFrame)


# Complex type sirDetectorFrame with content type ELEMENT_ONLY
class sirDetectorFrame (detectorFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sirDetectorFrame')
    # Base type is detectorFrame
    
    # Element {http://euclid.esa.org/schema/pro/le1}DetectorFrameFitsFile uses Python identifier DetectorFrameFitsFile
    __DetectorFrameFitsFile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorFrameFitsFile'), 'DetectorFrameFitsFile', '__httpeuclid_esa_orgschemaprole1_sirDetectorFrame_httpeuclid_esa_orgschemaprole1DetectorFrameFitsFile', False)

    
    DetectorFrameFitsFile = property(__DetectorFrameFitsFile.value, __DetectorFrameFitsFile.set, None, None)

    
    # Element Gain ({http://euclid.esa.org/schema/pro/le1}Gain) inherited from {http://euclid.esa.org/schema/pro/le1}detectorFrame
    
    # Element AstrometricSolution ({http://euclid.esa.org/schema/pro/le1}AstrometricSolution) inherited from {http://euclid.esa.org/schema/pro/le1}detectorFrame
    
    # Element ReadoutNoise ({http://euclid.esa.org/schema/pro/le1}ReadoutNoise) inherited from {http://euclid.esa.org/schema/pro/le1}detectorFrame
    
    # Element ChipId ({http://euclid.esa.org/schema/pro/le1}ChipId) inherited from {http://euclid.esa.org/schema/pro/le1}detectorFrame

    _ElementMap = detectorFrame._ElementMap.copy()
    _ElementMap.update({
        __DetectorFrameFitsFile.name() : __DetectorFrameFitsFile
    })
    _AttributeMap = detectorFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sirDetectorFrame', sirDetectorFrame)


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


# Complex type readoutMode with content type ELEMENT_ONLY
class readoutMode (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'readoutMode')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}ExpSampleTime uses Python identifier ExpSampleTime
    __ExpSampleTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExpSampleTime'), 'ExpSampleTime', '__httpeuclid_esa_orgschemaprole1_readoutMode_httpeuclid_esa_orgschemaprole1ExpSampleTime', False)

    
    ExpSampleTime = property(__ExpSampleTime.value, __ExpSampleTime.set, None, u' Exposure time in seconds for single samples of the readout')

    
    # Element {http://euclid.esa.org/schema/pro/le1}NumSamples uses Python identifier NumSamples
    __NumSamples = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumSamples'), 'NumSamples', '__httpeuclid_esa_orgschemaprole1_readoutMode_httpeuclid_esa_orgschemaprole1NumSamples', False)

    
    NumSamples = property(__NumSamples.value, __NumSamples.set, None, u' Number of exposures performed in the readout')

    
    # Element {http://euclid.esa.org/schema/pro/le1}ReadoutModeMethod uses Python identifier ReadoutModeMethod
    __ReadoutModeMethod = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReadoutModeMethod'), 'ReadoutModeMethod', '__httpeuclid_esa_orgschemaprole1_readoutMode_httpeuclid_esa_orgschemaprole1ReadoutModeMethod', False)

    
    ReadoutModeMethod = property(__ReadoutModeMethod.value, __ReadoutModeMethod.set, None, u' Redout method used')


    _ElementMap = {
        __ExpSampleTime.name() : __ExpSampleTime,
        __NumSamples.name() : __NumSamples,
        __ReadoutModeMethod.name() : __ReadoutModeMethod
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'readoutMode', readoutMode)


# Complex type nirRawFrame with content type ELEMENT_ONLY
class nirRawFrame (nispRawFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nirRawFrame')
    # Base type is nispRawFrame
    
    # Element ObservationSequence ({http://euclid.esa.org/schema/pro/le1}ObservationSequence) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element DataProduct ({http://euclid.esa.org/schema/pro/le1}DataProduct) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element GrismWheelPos ({http://euclid.esa.org/schema/pro/le1}GrismWheelPos) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element CommandedFPAPointing ({http://euclid.esa.org/schema/pro/le1}CommandedFPAPointing) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element FilterWheelPos ({http://euclid.esa.org/schema/pro/le1}FilterWheelPos) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element InstrumentMode ({http://euclid.esa.org/schema/pro/le1}InstrumentMode) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ObservationDate ({http://euclid.esa.org/schema/pro/le1}ObservationDate) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element {http://euclid.esa.org/schema/pro/le1}DetectorList uses Python identifier DetectorList
    __DetectorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), 'DetectorList', '__httpeuclid_esa_orgschemaprole1_nirRawFrame_httpeuclid_esa_orgschemaprole1DetectorList', False)

    
    DetectorList = property(__DetectorList.value, __DetectorList.set, None, None)

    
    # Element ObservationMode ({http://euclid.esa.org/schema/pro/le1}ObservationMode) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ReadoutMode ({http://euclid.esa.org/schema/pro/le1}ReadoutMode) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ExposureTime ({http://euclid.esa.org/schema/pro/le1}ExposureTime) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame
    
    # Element ReconsFPAPointing ({http://euclid.esa.org/schema/pro/le1}ReconsFPAPointing) inherited from {http://euclid.esa.org/schema/pro/le1}nispRawFrame

    _ElementMap = nispRawFrame._ElementMap.copy()
    _ElementMap.update({
        __DetectorList.name() : __DetectorList
    })
    _AttributeMap = nispRawFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'nirRawFrame', nirRawFrame)


# Complex type nisDetectorFrameList with content type ELEMENT_ONLY
class nisDetectorFrameList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nisDetectorFrameList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}Detector uses Python identifier Detector
    __Detector = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Detector'), 'Detector', '__httpeuclid_esa_orgschemaprole1_nisDetectorFrameList_httpeuclid_esa_orgschemaprole1Detector', True)

    
    Detector = property(__Detector.value, __Detector.set, None, None)


    _ElementMap = {
        __Detector.name() : __Detector
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nisDetectorFrameList', nisDetectorFrameList)


# Complex type nisDetectorFrame with content type ELEMENT_ONLY
class nisDetectorFrame (detectorFrame):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nisDetectorFrame')
    # Base type is detectorFrame
    
    # Element Gain ({http://euclid.esa.org/schema/pro/le1}Gain) inherited from {http://euclid.esa.org/schema/pro/le1}detectorFrame
    
    # Element AstrometricSolution ({http://euclid.esa.org/schema/pro/le1}AstrometricSolution) inherited from {http://euclid.esa.org/schema/pro/le1}detectorFrame
    
    # Element ChipId ({http://euclid.esa.org/schema/pro/le1}ChipId) inherited from {http://euclid.esa.org/schema/pro/le1}detectorFrame
    
    # Element ReadoutNoise ({http://euclid.esa.org/schema/pro/le1}ReadoutNoise) inherited from {http://euclid.esa.org/schema/pro/le1}detectorFrame
    
    # Element {http://euclid.esa.org/schema/pro/le1}DetectorFrameFitsFile uses Python identifier DetectorFrameFitsFile
    __DetectorFrameFitsFile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DetectorFrameFitsFile'), 'DetectorFrameFitsFile', '__httpeuclid_esa_orgschemaprole1_nisDetectorFrame_httpeuclid_esa_orgschemaprole1DetectorFrameFitsFile', False)

    
    DetectorFrameFitsFile = property(__DetectorFrameFitsFile.value, __DetectorFrameFitsFile.set, None, None)


    _ElementMap = detectorFrame._ElementMap.copy()
    _ElementMap.update({
        __DetectorFrameFitsFile.name() : __DetectorFrameFitsFile
    })
    _AttributeMap = detectorFrame._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'nisDetectorFrame', nisDetectorFrame)


# Complex type sirDetectorFrameList with content type ELEMENT_ONLY
class sirDetectorFrameList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sirDetectorFrameList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}Detector uses Python identifier Detector
    __Detector = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Detector'), 'Detector', '__httpeuclid_esa_orgschemaprole1_sirDetectorFrameList_httpeuclid_esa_orgschemaprole1Detector', True)

    
    Detector = property(__Detector.value, __Detector.set, None, None)


    _ElementMap = {
        __Detector.name() : __Detector
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sirDetectorFrameList', sirDetectorFrameList)


# Complex type nispCalibUnit with content type ELEMENT_ONLY
class nispCalibUnit (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nispCalibUnit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/pro/le1}IntensityLevel uses Python identifier IntensityLevel
    __IntensityLevel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IntensityLevel'), 'IntensityLevel', '__httpeuclid_esa_orgschemaprole1_nispCalibUnit_httpeuclid_esa_orgschemaprole1IntensityLevel', False)

    
    IntensityLevel = property(__IntensityLevel.value, __IntensityLevel.set, None, u' Calibration lamp intensity level (in W/m2)')

    
    # Element {http://euclid.esa.org/schema/pro/le1}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Status'), 'Status', '__httpeuclid_esa_orgschemaprole1_nispCalibUnit_httpeuclid_esa_orgschemaprole1Status', False)

    
    Status = property(__Status.value, __Status.set, None, u'Calibration unit status (ON=1, OFF=0)')


    _ElementMap = {
        __IntensityLevel.name() : __IntensityLevel,
        __Status.name() : __Status
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nispCalibUnit', nispCalibUnit)




nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservationSequence'), observationSequence, scope=nispRawFrame, documentation=u'Information on the observation sequence in which the exposure is acquired'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataProduct'), dataProduct, scope=nispRawFrame, documentation=u'Data product type and category (e.g. Image or Spectrum, Science or Calibration, Dark or Flat, etc.)'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GrismWheelPos'), grismWheelPosition, scope=nispRawFrame, documentation=u'Grism wheel position'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CommandedFPAPointing'), fpaPointing, scope=nispRawFrame, documentation=u'Commanded FPA pointing (RA, DEC, Pointing Angle)'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FilterWheelPos'), filterWheelPosition, scope=nispRawFrame, documentation=u'Filter wheel position'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InstrumentMode'), instrumentMode, scope=nispRawFrame, documentation=u'Instrument mode during the exposure acquisition'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate'), pyxb.binding.datatypes.dateTime, scope=nispRawFrame, documentation=u'Observation date of the exposure'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReconsFPAPointing'), fpaPointing, scope=nispRawFrame, documentation=u'Reconstructed FPA pointing (RA, DEC, Pointing Angle)'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode'), observationMode, scope=nispRawFrame, documentation=u'Observation mode: Wide Survey or Deep Survey'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode'), readoutMode, scope=nispRawFrame, documentation=u'Readout mode used in this exposure'))

nispRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime'), CommonDM.dm.ins.nis_stub.exposureTime, scope=nispRawFrame, documentation=u'Exposure of the CCD in seconds'))
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



nispCalibrationFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CalibUnit'), nispCalibUnit, scope=nispCalibrationFrame, documentation=u' Calibration Unit (ON/OFF and intensity level)'))

nispCalibrationFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), nisDetectorFrameList, scope=nispCalibrationFrame))
nispCalibrationFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationSequence')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InstrumentMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataProduct')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CommandedFPAPointing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReconsFPAPointing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GrismWheelPos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FilterWheelPos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode')), min_occurs=1, max_occurs=1)
    )
nispCalibrationFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CalibUnit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorList')), min_occurs=1, max_occurs=1)
    )
nispCalibrationFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibrationFrame._GroupModel_2, min_occurs=1, max_occurs=1)
    )
nispCalibrationFrame._ContentModel = pyxb.binding.content.ParticleModel(nispCalibrationFrame._GroupModel, min_occurs=1, max_occurs=1)



sirRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), sirDetectorFrameList, scope=sirRawFrame))
sirRawFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationSequence')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InstrumentMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataProduct')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CommandedFPAPointing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReconsFPAPointing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GrismWheelPos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FilterWheelPos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode')), min_occurs=1, max_occurs=1)
    )
sirRawFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorList')), min_occurs=1, max_occurs=1)
    )
sirRawFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sirRawFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirRawFrame._GroupModel_2, min_occurs=1, max_occurs=1)
    )
sirRawFrame._ContentModel = pyxb.binding.content.ParticleModel(sirRawFrame._GroupModel, min_occurs=1, max_occurs=1)


nisRawFrameFitsFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nisRawFrameFitsFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
nisRawFrameFitsFile._ContentModel = pyxb.binding.content.ParticleModel(nisRawFrameFitsFile._GroupModel, min_occurs=1, max_occurs=1)


sirRawFrameFitsFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sirRawFrameFitsFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
sirRawFrameFitsFile._ContentModel = pyxb.binding.content.ParticleModel(sirRawFrameFitsFile._GroupModel, min_occurs=1, max_occurs=1)



detectorFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ChipId'), pyxb.binding.datatypes.int, scope=detectorFrame))

detectorFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AstrometricSolution'), CommonDM.dm.bas.cot_stub.astrom, scope=detectorFrame))

detectorFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoise'), pyxb.binding.datatypes.double, scope=detectorFrame))

detectorFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Gain'), pyxb.binding.datatypes.double, scope=detectorFrame))
detectorFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(detectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ChipId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Gain')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoise')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(detectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AstrometricSolution')), min_occurs=1, max_occurs=1)
    )
detectorFrame._ContentModel = pyxb.binding.content.ParticleModel(detectorFrame._GroupModel, min_occurs=1, max_occurs=1)



sirDetectorFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorFrameFitsFile'), sirRawFrameFitsFile, scope=sirDetectorFrame))
sirDetectorFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sirDetectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ChipId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirDetectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Gain')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirDetectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoise')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirDetectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AstrometricSolution')), min_occurs=1, max_occurs=1)
    )
sirDetectorFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sirDetectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorFrameFitsFile')), min_occurs=1, max_occurs=1)
    )
sirDetectorFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sirDetectorFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sirDetectorFrame._GroupModel_2, min_occurs=1, max_occurs=1)
    )
sirDetectorFrame._ContentModel = pyxb.binding.content.ParticleModel(sirDetectorFrame._GroupModel, min_occurs=1, max_occurs=1)



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



readoutMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpSampleTime'), CommonDM.dm.ins.nis_stub.exposureTime, scope=readoutMode, documentation=u' Exposure time in seconds for single samples of the readout'))

readoutMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumSamples'), pyxb.binding.datatypes.int, scope=readoutMode, documentation=u' Number of exposures performed in the readout'))

readoutMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReadoutModeMethod'), readoutModeMethod, scope=readoutMode, documentation=u' Redout method used'))
readoutMode._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(readoutMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutModeMethod')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readoutMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumSamples')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(readoutMode._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpSampleTime')), min_occurs=1, max_occurs=1)
    )
readoutMode._ContentModel = pyxb.binding.content.ParticleModel(readoutMode._GroupModel, min_occurs=1, max_occurs=1)



nirRawFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorList'), nisDetectorFrameList, scope=nirRawFrame))
nirRawFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationSequence')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InstrumentMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationMode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataProduct')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservationDate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExposureTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CommandedFPAPointing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReconsFPAPointing')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GrismWheelPos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FilterWheelPos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutMode')), min_occurs=1, max_occurs=1)
    )
nirRawFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nirRawFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorList')), min_occurs=1, max_occurs=1)
    )
nirRawFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nirRawFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nirRawFrame._GroupModel_2, min_occurs=1, max_occurs=1)
    )
nirRawFrame._ContentModel = pyxb.binding.content.ParticleModel(nirRawFrame._GroupModel, min_occurs=1, max_occurs=1)



nisDetectorFrameList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Detector'), nisDetectorFrame, scope=nisDetectorFrameList))
nisDetectorFrameList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nisDetectorFrameList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Detector')), min_occurs=1, max_occurs=None)
    )
nisDetectorFrameList._ContentModel = pyxb.binding.content.ParticleModel(nisDetectorFrameList._GroupModel, min_occurs=1, max_occurs=1)



nisDetectorFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectorFrameFitsFile'), nisRawFrameFitsFile, scope=nisDetectorFrame))
nisDetectorFrame._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nisDetectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ChipId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nisDetectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Gain')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nisDetectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReadoutNoise')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nisDetectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AstrometricSolution')), min_occurs=1, max_occurs=1)
    )
nisDetectorFrame._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nisDetectorFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectorFrameFitsFile')), min_occurs=1, max_occurs=1)
    )
nisDetectorFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nisDetectorFrame._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nisDetectorFrame._GroupModel_2, min_occurs=1, max_occurs=1)
    )
nisDetectorFrame._ContentModel = pyxb.binding.content.ParticleModel(nisDetectorFrame._GroupModel, min_occurs=1, max_occurs=1)



sirDetectorFrameList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Detector'), sirDetectorFrame, scope=sirDetectorFrameList))
sirDetectorFrameList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sirDetectorFrameList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Detector')), min_occurs=1, max_occurs=None)
    )
sirDetectorFrameList._ContentModel = pyxb.binding.content.ParticleModel(sirDetectorFrameList._GroupModel, min_occurs=1, max_occurs=1)



nispCalibUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IntensityLevel'), pyxb.binding.datatypes.double, scope=nispCalibUnit, documentation=u' Calibration lamp intensity level (in W/m2)'))

nispCalibUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Status'), pyxb.binding.datatypes.boolean, scope=nispCalibUnit, documentation=u'Calibration unit status (ON=1, OFF=0)'))
nispCalibUnit._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nispCalibUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Status')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(nispCalibUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IntensityLevel')), min_occurs=1, max_occurs=1)
    )
nispCalibUnit._ContentModel = pyxb.binding.content.ParticleModel(nispCalibUnit._GroupModel, min_occurs=1, max_occurs=1)
