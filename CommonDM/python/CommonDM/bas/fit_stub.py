# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/bas/fit_stub.py
# PyXB bindings for NamespaceModule
# NSM:975654cc63c7654a0853e9fafa22678e8820cfb9
# Generated 2014-03-14 15:21:54.439935 by PyXB version 1.1.2
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
import CommonDM.sys.sgs_stub
import CommonDM.bas.imp.fits_stub
import CommonDM.bas.utd_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/fit', create_if_missing=True)
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
class fitsFormatVersion (pyxb.binding.datatypes.string):

    """The version of a FITS format. The version of a format (in the XML files) must be increased after any modification. Multiple versions of formats with the same identifier can coexist in the same version of the Data Model."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fitsFormatVersion')
    _Documentation = u'The version of a FITS format. The version of a format (in the XML files) must be increased after any modification. Multiple versions of formats with the same identifier can coexist in the same version of the Data Model.'
fitsFormatVersion._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'fitsFormatVersion', fitsFormatVersion)

# Atomic SimpleTypeDefinition
class fitsFormatIdentifier (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An identifier of a FITS format. Each Euclid metatada XML with a FITS file reference contains an instance of this identifier, which can be mapped to a FITS format description XML file in the Instances/fit directory of the Data Model. The format of the identifier is "ou_name.format_name", where ou_name is the name of the OU defining the FITS format (this is to avoid conflicts between OUs) and format_name is the identifier of the format. The CCB is responsible for validating that entries in this list of identifiers follow the correct format and the uniqueness of the format implementations in the Instances/fit directory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fitsFormatIdentifier')
    _Documentation = u'An identifier of a FITS format. Each Euclid metatada XML with a FITS file reference contains an instance of this identifier, which can be mapped to a FITS format description XML file in the Instances/fit directory of the Data Model. The format of the identifier is "ou_name.format_name", where ou_name is the name of the OU defining the FITS format (this is to avoid conflicts between OUs) and format_name is the identifier of the format. The CCB is responsible for validating that entries in this list of identifiers follow the correct format and the uniqueness of the format implementations in the Instances/fit directory.'
fitsFormatIdentifier._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fitsFormatIdentifier, enum_prefix=None)
fitsFormatIdentifier.sim_catalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.catalog')
fitsFormatIdentifier.le3_catalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le3.catalog')
fitsFormatIdentifier.le3_athena_output_shearshear2d = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le3.athena.output.shearshear2d')
fitsFormatIdentifier.le3_pallas_output_shearshearpspec2d = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le3.pallas.output.shearshearpspec2d')
fitsFormatIdentifier.sim_spectra = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.spectra')
fitsFormatIdentifier.sim_simulatedImage = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.simulatedImage')
fitsFormatIdentifier.sim_spectrum = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.spectrum')
fitsFormatIdentifier.sim_nipSimulatedImage = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sim.nipSimulatedImage')
fitsFormatIdentifier.nis_pixelPsf = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.pixelPsf')
fitsFormatIdentifier.nis_transmission = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.transmission')
fitsFormatIdentifier.nis_detectorQuantumEfficiencyMap = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.detectorQuantumEfficiencyMap')
fitsFormatIdentifier.nis_detectorQuantumEfficiencyCube = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.detectorQuantumEfficiencyCube')
fitsFormatIdentifier.nis_detectorReadoutNoiseMap = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.detectorReadoutNoiseMap')
fitsFormatIdentifier.nis_detectorDarkCurrentMap = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.detectorDarkCurrentMap')
fitsFormatIdentifier.nis_cosmicRayMap = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'nis.cosmicRayMap')
fitsFormatIdentifier.sky_absorptionFactors = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sky.absorptionFactors')
fitsFormatIdentifier.spm_spectrum = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'spm.spectrum')
fitsFormatIdentifier.phz_filter = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'phz.filter')
fitsFormatIdentifier.phz_sed = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'phz.sed')
fitsFormatIdentifier.phz_reddeningCurve = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'phz.reddeningCurve')
fitsFormatIdentifier.phz_photometryCatalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'phz.photometryCatalog')
fitsFormatIdentifier.phz_specZCatalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'phz.specZCatalog')
fitsFormatIdentifier.phz_photoZCatalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'phz.photoZCatalog')
fitsFormatIdentifier.phz_pdf = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'phz.pdf')
fitsFormatIdentifier.sl_merCatalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sl.merCatalog')
fitsFormatIdentifier.sl_shearCatalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sl.shearCatalog')
fitsFormatIdentifier.sl_specZCatalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sl.specZCatalog')
fitsFormatIdentifier.sl_photoZCatalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sl.photoZCatalog')
fitsFormatIdentifier.sl_preSelectedCatalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sl.preSelectedCatalog')
fitsFormatIdentifier.sl_subtractedImage = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sl.subtractedImage')
fitsFormatIdentifier.sl_lensCandidatesCatalog = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'sl.lensCandidatesCatalog')
fitsFormatIdentifier.le1_nisRawImage = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le1.nisRawImage')
fitsFormatIdentifier.le1_sirRawImage = fitsFormatIdentifier._CF_enumeration.addEnumeration(unicode_value=u'le1.sirRawImage')
fitsFormatIdentifier._InitializeFacetMap(fitsFormatIdentifier._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'fitsFormatIdentifier', fitsFormatIdentifier)

# Atomic SimpleTypeDefinition
class STD_ANON (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.int(1))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive)

# Atomic SimpleTypeDefinition
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.emptyString = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'*')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Union SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class hduMultiplicity (pyxb.binding.basis.STD_union):

    """Defines the allowed values for the multiplicity of an HDU. It can be a positive integer, which specifies the number the HDUs following this format, or the '*' character, which specifies that the HDU format can be repeated an undefined number of times."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hduMultiplicity')
    _Documentation = u"Defines the allowed values for the multiplicity of an HDU. It can be a positive integer, which specifies the number the HDUs following this format, or the '*' character, which specifies that the HDU format can be repeated an undefined number of times."

    _MemberTypes = ( STD_ANON, STD_ANON_, )
