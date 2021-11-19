from rest_framework import serializers
from .models import Course
from schools_app.models import School


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    is_active = serializers.BooleanField(default=False)
    price = serializers.DecimalField(max_digits=14, decimal_places=2)
    duration = serializers.IntegerField(min_value=1, max_value=9)
    max_students = serializers.IntegerField(min_value=1, max_value=28)

    def create(self, validated_data):
        """create() method creates and returns a new Course instance"""
        # Course.objects.create(**validated_data)

        course = Course.objects.create(
            name=validated_data["name"],
            school=validated_data["school"],
            is_active=validated_data["is_active"],
            price=validated_data["price"],
            duration=validated_data["duration"],
            max_students=validated_data["max_students"]
        )
        return course

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.school = validated_data.get("school", instance.school)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.price = validated_data.get("price", instance.price)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.max_students = validated_data.get("max_students", instance.max_students)
        instance.save()
        return instance
