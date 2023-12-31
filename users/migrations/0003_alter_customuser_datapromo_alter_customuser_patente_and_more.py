# Generated by Django 4.2.6 on 2023-10-31 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='datapromo',
            field=models.DateField(null=True, verbose_name='Última Promoção'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='patente',
            field=models.CharField(choices=[('Marinheiro', 'Marinheiro'), ('Cabo', 'Cabo'), ('Aluno', 'Aluno'), ('3° Sargento', '3° Sargento'), ('2° Sargento', '2° Sargento'), ('1° Sargento', '1° Sargento'), ('SubOficial', 'SubOficial'), ('Cadete', 'Cadete'), ('Aspirante-a-Oficial', 'Aspirante-a-Oficial'), ('Guarda-Marinha', 'Guarda-Marinha'), ('Segundo-Tenente', 'Segundo-Tenente'), ('Primeiro-Tenente', 'Primeiro-Tenente'), ('Capitão-Tenente', 'Capitão-Tenente'), ('Capitão-de-Corveta', 'Capitão-de-Corveta'), ('Capitão-de-Fragata', 'Capitão-de-Fragata'), ('Capitão-de-Mar-e-Guerra ⭐', 'Capitão-de-Mar-e-Guerra ⭐'), ('Contra-Almirante ⭐⭐', 'Contra-Almirante ⭐⭐'), ('Vice-Almirante ⭐⭐⭐', 'Vice-Almirante ⭐⭐⭐'), ('Almirante-de-Esquadra ⭐⭐⭐⭐', 'Almirante-de-Esquadra ⭐⭐⭐⭐'), ('Almirante ⭐⭐⭐⭐⭐', 'Almirante ⭐⭐⭐⭐⭐')], default='Marinheiro', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Demitido', 'Demitido'), ('Aposentado', 'Aposentado')], default='Ativo', max_length=50, null=True),
        ),
    ]
