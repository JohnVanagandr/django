from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.test, name="contacto"),
  path('create/', views.create, name="create"),
  path('delete/', views.delete, name="delete")
]
