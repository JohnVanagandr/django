from django import forms

class Contact(forms.Form):
  name = forms.CharField(
    label='Nombre',
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'input'}))
  email = forms.EmailField(
    label='Email',
    max_length=50,
    widget=forms.EmailInput(attrs={'class': 'input'}))
  coment = forms.CharField(
    widget=forms.Textarea(attrs={'class': 'input'})
  )

  def clean_name(self):
    name = self.cleaned_data.get("name")
    if name != 'Open':
      # Error
      raise forms.ValidationError('Solo se permite el valor Open para este campo')
    else:
      # Correcto
      return name

class Coment(forms.Form):
  name = forms.CharField(label='Escribe tu nombre', max_length=100, help_text='Maximo 100 caracteres')
  url = forms.URLField(label="Tu sitio web", required=False, initial='http://')
  coment = forms.CharField()