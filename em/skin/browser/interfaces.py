from zope import schema
from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer
from collective.captcha.form.field import Captcha

from zope.i18nmessageid import MessageFactory
_ = MessageFactory("plumi")

class IThemeSpecific(IDefaultPloneLayer):
    """theme-specific layer"""


class IEmSkinLayer(Interface):
    """Marker interface for browserlayer."""

class IEmSettings(Interface):
    """Engagemedia settings"""

    addNotification = schema.Bool(title = u'Display top page notification',
                             default = False,
                            )

    notificationText = schema.Text(title= u"Text to show at the top of the page",
                             default = u"",
                             required=False,
                            )

    notificationLinkText = schema.TextLine(title= u"Link text to show after the previous text",
                             default = u"",
                             required=False,
                            )

    notificationLink = schema.TextLine(title= u"URL to point to for the previous link",
                             default = u"",
                             required=False,
                            )

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
