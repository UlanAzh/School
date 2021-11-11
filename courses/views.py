from django.views import generic
from .models import Course
from .forms import CourseForm


class CourseCreateView(generic.CreateView):
    model = Course
    template_name = 'course.html'
    form_class = CourseForm
    success_url = 'home'
