from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
     
