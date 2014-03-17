# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/CommonDM/dm/bas/imp/stc_stub.py
# PyXB bindings for NamespaceModule
# NSM:c85a7aef9dd35afb45dde402fdc86e2ca92a56ad
# Generated 2014-03-17 11:53:47.250106 by PyXB version 1.1.2
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
import CommonDM.dm.bas.dtd_stub
import CommonDM.dm.bas.utd_stub

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/imp/stc', create_if_missing=True)
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
class UTCDateTime (pyxb.binding.datatypes.dateTime):

    """An UTC date-time value. date-time value restricted to the
						yyyy-mm-ddThh:mm:ss(.sss) Z pattern. Z character is mandatory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCDateTime')
    _Documentation = u'An UTC date-time value. date-time value restricted to the\n\t\t\t\t\t\tyyyy-mm-ddThh:mm:ss(.sss) Z pattern. Z character is mandatory.'
UTCDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
UTCDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d(\\.\\d+)?Z')
UTCDateTime._InitializeFacetMap(UTCDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTCDateTime', UTCDateTime)

# Atomic SimpleTypeDefinition
class UTCSecDateTime (pyxb.binding.datatypes.dateTime):

    """An UTC date-time value with a precision of one second. date-time value restricted to the yyyy-mm-ddThh:mm:ssZ pattern and excluding thus :a fractional seconds definition (value has a precision of one second), a TimeZone definition. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCSecDateTime')
    _Documentation = u'An UTC date-time value with a precision of one second. date-time value restricted to the yyyy-mm-ddThh:mm:ssZ pattern and excluding thus :a fractional seconds definition (value has a precision of one second), a TimeZone definition. '
UTCSecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
UTCSecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d?Z')
UTCSecDateTime._InitializeFacetMap(UTCSecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTCSecDateTime', UTCSecDateTime)

# Atomic SimpleTypeDefinition
class secDuration (pyxb.binding.datatypes.string):

    """Duration in seconds. Accuracy is microsec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'secDuration')
    _Documentation = u'Duration in seconds. Accuracy is microsec.'
secDuration._CF_pattern = pyxb.binding.facets.CF_pattern()
secDuration._CF_pattern.addPattern(pattern=u'\\d(\\.\\d{0,6})')
secDuration._InitializeFacetMap(secDuration._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'secDuration', secDuration)

# Atomic SimpleTypeDefinition
class UTCMicrosecDateTime (pyxb.binding.datatypes.dateTime):

    """An UTC date-time value with a precision of one microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssssZ pattern"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCMicrosecDateTime')
    _Documentation = u'An UTC date-time value with a precision of one microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssssZ pattern'
UTCMicrosecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
UTCMicrosecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d.\\d\\d\\d\\d\\d\\d?Z')
UTCMicrosecDateTime._InitializeFacetMap(UTCMicrosecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTCMicrosecDateTime', UTCMicrosecDateTime)

# Atomic SimpleTypeDefinition
class referencePosition (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The list of referencePosition is derived from STC metadata Linear String Implementation V0.10. Either a "known place" such as geocenter or barycenter, or a position defined in a known coordinate system. TOPOCENTER : Location of the observer/telescope, BARYCENTER : Barycenter of the solar system HELIOCENTER : Center of the sun GEOCENTER : Center of the earth GALACTIC_CENTER : Center of the Galaxy LOCAL_GROUP_CENTER : Center of the Local Group MOON : Center of the Moon EMBARYCENTER : Barycenter of the Earth-Moon system MERCURY :  VENUS :  MARS : JUPITER : SATURN : URANUS : NEPTUNE : PLUTO : UNKNOWNRefPos : Unknown origin ; the producer is responsible for assigning a default"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'referencePosition')
    _Documentation = u'The list of referencePosition is derived from STC metadata Linear String Implementation V0.10. Either a "known place" such as geocenter or barycenter, or a position defined in a known coordinate system. TOPOCENTER : Location of the observer/telescope, BARYCENTER : Barycenter of the solar system HELIOCENTER : Center of the sun GEOCENTER : Center of the earth GALACTIC_CENTER : Center of the Galaxy LOCAL_GROUP_CENTER : Center of the Local Group MOON : Center of the Moon EMBARYCENTER : Barycenter of the Earth-Moon system MERCURY :  VENUS :  MARS : JUPITER : SATURN : URANUS : NEPTUNE : PLUTO : UNKNOWNRefPos : Unknown origin ; the producer is responsible for assigning a default'
referencePosition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=referencePosition, enum_prefix=None)
referencePosition.TOPOCENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'TOPOCENTER')
referencePosition.BARYCENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'BARYCENTER')
referencePosition.HELIOCENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'HELIOCENTER')
referencePosition.GEOCENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'GEOCENTER')
referencePosition.GALACTIC_CENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'GALACTIC_CENTER')
referencePosition.LOCAL_GROUP_CENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'LOCAL_GROUP_CENTER')
referencePosition.MOON = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'MOON')
referencePosition.EMBARYCENTER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'EMBARYCENTER')
referencePosition.MERCURY = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'MERCURY')
referencePosition.VENUS = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'VENUS')
referencePosition.MARS = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'MARS')
referencePosition.JUPITER = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'JUPITER')
referencePosition.SATURN = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'SATURN')
referencePosition.URANUS = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'URANUS')
referencePosition.NEPTUNE = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'NEPTUNE')
referencePosition.PLUTO = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'PLUTO')
referencePosition.UNKNOWNRefPos = referencePosition._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWNRefPos')
referencePosition._InitializeFacetMap(referencePosition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'referencePosition', referencePosition)

# Atomic SimpleTypeDefinition
class UTCMillisecDateTime (pyxb.binding.datatypes.dateTime):

    """An UTC date-time value with a precision of one millisecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssZ pattern"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCMillisecDateTime')
    _Documentation = u'An UTC date-time value with a precision of one millisecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssZ pattern'
UTCMillisecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
UTCMillisecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\d?Z')
UTCMillisecDateTime._InitializeFacetMap(UTCMillisecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTCMillisecDateTime', UTCMillisecDateTime)

# Atomic SimpleTypeDefinition
class coordNaxesValue (pyxb.binding.datatypes.short):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coordNaxesValue')
    _Documentation = None
coordNaxesValue._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=coordNaxesValue, value=pyxb.binding.datatypes.short(3))
coordNaxesValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=coordNaxesValue, value=pyxb.binding.datatypes.short(1))
coordNaxesValue._InitializeFacetMap(coordNaxesValue._CF_maxInclusive,
   coordNaxesValue._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'coordNaxesValue', coordNaxesValue)

# Atomic SimpleTypeDefinition
class handednessValue (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'handednessValue')
    _Documentation = None
handednessValue._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=handednessValue, enum_prefix=None)
handednessValue.left = handednessValue._CF_enumeration.addEnumeration(unicode_value=u'left')
handednessValue.right = handednessValue._CF_enumeration.addEnumeration(unicode_value=u'right')
handednessValue._InitializeFacetMap(handednessValue._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'handednessValue', handednessValue)

# Atomic SimpleTypeDefinition
class UTCTenthMicrosecDateTime (pyxb.binding.datatypes.dateTime):

    """An UTC date-time value with a precision of one tenth-of-a-microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssssssZ pattern."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCTenthMicrosecDateTime')
    _Documentation = u'An UTC date-time value with a precision of one tenth-of-a-microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssssssZ pattern.'
UTCTenthMicrosecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
UTCTenthMicrosecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\d\\d\\d\\d\\d?Z')
UTCTenthMicrosecDateTime._InitializeFacetMap(UTCTenthMicrosecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTCTenthMicrosecDateTime', UTCTenthMicrosecDateTime)

# Atomic SimpleTypeDefinition
class projection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The spherical-to-cartesian or cartesian-to-cartesian projection to be used; c-to-c projections are marked as such, all others are to be interpreted as s-to-c"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'projection')
    _Documentation = u'The spherical-to-cartesian or cartesian-to-cartesian projection to be used; c-to-c projections are marked as such, all others are to be interpreted as s-to-c'
projection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=projection, enum_prefix=None)
projection.emptyString = projection._CF_enumeration.addEnumeration(unicode_value=u'')
projection.LOG = projection._CF_enumeration.addEnumeration(unicode_value=u'LOG')
projection.TAN = projection._CF_enumeration.addEnumeration(unicode_value=u'TAN')
projection.SIN = projection._CF_enumeration.addEnumeration(unicode_value=u'SIN')
projection.STG = projection._CF_enumeration.addEnumeration(unicode_value=u'STG')
projection.ARC = projection._CF_enumeration.addEnumeration(unicode_value=u'ARC')
projection.ZEA = projection._CF_enumeration.addEnumeration(unicode_value=u'ZEA')
projection.AIR = projection._CF_enumeration.addEnumeration(unicode_value=u'AIR')
projection.CEA = projection._CF_enumeration.addEnumeration(unicode_value=u'CEA')
projection.CAR = projection._CF_enumeration.addEnumeration(unicode_value=u'CAR')
projection.MER = projection._CF_enumeration.addEnumeration(unicode_value=u'MER')
projection.SFL = projection._CF_enumeration.addEnumeration(unicode_value=u'SFL')
projection.PAR = projection._CF_enumeration.addEnumeration(unicode_value=u'PAR')
projection.MOL = projection._CF_enumeration.addEnumeration(unicode_value=u'MOL')
projection.AIT = projection._CF_enumeration.addEnumeration(unicode_value=u'AIT')
projection.COE = projection._CF_enumeration.addEnumeration(unicode_value=u'COE')
projection.COD = projection._CF_enumeration.addEnumeration(unicode_value=u'COD')
projection.COO = projection._CF_enumeration.addEnumeration(unicode_value=u'COO')
projection.BON = projection._CF_enumeration.addEnumeration(unicode_value=u'BON')
projection.PCO = projection._CF_enumeration.addEnumeration(unicode_value=u'PCO')
projection.TSC = projection._CF_enumeration.addEnumeration(unicode_value=u'TSC')
projection.CSC = projection._CF_enumeration.addEnumeration(unicode_value=u'CSC')
projection.QSC = projection._CF_enumeration.addEnumeration(unicode_value=u'QSC')
projection._InitializeFacetMap(projection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'projection', projection)

# Atomic SimpleTypeDefinition
class dateTime (pyxb.binding.datatypes.dateTime):

    """A date-time value. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss[.sss][Z] pattern and excluding thus a TimeZone definition."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dateTime')
    _Documentation = u'A date-time value. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss[.sss][Z] pattern and excluding thus a TimeZone definition.'
dateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
dateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d(\\.\\d+)?Z?')
dateTime._InitializeFacetMap(dateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'dateTime', dateTime)

# Atomic SimpleTypeDefinition
class nonUTCTenthMicrosecDateTime (pyxb.binding.datatypes.dateTime):

    """A non UTC (a TAI) date-time value with a precision of one tenth-of-a-microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssssss pattern."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nonUTCTenthMicrosecDateTime')
    _Documentation = u'A non UTC (a TAI) date-time value with a precision of one tenth-of-a-microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sssssss pattern.'
nonUTCTenthMicrosecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
nonUTCTenthMicrosecDateTime._CF_pattern.addPattern(pattern=u'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.\\d{7}')
nonUTCTenthMicrosecDateTime._InitializeFacetMap(nonUTCTenthMicrosecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'nonUTCTenthMicrosecDateTime', nonUTCTenthMicrosecDateTime)

# Atomic SimpleTypeDefinition
class hsOffsetType (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hsOffsetType')
    _Documentation = None
hsOffsetType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=hsOffsetType, value=pyxb.binding.datatypes.double(1.0))
hsOffsetType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=hsOffsetType, value=pyxb.binding.datatypes.double(-1.0))
hsOffsetType._InitializeFacetMap(hsOffsetType._CF_maxInclusive,
   hsOffsetType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'hsOffsetType', hsOffsetType)

