"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path("dashboard/", include("dashboard.urls")),
    path("password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
