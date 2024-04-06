from django.shortcuts import render
from django.http import HttpResponse
from .form import Contact

def form(request):
  # contac_form = Contact({'name': 'John Becerra', 'url': 'http://www.sena.edu.co', 'coment': 'esto es un comentario'})
  form = Contact()
  return render(request, 'form.html', {
    'form': form
  })

def widget(request):
  if request.method == 'GET':
    form = Contact()
    return render(request, 'form.html', {
    'form': form
  })

  if request.method == 'POST':
    form = Contact(request.POST)
    if form.is_valid():
      # Acciones a realizar si todo esta bien
      return HttpResponse('Validos')
    else:
      # Acciones a realizar si algun dato no es valido
      # return HttpResponse('No validos')
      return render(request, 'form.html', {'form': form })