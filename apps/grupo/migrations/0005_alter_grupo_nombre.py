# Generated by Django 5.1.1 on 2024-11-09 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupo', '0004_remove_grupo_usuarios_grupo_userdueño'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]