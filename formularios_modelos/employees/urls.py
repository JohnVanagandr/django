from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('modificar/<int:id>/', views.modificar, name="modificar")
]
