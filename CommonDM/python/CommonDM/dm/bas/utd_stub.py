# /home/nikoapos/ISDC/Projects/Alexandria/2.0/CommonDM/python/CommonDM/dm/bas/utd_stub.py
# PyXB bindings for NamespaceModule
# NSM:2f30d0a941a2897d1cb3db270c7569e6047b1818
# Generated 2014-06-12 14:36:51.813091 by PyXB version 1.1.2
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

Namespace = pyxb.namespace.NamespaceForURI(u'http://euclid.esa.org/schema/bas/utd', create_if_missing=True)
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
class stdUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ List of Units attributes used in EUCLID SGS, implementation proposed via attributes XML. This grammar is derived from Table 3 and Table 4  IAU recommended basic units from FITS standard V3.0. The syntax of Unit is compliant with 3.2.1 of Standards for Astronomical Catalogues Version 2.0. Prefixes for multiples and submultiples are derived from table 5 from FITS units standards."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'stdUnit')
    _Documentation = u' List of Units attributes used in EUCLID SGS, implementation proposed via attributes XML. This grammar is derived from Table 3 and Table 4  IAU recommended basic units from FITS standard V3.0. The syntax of Unit is compliant with 3.2.1 of Standards for Astronomical Catalogues Version 2.0. Prefixes for multiples and submultiples are derived from table 5 from FITS units standards.'
stdUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stdUnit, enum_prefix=None)
stdUnit.m = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'm')
stdUnit.mm = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'mm')
stdUnit.nm = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'nm')
stdUnit.um = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'um')
stdUnit.km = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'km')
stdUnit.Angstrom = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'Angstrom')
stdUnit.kg = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'kg')
stdUnit.s = stdUnit._CF_enumeration.addEnumeration(unicode_value=u's')
stdUnit.h = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'h')
stdUnit.d = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'd')
stdUnit.JD = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'JD')
stdUnit.a = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'a')
stdUnit.yr = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'yr')
stdUnit.cy = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'cy')
stdUnit.sr = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'sr')
stdUnit.K = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'K')
stdUnit.CelsiusDeg = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'CelsiusDeg')
stdUnit.ADU = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'ADU')
stdUnit.mol = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'mol')
stdUnit.cd = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'cd')
stdUnit.Hz = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'Hz')
stdUnit.kHz = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'kHz')
stdUnit.MHz = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'MHz')
stdUnit.GHz = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'GHz')
stdUnit.J = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'J')
stdUnit.W = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'W')
stdUnit.Wm2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'W/m2')
stdUnit.mK = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'mK')
stdUnit.V = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'V')
stdUnit.mV = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'mV')
stdUnit.N = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'N')
stdUnit.Pa = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'Pa')
stdUnit.C = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'C')
stdUnit.Ohm = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'Ohm')
stdUnit.S = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'S')
stdUnit.F = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'F')
stdUnit.Wb = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'Wb')
stdUnit.T = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'T')
stdUnit.H = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'H')
stdUnit.lm = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'lm')
stdUnit.lx = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'lx')
stdUnit.deg = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'deg')
stdUnit.rad = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'rad')
stdUnit.arcmin = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'arcmin')
stdUnit.arcsec = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'arcsec')
stdUnit.uarcsec = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'uarcsec')
stdUnit.mas = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'mas')
stdUnit.min = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'min')
stdUnit.eV = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'eV')
stdUnit.keV = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'keV')
stdUnit.MeV = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'MeV')
stdUnit.GeV = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'GeV')
stdUnit.TeV = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'TeV')
stdUnit.erg = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'erg')
stdUnit.Ry = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'Ry')
stdUnit.solMass = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'solMass')
stdUnit.u = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'u')
stdUnit.solLum = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'solLum')
stdUnit.solRad = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'solRad')
stdUnit.AU = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'AU')
stdUnit.lyr = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'lyr')
stdUnit.pc = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'pc')
stdUnit.kpc = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'kpc')
stdUnit.count = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'count')
stdUnit.ct = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'ct')
stdUnit.photon = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'photon')
stdUnit.ph = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'ph')
stdUnit.Jy = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'Jy')
stdUnit.mag = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'mag')
stdUnit.R = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'R')
stdUnit.pixel = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'pixel')
stdUnit.pix = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'pix')
stdUnit.ms = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'm/s')
stdUnit.kms = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'km/s')
stdUnit.n1mol = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'1/mol')
stdUnit.JK = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'J/K')
stdUnit.m2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'm2')
stdUnit.gcm3 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'g/cm3')
stdUnit.m3s2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'm3/s2')
stdUnit.ms2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'm/s2')
stdUnit.degday = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'deg/day')
stdUnit.radday = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'rad/day')
stdUnit.deg2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'deg2')
stdUnit.um2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'um2')
stdUnit.rads = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'rad/s')
stdUnit.m2s2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'm2/s2')
stdUnit.m2s = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'm2/s')
stdUnit.eVK = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'eV/K')
stdUnit.kmskpc = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'km/s/kpc')
stdUnit.particlesscm2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'particles/s/cm2')
stdUnit.cy_ = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'c/y')
stdUnit.ppmK = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'ppm/K')
stdUnit.kmsMpc = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'km/s/Mpc')
stdUnit.Myr = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'Myr')
stdUnit.uarcsecyr = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'uarcsec/yr')
stdUnit.arcsecyr = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'arcsec/yr')
stdUnit.kmyrs = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'kmyr/s')
stdUnit.magkpc = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'mag/kpc')
stdUnit.smaskmyr = stdUnit._CF_enumeration.addEnumeration(unicode_value=u's/mas/km/yr')
stdUnit.Jm3K4 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'J/m3/K4')
stdUnit.n1m = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'1/m')
stdUnit.JmolK = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'J/mol/K')
stdUnit.m3khs2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'm3/kh/s2')
stdUnit.uNewtonkg = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'uNewton/kg')
stdUnit.uPa = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'uPa')
stdUnit.m2kg = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'm2/kg')
stdUnit.WmK = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'W/m/K')
stdUnit.JKkg = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'J/K/kg')
stdUnit.magarcsec2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'mag/arcsec2')
stdUnit.starsdeg2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'stars/deg2')
stdUnit.Mstarsdeg2 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'Mstars/deg2')
stdUnit.Mstars = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'Mstars')
stdUnit.stars = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'stars')
stdUnit.m2s2K = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'm2/s2/K')
stdUnit.Wm2K4 = stdUnit._CF_enumeration.addEnumeration(unicode_value=u'W/m2/K4')
stdUnit._InitializeFacetMap(stdUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'stdUnit', stdUnit)

