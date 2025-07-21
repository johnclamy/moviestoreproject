from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home.index'),
    path('about-us', views.about_us, name='home.about_us'),
]

