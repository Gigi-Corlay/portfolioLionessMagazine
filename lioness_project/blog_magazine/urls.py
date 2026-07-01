from django.urls import path
from . import views

app_name = "blog_magazine"

urlpatterns = [
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