from django.contrib import admin
from api.models import Article, Student
# Register your models here.
admin.site.register(Article)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
