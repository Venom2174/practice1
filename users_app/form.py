from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from .models import Users

class UserLoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4",
        "placeholder":"Foydalanuvchi nomini kiriting"
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control py-4",
        "placeholder":"Parolni kiriting kiriting"
    }))
    class Meta:
        model = Users
        fields=('username','password')

class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4",
        "placeholder":"Ismingizni kiriting"
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4",
        "placeholder":"Familiyangizni kiriting"
    }))
    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4",
        "placeholder":"Foydalanuvchi nomini kiriting"
    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4",
        "placeholder":"Email manzilini kiriting"
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control py-4",
        "placeholder":"Parolni kiriting"
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control py-4",
        "placeholder":"Parolni takrorlang"
    }))
    
    class Meta:
        model=Users
        fields={'first_name','last_name','username','email','password1','password2'}

class UserProfileForm(UserChangeForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4"
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4"
    }))
    photo=forms.ImageField(widget=forms.FileInput(attrs={
        "class":"custom-file-input"
    }),required=False)
    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4",
        "readonly":True
    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4",
        "readonly":True
    }))
    class Meta:
        model=Users
        fields={'first_name','last_name','photo','username','email'}