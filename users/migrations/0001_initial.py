# Generated by Django 4.2.6 on 2023-10-31 23:40

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('patente', models.CharField(choices=[('Marinheiro', 'Marinheiro'), ('Cabo', 'Cabo'), ('Aluno', 'Aluno'), ('3° Sargento', '3° Sargento'), ('2° Sargento', '2° Sargento'), ('1° Sargento', '1° Sargento'), ('SubOficial', 'SubOficial'), ('Cadete', 'Cadete'), ('Aspirante-a-Oficial', 'Aspirante-a-Oficial'), ('Guarda-Marinha', 'Guarda-Marinha'), ('Segundo-Tenente', 'Segundo-Tenente'), ('Primeiro-Tenente', 'Primeiro-Tenente'), ('Capitão-Tenente', 'Capitão-Tenente'), ('Capitão-de-Corveta', 'Capitão-de-Corveta'), ('Capitão-de-Fragata', 'Capitão-de-Fragata'), ('Capitão-de-Mar-e-Guerra ⭐', 'Capitão-de-Mar-e-Guerra ⭐'), ('Contra-Almirante ⭐⭐', 'Contra-Almirante ⭐⭐'), ('Vice-Almirante ⭐⭐⭐', 'Vice-Almirante ⭐⭐⭐'), ('Almirante-de-Esquadra ⭐⭐⭐⭐', 'Almirante-de-Esquadra ⭐⭐⭐⭐'), ('Almirante ⭐⭐⭐⭐⭐', 'Almirante ⭐⭐⭐⭐⭐')], default='Marinheiro', max_length=50)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Demitido', 'Demitido'), ('Aposentado', 'Aposentado')], default='Ativo', max_length=50)),
                ('datapromo', models.DateField(verbose_name='Última Promoção')),
                ('responsavel', models.TextField(verbose_name='Responsável pela promoção')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
