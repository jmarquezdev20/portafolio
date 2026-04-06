"""
Vistas del portafolio profesional.
Maneja toda la lógica de presentación usando Class-Based Views y Function-Based Views.
"""

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

from .models import Project, ContactMessage, Education
from .forms import ContactForm


class HomeView(TemplateView):
    """
    Vista principal del portafolio.
    Carga todos los datos necesarios para renderizar la página completa.
    """
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['projects'] = Project.objects.filter(
            is_active=True
        ).order_by('order', '-featured', '-created_at')

        context['featured_projects'] = Project.objects.filter(
            is_active=True, featured=True
        ).order_by('order')[:3]

        context['contact_form'] = ContactForm()

        context['skills'] = self._get_skills()

        # Formación desde la base de datos (administrable desde el admin)
        context['education'] = Education.objects.filter(
            is_active=True
        ).order_by('order', '-period')

        return context

    def _get_skills(self):
        """Retorna las habilidades organizadas por categoría."""
        return {
            'backend': [
                {'name': 'Python',    'level': 90, 'icon': '🐍'},
                {'name': 'Django',    'level': 88, 'icon': '🎯'},
                {'name': 'FastAPI',   'level': 80, 'icon': '⚡'},
                {'name': 'REST APIs', 'level': 85, 'icon': '🔗'},
            ],
            'database': [
                {'name': 'PostgreSQL', 'level': 82, 'icon': '🐘'},
                {'name': 'MySQL',      'level': 80, 'icon': '🗄️'},
                {'name': 'SQLite',     'level': 90, 'icon': '📦'},
            ],
            'tools': [
                {'name': 'Git & GitHub', 'level': 88, 'icon': '🔀'},
                {'name': 'Docker',       'level': 72, 'icon': '🐳'},
                {'name': 'Linux',        'level': 78, 'icon': '🐧'},
            ],
            'frontend': [
                {'name': 'HTML',       'level': 85, 'icon': '🌐'},
                {'name': 'CSS',        'level': 78, 'icon': '🎨'},
                {'name': 'JavaScript', 'level': 70, 'icon': '⚙️'},
            ],
        }


def contact_view(request):
    """
    Vista para manejar el envío del formulario de contacto.
    Guarda el mensaje en la base de datos y envía notificación por email.
    Soporta peticiones AJAX y tradicionales.
    """
    if request.method != 'POST':
        return redirect('portfolio:home')

    form = ContactForm(request.POST)

    if form.is_valid():
        contact = form.save(commit=False)

        # Capturar IP del visitante (compatible con proxies como Render/Nginx)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        contact.ip_address = (
            x_forwarded_for.split(',')[0].strip()
            if x_forwarded_for
            else request.META.get('REMOTE_ADDR')
        )
        contact.save()

        # Notificación por email (falla silenciosamente si no está configurado)
        try:
            send_mail(
                subject=f'[Portfolio] Nuevo mensaje de {contact.name}',
                message=(
                    f'Nombre: {contact.name}\n'
                    f'Email: {contact.email}\n'
                    f'Asunto: {contact.subject or "Sin asunto"}\n\n'
                    f'Mensaje:\n{contact.message}'
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER or 'tu@email.com'],
                fail_silently=True,
            )
        except Exception:
            pass

        success_msg = '¡Mensaje enviado! Me pondré en contacto pronto.'

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': success_msg})

        messages.success(request, success_msg)
        return redirect('portfolio:home')

    # Formulario inválido
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': False,
            'errors': form.errors,
            'message': 'Por favor corrige los errores en el formulario.'
        }, status=400)

    messages.error(request, 'Hubo un error. Por favor verifica los datos.')
    return redirect('portfolio:home')