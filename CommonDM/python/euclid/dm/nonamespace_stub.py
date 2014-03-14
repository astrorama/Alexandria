# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.465664 by PyXB version 1.1.2
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
import euclid.dm.pro.phz_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


PHZPhotoZCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHZPhotoZCatalog'), euclid.dm.pro.phz_stub.phzPhotoZCatalog)
Namespace.addCategoryObject('elementBinding', PHZPhotoZCatalog.name().localName(), PHZPhotoZCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.465996 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLExtPsfModel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLExtPsfModel'), euclid.dm.pro.she_stub.slExtPsfModel)
Namespace.addCategoryObject('elementBinding', SLExtPsfModel.name().localName(), SLExtPsfModel)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.466067 by PyXB version 1.1.2
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
import euclid.dm.pro.phz_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


PHZRadioCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHZRadioCatalog'), euclid.dm.pro.phz_stub.phzRadioCatalog)
Namespace.addCategoryObject('elementBinding', PHZRadioCatalog.name().localName(), PHZRadioCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.466252 by PyXB version 1.1.2
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
import euclid.dm.pro.spe_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SPESpectralTemplates = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SPESpectralTemplates'), euclid.dm.pro.spe_stub.SPESpectralTemplates)
Namespace.addCategoryObject('elementBinding', SPESpectralTemplates.name().localName(), SPESpectralTemplates)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.466438 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLLensCandidatesCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLLensCandidatesCatalog'), euclid.dm.pro.she_stub.slLensCandidatesCatalog)
Namespace.addCategoryObject('elementBinding', SLLensCandidatesCatalog.name().localName(), SLLensCandidatesCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.466969 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLVisPsfModel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLVisPsfModel'), euclid.dm.pro.she_stub.slVisPsfModel)
Namespace.addCategoryObject('elementBinding', SLVisPsfModel.name().localName(), SLVisPsfModel)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.467040 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLNirPsfModel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLNirPsfModel'), euclid.dm.pro.she_stub.slNirPsfModel)
Namespace.addCategoryObject('elementBinding', SLNirPsfModel.name().localName(), SLNirPsfModel)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.467172 by PyXB version 1.1.2
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
import euclid.dm.pro.phz_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


PHZCalibrationData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHZCalibrationData'), euclid.dm.pro.phz_stub.phzCalibrationData)
Namespace.addCategoryObject('elementBinding', PHZCalibrationData.name().localName(), PHZCalibrationData)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.467248 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLShearCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLShearCatalog'), euclid.dm.pro.she_stub.slShearCatalog)
Namespace.addCategoryObject('elementBinding', SLShearCatalog.name().localName(), SLShearCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.467728 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLLensQuasarSubtractedStamps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLLensQuasarSubtractedStamps'), euclid.dm.pro.she_stub.slLensQuasarSubtractedStamps)
Namespace.addCategoryObject('elementBinding', SLLensQuasarSubtractedStamps.name().localName(), SLLensQuasarSubtractedStamps)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.467911 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLPreSelectedCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLPreSelectedCatalog'), euclid.dm.pro.she_stub.slPreSelectedCatalog)
Namespace.addCategoryObject('elementBinding', SLPreSelectedCatalog.name().localName(), SLPreSelectedCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.467983 by PyXB version 1.1.2
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
import euclid.dm.pro.phz_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


PHZXRayCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHZXRayCatalog'), euclid.dm.pro.phz_stub.phzXRayCatalog)
Namespace.addCategoryObject('elementBinding', PHZXRayCatalog.name().localName(), PHZXRayCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.468055 by PyXB version 1.1.2
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
import euclid.dm.pro.spe_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SPECalibratedSpectra = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SPECalibratedSpectra'), euclid.dm.pro.spe_stub.SPECalibratedSpectra)
Namespace.addCategoryObject('elementBinding', SPECalibratedSpectra.name().localName(), SPECalibratedSpectra)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.468245 by PyXB version 1.1.2
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
import euclid.dm.pro.phz_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


PHZPhysicalParametersCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHZPhysicalParametersCatalog'), euclid.dm.pro.phz_stub.phzPhysicalParametersCatalog)
Namespace.addCategoryObject('elementBinding', PHZPhysicalParametersCatalog.name().localName(), PHZPhysicalParametersCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.468317 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLPhotoZCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLPhotoZCatalog'), euclid.dm.pro.she_stub.slPhotoZCatalog)
Namespace.addCategoryObject('elementBinding', SLPhotoZCatalog.name().localName(), SLPhotoZCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.468387 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLPreSelectionParameters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLPreSelectionParameters'), euclid.dm.pro.she_stub.slPreSelectionParameters)
Namespace.addCategoryObject('elementBinding', SLPreSelectionParameters.name().localName(), SLPreSelectionParameters)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.468457 by PyXB version 1.1.2
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
import euclid.dm.pro.spe_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SPESpectralFeatures = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SPESpectralFeatures'), euclid.dm.pro.spe_stub.SPESpectralFeatures)
Namespace.addCategoryObject('elementBinding', SPESpectralFeatures.name().localName(), SPESpectralFeatures)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.468527 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLMerCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLMerCatalog'), euclid.dm.pro.she_stub.slMerCatalog)
Namespace.addCategoryObject('elementBinding', SLMerCatalog.name().localName(), SLMerCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.468596 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLVisCoAddedFrame = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLVisCoAddedFrame'), euclid.dm.pro.she_stub.slVisCoAddedFrame)
Namespace.addCategoryObject('elementBinding', SLVisCoAddedFrame.name().localName(), SLVisCoAddedFrame)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.468668 by PyXB version 1.1.2
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
import euclid.dm.bas.cat_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


CatalogPrimitive = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogPrimitive'), euclid.dm.bas.cat_stub.catalogContainer)
Namespace.addCategoryObject('elementBinding', CatalogPrimitive.name().localName(), CatalogPrimitive)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.468737 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SL2DSpectrum = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SL2DSpectrum'), euclid.dm.pro.she_stub.sl2DSpectrum)
Namespace.addCategoryObject('elementBinding', SL2DSpectrum.name().localName(), SL2DSpectrum)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.468809 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub
import euclid.dm.sys_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# Complex type visCalibratedImageAndMask with content type ELEMENT_ONLY
class visCalibratedImageAndMask (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visCalibratedImageAndMask')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__AbsentNamespace0_visCalibratedImageAndMask_Data', False)

    
    Data = property(__Data.value, __Data.set, None, None)

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__AbsentNamespace0_visCalibratedImageAndMask_Header', False)

    
    Header = property(__Header.value, __Header.set, None, None)


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'visCalibratedImageAndMask', visCalibratedImageAndMask)




visCalibratedImageAndMask._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), euclid.dm.pro.she_stub.visCalibratedImageAndMaskData, scope=visCalibratedImageAndMask))

visCalibratedImageAndMask._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), euclid.dm.sys_stub.genericHeader, scope=visCalibratedImageAndMask))
visCalibratedImageAndMask._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visCalibratedImageAndMask._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visCalibratedImageAndMask._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
visCalibratedImageAndMask._ContentModel = pyxb.binding.content.ParticleModel(visCalibratedImageAndMask._GroupModel, min_occurs=1, max_occurs=1)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.469048 by PyXB version 1.1.2
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
import euclid.dm.pro.phz_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


PHZMorphologyCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHZMorphologyCatalog'), euclid.dm.pro.phz_stub.phzMorphologyCatalog)
Namespace.addCategoryObject('elementBinding', PHZMorphologyCatalog.name().localName(), PHZMorphologyCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.469344 by PyXB version 1.1.2
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
import euclid.dm.pro.spe_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SPEResults = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SPEResults'), euclid.dm.pro.spe_stub.SPEResults)
Namespace.addCategoryObject('elementBinding', SPEResults.name().localName(), SPEResults)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.469415 by PyXB version 1.1.2
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
import euclid.dm.pro.phz_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


PHZPhotometryCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHZPhotometryCatalog'), euclid.dm.pro.phz_stub.phzPhotometryCatalog)
Namespace.addCategoryObject('elementBinding', PHZPhotometryCatalog.name().localName(), PHZPhotometryCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.469593 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLNirFitsStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLNirFitsStamp'), euclid.dm.pro.she_stub.slNirFitsStamp)
Namespace.addCategoryObject('elementBinding', SLNirFitsStamp.name().localName(), SLNirFitsStamp)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.469907 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub
import euclid.dm.sys_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# Complex type shearMeasurement with content type ELEMENT_ONLY
class shearMeasurement (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shearMeasurement')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__AbsentNamespace1_shearMeasurement_Data', False)

    
    Data = property(__Data.value, __Data.set, None, None)

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__AbsentNamespace1_shearMeasurement_Header', False)

    
    Header = property(__Header.value, __Header.set, None, None)


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'shearMeasurement', shearMeasurement)




shearMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), euclid.dm.pro.she_stub.shearMeasurementData, scope=shearMeasurement))

shearMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), euclid.dm.sys_stub.genericHeader, scope=shearMeasurement))
shearMeasurement._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(shearMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shearMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
shearMeasurement._ContentModel = pyxb.binding.content.ParticleModel(shearMeasurement._GroupModel, min_occurs=1, max_occurs=1)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.469979 by PyXB version 1.1.2
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
import euclid.dm.pro.phz_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


PHZSpecZCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHZSpecZCatalog'), euclid.dm.pro.phz_stub.phzSpecZCatalog)
Namespace.addCategoryObject('elementBinding', PHZSpecZCatalog.name().localName(), PHZSpecZCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.470048 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLSpecZCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLSpecZCatalog'), euclid.dm.pro.she_stub.slSpecZCatalog)
Namespace.addCategoryObject('elementBinding', SLSpecZCatalog.name().localName(), SLSpecZCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.470117 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub
import euclid.dm.sys_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# Complex type shearMeasurement with content type ELEMENT_ONLY
class shearMeasurement (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shearMeasurement')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__AbsentNamespace23_shearMeasurement_Data', False)

    
    Data = property(__Data.value, __Data.set, None, None)

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__AbsentNamespace23_shearMeasurement_Header', False)

    
    Header = property(__Header.value, __Header.set, None, None)


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'shearMeasurement', shearMeasurement)


ShearMeasurement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ShearMeasurement'), shearMeasurement)
Namespace.addCategoryObject('elementBinding', ShearMeasurement.name().localName(), ShearMeasurement)



shearMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), euclid.dm.pro.she_stub.shearMeasurementData, scope=shearMeasurement))

shearMeasurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), euclid.dm.sys_stub.genericHeader, scope=shearMeasurement))
shearMeasurement._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(shearMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(shearMeasurement._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
shearMeasurement._ContentModel = pyxb.binding.content.ParticleModel(shearMeasurement._GroupModel, min_occurs=1, max_occurs=1)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.470303 by PyXB version 1.1.2
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
import euclid.dm.pro.phz_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


PHZPDFCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHZPDFCatalog'), euclid.dm.pro.phz_stub.phzPDFCatalog)
Namespace.addCategoryObject('elementBinding', PHZPDFCatalog.name().localName(), PHZPDFCatalog)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.470372 by PyXB version 1.1.2
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
import euclid.dm.pro.phz_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


PHZConfigurationSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PHZConfigurationSet'), euclid.dm.pro.phz_stub.phzConfigurationSet)
Namespace.addCategoryObject('elementBinding', PHZConfigurationSet.name().localName(), PHZConfigurationSet)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.470626 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLVisFitsStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLVisFitsStamp'), euclid.dm.pro.she_stub.slVisFitsStamp)
Namespace.addCategoryObject('elementBinding', SLVisFitsStamp.name().localName(), SLVisFitsStamp)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.470698 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLInspectionParameters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLInspectionParameters'), euclid.dm.pro.she_stub.slInspectionParameters)
Namespace.addCategoryObject('elementBinding', SLInspectionParameters.name().localName(), SLInspectionParameters)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.470910 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLNirCoAddedFrame = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLNirCoAddedFrame'), euclid.dm.pro.she_stub.slNirCoAddedFrame)
Namespace.addCategoryObject('elementBinding', SLNirCoAddedFrame.name().localName(), SLNirCoAddedFrame)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.471268 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLExtFrame = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLExtFrame'), euclid.dm.pro.she_stub.slExtFrame)
Namespace.addCategoryObject('elementBinding', SLExtFrame.name().localName(), SLExtFrame)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.471340 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub
import euclid.dm.sys_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# Complex type visCalibratedImageAndMask with content type ELEMENT_ONLY
class visCalibratedImageAndMask (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visCalibratedImageAndMask')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Data'), 'Data', '__AbsentNamespace2_visCalibratedImageAndMask_Data', False)

    
    Data = property(__Data.value, __Data.set, None, None)

    
    # Element Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Header'), 'Header', '__AbsentNamespace2_visCalibratedImageAndMask_Header', False)

    
    Header = property(__Header.value, __Header.set, None, None)


    _ElementMap = {
        __Data.name() : __Data,
        __Header.name() : __Header
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'visCalibratedImageAndMask', visCalibratedImageAndMask)


VisCalibratedImageAndMask = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VisCalibratedImageAndMask'), visCalibratedImageAndMask)
Namespace.addCategoryObject('elementBinding', VisCalibratedImageAndMask.name().localName(), VisCalibratedImageAndMask)



visCalibratedImageAndMask._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Data'), euclid.dm.pro.she_stub.visCalibratedImageAndMaskData, scope=visCalibratedImageAndMask))

visCalibratedImageAndMask._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Header'), euclid.dm.sys_stub.genericHeader, scope=visCalibratedImageAndMask))
visCalibratedImageAndMask._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(visCalibratedImageAndMask._UseForTag(pyxb.namespace.ExpandedName(None, u'Header')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(visCalibratedImageAndMask._UseForTag(pyxb.namespace.ExpandedName(None, u'Data')), min_occurs=1, max_occurs=1)
    )
visCalibratedImageAndMask._ContentModel = pyxb.binding.content.ParticleModel(visCalibratedImageAndMask._GroupModel, min_occurs=1, max_occurs=1)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.471411 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLExtFitsStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLExtFitsStamp'), euclid.dm.pro.she_stub.slExtFitsStamp)
Namespace.addCategoryObject('elementBinding', SLExtFitsStamp.name().localName(), SLExtFitsStamp)
# /home/nikoapos/ISDC/Projects/Alexandria/1.0/CommonDM/python/euclid/dm/nonamespace_stub.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-03-14 09:43:27.471481 by PyXB version 1.1.2
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
import euclid.dm.pro.she_stub

Namespace = pyxb.namespace.CreateAbsentNamespace()
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


SLPhysicalParametersCatalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SLPhysicalParametersCatalog'), euclid.dm.pro.she_stub.slPhysicalParametersCatalog)
Namespace.addCategoryObject('elementBinding', SLPhysicalParametersCatalog.name().localName(), SLPhysicalParametersCatalog)
