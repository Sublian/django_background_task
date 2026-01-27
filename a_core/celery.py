import os
from celery import Celery

# Configurar Django settings para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

app = Celery('a_core')

# Cargar config de Django settings (prefijo CELERY_)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-descubrir tasks en todas las apps
app.autodiscover_tasks()
