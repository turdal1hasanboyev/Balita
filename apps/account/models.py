from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    avatar = models.ImageField(upload_to="Avatars/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.username
    