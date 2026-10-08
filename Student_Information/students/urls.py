from django.urls import path
from . import views

app_name = "students"
urlpatterns = [
    path("", views.student_form, name="form"),
    path("results/", views.student_results, name="results"),
]