hduMultiplicity.emptyString = u'*'                # originally STD_ANON_.emptyString
hduMultiplicity._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'hduMultiplicity', hduMultiplicity)

# Complex type fitsFile with content type ELEMENT_ONLY
class fitsFile (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fitsFile')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DataContainer uses Python identifier DataContainer
    __DataContainer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'DataContainer'), 'DataContainer', '__httpeuclid_esa_orgschemabasfit_fitsFile_DataContainer', False)

    
    DataContainer = property(__DataContainer.value, __DataContainer.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFile_version', fitsFormatVersion, required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_fitsFile_format', fitsFormatIdentifier, required=True)
    
    format = property(__format.value, __format.set, None, None)


    _ElementMap = {
        __DataContainer.name() : __DataContainer
    }
    _AttributeMap = {
        __version.name() : __version,
        __format.name() : __format
    }
Namespace.addCategoryObject('typeBinding', u'fitsFile', fitsFile)


# Complex type genericHdu with content type ELEMENT_ONLY
class genericHdu (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'genericHdu')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}HeaderKeywordList uses Python identifier HeaderKeywordList
    __HeaderKeywordList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HeaderKeywordList'), 'HeaderKeywordList', '__httpeuclid_esa_orgschemabasfit_genericHdu_httpeuclid_esa_orgschemabasfitHeaderKeywordList', False)

    
    HeaderKeywordList = property(__HeaderKeywordList.value, __HeaderKeywordList.set, None, None)

    
    # Attribute multiplicity uses Python identifier multiplicity
    __multiplicity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'multiplicity'), 'multiplicity', '__httpeuclid_esa_orgschemabasfit_genericHdu_multiplicity', hduMultiplicity)
    
    multiplicity = property(__multiplicity.value, __multiplicity.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_genericHdu_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __HeaderKeywordList.name() : __HeaderKeywordList
    }
    _AttributeMap = {
        __multiplicity.name() : __multiplicity,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'genericHdu', genericHdu)


