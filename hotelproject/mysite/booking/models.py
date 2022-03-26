from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rooms(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    subtitle = models.CharField(max_length=100)
    price = models.IntegerField(null=False, verbose_name='Ценевой сегмент')
    count = models.IntegerField()
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,blank = True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Booking(models.Model):
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(auto_now_add=True)
    adults = models.IntegerField(null=False)
    children = models.IntegerField(null=False)
    email = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    rooms = models.ForeignKey(Rooms, on_delete=models.SET_NULL, null=True, blank=True)





