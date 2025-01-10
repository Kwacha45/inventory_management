import os
import sys

# Add the project directory to the Python path
sys.path.append(' C:/Users/mangw/PycharmProjects/pythonProject15/inventory_management')

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'inventory_management.settings'

# Import and set up the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
