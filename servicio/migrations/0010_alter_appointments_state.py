# Generated by Django 4.2.3 on 2023-11-18 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0009_alter_appointments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='state',
            field=models.CharField(choices=[('CANCELAR', 'Cancelar'), ('PENDIENTE', 'Pendiente'), ('PROCESO', 'Proceso'), ('COMPLETADO', 'Completado')], max_length=10),
        ),
    ]