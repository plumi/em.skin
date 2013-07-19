from zope.formlib import form
from zope.interface import implements
from plone.app.users.browser.register import RegistrationForm
from collective.captcha.form.widget import CaptchaWidget
from em.skin.browser.interfaces import IEMRegistrationForm, ICaptchaSchema
from zope.app.form.interfaces import WidgetInputError, InputErrors
from Products.CMFPlone import PloneMessageFactory as _


class EMRegistrationForm(RegistrationForm):
    """ Subclass the standard registration form
    """

    implements(IEMRegistrationForm)

    @form.action(_(u'label_register', default=u'Register'),
                 validator='validate_registration', name=u'register')
    def action_join(self, action, data):
        self.handle_join_success(data)
        # XXX Return somewhere else, depending on what
        # handle_join_success returns?
        return self.context.unrestrictedTraverse('registered')()


    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(EMRegistrationForm, self).form_fields

        # Add a captcha field to the schema
        myfields += form.Fields(ICaptchaSchema)
        myfields['captcha'].custom_widget = CaptchaWidget

        # Perform any field shuffling here...

        # Return the fiddled fields
        return myfields


    def validate_registration(self, action, data):
        """
        check captcha
        """

        errors = super(EMRegistrationForm, self).validate_registration(action, data)

        form_field_names = [f.field.getName() for f in self.form_fields]

        if 'captcha' in form_field_names:
            if not 'captcha' in data.keys():
                err_str = _(u'Please provide the captcha value to prove you are a person.')
                errors.append(WidgetInputError('captcha',
                              u'label_captcha', err_str))
                self.widgets['captcha'].error = err_str

        return errors

