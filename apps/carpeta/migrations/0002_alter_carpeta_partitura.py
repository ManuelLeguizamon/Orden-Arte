# Generated by Django 5.1.1 on 2024-11-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpeta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpeta',
            name='partitura',
            field=models.FileField(blank=True, null=True, upload_to='partituras/'),
        ),
    ]
