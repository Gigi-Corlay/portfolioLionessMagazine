from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",  # Affiché dans la liste
        "author",
        "created_at",
        "published",
    )
    list_filter = (
        "category",  # Permet de filtrer par catégorie dans l'admin
        "published",
        "created_at",
    )
    search_fields = (
        "title",
        "content",
        "author",
    )
