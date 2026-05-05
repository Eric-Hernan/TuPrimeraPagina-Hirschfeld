from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('pages/', views.lista_libros, name='lista_libros'), 
    path('pages/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('pages/<int:pk>/editar/', views.editar_libro, name='editar_libro'),
    path('pages/<int:pk>/borrar/', views.LibroDeleteView.as_view(), name='borrar_libro'),
    path('about/', views.about, name='about'),

  
    path('agregar-libro/', views.LibroCreateView.as_view(), name='agregar_libro'),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
    path('agregar-amigo/', views.agregar_amigo, name='agregar_amigo'),
    path('registrar-prestamo/', views.registrar_prestamo, name='registrar_prestamo'),
]