from django.views import generic
from django.http import JsonResponse,  HttpResponse
from rest_framework import views, status, parsers
from django.views.decorators.csrf import csrf_exempt

from .forms import CourseForm
from .serializers import CourseSerializer
from .models import Course


"""
    REST - Representational state transfer
    
    methods = GET, POST, PUT, PATH, DELETE ~ CRUD ops
    
    /courses/ ~ end point    
"""


@csrf_exempt
def courses_list(request):
    """
        List all courses or create a new course
    """
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(instance=courses, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = parsers.JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def courses_detail(request, pk):
    """
        Retrieve, update or delete a course
        /courses/1/
    """
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CourseSerializer(instance=course)
        return JsonResponse(data=serializer.data, status=200)
    elif request.method in {"PUT", "PATCH"}:
        data = parsers.JSONParser().parse(request)
        serializer = CourseSerializer(instance=course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    elif request.method == "DELETE":
        course.delete()
        return HttpResponse(status=204)


class CourseApiView(views.APIView):
    pass


class CourseCreateView(generic.CreateView):
    model = Course
    template_name = 'course.html'
    form_class = CourseForm
    success_url = '/courses/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.all()
        context["courses"] = courses
        return context