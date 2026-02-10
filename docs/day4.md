# 📅 Day 4: Celery Beat - Tareas Programadas ✅

📺 Video 4: Newsletter con Celery Beat

⏱️ Duración: 28min | Status: COMPLETED | Issue #4

---

## 🎯 Qué Aprendí: Scheduled Tasks

Celery Beat = Cron jobs pero en Python → Tareas automáticas por horario.

```text
SIN Beat: programar manualmente
CON Beat: "newsletter cada domingo 9AM"
```

## 🚀 Setup Celery Beat 

```bash
# 1. Instalar
pip install django-celery-beat

# 2. Migrations (DB scheduling)
python manage.py migrate

# 3. Terminal 5 (Beat Scheduler)
celery -A a_core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## ⚙️ Config settings.py

```python
# a_core/settings.py
INSTALLED_APPS += ['django_celery_beat']

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_BEAT_SCHEDULE = {
    'newsletter-semanal': {
        'task': 'a_core.tasks.send_newsletter',
        'schedule': crontab(hour=9, minute=0, day_of_week=0),  # Domingo 9AM
    },
    'cleanup-tasks': {
        'task': 'a_core.tasks.cleanup_old_tasks',
        'schedule': timedelta(hours=1),  # Cada hora
    },
}
```

## 📧 Task Newsletter (Ejemplo Video)

```python
# a_core/tasks.py
from celery import shared_task
from django.core.mail import send_mass_mail

@shared_task
def send_newsletter():
    """Newsletter semanal a 500+ usuarios"""
    users = User.objects.filter(subscribed=True)
    messages = []
    
    for user in users:
        messages.append((
            f'Newsletter #{week_num}',
            f'Hola {user.first_name}, tu contenido semanal...',
            'noreply@clinic.com',
            [user.email]
        ))
    
    send_mass_mail(messages, fail_silently=False)
    print(f"✅ Newsletter enviada a {len(users)} usuarios")
```

## 🗄️ Django Admin UI (Magia)

```text
1. /admin/django_celery_beat/periodic task/
2. Crear: "newsletter-semanal"
3. Schedule: "Every Sunday 09:00"
4. SAVE → Beat lo detecta automáticamente
```

## ✅ Resultados Day 4

```text
🎉 Tareas programadas: DOMINGO 9AM newsletter
🎉 Admin UI: Schedule visual NO código
🎉 Flower: Confirma ejecución automática
🎉 5 terminals → Production-ready
```