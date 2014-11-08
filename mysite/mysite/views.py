from django.http import HttpResponse
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
import datetime
import os.path


def hello(request):
    return HttpResponse("Hello world, Aadithya!! This is your first DJANGO application")

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def t_hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('hours_ahead.html')
    html = t.render(Context({'hours_ahead': dt,'hours_offset': offset}))
    return HttpResponse(html)