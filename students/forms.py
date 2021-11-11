from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'school', 'is_active', 'is_graduated']

    def __str__(self):
        return self.name