# Atomic SimpleTypeDefinition
class timeScale (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This type refers to : timeScaleType from stc IVOA.The actual time scale is derived from Representations of Time Coordinates in FITS Time and Relative Dimension in Space (V0.93) Astronomy and Astrophysics manuscript no. WCSPaperV0.93  ESO 2012 March 21, 2012. The original XML schema is derived from stc-v1.30 IVOA. TT Terrestrial Time; the basis for ephemerides, TDT Obsolete synonym for TT ET Ephemeris Time; predecessor of, and continuous with, TT TDB Barycentric Dynamic Time:the independent variable in planetay ephemerides; time at the solar system barycenter synchronous with TT on an annual basis; sometimes called TEB Barycentric Ephemeris Time: time at the solar system barycenter synchronous with TT on an annual basis; a deprecated synonym of TDB.TCG Terrestrial Coordinate Time TAI International Atomic Time; runs 32.184 s behind TT  IAT Synonym for TAI UTC Coordinated Universal Time; currently (2006) runs 33 leapseconds behind TAI GPS Global Positioning System's time scale; runs 19 s behind TAI, 51.184 s behind TT LST Local Siderial Time; only for ground-based observations; note that the second is shorter GMST Greenwich Mean Siderial Time; only for ground-based observations; note that the second is shorter LOCAL Only to be used for simulations in conjunction with a relocatable spatial frame. The enumeration comes from paragraph 5-1 of STC-S metadata linear string implementation V0.10."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeScale')
    _Documentation = u"This type refers to : timeScaleType from stc IVOA.The actual time scale is derived from Representations of Time Coordinates in FITS Time and Relative Dimension in Space (V0.93) Astronomy and Astrophysics manuscript no. WCSPaperV0.93  ESO 2012 March 21, 2012. The original XML schema is derived from stc-v1.30 IVOA. TT Terrestrial Time; the basis for ephemerides, TDT Obsolete synonym for TT ET Ephemeris Time; predecessor of, and continuous with, TT TDB Barycentric Dynamic Time:the independent variable in planetay ephemerides; time at the solar system barycenter synchronous with TT on an annual basis; sometimes called TEB Barycentric Ephemeris Time: time at the solar system barycenter synchronous with TT on an annual basis; a deprecated synonym of TDB.TCG Terrestrial Coordinate Time TAI International Atomic Time; runs 32.184 s behind TT  IAT Synonym for TAI UTC Coordinated Universal Time; currently (2006) runs 33 leapseconds behind TAI GPS Global Positioning System's time scale; runs 19 s behind TAI, 51.184 s behind TT LST Local Siderial Time; only for ground-based observations; note that the second is shorter GMST Greenwich Mean Siderial Time; only for ground-based observations; note that the second is shorter LOCAL Only to be used for simulations in conjunction with a relocatable spatial frame. The enumeration comes from paragraph 5-1 of STC-S metadata linear string implementation V0.10."
timeScale._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=timeScale, enum_prefix=None)
timeScale.TT = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TT')
timeScale.TDT = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TDT')
timeScale.ET = timeScale._CF_enumeration.addEnumeration(unicode_value=u'ET')
timeScale.TDB = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TDB')
timeScale.TEB = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TEB')
timeScale.TCG = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TCG')
timeScale.TCB = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TCB')
timeScale.TAI = timeScale._CF_enumeration.addEnumeration(unicode_value=u'TAI')
timeScale.IAT = timeScale._CF_enumeration.addEnumeration(unicode_value=u'IAT')
timeScale.UTC = timeScale._CF_enumeration.addEnumeration(unicode_value=u'UTC')
timeScale.GPS = timeScale._CF_enumeration.addEnumeration(unicode_value=u'GPS')
timeScale.LST = timeScale._CF_enumeration.addEnumeration(unicode_value=u'LST')
timeScale.GMST = timeScale._CF_enumeration.addEnumeration(unicode_value=u'GMST')
timeScale.LOCAL = timeScale._CF_enumeration.addEnumeration(unicode_value=u'LOCAL')
timeScale._InitializeFacetMap(timeScale._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'timeScale', timeScale)

# Atomic SimpleTypeDefinition
class coordRefFrame (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The different types of CoordRefFrame come from the list in STC ivoa V1.3. Sub list defined in 'STC-S metadata linear string implementation' is described here. Take care that for ICRS type : no equinox is required, FK[45] type  needs an equinox and  geodeticType refers to IAU 1976 reference spheroid . FK4  needs a Besselian epoch,  FK5 needs a Julian epoch, ECLIPTIC Ecliptic coordinates  shall be assumed to have an equinox of J2000 with respect to ICRS (to conform with common abuse, "J2000" and "FK5" will both be interpreted as "FK5 J2000" ; "B1950" and "FK4" will be interpreted  as "FK4 B1950",  GALACTIC : Galactic coordinates; first system, GALACTIC_II : Galactic coordinates; second system, SUPER_GALACTIC : SuperGalactic coordinates, GEO_C : The Geocentric (co-rotating) reference frame, GEO_D :  The Geodetic reference frame; semi-major axis and inverse flattening may be provided to define the reference spheroid; the default is the IAU 1976 reference spheroid, UNKNOWNFrame :  Unknown space reference frame; the producer is responsible for assigning a default"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coordRefFrame')
    _Documentation = u'The different types of CoordRefFrame come from the list in STC ivoa V1.3. Sub list defined in \'STC-S metadata linear string implementation\' is described here. Take care that for ICRS type : no equinox is required, FK[45] type  needs an equinox and  geodeticType refers to IAU 1976 reference spheroid . FK4  needs a Besselian epoch,  FK5 needs a Julian epoch, ECLIPTIC Ecliptic coordinates  shall be assumed to have an equinox of J2000 with respect to ICRS (to conform with common abuse, "J2000" and "FK5" will both be interpreted as "FK5 J2000" ; "B1950" and "FK4" will be interpreted  as "FK4 B1950",  GALACTIC : Galactic coordinates; first system, GALACTIC_II : Galactic coordinates; second system, SUPER_GALACTIC : SuperGalactic coordinates, GEO_C : The Geocentric (co-rotating) reference frame, GEO_D :  The Geodetic reference frame; semi-major axis and inverse flattening may be provided to define the reference spheroid; the default is the IAU 1976 reference spheroid, UNKNOWNFrame :  Unknown space reference frame; the producer is responsible for assigning a default'
coordRefFrame._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=coordRefFrame, enum_prefix=None)
coordRefFrame.ICRS = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'ICRS')
coordRefFrame.FK4 = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'FK4')
coordRefFrame.FK5 = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'FK5')
coordRefFrame.J2000 = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'J2000')
coordRefFrame.B1950 = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'B1950')
coordRefFrame.ECLIPTIC = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'ECLIPTIC')
coordRefFrame.GALACTIC_I = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'GALACTIC_I')
coordRefFrame.GALACTIC_II = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'GALACTIC_II')
coordRefFrame.SUPER_GALACTIC = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'SUPER_GALACTIC')
coordRefFrame.GEO_C = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'GEO_C')
coordRefFrame.GEO_D = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'GEO_D')
coordRefFrame.UNKNOWNFrame = coordRefFrame._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWNFrame')
coordRefFrame._InitializeFacetMap(coordRefFrame._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'coordRefFrame', coordRefFrame)

