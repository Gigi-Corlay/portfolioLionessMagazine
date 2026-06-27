from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm

# 1. AJOUT DE L'IMPORT DE TRADUCTION
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label=_("First Name"),  # Ajout de _()
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Your First Name"),  # Optionnel : traduit aussi le placeholder
                "class": "form-control"
            }
        )
    )

    last_name = forms.CharField(
        label=_("Last Name"),
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Your Last Name"),
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        label=_("Email Address"),
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "your@email.com",
                "class": "form-control"
            }
        )
    )

    country = forms.CharField(
        label=_("Country"),
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Your Country"),
                "class": "form-control"
            }
        )
    )

    occupation = forms.CharField(
        label=_("Occupation"),
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Your Occupation"),
                "class": "form-control"
            }
        )
    )

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                "placeholder": _("Password"),
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput(
            attrs={
                "placeholder": _("Confirm Password"),
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
            # Traduction du message d'erreur d'email existant
            raise forms.ValidationError(
                _("An account with this email already exists.")
            )

        return email

# Les autres formulaires restent identiques mais tu pourras y ajouter des _() au besoin.
class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(
            attrs={
                "placeholder": "your@email.com",
                "class": "form-control",
                "autofocus": True
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": _("Password"),
                "class": "form-control"
            }
        )
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("country", "occupation", "profile_picture", "bio")
        # Si c'est un ModelForm, on peut passer par l'attribut labels :
        labels = {
            "country": _("Country"),
            "occupation": _("Occupation"),
            "bio": _("Bio"),
        }
        widgets = {
            "country": forms.TextInput(attrs={"class": "form-control", "placeholder": _("Country")}),
            "occupation": forms.TextInput(attrs={"class": "form-control", "placeholder": _("Occupation")}),
            "profile_picture": forms.FileInput(attrs={"class": "form-control d-none", "id": "id_profile_picture", "accept": "image/*"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "placeholder": _("Tell us about yourself..."), "rows": 5}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        labels = {
            "first_name": _("First Name"),
            "last_name": _("Last Name"),
            "email": _("Email Address"),
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": _("First Name")}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": _("Last Name")}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": _("Email Address")}),
        }

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(_("This email address is already in use."))
        return email


class StyledPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Current Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": _("Current Password"), "autofocus": True}),
    )
    new_password1 = forms.CharField(
        label=_("New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": _("New Password")}),
        help_text=_("Your password must contain at least 8 characters and can't be entirely numeric."),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": _("Confirm New Password")}),
    )
