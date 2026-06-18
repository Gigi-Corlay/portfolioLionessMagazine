from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your First Name",
                "class": "form-control"
            }
        )
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Last Name",
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        label="Email Address",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "your@email.com",
                "class": "form-control"
            }
        )
    )

    country = forms.CharField(
        label="Country",
        max_length=100,
        required=True,
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
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Occupation",
                "class": "form-control"
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User

        fields = (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def clean_email(self):

        email = self.cleaned_data.get(
            "email",
            ""
        ).strip().lower()

        if User.objects.filter(
            email__iexact=email
        ).exists():

            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email


class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "your@email.com",
                "class": "form-control",
                "autofocus": True
            }
        )
    )

    password = forms.CharField(
        label="Password",
        strip=False,
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

        fields = (
            "country",
            "occupation",
            "profile_picture",
            "bio",
        )

        widgets = {
            "country": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Country"
                }
            ),

            "occupation": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Occupation"
                }
            ),

            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tell us about yourself...",
                    "rows": 5
                }
            ),
        }


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User

        fields = (
            "first_name",
            "last_name",
            "email",
        )

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First Name"
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last Name"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address"
                }
            ),
        }

    def clean_email(self):

        email = self.cleaned_data["email"].strip().lower()

        if User.objects.filter(
            email__iexact=email
        ).exclude(
            pk=self.instance.pk
        ).exists():

            raise forms.ValidationError(
                "This email address is already in use."
            )

        return email
