from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __sizeof__(self):
        return self.name