# Atomic SimpleTypeDefinition
class dopplerDefinition (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The Doppler definition used: optical, radio, or pseudo-relativistic (i.e., how is a redshift converted to a velocity); the most common is optical, except when the reference is LSR (usually radio)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dopplerDefinition')
    _Documentation = u'The Doppler definition used: optical, radio, or pseudo-relativistic (i.e., how is a redshift converted to a velocity); the most common is optical, except when the reference is LSR (usually radio)'
dopplerDefinition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dopplerDefinition, enum_prefix=None)
dopplerDefinition.OPTICAL = dopplerDefinition._CF_enumeration.addEnumeration(unicode_value=u'OPTICAL')
dopplerDefinition.RADIO = dopplerDefinition._CF_enumeration.addEnumeration(unicode_value=u'RADIO')
dopplerDefinition.RELATIVISTIC = dopplerDefinition._CF_enumeration.addEnumeration(unicode_value=u'RELATIVISTIC')
dopplerDefinition._InitializeFacetMap(dopplerDefinition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dopplerDefinition', dopplerDefinition)

# Atomic SimpleTypeDefinition
class millisecDateTime (pyxb.binding.datatypes.dateTime):

    """A date-time value with a precision of one millisecond. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sss[Z] pattern"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'millisecDateTime')
    _Documentation = u'A date-time value with a precision of one millisecond. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.sss[Z] pattern'
millisecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
millisecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\dZ?')
millisecDateTime._InitializeFacetMap(millisecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'millisecDateTime', millisecDateTime)

# Atomic SimpleTypeDefinition
class secDateTime (pyxb.binding.datatypes.dateTime):

    """A date-time value with a precision of one second. This date-time format allows the definition of TAI date and UTC date. date-time value is restricted to the yyyy-mm-ddThh:mm:ss[Z] pattern and excluding thus : a fractional seconds definition (value has a precision of one second), a TimeZone definition."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'secDateTime')
    _Documentation = u'A date-time value with a precision of one second. This date-time format allows the definition of TAI date and UTC date. date-time value is restricted to the yyyy-mm-ddThh:mm:ss[Z] pattern and excluding thus : a fractional seconds definition (value has a precision of one second), a TimeZone definition.'
secDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
secDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ?')
secDateTime._InitializeFacetMap(secDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'secDateTime', secDateTime)

# Atomic SimpleTypeDefinition
class TAIMillisecsecDateTime (pyxb.binding.datatypes.dateTime):

    """An non UTC date-time value with a precision of one millisecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss pattern"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TAIMillisecsecDateTime')
    _Documentation = u'An non UTC date-time value with a precision of one millisecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss pattern'
TAIMillisecsecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
TAIMillisecsecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\d')
TAIMillisecsecDateTime._InitializeFacetMap(TAIMillisecsecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'TAIMillisecsecDateTime', TAIMillisecsecDateTime)

# Atomic SimpleTypeDefinition
class TAIMicrosecDateTime (pyxb.binding.datatypes.dateTime):

    """An non UTC date-time value with a precision of one microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss pattern"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TAIMicrosecDateTime')
    _Documentation = u'An non UTC date-time value with a precision of one microsecond. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss pattern'
TAIMicrosecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
TAIMicrosecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\d\\d\\d\\d')
TAIMicrosecDateTime._InitializeFacetMap(TAIMicrosecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'TAIMicrosecDateTime', TAIMicrosecDateTime)

# Atomic SimpleTypeDefinition
class microsecDateTime (pyxb.binding.datatypes.dateTime):

    """A date-time value with a precision of one microsecond. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss[Z] pattern."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'microsecDateTime')
    _Documentation = u'A date-time value with a precision of one microsecond. This date-time format allows the definition of TAI date and UTC date. Date-time value restricted to the yyyy-mm-ddThh:mm:ss.ssssss[Z] pattern.'
microsecDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
microsecDateTime._CF_pattern.addPattern(pattern=u'\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d\\d\\d\\d\\d\\dZ?')
microsecDateTime._InitializeFacetMap(microsecDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'microsecDateTime', microsecDateTime)

# Atomic SimpleTypeDefinition
class redshiftFrameValue (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'redshiftFrameValue')
    _Documentation = None
redshiftFrameValue._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=redshiftFrameValue, enum_prefix=None)
redshiftFrameValue.VELOCITY = redshiftFrameValue._CF_enumeration.addEnumeration(unicode_value=u'VELOCITY')
redshiftFrameValue.REDSHIFT = redshiftFrameValue._CF_enumeration.addEnumeration(unicode_value=u'REDSHIFT')
redshiftFrameValue._InitializeFacetMap(redshiftFrameValue._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'redshiftFrameValue', redshiftFrameValue)

# Complex type UTCSecDateTimeRange with content type ELEMENT_ONLY
class UTCSecDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCSecDateTimeRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_UTCSecDateTimeRange_end', False)

    
    end = property(__end.value, __end.set, None, None)

    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_UTCSecDateTimeRange_start', False)

    
    start = property(__start.value, __start.set, None, None)


    _ElementMap = {
        __end.name() : __end,
        __start.name() : __start
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'UTCSecDateTimeRange', UTCSecDateTimeRange)


# Complex type UTCTenthMicrosecDateTimeRange with content type ELEMENT_ONLY
class UTCTenthMicrosecDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCTenthMicrosecDateTimeRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_UTCTenthMicrosecDateTimeRange_end', False)

    
    end = property(__end.value, __end.set, None, None)

    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_UTCTenthMicrosecDateTimeRange_start', False)

    
    start = property(__start.value, __start.set, None, None)


    _ElementMap = {
        __end.name() : __end,
        __start.name() : __start
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'UTCTenthMicrosecDateTimeRange', UTCTenthMicrosecDateTimeRange)


# Complex type coordScalarIntervalType with content type ELEMENT_ONLY
class coordScalarIntervalType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coordScalarIntervalType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LoLimit uses Python identifier LoLimit
    __LoLimit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'LoLimit'), 'LoLimit', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_LoLimit', False)

    
    LoLimit = property(__LoLimit.value, __LoLimit.set, None, u'Lower bound of interval.')

    
    # Element HiLimit uses Python identifier HiLimit
    __HiLimit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'HiLimit'), 'HiLimit', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_HiLimit', False)

    
    HiLimit = property(__HiLimit.value, __HiLimit.set, None, u'Upper bound of interval.')

    
    # Attribute hi_include uses Python identifier hi_include
    __hi_include = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hi_include'), 'hi_include', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_hi_include', pyxb.binding.datatypes.boolean, unicode_default=u'true')
    
    hi_include = property(__hi_include.value, __hi_include.set, None, u'Limit to be included, if true hi limit is included.')

    
    # Attribute FrameId uses Python identifier FrameId
    __FrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'FrameId'), 'FrameId', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_FrameId', pyxb.binding.datatypes.string)
    
    FrameId = property(__FrameId.value, __FrameId.set, None, None)

    
    # Attribute fill_factor uses Python identifier fill_factor
    __fill_factor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fill_factor'), 'fill_factor', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_fill_factor', pyxb.binding.datatypes.float, unicode_default=u'1.0')
    
    fill_factor = property(__fill_factor.value, __fill_factor.set, None, u'Fraction of interval that is occupied by data.')

    
    # Attribute lo_include uses Python identifier lo_include
    __lo_include = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lo_include'), 'lo_include', '__httpeuclid_esa_orgschemabasimpstc_coordScalarIntervalType_lo_include', pyxb.binding.datatypes.boolean, unicode_default=u'true')
    
    lo_include = property(__lo_include.value, __lo_include.set, None, u'Limit to be included, if true lo limit is included.')


    _ElementMap = {
        __LoLimit.name() : __LoLimit,
        __HiLimit.name() : __HiLimit
    }
    _AttributeMap = {
        __hi_include.name() : __hi_include,
        __FrameId.name() : __FrameId,
        __fill_factor.name() : __fill_factor,
        __lo_include.name() : __lo_include
    }
Namespace.addCategoryObject('typeBinding', u'coordScalarIntervalType', coordScalarIntervalType)


# Complex type timeIntervalType with content type ELEMENT_ONLY
class timeIntervalType (coordScalarIntervalType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeIntervalType')
    # Base type is coordScalarIntervalType
    
    # Element StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'StartTime'), 'StartTime', '__httpeuclid_esa_orgschemabasimpstc_timeIntervalType_StartTime', False)

    
    StartTime = property(__StartTime.value, __StartTime.set, None, u'astronTime may be expressed in ISO8601 or as a double relative to a reference time')

    
    # Element StopTime uses Python identifier StopTime
    __StopTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'StopTime'), 'StopTime', '__httpeuclid_esa_orgschemabasimpstc_timeIntervalType_StopTime', False)

    
    StopTime = property(__StopTime.value, __StopTime.set, None, u'astronTime may be expressed in ISO8601 or as a double relative to a reference time')

    
    # Element HiLimit (HiLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Element LoLimit (LoLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute hi_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute FrameId inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute fill_factor inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute lo_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType

    _ElementMap = coordScalarIntervalType._ElementMap.copy()
    _ElementMap.update({
        __StartTime.name() : __StartTime,
        __StopTime.name() : __StopTime
    })
    _AttributeMap = coordScalarIntervalType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'timeIntervalType', timeIntervalType)


# Complex type astronTimeType with content type ELEMENT_ONLY
class astronTimeType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'astronTimeType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element AbsoluteTime uses Python identifier AbsoluteTime
    __AbsoluteTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AbsoluteTime'), 'AbsoluteTime', '__httpeuclid_esa_orgschemabasimpstc_astronTimeType_AbsoluteTime', False)

    
    AbsoluteTime = property(__AbsoluteTime.value, __AbsoluteTime.set, None, None)

    
    # Element Timescale uses Python identifier Timescale
    __Timescale = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Timescale'), 'Timescale', '__httpeuclid_esa_orgschemabasimpstc_astronTimeType_Timescale', False)

    
    Timescale = property(__Timescale.value, __Timescale.set, None, None)

    
    # Element TimeOffset uses Python identifier TimeOffset
    __TimeOffset = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'TimeOffset'), 'TimeOffset', '__httpeuclid_esa_orgschemabasimpstc_astronTimeType_TimeOffset', False)

    
    TimeOffset = property(__TimeOffset.value, __TimeOffset.set, None, None)


    _ElementMap = {
        __AbsoluteTime.name() : __AbsoluteTime,
        __Timescale.name() : __Timescale,
        __TimeOffset.name() : __TimeOffset
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'astronTimeType', astronTimeType)


# Complex type UTCMillisecDateTimeRange with content type ELEMENT_ONLY
class UTCMillisecDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCMillisecDateTimeRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_UTCMillisecDateTimeRange_end', False)

    
    end = property(__end.value, __end.set, None, None)

    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_UTCMillisecDateTimeRange_start', False)

    
    start = property(__start.value, __start.set, None, None)


    _ElementMap = {
        __end.name() : __end,
        __start.name() : __start
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'UTCMillisecDateTimeRange', UTCMillisecDateTimeRange)


# Complex type coordFlavorType with content type EMPTY
class coordFlavorType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coordFlavorType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute coord_naxes uses Python identifier coord_naxes
    __coord_naxes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'coord_naxes'), 'coord_naxes', '__httpeuclid_esa_orgschemabasimpstc_coordFlavorType_coord_naxes', coordNaxesValue, unicode_default=u'2')
    
    coord_naxes = property(__coord_naxes.value, __coord_naxes.set, None, None)

    
    # Attribute handedness uses Python identifier handedness
    __handedness = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'handedness'), 'handedness', '__httpeuclid_esa_orgschemabasimpstc_coordFlavorType_handedness', handednessValue)
    
    handedness = property(__handedness.value, __handedness.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __coord_naxes.name() : __coord_naxes,
        __handedness.name() : __handedness
    }
Namespace.addCategoryObject('typeBinding', u'coordFlavorType', coordFlavorType)


# Complex type basicCoordinateType with content type ELEMENT_ONLY
class basicCoordinateType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'basicCoordinateType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_Name', False)

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Resolution uses Python identifier Resolution
    __Resolution = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Resolution'), 'Resolution', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_Resolution', True)

    
    Resolution = property(__Resolution.value, __Resolution.set, None, None)

    
    # Element Size uses Python identifier Size
    __Size = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Size'), 'Size', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_Size', True)

    
    Size = property(__Size.value, __Size.set, None, None)

    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element PixSize uses Python identifier PixSize
    __PixSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'PixSize'), 'PixSize', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_PixSize', True)

    
    PixSize = property(__PixSize.value, __PixSize.set, None, None)

    
    # Element Error uses Python identifier Error
    __Error = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Error'), 'Error', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_Error', True)

    
    Error = property(__Error.value, __Error.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_basicCoordinateType_CoordUnit', CommonDM.dm.bas.utd_stub.unit)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)


    _ElementMap = {
        __Name.name() : __Name,
        __Resolution.name() : __Resolution,
        __Size.name() : __Size,
        __Value.name() : __Value,
        __PixSize.name() : __PixSize,
        __Error.name() : __Error
    }
    _AttributeMap = {
        __CoordUnit.name() : __CoordUnit
    }
Namespace.addCategoryObject('typeBinding', u'basicCoordinateType', basicCoordinateType)


# Complex type coord3VecIntervalType with content type ELEMENT_ONLY
class coord3VecIntervalType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coord3VecIntervalType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element HiLimit3Vec uses Python identifier HiLimit3Vec
    __HiLimit3Vec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'HiLimit3Vec'), 'HiLimit3Vec', '__httpeuclid_esa_orgschemabasimpstc_coord3VecIntervalType_HiLimit3Vec', False)

    
    HiLimit3Vec = property(__HiLimit3Vec.value, __HiLimit3Vec.set, None, None)

    
    # Element LoLimit3Vec uses Python identifier LoLimit3Vec
    __LoLimit3Vec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'LoLimit3Vec'), 'LoLimit3Vec', '__httpeuclid_esa_orgschemabasimpstc_coord3VecIntervalType_LoLimit3Vec', False)

    
    LoLimit3Vec = property(__LoLimit3Vec.value, __LoLimit3Vec.set, None, None)

    
    # Attribute fill_factor uses Python identifier fill_factor
    __fill_factor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fill_factor'), 'fill_factor', '__httpeuclid_esa_orgschemabasimpstc_coord3VecIntervalType_fill_factor', pyxb.binding.datatypes.float, unicode_default=u'1.0')
    
    fill_factor = property(__fill_factor.value, __fill_factor.set, None, u'Fraction of interval that is occupied by data')

    
    # Attribute FrameId uses Python identifier FrameId
    __FrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'FrameId'), 'FrameId', '__httpeuclid_esa_orgschemabasimpstc_coord3VecIntervalType_FrameId', pyxb.binding.datatypes.string)
    
    FrameId = property(__FrameId.value, __FrameId.set, None, None)


    _ElementMap = {
        __HiLimit3Vec.name() : __HiLimit3Vec,
        __LoLimit3Vec.name() : __LoLimit3Vec
    }
    _AttributeMap = {
        __fill_factor.name() : __fill_factor,
        __FrameId.name() : __FrameId
    }
Namespace.addCategoryObject('typeBinding', u'coord3VecIntervalType', coord3VecIntervalType)


# Complex type spectralIntervalType with content type ELEMENT_ONLY
class spectralIntervalType (coordScalarIntervalType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectralIntervalType')
    # Base type is coordScalarIntervalType
    
    # Element LoLimit (LoLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Element HiLimit (HiLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute hi_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute FrameId inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute SpectralUnit uses Python identifier SpectralUnit
    __SpectralUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SpectralUnit'), 'SpectralUnit', '__httpeuclid_esa_orgschemabasimpstc_spectralIntervalType_SpectralUnit', CommonDM.dm.bas.utd_stub.unit, required=True)
    
    SpectralUnit = property(__SpectralUnit.value, __SpectralUnit.set, None, None)

    
    # Attribute lo_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute fill_factor inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType

    _ElementMap = coordScalarIntervalType._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = coordScalarIntervalType._AttributeMap.copy()
    _AttributeMap.update({
        __SpectralUnit.name() : __SpectralUnit
    })
Namespace.addCategoryObject('typeBinding', u'spectralIntervalType', spectralIntervalType)


# Complex type halfspaceType with content type ELEMENT_ONLY
class halfspaceType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'halfspaceType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Vector uses Python identifier Vector
    __Vector = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Vector'), 'Vector', '__httpeuclid_esa_orgschemabasimpstc_halfspaceType_Vector', False)

    
    Vector = property(__Vector.value, __Vector.set, None, u'This needs to be a spherical coordinate vector; it is the unit vector that is normal to the plane that forms a constraint for a convex')

    
    # Element Offset uses Python identifier Offset
    __Offset = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Offset'), 'Offset', '__httpeuclid_esa_orgschemabasimpstc_halfspaceType_Offset', False)

    
    Offset = property(__Offset.value, __Offset.set, None, u'The distance along the normal vector where the constraint plane intersects that vector; if positive, the spherical sector on the far side (seen from the center) is selected; if negative, the point of intersection is in the opposite direction of the vector, resulting in more than a hemisphere; the valid range is -1.0 to +1.0')


    _ElementMap = {
        __Vector.name() : __Vector,
        __Offset.name() : __Offset
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'halfspaceType', halfspaceType)


# Complex type redshiftIntervalType with content type ELEMENT_ONLY
class redshiftIntervalType (coordScalarIntervalType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'redshiftIntervalType')
    # Base type is coordScalarIntervalType
    
    # Element LoLimit (LoLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Element HiLimit (HiLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute hi_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_redshiftIntervalType_CoordUnit', CommonDM.dm.bas.utd_stub.unit, required=True)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)

    
    # Attribute RedshiftUnit uses Python identifier RedshiftUnit
    __RedshiftUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'RedshiftUnit'), 'RedshiftUnit', '__httpeuclid_esa_orgschemabasimpstc_redshiftIntervalType_RedshiftUnit', CommonDM.dm.bas.utd_stub.unit, required=True)
    
    RedshiftUnit = property(__RedshiftUnit.value, __RedshiftUnit.set, None, None)

    
    # Attribute fill_factor inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute lo_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute FrameId inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType

    _ElementMap = coordScalarIntervalType._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = coordScalarIntervalType._AttributeMap.copy()
    _AttributeMap.update({
        __CoordUnit.name() : __CoordUnit,
        __RedshiftUnit.name() : __RedshiftUnit
    })
Namespace.addCategoryObject('typeBinding', u'redshiftIntervalType', redshiftIntervalType)


# Complex type allSkyType with content type EMPTY
class allSkyType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'allSkyType')
    # Base type is pyxb.binding.datatypes.anyType

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'allSkyType', allSkyType)


# Complex type TAIMillisecsecDateTimeRange with content type ELEMENT_ONLY
class TAIMillisecsecDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TAIMillisecsecDateTimeRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_TAIMillisecsecDateTimeRange_end', False)

    
    end = property(__end.value, __end.set, None, None)

    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_TAIMillisecsecDateTimeRange_start', False)

    
    start = property(__start.value, __start.set, None, None)


    _ElementMap = {
        __end.name() : __end,
        __start.name() : __start
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'TAIMillisecsecDateTimeRange', TAIMillisecsecDateTimeRange)


# Complex type regionType with content type ELEMENT_ONLY
class regionType (coordScalarIntervalType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'regionType')
    # Base type is coordScalarIntervalType
    
    # Element LoLimit (LoLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Element Area uses Python identifier Area
    __Area = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Area'), 'Area', '__httpeuclid_esa_orgschemabasimpstc_regionType_Area', False)

    
    Area = property(__Area.value, __Area.set, None, None)

    
    # Element HiLimit (HiLimit) inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute hi_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute fill_factor inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute lo_include inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute FrameId inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordScalarIntervalType
    
    # Attribute astroCoordSystem uses Python identifier astroCoordSystem
    __astroCoordSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'astroCoordSystem'), 'astroCoordSystem', '__httpeuclid_esa_orgschemabasimpstc_regionType_astroCoordSystem', pyxb.binding.datatypes.string)
    
    astroCoordSystem = property(__astroCoordSystem.value, __astroCoordSystem.set, None, None)

    
    # Attribute note uses Python identifier note
    __note = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'note'), 'note', '__httpeuclid_esa_orgschemabasimpstc_regionType_note', pyxb.binding.datatypes.string)
    
    note = property(__note.value, __note.set, None, None)


    _ElementMap = coordScalarIntervalType._ElementMap.copy()
    _ElementMap.update({
        __Area.name() : __Area
    })
    _AttributeMap = coordScalarIntervalType._AttributeMap.copy()
    _AttributeMap.update({
        __astroCoordSystem.name() : __astroCoordSystem,
        __note.name() : __note
    })
Namespace.addCategoryObject('typeBinding', u'regionType', regionType)


# Complex type timeCoordinateType with content type ELEMENT_ONLY
class timeCoordinateType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeCoordinateType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Resolution uses Python identifier Resolution
    __Resolution = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Resolution'), 'Resolution', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_Resolution', True)

    
    Resolution = property(__Resolution.value, __Resolution.set, None, None)

    
    # Element TimeInstant uses Python identifier TimeInstant
    __TimeInstant = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'TimeInstant'), 'TimeInstant', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_TimeInstant', False)

    
    TimeInstant = property(__TimeInstant.value, __TimeInstant.set, None, None)

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_Name', False)

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element PixSize uses Python identifier PixSize
    __PixSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'PixSize'), 'PixSize', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_PixSize', True)

    
    PixSize = property(__PixSize.value, __PixSize.set, None, None)

    
    # Element Size uses Python identifier Size
    __Size = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Size'), 'Size', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_Size', True)

    
    Size = property(__Size.value, __Size.set, None, None)

    
    # Element Error uses Python identifier Error
    __Error = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Error'), 'Error', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_Error', True)

    
    Error = property(__Error.value, __Error.set, None, None)

    
    # Attribute TimeUnit uses Python identifier TimeUnit
    __TimeUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'TimeUnit'), 'TimeUnit', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_TimeUnit', CommonDM.dm.bas.utd_stub.unit)
    
    TimeUnit = property(__TimeUnit.value, __TimeUnit.set, None, None)

    
    # Attribute AstroCoordSystemId uses Python identifier AstroCoordSystemId
    __AstroCoordSystemId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'AstroCoordSystemId'), 'AstroCoordSystemId', '__httpeuclid_esa_orgschemabasimpstc_timeCoordinateType_AstroCoordSystemId', pyxb.binding.datatypes.string)
    
    AstroCoordSystemId = property(__AstroCoordSystemId.value, __AstroCoordSystemId.set, None, None)


    _ElementMap = {
        __Resolution.name() : __Resolution,
        __TimeInstant.name() : __TimeInstant,
        __Name.name() : __Name,
        __PixSize.name() : __PixSize,
        __Size.name() : __Size,
        __Error.name() : __Error
    }
    _AttributeMap = {
        __TimeUnit.name() : __TimeUnit,
        __AstroCoordSystemId.name() : __AstroCoordSystemId
    }
Namespace.addCategoryObject('typeBinding', u'timeCoordinateType', timeCoordinateType)


# Complex type coord2VecIntervalType with content type ELEMENT_ONLY
class coord2VecIntervalType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'coord2VecIntervalType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element HiLimit2Vec uses Python identifier HiLimit2Vec
    __HiLimit2Vec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'HiLimit2Vec'), 'HiLimit2Vec', '__httpeuclid_esa_orgschemabasimpstc_coord2VecIntervalType_HiLimit2Vec', False)

    
    HiLimit2Vec = property(__HiLimit2Vec.value, __HiLimit2Vec.set, None, None)

    
    # Element LoLimit2Vec uses Python identifier LoLimit2Vec
    __LoLimit2Vec = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'LoLimit2Vec'), 'LoLimit2Vec', '__httpeuclid_esa_orgschemabasimpstc_coord2VecIntervalType_LoLimit2Vec', False)

    
    LoLimit2Vec = property(__LoLimit2Vec.value, __LoLimit2Vec.set, None, None)

    
    # Attribute FrameId uses Python identifier FrameId
    __FrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'FrameId'), 'FrameId', '__httpeuclid_esa_orgschemabasimpstc_coord2VecIntervalType_FrameId', pyxb.binding.datatypes.string)
    
    FrameId = property(__FrameId.value, __FrameId.set, None, None)

    
    # Attribute fill_factor uses Python identifier fill_factor
    __fill_factor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fill_factor'), 'fill_factor', '__httpeuclid_esa_orgschemabasimpstc_coord2VecIntervalType_fill_factor', pyxb.binding.datatypes.float, unicode_default=u'1.0')
    
    fill_factor = property(__fill_factor.value, __fill_factor.set, None, u'Fraction of interval that is occupied by data')


    _ElementMap = {
        __HiLimit2Vec.name() : __HiLimit2Vec,
        __LoLimit2Vec.name() : __LoLimit2Vec
    }
    _AttributeMap = {
        __FrameId.name() : __FrameId,
        __fill_factor.name() : __fill_factor
    }
Namespace.addCategoryObject('typeBinding', u'coord2VecIntervalType', coord2VecIntervalType)


# Complex type convexType with content type ELEMENT_ONLY
class convexType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'convexType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Halfspace uses Python identifier Halfspace
    __Halfspace = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Halfspace'), 'Halfspace', '__httpeuclid_esa_orgschemabasimpstc_convexType_Halfspace', True)

    
    Halfspace = property(__Halfspace.value, __Halfspace.set, None, None)


    _ElementMap = {
        __Halfspace.name() : __Halfspace
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'convexType', convexType)


# Complex type unionType with content type ELEMENT_ONLY
class unionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unionType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Region uses Python identifier Region
    __Region = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Region'), 'Region', '__httpeuclid_esa_orgschemabasimpstc_unionType_Region', True)

    
    Region = property(__Region.value, __Region.set, None, None)


    _ElementMap = {
        __Region.name() : __Region
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'unionType', unionType)


# Complex type intersectionType with content type ELEMENT_ONLY
class intersectionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'intersectionType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Region uses Python identifier Region
    __Region = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Region'), 'Region', '__httpeuclid_esa_orgschemabasimpstc_intersectionType_Region', True)

    
    Region = property(__Region.value, __Region.set, None, None)


    _ElementMap = {
        __Region.name() : __Region
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'intersectionType', intersectionType)


# Complex type negationType with content type ELEMENT_ONLY
class negationType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'negationType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Region uses Python identifier Region
    __Region = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Region'), 'Region', '__httpeuclid_esa_orgschemabasimpstc_negationType_Region', False)

    
    Region = property(__Region.value, __Region.set, None, None)


    _ElementMap = {
        __Region.name() : __Region
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'negationType', negationType)


# Complex type diffType with content type ELEMENT_ONLY
class diffType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'diffType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Region2 uses Python identifier Region2
    __Region2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Region2'), 'Region2', '__httpeuclid_esa_orgschemabasimpstc_diffType_Region2', False)

    
    Region2 = property(__Region2.value, __Region2.set, None, None)

    
    # Element Region uses Python identifier Region
    __Region = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Region'), 'Region', '__httpeuclid_esa_orgschemabasimpstc_diffType_Region', False)

    
    Region = property(__Region.value, __Region.set, None, None)


    _ElementMap = {
        __Region2.name() : __Region2,
        __Region.name() : __Region
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'diffType', diffType)


# Complex type spaceFrame with content type ELEMENT_ONLY
class spaceFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spaceFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_spaceFrame_Name', False)

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element ReferencePosition uses Python identifier ReferencePosition
    __ReferencePosition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), 'ReferencePosition', '__httpeuclid_esa_orgschemabasimpstc_spaceFrame_ReferencePosition', False)

    
    ReferencePosition = property(__ReferencePosition.value, __ReferencePosition.set, None, None)

    
    # Element CoordFlavor uses Python identifier CoordFlavor
    __CoordFlavor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CoordFlavor'), 'CoordFlavor', '__httpeuclid_esa_orgschemabasimpstc_spaceFrame_CoordFlavor', False)

    
    CoordFlavor = property(__CoordFlavor.value, __CoordFlavor.set, None, None)

    
    # Element SpaceRefFrame uses Python identifier SpaceRefFrame
    __SpaceRefFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SpaceRefFrame'), 'SpaceRefFrame', '__httpeuclid_esa_orgschemabasimpstc_spaceFrame_SpaceRefFrame', False)

    
    SpaceRefFrame = property(__SpaceRefFrame.value, __SpaceRefFrame.set, None, None)

    
    # Attribute SpaceFrameId uses Python identifier SpaceFrameId
    __SpaceFrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SpaceFrameId'), 'SpaceFrameId', '__httpeuclid_esa_orgschemabasimpstc_spaceFrame_SpaceFrameId', pyxb.binding.datatypes.string)
    
    SpaceFrameId = property(__SpaceFrameId.value, __SpaceFrameId.set, None, None)


    _ElementMap = {
        __Name.name() : __Name,
        __ReferencePosition.name() : __ReferencePosition,
        __CoordFlavor.name() : __CoordFlavor,
        __SpaceRefFrame.name() : __SpaceRefFrame
    }
    _AttributeMap = {
        __SpaceFrameId.name() : __SpaceFrameId
    }
Namespace.addCategoryObject('typeBinding', u'spaceFrame', spaceFrame)


# Complex type redshiftFrame with content type ELEMENT_ONLY
class redshiftFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'redshiftFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_redshiftFrame_Name', False)

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasimpstc_redshiftFrame_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element ReferencePosition uses Python identifier ReferencePosition
    __ReferencePosition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), 'ReferencePosition', '__httpeuclid_esa_orgschemabasimpstc_redshiftFrame_ReferencePosition', False)

    
    ReferencePosition = property(__ReferencePosition.value, __ReferencePosition.set, None, None)

    
    # Element DopplerDefinition uses Python identifier DopplerDefinition
    __DopplerDefinition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'DopplerDefinition'), 'DopplerDefinition', '__httpeuclid_esa_orgschemabasimpstc_redshiftFrame_DopplerDefinition', False)

    
    DopplerDefinition = property(__DopplerDefinition.value, __DopplerDefinition.set, None, None)

    
    # Attribute RedshiftFrameId uses Python identifier RedshiftFrameId
    __RedshiftFrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'RedshiftFrameId'), 'RedshiftFrameId', '__httpeuclid_esa_orgschemabasimpstc_redshiftFrame_RedshiftFrameId', pyxb.binding.datatypes.string)
    
    RedshiftFrameId = property(__RedshiftFrameId.value, __RedshiftFrameId.set, None, None)


    _ElementMap = {
        __Name.name() : __Name,
        __Value.name() : __Value,
        __ReferencePosition.name() : __ReferencePosition,
        __DopplerDefinition.name() : __DopplerDefinition
    }
    _AttributeMap = {
        __RedshiftFrameId.name() : __RedshiftFrameId
    }
Namespace.addCategoryObject('typeBinding', u'redshiftFrame', redshiftFrame)


# Complex type spectralFrame with content type ELEMENT_ONLY
class spectralFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spectralFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ReferencePosition uses Python identifier ReferencePosition
    __ReferencePosition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), 'ReferencePosition', '__httpeuclid_esa_orgschemabasimpstc_spectralFrame_ReferencePosition', False)

    
    ReferencePosition = property(__ReferencePosition.value, __ReferencePosition.set, None, None)

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_spectralFrame_Name', False)

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute SpectralFrameId uses Python identifier SpectralFrameId
    __SpectralFrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SpectralFrameId'), 'SpectralFrameId', '__httpeuclid_esa_orgschemabasimpstc_spectralFrame_SpectralFrameId', pyxb.binding.datatypes.string)
    
    SpectralFrameId = property(__SpectralFrameId.value, __SpectralFrameId.set, None, None)


    _ElementMap = {
        __ReferencePosition.name() : __ReferencePosition,
        __Name.name() : __Name
    }
    _AttributeMap = {
        __SpectralFrameId.name() : __SpectralFrameId
    }
Namespace.addCategoryObject('typeBinding', u'spectralFrame', spectralFrame)


# Complex type spatialCoordDefType with content type ELEMENT_ONLY
class spatialCoordDefType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'spatialCoordDefType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element STRING uses Python identifier STRING
    __STRING = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'STRING'), 'STRING', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_STRING', False)

    
    STRING = property(__STRING.value, __STRING.set, None, None)

    
    # Element UNITSPHERE uses Python identifier UNITSPHERE
    __UNITSPHERE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'UNITSPHERE'), 'UNITSPHERE', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_UNITSPHERE', False)

    
    UNITSPHERE = property(__UNITSPHERE.value, __UNITSPHERE.set, None, None)

    
    # Element HEALPIX uses Python identifier HEALPIX
    __HEALPIX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'HEALPIX'), 'HEALPIX', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_HEALPIX', False)

    
    HEALPIX = property(__HEALPIX.value, __HEALPIX.set, None, None)

    
    # Element POLAR uses Python identifier POLAR
    __POLAR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'POLAR'), 'POLAR', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_POLAR', False)

    
    POLAR = property(__POLAR.value, __POLAR.set, None, None)

    
    # Element SPHERICAL uses Python identifier SPHERICAL
    __SPHERICAL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SPHERICAL'), 'SPHERICAL', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_SPHERICAL', False)

    
    SPHERICAL = property(__SPHERICAL.value, __SPHERICAL.set, None, None)

    
    # Element CYLINDRICAL uses Python identifier CYLINDRICAL
    __CYLINDRICAL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CYLINDRICAL'), 'CYLINDRICAL', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_CYLINDRICAL', False)

    
    CYLINDRICAL = property(__CYLINDRICAL.value, __CYLINDRICAL.set, None, None)

    
    # Element CARTESIAN uses Python identifier CARTESIAN
    __CARTESIAN = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CARTESIAN'), 'CARTESIAN', '__httpeuclid_esa_orgschemabasimpstc_spatialCoordDefType_CARTESIAN', False)

    
    CARTESIAN = property(__CARTESIAN.value, __CARTESIAN.set, None, None)


    _ElementMap = {
        __STRING.name() : __STRING,
        __UNITSPHERE.name() : __UNITSPHERE,
        __HEALPIX.name() : __HEALPIX,
        __POLAR.name() : __POLAR,
        __SPHERICAL.name() : __SPHERICAL,
        __CYLINDRICAL.name() : __CYLINDRICAL,
        __CARTESIAN.name() : __CARTESIAN
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'spatialCoordDefType', spatialCoordDefType)


# Complex type ellipseType with content type ELEMENT_ONLY
class ellipseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ellipseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Center uses Python identifier Center
    __Center = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Center'), 'Center', '__httpeuclid_esa_orgschemabasimpstc_ellipseType_Center', False)

    
    Center = property(__Center.value, __Center.set, None, u"The coordinates of the circle's center")

    
    # Element SemiMinorAxis uses Python identifier SemiMinorAxis
    __SemiMinorAxis = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SemiMinorAxis'), 'SemiMinorAxis', '__httpeuclid_esa_orgschemabasimpstc_ellipseType_SemiMinorAxis', False)

    
    SemiMinorAxis = property(__SemiMinorAxis.value, __SemiMinorAxis.set, None, u'Half the minor axis of the ellipse, in radius_unit')

    
    # Element SemiMajorAxis uses Python identifier SemiMajorAxis
    __SemiMajorAxis = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SemiMajorAxis'), 'SemiMajorAxis', '__httpeuclid_esa_orgschemabasimpstc_ellipseType_SemiMajorAxis', False)

    
    SemiMajorAxis = property(__SemiMajorAxis.value, __SemiMajorAxis.set, None, u'The radius of the circle')

    
    # Element PosAngle uses Python identifier PosAngle
    __PosAngle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'PosAngle'), 'PosAngle', '__httpeuclid_esa_orgschemabasimpstc_ellipseType_PosAngle', False)

    
    PosAngle = property(__PosAngle.value, __PosAngle.set, None, u'Position angle of major axis (Radius).')


    _ElementMap = {
        __Center.name() : __Center,
        __SemiMinorAxis.name() : __SemiMinorAxis,
        __SemiMajorAxis.name() : __SemiMajorAxis,
        __PosAngle.name() : __PosAngle
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ellipseType', ellipseType)


# Complex type pixelVector1CoordinateType with content type ELEMENT_ONLY
class pixelVector1CoordinateType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pixelVector1CoordinateType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__httpeuclid_esa_orgschemabasimpstc_pixelVector1CoordinateType_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_pixelVector1CoordinateType_Name', False)

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_pixelVector1CoordinateType_CoordUnit', CommonDM.dm.bas.utd_stub.unit)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)


    _ElementMap = {
        __Value.name() : __Value,
        __Name.name() : __Name
    }
    _AttributeMap = {
        __CoordUnit.name() : __CoordUnit
    }
Namespace.addCategoryObject('typeBinding', u'pixelVector1CoordinateType', pixelVector1CoordinateType)


# Complex type vector2CoordinateType with content type ELEMENT_ONLY
class vector2CoordinateType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'vector2CoordinateType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Value2 uses Python identifier Value2
    __Value2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value2'), 'Value2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Value2', False)

    
    Value2 = property(__Value2.value, __Value2.set, None, None)

    
    # Element PixSize2 uses Python identifier PixSize2
    __PixSize2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'PixSize2'), 'PixSize2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_PixSize2', True)

    
    PixSize2 = property(__PixSize2.value, __PixSize2.set, None, None)

    
    # Element Error2 uses Python identifier Error2
    __Error2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Error2'), 'Error2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Error2', True)

    
    Error2 = property(__Error2.value, __Error2.set, None, None)

    
    # Element Resolution2 uses Python identifier Resolution2
    __Resolution2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Resolution2'), 'Resolution2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Resolution2', True)

    
    Resolution2 = property(__Resolution2.value, __Resolution2.set, None, None)

    
    # Element Name2 uses Python identifier Name2
    __Name2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name2'), 'Name2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Name2', False)

    
    Name2 = property(__Name2.value, __Name2.set, None, None)

    
    # Element Size2 uses Python identifier Size2
    __Size2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Size2'), 'Size2', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Size2', True)

    
    Size2 = property(__Size2.value, __Size2.set, None, None)

    
    # Element Name1 uses Python identifier Name1
    __Name1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name1'), 'Name1', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_Name1', False)

    
    Name1 = property(__Name1.value, __Name1.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_vector2CoordinateType_CoordUnit', CommonDM.dm.bas.utd_stub.unit)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)


    _ElementMap = {
        __Value2.name() : __Value2,
        __PixSize2.name() : __PixSize2,
        __Error2.name() : __Error2,
        __Resolution2.name() : __Resolution2,
        __Name2.name() : __Name2,
        __Size2.name() : __Size2,
        __Name1.name() : __Name1
    }
    _AttributeMap = {
        __CoordUnit.name() : __CoordUnit
    }
Namespace.addCategoryObject('typeBinding', u'vector2CoordinateType', vector2CoordinateType)


# Complex type astroCoordSystem with content type ELEMENT_ONLY
class astroCoordSystem (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'astroCoordSystem')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RedshiftFrame uses Python identifier RedshiftFrame
    __RedshiftFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'RedshiftFrame'), 'RedshiftFrame', '__httpeuclid_esa_orgschemabasimpstc_astroCoordSystem_RedshiftFrame', False)

    
    RedshiftFrame = property(__RedshiftFrame.value, __RedshiftFrame.set, None, None)

    
    # Element SpaceFrame uses Python identifier SpaceFrame
    __SpaceFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SpaceFrame'), 'SpaceFrame', '__httpeuclid_esa_orgschemabasimpstc_astroCoordSystem_SpaceFrame', False)

    
    SpaceFrame = property(__SpaceFrame.value, __SpaceFrame.set, None, None)

    
    # Element TimeFrame uses Python identifier TimeFrame
    __TimeFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'TimeFrame'), 'TimeFrame', '__httpeuclid_esa_orgschemabasimpstc_astroCoordSystem_TimeFrame', False)

    
    TimeFrame = property(__TimeFrame.value, __TimeFrame.set, None, None)

    
    # Element SpectralFrame uses Python identifier SpectralFrame
    __SpectralFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SpectralFrame'), 'SpectralFrame', '__httpeuclid_esa_orgschemabasimpstc_astroCoordSystem_SpectralFrame', False)

    
    SpectralFrame = property(__SpectralFrame.value, __SpectralFrame.set, None, None)

    
    # Attribute AstroCoordSystemId uses Python identifier AstroCoordSystemId
    __AstroCoordSystemId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'AstroCoordSystemId'), 'AstroCoordSystemId', '__httpeuclid_esa_orgschemabasimpstc_astroCoordSystem_AstroCoordSystemId', pyxb.binding.datatypes.string, required=True)
    
    AstroCoordSystemId = property(__AstroCoordSystemId.value, __AstroCoordSystemId.set, None, None)


    _ElementMap = {
        __RedshiftFrame.name() : __RedshiftFrame,
        __SpaceFrame.name() : __SpaceFrame,
        __TimeFrame.name() : __TimeFrame,
        __SpectralFrame.name() : __SpectralFrame
    }
    _AttributeMap = {
        __AstroCoordSystemId.name() : __AstroCoordSystemId
    }
Namespace.addCategoryObject('typeBinding', u'astroCoordSystem', astroCoordSystem)


# Complex type smallCircleType with content type ELEMENT_ONLY
class smallCircleType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'smallCircleType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Pole uses Python identifier Pole
    __Pole = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Pole'), 'Pole', '__httpeuclid_esa_orgschemabasimpstc_smallCircleType_Pole', False)

    
    Pole = property(__Pole.value, __Pole.set, None, None)


    _ElementMap = {
        __Pole.name() : __Pole
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'smallCircleType', smallCircleType)


# Complex type pixelVector2CoordinateType with content type ELEMENT_ONLY
class pixelVector2CoordinateType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pixelVector2CoordinateType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Value2 uses Python identifier Value2
    __Value2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value2'), 'Value2', '__httpeuclid_esa_orgschemabasimpstc_pixelVector2CoordinateType_Value2', False)

    
    Value2 = property(__Value2.value, __Value2.set, None, None)

    
    # Element Name1 uses Python identifier Name1
    __Name1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name1'), 'Name1', '__httpeuclid_esa_orgschemabasimpstc_pixelVector2CoordinateType_Name1', False)

    
    Name1 = property(__Name1.value, __Name1.set, None, None)

    
    # Element Name2 uses Python identifier Name2
    __Name2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name2'), 'Name2', '__httpeuclid_esa_orgschemabasimpstc_pixelVector2CoordinateType_Name2', False)

    
    Name2 = property(__Name2.value, __Name2.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_pixelVector2CoordinateType_CoordUnit', CommonDM.dm.bas.utd_stub.unit)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)


    _ElementMap = {
        __Value2.name() : __Value2,
        __Name1.name() : __Name1,
        __Name2.name() : __Name2
    }
    _AttributeMap = {
        __CoordUnit.name() : __CoordUnit
    }
Namespace.addCategoryObject('typeBinding', u'pixelVector2CoordinateType', pixelVector2CoordinateType)


# Complex type polygonType with content type ELEMENT_ONLY
class polygonType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'polygonType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Vertex uses Python identifier Vertex
    __Vertex = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Vertex'), 'Vertex', '__httpeuclid_esa_orgschemabasimpstc_polygonType_Vertex', True)

    
    Vertex = property(__Vertex.value, __Vertex.set, None, u'In order to form polygons, vertices are to be connected with straight line segments. In the case of spherical coordinates: greatcircle segments; if a smallCircle element si present, the vertex and its predecessor are to be connected with a smallcircle, by default in the CoordSys that is referenced; optionally, a pole may be specified (other than the CoordSys pole) that defines the smallcircle system')


    _ElementMap = {
        __Vertex.name() : __Vertex
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'polygonType', polygonType)


# Complex type vertexType with content type ELEMENT_ONLY
class vertexType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'vertexType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SmallCircle uses Python identifier SmallCircle
    __SmallCircle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'SmallCircle'), 'SmallCircle', '__httpeuclid_esa_orgschemabasimpstc_vertexType_SmallCircle', False)

    
    SmallCircle = property(__SmallCircle.value, __SmallCircle.set, None, None)

    
    # Element Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Position'), 'Position', '__httpeuclid_esa_orgschemabasimpstc_vertexType_Position', False)

    
    Position = property(__Position.value, __Position.set, None, None)


    _ElementMap = {
        __SmallCircle.name() : __SmallCircle,
        __Position.name() : __Position
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'vertexType', vertexType)


# Complex type boxType with content type ELEMENT_ONLY
class boxType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'boxType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Size uses Python identifier Size
    __Size = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Size'), 'Size', '__httpeuclid_esa_orgschemabasimpstc_boxType_Size', False)

    
    Size = property(__Size.value, __Size.set, None, u"The lengths of the box's sides")

    
    # Element Center uses Python identifier Center
    __Center = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Center'), 'Center', '__httpeuclid_esa_orgschemabasimpstc_boxType_Center', False)

    
    Center = property(__Center.value, __Center.set, None, u"The coordinates of the box's center")


    _ElementMap = {
        __Size.name() : __Size,
        __Center.name() : __Center
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'boxType', boxType)


# Complex type UTCMicrosecDateTimeRange with content type ELEMENT_ONLY
class UTCMicrosecDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCMicrosecDateTimeRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_UTCMicrosecDateTimeRange_end', False)

    
    end = property(__end.value, __end.set, None, None)

    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_UTCMicrosecDateTimeRange_start', False)

    
    start = property(__start.value, __start.set, None, None)


    _ElementMap = {
        __end.name() : __end,
        __start.name() : __start
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'UTCMicrosecDateTimeRange', UTCMicrosecDateTimeRange)


# Complex type healpixType with content type EMPTY
class healpixType (coordFlavorType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'healpixType')
    # Base type is coordFlavorType
    
    # Attribute coord_naxes inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordFlavorType
    
    # Attribute handedness inherited from {http://euclid.esa.org/schema/bas/imp/stc}coordFlavorType
    
    # Attribute healpix_H uses Python identifier healpix_H
    __healpix_H = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'healpix_H'), 'healpix_H', '__httpeuclid_esa_orgschemabasimpstc_healpixType_healpix_H', pyxb.binding.datatypes.short, unicode_default=u'4')
    
    healpix_H = property(__healpix_H.value, __healpix_H.set, None, None)

    
    # Attribute healpix_K uses Python identifier healpix_K
    __healpix_K = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'healpix_K'), 'healpix_K', '__httpeuclid_esa_orgschemabasimpstc_healpixType_healpix_K', pyxb.binding.datatypes.short, unicode_default=u'3')
    
    healpix_K = property(__healpix_K.value, __healpix_K.set, None, None)


    _ElementMap = coordFlavorType._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = coordFlavorType._AttributeMap.copy()
    _AttributeMap.update({
        __healpix_H.name() : __healpix_H,
        __healpix_K.name() : __healpix_K
    })
Namespace.addCategoryObject('typeBinding', u'healpixType', healpixType)


# Complex type JDTime with content type SIMPLE
class JDTime (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'JDTime')
    # Base type is pyxb.binding.datatypes.decimal

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'JDTime', JDTime)


# Complex type sectorType with content type ELEMENT_ONLY
class sectorType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sectorType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PosAngle1 uses Python identifier PosAngle1
    __PosAngle1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'PosAngle1'), 'PosAngle1', '__httpeuclid_esa_orgschemabasimpstc_sectorType_PosAngle1', False)

    
    PosAngle1 = property(__PosAngle1.value, __PosAngle1.set, None, u'The area cw from this position angle is included')

    
    # Element PosAngle2 uses Python identifier PosAngle2
    __PosAngle2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'PosAngle2'), 'PosAngle2', '__httpeuclid_esa_orgschemabasimpstc_sectorType_PosAngle2', False)

    
    PosAngle2 = property(__PosAngle2.value, __PosAngle2.set, None, u'The area cw from this position angle is included.')

    
    # Element Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Position'), 'Position', '__httpeuclid_esa_orgschemabasimpstc_sectorType_Position', False)

    
    Position = property(__Position.value, __Position.set, None, u'The vertex position of the sector')


    _ElementMap = {
        __PosAngle1.name() : __PosAngle1,
        __PosAngle2.name() : __PosAngle2,
        __Position.name() : __Position
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'sectorType', sectorType)


# Complex type MJDTime with content type SIMPLE
class MJDTime (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MJDTime')
    # Base type is pyxb.binding.datatypes.decimal

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'MJDTime', MJDTime)


# Complex type timeOffset with content type SIMPLE
class timeOffset (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeOffset')
    # Base type is pyxb.binding.datatypes.decimal

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'timeOffset', timeOffset)


# Complex type isoTime with content type SIMPLE
class isoTime (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.dateTime
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'isoTime')
    # Base type is pyxb.binding.datatypes.dateTime

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'isoTime', isoTime)


# Complex type UTCDateTimeRange with content type ELEMENT_ONLY
class UTCDateTimeRange (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTCDateTimeRange')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'end'), 'end', '__httpeuclid_esa_orgschemabasimpstc_UTCDateTimeRange_end', False)

    
    end = property(__end.value, __end.set, None, None)

    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpeuclid_esa_orgschemabasimpstc_UTCDateTimeRange_start', False)

    
    start = property(__start.value, __start.set, None, None)


    _ElementMap = {
        __end.name() : __end,
        __start.name() : __start
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'UTCDateTimeRange', UTCDateTimeRange)


# Complex type regionAreaType with content type SIMPLE
class regionAreaType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'regionAreaType')
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute validArea uses Python identifier validArea
    __validArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'validArea'), 'validArea', '__httpeuclid_esa_orgschemabasimpstc_regionAreaType_validArea', pyxb.binding.datatypes.boolean, required=True)
    
    validArea = property(__validArea.value, __validArea.set, None, None)

    
    # Attribute linearAreaUnit uses Python identifier linearAreaUnit
    __linearAreaUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'linearAreaUnit'), 'linearAreaUnit', '__httpeuclid_esa_orgschemabasimpstc_regionAreaType_linearAreaUnit', CommonDM.dm.bas.utd_stub.unit, required=True)
    
    linearAreaUnit = property(__linearAreaUnit.value, __linearAreaUnit.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __validArea.name() : __validArea,
        __linearAreaUnit.name() : __linearAreaUnit
    }
Namespace.addCategoryObject('typeBinding', u'regionAreaType', regionAreaType)


# Complex type circleType with content type ELEMENT_ONLY
class circleType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'circleType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Radius uses Python identifier Radius
    __Radius = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Radius'), 'Radius', '__httpeuclid_esa_orgschemabasimpstc_circleType_Radius', False)

    
    Radius = property(__Radius.value, __Radius.set, None, u'The radius of the circle')

    
    # Element Center uses Python identifier Center
    __Center = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Center'), 'Center', '__httpeuclid_esa_orgschemabasimpstc_circleType_Center', False)

    
    Center = property(__Center.value, __Center.set, None, u"The coordinates of the circle's center")


    _ElementMap = {
        __Radius.name() : __Radius,
        __Center.name() : __Center
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'circleType', circleType)


# Complex type vector3CoordinateType with content type ELEMENT_ONLY
class vector3CoordinateType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'vector3CoordinateType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name3 uses Python identifier Name3
    __Name3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name3'), 'Name3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Name3', False)

    
    Name3 = property(__Name3.value, __Name3.set, None, None)

    
    # Element Value3 uses Python identifier Value3
    __Value3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value3'), 'Value3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Value3', False)

    
    Value3 = property(__Value3.value, __Value3.set, None, None)

    
    # Element PixSize3 uses Python identifier PixSize3
    __PixSize3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'PixSize3'), 'PixSize3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_PixSize3', True)

    
    PixSize3 = property(__PixSize3.value, __PixSize3.set, None, None)

    
    # Element Name1 uses Python identifier Name1
    __Name1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name1'), 'Name1', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Name1', False)

    
    Name1 = property(__Name1.value, __Name1.set, None, None)

    
    # Element Size3 uses Python identifier Size3
    __Size3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Size3'), 'Size3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Size3', True)

    
    Size3 = property(__Size3.value, __Size3.set, None, None)

    
    # Element Name2 uses Python identifier Name2
    __Name2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name2'), 'Name2', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Name2', False)

    
    Name2 = property(__Name2.value, __Name2.set, None, None)

    
    # Element Resolution3 uses Python identifier Resolution3
    __Resolution3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Resolution3'), 'Resolution3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Resolution3', True)

    
    Resolution3 = property(__Resolution3.value, __Resolution3.set, None, None)

    
    # Element Error3 uses Python identifier Error3
    __Error3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Error3'), 'Error3', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_Error3', True)

    
    Error3 = property(__Error3.value, __Error3.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_vector3CoordinateType_CoordUnit', CommonDM.dm.bas.utd_stub.unit)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)


    _ElementMap = {
        __Name3.name() : __Name3,
        __Value3.name() : __Value3,
        __PixSize3.name() : __PixSize3,
        __Name1.name() : __Name1,
        __Size3.name() : __Size3,
        __Name2.name() : __Name2,
        __Resolution3.name() : __Resolution3,
        __Error3.name() : __Error3
    }
    _AttributeMap = {
        __CoordUnit.name() : __CoordUnit
    }
Namespace.addCategoryObject('typeBinding', u'vector3CoordinateType', vector3CoordinateType)


# Complex type pixelVector3CoordinateType with content type ELEMENT_ONLY
class pixelVector3CoordinateType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pixelVector3CoordinateType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name1 uses Python identifier Name1
    __Name1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name1'), 'Name1', '__httpeuclid_esa_orgschemabasimpstc_pixelVector3CoordinateType_Name1', False)

    
    Name1 = property(__Name1.value, __Name1.set, None, None)

    
    # Element Value3 uses Python identifier Value3
    __Value3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value3'), 'Value3', '__httpeuclid_esa_orgschemabasimpstc_pixelVector3CoordinateType_Value3', False)

    
    Value3 = property(__Value3.value, __Value3.set, None, None)

    
    # Element Name3 uses Python identifier Name3
    __Name3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name3'), 'Name3', '__httpeuclid_esa_orgschemabasimpstc_pixelVector3CoordinateType_Name3', False)

    
    Name3 = property(__Name3.value, __Name3.set, None, None)

    
    # Element Name2 uses Python identifier Name2
    __Name2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name2'), 'Name2', '__httpeuclid_esa_orgschemabasimpstc_pixelVector3CoordinateType_Name2', False)

    
    Name2 = property(__Name2.value, __Name2.set, None, None)

    
    # Attribute CoordUnit uses Python identifier CoordUnit
    __CoordUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CoordUnit'), 'CoordUnit', '__httpeuclid_esa_orgschemabasimpstc_pixelVector3CoordinateType_CoordUnit', CommonDM.dm.bas.utd_stub.unit)
    
    CoordUnit = property(__CoordUnit.value, __CoordUnit.set, None, None)


    _ElementMap = {
        __Name1.name() : __Name1,
        __Value3.name() : __Value3,
        __Name3.name() : __Name3,
        __Name2.name() : __Name2
    }
    _AttributeMap = {
        __CoordUnit.name() : __CoordUnit
    }
Namespace.addCategoryObject('typeBinding', u'pixelVector3CoordinateType', pixelVector3CoordinateType)


# Complex type timeFrame with content type ELEMENT_ONLY
class timeFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpeuclid_esa_orgschemabasimpstc_timeFrame_Name', False)

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element ReferencePosition uses Python identifier ReferencePosition
    __ReferencePosition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), 'ReferencePosition', '__httpeuclid_esa_orgschemabasimpstc_timeFrame_ReferencePosition', False)

    
    ReferencePosition = property(__ReferencePosition.value, __ReferencePosition.set, None, None)

    
    # Element TimeScale uses Python identifier TimeScale
    __TimeScale = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'TimeScale'), 'TimeScale', '__httpeuclid_esa_orgschemabasimpstc_timeFrame_TimeScale', False)

    
    TimeScale = property(__TimeScale.value, __TimeScale.set, None, None)

    
    # Attribute TimeFrameId uses Python identifier TimeFrameId
    __TimeFrameId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'TimeFrameId'), 'TimeFrameId', '__httpeuclid_esa_orgschemabasimpstc_timeFrame_TimeFrameId', pyxb.binding.datatypes.string)
    
    TimeFrameId = property(__TimeFrameId.value, __TimeFrameId.set, None, None)


    _ElementMap = {
        __Name.name() : __Name,
        __ReferencePosition.name() : __ReferencePosition,
        __TimeScale.name() : __TimeScale
    }
    _AttributeMap = {
        __TimeFrameId.name() : __TimeFrameId
    }
Namespace.addCategoryObject('typeBinding', u'timeFrame', timeFrame)




UTCSecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), UTCSecDateTime, scope=UTCSecDateTimeRange))

UTCSecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), UTCSecDateTime, scope=UTCSecDateTimeRange))
UTCSecDateTimeRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(UTCSecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(UTCSecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), min_occurs=1, max_occurs=1)
    )
UTCSecDateTimeRange._ContentModel = pyxb.binding.content.ParticleModel(UTCSecDateTimeRange._GroupModel, min_occurs=1, max_occurs=1)



UTCTenthMicrosecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), UTCTenthMicrosecDateTime, scope=UTCTenthMicrosecDateTimeRange))

UTCTenthMicrosecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), UTCTenthMicrosecDateTime, scope=UTCTenthMicrosecDateTimeRange))
UTCTenthMicrosecDateTimeRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(UTCTenthMicrosecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(UTCTenthMicrosecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), min_occurs=1, max_occurs=1)
    )
UTCTenthMicrosecDateTimeRange._ContentModel = pyxb.binding.content.ParticleModel(UTCTenthMicrosecDateTimeRange._GroupModel, min_occurs=1, max_occurs=1)



coordScalarIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LoLimit'), CommonDM.dm.bas.dtd_stub.double1Type, scope=coordScalarIntervalType, documentation=u'Lower bound of interval.'))

coordScalarIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'HiLimit'), CommonDM.dm.bas.dtd_stub.double1Type, scope=coordScalarIntervalType, documentation=u'Upper bound of interval.'))
coordScalarIntervalType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coordScalarIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(coordScalarIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit')), min_occurs=0L, max_occurs=1)
    )
coordScalarIntervalType._ContentModel = pyxb.binding.content.ParticleModel(coordScalarIntervalType._GroupModel, min_occurs=1, max_occurs=1)



timeIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'StartTime'), astronTimeType, nillable=pyxb.binding.datatypes.boolean(1), scope=timeIntervalType, documentation=u'astronTime may be expressed in ISO8601 or as a double relative to a reference time'))

timeIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'StopTime'), astronTimeType, nillable=pyxb.binding.datatypes.boolean(1), scope=timeIntervalType, documentation=u'astronTime may be expressed in ISO8601 or as a double relative to a reference time'))
timeIntervalType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(timeIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(timeIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit')), min_occurs=0L, max_occurs=1)
    )
timeIntervalType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(timeIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'StartTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(timeIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'StopTime')), min_occurs=1, max_occurs=1)
    )
timeIntervalType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(timeIntervalType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(timeIntervalType._GroupModel_2, min_occurs=1, max_occurs=1)
    )
timeIntervalType._ContentModel = pyxb.binding.content.ParticleModel(timeIntervalType._GroupModel, min_occurs=1, max_occurs=1)



astronTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AbsoluteTime'), isoTime, scope=astronTimeType))

astronTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Timescale'), timeScale, scope=astronTimeType))

astronTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TimeOffset'), timeOffset, scope=astronTimeType))
astronTimeType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astronTimeType._UseForTag(pyxb.namespace.ExpandedName(None, u'Timescale')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(astronTimeType._UseForTag(pyxb.namespace.ExpandedName(None, u'TimeOffset')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(astronTimeType._UseForTag(pyxb.namespace.ExpandedName(None, u'AbsoluteTime')), min_occurs=1, max_occurs=1)
    )
astronTimeType._ContentModel = pyxb.binding.content.ParticleModel(astronTimeType._GroupModel, min_occurs=1, max_occurs=1)



UTCMillisecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), UTCMillisecDateTime, scope=UTCMillisecDateTimeRange))

UTCMillisecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), UTCMillisecDateTime, scope=UTCMillisecDateTimeRange))
UTCMillisecDateTimeRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(UTCMillisecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(UTCMillisecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), min_occurs=1, max_occurs=1)
    )
UTCMillisecDateTimeRange._ContentModel = pyxb.binding.content.ParticleModel(UTCMillisecDateTimeRange._GroupModel, min_occurs=1, max_occurs=1)



basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=basicCoordinateType))

basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Resolution'), CommonDM.dm.bas.dtd_stub.double1Type, scope=basicCoordinateType))

basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Size'), CommonDM.dm.bas.dtd_stub.double1Type, scope=basicCoordinateType))

basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), CommonDM.dm.bas.dtd_stub.double1Type, scope=basicCoordinateType))

basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PixSize'), CommonDM.dm.bas.dtd_stub.double1Type, scope=basicCoordinateType))

basicCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Error'), CommonDM.dm.bas.dtd_stub.double1Type, scope=basicCoordinateType))
basicCoordinateType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Error')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Resolution')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Size')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(basicCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'PixSize')), min_occurs=0L, max_occurs=2L)
    )
basicCoordinateType._ContentModel = pyxb.binding.content.ParticleModel(basicCoordinateType._GroupModel, min_occurs=1, max_occurs=1)



coord3VecIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'HiLimit3Vec'), CommonDM.dm.bas.dtd_stub.double3Type, scope=coord3VecIntervalType))

coord3VecIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LoLimit3Vec'), CommonDM.dm.bas.dtd_stub.double3Type, scope=coord3VecIntervalType))
coord3VecIntervalType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coord3VecIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit3Vec')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(coord3VecIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit3Vec')), min_occurs=0L, max_occurs=1)
    )
coord3VecIntervalType._ContentModel = pyxb.binding.content.ParticleModel(coord3VecIntervalType._GroupModel, min_occurs=1, max_occurs=1)


spectralIntervalType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectralIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectralIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit')), min_occurs=0L, max_occurs=1)
    )
spectralIntervalType._ContentModel = pyxb.binding.content.ParticleModel(spectralIntervalType._GroupModel, min_occurs=1, max_occurs=1)



halfspaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Vector'), CommonDM.dm.bas.dtd_stub.double3Type, scope=halfspaceType, documentation=u'This needs to be a spherical coordinate vector; it is the unit vector that is normal to the plane that forms a constraint for a convex'))

halfspaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Offset'), hsOffsetType, scope=halfspaceType, documentation=u'The distance along the normal vector where the constraint plane intersects that vector; if positive, the spherical sector on the far side (seen from the center) is selected; if negative, the point of intersection is in the opposite direction of the vector, resulting in more than a hemisphere; the valid range is -1.0 to +1.0'))
halfspaceType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(halfspaceType._UseForTag(pyxb.namespace.ExpandedName(None, u'Vector')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(halfspaceType._UseForTag(pyxb.namespace.ExpandedName(None, u'Offset')), min_occurs=1, max_occurs=1)
    )
halfspaceType._ContentModel = pyxb.binding.content.ParticleModel(halfspaceType._GroupModel, min_occurs=1, max_occurs=1)


redshiftIntervalType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(redshiftIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(redshiftIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit')), min_occurs=0L, max_occurs=1)
    )
redshiftIntervalType._ContentModel = pyxb.binding.content.ParticleModel(redshiftIntervalType._GroupModel, min_occurs=1, max_occurs=1)



TAIMillisecsecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), TAIMillisecsecDateTime, scope=TAIMillisecsecDateTimeRange))

TAIMillisecsecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), TAIMillisecsecDateTime, scope=TAIMillisecsecDateTimeRange))
TAIMillisecsecDateTimeRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(TAIMillisecsecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TAIMillisecsecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), min_occurs=1, max_occurs=1)
    )
TAIMillisecsecDateTimeRange._ContentModel = pyxb.binding.content.ParticleModel(TAIMillisecsecDateTimeRange._GroupModel, min_occurs=1, max_occurs=1)



regionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Area'), regionAreaType, scope=regionType))
regionType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regionType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(regionType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit')), min_occurs=0L, max_occurs=1)
    )
regionType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Area')), min_occurs=0L, max_occurs=1)
    )
regionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(regionType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(regionType._GroupModel_2, min_occurs=1, max_occurs=1)
    )
regionType._ContentModel = pyxb.binding.content.ParticleModel(regionType._GroupModel, min_occurs=1, max_occurs=1)



timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Resolution'), CommonDM.dm.bas.dtd_stub.double1Type, scope=timeCoordinateType))

timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TimeInstant'), astronTimeType, scope=timeCoordinateType))

timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=timeCoordinateType))

timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PixSize'), CommonDM.dm.bas.dtd_stub.double1Type, scope=timeCoordinateType))

timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Size'), CommonDM.dm.bas.dtd_stub.double1Type, scope=timeCoordinateType))

timeCoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Error'), CommonDM.dm.bas.dtd_stub.double1Type, scope=timeCoordinateType))
timeCoordinateType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'TimeInstant')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Error')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Resolution')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Size')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(timeCoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'PixSize')), min_occurs=0L, max_occurs=2L)
    )
timeCoordinateType._ContentModel = pyxb.binding.content.ParticleModel(timeCoordinateType._GroupModel, min_occurs=1, max_occurs=1)



coord2VecIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'HiLimit2Vec'), CommonDM.dm.bas.dtd_stub.double2Type, scope=coord2VecIntervalType))

coord2VecIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LoLimit2Vec'), CommonDM.dm.bas.dtd_stub.double2Type, scope=coord2VecIntervalType))
coord2VecIntervalType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(coord2VecIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'LoLimit2Vec')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(coord2VecIntervalType._UseForTag(pyxb.namespace.ExpandedName(None, u'HiLimit2Vec')), min_occurs=0L, max_occurs=1)
    )
coord2VecIntervalType._ContentModel = pyxb.binding.content.ParticleModel(coord2VecIntervalType._GroupModel, min_occurs=1, max_occurs=1)



convexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Halfspace'), halfspaceType, scope=convexType))
convexType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(convexType._UseForTag(pyxb.namespace.ExpandedName(None, u'Halfspace')), min_occurs=1, max_occurs=100L)
    )
convexType._ContentModel = pyxb.binding.content.ParticleModel(convexType._GroupModel, min_occurs=1, max_occurs=1)



unionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Region'), regionType, scope=unionType))
unionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(unionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Region')), min_occurs=2L, max_occurs=100L)
    )
unionType._ContentModel = pyxb.binding.content.ParticleModel(unionType._GroupModel, min_occurs=1, max_occurs=1)



intersectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Region'), regionType, scope=intersectionType))
intersectionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(intersectionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Region')), min_occurs=2L, max_occurs=100L)
    )
intersectionType._ContentModel = pyxb.binding.content.ParticleModel(intersectionType._GroupModel, min_occurs=1, max_occurs=1)



negationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Region'), regionType, scope=negationType))
negationType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(negationType._UseForTag(pyxb.namespace.ExpandedName(None, u'Region')), min_occurs=1, max_occurs=1)
    )
negationType._ContentModel = pyxb.binding.content.ParticleModel(negationType._GroupModel, min_occurs=1, max_occurs=1)



diffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Region2'), regionType, scope=diffType))

diffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Region'), regionType, scope=diffType))
diffType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(diffType._UseForTag(pyxb.namespace.ExpandedName(None, u'Region')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(diffType._UseForTag(pyxb.namespace.ExpandedName(None, u'Region2')), min_occurs=1, max_occurs=1)
    )
diffType._ContentModel = pyxb.binding.content.ParticleModel(diffType._GroupModel, min_occurs=1, max_occurs=1)



spaceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=spaceFrame))

spaceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), referencePosition, scope=spaceFrame))

spaceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CoordFlavor'), coordFlavorType, scope=spaceFrame))

spaceFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SpaceRefFrame'), coordRefFrame, scope=spaceFrame))
spaceFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spaceFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spaceFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'SpaceRefFrame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spaceFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'ReferencePosition')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spaceFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'CoordFlavor')), min_occurs=1, max_occurs=1)
    )
spaceFrame._ContentModel = pyxb.binding.content.ParticleModel(spaceFrame._GroupModel, min_occurs=1, max_occurs=1)



redshiftFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=redshiftFrame))

redshiftFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), redshiftFrameValue, scope=redshiftFrame))

redshiftFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), referencePosition, scope=redshiftFrame))

redshiftFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'DopplerDefinition'), dopplerDefinition, scope=redshiftFrame))
redshiftFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(redshiftFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(redshiftFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(redshiftFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'DopplerDefinition')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(redshiftFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'ReferencePosition')), min_occurs=1, max_occurs=1)
    )
redshiftFrame._ContentModel = pyxb.binding.content.ParticleModel(redshiftFrame._GroupModel, min_occurs=1, max_occurs=1)



spectralFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), referencePosition, scope=spectralFrame))

spectralFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=spectralFrame))
spectralFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(spectralFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spectralFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'ReferencePosition')), min_occurs=1, max_occurs=1)
    )
spectralFrame._ContentModel = pyxb.binding.content.ParticleModel(spectralFrame._GroupModel, min_occurs=1, max_occurs=1)



spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'STRING'), coordFlavorType, scope=spatialCoordDefType))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'UNITSPHERE'), coordFlavorType, scope=spatialCoordDefType))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'HEALPIX'), healpixType, scope=spatialCoordDefType))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'POLAR'), coordFlavorType, scope=spatialCoordDefType))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SPHERICAL'), coordFlavorType, scope=spatialCoordDefType))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CYLINDRICAL'), coordFlavorType, scope=spatialCoordDefType))

spatialCoordDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CARTESIAN'), coordFlavorType, scope=spatialCoordDefType))
spatialCoordDefType._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'SPHERICAL')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'CARTESIAN')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'UNITSPHERE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'POLAR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'CYLINDRICAL')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'STRING')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(spatialCoordDefType._UseForTag(pyxb.namespace.ExpandedName(None, u'HEALPIX')), min_occurs=1, max_occurs=1)
    )
spatialCoordDefType._ContentModel = pyxb.binding.content.ParticleModel(spatialCoordDefType._GroupModel, min_occurs=1, max_occurs=1)



ellipseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Center'), CommonDM.dm.bas.dtd_stub.double2Type, scope=ellipseType, documentation=u"The coordinates of the circle's center"))

ellipseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SemiMinorAxis'), CommonDM.dm.bas.dtd_stub.double1Type, scope=ellipseType, documentation=u'Half the minor axis of the ellipse, in radius_unit'))

ellipseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SemiMajorAxis'), CommonDM.dm.bas.dtd_stub.double1Type, scope=ellipseType, documentation=u'The radius of the circle'))

ellipseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PosAngle'), CommonDM.dm.bas.dtd_stub.double1Type, scope=ellipseType, documentation=u'Position angle of major axis (Radius).'))
ellipseType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ellipseType._UseForTag(pyxb.namespace.ExpandedName(None, u'Center')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ellipseType._UseForTag(pyxb.namespace.ExpandedName(None, u'SemiMajorAxis')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ellipseType._UseForTag(pyxb.namespace.ExpandedName(None, u'SemiMinorAxis')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ellipseType._UseForTag(pyxb.namespace.ExpandedName(None, u'PosAngle')), min_occurs=1, max_occurs=1)
    )
ellipseType._ContentModel = pyxb.binding.content.ParticleModel(ellipseType._GroupModel, min_occurs=1, max_occurs=1)



pixelVector1CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), CommonDM.dm.bas.dtd_stub.double1Type, scope=pixelVector1CoordinateType))

pixelVector1CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=pixelVector1CoordinateType))
pixelVector1CoordinateType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelVector1CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelVector1CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=0L, max_occurs=1)
    )
pixelVector1CoordinateType._ContentModel = pyxb.binding.content.ParticleModel(pixelVector1CoordinateType._GroupModel, min_occurs=1, max_occurs=1)



vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value2'), CommonDM.dm.bas.dtd_stub.double2Type, scope=vector2CoordinateType))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PixSize2'), CommonDM.dm.bas.dtd_stub.double2Type, scope=vector2CoordinateType))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Error2'), CommonDM.dm.bas.dtd_stub.double2Type, scope=vector2CoordinateType))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Resolution2'), CommonDM.dm.bas.dtd_stub.double2Type, scope=vector2CoordinateType))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name2'), pyxb.binding.datatypes.string, scope=vector2CoordinateType))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Size2'), CommonDM.dm.bas.dtd_stub.double2Type, scope=vector2CoordinateType))

vector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name1'), pyxb.binding.datatypes.string, scope=vector2CoordinateType))
vector2CoordinateType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Error2')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Resolution2')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Size2')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(vector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'PixSize2')), min_occurs=0L, max_occurs=2L)
    )
vector2CoordinateType._ContentModel = pyxb.binding.content.ParticleModel(vector2CoordinateType._GroupModel, min_occurs=1, max_occurs=1)



astroCoordSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'RedshiftFrame'), redshiftFrame, scope=astroCoordSystem))

astroCoordSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SpaceFrame'), spaceFrame, scope=astroCoordSystem))

astroCoordSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TimeFrame'), timeFrame, scope=astroCoordSystem))

astroCoordSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SpectralFrame'), spectralFrame, scope=astroCoordSystem))
astroCoordSystem._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(astroCoordSystem._UseForTag(pyxb.namespace.ExpandedName(None, u'TimeFrame')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(astroCoordSystem._UseForTag(pyxb.namespace.ExpandedName(None, u'SpaceFrame')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(astroCoordSystem._UseForTag(pyxb.namespace.ExpandedName(None, u'SpectralFrame')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(astroCoordSystem._UseForTag(pyxb.namespace.ExpandedName(None, u'RedshiftFrame')), min_occurs=0L, max_occurs=1)
    )
astroCoordSystem._ContentModel = pyxb.binding.content.ParticleModel(astroCoordSystem._GroupModel, min_occurs=1, max_occurs=1)



smallCircleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Pole'), CommonDM.dm.bas.dtd_stub.double2Type, scope=smallCircleType))
smallCircleType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(smallCircleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Pole')), min_occurs=0L, max_occurs=1)
    )
smallCircleType._ContentModel = pyxb.binding.content.ParticleModel(smallCircleType._GroupModel, min_occurs=1, max_occurs=1)



pixelVector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value2'), CommonDM.dm.bas.dtd_stub.double2Type, scope=pixelVector2CoordinateType))

pixelVector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name1'), pyxb.binding.datatypes.string, scope=pixelVector2CoordinateType))

pixelVector2CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name2'), pyxb.binding.datatypes.string, scope=pixelVector2CoordinateType))
pixelVector2CoordinateType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelVector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelVector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelVector2CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value2')), min_occurs=0L, max_occurs=1)
    )
pixelVector2CoordinateType._ContentModel = pyxb.binding.content.ParticleModel(pixelVector2CoordinateType._GroupModel, min_occurs=1, max_occurs=1)



polygonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Vertex'), vertexType, scope=polygonType, documentation=u'In order to form polygons, vertices are to be connected with straight line segments. In the case of spherical coordinates: greatcircle segments; if a smallCircle element si present, the vertex and its predecessor are to be connected with a smallcircle, by default in the CoordSys that is referenced; optionally, a pole may be specified (other than the CoordSys pole) that defines the smallcircle system'))
polygonType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(polygonType._UseForTag(pyxb.namespace.ExpandedName(None, u'Vertex')), min_occurs=1, max_occurs=100L)
    )
polygonType._ContentModel = pyxb.binding.content.ParticleModel(polygonType._GroupModel, min_occurs=1, max_occurs=1)



vertexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SmallCircle'), smallCircleType, scope=vertexType))

vertexType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Position'), CommonDM.dm.bas.dtd_stub.double2Type, scope=vertexType))
vertexType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(vertexType._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(vertexType._UseForTag(pyxb.namespace.ExpandedName(None, u'SmallCircle')), min_occurs=0L, max_occurs=1)
    )
vertexType._ContentModel = pyxb.binding.content.ParticleModel(vertexType._GroupModel, min_occurs=1, max_occurs=1)



boxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Size'), CommonDM.dm.bas.dtd_stub.double2Type, scope=boxType, documentation=u"The lengths of the box's sides"))

boxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Center'), CommonDM.dm.bas.dtd_stub.double2Type, scope=boxType, documentation=u"The coordinates of the box's center"))
boxType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(boxType._UseForTag(pyxb.namespace.ExpandedName(None, u'Center')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(boxType._UseForTag(pyxb.namespace.ExpandedName(None, u'Size')), min_occurs=1, max_occurs=1)
    )
boxType._ContentModel = pyxb.binding.content.ParticleModel(boxType._GroupModel, min_occurs=1, max_occurs=1)



UTCMicrosecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), UTCMicrosecDateTime, scope=UTCMicrosecDateTimeRange))

UTCMicrosecDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), UTCMicrosecDateTime, scope=UTCMicrosecDateTimeRange))
UTCMicrosecDateTimeRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(UTCMicrosecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(UTCMicrosecDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), min_occurs=1, max_occurs=1)
    )
UTCMicrosecDateTimeRange._ContentModel = pyxb.binding.content.ParticleModel(UTCMicrosecDateTimeRange._GroupModel, min_occurs=1, max_occurs=1)



sectorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PosAngle1'), CommonDM.dm.bas.dtd_stub.double1Type, scope=sectorType, documentation=u'The area cw from this position angle is included'))

sectorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PosAngle2'), CommonDM.dm.bas.dtd_stub.double1Type, scope=sectorType, documentation=u'The area cw from this position angle is included.'))

sectorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Position'), CommonDM.dm.bas.dtd_stub.double2Type, scope=sectorType, documentation=u'The vertex position of the sector'))
sectorType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sectorType._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sectorType._UseForTag(pyxb.namespace.ExpandedName(None, u'PosAngle1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(sectorType._UseForTag(pyxb.namespace.ExpandedName(None, u'PosAngle2')), min_occurs=1, max_occurs=1)
    )
sectorType._ContentModel = pyxb.binding.content.ParticleModel(sectorType._GroupModel, min_occurs=1, max_occurs=1)



UTCDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end'), UTCDateTime, scope=UTCDateTimeRange))

UTCDateTimeRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start'), UTCDateTime, scope=UTCDateTimeRange))
UTCDateTimeRange._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(UTCDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'start')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(UTCDateTimeRange._UseForTag(pyxb.namespace.ExpandedName(None, u'end')), min_occurs=1, max_occurs=1)
    )
UTCDateTimeRange._ContentModel = pyxb.binding.content.ParticleModel(UTCDateTimeRange._GroupModel, min_occurs=1, max_occurs=1)



circleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Radius'), CommonDM.dm.bas.dtd_stub.double1Type, scope=circleType, documentation=u'The radius of the circle'))

circleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Center'), CommonDM.dm.bas.dtd_stub.double2Type, scope=circleType, documentation=u"The coordinates of the circle's center"))
circleType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(circleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Center')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(circleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Radius')), min_occurs=1, max_occurs=1)
    )
circleType._ContentModel = pyxb.binding.content.ParticleModel(circleType._GroupModel, min_occurs=1, max_occurs=1)



vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name3'), pyxb.binding.datatypes.string, scope=vector3CoordinateType))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value3'), CommonDM.dm.bas.dtd_stub.double3Type, scope=vector3CoordinateType))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PixSize3'), CommonDM.dm.bas.dtd_stub.double3Type, scope=vector3CoordinateType))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name1'), pyxb.binding.datatypes.string, scope=vector3CoordinateType))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Size3'), CommonDM.dm.bas.dtd_stub.double3Type, scope=vector3CoordinateType))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name2'), pyxb.binding.datatypes.string, scope=vector3CoordinateType))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Resolution3'), CommonDM.dm.bas.dtd_stub.double3Type, scope=vector3CoordinateType))

vector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Error3'), CommonDM.dm.bas.dtd_stub.double3Type, scope=vector3CoordinateType))
vector3CoordinateType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name3')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value3')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Error3')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Resolution3')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Size3')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(vector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'PixSize3')), min_occurs=0L, max_occurs=2L)
    )
vector3CoordinateType._ContentModel = pyxb.binding.content.ParticleModel(vector3CoordinateType._GroupModel, min_occurs=1, max_occurs=1)



pixelVector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name1'), pyxb.binding.datatypes.string, scope=pixelVector3CoordinateType))

pixelVector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value3'), CommonDM.dm.bas.dtd_stub.double3Type, scope=pixelVector3CoordinateType))

pixelVector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name3'), pyxb.binding.datatypes.string, scope=pixelVector3CoordinateType))

pixelVector3CoordinateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name2'), pyxb.binding.datatypes.string, scope=pixelVector3CoordinateType))
pixelVector3CoordinateType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pixelVector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelVector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelVector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name3')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pixelVector3CoordinateType._UseForTag(pyxb.namespace.ExpandedName(None, u'Value3')), min_occurs=0L, max_occurs=1)
    )
pixelVector3CoordinateType._ContentModel = pyxb.binding.content.ParticleModel(pixelVector3CoordinateType._GroupModel, min_occurs=1, max_occurs=1)



timeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=timeFrame))

timeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReferencePosition'), referencePosition, scope=timeFrame))

timeFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TimeScale'), timeScale, scope=timeFrame))
timeFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(timeFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(timeFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'TimeScale')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(timeFrame._UseForTag(pyxb.namespace.ExpandedName(None, u'ReferencePosition')), min_occurs=1, max_occurs=1)
    )
timeFrame._ContentModel = pyxb.binding.content.ParticleModel(timeFrame._GroupModel, min_occurs=1, max_occurs=1)
