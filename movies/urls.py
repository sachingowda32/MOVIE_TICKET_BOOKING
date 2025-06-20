from django.urls import path
from . import views
urlpatterns = [
    path('movie_detail/<slug>/', views.movie_detail, name='movie_detail'),
]