# Complex type tableHdu with content type ELEMENT_ONLY
class tableHdu (genericHdu):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'tableHdu')
    # Base type is genericHdu
    
    # Element HeaderKeywordList ({http://euclid.esa.org/schema/bas/fit}HeaderKeywordList) inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu
    
    # Element {http://euclid.esa.org/schema/bas/fit}ColumnList uses Python identifier ColumnList
    __ColumnList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ColumnList'), 'ColumnList', '__httpeuclid_esa_orgschemabasfit_tableHdu_httpeuclid_esa_orgschemabasfitColumnList', False)

    
    ColumnList = property(__ColumnList.value, __ColumnList.set, None, None)

    
    # Attribute multiplicity inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu
    
    # Attribute name inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu

    _ElementMap = genericHdu._ElementMap.copy()
    _ElementMap.update({
        __ColumnList.name() : __ColumnList
    })
    _AttributeMap = genericHdu._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'tableHdu', tableHdu)


# Complex type arrayHdu with content type ELEMENT_ONLY
class arrayHdu (genericHdu):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'arrayHdu')
    # Base type is genericHdu
    
    # Element HeaderKeywordList ({http://euclid.esa.org/schema/bas/fit}HeaderKeywordList) inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu
    
    # Element {http://euclid.esa.org/schema/bas/fit}WCSList uses Python identifier WCSList
    __WCSList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WCSList'), 'WCSList', '__httpeuclid_esa_orgschemabasfit_arrayHdu_httpeuclid_esa_orgschemabasfitWCSList', False)

    
    WCSList = property(__WCSList.value, __WCSList.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}ArrayInfo uses Python identifier ArrayInfo
    __ArrayInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ArrayInfo'), 'ArrayInfo', '__httpeuclid_esa_orgschemabasfit_arrayHdu_httpeuclid_esa_orgschemabasfitArrayInfo', False)

    
    ArrayInfo = property(__ArrayInfo.value, __ArrayInfo.set, None, None)

    
    # Attribute multiplicity inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu
    
    # Attribute name inherited from {http://euclid.esa.org/schema/bas/fit}genericHdu

    _ElementMap = genericHdu._ElementMap.copy()
    _ElementMap.update({
        __WCSList.name() : __WCSList,
        __ArrayInfo.name() : __ArrayInfo
    })
    _AttributeMap = genericHdu._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'arrayHdu', arrayHdu)


# Complex type hduGroup with content type ELEMENT_ONLY
class hduGroup (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hduGroup')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}ArrayHDU uses Python identifier ArrayHDU
    __ArrayHDU = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ArrayHDU'), 'ArrayHDU', '__httpeuclid_esa_orgschemabasfit_hduGroup_httpeuclid_esa_orgschemabasfitArrayHDU', True)

    
    ArrayHDU = property(__ArrayHDU.value, __ArrayHDU.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}GenericHDU uses Python identifier GenericHDU
    __GenericHDU = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GenericHDU'), 'GenericHDU', '__httpeuclid_esa_orgschemabasfit_hduGroup_httpeuclid_esa_orgschemabasfitGenericHDU', True)

    
    GenericHDU = property(__GenericHDU.value, __GenericHDU.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}TableHDU uses Python identifier TableHDU
    __TableHDU = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TableHDU'), 'TableHDU', '__httpeuclid_esa_orgschemabasfit_hduGroup_httpeuclid_esa_orgschemabasfitTableHDU', True)

    
    TableHDU = property(__TableHDU.value, __TableHDU.set, None, None)

    
    # Attribute multiplicity uses Python identifier multiplicity
    __multiplicity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'multiplicity'), 'multiplicity', '__httpeuclid_esa_orgschemabasfit_hduGroup_multiplicity', hduMultiplicity)
    
    multiplicity = property(__multiplicity.value, __multiplicity.set, None, None)


    _ElementMap = {
        __ArrayHDU.name() : __ArrayHDU,
        __GenericHDU.name() : __GenericHDU,
        __TableHDU.name() : __TableHDU
    }
    _AttributeMap = {
        __multiplicity.name() : __multiplicity
    }
