from django.urls import path
from . import views
urlpatterns = [
    path('showtime/<slug>/<date_str>/',views.Theater_Showtime_view,name='theater_showtime'),
    path('Seat_Selection_view/<int:show_id>/',views.Seat_Selection_view,name='Seats'),
    path('seatbooking/<int:show_id>/',views.Book_Ticket_View,name='seatbooking'),

]