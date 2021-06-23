
from .views import get_characater_with_name
from django.urls import path

urlpatterns = [
    path('get_character_with_name', get_characater_with_name)
]
