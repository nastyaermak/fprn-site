from django.contrib import admin

from .models import Department, FacultyInfo, Program, Teacher

admin.site.register(FacultyInfo)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Teacher)