# Atomic SimpleTypeDefinition
class miscUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """List of miscellaneous Units attributes used in EUCLID SGS, implementation proposed via attributes XML.Rule proposes an empty field ''. TBD is prohibited. Micrometers character is u no greek character, no blank character allowed."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'miscUnit')
    _Documentation = u'List of miscellaneous Units attributes used in EUCLID SGS, implementation proposed via attributes XML.Rule proposes an empty field "". TBD is prohibited. Micrometers character is u no greek character, no blank character allowed.'
miscUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=miscUnit, enum_prefix=None)
miscUnit.emptyString = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'%')
miscUnit.Gain = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'Gain')
miscUnit.NA = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'NA')
miscUnit.Number = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'Number')
miscUnit.QE = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'QE')
miscUnit.emptyString_ = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'')
miscUnit.daymonth = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'day/month')
miscUnit.e = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'e-')
miscUnit.e_rms = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'e-rms')
miscUnit.ehrpix = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'e/hr/pix')
miscUnit.espix = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'e/s/pix')
miscUnit.epix = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'e/pix')
miscUnit.ergscm2Hzarcsec2 = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'erg/s/cm2/Hz/arcsec2')
miscUnit.s6months = miscUnit._CF_enumeration.addEnumeration(unicode_value=u's/6months')
miscUnit.sqxdeg = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'sqxdeg')
miscUnit.upix = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'u/pix')
miscUnit.ergscm2Angstrom = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'erg/s/cm2/Angstrom')
miscUnit.ergscm2Hz = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'erg/s/cm2/Hz')
miscUnit.ergscm2 = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'erg/s/cm2')
miscUnit.photonscm2 = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'photon/s/cm2')
miscUnit.photonsm2 = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'photon/s/m2')
miscUnit.mass = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'mas/s')
miscUnit.Wm2nm = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'W/m2/nm')
miscUnit.Wm2Hz = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'W/m2/Hz')
miscUnit.photonsm2nm = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'photon/s/m2/nm')
miscUnit.bit = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'bit')
miscUnit.magates = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'mag/at/e/s')
miscUnit.Fm = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'F/m')
miscUnit.NA2 = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'N/A2')
miscUnit.particlesm2shemisphere = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'particles/m2/s/hemisphere')
miscUnit.J_s = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'J s')
miscUnit.syr = miscUnit._CF_enumeration.addEnumeration(unicode_value=u's/yr')
miscUnit.Gpa = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'Gpa')
miscUnit.A = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'A')
miscUnit.ergcm2sA = miscUnit._CF_enumeration.addEnumeration(unicode_value=u'erg/cm2/s/A')
miscUnit._InitializeFacetMap(miscUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'miscUnit', miscUnit)

# Union SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class unit (pyxb.binding.basis.STD_union):

    """Simple type that is a union of stdUnit, miscUnit."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unit')
    _Documentation = None

    _MemberTypes = ( stdUnit, miscUnit, )
