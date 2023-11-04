from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from django.utils import timezone


class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    PATENTES = (
        ('Marinheiro', 'Marinheiro'),
        ('Cabo', 'Cabo'),
        ('Aluno', 'Aluno'),
        ('3° Sargento', '3° Sargento'),
        ('2° Sargento', '2° Sargento'),
        ('1° Sargento', '1° Sargento'),
        ('SubOficial', 'SubOficial'),
        ('Cadete', 'Cadete'),
        ('Aspirante-a-Oficial', 'Aspirante-a-Oficial'),
        ('Guarda-Marinha', 'Guarda-Marinha'),
        ('Segundo-Tenente', 'Segundo-Tenente'),
        ('Primeiro-Tenente', 'Primeiro-Tenente'),
        ('Capitão-Tenente', 'Capitão-Tenente'),
        ('Capitão-de-Corveta', 'Capitão-de-Corveta'),
        ('Capitão-de-Fragata', 'Capitão-de-Fragata'),
        ('Capitão-de-Mar-e-Guerra ⭐', 'Capitão-de-Mar-e-Guerra ⭐'),
        ('Contra-Almirante ⭐⭐', 'Contra-Almirante ⭐⭐'),
        ('Vice-Almirante ⭐⭐⭐', 'Vice-Almirante ⭐⭐⭐'),
        ('Almirante-de-Esquadra ⭐⭐⭐⭐', 'Almirante-de-Esquadra ⭐⭐⭐⭐'),
        ('Almirante ⭐⭐⭐⭐⭐', 'Almirante ⭐⭐⭐⭐⭐'),
        ('Conselheiro', 'Conselheiro'),
    )
    STATUS = (
        ('Ativo','Ativo'),
        ('Demitido','Demitido'),
        ('Aposentado','Aposentado'),
    )
    patente = models.CharField(choices=PATENTES,max_length=50, null=True)
    status = models.CharField(choices=STATUS, max_length=50, null=True)
    datapromo = models.DateField(("Última Promoção"),default=timezone.now, null=True)
    responsavel = models.TextField(("Responsável pela promoção"), null=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[a-zA-Z0-9@_:.,-]+$',
            message=_('Enter a valid username. This value may contain only letters (uppercase and lowercase), numbers, @, :, -, and _ characters.'),
            code='invalid_username',
        )],
        help_text=_('150 characters or fewer. Letters (uppercase and lowercase), digits, @, :, -, and _ only.'),
    )

    def __str__(self):
        return f"{self.username} ({self.patente})"