
from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Posteo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500)
    contenido = RichTextField(blank=True, null=True)
    imagen_posteo = models.ImageField(blank=True, null=True, upload_to='media/')
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_publicado = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicado = timezone.now()
        self.save()

<<<<<<< HEAD
    def __str__(self):
        return self.titulo
=======
# Create your models here.
class Blog(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    cuerpo=models.CharField(max_length=2000)
>>>>>>> 590e3063093a3e4f85b7adfda9fc913212890b1c
