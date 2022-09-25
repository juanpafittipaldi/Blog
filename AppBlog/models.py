from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    cuerpo=models.CharField(max_length=2000)
