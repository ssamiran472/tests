from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    return HttpResponse(now)
