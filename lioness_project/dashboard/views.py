from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blog_magazine.models import Article
from django.db.models import Q


@login_required
def dashboard_view(request):

    articles = Article.objects.filter(
        published=True
    ).order_by("-created_at")[:3]

    activities = [
        {
            "icon": "fa-regular fa-file-lines",
            "label": "Articles read",
            "count": 0,
        },
        {
            "icon": "fa-solid fa-book-open",
            "label": "Magazine issues",
            "count": Article.objects.filter(published=True).count(),
        },
        {
            "icon": "fa-regular fa-bookmark",
            "label": "Saved articles",
            "count": 0,
        },
        {
            "icon": "fa-regular fa-comment",
            "label": "Comments",
            "count": 0,
        },
    ]

    context = {
        "activities": activities,
        "articles": articles,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )


@login_required
def dashboard_search(request):

    query = request.GET.get("q", "")
    results = []

    if query:
        results = Article.objects.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query)
        ).order_by("-created_at")

    return render(
        request,
        "dashboard/search_results.html",
        {
            "query": query,
            "results": results,
        }
    )
