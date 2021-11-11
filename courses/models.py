from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey('schools_app.School', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    duration = models.IntegerField()
    max_students = models.IntegerField()

    def __str__(self):
        return self.name
