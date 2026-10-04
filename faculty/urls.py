from django.urls import path

from . import views

app_name = "faculty"

urlpatterns = [
    path("", views.home, name="home"),
    path("programs/", views.program_list, name="program-list"),
    path("programs/<int:pk>/", views.program_detail, name="program-detail"),
    path("departments/", views.department_list, name="department-list"),
    path("departments/<int:pk>/", views.department_detail, name="department-detail"),
]
