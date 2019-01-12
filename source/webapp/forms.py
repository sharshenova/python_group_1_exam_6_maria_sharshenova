from django import forms
from webapp.models import Post, UserInfo


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['phone', 'photo']
