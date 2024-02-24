from django.http import HttpResponse

def saludar(requets):
  return HttpResponse("Hola muchachos")

def despedirnos(request):
  return HttpResponse("Adios muchachos")

def persona(requets, edad):
  if edad >= 18:
    return HttpResponse("Eres mayor de edad")
  else:
    return HttpResponse("No eres mayor de edad")