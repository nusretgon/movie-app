from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("index.html", views.index),
    path("movies.html", views.movies),
    path("movies/<slug:slug>", views.movie_details)    
]

