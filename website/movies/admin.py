from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']


admin.site.register(Movie, MovieAdmin)