Namespace.addCategoryObject('typeBinding', u'hduGroup', hduGroup)


# Complex type fitsFormat with content type ELEMENT_ONLY
class fitsFormat (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fitsFormat')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}ArrayHDU uses Python identifier ArrayHDU
    __ArrayHDU = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ArrayHDU'), 'ArrayHDU', '__httpeuclid_esa_orgschemabasfit_fitsFormat_httpeuclid_esa_orgschemabasfitArrayHDU', True)

    
    ArrayHDU = property(__ArrayHDU.value, __ArrayHDU.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}HDUGroup uses Python identifier HDUGroup
    __HDUGroup = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HDUGroup'), 'HDUGroup', '__httpeuclid_esa_orgschemabasfit_fitsFormat_httpeuclid_esa_orgschemabasfitHDUGroup', True)

    
    HDUGroup = property(__HDUGroup.value, __HDUGroup.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}TableHDU uses Python identifier TableHDU
    __TableHDU = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TableHDU'), 'TableHDU', '__httpeuclid_esa_orgschemabasfit_fitsFormat_httpeuclid_esa_orgschemabasfitTableHDU', True)

    
    TableHDU = property(__TableHDU.value, __TableHDU.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}GenericHDU uses Python identifier GenericHDU
    __GenericHDU = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GenericHDU'), 'GenericHDU', '__httpeuclid_esa_orgschemabasfit_fitsFormat_httpeuclid_esa_orgschemabasfitGenericHDU', True)

    
    GenericHDU = property(__GenericHDU.value, __GenericHDU.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpeuclid_esa_orgschemabasfit_fitsFormat_version', fitsFormatVersion, required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpeuclid_esa_orgschemabasfit_fitsFormat_id', fitsFormatIdentifier, required=True)
    
    id = property(__id.value, __id.set, None, None)


    _ElementMap = {
        __ArrayHDU.name() : __ArrayHDU,
        __HDUGroup.name() : __HDUGroup,
        __TableHDU.name() : __TableHDU,
        __GenericHDU.name() : __GenericHDU
    }
    _AttributeMap = {
        __version.name() : __version,
        __id.name() : __id
    }
Namespace.addCategoryObject('typeBinding', u'fitsFormat', fitsFormat)


# Complex type fitsFormatList with content type ELEMENT_ONLY
class fitsFormatList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fitsFormatList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}FitsFormat uses Python identifier FitsFormat
    __FitsFormat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FitsFormat'), 'FitsFormat', '__httpeuclid_esa_orgschemabasfit_fitsFormatList_httpeuclid_esa_orgschemabasfitFitsFormat', True)

    
    FitsFormat = property(__FitsFormat.value, __FitsFormat.set, None, None)


    _ElementMap = {
        __FitsFormat.name() : __FitsFormat
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'fitsFormatList', fitsFormatList)


# Complex type headerComplexIntegerKeyword with content type EMPTY
class headerComplexIntegerKeyword (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerComplexIntegerKeyword')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerComplexIntegerKeyword_fixed', CommonDM.bas.imp.fits_stub.complexIntegerKeywordValue)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerComplexIntegerKeyword_name', CommonDM.bas.imp.fits_stub.headerKeywordName, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __fixed.name() : __fixed,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'headerComplexIntegerKeyword', headerComplexIntegerKeyword)


# Complex type binaryTableColumn with content type EMPTY
class binaryTableColumn (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'binaryTableColumn')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_binaryTableColumn_name', CommonDM.bas.imp.fits_stub.binaryTableColumnName, required=True)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_binaryTableColumn_format', CommonDM.bas.imp.fits_stub.binaryTableColumnFormat, required=True)
    
    format = property(__format.value, __format.set, None, None)

    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpeuclid_esa_orgschemabasfit_binaryTableColumn_unit', CommonDM.bas.utd_stub.unit, required=True)
    
    unit = property(__unit.value, __unit.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name,
        __format.name() : __format,
        __unit.name() : __unit
    }
Namespace.addCategoryObject('typeBinding', u'binaryTableColumn', binaryTableColumn)


