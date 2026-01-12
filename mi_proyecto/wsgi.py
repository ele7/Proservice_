import os
from django.core.wsgi import get_wsgi_application

# Aquí va el nombre de tu proyecto (el que contiene settings.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')

application = get_wsgi_application()
