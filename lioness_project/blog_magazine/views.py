from django.shortcuts import render, get_object_or_404
from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by("-id")

    return render(
        request,
        "blog_magazine/article_list.html",
        {
            "articles": articles
        }
    )


def article_detail(request, id):
    article = get_object_or_404(
        Article,
        id=id
    )

    return render(
        request,
        "blog_magazine/article_detail.html",
        {
            "article": article
        }
    )
