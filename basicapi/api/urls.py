from django import views
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('student_detail/', views.Student_detail),


]
