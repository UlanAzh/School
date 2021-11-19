from django.urls import path
# from .views import StudentCreateView, StudentCourseCreateView, \
from .views import StudentListApiView, StudentDetailAPIView

urlpatterns = [
    path("students/", StudentListApiView.as_view(), name="student_list"),
    # path("students/<int:pk>/", students_detail, name="student-detail"),
    path("students/<int:pk>/", StudentDetailAPIView.as_view(), name="student-detail"),
]