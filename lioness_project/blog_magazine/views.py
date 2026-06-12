from django.shortcuts import render, get_object_or_404
from .models import Article


def articles_by_category(request, category_slug):
    # Récupération des articles publiés filtrés par la catégorie choisie
    articles = Article.objects.filter(category=category_slug, published=True).order_by("-id")

    # Récupération du nom propre de la catégorie pour l'affichage du titre h1
    category_name = dict(Article.CATEGORY_CHOICES).get(category_slug, category_slug.upper())

    return render(
        request,
        "blog_magazine/category_articles.html",
        {
            "articles": articles,
            "category_name": category_name,
            "category_slug": category_slug,
        }
    )

def article_detail(request, id):
    # Vue de la page de l'article seul
    article = get_object_or_404(Article, id=id)
    return render(
        request,
        "blog_magazine/article_detail.html",
        {"article": article}
    )
