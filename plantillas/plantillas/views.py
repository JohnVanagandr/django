from django.shortcuts import render

def inicio(requets):
  return render(requets, 'index.html', {})

def nosotros(requets):
  return render(requets, 'nosotros.html', {})

def servicios(requets):
  return render(requets, 'servicios.html', {})

def contacto(requets):
  return render(requets, 'contacto.html', {})
