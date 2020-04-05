from django.shortcuts import render
import requests

# Create your views here.


def admin_page(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()

    context = {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    }
    return render(request, 'administrator/index.html', context)


def about(request):
    return render(request, 'administrator/about.html', {})
