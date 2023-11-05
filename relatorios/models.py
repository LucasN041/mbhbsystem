from django.db import models
from users.models import CustomUser
from treinamentos.models import Treinamentos
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

class Relatorios(models.Model):

    SALA = (
        ('CI', 'CI'),
        ('Sala [1]', 'Sala [1]'),
        ('Sala [2]', 'Sala [2]'),
    )
    STATUS = (
        ('Espera...', 'Espera...'),
        ('Aprovado', 'Aprovado'),
        ('Rejeitado', 'Rejeitado'),
    )

    treinamento = models.ForeignKey(Treinamentos, on_delete=models.CASCADE,related_name="treinamento", verbose_name=("Treinamento"), null=True)
    sala = models.CharField(choices=SALA, default='CI', max_length=50, null=True)
    responsavel = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="relatorios_responsavel", limit_choices_to={'groups__name': 'oficial'}, verbose_name=("Responsável pelo treinamento"), null=True)
    data1 = models.CharField(("Início"),max_length=50, null=True)
    treinador = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="relatorios_treinador", verbose_name=("Treinador"), null=True)
    aprovados = models.TextField(max_length=50, null=True)
    reprovados = models.TextField(max_length=50, null=True)
    data2 = models.CharField(("Fim"),max_length=50, null=True)
    observações = models.TextField(max_length=50, null=True)
    data_preenchimento = models.DateTimeField( blank=True)
    status = models.CharField(choices=STATUS,default='Espera...', max_length=50,blank=True, null=True)


    def __str__(self):
        return self.treinamento
