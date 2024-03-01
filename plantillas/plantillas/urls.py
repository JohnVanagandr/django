from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',           views.inicio, name='inicio' ),
    path('nosotros/',  views.nosotros, name='nosotros' ),
    path('servicios/', views.servicios, name='servicios' ),
    path('contacto/',  views.contacto, name='contacto' ),
]
