from django.shortcuts import render
from .models import Movie
from reviews.models import Review
from django.db.models import Avg
import datetime
# Create your views here.

def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    reviews = Review.objects.filter(movie=movie)
    rating = reviews.aggregate(avg=Avg('rating'))['avg']
    if rating is None:
        rating = 0
    if (rating - int(rating)) > 0:
        rating = '{:.1f}'.format(rating)
    else:
        rating = int(rating)
    context = {
        'movie': movie,
        'rating': rating,
        'reviews': reviews,
        'date' : datetime.date.today()

    }

    return render(request, 'movies/movie_detail.html', context)
