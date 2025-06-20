from django.shortcuts import render
from movies.models import Movie
# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'dashboard/home.html', context)