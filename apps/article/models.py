from django.db import models

from django.template.defaultfilters import slugify  # new
from django.urls import reverse

from apps.account.models import Account


class Category(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self) -> str:
        return self.title   


class Article(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # OneToMany
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image_1 = models.ImageField(upload_to='Article/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='Article/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='Article/', null=True, blank=True)
    for_banner = models.BooleanField(default=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    