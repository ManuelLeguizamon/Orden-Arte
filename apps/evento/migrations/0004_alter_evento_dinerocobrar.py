# Generated by Django 5.1.1 on 2024-11-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0003_evento_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='dineroCobrar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]