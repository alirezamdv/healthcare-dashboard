release: python manage.py migrate
worker: python manage.py process_tasks
web: gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker

