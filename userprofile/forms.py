from allauth.account.forms import LoginForm,SignupForm,ResetPasswordForm
from captcha.fields import CaptchaField
from django import forms



class AllauthLoginForm(LoginForm):
    
    captcha = CaptchaField()

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(AllauthLoginForm, self).login(*args, **kwargs)



class AllauthSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100,label='First Name')
    last_name = forms.CharField(max_length=100,label='Last Name')
    captcha = CaptchaField()

    def save(self, request):
        

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(AllauthSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # Add your own processing here.

        # You must return the original result.
        return user

        
class AllauthPasswordForm(ResetPasswordForm):

    captcha = CaptchaField()

    
