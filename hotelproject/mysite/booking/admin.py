from django.contrib import admin

from .models import Rooms, Category,Booking

class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id','category','subtitle','title','price')
    list_display_links = ('id','title')
    search_fields = ('title','category')
    list_filter = ('category', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    search_fields = ('title',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','check_in','check_out','adults','children','email','rooms')
    list_display_links = ('id','check_in')
    search_fields = ('check_in','rooms')
    list_filter = ('rooms', )

admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Booking,BookingAdmin)

