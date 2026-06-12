from django.db import models

class Article(models.Model):
    # Les 9 catégories officielles issues de la maquette Lioness
    CATEGORY_CHOICES = [
        ('news', 'News'),
        ('mood', 'Mood'),
        ('agenda', 'Agenda Business'),
        ('guest', 'Guest Focus'),
        ('cover', 'Cover'),
        ('well_being', 'Well-being'),
        ('what_if', 'What if we talked about it ?'),
        ('lifestyle', 'Lifestyle'),
        ('impactful', 'The Most Impactful Personalities'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=150, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="articles/", blank=True, null=True)

    # Ajout du champ catégorie
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='news'
    )

    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
