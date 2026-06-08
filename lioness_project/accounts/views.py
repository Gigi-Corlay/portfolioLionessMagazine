from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm
from .models import Profile


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():

            user = form.save(commit=False)

            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]

            # si tu veux te connecter avec l'email
            user.username = form.cleaned_data["email"]

            user.save()

            Profile.objects.create(
                user=user,
                country=form.cleaned_data["country"],
                occupation=form.cleaned_data["occupation"]
            )

            login(request, user)

            return redirect("home")

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def logout_view(request):
    logout(request)
    return redirect("home")
