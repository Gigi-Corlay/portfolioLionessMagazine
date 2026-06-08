from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Name",
            "class": "form-control"
        })
    )

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Your First Name",
            "class": "form-control"
        })
    )

    country = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Country",
            "class": "form-control"
        })
    )

    occupation = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Job",
            "class": "form-control"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "E-mail",
            "class": "form-control"
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirm Password",
            "class": "form-control"
        })
    )

    class Meta:
        model = User
        fields = [
            "last_name",
            "first_name",
            "email",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.EmailInput(attrs={
            "placeholder": "E-mail",
            "class": "form-control"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control"
        })
    )
