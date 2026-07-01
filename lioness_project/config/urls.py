from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("i18n/", include("django.conf.urls.i18n")),

    path("", include("core.urls")),
    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("blog/", include("blog_magazine.urls")),

    # Password reset
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

    # Legal pages
    path(
        "legal-notice/",
        TemplateView.as_view(template_name="legals_notices/legal_notice.html"),
        name="legal_notice",
    ),
    path(
        "privacy-policy/",
        TemplateView.as_view(template_name="legals_notices/privacy_policy.html"),
        name="privacy_policy",
    ),
    path(
        "terms-of-use/",
        TemplateView.as_view(template_name="legals_notices/terms_of_use.html"),
        name="terms_of_use",
    ),
    path(
        "cookie-policy/",
        TemplateView.as_view(template_name="legals_notices/cookie_policy.html"),
        name="cookie_policy",
    ),
]

# =====================================================
# ONLY FOR LOCAL DEVELOPMENT
# =====================================================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
