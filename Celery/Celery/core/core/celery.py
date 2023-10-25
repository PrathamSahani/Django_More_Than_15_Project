# Import necessary modules
import os
from celery import Celery

# Set the Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Create a Celery instance
app = Celery('core')

# Configure Celery from Django settings with the 'CELERY' namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover and register tasks from all installed apps
app.autodiscover_tasks()

# Define a sample Celery task
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
