from django.shortcuts import render
# from Stakeholder_Dashboard.views import 

# Create your views here.

# These view is to test that everything has been configured appropriately


def index(request):
    return render(request, 'index.html', {})
