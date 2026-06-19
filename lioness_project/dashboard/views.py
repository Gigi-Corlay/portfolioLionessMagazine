from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blog_magazine.models import Article


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
