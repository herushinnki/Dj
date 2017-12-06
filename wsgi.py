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
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled.settings")

application = get_wsgi_application()

def hello(request):
    return HttpResponse("Hello World")

def current_datatime(request):
    now=datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offest):
    try:
        offest=int(offest)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offest)
    html="<html><body>In %s hour(s),it will be %s.</body></html>"%(offest,dt)
    return HttpResponse(html)
