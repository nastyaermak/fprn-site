from django.urls import path

from . import views

app_name = "exchange"

urlpatterns = [
    path("", views.program_list, name="program-list"),
]
