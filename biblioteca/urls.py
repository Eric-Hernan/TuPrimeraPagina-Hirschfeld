from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'), # La página principal vacía
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
]

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    path('buscar/', views.buscar_libro, name='buscar_libro'), # <--- Esta es la nueva
]

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
    path('agregar-amigo/', views.agregar_amigo, name='agregar_amigo'),
    path('registrar-prestamo/', views.registrar_prestamo, name='registrar_prestamo'),
]