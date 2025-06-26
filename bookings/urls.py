from django.urls import path
from . import views
urlpatterns = [
    path('showtime/<slug>/<date_str>/',views.Theater_Showtime_view,name='theater_showtime'),

]