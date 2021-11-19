#!/home/c/cj28902/public_html/venv/bin/python3.6
import os
import sys
 
sys.path.append('/home/c/cj28902/public_html')
sys.path.append('/home/c/cj28902/public_html/venv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'connect4pro.settings'
import django
django.setup()
 
from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
