from django.urls import path
from . import views

urlpatterns = [
    path("lista_personas/", views.persona, name="persona"),
]
