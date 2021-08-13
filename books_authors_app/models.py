from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    descri = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  # autores : Lista de autores que tiene un libro

    def __repr__(self):
        return f"Nombre Libro: {self.titulo}, Descripción:{self.descri}"
    def __str__(self):
        return f"nombre libro: {self.titulo}, descripción:{self.descri}"

class Autor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notas = models.CharField(max_length=255)
    libros = models.ManyToManyField(Libro, related_name="autores")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Autor: {self.first_name} {self.last_name}"
    def __str__(self):
        return f"autor: {self.first_name} {self.last_name}"
