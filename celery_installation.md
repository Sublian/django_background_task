# Guía: Redis + Celery en Django (WSL Windows)
Instalación y configuración mínima para replicar en WSL Ubuntu. Tiempo total: 15min.

## Requisitos

- WSL2 Ubuntu instalado (24.04.1 LTS u otro)

- Proyecto Django clonado

- Terminal WSL abierta

## 1. Instalar Redis (WSL)

```
sudo apt update
sudo apt install redis-server -y
sudo service redis-server start
redis-cli ping  # → PONG
sudo systemctl enable redis-server  # Auto-inicio
```

## 2. Virtual Environment (WSL)

```
cd /ruta/a/tu/proyecto  # ej: /mnt/c/Users/.../django_background_task
sudo apt install python3.12-venv -y
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install django celery redis[lua]  # Si requirements falla
```

## 3. Configurar Celery (a_core app)

a_core/celery.py (crear archivo)

```python
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')
app = Celery('a_core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

a_core/__init__.py (agregar al final)

```python
from .celery import app as celery_app
__all__ = ('celery_app',)
a_core/settings.py (agregar al final)
```

```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Lima'
```

## 4. Levantar Stack (3 Terminales WSL)

### Terminal 1 (Redis):

```bash
sudo service redis-server start
redis-cli ping  # PONG
```

### Terminal 2 (Django):

```bash
source venv/bin/activate
python manage.py runserver
# → http://127.0.0.1:8000/
```

### Terminal 3 (Celery Worker):

```bash
source venv/bin/activate
celery -A a_core worker -l info
# → Connected to redis://localhost:6379/0 
```

## 5. VSCode Integración

```text
VSCode → Ctrl+Shift+P → "WSL: Reopen Folder in WSL"
Terminal VSCode auto-usa WSL ✅
```

### Troubleshooting

```text
❌ venv falla: sudo apt install python3.12-venv
❌ Celery "no celery attr": Verificar celery.py + __init__.py
❌ Redis no conecta: redis-cli ping en Terminal 1
```

### Docker Compose (Opcional - Prod)

```text
version: '3.8'
services:
  redis:
    image: redis:alpine
    ports: ["6379:6379"]
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes: [".:/app"]
    ports: ["8000:8000"]
    depends_on: [redis]
  celery:
    build: .
    command: celery -A a_core worker -l info
    volumes: [".:/app"]
    depends_on: [redis]
```

Ejecutar: docker-compose up --build
