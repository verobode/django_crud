from django.db import models

# Create your models here where we're going to selec the id, titulo, imagen y descripción

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen= models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripción', null=True)

#Al modificar un campo hacer python manage.py makemigration, y luego migrate para actualizar.

    def __str__(self):
        fila = "Título: " + self.titulo + " - " + "Descripción: " + self.descripcion
        return fila
    
    # Delete image: delete from storage according to the name.
    # Toma la imagen, accede al storage y la elimina
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

