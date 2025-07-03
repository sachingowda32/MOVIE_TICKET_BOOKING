from django.shortcuts import render,redirect
from movies.models import Movie
from django.contrib import messages
from bookings.models import Booking,BookingSeat,Seat
from payments.models import Payment
from theaters.models import showtime
# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'dashboard/home.html', context)

def movie_search(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        try:
            movie = Movie.objects.get(title__iexact=title)
            context = {'movie': movie}
            return render(request, 'movies/search_movie.html', context)
        except Movie.DoesNotExist:
            messages.error(request, 'Movie not found')
            return redirect('movie_list')
        
'''def Booking_History_View(request):
    payments = Payment.objects.filter(booking__user=request.user)
    seats_list = []
    for payment in payments:
        seats = BookingSeat.objects.filter(showtime = payment.booking.showtime,booking=payment.booking)
        seats_list.append(seats)
    
    context = {
        'payments' : payments,
        'seats' : seats,
    }
    return render(request,'bookings/booking_history.html',context)'''

def Booking_History_View(request):
    bookings = Booking.objects.filter(user=request.user, status='booked').order_by('-booking_time')

    all_ticket_data = []

    for booking in bookings:
        payment = Payment.objects.filter(booking=booking).first()
        seats = Seat.objects.filter(bookingseat__booking=booking)
        seat_numbers = [str(seat) for seat in seats]
        showtime = booking.showtime
        movie = showtime.movie
        theater = showtime.theater

        ticket = {
            'booking': booking,
            'payment': payment,
            'seats': seat_numbers,
            'showtime': showtime.showtime,
            'movie': movie,
            'theater': theater,
        }

        all_ticket_data.append(ticket)

    context = {
        'tickets': all_ticket_data,
    }

    return render(request, 'bookings/booking_history.html', context)


        