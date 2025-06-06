from django.shortcuts import render
from .models import Movie


def index(request):
    template_data = {}
    template_data['title'] = 'All available movies at Webflix'
    search_term = request.GET.get('search')

    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()
    
    template_data['movies'] = movies

    return render(
        request,
        'movies/index.html',
        {
            'template_data': template_data
        }
    )


def detail(request, id):
    template_data = {}
    movie = Movie.objects.get(id=id)

    template_data['title'] = movie.name
    template_data['movie'] = movie

    return render(
        request,
        'movies/detail.html',
        {
            'template_data': template_data
        }
    )
    