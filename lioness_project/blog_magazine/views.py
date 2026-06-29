from django.shortcuts import render, get_object_or_404
from .models import Article


def articles_by_category(request, category_slug):
    articles = Article.objects.filter(category=category_slug, published=True).order_by("-id")
    category_name = dict(Article.CATEGORY_CHOICES).get(category_slug, category_slug.upper())
    return render(
        request,
        "blog_magazine/category_articles.html",
        {
            "articles": articles,
            "category_name": category_name,
            "category_slug": category_slug,
            "active_category": category_slug,
        }
    )


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog_magazine/article_detail.html', {
        'article': article,
        'active_category': article.category,
    })
