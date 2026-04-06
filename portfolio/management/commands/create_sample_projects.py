"""
Comando de gestión Django: create_sample_projects
Crea proyectos de ejemplo para poblar el portafolio inicialmente.

Uso: python manage.py create_sample_projects
"""

from django.core.management.base import BaseCommand
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Crea proyectos de ejemplo para el portafolio'

    def handle(self, *args, **kwargs):
        sample_projects = [
            {
                'title': 'API REST de E-commerce con Django',
                'short_description': (
                    'Backend completo para plataforma de comercio electrónico con '
                    'autenticación JWT, gestión de inventario y pagos.'
                ),
                'description': (
                    'API RESTful completa para una plataforma de e-commerce construida '
                    'con Django REST Framework. Incluye autenticación JWT, manejo de '
                    'roles (admin/cliente), CRUD de productos con categorías, carrito de '
                    'compras, gestión de órdenes y sistema básico de pagos. '
                    'Documentada con Swagger/OpenAPI y con cobertura de tests al 85%.'
                ),
                'category': 'api',
                'technologies': 'Python, Django, DRF, PostgreSQL, JWT, Docker, Swagger',
                'github_url': 'https://github.com/tu-usuario/ecommerce-api',
                'demo_url': '',
                'featured': True,
                'order': 1,
            },
            {
                'title': 'Sistema de Gestión de Inventario',
                'short_description': (
                    'Aplicación web full-stack para gestión de inventario con '
                    'reportes, alertas de stock y panel de administración.'
                ),
                'description': (
                    'Sistema web completo para la gestión de inventario de pequeñas '
                    'y medianas empresas. Desarrollado con Django y Bootstrap. '
                    'Incluye módulos de proveedores, productos, entradas/salidas, '
                    'alertas de stock mínimo, reportes en PDF/Excel y dashboard '
                    'con métricas clave. Desplegado en Railway con PostgreSQL.'
                ),
                'category': 'fullstack',
                'technologies': 'Python, Django, PostgreSQL, Bootstrap, Chart.js, Pandas',
                'github_url': 'https://github.com/tu-usuario/inventario-system',
                'demo_url': 'https://inventario-demo.up.railway.app',
                'featured': True,
                'order': 2,
            },
            {
                'title': 'FastAPI Microservicio de Autenticación',
                'short_description': (
                    'Microservicio independiente de autenticación con OAuth2, '
                    'JWT y gestión de sesiones para arquitecturas distribuidas.'
                ),
                'description': (
                    'Microservicio de autenticación construido con FastAPI y SQLAlchemy. '
                    'Implementa OAuth2 con JWT tokens, refresh tokens, blacklist de tokens, '
                    'verificación de email, reset de contraseña y autenticación '
                    'de dos factores (2FA). Containerizado con Docker y documentado '
                    'automáticamente con Swagger UI.'
                ),
                'category': 'backend',
                'technologies': 'Python, FastAPI, SQLAlchemy, Redis, Docker, JWT, PostgreSQL',
                'github_url': 'https://github.com/tu-usuario/auth-microservice',
                'demo_url': '',
                'featured': False,
                'order': 3,
            },
            {
                'title': 'Dashboard Analítico con Django',
                'short_description': (
                    'Panel de análisis de datos con visualizaciones interactivas, '
                    'reportes automatizados y exportación a múltiples formatos.'
                ),
                'description': (
                    'Dashboard analítico para visualización de datos de negocio. '
                    'Integración con múltiples fuentes de datos (CSV, APIs externas, DB). '
                    'Gráficos interactivos con Chart.js, tablas dinámicas, '
                    'filtros avanzados y exportación a PDF/Excel. '
                    'Arquitectura limpia con separación de capas y uso de Celery '
                    'para tareas asíncronas de generación de reportes.'
                ),
                'category': 'fullstack',
                'technologies': 'Python, Django, Celery, Redis, Chart.js, Pandas, PostgreSQL',
                'github_url': 'https://github.com/tu-usuario/analytics-dashboard',
                'demo_url': '',
                'featured': False,
                'order': 4,
            },
        ]

        created_count = 0
        for project_data in sample_projects:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'  ✓ Proyecto creado: {project.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'  ~ Ya existe: {project.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Proceso completado: {created_count} proyectos nuevos creados.'
            )
        )
