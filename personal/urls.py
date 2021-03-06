from django.urls import path
from . import views

urlpatterns = [
    path("lista_personal/", views.personal, name="personal"),
]
