"""
Migración inicial - Crea las tablas Project y ContactMessage.
Generada automáticamente por Django migrations.
"""

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título del Proyecto')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('short_description', models.CharField(blank=True, help_text='Resumen breve para mostrar en la tarjeta del proyecto.', max_length=300, verbose_name='Descripción corta')),
                ('category', models.CharField(choices=[('backend', 'Backend'), ('fullstack', 'Full Stack'), ('api', 'API / REST'), ('database', 'Base de Datos'), ('automation', 'Automatización'), ('other', 'Otro')], default='backend', max_length=20, verbose_name='Categoría')),
                ('technologies', models.CharField(help_text='Separa las tecnologías con comas. Ej: Python, Django, PostgreSQL, Docker', max_length=500, verbose_name='Tecnologías')),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/', verbose_name='Imagen del Proyecto')),
                ('github_url', models.URLField(blank=True, verbose_name='URL de GitHub')),
                ('demo_url', models.URLField(blank=True, verbose_name='URL del Demo')),
                ('featured', models.BooleanField(default=False, verbose_name='Proyecto Destacado')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Orden')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['order', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(blank=True, max_length=200, verbose_name='Asunto')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('status', models.CharField(choices=[('new', 'Nuevo'), ('read', 'Leído'), ('replied', 'Respondido'), ('archived', 'Archivado')], default='new', max_length=20, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP del remitente')),
            ],
            options={
                'verbose_name': 'Mensaje de Contacto',
                'verbose_name_plural': 'Mensajes de Contacto',
                'ordering': ['-created_at'],
            },
        ),
    ]
