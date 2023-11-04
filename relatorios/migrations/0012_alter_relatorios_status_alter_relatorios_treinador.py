# Generated by Django 4.2.6 on 2023-11-02 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('relatorios', '0011_alter_relatorios_status_alter_relatorios_treinador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorios',
            name='status',
            field=models.CharField(blank=True, choices=[('Espera...', 'Espera...'), ('Aprovado', 'Aprovado'), ('Rejeitado', 'Rejeitado')], default='Espera...', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='relatorios',
            name='treinador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatorios_treinador', to=settings.AUTH_USER_MODEL, verbose_name='Treinador'),
        ),
    ]
