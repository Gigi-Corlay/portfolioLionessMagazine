from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    CATEGORY_CHOICES = [
        ("ACTUS", "ACTUS"),
        ("MOOD", "MOOD"),
        ("AGENDA", "AGENDA"),
        ("BUSINESS", "BUSINESS"),
        ("INVITÉ", "INVITÉ"),
        ("FOCUS", "FOCUS"),
        ("COVER", "COVER"),
        ("BIEN-ÊTRE", "BIEN-ÊTRE"),
        ("ET SI ON EN PARLAIT ?", "ET SI ON EN PARLAIT ?"),
        ("LIFESTYLE", "LIFESTYLE"),
        ("IMPACTFUL", "THE MOST IMPACTFUL PERSONALITIES"),
    ]

    title = models.CharField(
        max_length=255,
        verbose_name="Title",
    )

    author = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Author",
    )

    image = models.ImageField(
        upload_to="articles/",
        blank=True,
        null=True,
        verbose_name="Featured image",
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="ACTUS",
    )

    chapo = RichTextField(
        blank=True,
        null=True,
        verbose_name="Introduction",
    )

    texte = RichTextField(
        verbose_name="Article",
    )

    published = models.BooleanField(
        default=True,
        verbose_name="Published",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title
