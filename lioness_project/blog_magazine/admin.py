from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "created_at",
        "published",
    )

    list_filter = (
        "published",
        "created_at",
    )

    search_fields = (
    "title",
    "content",
    "author__username",
    "author__email",
    )
