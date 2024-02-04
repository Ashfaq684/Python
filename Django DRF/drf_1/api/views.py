from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from .models import Student

# Create your views here.

# Model Object - Single Student Data
def student_detail(request, pk):
    student = Student.objects.get(id = pk)
    serializer = StudentSerializer(student)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# Query Set - All Student Data
def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)