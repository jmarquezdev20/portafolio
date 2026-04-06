"""
WSGI config for myportfolio project.
Punto de entrada para servidores WSGI (Gunicorn, uWSGI).
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')

application = get_wsgi_application()
