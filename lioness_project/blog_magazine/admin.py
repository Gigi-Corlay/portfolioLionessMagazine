from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category", 
        "author",
        "created_at",
        "published",
    )
    list_filter = (
        "category",
        "published",
        "created_at",
    )
    search_fields = (
        "title",
        "texte",
        "author",
    )
