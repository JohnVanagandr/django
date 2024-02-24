from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', views.saludar, name='saludar'),
    path('despedirnos/', views.despedirnos, name='despedirnos'),
    path('persona/<int:edad>/', views.persona, name='persona')
]
