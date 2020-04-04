from django.shortcuts import render

# Create your views here.


def subscriber_page(request):
    return render(request, 'subscribers/subscribers.html', {})
