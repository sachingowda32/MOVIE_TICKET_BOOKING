from django.urls import path
from . import views
urlpatterns = [
    path('movie_list/', views.movie_list, name='movie_list'),
    path('movie_detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]