from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from em.skin.browser.interfaces import IEmSettings
from plone.z3cform import layout

class EmControlPanelForm(RegistryEditForm):
    schema = IEmSettings

EmControlPanelView = layout.wrap_form(EmControlPanelForm, ControlPanelFormWrapper)

