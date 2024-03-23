from django.shortcuts import render
from django.http import HttpResponse

def getform(request):
  return render(request, 'form.html', {})

def getgoal(request):
  if request.method != 'GET':
    return HttpResponse("El metodo Post no es soportado")
  
  firs_name = request.GET['firs_name']
  last_name = request.GET['last_name']
  return render(request, 'success.html', {
    'firs_name' : firs_name,
    'last_name' : last_name
  })

def posform(request):
  return render(request, 'form.html', {})

def posgoal(request):
  if request.method != 'POST':
    return HttpResponse("El metodo Get no es soportado")
  firs_name = request.POST['firs_name']
  last_name = request.POST['last_name']
  return render(request, 'success.html', {
    'firs_name' : firs_name,
    'last_name' : last_name
  })