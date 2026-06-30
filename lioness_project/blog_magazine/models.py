from django.db import models
from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    # Les rubriques officielles issues de la maquette Lioness
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
    author = models.CharField(max_length=150, blank=True)
    chapo = RichTextField(blank=True, null=True)
    texte = RichTextField()
    image = models.ImageField(upload_to="articles/", blank=True, null=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='ACTUS'
    )

    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
