from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blog_magazine.models import Article


@login_required
def dashboard_view(request):

    articles = Article.objects.filter(
        published=True
    ).order_by("-created_at")[:3]


    return render(
        request,
        "dashboard/dashboard.html",
        {
            "articles": articles
        }
    )
    