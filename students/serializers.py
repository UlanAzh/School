from rest_framework import serializers
from .models import Student
from schools_app.models import School


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    date_of_birth = serializers.DateField()
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    is_active = serializers.BooleanField(default=False)
    is_graduated = serializers.BooleanField(default=False)


def create(self, validated_data):
    Student.objects.create(**validated_data)
    return course


def update(self, instance, validated_data):
    instance.name = validated_data.get("name", instance.name)
    instance.date_of_birth = validated_data.get("date_of_birth", instance.date_of_birth)
    instance.school = validated_data.get("school", instance.school)
    instance.is_active = validated_data.get("is_active", instance.is_active)
    instance.is_graduated = validated_data.get("is_graduated", instance.is_graduated)
    instance.save()
    return instance
