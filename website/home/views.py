from django.shortcuts import render


def index(request):
    template_data = {}
    template_data['title'] = 'Welcome to Webfix | Home page'

    return render(
        request,
        'home/index.html',
        {
            'template_data': template_data
        }
    )


def about(request):
    template_data = {}
    template_data['title'] = 'Find out about us | About page'

    return render(
        request,
        'home/about.html',
        {
            'template_data': template_data
        }
    )
