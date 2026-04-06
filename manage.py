#!/usr/bin/env python
"""
Utilidad de línea de comandos de Django para tareas administrativas.
"""
import os
import sys


def main():
    """Punto de entrada principal para comandos de gestión."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y activado en el entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
