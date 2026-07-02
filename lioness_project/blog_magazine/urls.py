from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog_magazine"

urlpatterns = [
    # Accueil (ACTUS)
    path(
        "",
        views.articles_by_category,
        {"category": "ACTUS"},
        name="blog_home",
    ),

    # Articles par catégorie
    path(
        "category/<str:category>/",
        views.articles_by_category,
        name="category_articles",
    ),

    # Détail d'un article
    path(
        "article/<int:id>/",
        views.article_detail,
        name="article_detail",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
