from django.http import HttpResponse
from django.shortcuts import render
from itsdangerous import Serializer
from sympy import im
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

# function based view

# model object - single student data


def Student_detail(request):
    stu = Student.objects.all()  # complex data
    print(stu)
    serializer = StudentSerializer(stu, many=True)  # python data
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')
