from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.detail, name='movies.detail'),
]

