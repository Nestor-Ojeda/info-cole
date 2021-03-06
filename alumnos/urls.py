from django.urls import path
from . import views

urlpatterns = [
    path("lista_alumnos/", views.alumnos, name="alumnos"),
]
