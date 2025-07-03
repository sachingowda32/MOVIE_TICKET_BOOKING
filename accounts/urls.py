from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('home/', views.home_view, name='home'),
    path('identify/', views.identify_view, name='identify'),
    path('otp/<en_uname>/', views.otp_view, name='otp'),
    path('reset_password/<en_uname>/', views.reset_password_view, name='reset_password'),
    path('updatepassword/',views.updatepassword,name='updatepassword')
]