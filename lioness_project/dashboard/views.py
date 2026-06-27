from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
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
            "label": _("Articles read"),
            "count": 0,
        },
        {
            "icon": "fa-solid fa-book-open",
            "label": _("Magazine issues"),
            "count": Article.objects.filter(published=True).count(),
        },
        {
            "icon": "fa-regular fa-bookmark",
            "label": "Saved articles",   # ⚠️ NE PAS traduire, voir explication ci-dessous
            "count": 0,
        },
        {
            "icon": "fa-regular fa-comment",
            "label": "Comments",         # ⚠️ NE PAS traduire, voir explication ci-dessous
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
