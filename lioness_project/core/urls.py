from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('legal-notice/', views.legal_notice, name='legal_notice'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),
]
