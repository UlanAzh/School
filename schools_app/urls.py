from django.urls import path
from .views import SchoolCreateView


urlpatterns = [
    path("create/", SchoolCreateView.as_view()),
]