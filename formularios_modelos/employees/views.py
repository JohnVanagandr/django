from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm

# Create your views here.
def index(request):
  # return HttpResponse('Correcto')
  if request.method == 'POST':
    form = EmployeeForm(request.POST)
    if form.is_valid():
      # Guardamos la informacion
      form.save()
      return render(request, 'index.html', {'form': form })
  else:
    form = EmployeeForm()
    return render(request, 'index.html', {
      'form': form
    })