from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

class TopViewlet(ViewletBase):
    render = ViewPageTemplateFile('topviewlet.pt')

    def update(self):
        # set here the values that you need to grab from the template.
        registry = getUtility(IRegistry)
        self.displayNotification = registry['em.skin.browser.interfaces.IEmSettings.addNotification']
        self.notificationText = registry['em.skin.browser.interfaces.IEmSettings.notificationText']
        self.notificationLink = registry['em.skin.browser.interfaces.IEmSettings.notificationLink']
        self.notificationLinkText = registry['em.skin.browser.interfaces.IEmSettings.notificationLinkText']

