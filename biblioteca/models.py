from django.db import models

class Amigo(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100) #aca irian los generos

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
class Prestamo(models.Model):
        libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
        amigo = models.ForeignKey(Amigo, on_delete=models.CASCADE)
        fecha_prestamo = models.DateField(auto_now_add=True)

        def __str__(self):
             return f"{self.libro.titulo} prestado a {self.amigo.nombre}"