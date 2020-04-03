from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

# These view is to test that everything has been configured appropriately


def index(request):
    return render(request, 'index.html', {})
