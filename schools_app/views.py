"""
from django.shortcuts import render
from django.views import generic
from .models import School
from .forms import SchoolForm



class SchoolCreateView(generic.CreateView):
    model = School
    template_name = 'schools_app.html'
    form_class = SchoolForm
    success_url = '/schools/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schools = School.objects.all()
        context["schools"] = schools
        return context
"""
