from django.urls import path
from . import views


app_name = "blog_magazine"


urlpatterns = [
    path(
        "",
        views.article_list,
        name="blog"
    ),

    path(
        "article/<int:id>/",
        views.article_detail,
        name="article_detail"
    ),
]
