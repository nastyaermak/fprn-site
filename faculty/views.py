from django.shortcuts import get_object_or_404, render

from .models import Department, FacultyInfo, Program, ukrainian_sort_key


def home(request):
    info = FacultyInfo.objects.first()
    return render(request, "faculty/home.html", {"info": info})


def program_list(request):
    programs = Program.objects.select_related("department")
    return render(request, "faculty/program_list.html", {"programs": programs})


def program_detail(request, pk):
    program = get_object_or_404(Program.objects.select_related("department"), pk=pk)
    return render(request, "faculty/program_detail.html", {"program": program})


def department_list(request):
    departments = Department.objects.prefetch_related("programs")
    return render(request, "faculty/department_list.html", {"departments": departments})


def department_detail(request, pk):
    department = get_object_or_404(
        Department.objects.prefetch_related("programs", "teachers"), pk=pk
    )
    teachers = sorted(department.teachers.all(), key=lambda teacher: ukrainian_sort_key(teacher.name))
    return render(
        request,
        "faculty/department_detail.html",
        {"department": department, "teachers": teachers},
    )
