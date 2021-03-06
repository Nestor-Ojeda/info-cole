from django.urls import path
from . import views

urlpatterns = [
    path("lista_contactos/", views.contactos, name="contactos"),
]
