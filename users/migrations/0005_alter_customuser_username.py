# Generated by Django 4.2.6 on 2023-11-01 11:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(help_text='150 characters or fewer. Letters (uppercase and lowercase), digits, @, :, -, and _ only.', max_length=150, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Enter a valid username. This value may contain only letters (uppercase and lowercase), numbers, @, :, -, and _ characters.', regex='^[a-zA-Z0-9@_:.-]+$')], verbose_name='usuário'),
        ),
    ]