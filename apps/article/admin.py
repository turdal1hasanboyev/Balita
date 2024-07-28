from django.contrib import admin

from apps.article.models import Category, Tag, Article, Comment


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Comment)
