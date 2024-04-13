from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def index(request):
  data = {
    'form': EmployeeForm()
  }
  if request.method == 'POST':
    formulario = EmployeeForm(request.POST, files=request.FILES)
    if formulario.is_valid():
      # Guardamos la información
      formulario.save()
      data['mensaje'] = "Datos guardados correctamente"
      data['form'] = formulario
      return render(request, 'index.html', data)
  else:
    return render(request, 'index.html', data)

def modificar(request, id):
  empleado = Employee.objects.get(id=id)
  data = {
    'form': EmployeeForm(instance=empleado)
  }
  if request.method == "POST":
    formulario = EmployeeForm(data=request.POST, instance=empleado, files=request.FILES)
    if formulario.is_valid():
      formulario.save()
      data['mensaje'] = "Empleado actualizado"
  return render(request, 'index.html', data)
