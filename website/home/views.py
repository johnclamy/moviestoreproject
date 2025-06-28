from django.shortcuts import render


def index(request):
    data = {}
    data['title'] = 'Welcome to PUPS-R-US | Home page'

    return render(request, 'home/index.html', { 'data': data })


def about(request):
    return render(request, 'home/about.html')
