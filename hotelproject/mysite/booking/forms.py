from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class BookingForm(forms.Form):
    check_in = forms.DateTimeField(label='Дата заезда',widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    check_out = forms.DateTimeField(label='Дата выезда',widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    adults = forms.IntegerField(label='Количество взрослых',widget=forms.NumberInput(attrs={"class": "form-control"}))
    children = forms.IntegerField(label='Количество детей',widget=forms.NumberInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Почта',widget=forms.EmailInput(attrs={"class": "form-control"}))
    category = forms.ModelChoiceField(empty_label='Выберите категорию',queryset=Category.objects.all(),label='Категории',widget=forms.Select(attrs={"class": "form-control"}))
    rooms = forms.ModelChoiceField(empty_label='Выберите номер', queryset=Rooms.objects.all(), label='Номера', widget=forms.Select(attrs={"class": "form-control"}))

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']