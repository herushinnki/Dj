"""
WSGI config for untitled project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import datetime

from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse,Http404

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled.settings")

application = get_wsgi_application()

def hello(request):
    return HttpResponse("Hello World")

def current_datatime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" %now
    return HttpResponse(html)

def hours_ahead(request,offest):
    try:
        offest=int(offest)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offest)
    html="<html><body>In %s hour(s),it will be %s.</body></html>"%(offest,dt)
    return HttpResponse(html)
