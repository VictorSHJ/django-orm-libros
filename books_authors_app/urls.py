from django.urls import path
from . import views
urlpatterns = [
    path('', views.procesar_libros),
    path('autores/', views.procesar_autores),
    path('procesar_autores/', views.procesar_autores),
    path('authors/<int:id>', views.detalle_autores),
    path('authors/agregar_libro/', views.agregar_libro),
    path('libros/', views.procesar_libros),
    path('procesar_libros/', views.procesar_libros),
    path('books/<int:id>', views.detalle_libros),
    path('books/agregar_autor/', views.agregar_autor),
]