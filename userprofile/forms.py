from allauth.account.forms import LoginForm
from captcha.fields import CaptchaField




class AllauthLoginForm(LoginForm):
    
    captcha = CaptchaField()

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(AllauthLoginForm, self).login(*args, **kwargs)