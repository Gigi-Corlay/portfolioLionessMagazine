from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .forms import ProfileForm
import logging

from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile

logger = logging.getLogger(__name__)


@login_required(login_url="accounts:login")
def profile_view(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("accounts:profile")

    else:

        form = ProfileForm(instance=profile)

    return render(
        request,
        "accounts/profile.html",
        {"form": form}
    )


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

            return redirect("dashboard:dashboard")

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

                Profile.objects.create(
                    user=user,
                    country=form.cleaned_data.get("country"),
                    occupation=form.cleaned_data.get("occupation")
                )

            login(request, user)

            messages.success(
                request,
                "Account successfully created."
            )

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


@login_required
def profile_view(request):
    # On récupère le profil de l'utilisateur connecté grâce à la relation OneToOne
    profile = request.user.profile 

    if request.method == 'POST':
        # instance=profile permet de mettre à jour le profil existant au lieu d'en créer un nouveau
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile') # Redirige vers la page de profil pour voir les changements
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile/profile.html', {'form': form})