from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import StyledPasswordChangeForm

app_name = "accounts"

urlpatterns = [

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "register/",
        views.register_view,
        name="register"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    path(
        "profile/",
        views.profile_view,
        name="profile"
    ),

    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change.html"
        ),
        name="password_change",
    ),

    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
    ),

    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change.html",
            form_class=StyledPasswordChangeForm,
        ),
        name="password_change",
    ),
]
