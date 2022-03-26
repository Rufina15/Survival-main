from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import redirect
from .models import Rooms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import redirect
from .models import Rooms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Category
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    booking = Rooms.objects.all()
    return render(request, 'booking/index.html', {'menu':booking})

def register(request):
    form=CreateUserForm()

    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'booking/register.html', {"form": form })

def user_login(request):
    if request.method == "POST":
       username= request.POST.get('username')
       password =request.POST.get('password')

       user=authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           return redirect('home')
       else:
           messages.info(request, 'Username OR password is incorrect')

    #
    #     form = AuthenticationForm(request.POST)
    #     if form.is_valid():
    #         user=form.get_user()
    #         login(request, user)
    #
    #
    # else:
    #     form=AuthenticationForm()
    #
    context={}
    return render(request, 'booking/login.html', context)
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')




def add_booking(request):
    if request.method == 'POST':
       form = BookingForm(request.POST)
       if form.is_valid():
           Booking.objects.create(**form.cleaned_data)
           redirect('home')

    else:
        form = BookingForm()
    return render(request, 'booking/add_booking.html/', {'form': form})

def room(request):
    context = {}

    return render(request, 'booking/rooms.html', context)