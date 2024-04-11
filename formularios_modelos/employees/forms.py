from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
  class Meta:
    model = Employee
    # Los campos que deseamos se muestren en el formulario
    # fields = ['first_name', 'last_name', 'email']
    # Mostramos todos los campos del formulario
    fields = '__all__'
    # Agregamos campos extras al formulario
    # extra_fields = ['password', 'password_confirm']
