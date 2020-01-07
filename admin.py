from django.contrib import admin

from .models import *

admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(Record)
admin.site.register(StudentCourses)
admin.site.register(Teachers)
# Register your models here.
