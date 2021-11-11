from django.views import generic
from .models import Student
from .forms import StudentForm


class StudentCreateView(generic.CreateView):
    model = Student
    template_name = 'student.html'
    form_class = StudentForm
    success_url = 'home'
