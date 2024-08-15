from django.urls import path

from apps.contact.views import get_in_touch


urlpatterns = [
    path('contact/', get_in_touch, name="contact"),
]
