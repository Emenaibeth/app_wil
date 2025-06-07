from django.db import models

class Nota(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenido[:50] # Mostrar los primeros 50 caracteres