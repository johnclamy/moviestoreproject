from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def about_us(request):
    return render(request, 'home/about-us.html')
