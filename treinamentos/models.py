from django.db import models

class Treinamentos(models.Model):
    titulo = models.TextField(verbose_name='Título', null=True, blank=True)
    topico1 = models.TextField(verbose_name='Tópico-1', null=True, blank=True)
    texto1 = models.TextField(verbose_name='Texto-1', null=True, blank=True)
    topico2 = models.TextField(verbose_name='Tópico-2', null=True, blank=True)
    texto2 = models.TextField(verbose_name='Texto-2', null=True, blank=True)
    topico3 = models.TextField(verbose_name='Tópico-3', null=True, blank=True)
    texto3 = models.TextField(verbose_name='Texto-3', null=True, blank=True)
    topico4 = models.TextField(verbose_name='Tópico-4', null=True, blank=True)
    texto4 = models.TextField(verbose_name='Texto-4', null=True, blank=True)
    topico5 = models.TextField(verbose_name='Tópico-5', null=True, blank=True)
    texto5 = models.TextField(verbose_name='Texto-5', null=True, blank=True)
    topico6 = models.TextField(verbose_name='Tópico-6', null=True, blank=True)
    texto6 = models.TextField(verbose_name='Texto-6', null=True, blank=True)
    topico7 = models.TextField(verbose_name='Tópico-7', null=True, blank=True)
    texto7 = models.TextField(verbose_name='Texto-7', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.titulo)

