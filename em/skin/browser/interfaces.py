from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer
from collective.captcha.form.field import Captcha

from zope.i18nmessageid import MessageFactory
_ = MessageFactory("plumi")

class IThemeSpecific(IDefaultPloneLayer):
    """theme-specific layer"""


class IEmSkinLayer(Interface):
    """Marker interface for browserlayer."""

class IEMRegistrationForm(Interface):
    """Marker interface for my custom registration form
    """


class ICaptchaSchema(Interface):
    captcha = Captcha(
        title=_(u'Verification'),
        description=_(
            u'Type the code from the picture shown below.'
        ),
    )
