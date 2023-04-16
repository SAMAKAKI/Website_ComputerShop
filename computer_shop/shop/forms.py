from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Login',
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'placeholder': 'Email',
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Repeat password',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Login',
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Password',
    }))


class ContactForm(forms.Form):
    username = forms.CharField(label='Your login', widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Login',
    }))
    email = forms.EmailField(label='Your email', widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'placeholder': 'Email',
    }))
    content = forms.CharField(label='Your problem', widget=forms.Textarea(attrs={
        'class': 'form-textarea',
        'placeholder': 'Your problem',
    }))


class AddElem(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Category don't choose"

    class Meta:
        model = ComputerElems
        fields = ['title', 'slug', 'cat', 'content', 'photo', 'price']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Title'
            }),
            'slug': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'URL'
            }),
            'cat': forms.Select(attrs={
                'class': 'form-input',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Content'
            }),
            ''
            'price': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Price'
            }),
        }