# Complex type arrayInfo with content type EMPTY
class arrayInfo (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'arrayInfo')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format'), 'format', '__httpeuclid_esa_orgschemabasfit_arrayInfo_format', CommonDM.bas.imp.fits_stub.arrayFormat, required=True)
    
    format = property(__format.value, __format.set, None, None)

    
    # Attribute numberOfDimentions uses Python identifier numberOfDimentions
    __numberOfDimentions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numberOfDimentions'), 'numberOfDimentions', '__httpeuclid_esa_orgschemabasfit_arrayInfo_numberOfDimentions', CommonDM.bas.imp.fits_stub.arrayNumberOfDimensions, required=True)
    
    numberOfDimentions = property(__numberOfDimentions.value, __numberOfDimentions.set, None, None)

    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpeuclid_esa_orgschemabasfit_arrayInfo_unit', CommonDM.bas.utd_stub.unit, required=True)
    
    unit = property(__unit.value, __unit.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __format.name() : __format,
        __numberOfDimentions.name() : __numberOfDimentions,
        __unit.name() : __unit
    }
Namespace.addCategoryObject('typeBinding', u'arrayInfo', arrayInfo)


# Complex type headerUndefinedKeyword with content type EMPTY
class headerUndefinedKeyword (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerUndefinedKeyword')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerUndefinedKeyword_name', CommonDM.bas.imp.fits_stub.headerKeywordName, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'headerUndefinedKeyword', headerUndefinedKeyword)


# Complex type headerStringKeyword with content type EMPTY
class headerStringKeyword (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerStringKeyword')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerStringKeyword_fixed', CommonDM.bas.imp.fits_stub.stringKeywordValue)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerStringKeyword_name', CommonDM.bas.imp.fits_stub.headerKeywordName, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __fixed.name() : __fixed,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'headerStringKeyword', headerStringKeyword)


# Complex type headerLogicalKeyword with content type EMPTY
class headerLogicalKeyword (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerLogicalKeyword')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerLogicalKeyword_fixed', CommonDM.bas.imp.fits_stub.logicalKeywordValue)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerLogicalKeyword_name', CommonDM.bas.imp.fits_stub.headerKeywordName, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __fixed.name() : __fixed,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'headerLogicalKeyword', headerLogicalKeyword)


# Complex type headerIntegerKeyword with content type EMPTY
class headerIntegerKeyword (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerIntegerKeyword')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerIntegerKeyword_fixed', CommonDM.bas.imp.fits_stub.integerKeywordValue)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerIntegerKeyword_name', CommonDM.bas.imp.fits_stub.headerKeywordName, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __fixed.name() : __fixed,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'headerIntegerKeyword', headerIntegerKeyword)


# Complex type headerDoubleKeyword with content type EMPTY
class headerDoubleKeyword (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerDoubleKeyword')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerDoubleKeyword_fixed', CommonDM.bas.imp.fits_stub.doubleKeywordValue)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerDoubleKeyword_name', CommonDM.bas.imp.fits_stub.headerKeywordName, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __fixed.name() : __fixed,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'headerDoubleKeyword', headerDoubleKeyword)


# Complex type headerComplexDoubleKeyword with content type EMPTY
class headerComplexDoubleKeyword (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerComplexDoubleKeyword')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpeuclid_esa_orgschemabasfit_headerComplexDoubleKeyword_fixed', CommonDM.bas.imp.fits_stub.complexDoubleKeywordValue)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_headerComplexDoubleKeyword_name', CommonDM.bas.imp.fits_stub.headerKeywordName, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __fixed.name() : __fixed,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'headerComplexDoubleKeyword', headerComplexDoubleKeyword)


