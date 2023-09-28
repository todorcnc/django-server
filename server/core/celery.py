# The __future__ module enables features that are not available in the current version of Python 
# but will be available in future versions. In this case, the `absolute_import` ensures 
# that you get the new behavior for absolute imports (avoiding implicit relative imports), 
# and `unicode_literals` makes all string literals in the module unicode by default (useful for Python 2.x compatibility).
from __future__ import absolute_import, unicode_literals

# The os module provides a portable way of using operating system-dependent functionality like reading or 
# writing to the environment.
import os

# Import the Celery library. Celery is a distributed task queue that allows you to run tasks asynchronously.
from celery import Celery

# This sets the default setting module for Django. If the DJANGO_SETTINGS_MODULE environment variable is not 
# already set, it will default to 'core.settings'. This tells Django where to find its configuration.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Create a new instance of the Celery app and name it "core". 
# This initializes the Celery application and allows it to connect with your Django project.
app = Celery("core")

# Configure the Celery instance using the settings from Django's settings. 
# The namespace='CELERY' means that all celery-related configuration keys should be 
# prefixed with 'CELERY_' in the Django settings.
app.config_from_object("django.conf:settings", namespace="CELERY") 

# This tells Celery to auto-discover tasks in all of your INSTALLED_APPS, 
# so you can simply add tasks in your Django apps and they will be picked up by Celery without any extra configuration.
app.autodiscover_tasks()
