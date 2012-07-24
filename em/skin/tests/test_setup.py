from em.skin.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_is_em_skin_installed(self):
        self.failUnless(self.installer.isProductInstalled('em.skin'))

    def test_is_plone_app_theming_installed(self):
        self.failUnless(self.installer.isProductInstalled('plone.app.theming'))

    def test_is_hexagonit_portletstyle_installed(self):
        self.failUnless(self.installer.isProductInstalled('hexagonit.portletstyle'))

    def test_portlet_styles(self):
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        self.assertEquals(getUtility(IRegistry).get('hexagonit.portletstyle.interfaces.IPortletStyles.portlet_styles'), [
            'noheader|No header',
            'nofooter|No footer',
            'noheader nofooter|No header and no footer'])

    def test_uninstall(self):
        self.installer.uninstallProducts(['em.skin'])
        self.failIf(self.installer.isProductInstalled('em.skin'))

    def test_browserlayer(self):
        from em.skin.browser.interfaces import IEmSkinLayer
        from plone.browserlayer import utils
        self.failUnless(IEmSkinLayer in utils.registered_layers())

    def test_css_registry_configured(self):
        css_resources = set(
            getToolByName(self.portal, 'portal_css').getResourceIds())

        self.failUnless(
            '++theme++em.skin/css/style.css' in css_resources)

    def test_js_registry_configured(self):
        js_resources = set(
            getToolByName(self.portal, 'portal_javascripts').getResourceIds())

        self.failUnless(
            '++theme++em.skin/javascript/libs/modernizr.custom.js'
            in js_resources)
        self.failUnless(
            '++theme++em.skin/javascript/libs/respond.min.js'
            in js_resources)

    def test_doctype_configured(self):
        from plone.app.theming.interfaces import IThemeSettings
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility

        settings = getUtility(IRegistry).forInterface(IThemeSettings)
        self.assertEqual(settings.doctype, '<!doctype html>')
