from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,IdentityForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from .utils import generate_otp, encode_uname, decode_uname
from django.utils import timezone
from datetime import timedelta

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name') 
            email = form.cleaned_data.get('email')
            send_mail(
                'registration successful',
                f'Hi {fname} {lname},\n\nThank you for registering with us! We are excited to have you on board.\n\nBest regards,\nMovie Ticket Booking Team',
                'sachingowda741517@gmail.com',
                [email],
                fail_silently=False,

            )
            return redirect('login')
            #return HttpResponse('Registration successful! A confirmation email has been sent to your email address.')
    form = RegisterForm()
    context = {
        'form': form
    }   
    return render(request, 'accounts/register.html', context) 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_authenticated:
                    login(request, user)
                    messages.success(request, 'Login successful!')
                    return redirect('home')
        return HttpResponse('Invalid credentials')
    
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)  
@login_required
def logout_view(request):
    logout(request)
    messages.error(request, 'You have been logged out successfully.')
    return redirect('login')  # Redirect to the login page after logout  

def home_view(request):
    return render(request, 'accounts/home.html')

def identify_view(request):
    if request.method == 'POST':
        form = IdentityForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                otp = generate_otp()
                time = timezone.now() + timedelta(minutes=5)
                user.otp_expiry = time
                user.otp = otp
                email = user.email
                user.save()
                send_mail(
                    'OTP for Movie Ticket Booking',
                    f'Your OTP is {otp}. It is valid for 5 minutes.',
                    'sachingowda741517@gmail.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request,'User found otp has sent to registered email')
                en_uname = encode_uname(user.username)
                url = f'/accounts/otp/{en_uname}/'
                return redirect(url)
            messages.error(request, 'User not found')
    
    form = IdentityForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/identify.html', context)

def otp_view(request,en_uname):
    username = decode_uname(en_uname)
    if User.objects.filter(username=username).exists():
        if request.method == 'POST':
            otp = int(request.POST.get('otp'))
            user = User.objects.get(username=username)
            user.otp_verified = False
            if timezone.now() <= user.otp_expiry:
                if not user.otp_verified:
                    if otp == user.otp:
                        user.otp_verified = True
                        user.save()
                        messages.success(request, 'OTP verified successfully!')
                        url = f'/accounts/reset_password/{en_uname}/'
                        return redirect(url)
                    
                    messages.error(request, 'Invalid OTP. Please try again.')
                    return redirect(url)
                messages.error(request, 'OTP already verified.')
                return redirect('otp', en_uname=en_uname) 
            messages.error(request, 'OTP expired. Please request a new OTP.')
            return redirect('identify')
        return render(request, 'accounts/otp.html')
    messages.error(request, 'Invalid Request')
    return redirect('login')

def reset_password_view(request, en_uname):
    dec_name = decode_uname(en_uname)
    user = User.objects.get(username=dec_name)
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            user.otp_verified = False
            user.otp = None
            user.otp_expiry = None
            user.save()
            messages.success(request, 'Password reset successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Error resetting password. Please try again.')
    form = SetPasswordForm(user)
    context = {
        'form': form
    }
    return render(request, 'accounts/reset_password.html', context)