# Complex type headerKeywordList with content type ELEMENT_ONLY
class headerKeywordList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'headerKeywordList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}IntegerKeyword uses Python identifier IntegerKeyword
    __IntegerKeyword = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IntegerKeyword'), 'IntegerKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitIntegerKeyword', True)

    
    IntegerKeyword = property(__IntegerKeyword.value, __IntegerKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}ComplexIntegerKeyword uses Python identifier ComplexIntegerKeyword
    __ComplexIntegerKeyword = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComplexIntegerKeyword'), 'ComplexIntegerKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitComplexIntegerKeyword', True)

    
    ComplexIntegerKeyword = property(__ComplexIntegerKeyword.value, __ComplexIntegerKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}DoubleKeyword uses Python identifier DoubleKeyword
    __DoubleKeyword = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DoubleKeyword'), 'DoubleKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitDoubleKeyword', True)

    
    DoubleKeyword = property(__DoubleKeyword.value, __DoubleKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}StringKeyword uses Python identifier StringKeyword
    __StringKeyword = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StringKeyword'), 'StringKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitStringKeyword', True)

    
    StringKeyword = property(__StringKeyword.value, __StringKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}LogicalKeyword uses Python identifier LogicalKeyword
    __LogicalKeyword = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LogicalKeyword'), 'LogicalKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitLogicalKeyword', True)

    
    LogicalKeyword = property(__LogicalKeyword.value, __LogicalKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}ComplexDoubleKeyword uses Python identifier ComplexDoubleKeyword
    __ComplexDoubleKeyword = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComplexDoubleKeyword'), 'ComplexDoubleKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitComplexDoubleKeyword', True)

    
    ComplexDoubleKeyword = property(__ComplexDoubleKeyword.value, __ComplexDoubleKeyword.set, None, None)

    
    # Element {http://euclid.esa.org/schema/bas/fit}UndefinedKeyword uses Python identifier UndefinedKeyword
    __UndefinedKeyword = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'UndefinedKeyword'), 'UndefinedKeyword', '__httpeuclid_esa_orgschemabasfit_headerKeywordList_httpeuclid_esa_orgschemabasfitUndefinedKeyword', True)

    
    UndefinedKeyword = property(__UndefinedKeyword.value, __UndefinedKeyword.set, None, None)


    _ElementMap = {
        __IntegerKeyword.name() : __IntegerKeyword,
        __ComplexIntegerKeyword.name() : __ComplexIntegerKeyword,
        __DoubleKeyword.name() : __DoubleKeyword,
        __StringKeyword.name() : __StringKeyword,
        __LogicalKeyword.name() : __LogicalKeyword,
        __ComplexDoubleKeyword.name() : __ComplexDoubleKeyword,
        __UndefinedKeyword.name() : __UndefinedKeyword
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'headerKeywordList', headerKeywordList)


# Complex type tableColumnList with content type ELEMENT_ONLY
class tableColumnList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'tableColumnList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}Column uses Python identifier Column
    __Column = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Column'), 'Column', '__httpeuclid_esa_orgschemabasfit_tableColumnList_httpeuclid_esa_orgschemabasfitColumn', True)

    
    Column = property(__Column.value, __Column.set, None, None)


    _ElementMap = {
        __Column.name() : __Column
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'tableColumnList', tableColumnList)


# Complex type wcsAxis with content type EMPTY
class wcsAxis (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsAxis')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_wcsAxis_name', CommonDM.bas.imp.fits_stub.wcsAxisName, required=True)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpeuclid_esa_orgschemabasfit_wcsAxis_type', CommonDM.bas.imp.fits_stub.wcsAxisType, required=True)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpeuclid_esa_orgschemabasfit_wcsAxis_unit', CommonDM.bas.utd_stub.unit, required=True)
    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Attribute projectionAlgorithm uses Python identifier projectionAlgorithm
    __projectionAlgorithm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'projectionAlgorithm'), 'projectionAlgorithm', '__httpeuclid_esa_orgschemabasfit_wcsAxis_projectionAlgorithm', CommonDM.bas.imp.fits_stub.wcsAxisProjectionAlgorithm)
    
    projectionAlgorithm = property(__projectionAlgorithm.value, __projectionAlgorithm.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name,
        __type.name() : __type,
        __unit.name() : __unit,
        __projectionAlgorithm.name() : __projectionAlgorithm
    }
Namespace.addCategoryObject('typeBinding', u'wcsAxis', wcsAxis)


