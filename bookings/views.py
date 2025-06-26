from django.shortcuts import render,redirect
from theaters.models import Theater,showtime
from movies.models import Movie
from django.contrib import messages
import datetime
# Create your views here.
dates = [datetime.date.today(),datetime.date.today() + datetime.timedelta(days=1),datetime.date.today() + datetime.timedelta(days=2),datetime.date.today() + datetime.timedelta(days=3),datetime.date.today() + datetime.timedelta(days=4)]

def Theater_Showtime_view(request,slug,date_str=datetime.date.today()):
    if not Movie.objects.filter(slug=slug).exists():
        messages.error(request,'Movie not found')
        return redirect('movie_list')
    movie = Movie.objects.get(slug=slug)
    selected_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    theater_showtimes = [showtime.objects.filter(movie=movie,showtime__date=selected_date,
                                                 theater=theater).order_by('showtime') 
                                                 for theater in Theater.objects.all()
                                                 if showtime.objects.filter(movie=movie,showtime__date=selected_date,theater=theater).exists()]
    context = {
        'movie':movie,
        'theater_showtimes':theater_showtimes,
        'dates':dates,
        'slug':slug,
        'current_date' : selected_date,
        
    }
    return render(request,'theaters/theater_showtime.html',context)


    
