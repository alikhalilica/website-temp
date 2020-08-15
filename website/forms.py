from django import forms
from .models import contact
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=contact
        fields=('message','name','Email','subject')