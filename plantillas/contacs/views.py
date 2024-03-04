from django.shortcuts import render
from django.http import HttpResponse
from .models import Contac

# Create your views here.
def test(requets):
  return HttpResponse("Funciona mi nuevo modulo")

def create(requets):
  coment = Contac(name="John Becerra", phone="3160410637", email="jfbeccera@gmail.com", messaje="mensaje de prueba")
  coment.save()
  return HttpResponse("Guardar formulario")

def delete(request):
  #consultamos el objeto
  contac = Contac.objects.get(id=2)
  contac.delete()
  return HttpResponse("Contacto eliminado en la prueba")