# Complex type wcsAxesList with content type ELEMENT_ONLY
class wcsAxesList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsAxesList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}Axis uses Python identifier Axis
    __Axis = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Axis'), 'Axis', '__httpeuclid_esa_orgschemabasfit_wcsAxesList_httpeuclid_esa_orgschemabasfitAxis', True)

    
    Axis = property(__Axis.value, __Axis.set, None, None)


    _ElementMap = {
        __Axis.name() : __Axis
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'wcsAxesList', wcsAxesList)


# Complex type wcsType with content type ELEMENT_ONLY
class wcsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}AxesList uses Python identifier AxesList
    __AxesList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AxesList'), 'AxesList', '__httpeuclid_esa_orgschemabasfit_wcsType_httpeuclid_esa_orgschemabasfitAxesList', False)

    
    AxesList = property(__AxesList.value, __AxesList.set, None, None)

    
    # Attribute identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'identifier'), 'identifier', '__httpeuclid_esa_orgschemabasfit_wcsType_identifier', CommonDM.bas.imp.fits_stub.wcsIdentifier, required=True)
    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpeuclid_esa_orgschemabasfit_wcsType_name', CommonDM.bas.imp.fits_stub.wcsName, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __AxesList.name() : __AxesList
    }
    _AttributeMap = {
        __identifier.name() : __identifier,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'wcsType', wcsType)


# Complex type wcsList with content type ELEMENT_ONLY
class wcsList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wcsList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://euclid.esa.org/schema/bas/fit}WCS uses Python identifier WCS
    __WCS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WCS'), 'WCS', '__httpeuclid_esa_orgschemabasfit_wcsList_httpeuclid_esa_orgschemabasfitWCS', True)

    
    WCS = property(__WCS.value, __WCS.set, None, None)


    _ElementMap = {
        __WCS.name() : __WCS
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'wcsList', wcsList)


FitsFormatList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitsFormatList'), fitsFormatList, documentation=u'This element should be the root of all the XML files in the Instances/fit directory.')
Namespace.addCategoryObject('elementBinding', FitsFormatList.name().localName(), FitsFormatList)



fitsFile._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'DataContainer'), CommonDM.sys.sgs_stub.dataContainer, scope=fitsFile))
fitsFile._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fitsFile._UseForTag(pyxb.namespace.ExpandedName(None, u'DataContainer')), min_occurs=1, max_occurs=1)
    )
fitsFile._ContentModel = pyxb.binding.content.ParticleModel(fitsFile._GroupModel, min_occurs=1, max_occurs=1)



genericHdu._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HeaderKeywordList'), headerKeywordList, scope=genericHdu))
genericHdu._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(genericHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HeaderKeywordList')), min_occurs=1, max_occurs=1)
    )
genericHdu._ContentModel = pyxb.binding.content.ParticleModel(genericHdu._GroupModel, min_occurs=1, max_occurs=1)



tableHdu._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ColumnList'), tableColumnList, scope=tableHdu))
tableHdu._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(tableHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HeaderKeywordList')), min_occurs=1, max_occurs=1)
    )
tableHdu._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(tableHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ColumnList')), min_occurs=1, max_occurs=1)
    )
tableHdu._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(tableHdu._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(tableHdu._GroupModel_2, min_occurs=1, max_occurs=1)
    )
tableHdu._ContentModel = pyxb.binding.content.ParticleModel(tableHdu._GroupModel, min_occurs=1, max_occurs=1)



arrayHdu._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WCSList'), wcsList, scope=arrayHdu))

arrayHdu._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ArrayInfo'), arrayInfo, scope=arrayHdu))
arrayHdu._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(arrayHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HeaderKeywordList')), min_occurs=1, max_occurs=1)
    )
arrayHdu._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(arrayHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ArrayInfo')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(arrayHdu._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WCSList')), min_occurs=1, max_occurs=1)
    )
arrayHdu._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(arrayHdu._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(arrayHdu._GroupModel_2, min_occurs=1, max_occurs=1)
    )
