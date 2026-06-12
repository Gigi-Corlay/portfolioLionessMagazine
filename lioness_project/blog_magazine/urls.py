from django.urls import path
from . import views

app_name = "blog_magazine"

urlpatterns = [
    # C'est cette ligne avec le name="blog_home" qui va sauver ton tableau de bord !
    path("", views.articles_by_category, {"category_slug": "news"}, name="blog_home"),

    path("category/<str:category_slug>/", views.articles_by_category, name="category_articles"),
    path("article/<int:id>/", views.article_detail, name="article_detail"),
]
