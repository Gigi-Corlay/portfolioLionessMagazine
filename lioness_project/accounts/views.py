from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
import logging

from .forms import (
    RegisterForm,
    LoginForm,
    ProfileForm,
    UserUpdateForm,
)
from .models import Profile

logger = logging.getLogger(__name__)


@login_required(login_url="accounts:login")
def profile_view(request):
    try:
        profile, created = Profile.objects.get_or_create(user=request.user)

        if request.method == "POST":
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileForm(
                request.POST,
                request.FILES,
                instance=profile,
            )

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save(commit=False)
                user.username = user.email.lower().strip()
                user.save()
                profile_form.save()
                return redirect("accounts:profile")
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileForm(instance=profile)

        return render(
            request,
            "profile/profile.html",
            {
                "profile": profile,
                "user_form": user_form,
                "profile_form": profile_form,
            },
        )

    except Exception:
        logger.exception("Erreur dans profile_view")
        raise


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    form = LoginForm(
        request,
        data=request.POST or None
    )

    if request.method == "POST":

        if form.is_valid():

            login(
                request,
                form.get_user()
            )

            messages.success(
                request,
                "Welcome back!"
            )

            return redirect("dashboard")

        messages.error(
            request,
            "Invalid email or password."
        )

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    form = RegisterForm(
        request.POST or None
    )

    if request.method == "POST" and form.is_valid():

        try:

            with transaction.atomic():

                user = form.save(commit=False)

                email = form.cleaned_data["email"]

                user.username = email
                user.email = email
                user.first_name = form.cleaned_data["first_name"]
                user.last_name = form.cleaned_data["last_name"]

                user.save()

                profile = user.profile

                profile.country = form.cleaned_data.get(
                    "country"
                )

                profile.occupation = form.cleaned_data.get(
                    "occupation"
                )

                profile.save()

            login(
                request,
                user
            )

            """
            messages.success(
                request,
                "Account successfully created."
            )
            """

            return redirect("dashboard")

        except Exception as e:

            logger.exception(
                "Registration error"
            )

            messages.error(
                request,
                f"An unexpected error occurred: {e}"
            )

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


@login_required(login_url="accounts:login")
def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out."
    )

    return redirect("home")
