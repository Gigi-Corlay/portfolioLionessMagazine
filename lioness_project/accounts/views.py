from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction

from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile


@login_required
def profile_view(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("profile")

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

            user = form.get_user()

            login(request, user)

            messages.success(
                request,
                "Welcome back!"
            )

            return redirect("dashboard")

        else:

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

    form = RegisterForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            try:

                with transaction.atomic():

                    user = form.save(commit=False)

                    user.username = form.cleaned_data["email"]
                    user.email = form.cleaned_data["email"]
                    user.first_name = form.cleaned_data["first_name"]
                    user.last_name = form.cleaned_data["last_name"]

                    user.save()

                    Profile.objects.create(
                        user=user,
                        country=form.cleaned_data["country"],
                        occupation=form.cleaned_data["occupation"]
                    )

                login(request, user)

                messages.success(
                    request,
                    "Account successfully created."
                )

                return redirect("dashboard")

            except Exception as e:

                print("=" * 50)
                print("ERREUR INSCRIPTION")
                print(e)
                print("=" * 50)

                messages.error(
                    request,
                    str(e)
                )

        else:

            print("FORM ERRORS :", form.errors)

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out."
    )

    return redirect("home")
