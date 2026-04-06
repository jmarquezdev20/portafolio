"""
Configuración del Admin de Django para el portafolio.
Panel de administración profesional y funcional.
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import Project, ContactMessage, Education


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin para gestionar proyectos del portafolio."""

    # Columnas visibles en el listado
    list_display = [
        'title', 'category', 'featured', 'is_active',
        'order', 'image_preview', 'created_at'
    ]

    # Filtros laterales
    list_filter = ['category', 'featured', 'is_active', 'created_at']

    # Búsqueda
    search_fields = ['title', 'description', 'technologies']

    # Campos editables directamente en el listado
    list_editable = ['featured', 'is_active', 'order']

    # Ordenamiento por defecto
    ordering = ['order', '-featured', '-created_at']

    # Campos de solo lectura
    readonly_fields = ['created_at', 'updated_at', 'image_preview']

    # Organización del formulario de edición
    fieldsets = (
        ('📋 Información Principal', {
            'fields': ('title', 'short_description', 'description', 'category')
        }),
        ('🛠️ Tecnologías', {
            'fields': ('technologies',),
            'description': 'Separa las tecnologías con comas.'
        }),
        ('🖼️ Imagen', {
            'fields': ('image', 'image_preview'),
        }),
        ('🔗 Links', {
            'fields': ('github_url', 'demo_url'),
        }),
        ('⚙️ Control', {
            'fields': ('featured', 'is_active', 'order'),
        }),
        ('📅 Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def image_preview(self, obj):
        """Muestra una miniatura de la imagen del proyecto."""
        if obj.image:
            return format_html(
                '<img src="{}" style="width:80px; height:50px; '
                'object-fit:cover; border-radius:4px;" />',
                obj.image.url
            )
        return format_html('<span style="color:#888;">Sin imagen</span>')

    image_preview.short_description = 'Vista previa'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Admin para gestionar formación, cursos y certificaciones con PDF."""

    list_display  = ['title', 'type', 'institution', 'period', 'is_active', 'order', 'has_certificate']
    list_filter   = ['type', 'is_active']
    search_fields = ['title', 'institution', 'description']
    list_editable = ['is_active', 'order']
    ordering      = ['order', '-period']
    readonly_fields = ['certificate_preview']

    fieldsets = (
        ('📋 Información', {
            'fields': ('type', 'title', 'institution', 'period', 'description')
        }),
        ('🏷️ Etiquetas', {
            'fields': ('tags',),
            'description': 'Separa con comas. Ej: Python, Django, REST'
        }),
        ('📄 Certificado PDF', {
            'fields': ('certificate_pdf', 'certificate_preview'),
            'description': 'Sube el PDF del certificado. Aparecerá un botón "Ver certificado" en el portafolio.',
        }),
        ('⚙️ Control', {
            'fields': ('is_active', 'order'),
        }),
    )

    def has_certificate(self, obj):
        """Indica con ícono si tiene certificado PDF cargado."""
        if obj.certificate_pdf:
            return format_html(
                '<a href="{}" target="_blank" style="color:#00D4FF;font-size:0.85rem;">📄 Ver PDF</a>',
                obj.certificate_pdf.url
            )
        return format_html('<span style="color:#566A87;">—</span>')

    has_certificate.short_description = 'Certificado'

    def certificate_preview(self, obj):
        """Muestra enlace al PDF actual si existe."""
        if obj.certificate_pdf:
            return format_html(
                '<a href="{}" target="_blank" '
                'style="display:inline-flex;align-items:center;gap:6px;'
                'background:#0D1320;border:1px solid #1A2A42;color:#00D4FF;'
                'padding:6px 14px;border-radius:8px;font-size:0.85rem;text-decoration:none;">'
                '📄 Ver certificado actual</a>',
                obj.certificate_pdf.url
            )
        return format_html('<span style="color:#566A87;">Sin certificado cargado aún.</span>')

    certificate_preview.short_description = 'Vista previa del certificado'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin para gestionar mensajes de contacto."""

    list_display = [
        'name', 'email', 'subject_preview', 'status',
        'created_at', 'ip_address'
    ]
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['status']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at', 'ip_address']
    ordering = ['-created_at']

    fieldsets = (
        ('👤 Remitente', {
            'fields': ('name', 'email', 'ip_address')
        }),
        ('💬 Mensaje', {
            'fields': ('subject', 'message')
        }),
        ('📊 Estado', {
            'fields': ('status', 'created_at')
        }),
    )

    def subject_preview(self, obj):
        """Muestra asunto o primeras palabras del mensaje."""
        if obj.subject:
            return obj.subject[:50]
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message

    subject_preview.short_description = 'Asunto / Mensaje'

    def has_add_permission(self, request):
        """No permitir agregar mensajes manualmente desde el admin."""
        return False
