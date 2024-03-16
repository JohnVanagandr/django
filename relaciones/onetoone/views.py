from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.
def create(request):
  #Creamos un lugar
  place = Place(name="Centro", address="Calle 21 # 15 - 45")
  place.save()
  #Creamos un restaurante
  restaurant = Restaurant(place=place, employees=25)
  restaurant.save()
  return HttpResponse(restaurant.place.address)