from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    country = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    occupation = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["user__first_name"]

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()

        return self.user.email or self.user.username
