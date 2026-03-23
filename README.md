
![Django Celery - Background Tasks](static/images/celery_python.png?raw=true)

# Django Background Tasks con Celery

![CI](https://github.com/Sublian/django_background_task/workflows/Django%20CI%20Tests/badge.svg)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0%2B-green)](https://www.djangoproject.com/)
[![Celery](https://img.shields.io/badge/Celery-5.4%2B-orange)](https://docs.celeryq.dev/)
[![Coverage](https://codecov.io/gh/Sublian/django_background_task/branch/main/graph/badge.svg)](https://codecov.io/gh/Sublian/django_background_task)
[![CI](https://github.com/Sublian/django_background_task/actions/workflows/ci.yml/badge.svg)](https://github.com/Sublian/django_background_task/actions/workflows/ci.yml)

Este proyecto es un **fork educativo** basado en la excelente serie de videos de **Andreas Jud**: [*Background Tasks with Celery for Django*](https://youtube.com/playlist?list=PL5E1F5cTSTtRHN1WynTlFmr9ozlfZEUNI&si=EAtzgP95NYI-Fkb1) (5 videos prácticos).

## 🚀 Inspiración y Progreso
- **Origen**: Andreas Jud enseña integración de Celery + Redis en Django para tareas asíncronas (emails, newsletters, etc.). Repo original de referencia: [andyjud/celery](https://github.com/andyjud/celery).
- **Mi implementación**:
  - ✅ **Video 1**: Envío de notificaciones por correo como tareas en background (usando Celery workers).
  - ⏳ **Próximos**: Configuración de Redis, Celery Beat para newsletters programadas, monitoreo con Flower, y más.
- **Objetivo**: Usar como base para aprender, luego **modificar/customizar** (e.g., integrar PostgreSQL, Docker, async views, WhatsApp notifications via APIs).

## 📁 Estructura del Proyecto


```
django_background_task/
├── a_core/ # Lógica central (Celery config)
├── a_home/ # App principal
├── a_messageboard/ # Manejo de mensajes/notificaciones
├── a_users/ # Gestión de usuarios
├── static/ # Archivos estáticos
├── templates/ # Templates Django
├── manage.py
├── requirements.txt # Incluye celery, redis, django
└── README.md
```


## 🛠️ Instalación Rápida (Local + Docker recomendado)
1. Clona: `git clone https://github.com/Sublian/django_background_task.git`
2. Instala: `pip install -r requirements.txt`
3. Configura Redis (broker): Docker `docker run -p 6379:6379 redis`
4. Migra DB: `python manage.py migrate`
5. Worker: `celery -A a_core worker -l info`
6. Beat (scheduler): `celery -A a_core beat -l info`
7. Servidor: `python manage.py runserver`

**Demo**: Envía email async desde `/home/send-notification/`.

## 🎯 Próximas Modificaciones
- Integrar PostgreSQL con queries optimizadas.
- Automatización WhatsApp via Twilio/Wolfram.
- Monitoreo con Flower + profiling (cProfile).
- Deploy en PythonAnywhere/Docker.

¡Contribuciones bienvenidas! Este repo es mi portafolio para roles backend Python/Django en Lima, PE.

**Autor**: [Luis Gonzalez/[LinkedIn](https://www.linkedin.com/in/luisangelgp)] | Basado en [Andreas Jud](https://www.youtube.com/@AndreasJud).
