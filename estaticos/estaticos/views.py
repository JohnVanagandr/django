from django.shortcuts import render

def estaticos(requets):
  return render(requets, 'estaticos.html', {})