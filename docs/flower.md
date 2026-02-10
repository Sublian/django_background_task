# 🚀 Instalación Rápida (Django + Celery)

## 1. Requirements
pip install flower

## 2. Terminal 4 (Flower Dashboard)
celery -A a_core flower \
  --port=5555 \
  --host=localhost \
  --basic_auth=admin:password123

## → http://localhost:5555

---

# 📊 Dashboard Features

| Panel        | Qué Monitorea             | Útil Para            |
| ------------ | ------------------------- | -------------------- |
| Workers      | Estado workers activos    | Ver cuántos procesan |
| Tasks        | Tasks pendientes/fallidas | Debugging errores    |
| Task Details | Args, tiempo ejecución    | Performance analysis |
| Statistics   | Throughput, latency       | Capacidad sistema    |
| Revoke       | Cancelar tasks            | Control producción   |

Tags: celery flower monitoring devops dashboard