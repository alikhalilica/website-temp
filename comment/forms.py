from .models import Comment
from django import forms
from captcha.fields import CaptchaField


class CommentForm (forms.ModelForm):
    captcha = CaptchaField()
    class Meta : 
        model = Comment
        fields = ('user',"name","email","parent","body","url")