from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class newUserForm(UserCreationForm):
    email=forms.EmailField(label='Email', max_length=50)

    class Meta: 
        model=User
        fields=["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user=super(newUserForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class loginForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","password"]
     
class UpdateUserForm(forms.ModelForm):
    email=forms.EmailField(max_length=254,help_text='Required.inform a valid email address')
    class Meta:
        model=User
        fields=('username','email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('name','profile_pic','bio','location')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image_post', 'caption')

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'

    class Meta:
        model = Comment
        fields = ('comment',)