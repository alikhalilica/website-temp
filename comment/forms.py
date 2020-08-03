from .models import Comment
from django import forms


class BlogCommentForm (forms.ModelForm):
    class Meta : 
        model = Comment
        fields = ("name","email","parent","body","url")