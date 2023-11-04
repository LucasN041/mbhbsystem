from django.db import models

class Documentos(models.Model):
    titulo = models.TextField(verbose_name='Título', null=True, blank=True)
    texto1 = models.TextField(verbose_name='Texto-1', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.titulo)
