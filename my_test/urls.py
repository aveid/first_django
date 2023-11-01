from django.urls import path
from .views import get_fisrt_page, get_template_page

urlpatterns = [
    path("", get_fisrt_page),
    path("html/", get_template_page),
]