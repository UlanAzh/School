from django.urls import path
from .views import StudentCreateView


urlpatterns = [
    path("create/", StudentCreateView.as_view()),
]