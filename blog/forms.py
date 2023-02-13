from django import forms
from blog.models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "text",
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = (
            "text",
            "rating"
        )