from django.urls import path
from . import views

urlpatterns = [
    path("welcome", views.welcome),
    path("register", views.register),
    path("login",views.login),
    path("field",views.field),
    path("Sinfo",views.getStudentInformation),
    path("marks",views.marks),
    path("aadhar",views.aadhar),
    path("regii",views.regii),
]