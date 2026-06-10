from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):

    last_name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Name",
                "class": "form-control"
            }
        )
    )

    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your First Name",
                "class": "form-control"
            }
        )
    )

    country = forms.CharField(
        label="Country",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Country",
                "class": "form-control"
            }
        )
    )

    occupation = forms.CharField(
        label="Occupation",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Job",
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        label="E-mail address",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-mail",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-mail",
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        )
    )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            "country",
            "occupation",
        ]
