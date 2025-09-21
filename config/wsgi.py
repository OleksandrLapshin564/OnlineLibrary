"""
WSGI config for OnlineLibrary project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

# Telling Django where to look for settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Creating a WSGI application
application = get_wsgi_application()
