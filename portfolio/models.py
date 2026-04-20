"""
Modelos del portafolio profesional.
Define la estructura de datos para proyectos y mensajes de contacto.
"""

from django.db import models
from django.utils import timezone
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('fullstack', 'Full Stack'),
        ('api', 'API / REST'),
        ('database', 'Base de Datos'),
        ('automation', 'Automatización'),
        ('other', 'Otro'),
    ]

    title = models.CharField(max_length=200, verbose_name='Título del Proyecto')
    description = models.TextField(
        verbose_name='Descripción',
        help_text='Descripción detallada del proyecto, tecnologías usadas y desafíos resueltos.'
    )
    short_description = models.CharField(
        max_length=300,
        verbose_name='Descripción corta',
        help_text='Resumen breve para mostrar en la tarjeta del proyecto.',
        blank=True
    )
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='backend', verbose_name='Categoría'
    )
    technologies = models.CharField(
        max_length=500,
        verbose_name='Tecnologías',
        help_text='Separa las tecnologías con comas. Ej: Python, Django, PostgreSQL, Docker'
    )
    image = models.ImageField(
        upload_to='projects/',
        blank=True, null=True,
        verbose_name='Imagen del Proyecto',
        help_text='Captura de pantalla o imagen representativa del proyecto.'
    )
    github_url = models.URLField(blank=True, verbose_name='URL de GitHub')
    demo_url = models.URLField(blank=True, verbose_name='URL del Demo')
    featured = models.BooleanField(default=False, verbose_name='Proyecto Destacado')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    order = models.PositiveIntegerField(default=0, verbose_name='Orden')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['order', '-featured', '-created_at']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


class Education(models.Model):
    TYPE_CHOICES = [
        ('education', '🎓 Educación'),
        ('course',    '📚 Curso'),
        ('cert',      '🏆 Certificación'),
        ('experience','💼 Experiencia'),
    ]

    type        = models.CharField(max_length=20, choices=TYPE_CHOICES, default='course', verbose_name='Tipo')
    title       = models.CharField(max_length=200, verbose_name='Título')
    institution = models.CharField(max_length=200, verbose_name='Institución / Plataforma')
    period      = models.CharField(max_length=50, verbose_name='Período')
    description = models.TextField(verbose_name='Descripción', blank=True)
    tags        = models.CharField(max_length=300, blank=True, verbose_name='Etiquetas')

    # ← FIX: RawMediaCloudinaryStorage sube como /raw/upload/ (público) en vez de /image/upload/ (privado)
    certificate_pdf = models.FileField(
        upload_to='certificates/',
        blank=True, null=True,
        verbose_name='Certificado PDF',
        help_text='Sube el PDF del certificado o diploma.',
        storage=RawMediaCloudinaryStorage()
    )

    is_active = models.BooleanField(default=True, verbose_name='Activo')
    order     = models.PositiveIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name        = 'Formación / Experiencia'
        verbose_name_plural = 'Formación y Experiencia'
        ordering            = ['order', '-period']

    def __str__(self):
        return f'{self.title} — {self.institution}'

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def get_type_icon(self):
        icons = {'education': '🎓', 'course': '📚', 'cert': '🏆', 'experience': '💼'}
        return icons.get(self.type, '📌')


class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nuevo'),
        ('read', 'Leído'),
        ('replied', 'Respondido'),
        ('archived', 'Archivado'),
    ]

    name       = models.CharField(max_length=150, verbose_name='Nombre')
    email      = models.EmailField(verbose_name='Email')
    subject    = models.CharField(max_length=200, verbose_name='Asunto', blank=True)
    message    = models.TextField(verbose_name='Mensaje')
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name='IP del remitente')

    class Meta:
        verbose_name = 'Mensaje de Contacto'
        verbose_name_plural = 'Mensajes de Contacto'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email} ({self.created_at.strftime('%d/%m/%Y')})"