unit._CF_pattern = pyxb.binding.facets.CF_pattern()
unit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=unit)
unit.m = u'm'                                     # originally stdUnit.m
unit.mm = u'mm'                                   # originally stdUnit.mm
unit.nm = u'nm'                                   # originally stdUnit.nm
unit.um = u'um'                                   # originally stdUnit.um
unit.km = u'km'                                   # originally stdUnit.km
unit.Angstrom = u'Angstrom'                       # originally stdUnit.Angstrom
unit.kg = u'kg'                                   # originally stdUnit.kg
unit.s = u's'                                     # originally stdUnit.s
unit.h = u'h'                                     # originally stdUnit.h
unit.d = u'd'                                     # originally stdUnit.d
unit.JD = u'JD'                                   # originally stdUnit.JD
unit.a = u'a'                                     # originally stdUnit.a
unit.yr = u'yr'                                   # originally stdUnit.yr
unit.cy = u'cy'                                   # originally stdUnit.cy
unit.sr = u'sr'                                   # originally stdUnit.sr
unit.K = u'K'                                     # originally stdUnit.K
unit.CelsiusDeg = u'CelsiusDeg'                   # originally stdUnit.CelsiusDeg
unit.ADU = u'ADU'                                 # originally stdUnit.ADU
unit.mol = u'mol'                                 # originally stdUnit.mol
unit.cd = u'cd'                                   # originally stdUnit.cd
unit.Hz = u'Hz'                                   # originally stdUnit.Hz
unit.kHz = u'kHz'                                 # originally stdUnit.kHz
unit.MHz = u'MHz'                                 # originally stdUnit.MHz
unit.GHz = u'GHz'                                 # originally stdUnit.GHz
unit.J = u'J'                                     # originally stdUnit.J
unit.W = u'W'                                     # originally stdUnit.W
unit.Wm2 = u'W/m2'                                # originally stdUnit.Wm2
unit.mK = u'mK'                                   # originally stdUnit.mK
unit.V = u'V'                                     # originally stdUnit.V
unit.mV = u'mV'                                   # originally stdUnit.mV
unit.N = u'N'                                     # originally stdUnit.N
unit.Pa = u'Pa'                                   # originally stdUnit.Pa
unit.C = u'C'                                     # originally stdUnit.C
unit.Ohm = u'Ohm'                                 # originally stdUnit.Ohm
unit.S = u'S'                                     # originally stdUnit.S
unit.F = u'F'                                     # originally stdUnit.F
unit.Wb = u'Wb'                                   # originally stdUnit.Wb
unit.T = u'T'                                     # originally stdUnit.T
unit.H = u'H'                                     # originally stdUnit.H
unit.lm = u'lm'                                   # originally stdUnit.lm
unit.lx = u'lx'                                   # originally stdUnit.lx
unit.deg = u'deg'                                 # originally stdUnit.deg
unit.rad = u'rad'                                 # originally stdUnit.rad
unit.arcmin = u'arcmin'                           # originally stdUnit.arcmin
unit.arcsec = u'arcsec'                           # originally stdUnit.arcsec
unit.uarcsec = u'uarcsec'                         # originally stdUnit.uarcsec
unit.mas = u'mas'                                 # originally stdUnit.mas
unit.min = u'min'                                 # originally stdUnit.min
unit.eV = u'eV'                                   # originally stdUnit.eV
unit.keV = u'keV'                                 # originally stdUnit.keV
unit.MeV = u'MeV'                                 # originally stdUnit.MeV
unit.GeV = u'GeV'                                 # originally stdUnit.GeV
unit.TeV = u'TeV'                                 # originally stdUnit.TeV
unit.erg = u'erg'                                 # originally stdUnit.erg
unit.Ry = u'Ry'                                   # originally stdUnit.Ry
unit.solMass = u'solMass'                         # originally stdUnit.solMass
unit.u = u'u'                                     # originally stdUnit.u
unit.solLum = u'solLum'                           # originally stdUnit.solLum
unit.solRad = u'solRad'                           # originally stdUnit.solRad
unit.AU = u'AU'                                   # originally stdUnit.AU
unit.lyr = u'lyr'                                 # originally stdUnit.lyr
unit.pc = u'pc'                                   # originally stdUnit.pc
unit.kpc = u'kpc'                                 # originally stdUnit.kpc
unit.count = u'count'                             # originally stdUnit.count
unit.ct = u'ct'                                   # originally stdUnit.ct
unit.photon = u'photon'                           # originally stdUnit.photon
unit.ph = u'ph'                                   # originally stdUnit.ph
unit.Jy = u'Jy'                                   # originally stdUnit.Jy
unit.mag = u'mag'                                 # originally stdUnit.mag
unit.R = u'R'                                     # originally stdUnit.R
unit.pixel = u'pixel'                             # originally stdUnit.pixel
unit.pix = u'pix'                                 # originally stdUnit.pix
unit.ms = u'm/s'                                  # originally stdUnit.ms
unit.kms = u'km/s'                                # originally stdUnit.kms
unit.n1mol = u'1/mol'                             # originally stdUnit.n1mol
unit.JK = u'J/K'                                  # originally stdUnit.JK
unit.m2 = u'm2'                                   # originally stdUnit.m2
unit.gcm3 = u'g/cm3'                              # originally stdUnit.gcm3
unit.m3s2 = u'm3/s2'                              # originally stdUnit.m3s2
unit.ms2 = u'm/s2'                                # originally stdUnit.ms2
unit.degday = u'deg/day'                          # originally stdUnit.degday
unit.radday = u'rad/day'                          # originally stdUnit.radday
unit.deg2 = u'deg2'                               # originally stdUnit.deg2
unit.um2 = u'um2'                                 # originally stdUnit.um2
unit.rads = u'rad/s'                              # originally stdUnit.rads
unit.m2s2 = u'm2/s2'                              # originally stdUnit.m2s2
unit.m2s = u'm2/s'                                # originally stdUnit.m2s
unit.eVK = u'eV/K'                                # originally stdUnit.eVK
unit.kmskpc = u'km/s/kpc'                         # originally stdUnit.kmskpc
unit.particlesscm2 = u'particles/s/cm2'           # originally stdUnit.particlesscm2
unit.cy_ = u'c/y'                                 # originally stdUnit.cy_
unit.ppmK = u'ppm/K'                              # originally stdUnit.ppmK
unit.kmsMpc = u'km/s/Mpc'                         # originally stdUnit.kmsMpc
unit.Myr = u'Myr'                                 # originally stdUnit.Myr
unit.uarcsecyr = u'uarcsec/yr'                    # originally stdUnit.uarcsecyr
unit.arcsecyr = u'arcsec/yr'                      # originally stdUnit.arcsecyr
unit.kmyrs = u'kmyr/s'                            # originally stdUnit.kmyrs
unit.magkpc = u'mag/kpc'                          # originally stdUnit.magkpc
unit.smaskmyr = u's/mas/km/yr'                    # originally stdUnit.smaskmyr
unit.Jm3K4 = u'J/m3/K4'                           # originally stdUnit.Jm3K4
unit.n1m = u'1/m'                                 # originally stdUnit.n1m
unit.JmolK = u'J/mol/K'                           # originally stdUnit.JmolK
unit.m3khs2 = u'm3/kh/s2'                         # originally stdUnit.m3khs2
unit.uNewtonkg = u'uNewton/kg'                    # originally stdUnit.uNewtonkg
unit.uPa = u'uPa'                                 # originally stdUnit.uPa
unit.m2kg = u'm2/kg'                              # originally stdUnit.m2kg
unit.WmK = u'W/m/K'                               # originally stdUnit.WmK
unit.JKkg = u'J/K/kg'                             # originally stdUnit.JKkg
unit.magarcsec2 = u'mag/arcsec2'                  # originally stdUnit.magarcsec2
unit.starsdeg2 = u'stars/deg2'                    # originally stdUnit.starsdeg2
unit.Mstarsdeg2 = u'Mstars/deg2'                  # originally stdUnit.Mstarsdeg2
unit.Mstars = u'Mstars'                           # originally stdUnit.Mstars
unit.stars = u'stars'                             # originally stdUnit.stars
unit.m2s2K = u'm2/s2/K'                           # originally stdUnit.m2s2K
unit.Wm2K4 = u'W/m2/K4'                           # originally stdUnit.Wm2K4
unit.emptyString = u'%'                           # originally miscUnit.emptyString
unit.Gain = u'Gain'                               # originally miscUnit.Gain
unit.NA = u'NA'                                   # originally miscUnit.NA
unit.Number = u'Number'                           # originally miscUnit.Number
unit.QE = u'QE'                                   # originally miscUnit.QE
unit.emptyString_ = u''                           # originally miscUnit.emptyString_
unit.daymonth = u'day/month'                      # originally miscUnit.daymonth
unit.e = u'e-'                                    # originally miscUnit.e
unit.e_rms = u'e-rms'                             # originally miscUnit.e_rms
unit.ehrpix = u'e/hr/pix'                         # originally miscUnit.ehrpix
unit.espix = u'e/s/pix'                           # originally miscUnit.espix
unit.epix = u'e/pix'                              # originally miscUnit.epix
unit.ergscm2Hzarcsec2 = u'erg/s/cm2/Hz/arcsec2'   # originally miscUnit.ergscm2Hzarcsec2
unit.s6months = u's/6months'                      # originally miscUnit.s6months
unit.sqxdeg = u'sqxdeg'                           # originally miscUnit.sqxdeg
unit.upix = u'u/pix'                              # originally miscUnit.upix
unit.ergscm2Angstrom = u'erg/s/cm2/Angstrom'      # originally miscUnit.ergscm2Angstrom
unit.ergscm2Hz = u'erg/s/cm2/Hz'                  # originally miscUnit.ergscm2Hz
unit.ergscm2 = u'erg/s/cm2'                       # originally miscUnit.ergscm2
unit.photonscm2 = u'photon/s/cm2'                 # originally miscUnit.photonscm2
unit.photonsm2 = u'photon/s/m2'                   # originally miscUnit.photonsm2
unit.mass = u'mas/s'                              # originally miscUnit.mass
unit.Wm2nm = u'W/m2/nm'                           # originally miscUnit.Wm2nm
unit.Wm2Hz = u'W/m2/Hz'                           # originally miscUnit.Wm2Hz
unit.photonsm2nm = u'photon/s/m2/nm'              # originally miscUnit.photonsm2nm
unit.bit = u'bit'                                 # originally miscUnit.bit
unit.magates = u'mag/at/e/s'                      # originally miscUnit.magates
unit.Fm = u'F/m'                                  # originally miscUnit.Fm
unit.NA2 = u'N/A2'                                # originally miscUnit.NA2
unit.particlesm2shemisphere = u'particles/m2/s/hemisphere'# originally miscUnit.particlesm2shemisphere
unit.J_s = u'J s'                                 # originally miscUnit.J_s
unit.syr = u's/yr'                                # originally miscUnit.syr
unit.Gpa = u'Gpa'                                 # originally miscUnit.Gpa
unit.A = u'A'                                     # originally miscUnit.A
unit.ergcm2sA = u'erg/cm2/s/A'                    # originally miscUnit.ergcm2sA
unit._InitializeFacetMap(unit._CF_pattern,
   unit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'unit', unit)
