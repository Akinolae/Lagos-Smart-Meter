from django.shortcuts import render

# Create your views here.


def stakeholder(request):
    return render(request, 'stakeholder/index.html', {})
