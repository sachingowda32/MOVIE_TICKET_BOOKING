from django.shortcuts import render
from .models import Movie, Cast
# Create your views here.

def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    context = {
        'movie': movie
    }
    return render(request, 'movies/movie_detail.html', context)