from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, "inicio/inicio.html",{})

def inicio_privado(request):
	return render(request, "inicio/inicio_privado.html", {})