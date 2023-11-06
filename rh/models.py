from django.db import models
from users.models import CustomUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

class Requerimento(models.Model):
    OPCOES = (
        ('Promoção', 'Promoção'),
        ('Rebaixamento', 'Rebaixamento'),
        ('Demissão', 'Demissão'),
        ('Reserva', 'Reserva'),
    )

    STATUS = (
        ('Espera...', 'Espera...'),
        ('Aprovado', 'Aprovado'),
        ('Rejeitado', 'Rejeitado'),
    )

    opcoes = models.CharField(choices=OPCOES, max_length=50, null=True)
    solicitante = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'oficial'},related_name="requerimento_solicitante", verbose_name=("Solicitante"), null=True)
    data_preenchimento = models.DateTimeField(blank=True)
    militar = models.TextField(max_length=50, null=True)
    status = models.CharField(choices=STATUS,default='Espera...', max_length=50, null=True)



    def __str__(self):
        return self.opcoes
