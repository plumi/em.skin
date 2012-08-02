from zope.interface import Interface
from plonetheme.classic.browser.interfaces import IThemeSpecific as IClassicTheme


class IThemeSpecific(IClassicTheme):
    """theme-specific layer"""


class IEmSkinLayer(Interface):
    """Marker interface for browserlayer."""
