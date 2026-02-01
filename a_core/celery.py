import os
from celery import Celery

# Configurar Django settings para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

celery_app = Celery('a_core')

# Cargar config de Django settings (prefijo CELERY_)
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-descubrir tasks en todas las apps
celery_app.autodiscover_tasks()