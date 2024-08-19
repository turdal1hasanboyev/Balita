from django.db import models


class GetInTouch(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    phone = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    