arrayHdu._ContentModel = pyxb.binding.content.ParticleModel(arrayHdu._GroupModel, min_occurs=1, max_occurs=1)



hduGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ArrayHDU'), arrayHdu, scope=hduGroup))

hduGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GenericHDU'), genericHdu, scope=hduGroup))

hduGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TableHDU'), tableHdu, scope=hduGroup))
hduGroup._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(hduGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GenericHDU')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hduGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TableHDU')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(hduGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ArrayHDU')), min_occurs=1, max_occurs=1)
    )
hduGroup._ContentModel = pyxb.binding.content.ParticleModel(hduGroup._GroupModel, min_occurs=1, max_occurs=None)



fitsFormat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ArrayHDU'), arrayHdu, scope=fitsFormat))

fitsFormat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HDUGroup'), hduGroup, scope=fitsFormat))

fitsFormat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TableHDU'), tableHdu, scope=fitsFormat))

fitsFormat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GenericHDU'), genericHdu, scope=fitsFormat))
fitsFormat._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(fitsFormat._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GenericHDU')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fitsFormat._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TableHDU')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fitsFormat._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ArrayHDU')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(fitsFormat._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HDUGroup')), min_occurs=1, max_occurs=1)
    )
fitsFormat._ContentModel = pyxb.binding.content.ParticleModel(fitsFormat._GroupModel, min_occurs=1, max_occurs=None)



fitsFormatList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FitsFormat'), fitsFormat, scope=fitsFormatList))
fitsFormatList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(fitsFormatList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FitsFormat')), min_occurs=0L, max_occurs=None)
    )
fitsFormatList._ContentModel = pyxb.binding.content.ParticleModel(fitsFormatList._GroupModel, min_occurs=1, max_occurs=1)



headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IntegerKeyword'), headerIntegerKeyword, scope=headerKeywordList))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComplexIntegerKeyword'), headerComplexIntegerKeyword, scope=headerKeywordList))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DoubleKeyword'), headerDoubleKeyword, scope=headerKeywordList))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StringKeyword'), headerStringKeyword, scope=headerKeywordList))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogicalKeyword'), headerLogicalKeyword, scope=headerKeywordList))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComplexDoubleKeyword'), headerComplexDoubleKeyword, scope=headerKeywordList))

headerKeywordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UndefinedKeyword'), headerUndefinedKeyword, scope=headerKeywordList))
headerKeywordList._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UndefinedKeyword')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StringKeyword')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogicalKeyword')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IntegerKeyword')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DoubleKeyword')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComplexIntegerKeyword')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(headerKeywordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComplexDoubleKeyword')), min_occurs=1, max_occurs=1)
    )
headerKeywordList._ContentModel = pyxb.binding.content.ParticleModel(headerKeywordList._GroupModel, min_occurs=0L, max_occurs=None)



tableColumnList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Column'), binaryTableColumn, scope=tableColumnList))
tableColumnList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(tableColumnList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Column')), min_occurs=0L, max_occurs=999L)
    )
tableColumnList._ContentModel = pyxb.binding.content.ParticleModel(tableColumnList._GroupModel, min_occurs=1, max_occurs=1)



wcsAxesList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Axis'), wcsAxis, scope=wcsAxesList))
wcsAxesList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(wcsAxesList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Axis')), min_occurs=1, max_occurs=1)
    )
wcsAxesList._ContentModel = pyxb.binding.content.ParticleModel(wcsAxesList._GroupModel, min_occurs=1, max_occurs=None)



wcsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AxesList'), wcsAxesList, scope=wcsType))
wcsType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(wcsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AxesList')), min_occurs=1, max_occurs=1)
    )
wcsType._ContentModel = pyxb.binding.content.ParticleModel(wcsType._GroupModel, min_occurs=1, max_occurs=1)



wcsList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WCS'), wcsType, scope=wcsList))
wcsList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(wcsList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WCS')), min_occurs=1, max_occurs=1)
    )
wcsList._ContentModel = pyxb.binding.content.ParticleModel(wcsList._GroupModel, min_occurs=1, max_occurs=None)
