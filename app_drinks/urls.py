from django.urls import path
from app_drinks.views import home


urlpatterns = [
    path('', home),
]
