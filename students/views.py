from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse,  HttpResponse
from rest_framework import views, status, parsers, response
from django.views.decorators.csrf import csrf_exempt
from .models import Student, StudentCourse
from .forms import StudentForm, StudentCourseForm
from .serializers import StudentSerializer



# @csrf_exempt
# def students_list(request):
#
#     if request.method == "GET":
#         students = Students.objects.all()
#         serializer = StudentSerializer(many=True, instance=students)
#         return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         data = parsers.JSONParser().parse(request)
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @csrf_exempt
# def students_detail(request, pk):
#     try:
#         student = Student.objects.get(id=pk)
#     except Student.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == "GET":
#         serializer = StudentSerializer(instance=student)
#         return JsonResponse(data=serializer.data, status=200)
#     elif request.method in {"PUT", "PATCH"}:
#         data = parsers.JSONParser().parse(request)
#         serializer = StudentSerializer(instance=student, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, status=200)
#         return JsonResponse(data=serializer.errors, status=400)
#     elif request.method == "DELETE":
#         student.delete()
#         return HttpResponse(status=204)


class StudentListApiView(views.APIView):

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(many=True, instance=students)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exeption=True)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)


class StudentDetailAPIView(views.APIView):

    def get_object(self, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return HttpResponse(status=404)
        return student

    def get(self, request, pk, *args, **kwargs):
        student = self.get_object(pk=pk)
        serializer = StudentSerializer(instance=student)
        return JsonResponse(data=serializer.data, status=200)

    def patch(self, request, pk, *args, **kwargs):
        student = self.get_object(pk=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return response.Response(data=serializer.data, status=200)
        return response.Response(data=serializer.errors, status=400)

    def delete(self, request, pk, *args, **kwargs):
        student = self.get_object(pk=pk)
        student.delete()
        return HttpResponse(status=204)


class StudentCreateView(generic.CreateView):
    model = Student
    template_name = 'student.html'
    form_class = StudentForm
    success_url = '/student/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = Student.objects.all()
        context["students"] = students
        return context


class StudentCourseCreateView(generic.CreateView):
    model = StudentCourse
    form_class = StudentCourseForm
    template_name = 'studentcourse.html'
    success_url = '/studentcouse/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = StudentCourse.objects.all()
        context["students"] = students
        return context
