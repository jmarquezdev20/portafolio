#!/usr/bin/env bash
# build.sh — Render lo ejecuta automáticamente en cada deploy.
set -o errexit   # Detiene el script si cualquier comando falla

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate --no-input

# Crea un superusuario inicial solo si no existe
# (necesitas DJANGO_SUPERUSER_* en las env vars de Render)
python manage.py createsuperuser \
    --no-input \
    --username "${DJANGO_SUPERUSER_USERNAME:-admin}" \
    --email    "${DJANGO_SUPERUSER_EMAIL:-admin@example.com}" \
    2>/dev/null || echo "Superusuario ya existe, omitiendo."