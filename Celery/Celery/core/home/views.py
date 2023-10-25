from django.shortcuts import render
from django.http import HttpResponse
import time
from .tasks import *

# Create your views here.


def home(request):
    # time.sleep(10)
    handle_sleep.delay()
    return HttpResponse("Hello from celey!")
    