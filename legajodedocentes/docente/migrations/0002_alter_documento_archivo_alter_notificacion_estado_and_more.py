# Generated by Django 5.1.7 on 2025-04-20 19:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='documentos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'doc', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='notificacion',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Enviado', 'Enviado'), ('Renovado', 'Renovado')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='tipodocumento',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
