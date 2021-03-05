from django.urls import path
from . import views

app_name = "departamento"
urlpatterns = [
    path("hola_mundo/", views.hola_mundo, name="hola_mundo"),
    path("deptos", views.deptos, name="deptos"),
]