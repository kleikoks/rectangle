from .models import Book
from core.celery import app
from celery.signals import worker_ready
from celery.schedules import crontab

# @app.on_after_finalize.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(10, do_it.s())

@app.task()
def do_it():
    print('do_it')
    return 'do_it'

# @worker_ready.connect()
# def initial_do_it(sender='core', **kwargs):
#     Book.objects.create(name='celery', price=33)
#     print('initial_do_it')
# celery -A core worker -l info
# celery -A core beat -l info