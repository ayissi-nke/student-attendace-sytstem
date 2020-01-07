from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Teachers(models.Model):
    user = models.ForeignKey(User, on_delete="models.CASCADE")


class Student(models.Model):
    matricule = models.CharField(max_length=40, primary_key=True)
    level = models.IntegerField()
    user = models.ForeignKey(User, on_delete="models.CASCADE")

    def __str__(self):
        return str(self.matricule)


class Courses(models.Model):
    course_code = models.CharField(max_length=64, primary_key=True)
    title = models.CharField(max_length=30)
    level = models.IntegerField()
    teachers = models.ForeignKey(Teachers, on_delete="models.CASCADE")

    def __str__(self):
        return str(self.course_code)


class StudentCourses(models.Model):
    course_code = models.ForeignKey(Courses, on_delete="models.CASCADE")
    st_mtrl = models.ForeignKey(Student, on_delete="models.CASCADE")


class Record(models.Model):
    st_mtrl = models.ForeignKey(Student, on_delete="models.CASCADE")
    course_code = models.ForeignKey(Courses, on_delete="models.CASCADE", null=True)
    status = models.BooleanField()
    date = models.DateTimeField(default=datetime.now())
