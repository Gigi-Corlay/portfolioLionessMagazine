from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Article(models.Model):

    CATEGORY_CHOICES = [
        ('ACTUS', 'ACTUS'),
        ('MOOD', 'MOOD'),
        ('AGENDA', 'AGENDA'),
        ('BUSINESS', 'BUSINESS'),
        ('INVITÉ', 'INVITÉ'),
        ('FOCUS', 'FOCUS'),
        ('COVER', 'COVER'),
        ('BIEN-ÊTRE', 'BIEN-ÊTRE'),
        ('ET SI ON EN PARLAIT ?', 'ET SI ON EN PARLAIT ?'),
        ('LIFESTYLE', 'LIFESTYLE'),
        ('IMPACTFUL', 'THE MOST IMPACTFUL PERSONALITIES'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    author = models.CharField(max_length=150, blank=True)

    chapo = RichTextField(blank=True, null=True)
    texte = RichTextField()

    image = models.ImageField(
        upload_to="articles/",
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='ACTUS'
    )

    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            # évite doublons de slug (IMPORTANT en production)
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
