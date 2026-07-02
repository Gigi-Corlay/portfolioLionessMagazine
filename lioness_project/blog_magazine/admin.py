from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "author",
        "published",
        "created_at",
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

    ordering = ("-created_at",)

    list_per_page = 20

    date_hierarchy = "created_at"

    list_editable = (
        "published",
    )

    readonly_fields = (
        "created_at",
    )

    fieldsets = (
        (
            "Article",
            {
                "fields": (
                    "title",
                    "category",
                    "author",
                    "image",
                    "chapo",
                    "texte",
                )
            },
        ),
        (
            "Publication",
            {
                "fields": (
                    "published",
                    "created_at",
                )
            },
        ),
    )
