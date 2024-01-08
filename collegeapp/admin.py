from django.contrib import admin
from collegeapp.models import Course
from collegeapp.models import Student
from collegeapp.models import Usermember
# Register your models here.

admin.site.register(Course)

admin.site.register(Student)

admin.site.register(Usermember)