from django.shortcuts import render
from datetime import date
# Create your views here.
data = {
    "movies": [
        {
            "title": "film-1",
            "description": "film description",
            "imageUrl":"m1.jpg",
            "slug":"film-adi-1",
            "language": "english",
            "date": date(2021,10,10)
        },
        {
            "title": "film-2",
            "description": "film description",
            "imageUrl":"m1.jpg",
            "slug":"film-adi-2",
            "language": "english",
            "date": date(2021,1,2)
        },
        {
            "title": "film-3",
            "description": "film description",
            "imageUrl":"m1.jpg",
            "slug":"film-adi-3",
            "language": "english",
            "date": date(2023,5,3)
        },
        {
            "title": "film-4",
            "description": "film description",
            "imageUrl":"m1.jpg",
            "slug":"film-adi-4",
            "language": "english",
            "date": date(2022,5,3)
        }
    ],
    "sliders":[]
}
def index(request):
    movies=data["movies"]
    return render(request, 'index.html',{
        "movies":movies
    })

def movies(request):
    return render(request, 'movies.html')

def movie_details(request, slug):
    return render(request, 'movie-details.html', {
        "slug": slug
    })