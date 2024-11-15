# Generated by Django 5.1.1 on 2024-10-29 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventoTipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventoTipo', models.CharField(choices=[('ensayo', 'Ensayo'), ('grabacion', 'Grabacion'), ('show', 'Show'), ('otro', 'Otro')], default='otro', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horarioLlegada', models.DateField(blank=True, null=True)),
                ('horarioPruebaSonido', models.DateField(blank=True, null=True)),
                ('horarioTocar', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=35)),
                ('ciudad', models.CharField(max_length=35)),
                ('direccion', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Vestimenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vestimenta', models.CharField(choices=[('formal', 'Formal'), ('informal', 'Informal'), ('disfraz', 'Disfraz'), ('libre', 'Libre')], default='libre', max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('dineroCobrar', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='evento.eventotipo')),
                ('horario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='evento.horario')),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='evento.localidad')),
                ('vestimenta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='evento.vestimenta')),
            ],
        ),
    ]
