from django.shortcuts import render
from .models import Depto
# Create your views here.
def hola_mundo(request):
    #return HttpResponse("Hola Mundo")
    template = "departamento/hola_mundo.html"
    contexto = {
         "nombre":"Pedro",
        "numero":1234
    }
    return render(request, template, contexto)

def deptos(request):
        lista_depto = Depto.objects.all()
        return render(request, "departamento/depto.html",{"lista_depto":lista_depto})
