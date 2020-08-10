from __future__ import absolute_import, unicode_literals
from django.conf import settings
import os
from celery import Celery
import celery.signals

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'convin.settings')

app = Celery('convin')
# print(app)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@celery.signals.setup_logging.connect
def on_celery_setup_logging(**kwargs):
	pass
