from django.urls import path

from apps.article.views import index, article_detail, category_view


urlpatterns = [
    path('', index),
    path('detail/<slug:slug>/', article_detail, name="detail"),
    path('category/<slug:slug>/', category_view, name="category"),
]
