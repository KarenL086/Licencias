from django.urls import path
from . import views
#from .views import CustomPasswordResetView, generate_pdf, limpiar_busqueda, limpiar_busqueda1

urlpatterns = [
    path('', views.inicio, name='inicio'),
    #path('ayudaUsuario/', views.ayudaUsuario, name='ayudaUsuario'),
]