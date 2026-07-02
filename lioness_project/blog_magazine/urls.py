from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

app_name = "blog_magazine"

urlpatterns = [
    # Favicon (IMPORTANT : doit être dans la liste principale)
    path(
        "favicon.ico",
        RedirectView.as_view(url="/static/images/logo_favicon.png"),
    ),

    # Home blog (catégorie par défaut)
    path(
        "",
        views.articles_by_category,
        {"category_slug": "ACTUS"},
        name="blog_home"
    ),

    # Articles par catégorie
    path(
        "category/<str:category_slug>/",
        views.articles_by_category,
        name="category_articles"
    ),

    # Détail article
    path(
        "article/<int:id>/",
        views.article_detail,
        name="article_detail"
    ),
]

# MEDIA (OK)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
