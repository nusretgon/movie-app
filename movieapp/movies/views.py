from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    pass
def movies(request):
    pass
def movie_details(request,slug):
    return HttpResponse("movie_details:"+slug)
