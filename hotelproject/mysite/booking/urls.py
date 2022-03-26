from django.urls import path
from .views import *
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from xml.etree.ElementInclude import include
urlpatterns = [
    path('', views.index, name="home"),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('add_booking/', add_booking, name='add_booking'),
    path('logout/', logoutUser, name='logout'),
    path('rooms/', views.room, name='rooms'),

    ]
