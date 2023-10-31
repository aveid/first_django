from django.urls import path
from .views import get_fisrt_page

urlpatterns = [
    path("", get_fisrt_page),
]