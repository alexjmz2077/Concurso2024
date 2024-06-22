from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField('Usuario', max_length=100)
    nombres = models.CharField('Nombres', max_length=100)
    contraseña = models.CharField('Contraseña',max_length=100)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username