from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nombre de Usuario'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Creación'
    )

    class Meta:
        db_table = 'usuarios'
        ordering = ['-fecha_creacion']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre_usuario
