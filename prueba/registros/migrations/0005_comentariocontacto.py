# Generated by Django 5.0.6 on 2025-07-01 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_alter_comentario_options_alter_comentario_coment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioContacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave ')),
                ('usuario', models.TextField(verbose_name='Usuario')),
                ('mensaje', models.TextField(verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
            ],
            options={
                'verbose_name': ' Comentario Contacto',
                'verbose_name_plural': 'Comentarios Contactos',
                'ordering': ['-created'],
            },
        ),
    ]
