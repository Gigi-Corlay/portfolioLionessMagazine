from django.shortcuts import render, get_object_or_404
from .models import Article


def articles_by_category(request, category):
    articles = Article.objects.filter(
        category=category,
        published=True,
    ).order_by("-created_at")

    category_name = dict(Article.CATEGORY_CHOICES).get(
        category,
        category,
    )

    context = {
        "articles": articles,
        "category_name": category_name,
        "active_category": category,
    }

    return render(
        request,
        "blog_magazine/category_articles.html",
        context,
    )


def article_detail(request, id):
    article = get_object_or_404(
        Article,
        id=id,
        published=True,
    )

    return render(
        request,
        "blog_magazine/article_detail.html",
        {
            "article": article,
            "active_category": article.category,
        },
    )
