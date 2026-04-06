# 🚀 Portfolio — Juan Manuel Márquez Jiménez

> Backend Developer · Django · Python · REST APIs

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)](https://djangoproject.com)
[![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render)](https://render.com)

Portafolio profesional desarrollado con Django. Permite gestionar proyectos, formación y mensajes de contacto completamente desde el panel de administración.

**🌐 Demo en vivo:** [tu-portfolio.onrender.com](https://tu-portfolio.onrender.com) ← actualiza este enlace

---

## ✨ Características

- **Panel Admin completo** — gestiona proyectos, educación y mensajes sin tocar código
- **Formulario de contacto** — guarda mensajes en DB + notificación por email
- **Deploy listo para Render** — `render.yaml`, `build.sh` y settings de producción incluidos
- **Archivos estáticos** con WhiteNoise (sin necesidad de S3)
- **Media con Cloudinary** (opcional, configurable por env vars)
- **Seguridad en producción** — HTTPS forzado, HSTS, cookies seguras

---

## 🛠️ Stack

| Capa | Tecnología |
|------|-----------|
| Backend | Python 3.11 · Django 4.2 |
| Base de datos | PostgreSQL (prod) · SQLite (dev) |
| Archivos estáticos | WhiteNoise |
| Media | Cloudinary |
| Deploy | Render |
| Email | Gmail SMTP / Console (dev) |

---

## ⚡ Instalación local

```bash
# 1. Clonar el repositorio
git clone https://github.com/jmarquezdev20/django-portfolio.git
cd django-portfolio

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Variables de entorno
cp .env.example .env
# Edita .env con tus datos

# 5. Migraciones y datos iniciales
python manage.py migrate
python manage.py createsuperuser

# 6. Ejecutar
python manage.py runserver
```

Abre [http://localhost:8000](http://localhost:8000) y el admin en [http://localhost:8000/admin](http://localhost:8000/admin).

---

## 🚀 Deploy en Render

### Opción A — Automático con render.yaml (recomendado)

1. Haz fork/push de este repo a GitHub
2. En [render.com](https://render.com) → **New** → **Blueprint**
3. Conecta el repositorio — Render lee el `render.yaml` y crea todo automáticamente
4. Agrega las variables de entorno opcionales (Cloudinary, Email) en el dashboard

### Opción B — Manual

| Campo | Valor |
|-------|-------|
| Runtime | Python |
| Build Command | `./build.sh` |
| Start Command | `gunicorn myportfolio.wsgi:application --bind 0.0.0.0:$PORT --workers 2` |

**Variables de entorno mínimas:**

```
DJANGO_SECRET_KEY=<genera una clave segura>
DEBUG=False
DATABASE_URL=<Render lo pone automáticamente con el add-on PostgreSQL>
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=tu@email.com
DJANGO_SUPERUSER_PASSWORD=<contraseña segura>
```

---

## 📁 Estructura del proyecto

```
django_portfolio/
├── myportfolio/          # Configuración principal
│   ├── settings.py       # Dev + prod con env vars
│   ├── urls.py
│   └── wsgi.py
├── portfolio/            # App principal
│   ├── models.py         # Project, Education, ContactMessage
│   ├── views.py          # HomeView (CBV) + contact_view (FBV)
│   ├── forms.py          # ContactForm con validación
│   ├── admin.py          # Panel admin personalizado
│   ├── context_processors.py
│   ├── static/
│   └── templates/
├── build.sh              # Script de deploy para Render
├── render.yaml           # Infraestructura como código
├── requirements.txt
└── .env.example
```

---

## 📄 Licencia

MIT — úsalo libremente como base para tu propio portafolio.